# Crosswire Integration Ledger

## Purpose

Parallel agents should build lane-local sections without freely editing shared files. Cross-lane wiring must be treated like schematic work: identify the connection points, record them, then let the orchestrator integrate intentionally.

## Core rule

Lane agents build their own sections. They do not edit shared files unless the orchestrator assigns that specific integration task.

When a lane needs a shared file, endpoint, schema, package dependency, router registration, UI mount point, or shared state contract, it records a crosswire request here instead of patching randomly.

## Crosswire request format

Each request must include:

```text
ID:
Requesting lane:
Target shared file/module:
Needed connection:
Reason:
Proposed interface:
Risk:
Blocking status:
Related branch/commit:
```

## Shared files requiring orchestrator wiring

Backend shared files:

- `backend/app/main.py`
- `backend/requirements.txt`
- `backend/app/core/config.py`
- `backend/app/core/database.py`
- `backend/app/services/receipt_service.py`

Frontend shared files:

- `frontend/package.json`
- `frontend/src/app/*`
- `frontend/src/routes*`
- root layout/composition files

Documentation shared files:

- `docs/BUILD_STATUS.md`
- `docs/SOURCE_TO_TARGET_MAP.md`
- `docs/DOCUMENTATION_INDEX.md`
- `docs/PHASE_CHECKLIST.md`

## Orchestrator responsibilities

The orchestrator must:

1. Review lane branch receipts.
2. Inspect changed files.
3. Verify lane boundaries were respected.
4. Read crosswire requests.
5. Resolve shared-file edits deliberately.
6. Update build status and source-to-target map.
7. Record integration commit SHAs.

## Integration model

Preferred integration pattern:

1. Lane creates isolated service/schema/component.
2. Lane records required mount/wiring point here.
3. Orchestrator wires the mount point.
4. Smoke/contract test verifies the lane is reachable.
5. Receipt records what was connected.

## Non-negotiable

No lane agent should casually patch shared files. Crosswiring happens from a ledger, not from impulse.
