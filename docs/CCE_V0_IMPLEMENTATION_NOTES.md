# CCE v0.1 Implementation Notes

Status: implemented policy skeleton / not a full runtime council  
Scope: deterministic CAOS Council Engine mode selection and receipt contract

## What was implemented

CCE v0.1 adds a small backend policy package under `backend/app/cce/`:

- `types.py` defines the minimum policy input and output contracts.
- `policy.py` implements deterministic mode selection for `fast`, `verified`, `council`, and `lockdown`.
- `receipt.py` defines the minimum CCE receipt shape and a receipt builder with safe v0.1 defaults.
- `__init__.py` exports the small public surface for future backend integration.

The policy supports the v0.1 input concepts from the build task:

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
action_safety_clear
```

The policy returns:

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

## Deterministic baseline rules

The current v0.1 rules are intentionally simple:

1. Medical, emergency, or autonomous authority boundary selects `lockdown` and requires human escalation.
2. Unsafe high-risk action requests select `lockdown`; lower-risk unclear actions select `verified`.
3. Admin-requested council selects `council`, unless a lockdown condition exists.
4. Privacy-sensitive care workflow selects at least `verified`.
5. Source-heavy requests select `verified`, or `council` when the risk hint is high or critical.
6. Low-risk general requests select `fast`.

## Receipt shape

`build_cce_receipt` produces the minimum CCE audit fields:

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

Because no worker runtime exists in v0.1, claims, contradiction, and bias/framing arrays default to empty lists unless a caller supplies them.

## How to run tests

From the repository root:

```bash
PYTHONPATH=backend pytest backend/tests/cce
```

## What is intentionally not implemented

CCE v0.1 does not add:

- multi-model orchestration;
- provider API calls;
- autonomous tool execution;
- production deployment behavior;
- private CAOSCare implementation details;
- resident, staff, facility, or family data;
- medical, legal, emergency-service, or compliance authority.

## Future CCE worker-panel connection

Future CCE runtime work can use this policy result as the dispatch contract:

```text
request
  -> select_cce_policy
  -> mode + worker roles + stop conditions
  -> future bounded workers / verifier / synthesizer
  -> build_cce_receipt
  -> final answer, routed action, or escalation
```

The `worker_roles` output is only advisory in v0.1. A future orchestrator should map these role names to actual bounded workers, source posture checks, verifier passes, and receipt-backed final gate decisions.

## CAOSCare CCE-lite guidance

CAOSCare should use CCE-lite first:

```text
CCE-lite = intent classifier + risk gate + verifier + receipt + human escalation
```

For CAOSCare-shaped workflows, the policy should preserve the public safety boundary: assistive, advisory, privacy-aware, receipt-backed, and human-supervised. It must not claim autonomous medical judgment, emergency-service replacement, clinical authority, or compliance guarantees.
