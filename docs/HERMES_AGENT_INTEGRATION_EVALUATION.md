# Hermes Agent Integration Evaluation and Adapter Design

## Purpose

This document defines how CAOS should evaluate the `hermes-agent` project as a **candidate execution substrate** while preserving CAOS governance, receipts, and approval authority. This is an evaluation and adapter-design document only.

## What Hermes is

Hermes Agent (Nous Research) is an MIT-licensed Python 3.11 project published as package `hermes-agent` (observed version `0.14.0`) with CLI entrypoints including `hermes`, `hermes-agent`, and `hermes-acp`.

At a high level, Hermes exposes multiple entry paths (CLI, gateway, ACP, batch runner, API server, and Python library usage) and an agent architecture centered on:

- an `AIAgent` orchestration core;
- prompt-building and provider runtime resolution;
- tool dispatch and tool backends;
- SQLite/FTS5 session persistence;
- MCP integration;
- file/web/browser/code tooling;
- gateway/messaging interfaces;
- cron/scheduled execution;
- plugin/memory/skills subsystems;
- subagent delegation;
- multi-provider model flexibility;
- terminal backend choices (local, Docker, SSH, Singularity, Modal, Daytona, Vercel);
- security control primitives (approval gates, blocklists, allowlists, isolation, credential filtering, context scanning, input sanitization).

## Why Hermes is relevant to CAOS

CAOS needs a governed execution layer for bounded agent jobs without surrendering control of policy, approvals, memory doctrine, or user authority. Hermes is relevant as a potential substrate because it can provide execution mechanics (tool/runtime/job pathways) while CAOS keeps governance and truth-layer responsibilities.

In CAOS terms:

- Aria remains the governed executive/orchestrator.
- CAOS remains the platform for identity, memory policy, approvals, receipts, and UI controls.
- Hermes can be evaluated as a worker runtime for bounded job packets only.

## Capabilities CAOS wants to evaluate

The following capability areas are in-scope for evaluation:

1. **Multi-agent workstreams**
   - bounded worker/subagent coordination patterns;
   - deterministic task packet boundaries and stop conditions.

2. **Sandboxed execution**
   - strict separation of read/write/network scopes;
   - process-level containment and kill control.

3. **Skills**
   - role-specific skill packaging and controlled activation;
   - trust model for skill provenance.

4. **Persistent session/memory ideas**
   - session continuity mechanics;
   - compatibility with CAOS ARC/WCW/memory governance.

5. **Provider routing**
   - model/provider abstraction and runtime selection;
   - compatibility with CAOS model policy and receipt reporting.

6. **MCP/tool gateway**
   - connector/tool bridge potential;
   - capability discovery and policy filter hooks.

7. **Cron/scheduled tasks**
   - controlled recurring jobs;
   - explicit governance over unattended execution.

8. **Messaging gateway**
   - inbound/outbound agent communication channels;
   - authorization and provenance tracking.

9. **Terminal backends**
   - backend portability for isolated execution targets;
   - constraints by environment and trust level.

10. **ACP/Codex-like bridge potential**
    - protocol compatibility for a CAOS code-worker lane;
    - conversion of CAOS job packets into bounded runtime invocations.

## Security risks to address before any runtime use

1. **YOLO mode (disallowed)**
   - bypasses dangerous-command approvals;
   - incompatible with CAOS approval governance.

2. **Shell execution risk**
   - command execution can damage hosts, leak data, or bypass policy.

3. **Broad file access risk**
   - uncontrolled path access can expose secrets or mutate protected files.

4. **Connector/tool abuse risk**
   - high-capability tools can be used beyond user intent.

5. **MCP credential leakage risk**
   - credentials may appear in context, logs, tool I/O, or receipts.

6. **Prompt injection via context files**
   - untrusted repo/docs/web content can coerce unsafe actions.

7. **Memory/skill poisoning**
   - untrusted artifacts may become durable behavior influence.

8. **Runaway subagents**
   - uncontrolled spawning can expand blast radius and cost.

9. **Cron unattended execution risk**
   - scheduled tasks can perform stale or unauthorized actions.

10. **Messaging gateway auth failures**
    - incorrect authorization can allow unauthorized command paths.

## CAOS governance requirements (hard constraints)

Any Hermes integration candidate must satisfy:

1. CAOS owns approval policy.
2. YOLO mode is prohibited.
3. No default shell access.
4. No secret access by default.
5. No production deploy access.
6. Read-only-first posture.
7. Explicit sandbox contract per job.
8. Receipts required for every meaningful call/action.
9. CAOS job packets map to Hermes invocation only after approval.
10. Kill switch required and user-visible.

## Proposed adapter boundary

### Core files

- `backend/app/services/hermes_adapter.py`
- `backend/app/schemas/hermes.py`
- Optional future route surface: `backend/app/api/hermes.py`

### Boundary rules

- Hermes remains behind a CAOS adapter; no direct UI-to-Hermes calls.
- CAOS policy/approvals must execute before any invocation mapping.
- Adapter must support **capability discovery before execution**.
- Adapter v0 must expose **status/config/plan only** (non-executing).

### v0 adapter responsibilities

- Declare Hermes capability inventory schema.
- Report environment/feature availability as metadata only.
- Generate normalized invocation plans from CAOS job packets.
- Return policy-evaluation outcomes and required approvals.
- Emit receipts for plan-generation and policy decisions.

### v0 explicit exclusions

- No process spawn.
- No tool call execution.
- No connector execution.
- No file mutation.
- No scheduled job activation.

## First implementation sequence

### Phase H0 — documentation and capability map

- finalize this evaluation;
- define canonical CAOS↔Hermes capability mapping;
- define risk register and controls checklist.

### Phase H1 — non-executing adapter interface

- add schema and service interfaces only;
- support status/config/plan endpoints internally;
- enforce policy checks and receipt emission for planning.

### Phase H2 — local read-only dry-run command builder

- generate deterministic command/spec plans without execution;
- validate scope, tool policy, and approval requirements;
- preserve non-executing guarantee in default path.

### Phase H3 — sandboxed Hermes process in isolated directory

- introduce tightly scoped process execution in isolated workspace;
- enforce read-only default, hard resource/time limits, and kill control;
- maintain explicit approval gates.

### Phase H4 — read-only repo inspection job

- permit bounded inspection workloads only;
- return plans/receipts/artifacts without writes.

### Phase H5 — controlled write job with approval

- permit tightly scoped write operations only after explicit approval;
- enforce crosswire/shared-file governance and complete receipts.

## Explicit non-goals for this PR

- no Hermes installation;
- no Hermes execution;
- no agent spawning;
- no connector writes;
- no secrets usage.

## No-runtime-action confirmation

This evaluation intentionally performs no Hermes runtime actions. It defines governance, risk posture, and adapter boundaries so future implementation can proceed safely under CAOS contracts.
