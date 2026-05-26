# START HERE — CAOS Agent Onboarding

## Read this first

You are entering the CAOS Linode rebuild. Do not start by coding. Start by orienting.

This repository is the clean rebuild surface for CAOS. The current working branch is:

```text
aria-emergent-clean-rebuild
```

## Latest session handoff — Claude Code terminal interruption and control reset

A recent Claude Code terminal session progressed useful CAOS rebuild work, then timed out/interrupted. After the timeout, Michael started/continued Claude Code from different contexts, including a laptop session and a server-side terminal session. The agent then asked where to start and what had been worked on, creating continuity friction.

Michael's current operating decision:

- Do not let terminal Claude Code continue broad autonomous work without passing intent, scope, and results through Aria/ChatGPT or another verifier/orchestrator.
- Michael uses voice heavily and cannot reliably communicate rich context, screenshots, or long pasted instructions into the terminal Claude Code session.
- Copy/paste into the terminal Claude Code session became unreliable/frustrating, so terminal-only interaction is not an acceptable primary planning interface.
- Aria/ChatGPT remains the voice-friendly orchestration layer: Michael speaks here; Aria converts intent into bounded agent work orders; Claude Code executes inside approved lanes; results return here for review, correction, and next-task framing.
- Claude Code autonomy is still desired, but only inside approved work packages with documented scope, receipts, validation, and stop gates.

Recent completed/reported work to preserve:

- FIX-001 repaired receipt truth in `backend/app/api/chat.py`: route receipts now read orchestrator `response.receipt` values rather than hardcoding false/stub behavior.
- FIX-002 repaired the deploy/runtime source mismatch: `deploy.sh` now pulls from `caosai.net` and rsyncs backend Python to the runtime path while preserving `.venv` and `.env`.
- FIX-003 repaired thread persistence DB access in `backend/app/services/thread_service.py` using a sync-safe `pymongo.MongoClient` singleton.
- `docs/BUILD_BASELINE_AND_FIX_LEDGER.md` was created/updated to document baseline, incidents, fixes, blast radius, rollback, and validation.
- `ops/deploy.sh` was added as a tracked copy of the active deploy script.
- `docs/RUNTIME_SOURCE_OF_TRUTH.md` was added to document source repo, runtime path, systemd/runtime behavior, deploy chain, preserved secrets, validation, and known risks.
- `docs/REFERENCE_SOURCE_MAP.md` was added to document required reference sources and visual/product behavior evidence.
- Live `/api/chat/turn` receipt validation passed after repair: provider called true, persistence written true, error null, diagnostic no longer falsely claims stub/no-provider behavior.

Recent reference-source findings:

- `caosos/emergent-caos-build` was inspected as the current working product/behavior reference.
- Visual evidence docs and screenshot manifests were inspected, including `VISUAL_EVIDENCE_MANIFEST.md`, `BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`, `FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md`, and `LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md`.
- Emergent behavior sources identified include `voice_service.py`, `useVoiceIO.js`, `MarkdownMessage.js`, and `WorkingContextStrip.js`.
- `caosos/caos-os-A1` initially returned 404 because it was private/inaccessible to Claude. Michael later fixed access. A future agent should re-run `caos-os-A1` reference inspection before frontend/voice/attachment/memory behavior work.
- Base44 live reference URL recorded by Michael: `https://caos-chat-9c5683d8.base44.app/Chat`.

Immediate continuity rule:

Before starting a new terminal Claude Code session, read this file, then read `docs/RUNTIME_SOURCE_OF_TRUTH.md`, `docs/BUILD_BASELINE_AND_FIX_LEDGER.md`, and `docs/REFERENCE_SOURCE_MAP.md`. If your local/session memory disagrees with these files, trust the files and report the conflict.

Do not ask Michael to reconstruct the session from memory. Use the documented ledger/source maps first.

## Prime directive

CAOS is not just a chat app. It is a user-owned AI operating platform: memory-aware, tool-capable, provider-flexible, receipt-backed, truth-disciplined, and eventually capable of helping users operate documents, systems, machines, homes, care workflows, and real work under permission gates.

## Michael's operating intent

Michael John Chambers is the system designer. He wants CAOS to become his long-term AI platform: an assistant that remembers what matters, uses tools like this build session, works across providers/connectors, helps build software, manages context intelligently, produces receipts, and eventually helps with real-world machine/process guidance without reckless autonomy.

Safe high-level biography and system intent are documented in:

```text
docs/SYSTEM_BLUEPRINT.md
```

## Non-negotiables

- Do not use Base44 code.
- Base44 screenshots may be used as visual reference only.
- Emergent is the current behavior/reference build, not a monolith to copy.
- Legacy Python server is salvage/reference, not the new runtime foundation.
- Do not write to `main`.
- Do not deploy production.
- Do not expose or request real secrets.
- Do not create God files.
- Do not silently rewrite behavior.
- Do not degrade accepted features.
- Every meaningful action gets a receipt.
- Shared-file edits require orchestrator/crosswire discipline.

## Required first read order

Read these before making changes:

