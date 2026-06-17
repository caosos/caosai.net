# Checkpoint — CCE canonical repo setup

Date: 2026-06-16  
Agent / tool: ChatGPT using GitHub connector  
Repository: `caosos/caosai.net`  
Branch: `CLUADE-CODE-CLEAN-BUILD`

## What changed

- Added `AGENTS.md` as the mandatory agent entrypoint for this canonical public CAOS repo.
- Added `docs/CCE_CAOS_CARE_ENGINE_PROPOSAL.md` as the canonical CCE proposal.
- Updated `README.md` to include CCE direction and the CCE proposal in Start Here / Public Documentation.
- Updated `docs/ARCHITECTURE_CONCEPTS.md` to include CCE mode selection, receipt fields, worker roles, and execution-mode relationship.
- Added `docs/CODEX_CCE_V0_BUILD_TASK.md` with a small Codex-ready build package for CCE v0.1 policy skeleton.

## What was verified

- Confirmed `caosos/caosai.net` is the public clean-rebuild home for CAOS.
- Confirmed default branch is `CLUADE-CODE-CLEAN-BUILD`.
- Confirmed no `AGENTS.md` existed before this update.
- Confirmed this work did not deploy anything and did not touch secrets, tokens, private care data, facility data, resident/staff/family examples, or environment files.

## What is not built yet

- CCE runtime policy code is not implemented yet.
- No verifier model pass exists yet.
- No council worker orchestration exists yet.
- No provider calls, tool calls, or production runtime changes were added.

## Next safe step

Have Codex complete the small v0.1 build package in `docs/CODEX_CCE_V0_BUILD_TASK.md`:

1. create a minimal CCE policy/types/receipt skeleton;
2. add deterministic tests for fast / verified / council / lockdown mode selection;
3. document implementation notes;
4. avoid deployment, provider calls, private CAOSCare details, and secrets.
