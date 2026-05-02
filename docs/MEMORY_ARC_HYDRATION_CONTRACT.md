# Memory, ARC, Hydration, and Truth Contract

## Purpose

CAOS memory is not keyword search and not a prompt dump. Memory is a governed relevance system that gives Aria durable continuity while keeping the working context fast, bounded, and truthful.

A core purpose of CAOS memory is cognitive assist: helping Michael and future users recover the right word, document, feature, ticket, place, person, system concept, or prior decision when they can describe it but cannot immediately remember its exact name.

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

### Cognitive recall assist

Cognitive recall assist is the ability to recover a remembered target from partial, imprecise, descriptive, or circumstantial user language.

Examples:

- "that problem ticket book" -> `Troubleshooting Vault`
- "the context window thing" -> `WCW / Working Context Window`
- "the active context packet" -> `ARC / Active Relevant Context`
- "that build rule about not accepting weird dictated names" -> `STT / Whisper anomaly guard`

This is a first-class CAOS behavior, not a convenience feature. It matters for Michael and for elderly/care users whose memory, word recall, or attention may be degraded.

### Progressive memory trust

Progressive memory trust is the process where repeated user confirmation of the same or equivalent memory pattern increases confidence and can eventually allow low-risk equivalent memories to be accepted automatically.

This does not remove user control. It reduces repetitive confirmation burden for patterns the user has already approved multiple times.

### Context sanity gate

The context sanity gate is an LLM-side review step that checks whether incoming text, especially dictated or STT/Whisper text, appears internally inconsistent with known context.

It works like a lightweight verification challenge: if a fragment seems off, impossible, out of character, authority-changing, or unrelated to the active workflow, CAOS must pause before treating it as fact.

The gate does not accuse the user of error. It protects the workflow from transcription noise, hallucinated names, corrupted phrases, or accidental authority changes.

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
- user-specific terminology and aliases for recurring concepts
- recall-assist mappings from vague descriptions to precise project terms

Memory should not be created just because a word appeared. Keyword occurrence is not memory significance.

## Memory review and progressive auto-accept

Memory review is a product-critical surface. Users should be able to see what CAOS thinks is important, confirm it, correct it, reclassify it, or forget it.

Required review actions:

- confirm / approve
- edit / refine
- reclassify bin/category
- forget / remove
- mark as counter/correction
- add alias / alternate phrasing
- correct an incorrect recall match

Repeated confirmations should matter.

If the user confirms the same or equivalent low-risk memory pattern multiple times, CAOS may increase trust in that pattern and eventually auto-accept future equivalent captures.

Initial policy target:

```text
1st equivalent capture: pending review
2nd equivalent capture: pending review with increased confidence
3rd equivalent capture: eligible for auto-accept if low-risk and same category/pattern
```

Auto-accept eligibility requires:

- same user scope
- same or equivalent semantic pattern
- low-risk category
- no contradiction with active counter-memory
- confidence above configured threshold
- source/evidence retained
- receipt generated
- user setting allows progressive auto-accept

Auto-accept must not apply by default to high-risk categories such as:

- legal
- medical
- financial
- safety-critical instructions
- identity conflicts
- credentials/secrets
- external messaging authority
- destructive/admin permissions
- relationship-sensitive or highly personal claims unless explicitly allowed

Even when auto-accepted, memory must remain user-governed:

- visible in the memory console
- reversible via forget/remove
- editable
- reclassifiable
- capable of being countered/corrected
- traceable through receipts/evidence

## Cognitive recall behavior

When a user cannot remember the exact term but provides surrounding clues, CAOS should infer likely matches from memory, current project context, prior terminology, documents, and conversation state.

Required behavior:

- accept partial descriptions and circumstantial clues
- search aliases, synonyms, nearby concepts, and prior references
- return the likely target name plainly
- include confidence when uncertain
- distinguish verified memory from inference
- avoid inventing a target when evidence is weak
- ask a narrow clarification only when multiple plausible targets exist

