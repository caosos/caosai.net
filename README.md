# CAOS

**CAOS** is an experimental governed AI orchestration platform focused on persistent memory, tool-connected execution, multi-model inference routing, context hygiene, receipts, and practical workflow automation.

This repository is the public clean-rebuild home for CAOS. It is intended to make the project understandable to humans, AI coding agents, collaborators, and technical reviewers without exposing private CAOSCare implementation details or sensitive operational data.

## Built For User-Owned AI

CAOS is built for privacy, personalization, and user-directed AI experience.

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
2. [`docs/VISUAL_EVIDENCE_MANIFEST.md`](docs/VISUAL_EVIDENCE_MANIFEST.md) — what the working prototype looks like and does.
3. [`docs/visual-reference/README.md`](docs/visual-reference/README.md) — visual-reference evidence rules.
4. [`docs/ARCHITECTURE_CONCEPTS.md`](docs/ARCHITECTURE_CONCEPTS.md) — memory bins, hydration, receipts, model routing, worker agents, MCP, sandbox lane.
5. [`docs/PUBLIC_ROADMAP.md`](docs/PUBLIC_ROADMAP.md) — public rebuild roadmap.
6. [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to give feedback or build from the project.

## Current Status

CAOS is not being presented as a finished commercial platform. It is an active rebuild and consolidation effort based on earlier prototypes.

The current public source references are:

- [`caosos/emergent-caos-build`](https://github.com/caosos/emergent-caos-build) — full-stack prototype/reference implementation.
- [`caosos/caos-os-A1`](https://github.com/caosos/caos-os-A1) — earlier Base44 prototype/reference implementation.
- This repository — clean server-target rebuild and public project home.

Private product work, including CAOSCare implementation details, remains separated.

## What CAOS Is Trying To Do

CAOS explores the idea that modern AI systems should not only answer questions. They should operate inside a governed workbench with:

- memory that is structured instead of dumped into one long conversation;
- user-owned personalization;
- tool access that is visible, permissioned, and receipt-backed;
- model routing that uses cheaper models for bounded work and stronger models for harder synthesis;
- context hydration that pulls the right information at the right time;
- sanitation and compression that preserve raw source records while keeping active context affordable;
- explicit learning rather than silent mutation;
- agent workflows that can inspect, plan, execute, validate, and stop cleanly.

## What The Prototype Already Explored

The existing CAOS prototype evidence includes:

- main chat shell;
- engine/mode controls;
- memory console;
- quick capture;
- admin dashboard/admin docs;
- support tickets;
- working context/window meter;
- previous-thread search;
- voice/speech settings;
- role-aware settings;
- connector/tool surfaces;
- visual operating references.

See [`docs/VISUAL_EVIDENCE_MANIFEST.md`](docs/VISUAL_EVIDENCE_MANIFEST.md) for the public visual/behavioral summary.

## Core Concepts

```text
User request
  -> orchestrator
  -> relevant memory bins
  -> tool / MCP / repo / file access
  -> model routing
  -> bounded worker agents where useful
  -> receipts and validation
  -> final response / workflow action
```

The long-term direction is a governed AI operating layer that can support software work, administrative workflows, device-connected workflows, and domain-specific products.

## CAOSCare Product Direction

CAOSCare is the first major product direction planned around the CAOS architecture. It is focused on senior-care and assisted-living workflows: resident requests, staff support, care-plan documentation, alerts, reminders, wearable or pendant-style interaction, and workflow routing.

CAOSCare is intended as an assistive response and workflow layer, not an autonomous medical decision-maker.

The public concept is documented in [`docs/CAOSCARE_PRODUCT_PREVIEW.md`](docs/CAOSCARE_PRODUCT_PREVIEW.md). Private CAOSCare implementation code is intentionally not published here.

## Public Documentation

- [`docs/CAOS_PUBLIC_OVERVIEW.md`](docs/CAOS_PUBLIC_OVERVIEW.md)
- [`docs/CAOSCARE_PRODUCT_PREVIEW.md`](docs/CAOSCARE_PRODUCT_PREVIEW.md)
- [`docs/ARCHITECTURE_CONCEPTS.md`](docs/ARCHITECTURE_CONCEPTS.md)
- [`docs/PUBLIC_ROADMAP.md`](docs/PUBLIC_ROADMAP.md)
- [`docs/VISUAL_EVIDENCE_MANIFEST.md`](docs/VISUAL_EVIDENCE_MANIFEST.md)
- [`docs/visual-reference/README.md`](docs/visual-reference/README.md)
- [`SECURITY.md`](SECURITY.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Working Rules

- No production deploy without Michael approval.
- No private care-product implementation details in this public repo.
- No secrets, tokens, private resident/staff examples, or facility-specific data.
- Public claims must distinguish prototype, active rebuild, planned feature, and completed feature.
- AI agents inspecting this repo should read the public docs before making claims.

## License

This repository is released under the MIT License. See [`LICENSE`](LICENSE).

## Why This Exists

The agent-runtime space is moving quickly: coding agents, MCP-connected tools, E2B-style sandboxes, multi-agent workflows, model routing, and long-context systems are converging.

CAOS is an attempt to build a broader governed platform around those same primitives, with practical product use cases beyond coding alone.

Feedback is welcome, especially on user-owned memory, privacy-centered personalization, architecture, memory design, orchestration, cost-aware inference, safety boundaries, and product direction.
