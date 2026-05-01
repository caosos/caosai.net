"""
CAOS-A1 — HTTP Transport Stub (Session Only)

ROLE
----
Minimal transport binding placeholder.
No server framework.
No sockets.
No execution.

INVARIANTS
----------
- Delegation only
- Read-only
- Explicit invocation required
"""

from typing import Dict, Any
from caos_core.plane_b import PlaneB
from caos_api.server_entrypoint import handle_session_summary_request


def transport_handle_request(
    *,
    plane_b: PlaneB,
    request_json: Dict[str, Any],
) -> Dict[str, Any]:
    return handle_session_summary_request(
        plane_b=plane_b,
        request_json=request_json,
    )
