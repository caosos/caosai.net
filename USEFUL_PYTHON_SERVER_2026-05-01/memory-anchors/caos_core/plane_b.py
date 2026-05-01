"""
CAOS-A1 — Plane B (Authoritative Storage)

ROLE
----
Single source of truth.
Append-only, crash-safe, deterministic persistence.

INVARIANTS
----------
- SQLite is the only truth store
- WAL mode + synchronous=FULL
- No deletes, no overwrites
- All writes are atomic
- Server-authoritative timestamps only
- Client input is never trusted for IDs or time
- Stored data is inert (no executable representations)

ADDITIONAL CANONICAL INVARIANT
------------------------------
- Session is an anchor class.
  Plane B SHALL persist a deterministic session anchor:
    "session:<session_id>"
  on every record write.
"""

from __future__ import annotations

import sqlite3
import time
import json
from pathlib import Path
from typing import Iterable, Optional, Dict, Any, List


class PlaneB:
    """
    Authoritative persistence layer.
    """

    def __init__(self, root: Path):
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)
        self._db_path = self._root / "plane_b.sqlite3"

        self._conn = sqlite3.connect(
            self._db_path,
            isolation_level=None,
            check_same_thread=False,
        )

        self._configure()
        self._schema()

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def _configure(self) -> None:
        cur = self._conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL;")
        cur.execute("PRAGMA synchronous=FULL;")
        cur.execute("PRAGMA foreign_keys=ON;")
        cur.close()

    # ------------------------------------------------------------------
    # Schema
    # ------------------------------------------------------------------

    def _schema(self) -> None:
        cur = self._conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                record_id  TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                payload    TEXT NOT NULL,
                anchors    TEXT NOT NULL,
                ts_ms      INTEGER NOT NULL
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS amendments (
                amendment_id TEXT PRIMARY KEY,
                supersedes   TEXT NOT NULL,
                payload      TEXT NOT NULL,
                anchors      TEXT NOT NULL,
                ts_ms        INTEGER NOT NULL,
                FOREIGN KEY (supersedes) REFERENCES records(record_id)
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS latest_valid (
                logical_id TEXT PRIMARY KEY,
                record_id  TEXT NOT NULL
            )
            """
        )

        cur.close()

    # ------------------------------------------------------------------
    # Time
    # ------------------------------------------------------------------

    def _now_ms(self) -> int:
        return int(time.time() * 1000)

    # ------------------------------------------------------------------
    # Anchor normalization (mechanical only)
    # ------------------------------------------------------------------

    def _normalize_anchors(self, *, session_id: str, anchors: Iterable[str]) -> List[str]:
        """
        Mechanical, non-semantic normalization:
        - trims whitespace
        - drops empty entries
        - injects deterministic session anchor: session:<session_id>
        - returns sorted unique list
        """
        sid = (session_id or "").strip()
        if not sid:
            # Plane B does not guess. session_id is required upstream.
            raise ValueError("session_id must be a non-empty string")

        out = []
        for a in anchors:
            s = (a or "").strip()
            if s:
                out.append(s)

        out.append(f"session:{sid}")
        return sorted(set(out))

    # ------------------------------------------------------------------
    # Write API (append-only)
    # ------------------------------------------------------------------

    def insert_record(
        self,
        record_id: str,
        session_id: str,
        payload: Dict[str, Any],
        anchors: Iterable[str],
    ) -> None:
        ts = self._now_ms()

        anchors_norm = self._normalize_anchors(session_id=session_id, anchors=anchors)

        payload_blob = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        anchors_blob = json.dumps(anchors_norm, separators=(",", ":"), sort_keys=True)

        cur = self._conn.cursor()
        try:
            cur.execute("BEGIN;")

            cur.execute(
                """
                INSERT INTO records (record_id, session_id, payload, anchors, ts_ms)
                VALUES (?, ?, ?, ?, ?)
                """,
                (record_id, session_id, payload_blob, anchors_blob, ts),
            )

            cur.execute(
                """
                INSERT OR REPLACE INTO latest_valid (logical_id, record_id)
                VALUES (?, ?)
                """,
                (record_id, record_id),
            )

            cur.execute("COMMIT;")
        except Exception:
            cur.execute("ROLLBACK;")
            raise
        finally:
            cur.close()

    # ------------------------------------------------------------------
    # Read API
    # ------------------------------------------------------------------

    def get_record(self, record_id: str) -> Optional[Dict[str, Any]]:
        cur = self._conn.cursor()
        row = cur.execute(
            """
            SELECT record_id, session_id, payload, anchors, ts_ms
            FROM records
            WHERE record_id = ?
            """,
            (record_id,),
        ).fetchone()
        cur.close()

        if row is None:
            return None

        rid, sid, payload, anchors, ts = row
        return {
            "record_id": rid,
            "session_id": sid,
            "payload": json.loads(payload),
            "anchors": tuple(json.loads(anchors)),
            "ts_ms": ts,
        }

    def iter_records(self) -> Iterable[Dict[str, Any]]:
        cur = self._conn.cursor()
        rows = cur.execute(
            """
            SELECT record_id, session_id, payload, anchors, ts_ms
            FROM records
            ORDER BY ts_ms ASC, record_id ASC
            """
        )
        for rid, sid, payload, anchors, ts in rows:
            yield {
                "record_id": rid,
                "session_id": sid,
                "payload": json.loads(payload),
                "anchors": tuple(json.loads(anchors)),
                "ts_ms": ts,
            }
        cur.close()
