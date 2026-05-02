# Context Meter and Arbitration Contract

## Purpose

CAOS must make context usage visible, measurable, testable, and governable.

This contract defines the required context meter, admin observability tools, history-retention experiments, hydration/sanitization receipts, lane switching, and context arbitration rules.

It applies across CAOS Core and all CAOS verticals, including CAOS Care, CAOS Connect, and CAOS Tradings.

## Core problem

A fixed message-count rule such as `last 40 messages` is useful as a starting heuristic, but it can conflict with token budgets, hydration, sanitization, and active work priorities.

CAOS must be able to test whether last-N history works better or worse than token-budgeted relevance selection.

Core doctrine:

```text
Measure first. Then tune.
```

## Context meter requirement

CAOS must provide a context meter that shows what is being sent to the model and why.

The context meter should be available to admins/owners and optionally simplified for normal users.

Required measurements:

- model max context window
- configured CAOS max fill ratio
- current estimated input tokens
- reserved output tokens
- reserved tool/receipt/error buffer
- active message/history token count
- thin state snapshot token count
- memory/anchor token count
- source/tool output token count
- system/developer/runtime instruction token count
- active lane token count
- parked lane token count
- total estimated context fill percentage
- selected model/provider
- selected mode: light / normal / heavy / max-work

## Context budget categories

Every model call should be able to explain its context composition.

Recommended budget buckets:

```text
governance/system
user input
thin state snapshot
active lane state
recent history
ranked memory/anchors
source evidence/tool output
receipts/errors/diagnostics
reserved output
buffer
```

The meter should make visible when any bucket grows too large.

## Admin-only observability

Admins/owners need tools that regular users do not need.

Admin context tools should include:

- live context meter
- hydration receipt viewer
- sanitization receipt viewer
- memory inclusion/exclusion viewer
- lane state viewer
- model/provider call log
- token/cost estimate
- latency estimate and actual latency
- cache hit/miss viewer
- tool-call receipt viewer
- truncation/eviction explanation
- selected-history explanation
- debug export for a single turn

Public users should not see internal diagnostics, private memory details, admin logs, secrets, token accounting internals, or cross-user context.

## Last-N versus budgeted history

CAOS should support controlled testing of history selection policies.

Policy candidates:

### Fixed last-N messages

Example:

```text
include last 40 messages
```

Pros:

- simple
- predictable
- easy to reason about
- preserves conversational continuity

Cons:

- may include stale chatter
- may evict important anchors/source evidence
- message length varies wildly
- can fight context budget
- can slow responses unnecessarily

### Token-budgeted recent history

Example:

```text
include recent messages until recent_history_budget is full
```

Pros:

- respects cost and speed
- adapts to long/short messages
- prevents runaway history growth

Cons:

- may cut off useful conversational setup if relevance is not scored well

### Relevance-weighted history

Example:

```text
include recent + relevant older turns based on active lane/task
```

Pros:

- preserves what matters
- supports topic/lane switching
- avoids stale context

Cons:

- requires better scoring, receipts, and testing

## Required experiment mode

CAOS should support an admin experiment mode to compare:

```text
A: last 40 messages
B: token-budgeted recent history
C: relevance-weighted history
D: hybrid policy
```

For each turn, record:

- policy used
- estimated tokens
- latency
- model/provider
- response quality rating if available
- whether context was sufficient
- whether user corrected missing context
- whether unnecessary stale context was included
- cost estimate

This allows Michael and Aria to tune the system from evidence rather than guessing.

## Context arbitration layer

A Context Arbitration Layer must decide what enters the model call.

Priority order should generally be:

1. hard truth/governance requirements
2. current user input
3. platform/domain/role/scope
4. active lane state
5. thin state snapshot
6. required recent turns
7. ranked memory/anchors
8. relevant source/tool evidence
9. receipts/errors needed for current task
10. optional older history

Rules:

