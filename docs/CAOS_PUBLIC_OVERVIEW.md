# CAOS Public Overview

CAOS stands for **Cognitive Adaptive Operating System**.

It is an experimental governed AI orchestration platform. The central idea is that useful AI systems need more than a chat window. They need memory, tools, permissions, receipts, model routing, context hygiene, and structured workflows.

## Plain-English Summary

CAOS is being designed as a workbench where AI can:

- remember useful information across sessions;
- keep that information separated into relevant bins;
- connect to tools and files;
- inspect before changing anything;
- ask for approval before risky actions;
- produce receipts showing what happened;
- route simple tasks to cheaper models and harder tasks to stronger models;
- support product workflows beyond normal chat.

## Why It Matters

Most AI tools are powerful but temporary. They answer the current prompt, then the user has to re-explain the project, history, rules, and constraints again later.

CAOS is exploring a different pattern:

```text
persistent context
+ governed execution
+ tool access
+ model economics
+ workflow memory
= practical AI operating layer
```

## Current Prototype Sources

The project has gone through multiple prototype environments:

1. **Base44 prototype** — earlier hosted/serverless experiment.
2. **Emergent prototype** — full-stack prototype with backend, frontend, memory, diagnostics, receipts, and connectors.
3. **Clean rebuild** — current server-target rebuild direction.

This repository represents the clean rebuild/public home.

## What Is Built vs. Planned

CAOS should be read as an active project, not a finished product.

Already explored in prototypes:

- persistent memory concepts;
- receipts and diagnostics;
- multi-provider direction;
- tool/connector surfaces;
- admin-oriented visibility;
- frontend chat surfaces;
- backend orchestration spines;
- context hydration and compression ideas.

Planned / active rebuild direction:

- cleaner memory-bin architecture;
- safer tool execution;
- MCP-based connectors;
- E2B/sandbox execution lane;
- worker-agent orchestration;
- cost-aware model routing;
- CAOSCare product workflows;
- device/tablet/pendant integration experiments.

## Design Principle

The core design principle is:

```text
Determinism over fluency.
Transparency over hidden behavior.
Bounded execution over uncontrolled autonomy.
```

CAOS should not silently mutate memory, silently edit files, or pretend to have completed work it did not actually do.
