"""
CAOS-A1 — Session API Adapter (Guarded)

ROLE
----
Read-only adapter for API layer consumption.
Exposes session recall utilities with ambiguity gating.

INVARIANTS
----------
- No mutation
- No inference
- Explicit session_id required
- Deterministic outputs
- Ambiguity blocked
"""

from typing import Dict, Any
from .plane_b import PlaneB
from .session_guard import require_session_id
from .session_tools import (
    first_in_session,
    last_in_session,
    session_record_ids,
)


def get_session_summary(
    *,
    plane_b: PlaneB,
    session_id: str,
) -> Dict[str, Any]:
    sid = require_session_id(session_id)

    return {
        "session_id": sid,
        "first": first_in_session(plane_b, sid),
        "last": last_in_session(plane_b, sid),
        "record_ids": session_record_ids(plane_b, sid),
    }
