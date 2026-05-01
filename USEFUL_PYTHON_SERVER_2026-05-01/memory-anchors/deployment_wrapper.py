"""
CAOS-A1 — Deployment Wrapper (Read-Only)

ROLE
----
Outer process wiring only.
No logic. No inference. No mutation.

INVARIANTS
----------
- Single entrypoint
- Wires Plane B into selected framework adapter
- Does not start servers
- Explicit invocation only
"""

from typing import Dict, Any
from pathlib import Path

from caos_core.plane_b import PlaneB
from framework_adapters.fastapi_adapter_stub import fastapi_session_summary_adapter


def wire_session_api(*, request_json: Dict[str, Any]) -> Dict[str, Any]:
    root = Path("./data/plane_b_runtime")
    plane_b = PlaneB(root)

    return fastapi_session_summary_adapter(
        plane_b=plane_b,
        request_json=request_json,
    )
