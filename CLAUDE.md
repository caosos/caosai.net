# CAOS — Claude Code Session Bootstrap

## Read first on every session start

1. `docs/START_HERE_AGENT_ONBOARDING.md` — current task state, what's done, what's next
2. `docs/REFERENCE_SOURCE_MAP.md` — required before touching any frontend surface

Do not write code until you have read both. Do not ask Michael to paste context — it is in the docs.

## Repo identity

- **Repo:** `caosos/caosai.net`
- **Branch:** `aria-emergent-clean-rebuild`
- **Server:** Linode `172.234.25.199` — SSH as `michael-chambers`
- **Local path:** `/home/michael-chambers/caosai.net`

## Non-negotiables

- No silent code mutation
- No writes to `main`
- No production deploys without explicit approval
- No Base44 code — screenshots only
- Every meaningful action gets a receipt
- Inspect before write

## How Michael restarts a session

Michael says something short: "continue", "read issue X", or "pick up where we left off."
That is enough. Read `START_HERE_AGENT_ONBOARDING.md` and proceed.

## After each work session

Update `docs/START_HERE_AGENT_ONBOARDING.md` → `CURRENT SESSION STATE` section with:
- What was completed
- Current file state
- Next approved tasks

This is how context survives restarts.
