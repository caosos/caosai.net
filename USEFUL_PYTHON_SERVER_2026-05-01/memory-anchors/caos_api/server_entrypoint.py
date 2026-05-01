"""
CAOS-A1 — Server Entrypoint (Session API Only, Fully Guarded)

ROLE
----
Single, explicit entrypoint for session API exposure.
Adds request_id + timing boundary ONLY.

NON-NEGOTIABLE
--------------
- Fail-closed on auth/policy
- Recall and denials must be PROVABLE:
  _meta.recall_used, _meta.recall_count, _meta.deny_reason ALWAYS present for /recall
"""

from typing import Dict, Any
import uuid

from caos_api.auth_envelope import require_auth_envelope
from caos_api.autopolicy_gate import require_policy_allow
from caos_api.http_bindings import http_post_message
from caos_api.http_bindings_recall import http_post_recall
from caos_api.observability_stub import observe_start, observe_end


def handle_post_message(
    *,
    request_json: Dict[str, Any],
) -> Dict[str, Any]:
    request_id = str(uuid.uuid4())
    start_ts = observe_start()

    payload = require_auth_envelope(request_json)
    payload = require_policy_allow(payload)

    response = http_post_message(
        request_json=payload,
        request_id=request_id,
        start_ts=start_ts,
    )

    # response is expected to be a dict with _meta
    if isinstance(response, dict):
        response.setdefault("_meta", {})
        response["_meta"]["request_id"] = response["_meta"].get("request_id", request_id)
        response["_meta"]["elapsed_ms"] = observe_end(start_ts)
    return response


def handle_post_recall(
    *,
    request_json: Dict[str, Any],
) -> Dict[str, Any]:
    request_id = str(uuid.uuid4())
    start_ts = observe_start()

    # Default provable response (fail-closed, but never silent)
    out: Dict[str, Any] = {
        "recall": [],
        "_meta": {
            "request_id": request_id,
            "elapsed_ms": None,
            "recall_used": False,
            "recall_count": 0,
            "deny_reason": None,
        },
    }

    try:
        payload = require_auth_envelope(request_json)
        payload = require_policy_allow(payload)

        # http_post_recall returns normalized dict with recall + _meta
        inner = http_post_recall(request_json=payload)
        if isinstance(inner, dict):
            out["recall"] = list(inner.get("recall", []))
            inner_meta = inner.get("_meta", {}) if isinstance(inner.get("_meta"), dict) else {}
            out["_meta"]["recall_used"] = bool(inner_meta.get("recall_used"))
            out["_meta"]["recall_count"] = int(inner_meta.get("recall_count", len(out["recall"])))
            out["_meta"]["deny_reason"] = inner_meta.get("deny_reason")
        else:
            out["_meta"]["deny_reason"] = "invalid recall handler response"

    except Exception as e:
        out["_meta"]["deny_reason"] = str(e)

    out["_meta"]["elapsed_ms"] = observe_end(start_ts)
    return out
