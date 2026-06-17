# AGENTS.md — CAOS Agent Protocol

This file is the mandatory entry point for AI agents inspecting or modifying this repository.

## Repository role

`caosos/caosai.net` is the canonical public clean-rebuild home for CAOS.

This repo should document and build the public CAOS architecture without exposing private CAOSCare implementation details, facility data, resident/staff/family data, secrets, tokens, or operational screenshots.

## Operating mode

Default mode is inspect-first.

Before writing code or changing architecture, read:

1. `README.md`
2. `docs/CAOS_PUBLIC_OVERVIEW.md`
3. `docs/ARCHITECTURE_CONCEPTS.md`
4. `docs/CCE_CAOS_CARE_ENGINE_PROPOSAL.md`
5. `docs/CAOSCARE_PRODUCT_PREVIEW.md`
6. `docs/PUBLIC_ROADMAP.md`
7. `SECURITY.md`
8. `CONTRIBUTING.md`

If a listed file does not exist in the current branch/ref, record that fact instead of inventing behavior.

## CCE build rule

CCE means:

```text
CCE = CAOS Council Engine
```

CCE is the proposed CAOS trust engine for model routing, verifier passes, risk gates, source posture, council-mode synthesis, confidence, audit receipts, and human escalation.

Build CCE in small, testable slices. Do not attempt the entire dream in one PR.

Required mode ladder:

```text
fast      -> one model / low-risk path
verified  -> primary model plus verifier / critic
council   -> multiple bounded workers plus synthesizer plus verifier
lockdown  -> no AI final answer; human escalation only
```

## CAOSCare boundary

CAOSCare should use CCE-lite first:

```text
CCE-lite = intent classifier + risk gate + verifier + receipt + human escalation
```

CAOSCare remains assistive, advisory, human-supervised, privacy-aware, and receipt-backed. Do not add autonomous medical judgment, emergency-service replacement, medical-device claims, clinical authority, or compliance guarantees.

## Preserve list

Do not remove or silently degrade:

- user-owned memory direction
- model routing direction
- receipts and auditability
- context hygiene / hydration doctrine
- tool governance
- worker-agent boundaries
- CAOSCare safety boundary
- public/private separation
- no-secrets discipline

## Change discipline

Use small PRs.

For code:

1. Inspect existing structure first.
2. Add focused modules rather than God files.
3. Keep runtime behavior gated behind clear policy or feature flags where appropriate.
4. Add tests or at minimum deterministic examples for any runtime logic.
5. Preserve public/private boundaries.

For documentation:

1. Mark proposal, planned, prototype, and implemented status clearly.
2. Keep docs searchable for future agents.
3. Update `README.md` or relevant indexes when adding important docs.

## Stop conditions

Stop and report before acting if a task would:

- expose secrets, tokens, private data, or facility/resident/staff information;
- deploy to production without explicit Michael approval;
- imply autonomous clinical/legal/emergency authority;
- remove receipts, memory, model routing, tool governance, or safety boundaries;
- perform destructive repo/server changes without explicit approval.
