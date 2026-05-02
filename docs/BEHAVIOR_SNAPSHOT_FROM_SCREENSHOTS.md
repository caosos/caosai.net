# CAOS Behavior Snapshot From Screenshots

## Purpose

This document preserves visible behavior evidence from Michael's uploaded CAOS screenshots so the rebuild can target actual product behavior instead of vague memory.

Screenshots are evidence. They must be tagged by origin and translated into requirements before implementation.

## Reference origins

| Origin | Use |
|---|---|
| Base44 | Visual/behavior reference and feature-inventory evidence only. No code. Strong reference for starfield depth, translucency, and some menu flows. |
| Emergent | Preferred visual direction and current working feature/behavior reference. No monolith copying. |
| Current/new build | Implementation target and defect comparison surface. |

## Product domains observed

| Domain | Intended role |
|---|---|
| `caosos.com` | Core CAOS platform |
| `caoscare.com` | CAOS Care vertical |
| `caostradings.com` | Trading/finance vertical concept |
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
- Public crawlable pages must describe app-gated features so search engines and users can understand CAOS before login.

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

## Visual direction and starfield

Observed distinction:

- Base44 demonstrates stronger starfield visibility and depth behind translucent surfaces.
- Emergent is preferred for darker shell direction, translucent header treatment, and overall color mood.

Target:

- Use Emergent as preferred final visual direction.
- Preserve Base44-style starfield visibility/depth where appropriate.
- Do not use Base44 code.
- Do not preserve opaque user-message bubble treatment.
- Message bubbles should be translucent, readable, and in the same visual family.

## WCW / context meter

Observed surfaces:

- WCW/token meter visible near the header.
- Example visual state showed approximately `16.8K / 200.0K`.

Rebuild implication:

- WCW is not cosmetic.
- Backend must expose a context/receipt contract that explains measured or estimated context state.
- UI should render from backend-provided contract, not private local guessing only.
- WCW differs by inference engine and must appear in profile/settings, response receipts, and composer/model selector.

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
- Thread search must support partial title match, multi-keyword match, fuzzy spelling tolerance, body/content match, metadata match, and semantic retrieval where available.
- Users should not need exact wording to recover a thread.

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
- Memory retrieval must be relevance-based, not exact-string-only.

## Admin dashboard

Observed surfaces:

- Admin dashboard with user/session/usage metrics.
- Usage charts and 30-day statistics.
- Login method and tier distribution displays.

Rebuild implication:

- Admin routes require server-side authorization.
- Metrics must be backed by durable records, not UI mock state.
- Diagnostics must be gated by admin role.
- Analytics must be privacy-respecting and product-metric focused.

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
- Public docs/landing pages should explain product capabilities without exposing private app data.

## Behavioral priorities for rebuild

1. Testable without Emergent OAuth.
2. Server-side security boundaries.
3. Durable records for memory, tickets, threads, artifacts, and receipts.
4. Modular routes/services/schemas/adapters.
5. Preserve visible CAOS behavior before cosmetic reinvention.
6. No Base44 code.
7. No monolith mirror.
8. Public crawlable pages included in launch plan.
9. Privacy-respecting product analytics only; no ad-surveillance model.
