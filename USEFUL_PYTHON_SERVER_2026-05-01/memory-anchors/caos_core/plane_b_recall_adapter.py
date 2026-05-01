"""
CAOS-A1 — Plane B → Recall Adapter

ROLE
----
Adapt Plane B record dictionaries into RecallRecord objects.

INVARIANTS
----------
- No logic
- No mutation
- No inference
- Shape adaptation ONLY
"""

from typing import Iterable

from caos_core.recall import RecallRecord
from caos_core.plane_b import PlaneB


class PlaneBRecallAdapter:
    """
    Adapter that presents Plane B as a RecallStore.
    """

    def __init__(self, plane_b: PlaneB):
        self._pb = plane_b

    def iter_records(self) -> Iterable[RecallRecord]:
        for r in self._pb.iter_records():
            yield RecallRecord(
                record_id=r["record_id"],
                anchors=tuple(r["anchors"]),
                payload=r.get("payload"),
                created_at_ms=r.get("ts_ms"),
            )
