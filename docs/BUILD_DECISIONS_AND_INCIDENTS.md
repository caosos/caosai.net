# Build Decisions and Incidents

## Purpose

This document prevents repeated mistakes. Every major decision, correction, connector issue, and migration hazard should be recorded here.

## Active decisions

### No Base44 dependency

Base44 code is excluded from the rebuild. It may remain historically archived elsewhere, but it is not a source for this clean Linode build.

### Emergent repo is reference only

`caosos/emergent-caos-build` is the current working behavior reference. It should be inspected for behavior, contracts, docs, and implementation evidence, but not bulk-copied.

### Legacy Python server is salvage only

Branch `legacy-python-server-salvage-2026-05-01` contains old Python/memory work. It is useful for concepts such as Plane B, session guards, and deterministic recall, but it is not the new runtime foundation.

### No production secrets in GitHub or chat

Only `.env.example` templates and config variable names go into the repo. Real secrets are supplied by Michael later on the server/deployment surface.

### Development auth is intentional

`/api/auth/dev-login` exists so the app can be tested without Emergent OAuth. It is not production security.

## Incidents and corrections

### Wrong remote risk

Old server repo remotes pointed to:

- `caosos/caos-os-A1.git`
- `caosos/caos-server-live.git`

Correction: old Python salvage was pushed to `caosos/linode-repo` branch `legacy-python-server-salvage-2026-05-01`, not to those old remotes.

### Git author missing

Server commit initially failed because Git user identity was missing.

Correction: local repo config was set to:

- name: `Michael Chambers`
- email: `michael-chambers@users.noreply.github.com`

### Runtime data almost staged

Legacy memory SQLite/data files were seen in staged output during salvage preparation.

Correction: runtime data was moved out of useful source and ignored. SQLite, WAL, SHM, JSONL, venvs, caches, and secrets are excluded.

### GitHub connector search false negatives

Connector code search returned no results for known existing content. Direct path fetch worked.

Correction: do not treat search miss as absence. Prefer docs/REPO_MAP.md and direct known-path fetches.

## Current known hazards

- Accidentally copying God files from Emergent.
- Accidentally recreating page/controller monoliths in frontend.
- Treating UI-hidden admin controls as security.
- Treating WCW meter as cosmetic instead of backend contract.
- Forgetting support tickets, artifacts, summaries, seeds, receipts, and connector surfaces.
- Allowing development auth into production configuration.
- Committing `.env`, database files, archives, venvs, or generated build outputs.

## Replacement-agent rule

A future agent must read, in this order:

1. `docs/BUILD_STATUS.md`
2. `docs/REBUILD_CONTRACT.md`
3. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
4. `docs/SOURCE_TO_TARGET_MAP.md`
5. `docs/EMERGENT_DOCUMENTATION_LEDGER.md`
6. `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md`
7. `docs/PORTABILITY_MATRIX.md`

No future agent should begin writes before reading those documents.
