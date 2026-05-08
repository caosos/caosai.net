# Public Roadmap

This roadmap is intentionally public-facing. It describes direction without exposing private implementation details or sensitive product data.

## Phase 0 — Public Project Framing

Goal: make the project understandable to outside reviewers.

- [x] Public README explains CAOS clearly.
- [x] Public overview document.
- [x] CAOSCare product preview with safety boundary.
- [x] Architecture concepts document.
- [x] Security and disclosure boundary.

## Phase 1 — Clean Rebuild Foundation

Goal: establish a clean server-target foundation.

- [ ] Confirm clean repo layout.
- [ ] Separate prototype salvage from forward-build code.
- [ ] Define backend service boundaries.
- [ ] Define frontend/app boundaries.
- [ ] Define environment/secrets policy.
- [ ] Add minimal local development instructions.
- [ ] Add smoke-test expectations.

## Phase 2 — Memory and Context Core

Goal: build reliable memory behavior before adding broad automation.

- [ ] Memory bin schema.
- [ ] Raw record preservation.
- [ ] Sanitized record generation.
- [ ] Summary/tag/index layer.
- [ ] Selective rehydration policy.
- [ ] Receipt format for memory use.
- [ ] Explicit user-approved learning rules.

## Phase 3 — Tool and MCP Layer

Goal: connect tools through governed interfaces.

- [ ] Tool registry.
- [ ] MCP connector strategy.
- [ ] Permission modes.
- [ ] Tool call receipt format.
- [ ] Tool loop guard.
- [ ] Failure envelope.
- [ ] Admin-visible diagnostics.

## Phase 4 — Model Routing and Worker Agents

Goal: reduce cost and improve speed by routing work intelligently.

- [ ] Model registry.
- [ ] Task classifier.
- [ ] Cheap-worker policy.
- [ ] Strong-synthesis policy.
- [ ] Parallel worker orchestration proof of concept.
- [ ] Cost receipt.
- [ ] Quality comparison harness.

## Phase 5 — E2B / Sandbox Execution Lane

Goal: run code and experiments safely outside production.

- [ ] Define sandbox execution use cases.
- [ ] Add safe command policy.
- [ ] Add file boundary rules.
- [ ] Add output sanitation.
- [ ] Add rollback/checkpoint strategy.

## Phase 6 — CAOSCare MVP

Goal: launch a practical care-workflow MVP.

- [ ] Speech-friendly interaction.
- [ ] Persistent context for care workflows.
- [ ] Staff/resident request logging model.
- [ ] Repeated-call escalation concept.
- [ ] Tablet bridge proof of concept.
- [ ] Dashboard/work queue surface.
- [ ] Safety boundary copy.
- [ ] Private deployment path.

## Phase 7 — CAOSCare Device / Pendant Experiments

Goal: test practical interaction hardware.

- [ ] Existing pendant receiver investigation.
- [ ] Tablet pass-through testing.
- [ ] Voice-note capture workflow.
- [ ] Staff acknowledgement workflow.
- [ ] Escalation timer workflow.
- [ ] Privacy review.

## Phase 8 — Public Feedback Loop

Goal: invite useful criticism without exposing sensitive product internals.

- [ ] Publish public repo link.
- [ ] Ask for architecture feedback.
- [ ] Ask for memory/orchestration criticism.
- [ ] Track issues publicly where appropriate.
- [ ] Keep CAOSCare implementation private until ready.

## Roadmap Principle

The priority is not to chase every agent-tool trend.

The priority is to build a governed, useful system that can survive real workflows:

```text
clear boundaries
+ useful memory
+ safe tools
+ lower cost
+ practical product workflows
```
