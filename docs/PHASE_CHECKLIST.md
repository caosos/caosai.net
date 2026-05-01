# Phase Checklist

## Phase 1 — Portable foundation

Goal: prove the clean backend can boot and expose safe development/runtime contracts without Emergent OAuth, Base44, production secrets, or legacy runtime data.

### Required files

- [x] `backend/.env.example`
- [x] `backend/app/main.py`
- [x] `backend/app/api/health.py`
- [x] `backend/app/api/auth.py`
- [x] `backend/app/api/runtime.py`
- [x] `backend/app/core/config.py`
- [x] `backend/app/core/logging.py`
- [x] `backend/app/core/runtime_registry.py`
- [x] `backend/app/core/database.py`
- [x] `backend/app/core/dev_auth.py`
- [x] `backend/app/schemas/common.py`
- [x] `backend/app/schemas/auth.py`

### Required behavior

- [x] `/api/health` returns an API envelope.
- [x] `/api/runtime` returns runtime state without leaking secrets.
- [x] `/api/auth/dev-login` returns a development admin session when enabled.
- [x] Base44 runtime is explicitly reported disabled.
- [x] Emergent OAuth is explicitly reported disabled.
- [x] Mongo can be absent during early boot.
- [ ] Local checkout smoke test completed.
- [ ] Import/boot validation completed.

### Exit criteria

Phase 1 exits only when a real checkout can run the backend and call:

```text
GET  /api/health
GET  /api/runtime
POST /api/auth/dev-login
```

## Phase 2 — Minimal chat contract

Not started.

Required before implementation:

- Inspect Emergent chat docs/source.
- Update source-to-target map for chat files.
- Define chat request/response schema.
- Define receipt envelope for a chat turn.

## Phase 3 — Persistence and threads

Not started.

## Phase 4 — Memory and recall

Not started.

## Phase 5 — Frontend skeleton

Not started.

## Phase 6 — Admin, tickets, artifacts, connectors

Not started.
