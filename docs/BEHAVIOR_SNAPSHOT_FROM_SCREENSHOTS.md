# CAOS Behavior Snapshot From Screenshots

## Purpose

This document preserves the visible behavior evidence from Michael's uploaded CAOS screenshots so the rebuild can target actual product behavior instead of vague memory.

The screenshots themselves were provided in ChatGPT conversation context. This document captures the durable working interpretation inside the GitHub build surface.

## Product domains observed

| Domain | Intended role |
|---|---|
| `caosos.com` | Core CAOS platform |
| `caoscare.com` | CAOS Care vertical |
| `caostradings.com` | Trading/finance vertical |
| `caosconnect.com` | Connector/integration vertical |

## Public and authentication flow

Observed surfaces:

- Public CAOS landing page.
- Guided tour/onboarding modal.
- Google/Emergent login redirect flow.
- Authenticated app shell after login.

Rebuild implication:

- Phase 1 uses development auth so testing is not blocked by Emergent OAuth.
- Production auth remains pluggable and must be implemented through a dedicated auth adapter later.

## Main chat shell

Observed surfaces:

- CAOS/Aria branded chat interface.
- Authenticated user state for Michael Chambers.
- Thread title visible in the top/right area.
- Message composer with send, microphone, attachment, and voice/read controls.
- Starfield/dark UI style.
- Engine/model selector visible.
- Quick thought queue behavior visible.

Rebuild implication:

- Chat page must be feature-composed, not a page monolith.
- Input/composer behavior is a first-class feature module.
- Voice, attachments, quick thoughts, and provider selection must remain separate feature lanes.

## WCW / context meter

Observed surfaces:

- WCW/token meter visible near the header.
- Example visual state showed approximately `16.8K / 200.0K`.

Rebuild implication:

- WCW is not cosmetic.
- Backend must expose a context/receipt contract that explains measured or estimated context state.
- UI should render from backend-provided contract, not private local guessing only.

## Threads and search

Observed surfaces:

- Previous threads panel.
- Thread list with saved/generated titles.
- Search-this-thread modal.
- Search results containing conversation snippets.

Rebuild implication:

- Threads require scoped persistence and user isolation.
- Thread search must be scoped to the authenticated user/session.
- Thread title generation must be preserved as a later service lane.

## Memory console

Observed surfaces:

- Memory console populated with hundreds of atoms.
- Memory categories visible: Identity, Projects, Governance, Preferences, Relationship, Domains, Tech State, Behavioral, Traits, Learning, Real-world, Risk, Counter, Unclassified.
- Atom controls visible: confirm, reclassify, forget.
- Atom metadata visible: source type, confidence, evidence count, priority, date.

Rebuild implication:

- Memory atoms require explicit schemas.
- Promotion must be governed, not silent.
- Admin/user controls must not bypass policy.
- Legacy Plane B/session recall concepts are salvage references, not a direct storage copy.

## Admin dashboard

Observed surfaces:

- Admin dashboard with user/session/usage metrics.
- Usage charts and 30-day statistics.
- Login method and tier distribution displays.

Rebuild implication:

- Admin routes require server-side authorization.
- Metrics must be backed by durable records, not UI mock state.
- Diagnostics must be gated by admin role.

## Support tickets

Observed surfaces:

- Support ticket admin view.
- Status buckets: All, Open, In progress, Resolved, Closed.
- Bug/source metadata, including source via Aria.
- Ticket actions such as In Progress, Resolve, and Close.

Rebuild implication:

- Support tickets require a backend service and schema.
- Admin actions must be server-side authorized.
- Ticket changes should emit receipts/audit metadata.

## Artifacts / desktop

Observed surfaces:

- Stored items visible.
- Files, photos, links, receipts, summaries, seeds, and memory artifacts surfaced.
- File/photo/link tabs or grouped artifact browsing.

Rebuild implication:

- Artifacts need user-scoped storage.
- Generated and uploaded artifacts need distinct metadata.
- Receipts/summaries/seeds must remain first-class artifact types.

## Settings and connectors

Observed surfaces:

- Account/admin settings.
- Permanent memory count.
- Remember Conversations toggle.
- Game Mode, Developer Mode, Multi-Agent Mode toggles.
- Aria Mode and Voice/Speech settings.
- Connector list including Gmail, Drive, Docs, Calendar, GitHub, Slack, Twilio, Telegram, MCP.

Rebuild implication:

- Connector UI must distinguish available, configured, connected, and failed states.
- Remember Conversations must gate actual persistence/promotion behavior.
- Feature toggles must be backed by settings contracts.

## Admin docs / blueprints

Observed surfaces:

- Internal docs/blueprints visible from CAOS UI.
- Examples: CAOS Care playbook, roadmap, changelog, UX/system blueprints, connector sprint plan.

Rebuild implication:

- Docs panel should read from a controlled documentation source.
- Admin/private docs must not leak to normal users.

## Behavioral priorities for rebuild

1. Testable without Emergent OAuth.
2. Server-side security boundaries.
3. Durable records for memory, tickets, threads, artifacts, and receipts.
4. Modular routes/services/schemas/adapters.
5. Preserve visible CAOS behavior before cosmetic reinvention.
6. No Base44 dependency.
7. No monolith mirror.
