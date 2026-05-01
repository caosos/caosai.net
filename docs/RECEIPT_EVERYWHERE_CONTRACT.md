# Receipt Everywhere Contract

## Purpose

Every meaningful CAOS action must produce a legible receipt. Receipts are not decoration; they are the audit trail, user trust layer, debugging substrate, and continuity memory for the system.

## Core rule

If CAOS changes state, uses a capability, selects a model, writes memory, hydrates context, calls a connector, updates an artifact, changes settings, or performs admin work, it must produce a receipt.

## Receipt questions

A mature receipt should answer:

- What happened?
- Who/what initiated it?
- When did it happen?
- Why did it happen?
- What changed?
- What source/context/memory justified it?
- What model/provider/tool was used, if any?
- What metrics are available?
- What was skipped or excluded?
- Was the action local, provider-backed, connector-backed, or degraded?
- Was user approval required?
- Was user approval present?

## Required receipt domains

Receipts must exist for:

- chat turns
- model/provider selection
- WCW/context budget changes
- memory create/update/reclassify/forget
- ARC hydration decisions
- sanitizer truncation/compression
- prompt budget inclusion/exclusion
- connector/tool calls
- file/photo/link/artifact creation
- support ticket creation/status changes
- admin actions
- settings/profile changes
- deployment/system operations
- errors/degraded responses

## Receipt legibility

Receipts should be machine-readable and human-legible.

They should not expose secrets, raw credentials, private provider tokens, or full sensitive payloads unless explicitly safe and scoped.

## Minimum receipt fields

```text
receipt_id
event_type
actor_type
actor_id
reason
status
created_at
summary
metrics
inputs
outputs
changes
memory_refs
context_refs
model_ref
approval
error
```

## Non-negotiable

No silent state changes.
No invisible model switches.
No hidden memory writes.
No unreceipted connector/tool calls.
No admin mutation without a receipt.
