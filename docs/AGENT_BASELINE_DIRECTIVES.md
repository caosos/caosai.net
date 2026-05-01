# Agent Baseline Directives

## Purpose

Every agent working on the CAOS rebuild must follow the same baseline operating discipline, then apply its lane-specific build direction on top.

The goal is military/company-grade departmentalization: shared doctrine, bounded lanes, documented handoffs, and orchestrated integration.

## Core operating doctrine

All agents must obey:

1. Read required documentation before writing.
2. Stay inside assigned lane and branch.
3. Do not edit shared files unless explicitly assigned by the orchestrator.
4. Record crosswire needs instead of patching shared files casually.
5. Produce receipts for meaningful changes.
6. Update lane-relevant documentation in the same phase as code changes.
7. Preserve screenshot/photo provenance when using visual evidence.
8. Preserve behavior intent from Emergent and Base44 references without copying Base44 code.
9. Avoid God files and monolith reconstruction.
10. Stop and report when scope, authority, or source evidence becomes unclear.

## Required read order

Before writing, every agent must read:

1. `docs/DOCUMENTATION_INDEX.md`
2. `docs/BUILD_STATUS.md`
3. `docs/REBUILD_CONTRACT.md`
4. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
5. `docs/PARALLEL_AGENT_WORKFLOW.md`
6. `docs/CROSSWIRE_INTEGRATION_LEDGER.md`
7. `docs/SOURCE_TO_TARGET_MAP.md`
8. Its lane-specific assignment document

## Screenshot/photo provenance requirement

Any agent using screenshots, photos, UI captures, or visual references must document:

- reference ID
- origin
- screen/feature area
- reference type: visual, behavior, or both
- what the image proves
- what should be preserved
- what should be changed
- difference vs Base44, if relevant
- difference vs Emergent, if relevant
- target requirement
- acceptance criteria

No image may be treated as generic inspiration if it is being used to justify implementation.

## TSV/source log rule

If Michael provides TSV logs, screenshots, notes, support tickets, or historical build records, agents must treat them as build evidence.

Agents must not assume they have seen all prior evidence. If evidence is referenced but unavailable, mark the requirement as pending source review rather than inventing details.

## Shared directives for all lanes

### Receipts

Every meaningful action must produce or update a receipt trail.

### Memory and retrieval

Search and memory behavior must not rely on exact string matching only. Retrieval should support partial, fuzzy, semantic, and context-aware matching as the system matures.

### UI references

Base44 and Emergent are reference origins, not universal targets.

- Base44 may be used as a visual reference.
- Emergent may be used as visual and behavior reference.
- Neither should be copied blindly.
- Final CAOS implementation must document intentional divergence.

### Risk gates

Approval is required for destructive changes, production deployments, main-branch merges, financial actions, legal commitments, secret exposure/rotation, and external messages sent as the user.

Low-risk documentation, receipts, local lane work, and reversible build progress may proceed inside authorized scope.

## Lane handoff requirement

Each agent must finish a work session with a handoff note containing:

- branch name
- lane name
- files changed
- commits made
- behavior added
- docs updated
- crosswire requests created
- tests/smoke checks run or pending
- unresolved issues
- next recommended action

## Non-negotiable

Agents do not operate from memory alone. They operate from documented evidence, lane contracts, receipts, and orchestrator-managed integration.
