from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

from caos_core.paths import Paths
from caos_core.plane_b import PlaneB
from caos_core.recall import recall as recall_by_anchors


class RecallRequestError(Exception):
    pass


PATHS = Paths(
    plane_b="./data/plane_b_runtime",
    index="./data/anchor_index",
    exports="./data/exports",
)

PLANE_B = PlaneB(PATHS.plane_b)


def http_post_recall(*, request_json: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(request_json, dict):
        raise RecallRequestError("request_json must be a dict")

    mode = request_json.get("mode")
    records: List[Dict[str, Any]] = []
    deny_reason: Optional[str] = None

    try:
        if mode == "session":
            sid = request_json.get("session_id")
            if not isinstance(sid, str) or not sid.strip():
                raise RecallRequestError("session_id must be non-empty")
            records = list(
                recall_by_anchors(PLANE_B, anchors=[f"session:{sid.strip()}"])
            )

        else:
            anchors = request_json.get("anchors")
            if not isinstance(anchors, list):
                raise RecallRequestError("anchors must be a list")
            records = list(
                recall_by_anchors(PLANE_B, anchors=[a.strip() for a in anchors if a])
            )

    except Exception as e:
        deny_reason = str(e)
        records = []

    return {
        "recall": records,
        "_meta": {
            "recall_used": bool(records) and deny_reason is None,
            "recall_count": len(records),
            "deny_reason": deny_reason,
        },
    }
