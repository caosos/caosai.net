# CAOS AI

**CAOS AI** is the CAOS core brain, server runtime, and governed AI orchestration platform. It is focused on persistent memory, tool-connected execution, multi-model inference routing, context hygiene, receipts, server-side orchestration, and practical workflow automation.

This repository is the owned Linode/server-target rebuild home for the CAOS platform. It exists to make the CAOS core understandable to humans, AI coding agents, collaborators, and technical reviewers without mixing in private CAOS Care product implementation details or sensitive operational data.

CAOS Care lives separately in [`caosos/CAOSCARE.COM`](https://github.com/caosos/CAOSCARE.COM). CAOS Care is the senior-care product surface. CAOS AI is the brain/platform layer that CAOS products may later consume through APIs and contracts.

Emergent and Base44 builds are prototype/reference sources only. They are not the future deployment owners for this repo.

## Built For User-Owned AI

CAOS AI is built for privacy, personalization, and user-directed AI experience.

The goal is not a generic chatbot that forgets who you are every session. The goal is an AI workbench that can get to know the user, adapt to the user, and remain governed by the user.

Core product principles:

- **Your memory is yours.** CAOS memory is designed around user-owned context, not hidden data harvesting.
- **Your AI should know you because you allow it to.** Personalization should be explicit, inspectable, correctable, and removable.
- **Your experience should be customized to you and by you.** The user should control preferences, memory, models, tools, voice, workflows, and boundaries.
- **Use the model that fits the job.** CAOS is designed for multi-provider inference and future model routing instead of locking every task to one model.
- **Context should be governed.** Relevant context should be hydrated when useful, sanitized when needed, and backed by receipts.
- **Tools need rules.** File, repo, connector, MCP, and agent actions should be permissioned, visible, and auditable.

In short:

```text
Your memory.
Your models.
Your tools.
Your rules.
```

## Start Here

If you are new to the project, start in this order:

1. [`docs/CAOS_PUBLIC_OVERVIEW.md`](docs/CAOS_PUBLIC_OVERVIEW.md) — plain-English overview.
2. [`docs/PRODUCT_BOUNDARY.md`](docs/PRODUCT_BOUNDARY.md) — boundary between CAOS AI and CAOS Care.
3. [`docs/ENGINEERING_WORKFLOW.md`](docs/ENGINEERING_WORKFLOW.md) — AI-agent/Codex/GitHub/Linode workflow.
4. [`docs/MIGRATION_SOURCES.md`](docs/MIGRATION_SOURCES.md) — prototype/source/salvage map.
5. [`docs/BUILD_STATUS.md`](docs/BUILD_STATUS.md) — current rebuild/server status.
6. [`docs/VISUAL_EVIDENCE_MANIFEST.md`](docs/VISUAL_EVIDENCE_MANIFEST.md) — what the working prototype looks like and does.
7. [`docs/ARCHITECTURE_CONCEPTS.md`](docs/ARCHITECTURE_CONCEPTS.md) — memory bins, hydration, receipts, model routing, worker agents, MCP, sandbox lane.
8. [`docs/PUBLIC_ROADMAP.md`](docs/PUBLIC_ROADMAP.md) — public rebuild roadmap.
9. [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to give feedback or build from the project.

## Current Status

CAOS AI is not being presented as a finished commercial platform. It is an active migration, rebuild, and consolidation effort based on earlier prototypes.

The current source references are:

- [`caosos/emergent-caos-build`](https://github.com/caosos/emergent-caos-build) — full-stack prototype/source/salvage implementation.
- [`caosos/caos-os-A1`](https://github.com/caosos/caos-os-A1) — earlier Base44 prototype/reference implementation.
- [`caosos/CAOSCARE.COM`](https://github.com/caosos/CAOSCARE.COM) — separate CAOS Care product repo.
- This repository — CAOS AI server/core runtime repo for owned Linode/server work.

This repo was formerly named `caosos/linode-repo`. That name is historical only.

## What CAOS AI Is Trying To Do

CAOS AI explores the idea that modern AI systems should not only answer questions. They should operate inside a governed workbench with:

- memory that is structured instead of dumped into one long conversation;
- user-owned personalization;
- tool access that is visible, permissioned, and receipt-backed;
- model routing that uses cheaper models for bounded work and stronger models for harder synthesis;
- context hydration that pulls the right information at the right time;
- sanitation and compression that preserve raw source records while keeping active context affordable;
- explicit learning rather than silent mutation;
- agent workflows that can inspect, plan, execute, validate, and stop cleanly;
- server runtime discipline suitable for owned infrastructure.

## Core Runtime Concept

```text
User request
  -> CAOS AI orchestrator
  -> relevant memory bins
  -> tool / MCP / repo / file access
  -> model routing
  -> bounded worker agents where useful
  -> receipts and validation
  -> final response / workflow action
```

The long-term direction is a governed AI operating layer that can support software work, administrative workflows, device-connected workflows, and domain-specific products.

## CAOS Care Boundary

CAOS Care is the first major product direction planned around the CAOS architecture. It is focused on senior-care and assisted-living workflows: resident requests, staff support, care-plan documentation, alerts, reminders, wearable or pendant-style interaction, and workflow routing.

CAOS Care is intentionally separate from this repo. CAOS Care should consume CAOS AI services through defined APIs/contracts rather than absorbing the whole CAOS core.

The public concept is documented in [`docs/CAOSCARE_PRODUCT_PREVIEW.md`](docs/CAOSCARE_PRODUCT_PREVIEW.md). Private CAOS Care implementation code belongs in [`caosos/CAOSCARE.COM`](https://github.com/caosos/CAOSCARE.COM), not here.

## Public Documentation

- [`docs/CAOS_PUBLIC_OVERVIEW.md`](docs/CAOS_PUBLIC_OVERVIEW.md)
- [`docs/PRODUCT_BOUNDARY.md`](docs/PRODUCT_BOUNDARY.md)
- [`docs/ENGINEERING_WORKFLOW.md`](docs/ENGINEERING_WORKFLOW.md)
- [`docs/MIGRATION_SOURCES.md`](docs/MIGRATION_SOURCES.md)
- [`docs/BUILD_STATUS.md`](docs/BUILD_STATUS.md)
- [`docs/CAOSCARE_PRODUCT_PREVIEW.md`](docs/CAOSCARE_PRODUCT_PREVIEW.md)
- [`docs/ARCHITECTURE_CONCEPTS.md`](docs/ARCHITECTURE_CONCEPTS.md)
- [`docs/PUBLIC_ROADMAP.md`](docs/PUBLIC_ROADMAP.md)
- [`docs/VISUAL_EVIDENCE_MANIFEST.md`](docs/VISUAL_EVIDENCE_MANIFEST.md)
- [`SECURITY.md`](SECURITY.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Working Rules

- No production deploy without Michael approval.
- No private care-product implementation details in this public repo.
- No secrets, tokens, private resident/staff examples, or facility-specific data.
- Public claims must distinguish prototype, active rebuild, planned feature, and completed feature.
- AI agents inspecting this repo must read `AGENTS.md` before making changes.
- CAOS AI and CAOS Care must remain separate products in the same ecosystem.

## License

This repository is released under the MIT License. See [`LICENSE`](LICENSE).

## Why This Exists

The agent-runtime space is moving quickly: coding agents, MCP-connected tools, E2B-style sandboxes, multi-agent workflows, model routing, and long-context systems are converging.

CAOS AI is an attempt to build a broader governed platform around those same primitives, with practical product use cases beyond coding alone.

Feedback is welcome, especially on user-owned memory, privacy-centered personalization, architecture, memory design, orchestration, cost-aware inference, safety boundaries, and product direction.
