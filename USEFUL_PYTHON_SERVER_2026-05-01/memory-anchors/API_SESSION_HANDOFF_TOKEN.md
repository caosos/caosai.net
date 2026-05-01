CAOS-A1 — API SESSION HANDOFF TOKEN (CANONICAL)

================================================================
PURPOSE
================================================================
Define and lock the external API-facing session continuity surface.
This token is authoritative for wiring and integration.

================================================================
SOURCE OF TRUTH
================================================================
Plane B (SQLite, append-only)

================================================================
ALLOWED API CAPABILITY
================================================================
READ-ONLY SESSION CONTINUITY

The API MAY:
- Accept a session_id
- Return deterministic session summaries
- Expose first / last records
- Expose record_id ordering

The API MAY NOT:
- Mutate Plane B
- Infer intent
- Default session_id
- Cache or learn
- Perform scoring or heuristics

================================================================
VALID CALL PATH (LOCKED)
================================================================
HTTP
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
REQUIRED INVARIANTS
================================================================
- session_id is mandatory
- All failures are explicit
- Deterministic ordering only
- Derived layers are rebuildable
- No business logic in API layer

================================================================
PUBLIC API CONTRACT
================================================================
Input:
{
  "session_id": "<non-empty string>"
}

Output:
{
  "session_id": "<string>",
  "first": <record | null>,
  "last": <record | null>,
  "record_ids": [ "<record_id>", ... ]
}

================================================================
LOCK STATUS
================================================================
SESSION API SURFACE: LOCKED
MUTATION: FORBIDDEN
LEARNING: FORBIDDEN
CACHING: FORBIDDEN

================================================================
NEXT PERMITTED STEPS
================================================================
✔ Wire into server entrypoint
✔ Add auth envelope (non-semantic)
✔ Add transport (HTTP/WebSocket)

✘ Any change to session logic

================================================================
