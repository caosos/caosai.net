"""
CAOS-A1 — HTTP Recall Bindings (Read-Only)

ROLE
----
Translate validated HTTP recall requests into deterministic Plane B recall.
No writes. No mutation. No inference.
FAIL-CLOSED (but provable via _meta).

SUPPORTED MODES
---------------
A) anchors:
   { "anchors": ["a","b"] }

B) time_range:
   { "mode":"time_range", "since":"2026-01-01T00:00:00Z", "until":"2026-01-08T00:00:00Z" }

C) session:
   { "mode":"session", "session_id":"<id>" }  -> translated to anchor session:<id>
"""

from __future__ import annotations

from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timezone

from caos_core.paths import Paths
from caos_core.plane_b import PlaneB
from caos_core.recall import recall as recall_by_anchors


class RecallRequestError(Exception):
    pass


# Process-owned wiring (read-only)
PATHS = Paths(
    plane_b="./data/plane_b_runtime",
    index="./data/anchor_index",
    exports="./data/exports",
)

PLANE_B = PlaneB(PATHS.plane_b)


def _parse_iso_z_to_ms(s: str) -> int:
    """
    Accepts ISO8601 with trailing Z (UTC), returns epoch ms.
    Example: 2026-01-25T01:23:45Z
    """
    if not isinstance(s, str) or not s.strip():
        raise RecallRequestError("since/until must be non-empty ISO strings")
    t = s.strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(t)
    except Exception:
        raise RecallRequestError("since/until must be ISO8601 (e.g. 2026-01-25T01:23:45Z)")
    if dt.tzinfo is None:
        # Fail-closed: caller must be explicit timezone
        raise RecallRequestError("since/until must include timezone (use Z)")
    return int(dt.astimezone(timezone.utc).timestamp() * 1000)


def _as_str_list(x: Any) -> List[str]:
    if not isinstance(x, list):
        raise RecallRequestError("anchors must be a list")
    out: List[str] = []
    for v in x:
        if not isinstance(v, str) or not v.strip():
            raise RecallRequestError("anchors must contain non-empty strings")
        out.append(v.strip())
    return out


def http_post_recall(*, request_json: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns a normalized dict:
      { "recall":[...], "_meta":{ recall_used, recall_count, deny_reason } }
    """
    if not isinstance(request_json, dict):
        raise RecallRequestError("request_json must be a dict")

    mode = request_json.get("mode")

    deny_reason: Optional[str] = None
    records: List[Dict[str, Any]] = []

    try:
        # MODE: time_range
        if mode == "time_range":
            since = _parse_iso_z_to_ms(request_json.get("since"))
            until = _parse_iso_z_to_ms(request_json.get("until"))
            if until < since:
                raise RecallRequestError("until must be >= since")

            # Deterministic scan of Plane B ordered by (ts_ms, record_id)
            for r in PLANE_B.iter_records():
                ts = int(r.get("ts_ms", 0))
                if ts < since:
                    continue
                if ts > until:
                    break
                records.append(r)

        # MODE: session -> anchor session:<id>
        elif mode == "session":
            sid = request_json.get("session_id")
            if not isinstance(sid, str) or not sid.strip():
                raise RecallRequestError("session_id must be a non-empty string")
            anchors = [f"session:{sid.strip()}"]
            records = list(recall_by_anchors(PLANE_B, anchors=anchors))

        # MODE: anchors (default behavior)
        else:
            anchors = _as_str_list(request_json.get("anchors"))
            records = list(recall_by_anchors(PLANE_B, anchors=anchors))

    except Exception as e:
        deny_reason = str(e)
        records = []

    return {
        "recall": records,
        "_meta": {
            "recall_used": bool(records) and deny_reason is None,
            "recall_count": len(records),
            "deny_reason": deny_reason,
        },
    }
