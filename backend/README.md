# Backend

This directory will hold the Python API/runtime extracted from `caosos/emergent-caos-build`.

## Initial source references
- `backend/requirements.txt`
- `backend/app/services/chat_pipeline.py`
- `backend/app/services/hydration_policy.py`
- `backend/app/services/proactivity_policy.py`
- `backend/app/services/surface_registry.py`
- `backend/app/services/turn_trace.py`
- `backend/app/services/artifact_builder.py`

## First migration goal
Preserve the orchestration spine, context/memory handling, receipts, diagnostics, and connectors while removing dependency on Emergent-hosted runtime assumptions.
