# CAOS Build Execution Checklist

## Purpose

This is the controlling execution checklist for the clean CAOS Linode rebuild.

It translates the current contract set into ordered build work so agents do not improvise, duplicate effort, or create conflicting architecture.

## Current verified state

Repository:

```text
caosos/linode-repo
```

Active branch:

```text
aria-emergent-clean-rebuild
```

Current repo role:

```text
Clean CAOS Core rebuild for Ubuntu/Linode deployment.
```

Reference source:

```text
caosos/emergent-caos-build
```

CAOS Care migration is separate and belongs in its own isolated repo/server lane. Do not place CAOS Care under CAOS Core or CAOS A1.

## Current implementation status

Verified from repo inspection:

- Backend foundation exists.
- FastAPI app entrypoint exists.
- Health/runtime/auth/chat/admin/memory/models routes exist.
- Chat route is still a local contract stub.
- Memory service is in-process only and not production persistence.
- ARC/sanitizer/prompt-budget services are scaffolds.
- No frontend skeleton exists in this repo yet.
- No provider adapters are wired yet.
- No real thread persistence exists yet.
- No semantic/fuzzy thread search exists yet.
- No context meter implementation exists yet.
- Documentation contracts are ahead of implementation.

## Current monolith assessment

### linode-repo

No major application-code monolith was found during this checklist pass.

The current backend files inspected are small and modular:

- `backend/app/main.py`
- `backend/app/api/chat.py`
- `backend/app/services/chat_orchestrator.py`
- `backend/app/services/memory_service.py`
- `backend/app/services/arc_assembler.py`
- `backend/app/services/prompt_budget_service.py`
- `backend/app/services/sanitizer_service.py`

Main risk is not a current code monolith. Main risk is doctrine/implementation drift.

### CAOS Care reference warning

The separate `caosos/CAOSCARE.COM` repo does contain larger prototype files, especially `frontend/src/pages/Admin.jsx`. That belongs to the CAOS Care migration/refactor lane, not this CAOS Core checklist.

## Non-negotiable execution rules

- No fabrication.
- No simulated retrieval.
- No claiming tests passed unless actually run.
- No production deploy without Michael approval.
- No merge to protected/main branch without Michael approval.
- No CAOS Care nesting under CAOS A1 or CAOS Core directories.
- No frontend build before backend contracts for the required surface exist.
- No provider calls before provider adapter contract and receipts exist.
- No memory mutation without receipt and user governance path.
- No God files.
- Code target: <= 200 lines where practical.
- Code hard cap: 400 lines unless Michael explicitly approves an exception.
- Documentation/contract/vault files may be long-form when useful.

## Phase 0 — Repo truth and checklist alignment

Goal: bring the repo control documents into alignment before more implementation.

Tasks:

- [x] Inspect `README.md`.
- [x] Inspect `docs/BUILD_STATUS.md`.
- [x] Inspect `docs/PHASE_CHECKLIST.md`.
- [x] Inspect current backend route/service scaffolds.
- [x] Create this execution checklist.
- [ ] Update `docs/PHASE_CHECKLIST.md` so it no longer says Phase 2/4 are not started when stubs already exist.
- [ ] Update `docs/BUILD_STATUS.md` with latest contracts added after the earlier status doc.
- [ ] Add missing `AGENTS.md` at repo root.

Acceptance criteria:

- `BUILD_EXECUTION_CHECKLIST.md` exists.
- `PHASE_CHECKLIST.md` matches actual repo state.
- `BUILD_STATUS.md` mentions current context/memory/governance contracts.
- Future agents know where to start.

## Phase 1 — Local smoke test and route receipts

Goal: prove the backend boots from a real checkout and each current route returns the required envelope/receipt behavior.

Do not add provider calls in this phase.

Tasks:

- [ ] Run real local checkout smoke test.
- [ ] Verify backend import/boot.
- [ ] Verify `GET /api/health`.
- [ ] Verify `GET /api/runtime`.
- [ ] Verify `POST /api/auth/dev-login`.
- [ ] Verify `GET /api/models`.
- [ ] Verify `POST /api/models/select`.
- [ ] Verify `POST /api/chat/turn`.
- [ ] Verify `POST /api/admin/probe`.
- [ ] Verify `POST /api/memory/atoms`.
- [ ] Verify `POST /api/memory/atoms/query`.
- [ ] Update `docs/LOCAL_SMOKE_TEST.md` with exact results.

