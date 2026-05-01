from caos_core.plane_b import PlaneB
from caos_core.anchors import AnchorRegistry
from caos_core.amendments import Amendments
from caos_core.anchor_maps import AnchorMaps
from caos_core.recall import RecallEngine, RecallIndex
from caos_core.context import ContextResolver
from caos_core.pending_queue import PendingResolutionQueue
from caos_core.export import Exporter
from caos_core.plane_b_adapter import PlaneBAdapter


class CAOSKernel:
    """
    Canonical wiring only.
    No execution side effects.
    """

    def __init__(self, paths):
        # 1) Truth
        self.plane_b = PlaneB(paths.plane_b)

        # 2) Deterministic tagging
        self.anchors = AnchorRegistry()

        # 3) Corrections
        self.amendments = Amendments(self.plane_b)

        # 4) Index plane (derived)
        self.plane_b_adapter = PlaneBAdapter(self.plane_b)
        self.anchor_maps = AnchorMaps(paths.index)

        # 5) Recall (verification always hits Plane B)
        self.recall_index = RecallIndex.from_store(self.plane_b)
        self.recall = RecallEngine(self.recall_index)

        # 6) Ambiguity handling
        self.pending = PendingResolutionQueue(paths.exports)
        self.context = ContextResolver(self.pending)

        # 7) Export (read-only)
        self.exporter = Exporter(self.plane_b, paths.exports)
