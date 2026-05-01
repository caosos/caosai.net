"""
CAOS-A1 — API Gate (Session Only)

ROLE
----
Read-only API gate exposing session continuity.
No business logic. No persistence. No inference.

INVARIANTS
----------
- Plane B is authoritative
- Session guard enforced
- Deterministic outputs only
"""

from typing import Dict, Any
from caos_core.plane_b import PlaneB
from caos_core.session_api_adapter import get_session_summary


def api_get_session_summary(
    *,
    plane_b: PlaneB,
    session_id: str,
) -> Dict[str, Any]:
    """
    API-safe wrapper for session summary.
    """
    return get_session_summary(
        plane_b=plane_b,
        session_id=session_id,
    )
