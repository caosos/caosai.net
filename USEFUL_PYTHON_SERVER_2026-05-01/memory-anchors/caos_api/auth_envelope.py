"""
CAOS-A1 — Auth Envelope (Non-Semantic)

ROLE
----
Structural authentication wrapper.
No auth logic. No inference. No mutation.
Validates presence only.

INVARIANTS
----------
- No interpretation of auth data
- No defaults
- Fail-closed
"""

from typing import Dict, Any


class AuthEnvelopeError(Exception):
    pass


def require_auth_envelope(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise AuthEnvelopeError("payload must be a dict")

    auth = payload.get("auth")
    if not isinstance(auth, dict):
        raise AuthEnvelopeError("auth envelope required")

    return payload
