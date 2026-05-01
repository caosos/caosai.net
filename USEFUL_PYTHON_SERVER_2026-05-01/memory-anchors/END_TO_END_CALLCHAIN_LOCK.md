CAOS-A1 — END-TO-END CALL CHAIN LOCK (CANONICAL)

================================================================
PURPOSE
================================================================
Freeze the complete read-only session call chain from framework
adapter to Plane B.

================================================================
CALL CHAIN (LOCKED)
================================================================
Framework Adapter
  ↓
http_transport_stub.py
  ↓
server_entrypoint.py
  ↓
api_gate_guarded.py
  ↓
request_validator.py
  ↓
session_guard.py
  ↓
session_api_adapter.py
  ↓
session_tools.py
  ↓
session_recall.py / session_index.py
  ↓
Plane B

================================================================
INVARIANTS
================================================================
- Single forward path only
- No bypasses
- No alternate entrypoints
- No mutation
- Deterministic results
- Fail-closed on any error

================================================================
FORBIDDEN
================================================================
- Short-circuiting layers
- Adding logic at boundaries
- Introducing state
- Caching or learning
- Writing tests that mutate Plane B

================================================================
STATUS
================================================================
END-TO-END CALL CHAIN: LOCKED
READY FOR DEPLOYMENT WRAPPER
================================================================
