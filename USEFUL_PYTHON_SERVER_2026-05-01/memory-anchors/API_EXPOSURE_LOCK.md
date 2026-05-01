CAOS-A1 — API EXPOSURE LOCK (CANONICAL)

================================================================
SCOPE
================================================================
Session continuity API surface only.

================================================================
ENTRYPOINT (SINGLE)
================================================================
caos_api/server_entrypoint.py

================================================================
REQUIRED ENVELOPES (ORDERED)
================================================================
1) Auth Envelope (structural only)
2) Request Validator
3) Session Guard

================================================================
CALL FLOW (LOCKED)
================================================================
HTTP
 ↓
server_entrypoint.py
 ↓
auth_envelope.py
 ↓
http_bindings.py
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
FORBIDDEN
================================================================
- Any write path
- Any learning
- Any caching
- Any inference
- Any new entrypoints

================================================================
STATUS
================================================================
API SURFACE: LOCKED
SESSION CONTINUITY: LOCKED
READY FOR TRANSPORT BINDING
================================================================
