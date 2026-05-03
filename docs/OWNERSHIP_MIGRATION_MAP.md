# CAOS Ownership Migration Map

## Purpose

This document defines the corrected ownership path for taking the already-working CAOS behavior out of hosted build-platform dependency and rebuilding it as clean, Michael-owned CAOS infrastructure.

This is not a from-zero product invention.

Michael has already built working CAOS systems on two external build platforms:

```text
1. Base44 / Deno serverless build reference
2. Emergent full-stack build reference
```

The current Linode lane is the third build. Its purpose is to produce the cleanest, most owned, most modular CAOS implementation to date.

## Active lane

```text
Lane: CAOS Core clean ownership rebuild
```

Do not mix this lane with CAOS Care migration unless Michael explicitly opens a CAOS Care work package.

## Corrected controlling doctrine

```text
Do not deploy emergent-caos-build as the runtime target.
Do not move the Emergent app as-is to Linode.
Do not clone monolithic hosted-platform runtime code into production.
Treat external platform builds as behavior/source evidence.
Build clean owned modules in linode-repo.
Wire clean modules through explicit orchestrators.
Receipt every meaningful decision and change.
```

The old direct-deploy doctrine is superseded.

## Source/reference repos

### Emergent full-stack reference

```text
Repository: caosos/emergent-caos-build
Clone URL: https://github.com/caosos/emergent-caos-build.git
Branch: main
Role: Working full-stack behavior/source reference
```

This repository contains working CAOS behavior, but it is not the runtime deployment target for this lane.

Use it to inspect:

- existing product behavior
- feature surfaces
- backend service responsibilities
- frontend component behavior
- route/API shape
- visual and interaction evidence
- data/model assumptions
- implementation hazards

Do not copy monoliths wholesale.

### Base44 / serverless reference

Base44 remains a visual, behavioral, and feature-inventory reference where relevant.

Use it to compare:

- starfield and glass layering behavior
- UI feature inventory
- menu/settings/user-flow behavior
- serverless-platform assumptions to avoid

Do not use Base44 code.

### Clean ownership target

```text
Repository: caosos/linode-repo
Branch: aria-emergent-clean-rebuild
Role: Clean CAOS Core rebuild target, doctrine source, modular implementation workspace, and future ownership runtime source
```

All durable clean CAOS Core architecture should be built here.

## Server target

Preferred future production/runtime directory:

```text
/srv/caosos.com
```

Do not place the clean CAOS Core runtime under:

```text
/home/michael-chambers/caos-a1
```

CAOS A1 is a separate legacy/project directory and must not be used as the parent for the self-hosted CAOS Core platform.

## Correct mental model

```text
Base44 build = serverless visual/behavior/feature reference
emergent-caos-build = full-stack working behavior/source reference
linode-repo = clean owned CAOS Core implementation target
/srv/caosos.com = future server runtime directory
```

## Migration principle

```text
Move behavior, not mess.
Preserve proven behavior.
Rebuild clean structure.
Wire through orchestrators.
Verify with receipts.
```

The goal is not to make a working copy of the Emergent build. The goal is to produce a cleaner third-generation CAOS build using the first two builds as evidence.

## Non-negotiable architecture rule

CAOS Core must be built from clean, isolated modules coordinated by explicit orchestrators.

Required pattern:

```text
inspect reference behavior
-> map responsibilities
-> define contract
-> build clean module
-> wire through orchestrator
-> validate route/UI behavior
-> receipt
-> stop or proceed to next bounded unit
```

Forbidden pattern:

```text
clone hosted-platform runtime
-> deploy monolith
-> patch around platform assumptions
-> call it owned
```

## Module extraction model

Reference source should be treated as a quarry for behavior contracts.

For each major source file or feature cluster, produce:

- source path
- observed responsibility
- required behavior
- clean target module(s)
- orchestrator boundary
- dependencies
- acceptance criteria
- what not to copy
- verification receipt

Example backend direction:

