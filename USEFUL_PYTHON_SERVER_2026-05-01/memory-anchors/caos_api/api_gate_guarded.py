"""
CAOS-A1 — API Gate (Guarded)

ROLE
----
Read-only API gate with strict request validation.
No business logic. No persistence. No inference.

INVARIANTS
----------
- Request validation required
- Session guard enforced downstream
- Deterministic outputs only
"""

from typing import Dict, Any
from caos_core.plane_b import PlaneB
from caos_api.request_validator import validate_session_request
from caos_core.session_api_adapter import get_session_summary


def api_get_session_summary_guarded(
    *,
    plane_b: PlaneB,
    payload: Dict[str, Any],
) -> Dict[str, Any]:
    data = validate_session_request(payload)

    return get_session_summary(
        plane_b=plane_b,
        session_id=data["session_id"],
    )
