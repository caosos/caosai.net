# Codex Issue Body — Build CCE v0.1

Codex: build the first small, testable CCE slice in `caosos/caosai.net`.

Base branch: `CLUADE-CODE-CLEAN-BUILD`

Read first:

- `AGENTS.md`
- `docs/CCE_CAOS_CARE_ENGINE_PROPOSAL.md`
- `docs/CODEX_CCE_V0_BUILD_TASK.md`
- `docs/CODEX_PROMPT_CCE_V0_1.md`
- `docs/ARCHITECTURE_CONCEPTS.md`

Mission:

Implement CCE v0.1 as a deterministic policy/data-contract skeleton, not a full multi-model council.

Must support modes:

```text
fast
verified
council
lockdown
```

Acceptance criteria:

- deterministic policy selection for baseline rules;
- receipt shape with required fields;
- tests for fast / verified / council / lockdown / lockdown-overrides-council / receipt fields;
- `docs/CCE_V0_IMPLEMENTATION_NOTES.md` added;
- no deployment, no provider API calls, no autonomous tool execution, no secrets, no private CAOSCare data.

Return a small PR with summary, changed files, tests run, limitations, and next safe step.
