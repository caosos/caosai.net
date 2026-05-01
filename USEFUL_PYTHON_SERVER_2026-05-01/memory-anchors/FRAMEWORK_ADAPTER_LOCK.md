CAOS-A1 — FRAMEWORK ADAPTER LOCK (CANONICAL)

================================================================
PURPOSE
================================================================
Lock framework adapters as non-authoritative shells.

================================================================
SCOPE
================================================================
framework_adapters/*

================================================================
ALLOWED BEHAVIOR
================================================================
- Accept framework-native request objects
- Normalize to plain dict (no interpretation)
- Delegate to http_transport_stub only
- Return response verbatim

================================================================
FORBIDDEN
================================================================
- Business logic
- Validation
- Authentication
- Caching
- Learning
- Inference
- Persistence
- Direct Plane B access
- Skipping transport layer

================================================================
INVARIANTS
================================================================
- Read-only
- Deterministic
- Rebuildable
- Outside core boundary

================================================================
STATUS
================================================================
FRAMEWORK ADAPTER LAYER: LOCKED
================================================================
