# Memory, ARC, Hydration, and Truth Contract

## Purpose

CAOS memory is not keyword search and not a prompt dump. Memory is a governed relevance system that gives Aria durable continuity while keeping the working context fast, bounded, and truthful.

## Core vocabulary

### WCW — Working Context Window

The full context capacity available for a turn. WCW is the outer budget. It must be measured, budgeted, and protected.

### ARC — Active Relevant Context

The selected context actually useful for the current turn. ARC lives inside the WCW. ARC should contain only the relevant memories, summaries, recent thread material, tool/capability state, and documents needed for the present conversation.

### Hydration

The process of deciding what context should be loaded into ARC for the current turn.

Hydration must be selective. Aria should know capabilities exist without loading every capability, connector, memory, document, or prior thread every time.

### Sanitization

The process of cleaning, compressing, de-duplicating, bounding, and safety-filtering candidate context before it enters ARC.

Sanitization must preserve meaning and truth. It must not destroy important nuance just to reduce tokens.

## Memory model

Memory must support many bins/categories, including:

- identity
- projects
- governance
- preferences
- relationship
- domains
- tech state
- behavioral patterns
- traits
- learning
- real-world context
- risk
- counter/corrections
- unclassified

These bins are not cosmetic labels. They help Aria select the right continuity for the right moment.

## Memory capture

Aria should identify memory-worthy material from conversation naturally, similar to how ChatGPT memory works, but with stronger user governance and receipts.

Memory-worthy material includes:

- durable user preferences
- identity facts
- long-term project facts
- technical architecture decisions
- governance rules
- repeated interaction patterns
- corrections/counter-memories
- real-world operational context
- safety/risk constraints
- domain-specific vocabulary and intent

Memory should not be created just because a word appeared. Keyword occurrence is not memory significance.

## User governance

The system should support user review and correction of memory.

User controls should include:

- approve/confirm
- reclassify to another bin
- edit/refine
- forget/remove
- mark as counter/correction

The long-term goal is high-quality automated capture with user override, not passive dumping and not paralyzed manual-only capture.

## Metadata requirements

Memory atoms and context segments should carry metadata, such as:

- category/bin
- confidence
- priority
- source type
- evidence reference
- timestamp
- thread/session reference
- user scope
- relevance signals
- correction/supersession state

For compressed/summarized work, summaries must preserve lineage. A compressed summary should know what thread, segment, or source material it came from.

## Summaries and compression

During heavy work, conversations may be summarized or compressed.

Compression must:

- preserve decisions
- preserve unresolved issues
- preserve constraints
- preserve user intent
- preserve receipts and commit references when relevant
- avoid inventing conclusions
- avoid smoothing over uncertainty

## Capability awareness

Aria must know what it can do without loading every tool/capability into every turn.

Capability awareness should be lightweight by default:

- know capability exists
- know how to request/hydrate it when relevant
- load specific connector/tool details only when conversation demands it

Examples:

- Email tools should hydrate when the user asks about email.
- GitHub tools should hydrate when building or inspecting code.
- Memory bins should hydrate based on user/project relevance, not all at once.
- Admin diagnostics should hydrate only for admin/debug contexts.

## Truth machine rule

CAOS is a truth machine.

Aria must not fabricate, over-assume, or add unsupported content just to sound fluent. Adjustable model temperature may affect style/creativity, but it must never override truth discipline.

Required distinctions:

- verified
- source-backed
- inferred
- uncertain
- degraded/partial
- blocked

Aria can be warm, direct, funny, reflective, and human-useful without becoming dishonest or sycophantic. It should not put up with bullshit, including the user's bullshit, when truth requires correction.

## Latency implication

Fast behavior depends on not overhydrating.

Every mature turn should answer:

- What context was loaded?
- Why was it relevant?
- What was excluded?
- Was memory used?
- Was memory written?
- Were tools used?
- Was the response local, provider-backed, or degraded?

## Implementation direction

Memory and ARC should be implemented through modular services:

- memory_service
- memory_capture_service
- memory_review_service
- memory_relevance_service
- arc_assembler
- hydration_policy
- sanitizer_service
- summary_service
- context_lineage_service
- prompt_budget_service
- receipt_service

No God-file memory engine. No full-context dumping. No keyword-only recall.
