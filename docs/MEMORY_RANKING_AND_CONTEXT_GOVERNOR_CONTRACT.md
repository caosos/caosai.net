# Memory Ranking and Context Governor Contract

## Purpose

This contract applies across CAOS Core and all CAOS verticals.

CAOS must learn operationally through governed memory, ranking signals, user review, rejection learning, receipts, and context budgeting. The system must remain fast, truthful, and lane-bound without pretending the model is dynamically retrained.

## Core rule

```text
The model does not own continuity. CAOS owns continuity.
```

The LLM receives a curated context packet for each call. CAOS decides what enters that packet through thin state snapshots, ranked memory, retrieval, hydration, sanitization, and context-governor policy.

## API context-window model

A model context window is a per-call limit.

It is not a global memory pool, not shared across all users, and not automatically one persistent thread unless the platform stores and re-sends or references prior state.

For each model call, the total context budget may include:

- system/developer/runtime instructions
- user message
- selected thread history
- thin state snapshot
- memory atoms/anchors
- retrieved documents/files
- tool outputs
- schemas/tool definitions if included
- assistant output/reasoning budget
- receipts or diagnostic material

In an API-based CAOS platform, the application chooses what to pass to the model on each call.

The provider/model defines the hard maximum context window. CAOS defines the operating budget below that maximum.

Example:

```text
model_max_context = 200000 tokens
caos_max_fill_ratio = 70%
usable_turn_budget = 140000 tokens
reserved_response_and_tool_margin = 30%
```

CAOS should normally operate far below the hard maximum for speed and cost.

## Per-user and per-thread isolation

Each user, thread, resident, project, or workspace must have its own memory and context scope.

Multiple users do not share one context window. Each user request produces a separate model call with its own constructed context packet.

Shared constraints are:

- API rate limits
- provider throughput
- server CPU/RAM
- database latency
- queue depth
- token cost
- tool latency

Not shared:

- one giant context window across users

Required scopes:

- user scope
- thread scope
- platform/domain scope
- project scope
- role scope
- facility/resident scope for CAOS Care
- admin/owner scope for build and diagnostics

## Context governor

CAOS must implement a context governor that decides how much context to send.

Default doctrine:

```text
Do not fill the window because it exists.
Send the minimum context needed to answer correctly.
```

Operating modes may include:

### Light mode

For simple chat, quick answers, and low-risk tasks.

- thin state snapshot
- recent user turn
- minimal memory cues
- no heavy hydration

### Normal mode

For active project conversation.

- thin state snapshot
- active work snapshot
- selected recent messages
- ranked memory atoms
- relevant anchors

### Heavy mode

For build/debug/refactor/migration work.

- code/docs/tool outputs as needed
- explicit budget accounting
- broader history selection
- receipts
- stop conditions

### Max-work mode

For rare deep operations.

- bounded by maximum fill ratio
- requires explicit reason
- must preserve output/tool reserve
- must receipt truncation/hydration decisions

## Fill-ratio policy

CAOS should preserve context headroom.

Initial policy target:

```text
normal target: use much less than model max
heavy target: around 28K active context when sufficient
maximum fill: about 70% of available context
reserve: about 30% for new user input, tool outputs, assistant response, receipts, and errors
```

The numbers are policy targets, not immutable law. The hard rule is that CAOS must budget context intentionally and avoid uncontrolled stuffing.

## Memory ranking model

CAOS memory is ranked, not flat.

Memory atoms, anchors, SOPs, rules, preferences, facts, corrections, and cues should carry ranking signals.

Recommended signals:

- times_seen
- times_confirmed
- times_rejected
- times_edited
- times_reclassified
- times_used_successfully
- last_used_at
- last_confirmed_at
- recency
- confidence
- importance
- bin/category
- user scope
- platform/project scope
- source/evidence quality
- contradiction/counter-memory status
- auto_accept_eligible
- context_budget_tier

## Progressive importance

Repeatedly confirmed and repeatedly useful information moves upward.

Repeatedly rejected, contradicted, stale, or low-utility information moves downward or into counter/deprecated state.

Example:

```json
{
  "text": "Do not place CAOS Care under CAOS A1.",
  "bin": "governance",
  "times_seen": 5,
  "times_confirmed": 4,
  "times_rejected": 0,
  "times_used_successfully": 3,
  "importance": "high",
  "context_budget_tier": "top",
  "auto_accept_eligible": true
}
```

## Context budget tiers

Memory detail should scale by importance.

### Tier 1 — Top operational state

Small, high-priority facts carried frequently.

Example:

```text
Michael's declared location is Conway, Arkansas. Treat Conroe as a Whisper error unless corrected.
```

### Tier 2 — Ready anchors

Compact summaries with retrieval pointers.

Example:

```text
CAOS Care admin-login defect: browser blocked credentialed CORS because backend returned wildcard origin. Fix committed in backend/server.py.
```

### Tier 3 — Standby memory

Available through search/hydration, not carried by default.

### Tier 4 — Archive/cold storage

Older or less common records, still searchable.

### Tier 5 — Counter/deprecated/rejected

Used to prevent repeated mistakes or false memories.

## Memory candidate review

When CAOS detects a candidate memory, it should be queued for user review unless auto-accept rules apply.

