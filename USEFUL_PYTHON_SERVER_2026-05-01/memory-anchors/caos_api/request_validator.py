"""
CAOS-A1 — API Request Validator (Session)

ROLE
----
Validate external inputs before reaching API gate.
Fail-closed. No defaults. No mutation.

INVARIANTS
----------
- session_id required
- Exact types only
- Deterministic behavior
"""

from typing import Dict, Any


class RequestValidationError(Exception):
    pass


def validate_session_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise RequestValidationError("payload must be a dict")

    session_id = payload.get("session_id")
    if not isinstance(session_id, str) or not session_id:
        raise RequestValidationError("session_id must be a non-empty string")

    return {"session_id": session_id}
