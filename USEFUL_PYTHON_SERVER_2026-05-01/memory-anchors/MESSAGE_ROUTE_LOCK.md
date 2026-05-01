CAOS-A1 — /message Route Lock (LOCKED)

STATUS
------
LOCKED

ROUTE
-----
POST /message

ENVELOPE (REQUIRED)
-------------------
{
  "auth": { ... },
  "policy": "allow",
  "session_id": "<string>",
  "payload": { ... },
  "anchors": ["<string>", ...]
}

CANONICAL FLOW
--------------
FastAPI (/message)
  -> caos_api.server_entrypoint.handle_post_message
     -> require_auth_envelope
     -> require_policy_allow
     -> caos_api.http_bindings.http_post_message
        -> KERNEL.write_record(...)
           -> PlaneB.insert_record(...)
              - MUST inject "session:<session_id>" anchor

INVARIANTS
----------
- No business logic in transport/bindings
- Deterministic
- Fail-closed
- Plane B authoritative
