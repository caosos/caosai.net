# Documentation Index

## Purpose

Documentation is part of the CAOS product, not an afterthought. The rebuild must remain understandable, transferable, inspectable, and recoverable by future agents and humans.

This index is the starting point for anyone entering the build.

## Read order for replacement agents

1. `docs/BUILD_STATUS.md`
2. `docs/REBUILD_CONTRACT.md`
3. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
4. `docs/SOURCE_TO_TARGET_MAP.md`
5. `docs/EMERGENT_DOCUMENTATION_LEDGER.md`
6. `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`
7. `docs/PORTABILITY_MATRIX.md`
8. `docs/SALVAGE_POLICY.md`
9. `docs/ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md`
10. `docs/MEMORY_ARC_HYDRATION_CONTRACT.md`
11. `docs/WCW_ENGINE_CONTEXT_CONTRACT.md`
12. `docs/RECEIPT_EVERYWHERE_CONTRACT.md`
13. `docs/PHASE_CHECKLIST.md`
14. `docs/LOCAL_SMOKE_TEST.md`

## Documentation groups

### Build continuity

- `BUILD_STATUS.md` — current branch, phase, completed work, next work.
- `BUILD_DECISIONS_AND_INCIDENTS.md` — decisions, corrections, hazards, incidents.
- `PHASE_CHECKLIST.md` — phase completion and exit criteria.

### Architecture contracts

- `REBUILD_CONTRACT.md` — master rebuild rules and module doctrine.
- `SOURCE_TO_TARGET_MAP.md` — source behavior to clean target modules.
- `PORTABILITY_MATRIX.md` — portable Ubuntu/Linode runtime assumptions.
- `SALVAGE_POLICY.md` — when old code can/cannot be reused.

### Product behavior evidence

- `BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` — visible product surfaces from screenshots.
- `EMERGENT_DOCUMENTATION_LEDGER.md` — source documentation intake and rules.

### Runtime/product contracts

- `ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md` — Aria behavior, proactivity, truth, speed.
- `MEMORY_ARC_HYDRATION_CONTRACT.md` — WCW/ARC/memory/hydration/sanitization doctrine.
- `WCW_ENGINE_CONTEXT_CONTRACT.md` — model-specific working context requirements.
- `RECEIPT_EVERYWHERE_CONTRACT.md` — receipt requirements for every meaningful action.

### Validation

- `LOCAL_SMOKE_TEST.md` — commands for local backend validation.

## Documentation maintenance rule

When the build changes direction, adds a major capability, hits an architectural issue, or makes a correction, update documentation in the same phase.

A future builder should not need to reconstruct intent from chat history.

## Non-negotiable

Undocumented architecture becomes operational debt. If it matters, document it.
