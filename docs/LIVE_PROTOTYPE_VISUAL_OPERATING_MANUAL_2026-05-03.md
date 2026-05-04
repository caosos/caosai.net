# Live Prototype Visual Operating Manual

Date: 2026-05-03
Repository: caosos/linode-repo
Branch: aria-emergent-clean-rebuild
Status: Working evidence manual, v1
Authoring context: Built from visually inspected CAOS screenshots supplied by Michael and existing repo documentation.

## Purpose

This manual records what is visibly proven about the live CAOS prototype systems so the new Linode-owned build can preserve real working behavior instead of rebuilding from vague memory.

This is not a final product specification. It is a visual operating manual and evidence report. Michael will fill in behavioral blanks where screenshots cannot prove runtime behavior.

## Core correction

Base44 and Emergent are not dead historical builds.

They are live working prototype systems.

The forward build lane is moving to the Linode repository because Michael is not investing more time or money into those hosted prototype platforms. They remain active behavioral and visual references unless Michael explicitly deprecates or supersedes them.

## Build lineage and current authority

### Base44 / Basecamp 4 Deno serverless prototype

- Status: live working prototype/reference system.
- Role: visual, behavioral, architecture, and UX reference.
- Constraint: do not continue primary investment there unless Michael reauthorizes it.
- Code posture: reference only unless explicitly approved.

### Emergent full-stack prototype

- Status: live working prototype/reference system.
- Role: strongest current full-stack visual and behavioral evidence lane.
- Constraint: do not spend more money or primary development effort there unless Michael reauthorizes it.
- Code posture: extract behavior contracts; do not copy monoliths wholesale.

### Linode repo / new owned build

- Status: forward build lane.
- Repository: caosos/linode-repo.
- Current branch observed: aria-emergent-clean-rebuild.
- Role: clean owned implementation target.
- Doctrine: preserve proven live behavior, remove platform contamination, build modular owned services.

## Evidence doctrine

Screenshots are live behavioral evidence.

They are not decoration, mockups, or vague inspiration. A visible surface proves at minimum that the prototype had a designed and reachable UI state. Runtime details not visible in screenshots must be labeled as unknown until Michael confirms or repo/runtime code proves them.

Required future behavior:

- Do not claim a feature does not exist until visual evidence and docs have been inspected.
- Do not describe proven live systems as past-tense dead prototypes.
- Do not conflate live reference systems with the forward build lane.
- Preserve proven behavior unless Michael explicitly removes it.
- Rebuild cleanly in the Linode-owned architecture.

## Visual identity and shell

Observed visual system:

- Dark purple/black cosmic/starfield background.
- Large centered CAOS branding on public entry surfaces.
- Translucent cards and panels with purple borders/glow.
- Rounded panels and modal shells.
- White/soft text hierarchy with purple and teal/green accents.
- Browser-visible domain: caosos.com.

Operating implication:

The visual identity is already strong enough to be treated as a product identity. The clean build should not randomly redesign it. Refinement is allowed, replacement is not assumed.

## Public landing surface

Observed elements:

- CAOS logo/mark.
- Title: CAOS.
- Subtitle: Cognitive Adaptive Operating System.
- Description: personal AI platform language.
- Feature cards:
  - Persistent Memory.
  - Web Search.
  - File Intelligence.
  - Voice Ready.
- Primary action: Take the Tour.
- Secondary action: Sign In.
- Guest option: Continue as Guest.

Operating implications:

- The public app already has an onboarding gateway.
- The product promise is persistent memory, web capability, file intelligence, and voice.
- The new build needs a public landing route and a logged-out mode, not only an authenticated chat surface.

Behavioral blanks for Michael:

- Whether guest mode stores temporary session state.
- Whether guest mode permits tools, files, memory, or voice.
- Whether landing content should be SEO/crawlable or app-rendered only.

## Guided onboarding tour

Observed tour steps:

1. Start here.
2. Your threads.
3. Aria remembers.
4. Attach anything.
5. Get started.

Observed behavior:

- Modal overlay blurs/dims the landing surface behind it.
- Step progress indicator is visible at top of modal.
- Next button advances step.
- Skip tour control exists.
- Close control exists.

Operating implications:

- Onboarding is not hypothetical; it exists as a guided product surface.
- The clean build should preserve first-run guidance.
- Tour content should explain actual core behaviors: chat, thread continuity, memory, attachments, and starting cleanly.

