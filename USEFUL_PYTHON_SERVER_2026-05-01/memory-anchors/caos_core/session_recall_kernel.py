"""
CAOS-A1 — Session Recall Kernel Adapter

ROLE
----
Kernel-level adapter exposing session recall.
Read-only. Non-authoritative.

INVARIANTS
----------
- Explicit invocation only
- Exact session_id matching
- Deterministic ordering
- No inference
- No side effects
"""

from typing import Iterable, Dict, Any, Optional
from .plane_b import PlaneB
from .session_recall import recall_session


def kernel_recall_session(
    *,
    plane_b: PlaneB,
    session_id: str,
    order: str = "asc",
    limit: Optional[int] = None,
) -> Iterable[Dict[str, Any]]:
    return recall_session(
        plane_b=plane_b,
        session_id=session_id,
        order=order,
        limit=limit,
    )
