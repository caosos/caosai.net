"""
CAOS-A1 — Session Tools (Derived Helpers)

ROLE
----
Convenience helpers built on session recall and session index.
Derived-only. Non-authoritative. Read-only.

INVARIANTS
----------
- No mutation
- No inference
- Exact session_id usage
- Deterministic behavior
"""

from typing import List, Dict, Any, Optional
from .plane_b import PlaneB
from .session_recall import recall_session
from .session_index import build_session_index


def first_in_session(
    plane_b: PlaneB,
    session_id: str,
) -> Optional[Dict[str, Any]]:
    records = recall_session(plane_b, session_id, order="asc", limit=1)
    return records[0] if records else None


def last_in_session(
    plane_b: PlaneB,
    session_id: str,
) -> Optional[Dict[str, Any]]:
    records = recall_session(plane_b, session_id, order="desc", limit=1)
    return records[0] if records else None


def session_record_ids(
    plane_b: PlaneB,
    session_id: str,
) -> List[str]:
    index = build_session_index(plane_b)
    return index.get(session_id, [])