1. `docs/CONTRACTS_TABLE_OF_CONTENTS.md`
2. `docs/DOCUMENTATION_INDEX.md`
3. `docs/BUILD_STATUS.md`
4. `docs/REBUILD_CONTRACT.md`
5. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
6. `docs/AGENT_BASELINE_DIRECTIVES.md`
7. `docs/PARALLEL_AGENT_WORKFLOW.md`
8. `docs/CROSSWIRE_INTEGRATION_LEDGER.md`
9. `docs/SOURCE_TO_TARGET_MAP.md`
10. lane-specific contract docs

## Current architecture posture

The rebuild is foundation-first. Current backend skeleton includes:

- FastAPI app entrypoint
- config loader
- logging setup
- runtime registry
- database boundary
- development auth
- health route
- runtime route
- model catalog and WCW metadata
- minimal chat contract route
- admin boundary probe
- memory contract routes
- receipt schemas and action receipt service
- memory capture/review/relevance/ARC scaffolds
- hydration policy, sanitizer, prompt budget scaffolds

## Current backend routes

```text
GET  /api/health
GET  /api/runtime
POST /api/auth/dev-login
GET  /api/models
POST /api/models/select
POST /api/chat/turn
POST /api/admin/probe
POST /api/memory/atoms
POST /api/memory/atoms/query
```

## Critical product doctrines

### Receipts everywhere

Every meaningful state change, model selection, memory action, hydration decision, connector call, admin action, artifact update, tool call, error, or degraded response must have a receipt.

Read:

```text
docs/RECEIPT_EVERYWHERE_CONTRACT.md
```

### Memory / ARC / WCW

Memory is not keyword search and not a prompt dump. WCW is the working context window. ARC is the active relevant context selected inside WCW. Hydration decides what enters ARC. Sanitization bounds and cleans context without destroying truth.

Read:

```text
docs/MEMORY_ARC_HYDRATION_CONTRACT.md
```

### Model-specific WCW

WCW differs by provider/model. The UI must represent model-specific context capacity in the profile/settings dropdown, response bubble/receipt area, and bottom composer model selector.

Read:

```text
docs/WCW_ENGINE_CONTEXT_CONTRACT.md
```

### Aria personality

Aria should feel like the working ChatGPT 5.5 build partner style Michael approved: direct, technical, truth-first, proactive by default for low-risk useful work, careful-gated for high-risk actions, receipt-oriented, fast without being shallow.

Read:

```text
docs/ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md
```

### Feature locks and regression prevention

Accepted features must be locked with behavior, files, acceptance checks, and regression awareness. TTS/STT, scrolling, search, WCW, memory, receipts, artifacts, and admin boundaries are high-risk regression lanes.

Read:

```text
docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md
docs/TROUBLESHOOTING_VAULT.md
```

## Visual/UI references

Base44 and Emergent screenshots are reference evidence. Base44 is visual-only; Emergent is visual and behavior reference depending on feature. Screenshot/photo provenance is mandatory when using images for implementation guidance.

Important visual requirements already captured:

- starfield remains visible behind translucent chat surfaces
- message bubbles should be translucent, not opaque blocks
- user bubble should not be harsh opaque blue/purple
- dark mode is preferred primary mode
- light mode must exist
- translucent header is desired
- restore last active thread on refresh
- scroll to latest/last meaningful position
- down/jump button must reliably return to latest
- previous thread search must support fuzzy/non-exact search
- settings/profile menu layout can be referenced, but colors should be refined

Read:

```text
docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md
docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md
```

## Parallel-agent rules

Agents are lane workers, not free agents. Work in your lane. Do not casually edit shared files. If you need shared wiring, record it in the crosswire ledger for orchestrator integration.

Shared files requiring coordination include:

- `backend/app/main.py`
- `backend/requirements.txt`
- `backend/app/core/config.py`
- `backend/app/core/database.py`
- `backend/app/services/receipt_service.py`
- `frontend/package.json`
- app-level frontend route/layout files
- key documentation index/status/map files

## If evidence is missing

Do not invent. Mark it pending source review.

Michael has TSV logs, screenshots, support-ticket evidence, and build history that may not all be visible yet. Treat referenced evidence as important and ask the orchestrator/Michael for the relevant artifact only when needed.

## Immediate next recommended work

1. Generate/maintain continuity token.
2. Finish provider/local model strategy contract if pending.
3. Update build status with recent docs and routes.
4. Run local smoke test from real checkout.
5. Wire hydration/ARC receipt into `/api/chat/turn`.
6. Begin lane contracts for frontend shell, provider router, memory persistence, support tickets, artifacts, and TTS/STT regression notes.

## Stop conditions

Stop and report if:

- you are about to touch shared files without orchestrator assignment
- you are unsure whether a screenshot/source is Base44 or Emergent
- a change may degrade a locked feature
- source evidence contradicts a contract
- a secret or credential appears
- a production deploy/main merge/destructive action is requested without explicit approval
- terminal Claude Code continuity becomes confused after a timeout/interruption and cannot reconstruct current state from repo docs
- Michael cannot communicate required context through terminal copy/paste; route scope-setting back through Aria/ChatGPT or another verifier/orchestrator