Behavioral blanks for Michael:

- Whether tour completion is stored per user.
- Whether tour can be reset from settings.
- Whether guest and signed-in users see the same tour.

## Authentication handoff

Observed elements:

- Emergent auth domain shown during redirect.
- Login title: LOG IN TO Caosos.
- Continue with Google button.
- reCAPTCHA/legal text.
- Emergent-secured login footer.

Operating implications:

- Authentication worked through the Emergent-hosted auth flow.
- The clean Linode build must replace this with owned/pluggable auth.
- The visual identity is interrupted during auth by a generic Emergent surface.

Behavioral blanks for Michael:

- Desired auth providers for the clean build.
- Whether Google remains primary.
- Whether passwordless/email login is needed.
- Whether facility/customer accounts need enterprise SSO later.

## Authenticated main shell

Observed elements:

- User chip: MICHAEL CHAMBERS.
- Top centered CAOS branding and subtitle.
- New Thread control.
- Search this thread control.
- Working Context Window meter.
- Central welcome page.
- Starfield background persists.
- Bottom composer persists.

Operating implications:

The authenticated shell is a complete product frame. Future pages should plug into this shell rather than recreate layout independently.

Preserve:

- User identity chip.
- Top-right thread/context tools.
- Bottom composer lane.
- Background visual identity.
- Modal/drawer side panels.

## Home capability carousel

Observed capability cards include:

- Create Image.
- Create Video.
- Create Mindmap.
- Chat with Multiple Models.
- Search Anything.
- Analyze Data.
- Generate Content.
- Create & Design.

Observed behavior:

- Horizontal carousel with navigation arrows.
- Dot/page indicators.
- Cards provide capability discovery.

Operating implications:

The app has a product-discovery layer. The new build should not expose only a blank chat input. It should show available powers and guide the user into workflows.

Behavioral blanks for Michael:

- Which cards are active vs aspirational.
- Which cards should remain in CAOS core vs CAOSCare vertical.
- Whether cards should launch templates, agents, or modes.

## Chat surface and message cards

Observed elements:

- Thread title shown near top-right area.
- Rich formatted assistant response card.
- Message action controls:
  - Copy.
  - Read.
  - Mail.
  - Reply.
  - Useful.
  - Why?.
- Response timing chip visible, e.g. 29.2s.
- Thread content supports long formatted responses with headings and lists.

Operating implications:

- Responses have action affordances.
- Latency/receipt visibility is part of the product behavior.
- Mail/share/reply/usefulness/explanation actions are part of the interface vocabulary.

Behavioral blanks for Michael:

- What Mail does exactly.
- What Why? explains: model reasoning, source trace, decision receipt, or feedback prompt.
- Whether Useful trains preference/memory or only records feedback.

## Composer and input operations

Observed elements:

- Attachment button.
- Speaker/read button.
- Plus button.
- Text input.
- Microphone button.
- Send button.
- Engine chip, e.g. Claude engine for next reply.
- Multi-Agent OFF chip.
- Full Voice chip.
- Status text such as Created session New Thread or Loaded session.

Observed staged input behavior:

- Thought queue panel visible.
- Text: 1 THOUGHT QUEUED · SEND TOGETHER.
- Queued item visible with remove control.
- Additional draft text present in composer.

Operating implications:

The composer is not a simple text box. It is a command center with attachments, voice, staged thoughts, model selection, multi-agent state, and session status.

Preserve as separate modules:

- Input text state.
- Attachment handling.
- Voice capture.
- Read-aloud output.
- Thought queue / send-together behavior.
- Provider selection.
- Multi-agent toggle.
- Full voice mode.

Behavioral blanks for Michael:

- Exact rule for when text becomes a queued thought.
- Whether queue survives page reload.
- Whether queued thoughts can be reordered.
- Whether each queued thought gets independent receipts.

## Working Context Window meter

Observed states:

- 0 / 200.0K.
- 16.8K / 200.0K.
- Tooltip: Working Context Window — click to inspect what's in context.

Operating implications:

The context meter is a product-visible system-health and reasoning-budget indicator. It must not be treated as cosmetic.

Required clean-build contract:

- Show current context/window state in the shell.
- Tie meter to backend/model context contract where possible.
- Include source/estimation status in receipts.
- Support model-specific context windows.
- Let users inspect what is consuming context.

