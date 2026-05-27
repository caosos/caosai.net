# Contracts Table of Contents

## Purpose

This document is the front-of-book table of contents for CAOS rebuild contracts. It tells builders, agents, and future maintainers where each rule lives and what question each contract answers.

No future builder should need Michael to re-explain system behavior that is already documented here.

## How to use this book

Read in this order when entering the project:

1. Orientation and current status.
2. Build governance and agent rules.
3. Source/reference evidence.
4. Architecture and runtime contracts.
5. Product behavior contracts.
6. Public launch, discoverability, analytics, and trust contracts.
7. Validation, troubleshooting, and regression controls.
8. Lane-specific implementation docs.

## Chapter 1 — Orientation

| Contract | Purpose |
|---|---|
| `docs/START_HERE_AGENT_ONBOARDING.md` | First-read onboarding guide for future agents. |
| `docs/DOCUMENTATION_INDEX.md` | Master documentation index and read order. |
| `docs/BUILD_STATUS.md` | Current branch, phase, completed work, next work, and not-built-yet list. |
| `docs/PHASE_CHECKLIST.md` | Phase completion criteria and exit gates. |
| `docs/LOCAL_SMOKE_TEST.md` | Local backend smoke-test commands and expected results. |
| `docs/SYSTEM_BLUEPRINT.md` | System introduction, safe designer biography, platform philosophy, and long-term direction. |

## Chapter 2 — Build Governance

| Contract | Purpose |
|---|---|
| `docs/REBUILD_CONTRACT.md` | Master rebuild rules: clean rebuild, no monolith, no Base44 dependency, no main writes. |
| `docs/BUILD_DECISIONS_AND_INCIDENTS.md` | Decisions, corrections, mistakes, hazards, and replacement-agent rules. |
| `docs/AGENT_BASELINE_DIRECTIVES.md` | Required baseline behavior for every agent. |
| `docs/PARALLEL_AGENT_WORKFLOW.md` | How multiple agents work in bounded lanes. |
| `docs/CROSSWIRE_INTEGRATION_LEDGER.md` | How agents request shared-file wiring without editing shared files randomly. |
| `docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md` | How accepted features become locked and protected from regressions. |
| `docs/BUILD_PARTNERSHIP_STATEMENT.md` | Defines Michael/AI colleague build-partner doctrine. |

## Chapter 3 — Source Evidence and Provenance

| Contract | Purpose |
|---|---|
| `docs/SOURCE_TO_TARGET_MAP.md` | Maps source behavior and legacy salvage to clean target modules. |
| `docs/EMERGENT_DOCUMENTATION_LEDGER.md` | Ensures Emergent documentation is inspected before rebuilding major lanes. |
| `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` | Preserves observed behavior and origin distinctions from screenshots. |
| `docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md` | Defines Base44/Emergent visual behavior references and frontend acceptance rules. |
| `docs/SALVAGE_POLICY.md` | Defines what may be salvaged, inspected, or excluded. |
| `docs/TROUBLESHOOTING_VAULT.md` | Stores solved problems, failed attempts, fixes, and prevention rules. |

## Chapter 4 — Runtime and Portability

| Contract | Purpose |
|---|---|
| `docs/PORTABILITY_MATRIX.md` | Defines how CAOS runs outside Emergent/Base44 assumptions. |
| `docs/WCW_ENGINE_CONTEXT_CONTRACT.md` | Defines model-specific WCW behavior and UI display requirements. |
| `docs/RECEIPT_EVERYWHERE_CONTRACT.md` | Requires receipts for every meaningful system action. |
| `docs/LOCAL_MODEL_HOSTING_AND_COST_STRATEGY.md` | Defines cloud/local model hosting, cost, latency, and routing strategy. |
| `docs/AGENTIC_PLATFORM_REQUIREMENT.md` | Defines authorized agentic work mode and provider-native capability doctrine. |
| `docs/AGENT_PLAYGROUND_AND_HERMES_EVALUATION_CONTRACT.md` | Defines bounded agent playground work, Hermes-like runtime evaluation, sandbox contracts, security risks, tool economy, and Codex bridge direction. |

## Chapter 5 — Aria Behavior and Intelligence

| Contract | Purpose |
|---|---|
| `docs/ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md` | Defines Aria's personality, proactivity, truth discipline, and latency doctrine. |
| `docs/MEMORY_ARC_HYDRATION_CONTRACT.md` | Defines memory, ARC, WCW, hydration, sanitization, summaries, and truth-machine behavior. |
| `docs/SEARCH_AND_RETRIEVAL_BEHAVIOR_CONTRACT.md` | Defines fuzzy, partial, body, metadata, semantic, and ranked retrieval expectations. |
| `docs/FUTURE_MACHINE_INTERFACE_VISION.md` | Captures the long-term machine/HMI/PLC guidance vision. |

## Chapter 6 — Frontend and Visual Behavior

| Contract | Purpose |
|---|---|
| `docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md` | Defines starfield, translucency, menus, scroll behavior, settings, thread search, and visual reference rules. |
| `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` | Ties screenshots to observable behavior, feature inventory, and implementation implications. |
| `docs/PUBLIC_DISCOVERABILITY_SEO_CONTRACT.md` | Defines public crawlable pages, metadata, sitemap, robots, and app-gated feature descriptions. |

## Chapter 7 — Public Launch, Trust, and Analytics

| Contract | Purpose |
|---|---|
| `docs/PUBLIC_DISCOVERABILITY_SEO_CONTRACT.md` | Ensures CAOS is publicly understandable even when app features are login-gated. |
| `docs/PRIVACY_RESPECTING_ANALYTICS_CONTRACT.md` | Defines product-metric analytics with no ad-surveillance, no selling user data, and no third-party behavioral profiling. |

## Chapter 8 — Validation and Regression

| Contract | Purpose |
|---|---|
| `docs/LOCAL_SMOKE_TEST.md` | Verifies current backend routes and receipts from real checkout. |
| `docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md` | Prevents re-breaking accepted TTS/STT/UI/memory/WCW behaviors. |
| `docs/TROUBLESHOOTING_VAULT.md` | Prevents repeated fixes for the same problem. |

## Required builder rule

Before writing code, a builder must identify which chapter applies to the work and read the relevant contracts.

If a feature behavior is not documented, the builder must document it before or during implementation. If source evidence is missing, mark it pending source review instead of inventing behavior.

## Non-negotiable

The contracts are the book. The code is the implementation. If the book and code disagree, stop, identify the mismatch, and correct either the contract or the code with a receipt.
