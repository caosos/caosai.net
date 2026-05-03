# CAOS Ownership Migration Map

## Purpose

This document defines the migration path for taking ownership of the already-working CAOS system outside Emergent.

This is not a from-zero rebuild plan.

Michael has already built working CAOS systems. The immediate objective is to move the working source under Michael-controlled server infrastructure, preserve behavior, and only then refactor.

## Active lane

```text
Lane: CAOS Core ownership migration
```

Do not mix this lane with CAOS Care migration. CAOS Care is separate.

## Source of working behavior

```text
Repository: caosos/emergent-caos-build
Clone URL: https://github.com/caosos/emergent-caos-build.git
Branch: main
Role: Working CAOS source exported from Emergent build
```

This repository contains the working CAOS app behavior and should be treated as the source to deploy first.

## Target ownership repo

```text
Repository: caosos/linode-repo
Branch: aria-emergent-clean-rebuild
Role: Linode ownership/migration planning, doctrine, clean target architecture, and future controlled extraction workspace
```

`linode-repo` is not the current working app source. It is the migration/control repo and clean target lane.

## Server target

Preferred production/runtime directory:

```text
/srv/caosos.com
```

Do not place the working CAOS app under:

```text
/home/michael-chambers/caos-a1
```

CAOS A1 is a separate legacy/project directory and must not be used as the parent for the self-hosted CAOS Core platform.

## Correct mental model

```text
emergent-caos-build = working source to move
linode-repo = migration/control/doctrine/clean target workspace
/srv/caosos.com = server runtime target
```

## Migration principle

```text
Move first. Verify behavior. Then refactor.
```

Do not combine migration, refactor, redesign, provider changes, and frontend polish in one step.

## Phase 1 — Take server custody

Goal: run the current working CAOS source from `emergent-caos-build` on Michael-controlled Linode infrastructure.

Steps:

1. Create isolated server directory `/srv/caosos.com`.
2. Clone `https://github.com/caosos/emergent-caos-build.git` into that directory.
3. Create backend environment file from inspected requirements/config.
4. Install backend dependencies.
5. Install frontend dependencies.
6. Configure MongoDB or existing database connection.
7. Start backend locally on server.
8. Build frontend locally on server.
9. Serve frontend through Nginx.
10. Add HTTPS through Let's Encrypt.
11. Verify critical routes and UI behavior.

## Phase 1 acceptance checks

Minimum checks before refactor:

- backend boots
- database connection works
- frontend builds
- landing/auth shell loads
- login/auth flow works or has exact failure receipt
- chat page loads
- admin docs route loads
- support tickets/admin surface loads
- memory console route loads
- context/window meter surface loads if present
- no Emergent runtime dependency blocks normal operation

## Phase 2 — Environment and dependency map

The working source requires inspection before server launch.

Known required files to inspect:

- `backend/server.py`
- `backend/app/config.py`
- `backend/requirements.txt`
- `frontend/package.json`
- frontend environment variables
- backend environment variables
- object storage configuration
- auth/session configuration
- connector/OAuth configuration
- billing/webhook configuration
- MongoDB configuration

Important current finding:

`backend/app/config.py` requires:

```text
MONGO_URL
DB_NAME
```

It also reads optional:

```text
CORS_ORIGINS
```

## Phase 3 — Server-to-GitHub custody loop

After the app runs on the server, CAOS must support a safe commit path back to GitHub.

Required feature:

```text
Commit Workspace to GitHub
```

Minimum workflow:

1. Inspect git status.
2. Show changed files.
3. Show diff.
4. Generate commit message.
5. Require Michael approval.
6. Commit locally.
7. Push selected branch to GitHub.
8. Store receipt with commit SHA.

Forbidden without explicit approval:

- force push
- delete repo directory
- overwrite production database
- rotate secrets
- restart production service
- deploy to production
- change firewall
- push to protected/main without review

## Phase 4 — Refactor only after ownership

Refactor begins only after the working app runs on Michael's server.

Refactor workflow:

```text
inspect
map responsibility
extract one piece
preserve behavior
test
commit
receipt
stop
```

Line policy:

```text
Target: <= 200 lines per code file where practical
Hard cap: 400 lines unless Michael explicitly approves exception
Docs/contracts/vault files may be longer
```

## Repo relationship decision

Initial recommendation:

- Do not copy all working source into `linode-repo` immediately.
- First deploy `emergent-caos-build` directly to `/srv/caosos.com`.
- Use `linode-repo` to hold migration doctrine, checklists, contracts, and future clean extraction targets.
- Once the working system is owned and running, decide whether to:
  - keep `emergent-caos-build` as runtime repo, or
  - promote/copy working source into `linode-repo`, or
  - create a new canonical `caosos.com` runtime repo.

Do not make that repo consolidation decision during the first migration step.

## Why this order

The working system already exists.

Destroying or rewriting it before server custody creates avoidable risk.

The correct first win is:

```text
CAOS runs from Michael's server instead of Emergent.
```

Then the system can be measured, cleaned, refactored, and extended under Michael's control.

## Current source confirmation

Michael confirmed the source code repository:

```text
https://github.com/caosos/emergent-caos-build.git
```

This is the repository to clone for the first CAOS Core ownership migration.
