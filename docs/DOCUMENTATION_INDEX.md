# Documentation Index

## Purpose

Documentation is part of the CAOS product, not an afterthought. The rebuild must remain understandable, transferable, inspectable, and recoverable by future agents and humans.

This index is the starting point for anyone entering the build.

## Read order for replacement agents

1. `docs/START_HERE_AGENT_ONBOARDING.md`
2. `docs/CONTRACTS_TABLE_OF_CONTENTS.md`
3. `docs/BUILD_STATUS.md`
4. `docs/REBUILD_CONTRACT.md`
5. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
6. `docs/AGENT_BASELINE_DIRECTIVES.md`
7. `docs/PARALLEL_AGENT_WORKFLOW.md`
8. `docs/CROSSWIRE_INTEGRATION_LEDGER.md`
9. `docs/SOURCE_TO_TARGET_MAP.md`
10. `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`
11. `docs/LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md`
12. lane-specific contract docs

## Documentation groups

### Build continuity

- `START_HERE_AGENT_ONBOARDING.md` — first-read onboarding guide for agents entering the rebuild.
- `CONTRACTS_TABLE_OF_CONTENTS.md` — front-of-book guide to the contract stack.
- `BUILD_STATUS.md` — current branch, phase, completed work, next work.
- `BUILD_DECISIONS_AND_INCIDENTS.md` — decisions, corrections, hazards, incidents.
- `PHASE_CHECKLIST.md` — phase completion and exit criteria.
- `LOCAL_SMOKE_TEST.md` — commands for local backend validation.

### Architecture contracts

- `REBUILD_CONTRACT.md` — master rebuild rules and module doctrine.
- `SOURCE_TO_TARGET_MAP.md` — source behavior to clean target modules.
- `PORTABILITY_MATRIX.md` — portable Ubuntu/Linode runtime assumptions.
- `SALVAGE_POLICY.md` — when old code can/cannot be reused.
- `AGENTIC_PLATFORM_REQUIREMENT.md` — agentic work mode and native capability doctrine.
- `AGENT_PLAYGROUND_AND_HERMES_EVALUATION_CONTRACT.md` — bounded agent playground, Hermes-like substrate evaluation, sandbox, security, Codex bridge, and tool-economy doctrine.
- `HERMES_AGENT_INTEGRATION_EVALUATION.md` — Hermes Agent evaluation, CAOS governance constraints, risk register, and phased adapter boundary plan.
- `LOCAL_MODEL_HOSTING_AND_COST_STRATEGY.md` — cloud/local model hosting, cost, latency, and routing strategy.

### Agent and integration governance

- `AGENT_BASELINE_DIRECTIVES.md` — required baseline behavior for every agent.
- `PARALLEL_AGENT_WORKFLOW.md` — how multiple agents work in bounded lanes.
- `CROSSWIRE_INTEGRATION_LEDGER.md` — how agents request shared-file wiring without random cross-edits.
- `FEATURE_LOCK_AND_REGRESSION_CONTRACT.md` — how accepted features are protected from degradation.
- `TROUBLESHOOTING_VAULT.md` — solved problems, failed attempts, fixes, and prevention rules.

### Product behavior evidence

- `LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md` — detailed visual operating manual for the live Base44 and Emergent CAOS prototype systems; identifies proven surfaces, operating implications, and behavioral blanks for Michael to fill.
- `BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` — visible product surfaces and behavior evidence from screenshots.
- `EMERGENT_DOCUMENTATION_LEDGER.md` — source documentation intake and rules.
- `FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md` — visual/UI behavior contract from Base44 and Emergent references.
- `SEARCH_AND_RETRIEVAL_BEHAVIOR_CONTRACT.md` — concrete fuzzy/partial/semantic retrieval behavior.

### Runtime/product contracts

- `ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md` — Aria behavior, proactivity, truth, speed.
- `MEMORY_ARC_HYDRATION_CONTRACT.md` — WCW/ARC/memory/hydration/sanitization doctrine.
- `WCW_ENGINE_CONTEXT_CONTRACT.md` — model-specific working context requirements.
- `RECEIPT_EVERYWHERE_CONTRACT.md` — receipt requirements for every meaningful action.
- `AGENT_PLAYGROUND_AND_HERMES_EVALUATION_CONTRACT.md` — agent playground, sandbox contracts, visible tool-call/token accounting, Hermes-like evaluation boundaries, and Codex bridge direction.
- `HERMES_AGENT_INTEGRATION_EVALUATION.md` — Hermes runtime-candidate evaluation and non-executing CAOS adapter roadmap from H0 through H5.
- `FUTURE_MACHINE_INTERFACE_VISION.md` — future PLC/HMI/machine guidance vision.

### Public launch, discoverability, and trust

- `PUBLIC_DISCOVERABILITY_SEO_CONTRACT.md` — public crawlable pages, SEO, metadata, sitemap, app-gated feature descriptions.
- `PRIVACY_RESPECTING_ANALYTICS_CONTRACT.md` — privacy-safe product analytics, no ad-surveillance model.
- `SYSTEM_BLUEPRINT.md` — system introduction, safe designer biography, platform philosophy, and long-term direction.
- `BUILD_PARTNERSHIP_STATEMENT.md` — Michael/AI build-colleague doctrine.

## Documentation maintenance rule

When the build changes direction, adds a major capability, hits an architectural issue, or makes a correction, update documentation in the same phase.

A future builder should not need to reconstruct intent from chat history.

## Non-negotiable

Undocumented architecture becomes operational debt. If it matters, document it.
