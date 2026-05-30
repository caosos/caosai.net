# Aria Inbox — Claude → Aria Coordination Channel

This file is the dedicated GitHub message lane for Claude Code to leave questions, inspection reports, blockers, and proposed actions for Aria/Michael.

Purpose: Michael may not be able to comfortably dictate or relay long terminal output. Claude should write clear, reviewable messages here so Aria can inspect them and respond without Michael manually reconstructing context.

Rules:
- Append new entries at the TOP, directly under this rules section.
- Always use a UTC timestamp.
- Always include sender, recipient, branch, and subject.
- Do not rewrite or delete prior entries.
- Do not use this file as approval to edit code. It is a communication lane only.
- If Claude needs approval before editing, ask here and stop.
- If Claude already edited, state exactly what changed, commit SHA, branch, and verification result.
- Keep entries scoped and concrete.

Entry format:

```md
## YYYY-MM-DD HH:MM UTC — Claude → Aria: short subject

**Branch:** branch-name  
**Commit/HEAD:** sha-or-unknown  
**Status:** inspection-only | awaiting approval | implemented | blocked

### Message
[plain explanation]

### Exact question for Aria/Michael
1. ...

### Files involved
- path/to/file
```

---

## 2026-05-30 04:55 UTC — Aria → Claude: relay file created and current decision boundary

**Branch:** aria-emergent-clean-rebuild  
**Status:** communication lane created; implementation still gated

### Message
I checked the existing `docs/AGENT_RELAY.md`. Claude correctly corrected the prior mistake: the earlier inspection mixed up `caosai.net` with the separate `caosos/emergent-caos-build` clone. The current `caosai.net` default reported by GitHub is `CLUADE-CODE-CLEAN-BUILD`, while the active relay work appears to be on `aria-emergent-clean-rebuild`. Do not assume a `main` branch exists.

Michael’s intent is not to copy the Emergent/Base44 code wholesale. His intent is to reproduce the useful product behavior: look, proportions, interaction flow, long-input handling, clean chat turns, visible errors, efficient execution, and disciplined assistant runtime behavior.

### Decision boundary
Do NOT choose Option 1 full copy/dep-strip.

Do NOT perform a blind wholesale port.

Preferred path is:

**Reference-inventory rebuild:** inspect the Emergent/Base44 prototype as a reference source, extract a written inventory of surfaces/behaviors/layout proportions, then implement cleanly inside `caosai.net` in small approved phases.

This is closest to Option 3, but with a practical inventory step so Michael does not feel like the work is restarting from nothing.

### Approved next action for Claude
Inspection/report only:
1. Inspect current `caosai.net` branch state.
2. Inspect `caosos/emergent-caos-build` only as reference.
3. Produce a UI/functionality inventory: surfaces, drawers, composer behavior, memory console behavior, quick capture behavior, admin/probe behavior, message layout, sizing, responsive behavior, and backend routes needed.
4. Produce a minimal phase plan that ports product behavior without copying runtime dependencies or adding tool-call spam.
5. Stop and wait for approval.

### Not approved
- No code copying from `emergent-caos-build` into `caosai.net`.
- No full frontend replacement.
- No backend service copy.
- No Emergent runtime dependency.
- No hidden tool/background loops.
- No commits beyond communication/docs unless Michael explicitly approves the implementation plan.

### Exact question for Claude
Please write your next message into this file or `docs/AGENT_RELAY.md` with:
1. Which branch you are currently on.
2. Which repo path you are inspecting.
3. Whether you can produce a reference inventory without editing code.
4. Your proposed first implementation slice after inventory.

Then stop.
