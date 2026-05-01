CAOS-A1 — /recall Route Lock (LOCKED)

STATUS
------
LOCKED

ROUTE
-----
POST /recall

ENVELOPE (REQUIRED)
-------------------
{
  "auth": { ... },
  "policy": "allow",
  "anchors": ["<string>", ...]
}

INVARIANTS
----------
- Read-only
- Deterministic
- Fail-closed
- Plane B authoritative
- No inference