Acceptance criteria:

- Every existing route either passes or has a precise failure receipt.
- No hidden dependency on Mongo for early boot unless explicitly required.
- No production credentials are needed.

## Phase 2 — Context meter and arbitration scaffold

Goal: implement admin-visible context measurement before deep chat/provider work.

Reason: CAOS must not fly blind on context usage.

Source contract:

```text
docs/CONTEXT_METER_AND_ARBITRATION_CONTRACT.md
```

Tasks:

- [ ] Create context meter schema.
- [ ] Create `context_meter_service`.
- [ ] Extend `prompt_budget_service` from char-only accounting toward token-estimate buckets.
- [ ] Add bucket labels:
  - governance/system
  - user input
  - thin state snapshot
  - active lane state
  - recent history
  - ranked memory/anchors
  - source evidence/tool output
  - receipts/errors/diagnostics
  - reserved output
  - buffer
- [ ] Add admin route for context meter/probe.
- [ ] Add diagnostic receipt for context composition.

Acceptance criteria:

- Admin can inspect estimated context composition for a simulated turn.
- Receipt identifies included/excluded buckets.
- No provider call required.

## Phase 3 — Thin State Snapshot / lane scaffold

Goal: create the compact state layer before long-term memory and provider routing.

Source contracts:

```text
docs/THIN_STATE_SNAPSHOT_AND_RECALL_CONTRACT.md
docs/CONTEXT_METER_AND_ARBITRATION_CONTRACT.md
```

Tasks:

- [ ] Create thin state schema.
- [ ] Create lane schema.
- [ ] Create `thin_state_service`.
- [ ] Create `lane_state_service`.
- [ ] Support active/parked lane states.
- [ ] Add admin probe route for lane snapshots.
- [ ] Ensure CAOS Care, CAOS Core, CAOS Connect can be represented as separate lanes.

Acceptance criteria:

- Active lane can be represented without hydrating unrelated lanes.
- Parked lane carries summary, constraints, next action, receipts.
- State packets remain small and inspectable.

## Phase 4 — Memory ranking, feedback, and anti-duplication scaffold

Goal: evolve memory from flat in-process atoms toward ranked, canonical, feedback-aware memory.

Source contracts:

```text
docs/MEMORY_RANKING_AND_CONTEXT_GOVERNOR_CONTRACT.md
docs/MEMORY_EVICTION_AND_ANTI_DUPLICATION_CONTRACT.md
docs/MEMORY_ARC_HYDRATION_CONTRACT.md
```

Tasks:

- [ ] Add canonical memory fields.
- [ ] Add ranking fields:
  - times_seen
  - times_confirmed
  - times_rejected
  - times_used_successfully
  - last_used_at
  - confidence
  - importance
  - context_budget_tier
- [ ] Create `memory_ranking_service`.
- [ ] Create `memory_feedback_service`.
- [ ] Create duplicate/canonicalization helper.
- [ ] Add reject/adopt/edit/reclassify actions.
- [ ] Add counter-memory support.
- [ ] Add possible transcription error state.

Acceptance criteria:

- Repeated equivalent memories consolidate instead of duplicating.
- Rejection reason can update future ranking/capture behavior.
- Memory inclusion can be explained by receipt.

## Phase 5 — Context sanity and transcription anomaly gate

Goal: prevent bad STT or context-breaking fragments from becoming memory, authority, or action.

Source contract:

```text
docs/MEMORY_ARC_HYDRATION_CONTRACT.md
```

Tasks:

- [ ] Create `context_sanity_service`.
- [ ] Create `transcription_anomaly_service`.
- [ ] Add suspicious fragment classification.
- [ ] Add handling for actor/name anomalies.
- [ ] Add handling for location/name corrections.
- [ ] Add receipt fields for sanity checks.
- [ ] Block authority/deployment/destructive changes when transcript confidence is suspect.

Acceptance criteria:

- `Conroe, Arkansas` can be marked as suspected STT error when stable context says Conway.
- Unknown actor insertion like `Ed` is not accepted as authority without confirmation.
- Sanity gate runs before memory write and high-risk actions.

## Phase 6 — Chat pipeline integration without provider calls

