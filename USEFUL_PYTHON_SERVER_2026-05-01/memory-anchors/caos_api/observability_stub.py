"""
CAOS-A1 — Observability Stub (Read-Only)

ROLE
----
Structural audit hook.
Pass-through only (request_id, timing).
No payload logging.
No mutation. No inference.

INVARIANTS
----------
- Read-only
- Optional invocation
- Deterministic behavior
"""

from typing import Dict, Any
import time


def observe_start() -> float:
    return time.time()


def observe_end(start_ts: float) -> int:
    return int((time.time() - start_ts) * 1000)


def build_meta(
    *,
    request_id: str,
    recall_used: bool,
    recall_count: int,
    elapsed_ms: int,
) -> Dict[str, Any]:
    return {
        "request_id": request_id,
        "recall_used": recall_used,
        "recall_count": recall_count,
        "elapsed_ms": elapsed_ms,
    }
