"""
CAOS-A1 — Session Guard (Ambiguity Gate)

ROLE
----
Hard gate enforcing presence of session_id.
Blocks ambiguous session access.

INVARIANTS
----------
- No defaults
- No inference
- No mutation
- Explicit failure on ambiguity
"""

from typing import Optional


class SessionAmbiguityError(Exception):
    pass


def require_session_id(session_id: Optional[str]) -> str:
    if not session_id or not isinstance(session_id, str):
        raise SessionAmbiguityError("session_id is required and must be a non-empty string")
    return session_id
