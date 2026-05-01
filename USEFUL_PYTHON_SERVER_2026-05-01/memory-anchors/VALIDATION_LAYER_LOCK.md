CAOS-A1 — VALIDATION LAYER LOCK (CANONICAL)

================================================================
PURPOSE
================================================================
Freeze validation as a strictly structural concern.
Validation checks shape and presence only — never meaning.

================================================================
SCOPE
================================================================
- caos_api/request_validator.py
- caos_api/auth_envelope.py
- caos_api/autopolicy_gate.py

================================================================
ALLOWED VALIDATION
================================================================
- Type checks
- Required-field presence
- Explicit allow / deny decisions
- Structural envelope verification

================================================================
FORBIDDEN
================================================================
- Semantic interpretation
- Heuristics
- Defaults
- Learning
- Caching
- Any Plane B access

================================================================
INVARIANTS
================================================================
- Fail-closed on error
- Deterministic behavior
- No side effects
- No mutation

================================================================
STATUS
================================================================
VALIDATION LAYER: LOCKED
================================================================
