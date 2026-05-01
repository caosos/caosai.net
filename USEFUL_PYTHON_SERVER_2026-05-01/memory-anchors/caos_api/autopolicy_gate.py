"""
CAOS-A1 — Autopolicy Gate (Structural Only)

ROLE
----
External policy decision hook.
Structural allow/deny only.
No inference. No defaults. No mutation.

INVARIANTS
----------
- Decision is explicit
- No session logic
- No Plane B access
- Fail-closed
"""

from typing import Dict, Any


class PolicyDeniedError(Exception):
    pass


def require_policy_allow(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise PolicyDeniedError("payload must be a dict")

    decision = payload.get("policy")
    if decision != "allow":
        raise PolicyDeniedError("policy denied")

    return payload
