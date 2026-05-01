# Source-to-Target Map

## Rule

This map is a migration ledger, not a copy plan. Source files explain behavior; target modules implement cleanly.

## Emergent source reference

| Source area | Target area | Notes |
|---|---|---|
| `backend/app/services/chat_pipeline.py` | `backend/app/services/chat_orchestrator.py` plus context/prompt/tool/receipt modules | Split orchestration from business logic. |
| `backend/app/services/hydration_policy.py` | `backend/app/policies/hydration_policy.py` | Policy module only. |
| `backend/app/services/proactivity_policy.py` | `backend/app/policies/proactivity_policy.py` | Policy module only. |
| `backend/app/services/turn_trace.py` | `backend/app/schemas/turn_trace.py` and `backend/app/services/receipt_service.py` | Schema separated from receipt assembly. |
| `backend/app/services/artifact_builder.py` | `backend/app/services/artifact_service.py` and `backend/app/schemas/artifacts.py` | No UI formatting inside service. |
| `frontend/src/...` | `frontend/src/features/...` | Recompose by feature, not by page monolith. |

## Legacy Python salvage reference

| Salvage file | Target usage | Status |
|---|---|---|
| `memory-anchors/caos_core/plane_b.py` | Concept reference for append-only deterministic persistence | Do not copy SQLite store wholesale. Extract invariants. |
| `memory-anchors/caos_core/session_guard.py` | Direct conceptual fit for ambiguity gating | Candidate for clean port. |
| `memory-anchors/caos_core/session_recall.py` | Deterministic recall logic | Candidate for Mongo-backed equivalent. |
| `memory-anchors/caos_core/session_api_adapter.py` | API-safe adapter pattern | Candidate for service boundary. |
| `memory-anchors/caos_api/main.py` | Route/API wrapper pattern | Reference only; implement FastAPI routes cleanly. |

## Immediate target modules

```text
backend/app/main.py
backend/app/api/health.py
backend/app/api/auth.py
backend/app/core/config.py
backend/app/core/logging.py
backend/app/core/runtime_registry.py
backend/app/core/database.py
backend/app/core/dev_auth.py
backend/app/schemas/auth.py
backend/app/schemas/common.py
```

## Explicit exclusions

- Base44 code is excluded.
- Emergent OAuth is excluded from Phase 1.
- Legacy SQLite runtime data is excluded.
- Old `.env`, venvs, caches, and archives are excluded.
