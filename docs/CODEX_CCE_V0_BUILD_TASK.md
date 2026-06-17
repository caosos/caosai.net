# Codex Build Task — CCE v0.1 Policy Skeleton

Status: ready for Codex / small build package  
Target repo: `caosos/caosai.net`  
Target branch: `CLUADE-CODE-CLEAN-BUILD` or a new branch from it  
Do not deploy.

## Mission

Build the first small, testable slice of CCE — CAOS Council Engine.

CCE v0.1 is not a full multi-model council. It is the policy/data-contract skeleton that future runtime work can use.

## Required first read

Read these before editing:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE_CONCEPTS.md`
4. `docs/CCE_CAOS_CARE_ENGINE_PROPOSAL.md`
5. `docs/CAOSCARE_PRODUCT_PREVIEW.md`

If the active repository is not `caosos/caosai.net`, stop and return:

```text
WRONG_REPOSITORY_CONTEXT
```

## Build scope

Create a small, dependency-light CCE policy skeleton.

Recommended files, adjusted to fit the existing repo structure after inspection:

```text
src/cce/policy.*
src/cce/types.*
src/cce/receipt.*
src/cce/index.*
tests/cce/policy.test.*
docs/CCE_V0_IMPLEMENTATION_NOTES.md
```

If this repo uses a different language/framework, match the existing conventions. If no runtime source tree exists, create the smallest reasonable source/test structure and document how to run it.

## Required behavior

Implement deterministic policy selection for the four CCE modes:

```text
fast
verified
council
lockdown
```

Inputs should support at minimum:

```text
request_text
surface
actor_role
risk_hint
requires_sources
requires_action
care_related
medical_or_emergency_boundary
privacy_sensitive
admin_requested_council
```

Outputs should include at minimum:

```text
cce_mode
risk_level
reason_for_mode
worker_roles
requires_verifier
requires_human_escalation
receipt_required
stop_conditions
```

## Baseline policy rules

Use clear deterministic rules first:

1. Medical/emergency boundary -> `lockdown` + human escalation.
2. Privacy-sensitive care workflow -> at least `verified`.
3. Admin-requested council -> `council`, unless lockdown condition exists.
4. Source-heavy public/policy/government question -> `verified` or `council` depending risk.
5. Low-risk general request -> `fast`.
6. Any action with unclear safety -> `verified` or `lockdown` depending severity.

## Receipt shape

Add a receipt builder or receipt interface with at least:

```text
cce_mode
risk_level
worker_roles_used
reason_for_mode
claims_checked
contradictions_found
bias_or_framing_flags
safety_flags
human_escalation_required
confidence
final_gate_decision
```

For v0.1, empty arrays/defaults are acceptable where no runtime workers exist yet.

## Tests

Add tests for at least:

1. low-risk request -> fast
2. family/staff/care-sensitive request -> verified
3. admin council request -> council
4. medical/emergency/autonomous authority request -> lockdown
5. lockdown overrides council
6. receipt builder includes required fields

## Documentation

Add `docs/CCE_V0_IMPLEMENTATION_NOTES.md` explaining:

- what was implemented;
- what is intentionally not implemented;
- how to run tests;
- how this connects to future CCE worker panels;
- how CAOSCare should use CCE-lite first.

Update `README.md` or an existing docs index only if needed to make the new implementation discoverable.

## Explicit non-goals

Do not build:

- full multi-model orchestration;
- provider API calls;
- autonomous tool execution;
- production deployment;
- CAOSCare private implementation;
- resident/staff/facility examples using real people;
- medical, legal, emergency-service, or compliance authority claims.

Do not add secrets, tokens, env values, or private operational data.

## Acceptance criteria

The PR is acceptable when:

- CCE v0.1 policy selection is deterministic.
- Tests cover the baseline policy rules.
- The implementation is small and easy to replace/extend.
- Documentation explains v0.1 and next steps.
- No production deploy or private data exposure occurred.
