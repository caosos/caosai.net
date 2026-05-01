CAOS-A1 — API Route Locks (LOCKED)

STATUS
------
LOCKED

ROUTES
------
POST /message
POST /recall

INVARIANTS
----------
- Auth envelope REQUIRED
- Policy MUST be "allow"
- Deterministic behavior
- Fail-closed on violation
- Plane B authoritative
- /message: write-only
- /recall: read-only
