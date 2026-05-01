"""
CAOS-A1 — Kernel Wiring

ROLE
----
Canonical system wiring.
Provides explicit, auditable entrypoints for write operations.

INVARIANTS
----------
- Plane B is authoritative
- No inference
- No implicit writes
- Explicit invocation only
"""

from uuid import uuid4
from typing import Dict, Any, Iterable

from caos_core.plane_b import PlaneB
from caos_core.anchors import AnchorRegistry
from caos_core.amendments import Amendments
from caos_core.anchor_maps import AnchorMaps
from caos_core.context import ContextResolver
from caos_core.pending_queue import PendingResolutionQueue
from caos_core.export import Exporter


class CAOSKernel:
    """
    Canonical system assembly.

    Order matters.
    Dependencies are explicit.
    """

    def __init__(self, paths):
        # 1) Authoritative truth
        self.plane_b = PlaneB(paths.plane_b)

        # 2) Deterministic tagging
        self.anchors = AnchorRegistry()

        # 3) Amendments / corrections
        self.amendments = Amendments(self.plane_b)

        # 4) Derived index (non-authoritative)
        self.anchor_maps = AnchorMaps(paths.index)

        # 5) Ambiguity handling
        self.pending = PendingResolutionQueue(paths.exports)
        self.context = ContextResolver(self.pending)

        # 6) Audit / export (read-only)
        self.exporter = Exporter(self.plane_b, paths.exports)

    # ------------------------------------------------------------------
    # Write entrypoint (explicit)
    # ------------------------------------------------------------------

    def write_record(
        self,
        *,
        session_id: str,
        payload: Dict[str, Any],
        anchor_candidates: Iterable[str],
    ) -> str:
        """
        Explicit write entrypoint.
        """
        record_id = str(uuid4())
        anchors = self.anchors.generate(anchor_candidates)

        self.plane_b.insert_record(
            record_id=record_id,
            session_id=session_id,
            payload=payload,
            anchors=anchors,
        )

        # Best-effort index update (never authoritative)
        try:
            self.anchor_maps.index_record_best_effort(record_id, anchors)
        except Exception:
            pass

        return record_id
