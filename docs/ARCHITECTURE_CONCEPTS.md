# Architecture Concepts

This document describes the public architecture concepts behind CAOS.

## 1. Orchestrator

The orchestrator is the main controller. It receives the user request, decides what context is needed, chooses tools/models, and coordinates the response.

It should not blindly call every tool or hydrate every memory source. It should ask:

```text
What is the task?
What context is relevant?
What tool is safe?
What model is appropriate?
Does this need CCE fast, verified, council, or lockdown mode?
What needs approval?
What receipt should be produced?
```

## 2. Memory Bins

CAOS should avoid one large undifferentiated memory pile.

Instead, memory should be separated into bins such as:

- platform architecture;
- repo/server history;
- product direction;
- CAOSCare workflows;
- device/tablet experiments;
- user preferences;
- debugging records;
- launch/business planning;
- safety/compliance notes;
- CCE trust-layer receipts and decisions.

The goal is to hydrate the right memory at the right time instead of dragging unrelated history into every turn.

## 3. Rehydration

Rehydration means pulling relevant stored context back into the active AI working context.

Good rehydration is selective:

```text
current task
  -> relevant bins
  -> relevant records
  -> sanitized context packet
  -> active reasoning context
```

## 4. Sanitation

Sanitation means cleaning context before it is injected into an AI prompt or workflow.

It can include:

- removing secrets;
- removing irrelevant noise;
- deduplicating repeated logs;
- trimming oversized outputs;
- marking uncertain or unverified claims;
- preserving links to raw source records.

Sanitation should not destroy raw records unless explicitly intended.

## 5. Compression

Compression should mean making active context cheaper and easier to use without losing the ability to retrieve original details.

Preferred pattern:

```text
raw source record
  -> sanitized copy
  -> summary
  -> tags / embedding / index
  -> selective rehydration later
```

Plain summarization alone is not enough when exact details may matter later.

## 6. Receipts

Receipts are records of what happened.

Examples:

- which tool was called;
- what file was inspected;
- what branch was edited;
- what model was used;
- what memory bin was hydrated;
- what validation passed or failed;
- what changed and why;
- which CCE mode was selected;
- what a verifier checked;
- what was blocked or escalated.

Receipts are important because agent systems need auditability.

## 7. Model Routing

Not every task needs the most expensive model.

CAOS should support cost-aware routing:

```text
cheap / fast model:
- extraction
- classification
- short summaries
- bounded inspection
- repetitive checks

stronger model:
- synthesis
- architecture decisions
- conflict resolution
- safety-sensitive reasoning
- final review
```

Model routing should eventually integrate with CCE mode selection so low-risk tasks stay fast and high-impact tasks receive verification or council review.

## 8. CCE — CAOS Council Engine

CCE is the proposed CAOS trust engine.

It decides when a turn should use:

```text
fast      -> one model / low-risk path
verified  -> primary model plus verifier / critic
council   -> multiple bounded workers plus synthesizer plus verifier
lockdown  -> no AI final answer; human escalation only
```

CCE should not wake every worker for every task. It should classify risk, cost, source need, domain sensitivity, and user/admin policy.

Minimum CCE runtime contract:

```text
request
  -> cce policy decision
  -> selected mode
  -> selected worker roles
  -> verifier / gatekeeper where needed
  -> receipt
  -> final answer, routed action, or escalation
```

Important receipt fields:

```text
cce_mode
risk_level
worker_roles_used
models_used
source_mode
claims_checked
contradictions_found
bias_or_framing_flags
safety_flags
confidence
final_gate_decision
```

CCE is not a political alignment system. It is a verification and trust system: bias-detected, source-grounded, contradiction-checked, risk-gated, receipt-backed, audit-visible, and human-governed.

## 9. Worker Agents

Worker agents are bounded helpers. They should perform narrow tasks, then report back to the orchestrator.

Examples:

- repo inspector;
- test runner;
- document reader;
- cost checker;
- safety reviewer;
- frontend reviewer;
- backend reviewer;
- CCE verifier;
- CCE source reviewer;
- CCE opposition/red-team worker;
- CCE synthesizer.

The orchestrator remains responsible for final synthesis and governance.

## 10. Tool Loop Guard

Agent systems can get stuck repeating the same failed action.

CAOS should detect repeated tool calls, repeated failures, and circular behavior.

Example policy:

```text
same tool + same arguments repeated 3 times
  -> stop repeat
  -> record loop warning
  -> force correction or escalate
```

## 11. Execution Modes

Suggested operating modes:

### Inspect Mode

Read only. No changes.

### Plan Mode

Produce a bounded plan with risks and acceptance criteria.

### Agent Mode

May act with explicit approval for writes or risky operations.

### Trusted Mode

May perform pre-approved operations inside a defined sandbox or trusted project scope.

Trusted mode should be narrow, logged, and reversible.

### CCE Modes

CCE adds response-trust modes on top of execution modes:

```text
fast
verified
council
lockdown
```

Execution mode controls what the system may do. CCE mode controls how much verification the answer/action needs.

## 12. MCP and External Tools

MCP-style connections allow CAOS to connect with tools, services, files, repos, and systems through a more standardized interface.

The goal is not uncontrolled access. The goal is governed access.

## 13. E2B / Sandbox Lane

A sandbox execution lane can allow code tests, experiments, and command execution without risking production systems.

This is especially important for:

- code execution;
- package tests;
- generated scripts;
- unsafe command evaluation;
- worker-agent experiments;
- future CCE worker-panel experiments.

## Summary

CAOS architecture is centered on this pattern:

```text
memory bins
+ selective hydration
+ governed tools
+ cost-aware models
+ bounded workers
+ CCE trust modes
+ verifier / gatekeeper paths
+ receipts
+ rollback/safety boundaries
```