Expected pattern:

```text
User: "What's that problem ticket book called?"
Aria: "Troubleshooting Vault. That's the build doc where solved problems, root causes, fixes, and prevention rules go."
```

This behavior should support:

- project work
- personal memory continuity
- elder-care assistance
- maintenance/workflow recall
- document and ticket retrieval
- feature names and system concepts
- safety-critical clarification when the wrong recalled item could cause harm

## Context sanity behavior

Incoming text must be checked against the active context before being treated as authoritative.

This is especially important for dictated input, STT/Whisper transcripts, copied handoffs, and long operational messages.

The context sanity gate should look for:

- newly introduced actors or names that do not fit known workflow context
- phrases that are grammatical but nonsensical in context
- corrupted analogies or object names
- repo, branch, domain, or tool names that conflict with established state
- authority changes that Michael did not explicitly grant
- instructions that contradict active governance rules
- sudden high-risk actions embedded in otherwise casual speech
- impossible or out-of-character claims

Required handling:

```text
If confidence is high that the fragment is corrupted:
  mark POSSIBLE_TRANSCRIPTION_ERROR
  infer the likely intended meaning only when context strongly supports it
  do not create durable memory from the corrupted phrase
  do not create a new actor/authority/tool from the corrupted phrase

If confidence is medium or low:
  ask Michael a narrow clarification before acting

If the fragment affects authority, identity, repo, branch, deployment, deletion, secrets, external messages, or real-world action:
  stop and require explicit confirmation
```

Examples:

```text
Transcript: "message I got from Ed"
Known context: no Ed exists in the CAOS build workflow
Handling: mark POSSIBLE_TRANSCRIPTION_ERROR; do not create a new actor

Transcript: "trinket and the head"
Known context: user was describing mall directory stands/map kiosks
Handling: mark POSSIBLE_TRANSCRIPTION_ERROR; resolve as mall directory kiosk only if context is strong
```

The context sanity gate should be implemented as a secondary prompt/check before memory capture, command execution, authority changes, or build-state mutation.

## User governance

The system should support user review and correction of memory.

User controls should include:

- approve/confirm
- reclassify to another bin
- edit/refine
- forget/remove
- mark as counter/correction
- add alias / alternate phrasing
- correct an incorrect recall match
- enable/disable progressive auto-accept for eligible low-risk memory patterns
- reset trust for a memory pattern if auto-accept becomes wrong or annoying

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
- aliases / alternate phrasings
- recall cues
- confirmation count
- auto_accept_eligible
- auto_accept_reason
- trust pattern ID
- sanity_check_status
- transcription_suspect
- corrected_from

For compressed/summarized work, summaries must preserve lineage. A compressed summary should know what thread, segment, or source material it came from.

## Summaries and compression

During heavy work, conversations may be summarized or compressed.

Compression must:

- preserve decisions
- preserve unresolved issues
- preserve constraints
- preserve user intent
- preserve receipts and commit references when relevant
- preserve aliases and user-specific names for recurring concepts
- preserve confirmation/correction signals relevant to progressive trust
- preserve STT/transcription anomaly corrections when relevant to future safety
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
- possible transcription error

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
- Was memory auto-accepted or queued for review?
- Was a context sanity check run?
- Was any fragment marked possible transcription error?
- Was the response local, provider-backed, or degraded?

## Implementation direction

Memory and ARC should be implemented through modular services:

- memory_service
- memory_capture_service
- memory_review_service
- memory_relevance_service
- memory_trust_service
- context_sanity_service
- transcription_anomaly_service
- arc_assembler
- hydration_policy
- sanitizer_service
- summary_service
- context_lineage_service
- prompt_budget_service
- recall_assist_service
- alias_resolution_service
- receipt_service

No God-file memory engine. No full-context dumping. No keyword-only recall. No exact-name-only retrieval. No uncontrolled memory auto-accept. No silent acceptance of context-breaking transcription artifacts.