Behavioral blanks for Michael:

- What opens when the meter is clicked.
- Whether meter shows provider usage, estimated tokens, saved thread tokens, ARC, memory, or all of those.
- Whether non-admin users should see full detail.

## Thread search and previous threads

Observed thread search:

- Search this thread panel.
- Query example: we.
- Match count: 227 matches.
- Search results show speaker label, snippet, and highlighted query terms.
- Results appear scrollable.

Observed previous-thread drawer:

- Previous Threads title.
- Search across all threads field.
- Thread cards with titles and snippets.
- Per-thread controls/icons visible.

Operating implications:

Thread retrieval is a core CAOS behavior. The system already supports visible thread search and cross-thread browsing.

Clean-build requirements:

- Thread persistence.
- Thread titles.
- Search within current thread.
- Search across all threads.
- Snippets and match counts.
- User-scoped isolation.
- Future semantic/fuzzy retrieval.

Behavioral blanks for Michael:

- Whether search uses exact text only or fuzzy/semantic search.
- What the icons on thread cards perform.
- Whether deleted threads are recoverable.

## Navigation menu and role-aware shell

Observed menu items:

- Desktop.
- New Thread.
- Previous Threads.
- Settings.
- Memory Console.
- Quick Capture.
- Engine.
- Agent Swarm.
- Admin Dashboard.
- Admin Docs.
- Support Tickets.
- Log Out.

Observed labels:

- NEW for Memory Console and Quick Capture.
- E2B for Agent Swarm.
- ADMIN for Admin Dashboard and Admin Docs.
- Engine value visible as Claude.

Operating implications:

Navigation is role-aware, feature-flag-aware, and status-labeled. The clean build must preserve role and capability labeling, not flatten all features into one menu.

Behavioral blanks for Michael:

- Which roles exist besides admin/user/guest.
- Whether E2B label means E2B runtime specifically or agent sandbox generally.
- Whether feature labels are manually configured or computed.

## Desktop and artifacts

Observed Desktop submenu:

- Files.
- Photos.
- Links.

Observed artifact panel:

- Artifacts.
- Stored items: 66.
- Receipts: 8.
- Memory artifacts: 12.
- Files: 2.
- Photos: 59.
- Links: 5.
- Receipts: 8.
- Summaries: 6.
- Seeds: 6.

Visible file examples:

- TransactionList-2026-04-26-364.pdf.
- pasted.txt.

Operating implications:

Artifacts are first-class objects. CAOS is not only chat; it stores files, photos, links, receipts, summaries, seeds, and memory artifacts.

Clean-build requirements:

- User-scoped artifact storage.
- Artifact type taxonomy.
- Upload controls.
- Generated vs uploaded provenance.
- Receipts and summaries as first-class artifacts.
- Browse/filter by type.

Behavioral blanks for Michael:

- Whether artifacts are stored in database, object storage, filesystem, or provider storage.
- Whether artifacts can be attached back into a thread.
- Whether artifacts are searchable.

## Memory Console

Observed elements:

- Memory Console.
- Atom count visible, e.g. 329 atoms.
- Category bins:
  - Identity.
  - Projects.
  - Governance.
  - Preferences.
  - Relationship.
  - Domains.
  - Tech State.
  - Behavioral.
  - Traits.
  - Learning.
  - Real-world.
  - Risk.
  - Counter.
  - Unclassified.
- Atom metadata:
  - USER-STATED.
  - DERIVED.
  - confidence percent.
  - evidence count.
  - P95.
  - date.
- Atom controls:
  - Confirm.
  - Reclassify.
  - Forget.

Operating implications:

Memory is governed, inspectable, and user/admin-controlled. It is not silent black-box memory.

Clean-build requirements:

- Memory atoms with schema.
- Classification bins.
- Evidence count.
- Confidence/priority.
- Confirm/reclassify/forget workflows.
- Provenance distinction between user-stated and derived.
- Retrieval should be relevance-based and governed.

Behavioral blanks for Michael:

- What P95 means operationally.
- Whether confirmed memories become locked, weighted, or promoted.
- Whether derived memories require confirmation before use.

## Settings / control plane

Observed settings fields:

