# CAOS Linode Rebuild Contract

## Purpose

This repository is the clean, server-owned CAOS rebuild surface. `caosos/emergent-caos-build` is a behavioral reference only. The old server salvage branch is a reference/quarry only. Neither source is to be mirrored as a monolith.

## Non-negotiables

- No direct writes to `main`.
- No production deploy without Michael approval.
- No bulk-copying God files from Emergent, Base44, or legacy server code.
- Preserve behavior, contracts, receipts, diagnostics, memory, tools, connectors, support tickets, files, summaries, seeds, and admin boundaries.
- Target files should stay near 200–300 lines. 400 lines requires a clear reason.
- Orchestrators coordinate only; services own domain logic; adapters own external systems; policies own decisions; schemas own contracts.

## Source roles

| Source | Role |
|---|---|
| `caosos/emergent-caos-build` | Current working product behavior reference |
| `legacy-python-server-salvage-2026-05-01` | Old Python/memory salvage reference |
| `aria-emergent-clean-rebuild` | Clean destination branch |

## Build order

1. Foundation: config, logging, health, dev auth, runtime registry.
2. Chat spine: routes, schemas, orchestrator, receipt envelope.
3. Persistence: Mongo adapter plus explicit migration boundary for legacy SQLite concepts.
4. Memory: read path, write/promotion path, ambiguity gates.
5. Frontend: modular React surfaces with dev-auth testability.
6. Diagnostics and admin: server-side gated, never UI-only.
7. Provider/router/connectors: isolated adapters.

## Acceptance rule

A feature is not considered ported until it has: route/service/schema placement, visible behavior mapping, security boundary, receipt/error behavior, and a test or smoke path.
