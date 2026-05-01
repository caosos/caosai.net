# Salvage Policy

## Purpose

The rebuild should not waste useful prior work, but it must not inherit old architecture, stale runtime assumptions, or hidden mess.

## Ruling

Salvage is allowed only when it saves time without compromising the clean modular architecture.

Legacy code is evidence and reference material first. It becomes production code only after being rewritten or cleanly ported into the target module structure.

## Salvage sources

| Source | Role |
|---|---|
| `legacy-python-server-salvage-2026-05-01` | Old Python/memory concepts and contracts |
| `caosos/emergent-caos-build` | Current working behavior and feature reference |
| Screenshots/behavior snapshot | UI and behavior parity reference |

## Salvage categories

### Green: likely worth salvaging conceptually

- Session ambiguity guards.
- Deterministic recall ordering.
- Append-only persistence invariants.
- Receipt/error envelope patterns.
- Smoke test patterns.
- API boundary patterns.

### Yellow: inspect before use

- Plane B SQLite implementation.
- Legacy FastAPI stubs.
- Memory/session adapters.
- Cache helpers.
- Old deployment wrappers.

### Red: do not salvage into runtime

- `.env` values.
- venvs and installed packages.
- SQLite runtime databases.
- WAL/SHM files.
- Backups, archives, generated logs, cache/state folders.
- Base44 code.
- Emergent OAuth implementation as a direct dependency.

## Porting standard

For each salvaged idea:

1. Identify the behavior/invariant worth preserving.
2. Write the target module name.
3. Reimplement in clean target architecture.
4. Add schema/route/service boundaries where needed.
5. Preserve receipts and failure modes.
6. Record the decision in this file or `BUILD_DECISIONS_AND_INCIDENTS.md`.

## Current position

The rebuild should proceed clean-first. Salvage should be used to avoid rethinking proven CAOS-specific concepts, not to avoid writing clean code.
