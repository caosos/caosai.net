"""
CAOS-A1 — Session Index (Derived)

ROLE
----
Derived, non-authoritative index grouping record_ids by session_id.
Acceleration only. Fully rebuildable from Plane B.

INVARIANTS
----------
- Derived-only
- Exact session_id grouping
- Deterministic ordering (ts_ms, record_id)
- Fail-closed
- Read-only relative to Plane B
"""

from typing import Dict, List
from .plane_b import PlaneB


def build_session_index(plane_b: PlaneB) -> Dict[str, List[str]]:
    """
    Returns:
        { session_id: [record_id, ...] }
    """
    index: Dict[str, List[str]] = {}

    try:
        for record in plane_b.iter_records():
            sid = record["session_id"]
            index.setdefault(sid, []).append(record["record_id"])
    except Exception:
        return {}

    return index
