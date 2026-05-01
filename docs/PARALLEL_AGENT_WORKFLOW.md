# Parallel Agent Workflow

## Purpose

Multiple build agents can work in parallel if each agent has a bounded lane, a dedicated branch, clear receipts, and no authority to modify shared architecture silently.

Parallelism is useful only when it reduces cycle time without creating merge chaos.

## Ruling

Parallel agents are worth using after foundation contracts are stable.

Each agent must have:

- named branch
- declared scope
- allowed files/directories
- forbidden files/directories
- required docs to read before writing
- acceptance criteria
- receipt requirements
- final handoff note

## Required read order

1. `docs/DOCUMENTATION_INDEX.md`
2. `docs/BUILD_STATUS.md`
3. `docs/REBUILD_CONTRACT.md`
4. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
5. `docs/SOURCE_TO_TARGET_MAP.md`
6. lane-specific assignment document

## Lane model

### Orchestrator lane

Owns integration strategy, branch review, conflict resolution, build status updates, documentation index updates, and contract enforcement.

### Backend foundation lane

Owns backend routes, schemas, receipts, runtime, auth boundaries, and persistence boundaries.

Allowed areas:

- `backend/app/api/`
- `backend/app/core/`
- `backend/app/schemas/`
- `backend/app/services/`
- `backend/app/policies/`

### Memory and ARC lane

Owns memory capture, review, relevance, hydration, ARC assembly, summarization, context lineage, and prompt budget.

### Provider and model lane

Owns model catalog, provider router, adapter interfaces, WCW metadata, temperature controls, and provider receipts.

### Frontend shell lane

Owns React shell, layout, route composition, profile/settings dropdown, composer selector, response bubble receipts, and WCW meter surfaces.

### Admin, support, and artifacts lane

Owns admin dashboard contracts, support tickets, artifacts/files/photos/links, receipts, and audit surfaces.

## Branch naming

```text
agent/<lane>/<short-task>
```

Examples:

```text
agent/memory/arc-hydration-v1
agent/frontend/wcw-surfaces-v1
agent/provider/model-router-v1
agent/admin/support-ticket-contract-v1
```

## Merge strategy

No parallel branch merges directly to `main`.

All completed work targets:

```text
aria-emergent-clean-rebuild
```

Integration requires:

- receipts present
- docs updated
- scope stayed bounded
- forbidden files untouched
- smoke or contract checks listed

## Shared files requiring coordination

- `backend/app/main.py`
- `backend/requirements.txt`
- `frontend/package.json`
- `docs/BUILD_STATUS.md`
- `docs/SOURCE_TO_TARGET_MAP.md`
- `docs/DOCUMENTATION_INDEX.md`

## Final handoff note

Every agent must leave a handoff note containing:

- branch name
- files changed
- commits made
- behavior added
- tests or smoke checks run or pending
- unresolved issues
- docs updated
- next recommended action

## Non-negotiable

Parallel agents are bounded workers. The orchestrator owns integration. Michael owns approval for production deploys, main merges, destructive changes, and high-risk capability activation.
