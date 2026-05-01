"""
CAOS-A1 — Evaluator (Stub v1)

ROLE
----
Side-band semantic evaluator.
Observe-only. Non-blocking. Non-authoritative.

INVARIANTS
----------
- Never mutates payloads
- Never blocks execution
- Never accesses Plane B
- Always emits a result
- Fail-open (evaluation failure does not affect flow)
"""

from typing import Dict, Any, List


def evaluate(
    *,
    scope: str,
    payload: Dict[str, Any],
    context: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Evaluate a request or message without enforcement.

    Returns a deterministic EVAL_RESULT structure.
    """

    return {
        "scope": scope,
        "classification": "neutral",
        "confidence": 1.0,
        "signals": [],
        "action_required": False,
        "notes": "evaluator_stub_active",
    }
