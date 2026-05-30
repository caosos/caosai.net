# Agent Playground and Hermes Evaluation Contract

## Purpose

This contract captures the current CAOS direction for building an agent playground inside the fresh owned-server rebuild. The playground is intended to let CAOS evaluate and eventually operate bounded specialist agents, sandboxed work packets, connector/tool execution, Codex-style code work, and future Hermes-like control-layer capabilities without turning CAOS into a rogue autonomous framework.

This document is part of the UI/Admin Docs knowledge base and must be treated as a first-class build contract for agent, connector, sandbox, and Codex-bridge work.

## Current decision

CAOSAI.net is the current clean playground chassis.

The new build should use the existing clean shell and owned-server direction as the place to test and grow real CAOS behavior:

- persistent conversations and project context;
- governed memory and context bins;
- provider-flexible inference routing;
- visible WCW/token/tool-call accounting;
- connector access with receipts;
- Codex/code-worker integration;
- bounded specialist agents;
- future Hermes-like control/runtime capabilities.

The existing starfield/time-space visual direction is approved as a useful visual identity for the new shell, but visual effects are not the next priority. Functional wiring comes first.

## Reference lineage

CAOS has three important reference lines:

1. Base44 original prototype
   - Original serverless CAOS environment.
   - Valuable for early governance, WCW, receipt, and workflow lessons.
   - Visual/reference evidence only; do not copy Base44 code.

2. Emergent full-stack prototype
   - Later, richer behavior/product reference.
   - Valuable for profile, threads, memory console, artifacts, admin, tickets, docs, voice, onboarding, and operating feel.
   - Behavior/reference source, not a monolith to copy.

3. CAOSAI.net fresh owned-server rebuild
   - Current clean rebuild/playground target.
   - Python/FastAPI/Mongo-backed direction.
   - Must preserve proven behavior while removing platform lock-in and overgrown prototype debt.

## Product doctrine

CAOS is not a chat app. Chat is the command surface.

CAOS is a governed AI workspace where the user brings their AI, memory, projects, files, connectors, tools, and agents into one controlled operating environment.

The target operating model is:

```text
Michael = final authority
Aria = governed executive interface and orchestrator
CAOS = owned platform, memory, UI, governance, receipts, and runtime shell
Hermes-like runtime = optional controlled agent execution substrate
Specialist agents = bounded disposable workers
Connectors/tools = scoped capabilities with visible receipts
```

## Hermes position

There is no specific Hermes implementation target locked in this repository yet.

Until a concrete Hermes repository/package/runtime is identified and inspected, Hermes must be treated as a candidate agent-control substrate, not as an adopted dependency and not as CAOS itself.

Hermes-like capabilities may be evaluated for:

- project sandboxes;
- multi-agent job coordination;
- task packet execution;
- repo/code inspection;
- bounded file operations;
- connector/tool harnessing;
- log and receipt generation;
- controlled stop/kill behavior.

Hermes must not own:

- CAOS governance;
- user identity;
- connector authority;
- memory policy;
- permission gates;
- receipt standards;
- project truth;
- final action approval.

Rule:

```text
Hermes may execute bounded jobs. Aria governs, reports, and asks for approval. Michael remains authority.
```

## Agent playground scope

The first playground must be small, visible, and non-dangerous.

Initial playground capabilities should support:

- creating an agent job packet;
- assigning a bounded task;
- showing allowed tools and scopes;
- showing token/WCW/tool-call estimates;
- showing execution receipts;
- showing logs and returned artifacts/plans;
- stopping/killing a job;
- routing results back to Aria for review.

The first implementation slice should be read-only.

It may inspect repository files and produce an implementation plan, but it must not write files, deploy, access secrets, send email, modify calendars, call destructive tools, or spawn additional agents.

## Sandbox contract

Every agent job must run under an explicit sandbox contract.

Minimum fields:

```text
project_id
job_id
agent_role
task_summary
allowed_repositories
allowed_paths
forbidden_paths
allowed_tools
forbidden_tools
read_scope
write_scope
network_scope
connector_scope
memory_bins_available
secret_access_allowed
max_runtime_seconds
max_tool_calls
max_tokens
max_spawned_agents
approval_required_for
stop_conditions
receipt_required
```

Default policy:

- no secret access;
- no production deploy;
- no main branch writes;
- no destructive actions;
- no connector writes without explicit approval;
- no agent spawning unless explicitly authorized;
- no shared-file edits without orchestrator/crosswire approval;
- no broad autonomous continuation after timeout/interruption.