Goal: wire the local chat stub through the mature pre-LLM pipeline before real provider calls.

Tasks:

- [ ] Update `ChatOrchestrator` to call:
  - context sanity
  - thin state
  - lane state
  - memory relevance/ranking
  - sanitizer
  - prompt budget/context meter
  - ARC assembler
  - receipt service
- [ ] Keep provider_called false.
- [ ] Return local contract response with full diagnostic receipt.
- [ ] Add unit/smoke test for the pipeline.

Acceptance criteria:

- `/api/chat/turn` produces a receipt showing pre-LLM context composition.
- No provider calls occur.
- No persistence mutation occurs unless explicitly part of a test route.

## Phase 7 — Persistence boundary

Goal: replace temporary in-process memory with Mongo-backed repository interfaces while preserving testability.

Tasks:

- [ ] Define persistence repository interfaces.
- [ ] Add Mongo-backed memory store.
- [ ] Add thread store.
- [ ] Add receipt store.
- [ ] Add lane/state store.
- [ ] Preserve in-memory fallback for tests only.
- [ ] Add migration/seed plan.

Acceptance criteria:

- Memory survives process restart in configured environment.
- Thread and receipt records have stable IDs.
- Tests can still run without production Mongo.

## Phase 8 — Provider adapter lane

Goal: add real model calls only after context/accounting/receipt scaffolds exist.

Tasks:

- [ ] Create provider adapter interface.
- [ ] Add OpenAI adapter first unless Michael changes order.
- [ ] Add model selection policy hooks.
- [ ] Add cost/latency metadata.
- [ ] Add timeout/degraded-response handling.
- [ ] Add provider receipt.

Acceptance criteria:

- Provider call is optional/config-gated.
- Every provider call has receipt metadata.
- Failure does not break the whole platform silently.

## Phase 9 — Frontend shell

Goal: build app/public/admin shells only after backend state/context surfaces exist.

Tasks:

- [ ] Public landing shell.
- [ ] Auth shell.
- [ ] Chat shell.
- [ ] Admin shell.
- [ ] Context meter admin panel.
- [ ] Memory console shell.
- [ ] Lane manager shell.
- [ ] Receipt viewer shell.

Acceptance criteria:

- Frontend surfaces map directly to backend contracts.
- Admin-only tools are permission-gated.
- No public exposure of internal diagnostics.

## Phase 10 — Agent/work package system

Goal: support bounded specialist agents and work packages.

Source contracts:

```text
docs/MULTI_AGENT_WORKFORCE_CONTRACT.md
docs/AGENT_TEMPLATE_AND_GLOBAL_BIN_CONTRACT.md
```

Tasks:

- [ ] Work package schema.
- [ ] Agent lane schema.
- [ ] Tool permission schema.
- [ ] Budget/stop-condition schema.
- [ ] Receipt requirements.
- [ ] Checker/QA lane.

Acceptance criteria:

- Agent work cannot infer unlimited authority.
- Work package defines lane, files, forbidden actions, acceptance checks, stop conditions.

## Phase 11 — Cleanup/refactor pass

Goal: clean as we go, not after the project turns into sludge.

Tasks:

- [ ] Identify files over 200 lines.
- [ ] Flag files approaching 400 lines.
- [ ] Split only after behavior is covered.
- [ ] Remove obsolete scaffolds.
- [ ] Park useful but unused concepts in docs or backlog.
- [ ] Update troubleshooting vault and build status.

Acceptance criteria:

- No known code file exceeds 400 lines without explicit approval.
- No dead contract stubs pretending to be implementation.
- Build status is current.

## Immediate next work queue

The next safe actions are:

1. Update `docs/PHASE_CHECKLIST.md` to match actual current state.
2. Update `docs/BUILD_STATUS.md` with latest contracts.
3. Add root `AGENTS.md` for future agents.
4. Create context meter schemas/services.
5. Wire context meter into admin probe.

## Stop conditions

Stop before proceeding if:

- file creation would conflict with existing path
- route behavior is unclear
- implementation would require provider secrets
- implementation would require production deployment
- context contracts conflict
- Michael needs to approve phase order change
- line limits would be exceeded

## Non-negotiable

Build order matters.

CAOS must not skip ahead to provider calls, frontend polish, or agent autonomy before the context/memory/state/receipt foundation can explain what is happening and why.
