"""
CAOS-A1 — Anchor Reinforcement Engine (ARE)
v0.1 — durable, inspectable, deterministic

Principle:
- ARE observes anchor usage events (write/recall/promote/suppress).
- It maintains durable stats per anchor, per lane, per profile.
- It emits weights (reinforcement_score) and receipts.
- Correlator consumes weights; correlator does NOT decide importance.

No embeddings. No heuristics. Just math + receipts.
"""

from __future__ import annotations

import os
import sqlite3
import time
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any


# ----------------------------
# CONFIG (tunable but explicit)
# ----------------------------

@dataclass(frozen=True)
class AREConfig:
    # Smoothing / decay settings
    recent_window_seconds: int = 7 * 24 * 3600        # 7 days window
    half_life_seconds: int = 3 * 24 * 3600            # 3 days half-life for recency
    # Weight coefficients
    alpha_recent: float = 1.00
    beta_total: float = 0.05
    gamma_consistency: float = 0.75
    gamma_lane_affinity: float = 0.50
    # Caps / floors
    min_weight: float = 0.01
    max_weight: float = 1.00


# ----------------------------
# EVENT MODEL
# ----------------------------

@dataclass(frozen=True)
class AREEvent:
    ts_ms: int
    op: str                       # "write" | "recall" | "promote" | "suppress"
    profile_id: str
    lane_id: str
    session_id: str
    anchors: List[str]
    # Optional: freeform metadata for auditing only (not used in scoring)
    meta: Optional[Dict[str, Any]] = None


# ----------------------------
# RECEIPT MODEL
# ----------------------------

@dataclass(frozen=True)
class AREReceipt:
    request_id: str
    ts_ms: int
    op: str
    profile_id: str
    lane_id: str
    session_id: str
    anchors_updated: int
    weights_emitted: Dict[str, float]
    elapsed_ms: int


# ----------------------------
# STORAGE (SQLite — simple + durable)
# ----------------------------

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS are_anchor_stats (
  anchor TEXT NOT NULL,
  profile_id TEXT NOT NULL,
  lane_id TEXT NOT NULL,
  total_count INTEGER NOT NULL DEFAULT 0,
  recent_count INTEGER NOT NULL DEFAULT 0,
  last_seen_ts_ms INTEGER NOT NULL DEFAULT 0,
  last_window_reset_ts_ms INTEGER NOT NULL DEFAULT 0,
  consistency_score REAL NOT NULL DEFAULT 0.0,
  lane_affinity REAL NOT NULL DEFAULT 0.0,
  PRIMARY KEY (anchor, profile_id, lane_id)
);

