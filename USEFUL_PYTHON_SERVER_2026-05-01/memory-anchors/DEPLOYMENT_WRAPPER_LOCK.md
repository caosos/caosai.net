CAOS-A1 — DEPLOYMENT WRAPPER LOCK (CANONICAL)

================================================================
PURPOSE
================================================================
Define the outermost deployment boundary.
This wrapper is responsible ONLY for process lifecycle.

================================================================
ALLOWED
================================================================
- Process start/stop
- Env loading
- Wiring Plane B into server_entrypoint
- Selecting framework adapter

================================================================
FORBIDDEN
================================================================
- Business logic
- Validation
- Auth decisions
- Session logic
- Caching
- Learning
- Inference

================================================================
INVARIANTS
================================================================
- Single entrypoint
- Read-only behavior
- Deterministic startup
- No side effects beyond wiring

================================================================
STATUS
================================================================
DEPLOYMENT WRAPPER: LOCKED
================================================================
