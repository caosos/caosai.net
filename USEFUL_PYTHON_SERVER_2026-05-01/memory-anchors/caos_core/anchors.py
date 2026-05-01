"""
CAOS-A1 — Deterministic Anchors

ROLE
----
Deterministic anchor generation at write-time.

INVARIANTS
----------
- Registry-governed
- No inference
- No learning
- No runtime mutation
- Same input + same registry = same anchors
"""

from __future__ import annotations

from typing import Iterable, List, Dict, Set


class AnchorRegistry:
    """
    Deterministic anchor registry.

    This class defines which anchors are allowed
    and how they are produced.
    """

    def __init__(self) -> None:
        # Canonical registry (explicit, versioned)
        self._whitelist: Set[str] = set()

    # ------------------------------------------------------------------
    # Registry management (explicit only)
    # ------------------------------------------------------------------

    def register(self, anchor: str) -> None:
        """
        Register an anchor explicitly.

        This is a schema change, not learning.
        """
        a = anchor.strip()
        if not a:
            return
        self._whitelist.add(a)

    # ------------------------------------------------------------------
    # Anchor generation
    # ------------------------------------------------------------------

    def generate(self, candidates: Iterable[str]) -> List[str]:
        """
        Generate anchors deterministically.

        Only whitelisted anchors are emitted.
        """
        out: List[str] = []
        for c in candidates:
            a = c.strip()
            if not a:
                continue
            if a in self._whitelist:
                out.append(a)

        # Deterministic ordering
        return sorted(set(out))
