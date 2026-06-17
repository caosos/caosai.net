# Copyable Codex Prompt — Build CCE v0.1

Use this exact prompt for Codex.

---

ACTIVE REPO MUST BE: `caosos/caosai.net`  
BASE BRANCH MUST BE: `CLUADE-CODE-CLEAN-BUILD`

If you are not in `caosos/caosai.net`, stop and return exactly:

```text
WRONG_REPOSITORY_CONTEXT
```

## Mission

Build the first small, testable slice of CCE — CAOS Council Engine.

Do not build the whole multi-model council yet. Build the v0.1 deterministic policy/data-contract skeleton that future runtime work can use.

## Read first

Read:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE_CONCEPTS.md`
4. `docs/CCE_CAOS_CARE_ENGINE_PROPOSAL.md`
5. `docs/CODEX_CCE_V0_BUILD_TASK.md`
6. `docs/CAOSCARE_PRODUCT_PREVIEW.md`

## Build requirements

Implement CCE v0.1 with deterministic selection for:

```text
fast
verified
council
lockdown
```

Create or adapt the smallest reasonable source structure after inspecting the repo. Suggested structure:

```text
src/cce/policy.*
src/cce/types.*
src/cce/receipt.*
src/cce/index.*
tests/cce/policy.test.*
docs/CCE_V0_IMPLEMENTATION_NOTES.md
```

If the repo already uses a different runtime/language convention, follow it.

## Required input fields

Support these input concepts:

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

## Required output fields

Return at least:

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

## Baseline rules

1. Medical/emergency/autonomous authority boundary -> `lockdown` + human escalation.
2. Privacy-sensitive care workflow -> at least `verified`.
3. Admin requested council -> `council`, unless lockdown exists.
4. Source-heavy public/policy/government question -> `verified` or `council` depending risk.
5. Low-risk general request -> `fast`.
6. Any action with unclear safety -> `verified` or `lockdown` depending severity.
7. Lockdown overrides council.

## Receipt builder

Add a receipt interface/builder with at least:

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

For v0.1, empty arrays/defaults are acceptable where no runtime workers exist.

## Tests

Add deterministic tests for:

1. low-risk request -> fast
2. family/staff/care-sensitive request -> verified
3. admin council request -> council
4. medical/emergency/autonomous authority request -> lockdown
5. lockdown overrides council
6. receipt builder includes required fields

## Docs

Add `docs/CCE_V0_IMPLEMENTATION_NOTES.md` explaining:

- what was implemented;
- how to run tests;
- what is intentionally not implemented;
- how this connects to future verifier passes and council workers;
- how CAOSCare should use CCE-lite first.

## Hard limits

Do not deploy.  
Do not add provider API calls.  
Do not add autonomous tool execution.  
Do not expose secrets, tokens, env values, private CAOSCare implementation details, facility data, resident/staff/family data, or real care examples.  
Do not claim medical, legal, emergency-service, or compliance authority.

## PR result

Open a small PR with:

- summary;
- changed files;
- tests run;
- acceptance criteria status;
- known limitations;
- next safe step.
