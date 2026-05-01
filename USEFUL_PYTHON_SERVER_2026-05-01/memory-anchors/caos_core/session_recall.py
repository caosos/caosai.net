"""
CAOS-A1 — Session Recall Engine

ROLE
----
Deterministic, sequence-based recall within a single session.
Non-authoritative. Read-only.

INVARIANTS
----------
- Exact session_id matching only
- Deterministic ordering by ts_ms then record_id
- No inference
- No scoring
- No fallback
"""

from typing import Iterable, Dict, Any, Optional
from .plane_b import PlaneB


def recall_session(
    plane_b: PlaneB,
    session_id: str,
    *,
    order: str = "asc",
    limit: Optional[int] = None
) -> Iterable[Dict[str, Any]]:
    """
    Recall records belonging to a single session.

    order:
      - "asc"  : earliest → latest
      - "desc" : latest → earliest
    """

    if order not in ("asc", "desc"):
        raise ValueError("order must be 'asc' or 'desc'")

    records = [
        r for r in plane_b.iter_records()
        if r["session_id"] == session_id
    ]

    if order == "desc":
        records = list(reversed(records))

    if limit is not None:
        records = records[:limit]

    return records
