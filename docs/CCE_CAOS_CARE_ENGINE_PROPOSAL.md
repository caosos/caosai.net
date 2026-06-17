# CCE — CAOS Council Engine Proposal

Status: proposal / architecture direction  
Scope: CAOS core engine, reusable by CAOSCare and future verticals  
Canonical repo: `caosos/caosai.net`

## Executive decision

CAOS should treat multi-model council orchestration as a core engine capability, not as a vendor feature, marketing add-on, or one-off prompt trick.

The engine name is:

```text
CCE = CAOS Council Engine
```

CCE is the governed trust layer that lets CAOS move beyond one model answering alone. It gives CAOS a repeatable way to route important work through independent workers, contradiction checks, bias/framing checks, source review, synthesis, verification, and receipts.

The first implementation should not start with a giant council. The first implementation should define the contract and ship a small mode ladder:

```text
fast      -> one model, low-risk, low-cost
verified  -> one model plus verifier / critic
council   -> multiple bounded workers plus synthesizer plus verifier
lockdown  -> no AI final answer; human escalation only
```

CAOSCare should use CCE-lite first:

```text
CCE-lite = intent classifier + risk gate + verifier + receipt + human escalation
```

Resident-facing and staff-facing care flows need speed, clarity, audit logs, and escalation more than a heavy multi-model debate on every turn.

## Why this belongs in CAOS

CAOS is already structured around governed context, memory, tools, routing, receipts, diagnostics, and user-owned rules. CCE turns those primitives into a verified decision flow.

Current CAOS primitives that CCE builds on:

- model/provider routing;
- context hydration and memory bins;
- tool and connector governance;
- receipts and lineage;
- bounded worker agents;
- admin-visible diagnostics;
- human approval and escalation.

CCE should not replace those systems. It should coordinate them.

## Core doctrine

One model is a voice. A governed council is a system.

CCE exists to reduce unchecked model failure modes:

- confident wrong answers;
- missing assumptions;
- ideological or emotional framing;
- weak source selection;
- overbroad conclusions;
- unsafe action recommendations;
- undocumented reasoning paths;
- hidden uncertainty;
- one-provider dependence.

The target is not magical neutrality. The target is:

```text
bias-detected
source-grounded
contradiction-checked
risk-gated
receipt-backed
audit-visible
human-governed
```

## CCE is not a political system

CCE is not a party-position engine. It should not be tuned to produce left-wing or right-wing answers.

For civic, policy, government, and public-trust use cases, CCE should separate:

- primary facts;
- source quality;
- legal/procedural constraints;
- left/right/center framing;
- opinion versus reporting;
- consensus versus dispute;
- confidence versus uncertainty;
- recommended next verification steps.

The correct output is not artificial centrism. The correct output is a clear distinction between what is known, what is claimed, what is disputed, and what still needs verification.

## Engine roles

CCE should support a configurable role set. Not every turn wakes every role.

### Router / dispatcher

Classifies the request and selects the mode.

Outputs:

```text
cce_mode
risk_level
selected_worker_roles
allowed_tools
required_receipts
stop_conditions
```

### Primary worker

Produces the initial useful answer, plan, extraction, or draft.

### Research worker

Finds and summarizes evidence when sources matter.

Rules:

- prefer primary sources;
- separate direct evidence from commentary;
- record source gaps;
- do not inflate certainty.

### Opposition / red-team worker

Attacks the answer.

Questions:

- What is missing?
- What assumption is doing too much work?
- What would a critic say?
- What could be unsafe, misleading, or incomplete?
- What would change the conclusion?

### Bias / framing worker

Identifies loaded wording, one-sided source pools, cherry-picked evidence, and hidden normative assumptions.

### Domain safety worker

Checks lane-specific boundaries.

Examples:

- CAOSCare: resident safety, privacy, human oversight, no autonomous medical authority.
- Government/civic: law, process, public record, auditability.
- Finance: no unsupported investment certainty.
- Health: no diagnosis or treatment authority without proper scope.

### Synthesizer

Builds the final answer from worker outputs while preserving facts, material disagreement, source limits, confidence, and next safe steps.

