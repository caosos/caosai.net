"""
CAOS-A1 — HTTP Bindings
ROLE:
- Memory write ALWAYS
- Optional recall
- Delegate reply generation to responder
"""

from typing import Dict, Any
from caos_core.kernel import CAOSKernel
from caos_core.paths import Paths
from caos_core.recall import recall
from caos_api.observability_stub import build_meta
from caos_api.responder import generate_reply

PATHS = Paths(
    plane_b="./data/plane_b_runtime",
    index="./data/anchor_index",
    exports="./data/exports",
)

KERNEL = CAOSKernel(PATHS)

def http_post_message(
    *,
    request_json: Dict[str, Any],
    request_id: str,
    start_ts: float,
) -> Dict[str, Any]:

    session_id = request_json["session_id"]
    payload = request_json["payload"]
    anchors = request_json.get("anchors", [])

    # 1) ALWAYS WRITE MEMORY
    record_id = KERNEL.write_record(
        session_id=session_id,
        payload=payload,
        anchor_candidates=anchors,
    )

    # 2) OPTIONAL RECALL
    recall_records = []
    recall_used = False
    recall_req = request_json.get("recall")

    if isinstance(recall_req, dict) and recall_req.get("mode") == "session_tail":
        recall_used = True
        limit = int(recall_req.get("limit", 10))
        recall_records = list(
            recall(
                KERNEL.plane_b,
                anchors=[f"session:{session_id}"],
            )
        )[-limit:]

    # 3) GENERATE REPLY (REAL RESPONDER)
    reply = generate_reply(
        payload=payload,
        recall_records=recall_records,
    )

    return {
        "record_id": record_id,
        "reply": reply,
        "recall": recall_records,
        "_meta": build_meta(
            request_id=request_id,
            recall_used=recall_used,
            recall_count=len(recall_records),
            elapsed_ms=0,
        ),
    }
