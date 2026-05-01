CAOS-A1 — HTTP TRANSPORT LOCK (CANONICAL)

================================================================
PURPOSE
================================================================
Lock the HTTP transport layer as a pure delegation shell.

================================================================
SCOPE
================================================================
memory-anchors/caos_api/http_transport_stub.py

================================================================
ALLOWED BEHAVIOR
================================================================
- Accept structured request payload
- Delegate to server_entrypoint
- Return response verbatim

================================================================
FORBIDDEN
================================================================
- Server frameworks (FastAPI, Flask, Express, etc.)
- Socket binding
- Middleware
- Authentication logic
- Validation logic
- Caching
- Learning
- Inference
- Mutation

================================================================
INVARIANTS
================================================================
- Read-only
- Deterministic
- Explicit invocation
- Zero business logic

================================================================
STATUS
================================================================
HTTP TRANSPORT: LOCKED
READY FOR FRAMEWORK ADAPTER (OUTSIDE CORE)
================================================================
