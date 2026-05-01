# Emergent Documentation Ledger

## Purpose

The Emergent repository already contains documentation that must be treated as migration input, not forgotten context. This ledger preserves the rule that source documentation is evidence for the rebuild.

## Primary documented source map

`caosos/emergent-caos-build/docs/REPO_MAP.md` is the first authoritative navigation document inspected for this rebuild.

It documents:

- Top-level repo layout: `backend/`, `frontend/`, `memory/`, `tests/`, `test_reports/`, `docs/`.
- Primary chat orchestration file: `backend/app/services/chat_pipeline.py`.
- Context and memory service cluster.
- Hydration, proactivity, and surface-awareness policies.
- TurnTrace, latency receipts, token meter, and artifact builder.
- Runtime/model selection services.
- Tools and connector likely locations.
- Support ticket, diagnostics, and admin areas.
- Frontend search targets and visible UI strings.
- Admin-vs-user boundaries.
- Recommended future extraction targets.

## Documentation handling rule

Before rebuilding any major lane, inspect the relevant Emergent docs first when they exist.

Required migration sequence per lane:

1. Read source docs and repo maps.
2. Inspect source implementation files.
3. Compare with screenshot behavior ledger.
4. Update `SOURCE_TO_TARGET_MAP.md` if needed.
5. Build clean target modules.
6. Record receipts/commits.

## Known source documentation inputs

| Source doc | Migration use |
|---|---|
| `docs/REPO_MAP.md` | Primary source repo navigation and extraction guidance |
| Emergent docs under `docs/` | Architecture and feature behavior evidence |
| Admin docs visible in CAOS UI | Product/domain behavior evidence |
| Screenshot behavior snapshot | UI/behavior parity evidence |
| Legacy Python salvage docs | Memory/session/kernel salvage evidence |

## Current warning

GitHub connector code search can return false negatives. Failed search does not prove a document is absent. Prefer direct known-path fetches and source repo maps when available.

## Immediate extraction targets from source docs

The following lanes must be mapped from docs before code porting:

- Chat pipeline orchestration.
- Context and memory.
- Hydration policy.
- Proactivity policy.
- Surface registry.
- TurnTrace and latency receipts.
- Artifact builder.
- Runtime/model selection.
- Tools/connectors.
- Support tickets.
- Admin diagnostics.
- Frontend chat shell and admin surfaces.