CREATE TABLE IF NOT EXISTS are_events (
  event_id TEXT PRIMARY KEY,
  ts_ms INTEGER NOT NULL,
  op TEXT NOT NULL,
  profile_id TEXT NOT NULL,
  lane_id TEXT NOT NULL,
  session_id TEXT NOT NULL,
  anchors_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_are_anchor_stats_profile_lane
ON are_anchor_stats(profile_id, lane_id);

CREATE INDEX IF NOT EXISTS idx_are_events_ts
ON are_events(ts_ms);
"""


def _now_ms() -> int:
    return int(time.time() * 1000)


def _exp_decay(age_seconds: float, half_life_seconds: float) -> float:
    # weight = 0.5^(age/half_life)
    if half_life_seconds <= 0:
        return 0.0
    return 0.5 ** (age_seconds / float(half_life_seconds))


class AREngine:
    def __init__(self, db_path: str, config: Optional[AREConfig] = None):
        self.db_path = db_path
        self.cfg = config or AREConfig()
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self._init_db()

    def _conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._conn() as conn:
            conn.executescript(SCHEMA_SQL)
            conn.commit()

    # ----------------------------
    # PUBLIC API
    # ----------------------------

    def apply_event(self, event: AREEvent) -> AREReceipt:
        t0 = _now_ms()
        request_id = str(uuid.uuid4())

        # Sanity: deterministic
        anchors = [a.strip() for a in event.anchors if a and a.strip()]
        anchors = sorted(set(anchors))  # stable, unique

        with self._conn() as conn:
            # Store event for audit trail (not required for scoring, but required for proof)
            conn.execute(
                "INSERT INTO are_events(event_id, ts_ms, op, profile_id, lane_id, session_id, anchors_json) "
                "VALUES(?,?,?,?,?,?,?)",
                (str(uuid.uuid4()), event.ts_ms, event.op, event.profile_id, event.lane_id, event.session_id, str(anchors)),
            )

            # Update stats per anchor
            for anchor in anchors:
                self._upsert_and_update_stats(conn, event, anchor)

            conn.commit()

            # Emit weights after update
            weights = self.get_weights(conn, event.profile_id, event.lane_id, anchors)

        elapsed = _now_ms() - t0
        return AREReceipt(
            request_id=request_id,
            ts_ms=_now_ms(),
            op=event.op,
            profile_id=event.profile_id,
            lane_id=event.lane_id,
            session_id=event.session_id,
            anchors_updated=len(anchors),
            weights_emitted=weights,
            elapsed_ms=elapsed,
        )

    def get_weights_for_lane(self, profile_id: str, lane_id: str, top_n: int = 20) -> Dict[str, float]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT anchor, total_count, recent_count, last_seen_ts_ms, last_window_reset_ts_ms, "
                "consistency_score, lane_affinity "
                "FROM are_anchor_stats WHERE profile_id=? AND lane_id=?",
                (profile_id, lane_id),
            ).fetchall()

            scored = []
            for r in rows:
                w = self._score_row(r)
                scored.append((r["anchor"], w))

            scored.sort(key=lambda x: x[1], reverse=True)
            return {a: w for a, w in scored[: max(1, int(top_n))]}

    # ----------------------------
    # INTERNALS
    # ----------------------------

    def _upsert_and_update_stats(self, conn: sqlite3.Connection, event: AREEvent, anchor: str) -> None:
        # Get row
        row = conn.execute(
            "SELECT total_count, recent_count, last_seen_ts_ms, last_window_reset_ts_ms, "
            "consistency_score, lane_affinity "
            "FROM are_anchor_stats WHERE anchor=? AND profile_id=? AND lane_id=?",
            (anchor, event.profile_id, event.lane_id),
        ).fetchone()

        if row is None:
            # Insert new
            conn.execute(
                "INSERT INTO are_anchor_stats(anchor, profile_id, lane_id, total_count, recent_count, "
                "last_seen_ts_ms, last_window_reset_ts_ms, consistency_score, lane_affinity) "
                "VALUES(?,?,?,?,?,?,?,?,?)",
                (anchor, event.profile_id, event.lane_id, 0, 0, 0, event.ts_ms, 0.0, 0.0),
            )
            row = conn.execute(
                "SELECT total_count, recent_count, last_seen_ts_ms, last_window_reset_ts_ms, "
                "consistency_score, lane_affinity "
                "FROM are_anchor_stats WHERE anchor=? AND profile_id=? AND lane_id=?",
                (anchor, event.profile_id, event.lane_id),
            ).fetchone()

        total = int(row["total_count"])
        recent = int(row["recent_count"])
        last_seen = int(row["last_seen_ts_ms"])
        last_reset = int(row["last_window_reset_ts_ms"])
        consistency = float(row["consistency_score"])
        affinity = float(row["lane_affinity"])

        # Window reset if stale
        if event.ts_ms - last_reset > self.cfg.recent_window_seconds * 1000:
            recent = 0
            last_reset = event.ts_ms

        # Increment counts for write/recall only (promote/suppress handled separately)
        if event.op in ("write", "recall"):
            total += 1
            recent += 1

            # Consistency: reward repeated use without long gaps
            # If the anchor repeats within half-life, it increases consistency more.
            if last_seen > 0:
                age_s = max(0.0, (event.ts_ms - last_seen) / 1000.0)
                consistency_boost = _exp_decay(age_s, self.cfg.half_life_seconds)
            else:
                consistency_boost = 0.25
            consistency = min(1.0, consistency + 0.10 * consistency_boost)

            # Lane affinity: if anchor is used in this lane repeatedly, rise slowly
            affinity = min(1.0, affinity + 0.02)

        elif event.op == "promote":
            consistency = min(1.0, consistency + 0.15)
            affinity = min(1.0, affinity + 0.10)

        elif event.op == "suppress":
            consistency = max(0.0, consistency - 0.20)
            affinity = max(0.0, affinity - 0.15)

        # Update row
        conn.execute(
            "UPDATE are_anchor_stats SET total_count=?, recent_count=?, last_seen_ts_ms=?, "
            "last_window_reset_ts_ms=?, consistency_score=?, lane_affinity=? "
            "WHERE anchor=? AND profile_id=? AND lane_id=?",
            (total, recent, event.ts_ms, last_reset, consistency, affinity, anchor, event.profile_id, event.lane_id),
        )

    def get_weights(self, conn: sqlite3.Connection, profile_id: str, lane_id: str, anchors: List[str]) -> Dict[str, float]:
        weights: Dict[str, float] = {}
        for anchor in anchors:
            r = conn.execute(
                "SELECT anchor, total_count, recent_count, last_seen_ts_ms, last_window_reset_ts_ms, "
                "consistency_score, lane_affinity "
                "FROM are_anchor_stats WHERE anchor=? AND profile_id=? AND lane_id=?",
                (anchor, profile_id, lane_id),
            ).fetchone()
            if r is None:
                weights[anchor] = self.cfg.min_weight
            else:
                weights[anchor] = self._score_row(r)
        return weights

    def _score_row(self, r: sqlite3.Row) -> float:
        total = float(r["total_count"])
        recent = float(r["recent_count"])
        last_seen_ms = int(r["last_seen_ts_ms"])
        consistency = float(r["consistency_score"])
        affinity = float(r["lane_affinity"])

        # Decay from last seen
        now_ms = _now_ms()
        age_s = max(0.0, (now_ms - last_seen_ms) / 1000.0) if last_seen_ms > 0 else (10**9)
        decay = _exp_decay(age_s, self.cfg.half_life_seconds)

        raw = (
            (recent * self.cfg.alpha_recent)
            + (total * self.cfg.beta_total)
            + (consistency * self.cfg.gamma_consistency)
            + (affinity * self.cfg.gamma_lane_affinity)
        )

        # Apply decay to keep "now matters" true
        raw *= decay

        # Normalize into [min_weight, max_weight] via a simple squash
        # weight = raw / (1 + raw)
        w = raw / (1.0 + raw) if raw > 0 else 0.0
        w = max(self.cfg.min_weight, min(self.cfg.max_weight, w))
        return float(w)