### Verifier / gatekeeper

Final pass before user-visible output or system action.

Possible gate decisions:

```text
allow
allow_with_caveats
ask_for_missing_information
escalate_to_human
block_action
create_ticket_or_record
require_admin_review
```

## Mode ladder

### Fast Mode

Use when being slightly wrong is low consequence and speed matters.

Shape:

```text
router -> primary model -> response + lightweight receipt
```

### Verified Mode

Use when the answer matters, but full council is unnecessary.

Shape:

```text
router -> primary model -> verifier/critic -> final response + receipt
```

### Council Mode

Use when error cost, ambiguity, ideology, source quality, or strategic impact is high.

Shape:

```text
router
  -> worker panel
  -> opposition / bias / safety checks
  -> synthesizer
  -> verifier
  -> final response + council receipt
```

### Lockdown Mode

Use when the system should not answer as authority.

Shape:

```text
router -> block/escalate -> receipt
```

## Source doctrine

CCE should prefer sources in this order:

1. Primary sources: statutes, court filings, official records, transcripts, raw data, original studies, direct statements.
2. Institutional sources: auditors, watchdogs, universities, standards bodies, regulators, official agencies.
3. Reputable reporting: labeled as reporting and checked against primary evidence where possible.
4. Ideological/opinion sources: allowed when relevant, but labeled as framing or commentary.
5. Unverified claims: surfaced only as claims, never as established facts.

Receipt source posture:

```text
source_mode
primary_source_count
ideological_span
known_gaps
citation_quality
unverified_claims
```

## Receipt requirements

Minimum CCE receipt fields:

```text
cce_mode
worker_roles_used
models_used
provider_mix
reason_for_mode
risk_level
source_mode
claims_checked
contradictions_found
bias_or_framing_flags
safety_flags
human_escalation_required
confidence
cost_estimate
latency_ms
final_gate_decision
```

## CAOSCare integration decision

CAOSCare needs trust today, but it does not need full CCE on every resident/staff interaction.

CAOSCare should use:

```text
CCE-lite = router + risk gate + verifier + receipt + human escalation
```

The care product should sell operational trust, not multi-model complexity.

What senior care needs first:

- resident heard;
- right staff notified;
- task/alert documented;
- family/staff communication cleaned up;
- unsafe medical/legal authority avoided;
- private data protected;
- leadership can inspect what happened.

Full CCE can be enabled later for policy creation, serious incident review, family dispute summaries, regulatory/compliance-adjacent research, architecture decisions, care workflow redesign, and multi-source research.

## Proposed implementation phases

### Phase 0 — Documentation contract

Add this proposal and update README / architecture docs.

### Phase 1 — Data contract

Add internal schema/constants for:

```text
cce_mode
risk_level
worker_role
cce_receipt
final_gate_decision
```

### Phase 2 — Verified Mode

Add one verifier/critic pass behind an admin or feature flag.

### Phase 3 — CAOSCare CCE-lite

Expose CCE-lite to care flows: request classification, staff notes, family update drafts, incident/handoff summaries, and privacy/safety gates.

### Phase 4 — Council Mode

Add configurable worker panels for admin/research/civic/architecture workflows.

### Phase 5 — Builder/admin UX

Expose mode selected, why selected, what was checked, what was blocked, source posture, cost, and latency.

## Acceptance criteria

CCE is real when CAOS can answer:

```text
Why did this turn use this mode?
Which model(s) worked on it?
What did the verifier check?
What contradictions or risks were found?
What sources supported the answer?
What was blocked or escalated?
What confidence was assigned?
Where is the receipt?
```

CAOSCare CCE-lite is real when staff/admin can answer:

```text
What did the resident/staff/family ask?
What action was taken?
Who was notified?
Was a human required?
Was private or medical-adjacent content protected?
What receipt proves the flow?
```

## Final product position

CCE is the trust engine.

CAOS is the governed operating system.

CAOSCare is the senior-care product using the engine in a practical, fast, human-supervised way.

The platform should not be valuable because it merely has AI. It should be valuable because it makes AI behave like it is being audited before it speaks or acts.
