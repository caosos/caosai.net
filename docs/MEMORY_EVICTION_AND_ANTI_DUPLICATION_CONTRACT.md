# Memory Eviction and Anti-Duplication Contract

## Purpose

This contract defines how CAOS keeps active context fresh, relevant, non-duplicative, and fast without deleting useful long-term memory too aggressively.

It applies across CAOS Core, CAOS Care, CAOS Connect, CAOS Tradings, and future CAOS verticals.

## Core doctrine

```text
Nothing stale belongs in active context.
Nothing useful should be deleted just because it is not active right now.
```

CAOS must distinguish between:

- evicting from active context
- demoting to standby memory
- archiving to cold storage
- deprecating as superseded
- rejecting as wrong
- deleting/forgetting by user command

Eviction from context is not the same thing as forgetting.

## Time-aware relevance

CAOS must evaluate relevance by time and context, not only by message count or call count.

A memory should not stay active merely because it is recent if it no longer belongs to the current task.

A memory should not be ejected too quickly if it remains relevant to the active work, even across many calls.

Required signals:

- last_used_at
- last_confirmed_at
- last_referenced_at
- task/session relevance
- active goal relevance
- platform/domain relevance
- thread/workstream relevance
- user role relevance
- recency
- importance
- confidence
- contradiction/counter-memory status

## Contextual eviction

CAOS should ask:

```text
Does this item belong in the current context packet?
```

Not merely:

```text
How old is this item?
```

Evict from active context when:

- it does not relate to the current task
- it belongs to another platform/lane
- it is superseded by a newer memory/contract/receipt
- it is low-ranking and budget is tight
- it was rejected or corrected
- it is duplicated by a stronger anchor
- it introduces stale ambiguity
- it is no longer needed after a task is closed

Keep or hydrate when:

- the user references it directly or indirectly
- it is a top operational rule/SOP
- it is part of the current active work
- it prevents known mistakes
- it is needed to interpret the user's current wording
- it is required for safety/truth/governance
- it is a retrieval handle for deeper evidence

## Duplicate consolidation

Duplicate memories must not be repeatedly injected into active context.

Repeated mentions should increase ranking, confidence, and importance, not create repeated context bulk.

Bad pattern:

```text
Carry five copies of "Do not place CAOS Care under CAOS A1."
```

Good pattern:

```json
{
  "canonical_text": "Do not place CAOS Care under CAOS A1.",
  "times_seen": 5,
  "times_confirmed": 4,
  "importance": "high",
  "context_budget_tier": "top"
}
```

## Canonical memory records

Equivalent statements should resolve into a canonical memory record when possible.

Canonical record fields should include:

- canonical_text
- aliases / alternate phrasings
- source instances
- times_seen
- times_confirmed
- times_rejected
- times_used_successfully
- first_seen_at
- last_seen_at
- last_used_at
- confidence
- importance
- bin/category
- context_budget_tier
- evidence pointers
- counter/supersession status

## Anchor and metadata hydration

When a topic is active, CAOS should use anchor seeds and metadata to hydrate only the necessary information.

Hydration should prefer:

1. canonical memory record
2. compact anchor summary
3. retrieval handles / evidence pointers
4. specific source excerpts only when needed
5. full source only for deep verification or build work

The system must not hydrate duplicate source fragments simply because the same concept was mentioned many times.

Repeated mentions should influence ranking and retrieval priority.

They should not multiply token load.

## Staleness model

Staleness is contextual.

A memory may be old but still highly relevant.

A memory may be new but irrelevant.

Recommended staleness states:

- active
- fresh standby
- stale standby
- archived
- superseded
- deprecated
- rejected
- counter-memory

A stale item should remain searchable unless the user explicitly forgets/removes it or policy requires removal.

## Eviction receipts

Important context evictions should be receipted when they affect behavior.

Receipt-worthy events:

- active context item demoted
- memory superseded
- duplicate consolidated
- rejected item converted to counter-memory
- high-ranking item downgraded due to non-use or contradiction
- old item rehydrated because the user referenced it
- context budget forced exclusion of otherwise relevant material

Receipt fields:

- item id
- action
- reason
- previous state
- new state
- timestamp
- trigger
- affected platform/thread/project

## User feedback loop

User rejection, adoption, correction, and reclassification must update future eviction and ranking behavior.

Examples:

```text
User rejects a candidate as wrong:
  -> demote or reject candidate
  -> create counter-memory if useful
  -> reduce similar future captures

User confirms a memory repeatedly:
  -> increase rank/confidence
  -> consolidate duplicates
  -> carry thinner canonical form more often

User reclassifies a memory:
  -> update bin/category
  -> adjust hydration rules for that bin
```

## Watchers, gates, relays

Eviction and ranking can be automated by deterministic watchers/gates.

Examples:

```text
If memory has not been used for the active platform/workstream in N days -> demote from active to standby.
If memory remains unused across multiple completed tasks -> archive.
If user references a stale item -> rehydrate and update last_used_at.
If duplicate candidate appears -> merge into canonical record and increment times_seen.
If candidate conflicts with counter-memory -> queue for clarification instead of saving.
```

These systems create autonomy-like intelligence through explicit rules, not uncontrolled model behavior.

## Active context packet requirement

Every active context packet should be able to answer:

- why this item is included
- what item it replaced or superseded
- whether it is canonical or duplicate-derived
- when it was last used
- why excluded items were left out if budget mattered
- what retrieval handles exist for deeper hydration

## Performance requirement

The purpose of eviction and anti-duplication is speed and precision.

CAOS must avoid:

- repeated duplicate facts
- stale cross-platform contamination
- full-history context bloat
- active context sludge
- overhydrating rarely used memory
- losing useful old memories by deleting too aggressively

Target behavior:

```text
Small active state.
Ranked canonical facts.
Searchable deep memory.
No duplicate token waste.
Contextual eviction instead of blind deletion.
```

## Non-negotiable

CAOS must be smart about what stays active.

A memory's value is not just whether it exists. Its value is whether it belongs in the current context, whether it has been confirmed, whether it has been useful, and whether it can help the system retrieve deeper truth when needed.