- Profile/avatar.
- Name: Michael.
- Role: Admin.
- Files / Photos / Links buttons.
- Email.
- Member since.
- Assistant name: Aria, with rename control.
- Birthday.
- Permanent Memories count with view/edit.
- Remember Conversations toggle.
- Game Mode.
- Developer Mode.
- Multi-Agent Mode.
- System Console.
- Aria Mode: Fact, temp 0.1, F/B/C toggles.
- Voice & Speech: nova, 1.00x.
- Ambient Mode.
- Scroll step slider.
- Bubble transparency slider.
- Connectors: Gmail, Drive, Docs, Calendar, GitHub, Slack, Twilio, Telegram, MCP.
- Pricing & Tiers.
- Delete Account.

Operating implications:

Settings is a role-aware control plane, not a simple preferences page.

Clean-build requirements:

- Role-aware settings sections.
- Memory persistence controls.
- Assistant identity controls.
- Voice/TTS preferences.
- Mode toggles.
- Connector status and configuration.
- Account deletion with safety confirmations.
- Admin-only controls gated server-side.

Behavioral blanks for Michael:

- Whether mode toggles immediately affect runtime or require reload.
- Whether connector status is live or static.
- Whether deleting account deletes artifacts/memory/threads.

## Admin Dashboard

Observed sections/tabs:

- CAOS Admin.
- System monitoring and diagnostics.
- Users & Stats.
- Spend by Engine.
- Errors.
- Engine Timeline.
- Top Users.
- Usage (30d).

Observed metrics:

- Active now registered.
- Active now guests.
- Active today.
- Active this week.
- Total registered.
- Ever logged in.
- New this month.
- New today.
- Total sessions ever.
- Guest sessions.
- Avg session length.
- Total threads.
- New registrations chart.
- Sessions started chart.
- Tier distribution.
- Login methods.

Operating implications:

Admin dashboard is an operations surface. It must be backed by durable event/session/user/usage records in the clean build.

Clean-build requirements:

- Server-side admin authorization.
- Durable analytics records.
- Privacy-respecting product metrics.
- Usage/spend by engine.
- Error/diagnostic surfaces.
- Time-windowed usage charts.

Behavioral blanks for Michael:

- Which metrics are exact vs approximated.
- Whether spend by engine is provider-billing derived or estimated.
- Whether admin refresh performs live backend query.

## Support Tickets

Observed support surface:

- SUPPORT TICKETS.
- Admin view · all users.
- Status buckets:
  - All: 25.
  - Open: 12.
  - In progress: 0.
  - Resolved: 13.
  - Closed: 0.
- Ticket cards show BUG, OPEN, VIA ARIA, user/email, timestamp.
- Actions: IN PROGRESS, RESOLVE, CLOSE.

Visible ticket examples:

- TTS Read Aloud button doesn't toggle to Stop.
- Core Engine Optimization: Context Cap and UI Sync.
- Hardcoded 3K Context Cap and Aggressive Sanitization.
- Aggressive Sanitization and WCW Meter Stagnation.

Operating implications:

Support tickets are a real admin/diagnostic workflow. Aria can apparently originate or route ticket content into an admin surface.

Clean-build requirements:

- Ticket schema.
- Status transitions.
- Admin authorization.
- Ticket provenance/source.
- User attribution.
- Audit receipts for status changes.
- Ability to promote bugs/incidents into build docs when needed.

Behavioral blanks for Michael:

- Whether users can create tickets directly.
- Whether Aria auto-files tickets or only files when asked.
- Whether tickets link to threads/errors/logs.

## Admin Docs / Project Blueprints

Observed surface:

- Admin Docs · Project Blueprints.
- Left file list.
- Document viewer with markdown-like rendering.

Visible documents:

- CAOS_CARE_PLAYBOOK.md.
- CHANGELOG.md.
- CONNECTORS_SPRINT_PLAN.md.
- CONNECTOR_BLUEPRINT.md.
- EMERGENT_MEETING_NOTES.md.
- FORK_HANDOFF_2026_04_26.md.
- MASTER_IMPLEMENTATION_CHECKLIST.md.
- PLATFORM_PAIN_POINTS.md.
- PRD.md.
- ROADMAP.md.
- SystemBlueprint.md.
- TIER1_SPEC.md.
- TROUBLESHOOTING_BULLETIN.md.
- TSB_LOG.md.
- UX_BLUEPRINT.md.
- test_credentials.md.

