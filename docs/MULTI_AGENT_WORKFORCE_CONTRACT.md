# Multi-Agent Workforce Contract

## Purpose

CAOS must evolve from a single chat surface into a governed multi-agent AI workforce platform: specialized agents that can plan, remember, collaborate, use tools, and execute bounded workflows under Michael's authority.

This contract captures the required direction from the agentic architecture discussion/transcript supplied by Michael on 2026-05-02.

## Core shift

CAOS is not merely a chatbot. CAOS must support the shift from using an AI tool to managing AI teammates.

Required platform direction:

```text
stateless chatbot -> tool-using agent -> memory-aware worker -> specialized multi-agent workforce -> governed CAOS-owned operating platform
```

## Agent definition

A CAOS agent is a governed software worker that can:

- perceive a bounded environment or task context
- reason about a goal
- use approved tools
- access relevant memory/context
- produce or modify artifacts
- collaborate with other specialized agents
- emit receipts
- stop at risk gates

An agent is not just a persona. It is a bounded role with tools, permissions, memory scope, lane assignment, and receipts.

## Why memory is mandatory

Tools alone are not enough. An agent that cannot remember results from prior steps is not a reliable worker.

CAOS agents must use memory and ARC hydration to retain continuity across multi-step work:

- task state
- prior step results
- decisions
- source evidence
- user preferences
- constraints
- open questions
- receipts
- artifacts created

Memory must be retrieved into active context only when relevant. CAOS must not dump all memory every turn.

## Multi-agent workforce model

CAOS should support specialized agents rather than one bloated monolith agent.

Specialization reduces context overload, cost, confusion, and instruction conflict.

Initial agent lanes may include:

- Orchestrator / conductor agent
- Backend foundation agent
- Memory / ARC agent
- Provider / model router agent
- Frontend shell agent
- Admin / support / artifacts agent
- TTS/STT agent
- Security / policy agent
- Documentation / contract agent
- QA / checker agent

## Orchestration patterns

CAOS should support multiple orchestration patterns, selected by task type.

### Peer-to-peer delegation

One agent calls another specialist when a bounded subtask requires that expertise.

Example:

```text
Frontend agent -> asks Memory agent for memory-console behavior requirements
```

### DAG / pipeline execution

A predefined sequence where each step must complete before the next begins.

Useful for deterministic workflows:

```text
inspect -> map -> extract -> write -> test -> receipt -> handoff
```

### Supervisor routing

A manager/orchestrator agent analyzes an ambiguous or complex task and assigns subtasks dynamically to the right specialist.

Supervisor routing must remain governed by work-package scope and stop conditions.

## Framework / execution strategy

CAOS should favor high-control, state-machine-like execution for core build and operational workflows.

Deep autonomy is allowed only inside bounded work packages.

Principle:

```text
High control for speed and safety.
Deep autonomy only when the work package, tools, permissions, and stop conditions are explicit.
```

Message-passing collaboration can be useful, but uncontrolled conversational agent chatter creates cost, latency, and context overhead.

Artifact/shared-state collaboration is useful when agents need a common source of truth, such as:

- feature inventory matrix
- crosswire ledger
- troubleshooting vault
- build status
- receipts
- source-to-target map
- work package files

## Autonomy work packages

An agent may work without constant user intervention only when given a complete work package.

Each work package must include:

```text
objective
lane
allowed branch
source files to inspect
target files to create/update
forbidden files/actions
behavior to preserve
line limits for code files
acceptance checks
smoke tests
receipt requirements
risk gates
stop conditions
handoff format
```

No agent may infer unlimited authority from a vague goal.

## Code reuse / monolith teardown

CAOS may reuse valuable code and behavior from reference builds, especially Emergent, but must not bulk-copy monoliths.

Allowed:

- inspect reference code
- salvage useful functions
- extract working logic
- split large files into focused modules
- remove platform-specific glue
- preserve good behavior
- rebuild wiring in clean CAOS architecture

Forbidden:

- blind monolith copying
- God files
- hidden platform coupling
- secret/runtime junk
- uncontrolled line growth
- undeclared behavior changes

Code-file discipline:

```text
Target: <= 200 lines where practical
Hard cap: 400 lines unless Michael explicitly approves an exception
```

Text/blueprint/vault files are not bound by code-file line limits.

## Security doctrine

Agentic capability increases risk. CAOS must presume breach and constrain agents by design.

Required controls:

- least privilege
- scoped tool credentials
- sandboxing
- branch discipline
- no main writes without approval
- no production deploy without approval
- no destructive deletion without approval
- no secret exposure
- human-in-the-loop risk gates
- circuit breaker / emergency stop path
- receipts for tool use, memory use, writes, errors, and degraded responses

Prompt injection and memory poisoning must be treated as active threats.

External text from email, websites, documents, logs, scraped pages, or uploaded files must not be allowed to silently override CAOS governance.

## Memory poisoning prevention

Because CAOS memory affects future behavior, memory writes must be governed.

Memory safety requirements:

- source/evidence tracking
- confidence scoring
- user review controls
- counter/correction support
- high-risk memory gating
- progressive auto-accept only for low-risk repeated patterns
- no memory write from untrusted external content without sanity checks
- receipts for memory creation/update/forget/reclassify

## Performance doctrine

CAOS should not rely on huge context windows as the primary architecture.

Performance comes from:

- specialized agents
- small scoped prompts
- hydration gates
- ARC selection
- verified knowledge cache
- standby context
- receipts/TurnTrace
- avoiding repeated research when cached verified information is fresh

The platform should prefer deterministic pipelines for known workflows and only escalate to flexible supervisor routing when needed.

## Human role

Michael remains the system owner/operator.

CAOS agents may become powerful teammates, but authority remains governed:

- Michael defines objectives
- contracts define lanes
- work packages define scope
- receipts prove actions
- risk gates stop unsafe execution
- the orchestrator/conductor coordinates specialists
- checker/QA agents verify work before acceptance

## Platform goal

CAOS should become a user-owned alternative to expensive external app-building/agent platforms where possible.

Target capability:

- launch specialized agents
- assign lanes
- inspect repos/docs/files
- build and modify code
- write contracts/docs
- create artifacts
- run checks
- preserve receipts
- coordinate through shared state
- stop at risk gates

The goal is maximal human + AI effectiveness and efficiency, not autonomy theater.

## Non-negotiable

CAOS must build toward a governed multi-agent workforce platform with memory, tools, receipts, least privilege, context sanity checks, and work-package discipline.

No reckless autonomy. No stateless chatbot ceiling. No paying external platforms forever for work CAOS can safely own.
