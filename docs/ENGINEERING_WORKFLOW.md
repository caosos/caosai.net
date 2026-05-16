# CAOS Engineering Workflow

Status: standing operating rule
Authority: Michael Chambers
Scope: coding, build, migration, deployment, and repository-agent work across the CAOS ecosystem.

## Permanent operating model

For coding, build, migration, and deployment work:

1. ChatGPT / Aria is the orchestrator, architect, reviewer, and task framer.
2. Codex is the repo worker / coding agent.
3. GitHub repositories are the primary workspace and source of truth.
4. Linode / owned server infrastructure is the runtime target.
5. Michael is the authority, final approver, and facilitator for actions agents cannot physically execute.

## Default flow

```text
Michael gives objective
  -> Aria frames bounded Codex task
  -> Codex works selected GitHub repo
  -> Codex returns report/diff/branch/PR
  -> Aria verifies through GitHub and reviews architecture/risk/correctness
  -> Michael approves
  -> server pulls/builds/runs from GitHub
```

## Verification rule

No agent output is trusted because it sounds confident.

Every repository task must end with:

```text
REMOTE STATE VERIFICATION
VERIFY FILES
VERIFY DIFF
VERIFY VALIDATION
VERIFY NO SECRET LEAK
VERIFY NO OUT-OF-SCOPE CHANGES
RETURN PASS/FAIL
```

Valid task states:

```text
LOCAL WORK DONE
REMOTE PR CREATED
ARIA VERIFIED
MICHAEL APPROVED
```

A task is not complete until the branch or PR is visible in GitHub and the result is independently reviewed.

## Codex usage standard

Use Codex for:

- repo audits;
- file edits;
- deploy scaffolds;
- Docker and compose files;
- test/build attempts;
- branch and PR preparation;
- code review support;
- migration patches.

Do not use Codex as final authority. Codex is a worker, not the product owner.

## Aria usage standard

Use ChatGPT / Aria for:

- architecture;
- task framing;
- migration sequencing;
- Codex prompt design;
- GitHub verification;
- risk review;
- server command planning;
- final recommendation before merge/deploy.

## Michael approval boundary

Michael approves:

- product direction;
- repo boundaries;
- merges;
- server deployments;
- domain cutovers;
- production claims.

Agents may prepare work, but they do not own authority.

## No fallback to old workflow

Do not default back to manual file-by-file patching in chat when a repo-level Codex task is appropriate.

Manual direct GitHub edits are acceptable when:

- Codex is blocked by repo access or publication failure;
- the correction is small and bounded;
- GitHub state can be verified directly;
- the change is documented with receipts.
