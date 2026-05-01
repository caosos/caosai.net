# CAOS Linode Rebuild Status

## Current branch

`aria-emergent-clean-rebuild`

## Mission

Build a clean, server-owned CAOS on Ubuntu/Linode using `caosos/emergent-caos-build` as the working product reference and `legacy-python-server-salvage-2026-05-01` as old Python/memory salvage reference.

This is a clean modular rebuild, not a monolith mirror.

## Current phase

Phase 1: Portable foundation.

## Completed so far

### Documentation foundation

- `docs/REBUILD_CONTRACT.md`
- `docs/SOURCE_TO_TARGET_MAP.md`
- `docs/PORTABILITY_MATRIX.md`
- `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`
- `docs/EMERGENT_DOCUMENTATION_LEDGER.md`

### Backend foundation

- `backend/.env.example`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/api/__init__.py`
- `backend/app/api/health.py`
- `backend/app/api/auth.py`
- `backend/app/core/__init__.py`
- `backend/app/core/config.py`
- `backend/app/core/logging.py`
- `backend/app/core/runtime_registry.py`
- `backend/app/core/database.py`
- `backend/app/core/dev_auth.py`
- `backend/app/schemas/__init__.py`
- `backend/app/schemas/common.py`
- `backend/app/schemas/auth.py`

## Current capabilities

- FastAPI app entrypoint exists.
- `/api/health` route exists.
- `/api/auth/dev-login` route exists.
- Development admin auth exists for local/test validation.
- Runtime registry reports Base44 and Emergent OAuth disabled.
- Mongo boundary exists without forcing Mongo to be present during early boot.
- `.env.example` defines placeholder variables only; no real secrets are committed.

## Not built yet

- Runtime inspection route.
- Local smoke-test instructions.
- Phase checklist.
- Chat route/schema/orchestrator.
- Provider router/adapters.
- Thread persistence.
- Memory atom schemas/services.
- Artifact service.
- Support ticket service.
- Admin metrics/diagnostics.
- Frontend app skeleton.
- Deployment/systemd/nginx layer.

## Next immediate target

1. Add `backend/app/api/runtime.py`.
2. Add `docs/PHASE_CHECKLIST.md`.
3. Add `docs/LOCAL_SMOKE_TEST.md`.
4. Verify backend import/boot path from a real checkout.
5. Start minimal chat contract only after foundation smoke path exists.