Observed open document:

- CAOS Care — Founder's Playbook.

Operating implications:

Documentation is already part of the product UI. The new build should preserve an admin-readable docs browser and a disciplined documentation source.

Clean-build requirements:

- Admin docs source registry.
- Markdown/document rendering.
- Private/admin access controls.
- Search and navigation.
- Clear separation between public docs and admin-only docs.

Behavioral blanks for Michael:

- Where docs were stored in the live prototypes.
- Whether docs were editable from UI.
- Whether docs sync to GitHub.

## Engine, provider, and multi-agent controls

Observed elements:

- Engine chip showing Claude.
- Text: engine for next reply.
- Multi-Agent OFF.
- Agent Swarm menu item with E2B label.
- Aria Mode controls in settings.

Operating implications:

CAOS is not single-provider-only. Provider choice, agent mode, and response style/mode are product concepts.

Clean-build requirements:

- Provider abstraction.
- Per-reply engine selection.
- Model/provider capability registry.
- Multi-agent execution mode as a governed feature.
- Runtime receipts showing selected engine and mode.

Behavioral blanks for Michael:

- Which providers are live in each prototype.
- Whether engine can switch mid-thread or only next reply.
- Whether multi-agent mode uses E2B, internal orchestration, or both.

## Voice and audio

Observed elements:

- Full Voice chip.
- Microphone input button.
- Speaker/read button.
- Voice & Speech settings: nova, 1.00x.
- Support ticket about TTS Read Aloud button not toggling to Stop.

Operating implications:

Voice is a first-class product lane, but TTS/read-aloud has known defect evidence.

Clean-build requirements:

- Speech-to-text path.
- Text-to-speech/read-aloud path.
- Per-message read control.
- Global/full voice mode.
- Voice settings.
- Stop/cancel playback correctness.
- Receipts/error handling for audio issues.

Behavioral blanks for Michael:

- Which TTS provider is used.
- Which STT provider is used.
- Whether voice mode is push-to-talk, continuous, or both.

## CAOSCare evidence from docs surface

Observed Admin Docs content shows CAOS Care — Founder's Playbook and the origin sentence:

Built because two of my residents couldn't see the call button.

Operating implications:

CAOSCare is already represented in the live system's internal docs and product thinking. It is the likely vertical product/revenue/help-people lane, while CAOS is the broader governed AI operating/orchestration layer.

Clean-build requirements:

- Preserve CAOSCare as a primary vertical lane.
- Keep product story, safety, care workflow, and facility operations grounded.
- Do not lose the human origin of the product.

## Documentation operations for the Linode repo

Going forward, documentation should be created in the Linode repo under `docs/` with clear names and dates when the document records a point-in-time finding.

Recommended naming patterns:

- Point-in-time evidence report: `docs/TOPIC_YYYY-MM-DD.md`.
- Living contract: `docs/TOPIC_CONTRACT.md`.
- Index/ledger: `docs/TOPIC_LEDGER.md`.
- Operational checklist: `docs/TOPIC_CHECKLIST.md`.

Every substantial document should include:

- Date.
- Repository and branch context when relevant.
- Status: draft, active, superseded, or historical evidence.
- Purpose.
- Scope.
- Source/evidence basis.
- Behavioral blanks or unknowns.
- Next action.

Do not over-document trivial edits. Do document decisions, architecture, evidence, contracts, defects, source maps, build phases, and accepted corrections.

## Immediate new-build preservation checklist

The clean Linode build should preserve or intentionally replace these live-proven surfaces:

1. Public landing page.
2. Guided onboarding tour.
3. Auth handoff / login.
4. Authenticated shell.
5. Home capability carousel.
6. Bottom composer with voice, attachment, provider, multi-agent, and queued-thought controls.
7. Thread persistence and previous-thread drawer.
8. Search-this-thread and cross-thread search.
9. Working Context Window meter and inspection behavior.
10. Memory Console with atom governance.
11. Desktop/artifact vault.
12. Settings/control plane.
13. Admin Dashboard.
14. Support Tickets.
15. Admin Docs / Project Blueprints.
16. Provider/engine controls.
17. Voice/read-aloud behavior.
18. CAOSCare documentation/product lane.

## Next action

Michael should fill in behavioral blanks from live use.

After that, convert this manual into implementation contracts and task lanes for the Linode-owned build.
