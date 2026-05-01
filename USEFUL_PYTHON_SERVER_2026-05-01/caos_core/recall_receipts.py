"""
CAOS-A1 — Recall Receipts (V1)

Canonical construction of recall metadata.
Pure, deterministic, side-effect free.
"""

from typing import Dict, Any


def build_recall_receipt(
    recall_mode: str | None,
    recall_count: int,
    limit: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """
    Construct a recall receipt for attachment to response metadata.

    This does NOT decide recall.
    It only reports what occurred.
    """

    receipt = {
        "recall_used": recall_count > 0,
        "recall_count": recall_count,
        "recall_mode": recall_mode,
    }

    if limit is not None:
        receipt["limit"] = limit

    if offset is not None:
        receipt["offset"] = offset

    return receipt
