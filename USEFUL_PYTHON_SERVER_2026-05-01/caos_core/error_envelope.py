"""
CAOS-A1 — Error Envelope (Canonical)
Deterministic, machine + human readable.
Non-authoritative. Fail-closed compatible.
"""

import time
from typing import Dict, Any, Optional


def make_error(
    *,
    code: str,
    category: str,
    message: str,
    receipts: Optional[Dict[str, Any]] = None,
    actor: str = "system"
) -> Dict[str, Any]:
    return {
        "type": "error",
        "code": code,
        "category": category,
        "message": message,
        "receipts": receipts or {},
        "actor": actor,
        "ts_ms": int(time.time() * 1000),
    }


# Common helpers (optional usage)
def recall_insufficient(
    *,
    recall_mode: str,
    recall_count: int,
    required_minimum: int,
    window: Dict[str, int]
) -> Dict[str, Any]:
    return make_error(
        code="RECALL_INSUFFICIENT_CONTEXT",
        category="recall",
        message="Insufficient recalled messages to answer request.",
        receipts={
            "recall_mode": recall_mode,
            "recall_count": recall_count,
            "required_minimum": required_minimum,
            "window": window,
        },
    )
