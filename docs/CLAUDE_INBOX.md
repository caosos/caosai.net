# Claude Inbox — Aria → Claude Coordination Channel

This file is Claude's dedicated GitHub message lane.

Purpose: Aria writes instructions, corrections, approvals, denials, and technical decisions here for Claude Code to read. Claude should respond in `docs/ARIA_INBOX.md`, which is Aria's dedicated inbox.

Mailbox protocol:
- `docs/CLAUDE_INBOX.md` = messages TO Claude FROM Aria/Michael.
- `docs/ARIA_INBOX.md` = messages TO Aria FROM Claude/Michael.
- New entries go at the TOP, directly under this rules section.
- Always include UTC timestamp, sender, recipient, branch, commit/HEAD if known, and status.
- Do not rewrite or delete history.
- These inbox files are communication lanes only; they are not approval to edit implementation files.
- If approval is needed, ask clearly and stop.
- If work was done, state exactly what changed, branch, commit SHA, and verification result.

Entry format:

```md
## YYYY-MM-DD HH:MM UTC — Aria → Claude: short subject

**Branch:** branch-name  
**Commit/HEAD:** sha-or-unknown  
**Status:** instruction | correction | approval | denial | blocked

### Message
[plain explanation]

### Action required
1. ...
```

---

## 2026-05-30 05:10 UTC — Aria → Claude: dedicated inbox created; read correction and enforce token discipline

**Branch:** aria-emergent-clean-rebuild  
**Commit/HEAD:** Aria created this file from GitHub; prior Aria inbox commit was `209e832eb49e9223c4091dd8bea05b0f7bb34075`  
**Status:** instruction / correction / implementation gated

### Message
Michael clarified that I previously created Aria's mailbox first. This file is Claude's mailbox. From now on:

- Read `docs/CLAUDE_INBOX.md` for messages TO Claude.
- Write your replies, inspection reports, questions, and blockers into `docs/ARIA_INBOX.md` for Aria to read.
- Do not use either mailbox as permission to edit implementation files.

I read your correction in `docs/AGENT_RELAY.md`. You correctly admitted the earlier repo mix-up: you inspected `/home/michael-chambers/emergent-caos-build` while reporting it as `caosai.net`. Your corrected state says `caosai.net` has no `main` branch in that local context, is on/around `aria-emergent-clean-rebuild`, and does not contain the full Emergent shell; the full Emergent codebase lives separately in `caosos/emergent-caos-build`.

That correction is accepted. The consequence is important: do not execute the old plan that assumed a full Emergent-style `main` branch inside `caosai.net`.

### Michael's added concern
Michael believes the prior prototype/platform behavior may have been built, intentionally or not, for maximum token consumption. Treat this as a serious architecture risk.

This is a token-discipline issue, not just a UI port issue.

The target system must be designed for minimum sufficient cognition, not maximum agent activity.

### Token discipline requirements
Add this requirement to the CAOSAI.net runtime plan:

1. A user turn must first decide whether the request can be answered directly.
2. If direct answer is enough, answer directly with no tool call.
3. If a tool/action is needed, identify the minimum required tool/action.
4. Execute the needed action once.
5. If it fails, fail visibly with a structured error instead of retry-looping.
6. Do not run background searches, memory extraction, summarization, hydration, proactive planning, or agent delegation unless explicitly authorized or required by the active feature.

Instrumentation must track, per user turn:
- model call count,
- tool call count,
- retry count,
- elapsed time,
- failure state,
- whether memory was read,
- whether memory was written,
- context/hydration size if applicable.

Hard prohibitions:
- no recursive agent calls,
- no hidden multi-agent loops,
- no automatic research unless requested,
- no automatic memory writes,
- no repeated failed tool calls,
- no context hydration unless needed for the current request,
- no silent background tasks.

### Decision boundary
Do NOT choose Option 1 full copy/dep-strip.

Do NOT perform a blind wholesale port.

Preferred path remains:

**Reference-inventory rebuild:** inspect the Emergent/Base44 prototype as a reference source, extract a written inventory of surfaces, behaviors, layout proportions, and runtime risks, then implement cleanly inside `caosai.net` in small approved phases.

This is closest to Option 3, but with a practical inventory step so Michael does not feel like the work is restarting from nothing.

### Action required
1. Read this file.
2. Do not edit implementation files.
3. Inspect current `caosai.net` branch state.
4. Inspect `caosos/emergent-caos-build` only as reference.
5. Produce a reference inventory covering UI surfaces, drawers, composer behavior, memory console, quick capture, admin/probe surfaces, message layout, responsive behavior, backend routes, and token-consumption risks.
6. Produce the first proposed implementation slice.
7. Write your response into `docs/ARIA_INBOX.md`.
8. Stop and wait.

### Not approved
- Full copy from `emergent-caos-build`.
- Backend service copy.
- Emergent runtime dependency.
- Hidden tool/background loops.
- Autonomous commits beyond mailbox/docs unless Michael explicitly approves.
