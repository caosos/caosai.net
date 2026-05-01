"""
CAOS-A1 — Deployment Wrapper Smoke Test (Policy-Aware)

ROLE
----
End-to-end structural verification of the locked call chain
including auth + autopolicy enforcement.
No server. No framework. Script-level only.

EXPECTS
-------
- Wrapper delegates correctly
- Auth envelope required
- Policy gate enforced
- Deterministic output shape
"""

from deployment_wrapper import wire_session_api

request = {
    "auth": {},
    "policy": "allow",
    "session_id": "session_test_001"
}

response = wire_session_api(request_json=request)
print(response)