```text
chat pipeline behavior
-> context_sanity_service.py
-> thin_state_service.py
-> lane_state_service.py
-> memory_ranking_service.py
-> context_meter_service.py
-> provider_router.py
-> response_validator.py
-> receipt_writer.py
-> chat_orchestrator.py
```

Example frontend direction:

```text
chat shell behavior
-> AppShell
-> MessageList
-> Composer
-> ThreadSidebar
-> SettingsPanel
-> MemoryConsole
-> ContextMeterPanel
-> AdminDocsPanel
-> SupportTicketsPanel
```

The orchestrator coordinates. It must not become another God file.

## Phase 1 — Documentation and doctrine reconciliation

Goal: ensure the book matches Michael's corrected direction before additional build work.

Tasks:

1. Read the documented contract stack.
2. Identify docs that still imply direct Emergent runtime deployment.
3. Correct old doctrine to this clean rebuild model.
4. Record contradictions and supersessions where needed.
5. Do not claim a doc is verified unless it has been inspected or searched for the specific issue.

Acceptance checks:

- This document no longer instructs direct deployment of `emergent-caos-build`.
- Conflicting docs are either updated or explicitly marked pending correction.
- Replacement agents can distinguish reference repos from target runtime source.

## Phase 2 — Reference inventory

Goal: inspect the working reference systems without migrating monoliths.

Emergent source-reference targets include, subject to actual repo inspection:

- backend application entrypoints
- backend service files
- chat pipeline / context engine behavior
- continuity and memory behavior
- hydration/proactivity policy
- frontend shell/components
- admin/docs/support/memory/context-meter surfaces
- visual evidence and screenshots if present

For each inspected target, produce an extraction map rather than a direct copy plan.

## Phase 3 — Clean target module build

Goal: build owned CAOS Core modules in `linode-repo`.

Priority foundation:

- context meter
- thin state snapshot
- lane state manager
- memory ranking and anti-duplication
- context sanity / transcription anomaly gate
- receipt service
- chat orchestrator pre-provider pipeline
- persistence boundary
- provider adapters only after context/memory/state/receipt scaffolds are explainable

## Phase 4 — Validation and runtime ownership

Goal: validate clean modules locally, then prepare owned deployment only after the clean architecture is coherent.

Validation requirements:

- backend boot verified from real checkout
- route receipts verified
- context meter receipt verified
- memory/state behavior verified
- no hidden dependency on hosted-platform runtime
- no production secrets required for local validation
- no monolithic hosted-platform deployment masquerading as ownership

Deployment remains a separate approved action.

## Line and file policy

```text
Target: <= 200 lines per code file where practical
Hard cap: 400 lines unless Michael explicitly approves exception
Docs/contracts/vault files may be longer
```

No God files.

If a module approaches the hard cap, stop and map extraction before adding more behavior.

## Source integrity rule

Verification is binary.

Do not say a file, repo, behavior, route, screenshot, or feature is verified unless it has actually been inspected, executed, or otherwise source-confirmed for the specific claim.

Allowed labels:

- verified
- source-backed
- user-stated
- inferred
- unverified
- partially inspected
- pending inspection
- contradicted
- superseded

Forbidden framing:

```text
verified enough
good enough
probably fine
assume complete
```

There is no "enough" standard for core truth claims. A claim is verified for the stated scope or it is not.

## Current source confirmation

Michael confirmed the two active GitHub anchors:

```text
https://github.com/caosos/emergent-caos-build.git
https://github.com/caosos/linode-repo.git
```

Correct role assignment:

```text
emergent-caos-build = working full-stack reference
linode-repo = clean owned implementation target
```

## Non-negotiable

This is the third CAOS build generation.

The first two working platforms prove behavior and direction. The Linode build must not inherit avoidable hosted-platform contamination or monolithic structure.

The correct win is:

```text
clean owned CAOS Core modules
+ explicit orchestrators
+ receipts
+ context/memory/state governance
+ verified behavior parity where required
= best CAOS build to date
```
