# Portability Matrix

## Goal

CAOS must run outside Emergent/Base44 assumptions on a normal Ubuntu/Linode host.

| Capability | Phase 1 decision | Later production decision |
|---|---|---|
| Auth | Development admin auth adapter | Real OAuth/session provider |
| Database | Mongo interface boundary, no hard runtime dependency in route imports | MongoDB service with indexes/migrations |
| Inference | Provider router interface only | OpenAI/other adapters behind router |
| File storage | Interface only | Local/object storage adapter |
| Memory | Schema and service boundary | Mongo-backed memory atoms plus governed promotion |
| Legacy Plane B | Preserve invariants as reference | Optional import/migration tool if useful |
| Admin | Server-side role check required | Full admin audit boundary |
| Frontend | Modular app skeleton | Feature-by-feature behavior parity |

## Phase 1 portable foundation

Phase 1 must be runnable without:

- Emergent OAuth
- Base44 SDK/runtime
- production secrets
- legacy SQLite data
- old server venv
- frontend monolith assumptions

## Required environment variables

```text
CAOS_ENV=development
CAOS_DEV_AUTH_ENABLED=true
CAOS_APP_NAME=CAOS
CAOS_LOG_LEVEL=INFO
MONGO_URI=
MONGO_DB_NAME=caos
```

Empty `MONGO_URI` is allowed during early skeleton work. Routes that do not require persistence must still run.