## Security risk register

Agent playground and Hermes-like work must account for these risks before implementation:

1. Prompt injection
   - Malicious repo text, email, webpage, document, or tool output may try to redirect the agent.

2. Tool abuse
   - Agent may call unnecessary or risky tools if not budgeted and scoped.

3. Secret exposure
   - Logs, errors, diffs, receipts, or prompts may accidentally reveal tokens, keys, or private data.

4. Rogue file writes
   - Agent may modify shared files, config, deploy scripts, lockfiles, or runtime paths outside its lane.

5. Memory poisoning
   - Untrusted inputs may be saved as durable memory or injected into ARC/WCW as if trusted.

6. Connector misuse
   - Email, GitHub, Drive, calendar, or future server connectors may be used beyond user intent.

7. Confused-deputy behavior
   - A low-trust source may persuade a high-trust agent to perform privileged actions.

8. Dependency and plugin risk
   - Agent frameworks, plugins, skills, or execution tools may include unsafe supply-chain behavior.

9. Shell execution risk
   - Local/server shell access can damage runtime, expose secrets, or deploy unintended changes.

10. Continuity loss
    - Timeout/interruption may cause an agent to lose scope and ask Michael to reconstruct context.

## Required controls

Agent playground work requires these controls:

- inspect-before-write;
- read/write tool separation;
- explicit user approval for high-risk writes;
- scoped job packet before execution;
- visible receipts for every meaningful action;
- token and tool-call accounting;
- no fake receipts;
- no hidden autonomy;
- timeout recovery through documented handoff files;
- stop/kill control visible in UI;
- redaction of secret-like content before user-visible logs;
- role/lane assignment for every worker agent;
- crosswire ledger for shared-file changes.

## UI/Admin Docs requirements

The UI should eventually expose the agent playground as a power-user workbench, not as clutter in the main chat.

Target surfaces:

- Agent Playground panel;
- project/job selector;
- split screen for User / Aria / Agent Workbench;
- job packet viewer;
- allowed-tool list;
- WCW/token/tool-call detail panel;
- execution log;
- receipt drawer;
- returned artifact/plan viewer;
- diff/PR viewer for code work;
- stop/kill button;
- route results back to chat.

The main chat remains the primary command surface. The playground is an advanced operating surface.

## Codex bridge direction

CAOS should eventually include a Codex-like work lane inside the platform.

Target model:

```text
User gives intent by voice/chat.
Aria converts intent into bounded work order.
Codex/code-worker executes inside scoped repo lane.
Agent returns diff/plan/logs/receipts.
Aria verifies and explains.
Michael approves final merge/deploy/action.
```

The Codex bridge must support:

- repo/file inspection;
- task packet creation;
- diff viewing;
- PR status viewing;
- test/validation receipts;
- Aria/user/code-worker split screen;
- no merge/deploy without explicit approval.

## Tool economy doctrine

CAOS must not waste tool calls.

Every tool call should be justified by one of these reasons:

- inspect required source evidence;
- verify current state;
- perform approved action;
- validate completed work;
- retrieve user-requested connected data.

The WCW/details panel should show:

```text
model/provider
estimated input tokens
reserved output tokens
memory/context tokens
thread-history tokens
tool-result tokens
tool-call count
tool-call names
read/write/destructive classification
receipt references
error/degraded states
```

Power users should be able to click the WCW/context indicator and see what happened.

## First implementation slice

Recommended first PR-sized implementation for this lane:

```text
Read-only Agent Playground v0
```

Behavior:

- Create backend schemas for an agent job packet and agent receipt.
- Add read-only job creation and listing endpoints, if not already present.
- Add a frontend placeholder/panel that displays job packets and receipts.
- Do not wire real autonomous execution yet.
- Do not grant write access.
- Do not add external Hermes dependency yet.
- Do not spawn sub-agents yet.

Acceptance checks:

- User can see an Agent Playground/Admin Docs entry.
- A job packet can be represented with scope, tools, limits, and stop conditions.
- Receipts can be represented without fake execution claims.
- UI clearly marks playground as read-only/prototype if execution is not wired.
- No production deploy or main write occurs.

## Documentation maintenance

When a concrete Hermes repository/runtime is selected, update this document with:

- source URL/repo;
- inspected version/commit;
- capability map;
- security review;
- dependency implications;
- sandbox compatibility;
- adoption decision.

Until then, references to Hermes remain architectural placeholders for a candidate control substrate.
