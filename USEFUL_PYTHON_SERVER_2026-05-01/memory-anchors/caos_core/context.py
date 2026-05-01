"""
CAOS-A1 — Context Resolution & Ambiguity Handling

ROLE
----
Detect ambiguity and block unsafe behavior.

INVARIANTS
----------
- No guessing
- No silent fallback
- Ambiguity blocks recall
- Human resolution is required (pending queue)
- No eval(), no repr(), no executable serialization
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Dict, Any, Optional

from caos_core.pending_queue import PendingResolutionQueue


@dataclass(frozen=True)
class ContextDecision:
    ok: bool
    reason: str
    pending_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None


class ContextResolver:
    """
    Minimal ambiguity detector.

    This module does not interpret meaning.
    It enforces explicitness only.
    """

    def __init__(self, pending: PendingResolutionQueue):
        self._pending = pending

    def resolve_for_recall(
        self,
        user_text: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> ContextDecision:
        """
        Determine whether recall is permitted.

        Policy (v1 minimal):
        - If context contains {"allow_recall": True} => ok
        - Otherwise => ambiguous => block and queue
        """
        ctx = dict(context or {})

        if ctx.get("allow_recall") is True:
            return ContextDecision(ok=True, reason="CONTEXT_OK", context=ctx)

        pending_id = self._make_pending_id(user_text, ctx)

        self._pending.add(
            pending_id=pending_id,
            reason="AMBIGUOUS_CONTEXT",
            raw_input=user_text,
            context={"needed": ["allow_recall"], "provided": ctx},
        )

        return ContextDecision(
            ok=False,
            reason="AMBIGUOUS_CONTEXT",
            pending_id=pending_id,
            context=ctx,
        )

    def _make_pending_id(self, user_text: str, ctx: Dict[str, Any]) -> str:
        """
        Deterministic pending id.

        Uses JSON canonicalization (sort_keys + compact separators).
        No repr() is permitted.
        """
        h = hashlib.sha256()
        h.update(user_text.encode("utf-8", errors="replace"))
        h.update(b"\n")

        canonical_ctx = json.dumps(ctx, sort_keys=True, separators=(",", ":"))
        h.update(canonical_ctx.encode("utf-8", errors="replace"))

        return h.hexdigest()[:16]