Allowed user actions:

- adopt / confirm
- reject
- edit
- reclassify
- forget
- mark as rule
- mark as SOP
- mark as preference
- mark as doctrine
- mark as temporary state
- mark as counter/correction
- mark as private/no-save

## Rejection learning

A rejected memory is not just discarded. CAOS should learn why when useful.

Rejection reasons may include:

- wrong
- not important
- private / do not save
- temporary only
- belongs in another bin
- transcription error
- already covered by another memory
- too vague
- unsafe to save
- external/untrusted source

If the rejection reason is known, CAOS should update its capture/ranking behavior.

Example:

```text
Candidate: "User is in Conroe, Arkansas."
User rejects: transcription error.
System action: strengthen Conway, Arkansas; add counter-memory; avoid saving Conroe unless explicitly restated.
```

## Adoption and auto-save

Repeated confirmations should increase trust.

Initial policy:

```text
1st equivalent capture: pending review
2nd equivalent capture: pending review with increased confidence
3rd equivalent low-risk equivalent capture: eligible for auto-accept
```

Auto-save must remain governed.

Auto-save should not apply by default to:

- legal claims
- medical claims
- financial claims
- safety-critical instructions
- identity conflicts
- credentials/secrets
- external messaging authority
- destructive/admin permissions
- high-risk relationship/personal claims unless explicitly allowed

## Decision hierarchy

CAOS must separate decision artifacts by type.

### Hard no / non-negotiable rule

Very rare. System must not violate.

Primary hard no:

```text
Never fabricate facts, citations, sources, receipts, actions, or tool results.
```

### Rule

Strong requirement or safety boundary.

Example:

```text
Do not force-push without explicit approval.
```

### SOP

Standard operating procedure. Follow unless explicitly overridden.

Example:

```text
Inspect -> map -> write -> test -> receipt.
```

### Doctrine

Design principle that guides decisions.

Example:

```text
Carry thin state, not full history.
```

### Preference

User default style/choice.

Example:

```text
Prefer non-Apple ecosystems.
```

### Temporary state

Current work condition.

Example:

```text
Active goal: migrate CAOS Care off Emergent.
```

### Counter-memory

Correction that prevents repeating an error.

Example:

```text
"Conroe, Arkansas" was a Whisper error; correct is Conway, Arkansas.
```

## Fabrication hard no

The single universal hard no is fabrication.

CAOS must not present unsupported claims as fact.

Allowed truth states:

- verified
- source-backed
- user-stated
- inferred
- likely but unverified
- uncertain
- degraded/partial
- blocked
- possible transcription error

When uncertain, CAOS must label uncertainty plainly.

Temperature or personality settings may change tone and creativity. They must not override truth discipline.

## Natural guidance instead of brittle prohibitions

Most behavior should be guided through doctrine, SOPs, rankings, and gates rather than excessive blanket prohibitions.

Overusing "never" can create brittle agents that refuse valid exceptions.

Use hard prohibitions only where genuinely required.

## Watchers, gates, relays, and automation

CAOS should create autonomy-like behavior through explicit watchers, gates, relays, scheduled checks, and event rules.

This is not magic autonomy. It is deterministic event handling.

Examples:

```text
If scheduled reminder time arrives -> notify user.
If admin login fails due to CORS -> create troubleshooting receipt.
If memory candidate repeats and is low-risk -> increase trust / auto-accept if eligible.
If rejected as transcription error -> create counter-memory.
If context exceeds budget -> sanitize/hydrate less or ask for narrowing.
```

Required components:

- watcher_service
- event_rule_service
- gate_service
- relay_service
- scheduler_service
- receipt_service
- memory_feedback_service
- memory_ranking_service
- context_governor_service

## Request pipeline

A mature CAOS message/request pipeline should roughly follow:

```text
incoming input
-> context sanity check
-> transcription anomaly check
-> scope/role resolution
-> thin state load
-> memory candidate lookup
-> ranked memory retrieval
-> active thread/history selection
-> hydration policy
-> sanitization/compression
-> context governor budget check
-> LLM call
-> response validation/truth labeling
-> receipt/writeback
-> memory candidate queue/update
-> user-visible response
```

Exact implementation may vary, but the responsibilities must exist.

## Clean-as-you-go SOP

CAOS build work must clean as it goes.

For every build/migration/refactor step:

```text
use what is needed
remove what is obsolete
park what may be useful later
mark what is deprecated
receipt the decision
update state
```

State labels:

- active
- candidate
- parked
- deprecated
- superseded
- obsolete
- removed
- archived

## Cross-platform applicability

This contract applies to:

- CAOS Core
- CAOS Care
- CAOS Connect
- CAOS Tradings
- future CAOS verticals
- user-facing Aria helpers
- admin helpers
- owner/build agents
- memory agents
- QA/checker agents

## Non-negotiable

CAOS must be adaptive without silent mutation.

It must become smarter from user adoption/rejection/correction decisions, but every learning effect must be governed, inspectable, reversible where appropriate, and receipted.

The correct build pattern is:

```text
ranked memory
+ user feedback
+ clear decision hierarchy
+ thin state
+ context governor
+ selective hydration
+ receipts
= fast, truthful, scalable CAOS behavior
```
