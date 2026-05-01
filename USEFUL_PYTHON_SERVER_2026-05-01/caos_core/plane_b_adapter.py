from typing import Iterable, Optional, Dict, Any

class PlaneBAdapter:
    """
    Shape adapter ONLY.
    No logic, no mutation, no inference.
    """

    def __init__(self, plane_b):
        self._pb = plane_b

    def iter_records(self) -> Iterable[Dict[str, Any]]:
        for r in self._pb.iter_records():
            yield {
                "record_id": r["record_id"] if isinstance(r, dict) else r.record_id,
                "anchors": r["anchors"] if isinstance(r, dict) else r.anchors,
            }

    def get_record(self, record_id: str) -> Optional[Dict[str, Any]]:
        r = self._pb.get_record(record_id)
        if r is None:
            return None
        return {
            "record_id": r["record_id"] if isinstance(r, dict) else r.record_id,
            "anchors": r["anchors"] if isinstance(r, dict) else r.anchors,
        }