```text
Budget beats fixed message count.
Relevance beats raw recency.
Active lane beats parked lane.
Hydration requires a budget.
Sanitization must preserve required anchors.
Duplicate concepts consolidate into ranking, not repeated text.
```

## Lane and sandbox context

CAOS must support multiple work lanes without blending them into sludge.

Examples:

```text
Lane: CAOS Core
Lane: CAOS Care migration
Lane: CAOS Connect product doctrine
Lane: CAOS Trading research
Lane: personal recall / life admin
```

Each lane should have:

- lane id
- title
- active/parked/archived state
- thin summary
- current goal
- next action
- important constraints
- relevant files/repos/docs
- latest receipts
- memory tags
- hydration priority

When the user switches topics:

```text
park current lane
update lane snapshot
load target lane snapshot
hydrate only necessary anchors/evidence
exclude unrelated lane detail
```

## Work-mode detection

CAOS must detect when serious work is happening.

Signals include:

- repo/file/path references
- code/log/error screenshots
- repeated build/debug terms
- urgency terms: fix, broken, migrate, deploy, test
- tool calls
- branch/commit/domain references
- high message density
- user asks for exact cause
- unresolved task chain
- active work package

When work mode is active, CAOS may increase context budget and model strength.

When work mode is inactive, CAOS should stay lean.

## Hydration/sanitization receipts

Every mature model call should be able to produce a compact internal receipt.

Receipt should answer:

- what was hydrated
- why it was hydrated
- what was excluded
- why it was excluded
- what was sanitized/compressed
- whether duplicates were consolidated
- whether stale items were evicted
- what lane was active
- which parked lanes were summarized only
- estimated token usage by bucket
- whether max fill ratio was approached
- whether a follow-up hydration call was needed

## Context conflict detection

CAOS must detect conflicting rules before they cause runtime failure.

Examples:

```text
Conflict: include last 40 messages + max context fill 70% + hydrate source file.
Resolution: context arbitration chooses required source/anchors first, then includes recent history up to budget.
```

```text
Conflict: CAOS Care lane and CAOS Core lane both active.
Resolution: choose active lane based on current user intent; park the other lane with a thin summary.
```

## Tools available inside CAOS

CAOS should eventually expose platform-native tools comparable to or better than external app-building/agent platforms.

Admin/build tools should include:

- repo/file inspector
- code search
- branch/commit viewer
- diff viewer
- file writer with receipts
- sandbox runner
- test runner
- deployment status viewer
- log viewer
- context meter
- memory console
- lane manager
- work package manager
- agent launcher
- model/provider selector
- cost/token monitor
- cache viewer
- troubleshooting vault

These tools must be permissioned, logged, and receipt-backed.

## Cost and latency awareness

Every context policy affects cost and speed.

CAOS should record:

- estimated input tokens
- estimated output tokens
- selected model cost class
- latency target
- actual latency
- cache hits/misses
- tool-call latency
- whether a cheaper/local model could have handled the task

Cost policy is not fully defined here, but the architecture must leave room for model lanes and cost-aware routing.

## Current build implication

For the new CAOS build, do not hard-code last 40 messages as the final rule.

Allow it as one test policy.

Preferred implementation direction:

```text
recent_history_policy = configurable
recent_history_budget_tokens = configurable
max_fill_ratio = configurable
lane_hydration_policy = configurable
admin context meter = required
hydration receipts = required
```

## Acceptance criteria

A successful implementation must let an admin answer:

- how much context was used this turn?
- what used the most tokens?
- which memories were included?
- which recent messages were included?
- why was a source/file hydrated?
- what was evicted or excluded?
- which lane was active?
- did the system use last-N, token-budgeted, or relevance-weighted history?
- did the turn stay under target fill ratio?
- how long did the call take?
- what did it cost approximately?

## Non-negotiable

CAOS must not fly blind on context.

If CAOS is going to be fast, cheap, truthful, and stable, it must measure context usage, expose it to admins, and arbitrate history/memory/source hydration before every model call.
