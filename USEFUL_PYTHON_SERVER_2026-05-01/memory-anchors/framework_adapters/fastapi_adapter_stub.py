"""
CAOS-A1 — FastAPI Adapter Stub (Session API)

ROLE
----
Framework-specific adapter.
Lives OUTSIDE core.
Delegates only to HTTP transport stub.

INVARIANTS
----------
- No business logic
- No persistence
- No inference
- No mutation
- Delegation only
"""

from typing import Dict, Any
from caos_core.plane_b import PlaneB
from caos_api.http_transport_stub import transport_handle_request


def fastapi_session_summary_adapter(
    *,
    plane_b: PlaneB,
    request_json: Dict[str, Any],
) -> Dict[str, Any]:
    return transport_handle_request(
        plane_b=plane_b,
        request_json=request_json,
    )
