# CAOS Linode Rebuild Status

## Current branch

`aria-emergent-clean-rebuild`

## Mission

Build a clean, server-owned CAOS on Ubuntu/Linode using `caosos/emergent-caos-build` as the working product reference and `legacy-python-server-salvage-2026-05-01` as old Python/memory salvage reference.

This is a clean modular rebuild, not a monolith mirror.

## Current phase

Phase 1: Portable foundation and contract book.

## Completed so far

### Agent onboarding and documentation foundation

- `docs/START_HERE_AGENT_ONBOARDING.md`
- `docs/CONTRACTS_TABLE_OF_CONTENTS.md`
- `docs/DOCUMENTATION_INDEX.md`
- `docs/BUILD_STATUS.md`
- `docs/REBUILD_CONTRACT.md`
- `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
- `docs/AGENT_BASELINE_DIRECTIVES.md`
- `docs/PARALLEL_AGENT_WORKFLOW.md`
- `docs/CROSSWIRE_INTEGRATION_LEDGER.md`
- `docs/PHASE_CHECKLIST.md`
- `docs/LOCAL_SMOKE_TEST.md`
- `docs/TROUBLESHOOTING_VAULT.md`
- `docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md`

### Source, salvage, and behavior evidence

- `docs/SOURCE_TO_TARGET_MAP.md`
- `docs/EMERGENT_DOCUMENTATION_LEDGER.md`
- `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`
- `docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md`
- `docs/SALVAGE_POLICY.md`
- `docs/SEARCH_AND_RETRIEVAL_BEHAVIOR_CONTRACT.md`

### Runtime/product contracts

- `docs/PORTABILITY_MATRIX.md`
- `docs/ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md`
- `docs/MEMORY_ARC_HYDRATION_CONTRACT.md`
- `docs/WCW_ENGINE_CONTEXT_CONTRACT.md`
- `docs/RECEIPT_EVERYWHERE_CONTRACT.md`
- `docs/AGENTIC_PLATFORM_REQUIREMENT.md`
- `docs/LOCAL_MODEL_HOSTING_AND_COST_STRATEGY.md`
- `docs/FUTURE_MACHINE_INTERFACE_VISION.md`
- `docs/SYSTEM_BLUEPRINT.md`
- `docs/BUILD_PARTNERSHIP_STATEMENT.md`

### Public launch and analytics contracts

- `docs/PUBLIC_DISCOVERABILITY_SEO_CONTRACT.md`
- `docs/PRIVACY_RESPECTING_ANALYTICS_CONTRACT.md`

### Backend foundation

- `backend/.env.example`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/api/__init__.py`
- `backend/app/api/health.py`
- `backend/app/api/runtime.py`
- `backend/app/api/auth.py`
- `backend/app/api/models.py`
- `backend/app/api/chat.py`
- `backend/app/api/admin.py`
- `backend/app/api/memory.py`
- `backend/app/core/__init__.py`
- `backend/app/core/config.py`
- `backend/app/core/logging.py`
- `backend/app/core/runtime_registry.py`
- `backend/app/core/database.py`
- `backend/app/core/dev_auth.py`
- `backend/app/policies/__init__.py`
- `backend/app/policies/admin_boundary_policy.py`
- `backend/app/policies/hydration_policy.py`
- `backend/app/schemas/__init__.py`
- `backend/app/schemas/common.py`
- `backend/app/schemas/auth.py`
- `backend/app/schemas/admin.py`
- `backend/app/schemas/chat.py`
- `backend/app/schemas/memory.py`
- `backend/app/schemas/models.py`
- `backend/app/schemas/receipts.py`
- `backend/app/services/__init__.py`
- `backend/app/services/receipt_service.py`
- `backend/app/services/chat_orchestrator.py`
- `backend/app/services/memory_service.py`
- `backend/app/services/memory_capture_service.py`
- `backend/app/services/memory_review_service.py`
- `backend/app/services/memory_relevance_service.py`
- `backend/app/services/arc_assembler.py`
- `backend/app/services/sanitizer_service.py`
- `backend/app/services/prompt_budget_service.py`
- `backend/app/services/model_catalog.py`
- `backend/app/services/model_selection_service.py`

## Current backend routes

- `GET /api/health`
- `GET /api/runtime`
- `POST /api/auth/dev-login`
- `GET /api/models`
- `POST /api/models/select`
- `POST /api/chat/turn`
- `POST /api/admin/probe`
- `POST /api/memory/atoms`
- `POST /api/memory/atoms/query`

## Current capabilities

- FastAPI app entrypoint exists.
- Health, runtime, dev auth, model catalog, minimal chat, admin probe, and memory routes exist.
- Development admin auth exists for local/test validation.
- Runtime registry reports Base44 and Emergent OAuth disabled.
- Mongo boundary exists without forcing Mongo to be present during early boot.
- `.env.example` defines placeholder variables only; no real secrets are committed.
- Model catalog exposes provider/model WCW metadata.
- Minimal chat route returns a local contract response without provider/memory/tool/persistence side effects.
- Admin probe proves server-side admin boundary behavior.
- Memory atom route provides temporary in-process memory contract for testing.
- Action receipts are wired into health, runtime, model, memory, chat, and admin routes.
- Hydration, sanitization, prompt-budget, memory capture/review/relevance, and ARC assembly scaffolds exist.

## Not built yet

- Real provider router/adapters.
- Real OpenAI/Claude/Gemini/Grok/DeepSeek/local model calls.
- Persistent Mongo-backed memory/thread/artifact/ticket storage.
- Thread persistence and fuzzy/semantic thread search.
- Artifact/file/photo/link service.
- Support ticket service.
- Admin metrics/diagnostics implementation.
- Frontend app skeleton.
- Public crawlable website pages.
- Privacy-respecting analytics event taxonomy/implementation.
- TTS/STT rebuild and regression locks from Michael's logs.
- Deployment/systemd/nginx layer.
- Local smoke test from real checkout.

## Latest contract updates

- `FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md` completed with Base44/Emergent reference rules, Emergent preferred visual direction, public/app surface distinction, screenshot provenance, and no-frontend-before-contracts rule.
- `LOCAL_MODEL_HOSTING_AND_COST_STRATEGY.md` completed with cloud/local provider strategy, cost/latency routing, and local model runner guidance.
- `PUBLIC_DISCOVERABILITY_SEO_CONTRACT.md` added for crawlable public pages, sitemap, robots, metadata, and app-gated feature descriptions.
- `PRIVACY_RESPECTING_ANALYTICS_CONTRACT.md` added for product metrics only, no ad-surveillance model, no selling data, and no third-party behavioral profiling.
- `BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` updated with source-origin distinctions, SEO/public-page implications, analytics doctrine, and improved search requirements.
- `DOCUMENTATION_INDEX.md` and `CONTRACTS_TABLE_OF_CONTENTS.md` updated to include new contracts.

## Next immediate target

1. Run local smoke test from a real checkout.
2. Update `docs/LOCAL_SMOKE_TEST.md` to verify receipts on every route.
3. Wire hydration/ARC receipt into `/api/chat/turn`.
4. Start provider/router adapter lane after smoke validation.
5. Start frontend only after visual contracts and public/app surface contracts are accepted.
