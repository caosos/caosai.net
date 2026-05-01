"""
CAOS-A1 — Recall Engine (Anchor-Based)

ROLE
----
Deterministic, high-precision recall.
Retrieves records correctly, or not at all.

INVARIANTS
----------
- Explicit recall gate required ("recall:")
- Exact anchor matching only
- Deterministic ordering
- No semantic inference
- Fail-closed on ambiguity
"""

from typing import Iterable, Dict, Any, List
from .plane_b import PlaneB


def recall(
    plane_b: PlaneB,
    *,
    anchors: List[str],
) -> Iterable[Dict[str, Any]]:
    """
    Recall records that exactly match the provided anchors.

    This function is non-authoritative and read-only.
    """

    if not anchors:
        return []

    anchor_set = set(anchors)
    results = []

    for record in plane_b.iter_records():
        record_anchors = set(record.get("anchors", []))
        if anchor_set.issubset(record_anchors):
            results.append(record)

    # deterministic ordering: strongest overlap first, then time, then id
    def score(r):
        overlap = len(anchor_set.intersection(r["anchors"]))
        extra = len(r["anchors"]) - overlap
        return (-overlap, extra, r["ts_ms"], r["record_id"])

    results.sort(key=score)
    return results
