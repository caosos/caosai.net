# CAOS AI Agent Protocol

Status: mandatory repository entrypoint
Authority: Michael Chambers
Scope: all AI-agent, Codex, GitHub, server, migration, and documentation work in this repository.

## Repository role

`caosos/caosai.net` is the CAOS AI server/core/runtime/orchestration repository.

It is not the CAOS Care product repository. CAOS Care lives separately in `caosos/CAOSCARE.COM`.

## Operating model

- ChatGPT / Aria is the orchestrator, architect, reviewer, and task framer.
- Codex is the repo worker / coding agent.
- GitHub repositories are the primary workspace and source of truth.
- Linode / owned server infrastructure is the runtime target.
- Michael Chambers is the authority, final approver, and facilitator for actions agents cannot physically execute.

## Required workflow

```text
Michael gives objective
  -> Aria frames bounded Codex task
  -> Codex works selected GitHub repo
  -> Codex returns report/diff/branch/PR
  -> Aria verifies through GitHub and reviews architecture/risk/correctness
  -> Michael approves
  -> server pulls/builds/runs from GitHub
```

## Hard rules

1. Inspect first. Do not write before reading relevant files.
2. GitHub is the durable source of truth.
3. Do not default to manual file-by-file patching unless Codex is blocked or direct GitHub correction is safer.
4. Do not merge CAOS AI and CAOS Care into one giant app.
5. Do not import large prototype code without a bounded migration task.
6. Do not make broad rewrites without explicit scope.
7. Do not silently mutate behavior, memory, policy, auth, billing, storage, or model-routing paths.
8. Do not add secrets, tokens, API keys, private facility details, resident/staff data, or production credentials.
9. Do not claim production readiness unless deployment, runtime, auth, persistence, monitoring, and security have been verified.
10. Receipts are required for changes: files changed, purpose, validation performed, and unresolved blockers.

## Prototype/source boundaries

- `caosos/emergent-caos-build` is prototype/source/salvage.
- `caosos/caos-os-A1` is Base44 reference only.
- `caosos/CAOSCARE.COM` is the CAOS Care product repo.
- `/home/michael-chambers/CAOS_LINODE_SALVAGE_2026-05-09` on the Linode server is salvage-only.
- `/opt` is the clean forward deployment target.

## Server discipline

Before touching server runtime:

1. Inspect active services.
2. Inspect nginx/proxy configuration.
3. Identify what owns active ports.
4. Preserve current working services until replacement is explicitly approved.
5. Use explicit `cd` in every command block.
6. Keep CAOS AI and CAOS Care deploy targets separate.

Recommended forward targets:

```text
/opt/caosai
/opt/caoscare
```

## Default stop gate

If repo, branch, runtime, or tool context does not match the requested task, stop and report the mismatch instead of improvising.
