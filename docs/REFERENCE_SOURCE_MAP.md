# CAOS Reference Source Map

**Status:** Active — required reading before any frontend, UX, or behavior change  
**Date:** 2026-05-26  
**Maintained by:** Every agent working on caosai.net

---

## 1. Purpose

This document is the required reference map for all CAOS rebuild work. Before modifying any frontend surface, UX flow, chat behavior, composer, sidebar, message rendering, model selector, WCW display, TTS/STT, attachments, or memory surface, the relevant section of this document must be consulted and the "Reference Sources Consulted" format used in the task report.

This map prevents rebuilding from imagination when working evidence exists. It does not authorize copying old code. It authorizes extracting proven behavior and rebuilding it cleanly.

---

## 2. Emergent Build Repo Role

**Repo:** `caosos/emergent-caos-build`  
**Status:** Public, accessible  
**Role:** Current working product reference. Strongest behavioral and visual evidence lane.  
**Constraint:** Do not copy monolith code wholesale. Extract behavior contracts and component logic, then rebuild modularly in caosai.net.  
**Access:** GitHub API readable. Not cloned locally. Fetch specific files via GitHub API when inspecting.

### What it contains (confirmed via file tree inspection)

**Backend services relevant to rebuild:**

| File | Behavior |
|---|---|
| `backend/app/services/chat_pipeline.py` | Full chat orchestration with hydration, context, memory, receipts |
| `backend/app/services/context_engine.py` | WCW / ARC token tracking and arbitration |
| `backend/app/services/hydration_policy.py` | Context hydration policy and memory injection |
| `backend/app/services/memory_extractor.py` | Memory extraction from conversation turns |
| `backend/app/services/token_meter.py` | Token counting, budget tracking |
| `backend/app/services/voice_service.py` | TTS + STT — OpenAI direct preferred, Emergent proxy fallback |
| `backend/app/services/prompt_builder.py` | Prompt assembly with memory, context, system instructions |
| `backend/app/services/continuity_service.py` | Thread continuity / history recall |
| `backend/app/services/thread_title_service.py` | Auto-generated thread titles |
| `backend/app/routes/memory_atoms.py` | Memory atom CRUD API |
| `backend/app/routes/captures.py` | Quick Capture ingestion API |
| `backend/app/routes/support.py` | Support ticket backend |
| `backend/app/routes/admin_dashboard.py` | Admin metrics and dashboard API |
| `backend/app/routes/admin_docs.py` | Admin docs browser API |

**Frontend components relevant to rebuild:**

| File | Behavior |
|---|---|
| `CaosShell.js` | Top-level authenticated shell and layout |
| `ShellHeader.js` | Header with WCW meter, thread title, controls |
| `Composer.js` | Full composer: text, attachment, voice, engine chip, thought queue |
| `MessagePane.js` | Message list and scroll behavior |
| `MarkdownMessage.js` | Custom markdown renderer (bold, code, tables, lists) — no react-markdown |
| `SelectionReactionPopover.js` | Per-message action buttons: Copy, Re-Read, Mail, Reply, Useful, Why? |
| `LatencyIndicator.js` | Per-message latency chip (e.g., "43 seconds") |
| `WorkingContextStrip.js` | WCW meter: ARC / sent / received / facts / global — fed from receipt |
| `PreviousThreadsPanel.js` | Thread browser with search and snippets |
| `MemoryConsoleDrawer.js` | Memory console with category bins and atom controls |
| `QuickCaptureDrawer.js` | Quick Capture ingestion surface |
| `SupportTicketsDrawer.js` | Support ticket admin view |
| `AdminDashboard.js` | Admin metrics dashboard |
| `AdminDocsDrawer.js` | Admin docs browser |
| `ThreadRail.js` | Thread navigation rail |
| `VoiceFirstMode.js` | Full-voice mode — dedicated voice interaction surface |
| `useVoiceIO.js` | Voice hook: transcribeAudio, transcribeAudioChunk, speakText, stopSpeech |
| `useCaosShell.js` | Shell state orchestrator |
| `EngineChip.js` | Provider/model selector chip in composer |

---

## 3. Base44 / caos-os-A1 Repo Role

**Repo:** `caosos/caos-os-A1`  
**Status:** Private — not accessible via GitHub API (returned 404)  
**Role as documented:** Base44 mature behavior reference for prior feature behavior, governance rules, attachment handling, search gating, receipts, TTS/STT, and UI behavior.  
**Constraint:** Cannot inspect directly. Behavior captured in the local visual evidence docs (VISUAL_EVIDENCE_MANIFEST.md, BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md, LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md).

### Base44 behavioral notes (from visual evidence docs)

- Starfield was more visible and deeper in Base44 than Emergent.
- User message bubbles were harsh opaque slabs — **do not replicate**.
- Menu pattern and thread navigation flow are visual references.
- Code must not be copied from Base44.

---

## 4. Visual Evidence Files and Assets

### Local documentation (in caosai.net/docs/)

| File | Contents |
|---|---|
| `docs/VISUAL_EVIDENCE_MANIFEST.md` | Surface-by-surface evidence: main shell, support tickets, admin docs, WCW meter, memory console, settings, quick capture, threads search, mobile bugs |
| `docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md` | Behavioral implications per product domain: landing, shell, WCW, threads, memory, admin, artifacts, settings, connectors, admin docs |
| `docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md` | Hard exclusions, visual targets, starfield rules, bubble rules, thread restore, down button, settings behavior, screenshot provenance format |
| `docs/LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md` | Full operating manual: public landing, onboarding tour, auth handoff, shell, carousel, chat surface, WCW, threads, nav menu, desktop, memory, settings, admin, support tickets, admin docs, voice, CAOSCare |

### Screenshot assets (in caosai.net/docs/visual-reference/emergent/)

15 screenshots from 2026-04-27. All show the live Emergent caosos.com prototype.

| Screenshot | Surface observed |
|---|---|
| `01-29-11` | Public landing page — CAOS hero, 4 feature cards, Take the Tour, Sign In, Guest |
| `01-29-18` | Onboarding tour step 1 — "Start here" modal with dim/blur overlay |
| `01-29-30` | Onboarding tour step — "Attach anything" with file/photo/screenshot description |
| `01-31-03` | **Authenticated main shell** — full LEFT SIDEBAR, Welcome to CAOS hero, 4 capability cards, bottom composer with Claude chip, Multi-Agent OFF, Full Voice, WCW meter |
| `01-31-13` | **Chat surface** — rich formatted message, action strip: Copy · Re-Read · Mail · Reply · Useful · Why?, latency chip |
| `01-31-30` | **Chat surface continued** — same thread, response formatting, action controls |
| `01-31-40` | **Previous Threads drawer** — search across all threads, thread cards with titles/snippets |
| `01-31-56` | **Admin Dashboard** — CAOS Admin, Users & Stats, Spend by Engine, Errors, Engine Timeline, Top Users, Usage 30d, live status metrics |
| `01-32-20` | **Admin Docs** — left file list, document viewer showing CAOS Care Founder's Playbook in markdown |
| `01-32-29` | **Memory Console** — left category bin rail, atom cards with USER-STATED/DERIVED labels, confidence%, evidence count, Confirm/Reclassify/Forget buttons |
| `01-32-44` | **Support Tickets** — All 44 / Open / In Progress / Resolved / Closed, ticket cards with BUG/OPEN/VIA ARIA labels |
| `01-33-17` | **Settings drawer** — Admin access, Split screen, Collaboration, Monitor Metrics, Aria Mode, Standard Bubbles, connector list, Delete Account |
| `01-33-58` | Chat — Aria discussing Google Maps integration with pros/cons analysis (connector behavior example) |
| `01-34-54` | Chat continued — Google Maps integration Aria response, connector analysis |

**Root-level screenshot:**

| File | Surface observed |
|---|---|
| `Screenshot from 2026-05-24 20-53-34.png` | **Current caosai.net rebuild** — sidebar with Threads/Memory/Desktop/Settings/New Thread, hero "CAOS — Your memory, Your rules, Your right", 6 capability cards: Persistent Memory, Multi-Model Routing, Desktop & Files, Content Hygiene, Governed Actions, Text Orchestration |

---

## 5. Behavior Lanes Requiring Reference Inspection

The following lanes require reference inspection before any change is made:

| Lane | Reference Required | Current caosai.net Status |
|---|---|---|
| Sidebar / navigation rail | Screenshot 01-31-03, LIVE_PROTOTYPE_MANUAL | Simplified — missing Memory Console, Quick Capture, Engine, Agent Swarm, Admin Dashboard, Admin Docs, Support Tickets |
| Welcome / home carousel | Screenshots 01-31-03, 01-31-13 | Rebuilt — 6 cards present |
| Chat message rendering | Emergent `MarkdownMessage.js` | Plain text only — no markdown rendering yet |
| Message action buttons | Emergent `SelectionReactionPopover.js` | Not built |
| Latency indicator | Emergent `LatencyIndicator.js` | Latency tracked in hook, not displayed per-message |
| WCW / context meter | Emergent `WorkingContextStrip.js`, VISUAL_EVIDENCE_MANIFEST §5 | Not in UI — token count exists in Composer footer only |
| Previous threads / search | Emergent `PreviousThreadsPanel.js` | Thread list in sidebar, no search yet |
| Memory console | Emergent `MemoryConsoleDrawer.js`, VISUAL_EVIDENCE_MANIFEST §6 | Not built in this rebuild |
| Quick Capture | Emergent `QuickCaptureDrawer.js`, VISUAL_EVIDENCE_MANIFEST §8 | Not built |
| Support tickets | Emergent `SupportTicketsDrawer.js` | Not built |
| Admin dashboard | Emergent `AdminDashboard.js` | Not built |
| Admin docs browser | Emergent `AdminDocsDrawer.js` | Not built |
| TTS / read-aloud | Emergent `useVoiceIO.js`, `voice_service.py` | Not built |
| STT / microphone input | Emergent `useVoiceIO.js`, `voice_service.py` | Not built |
| Attachments / file upload | Emergent `useFilesCrud.js`, `ArtifactsDrawer.js` | Not built |
| Desktop / artifacts vault | Emergent `ArtifactsDrawer.js` | Not built |
| Settings panel | Emergent `ProfileDrawer.js`, screenshot 01-33-17 | Scaffolded, not production-complete |
| Connector status | Emergent `ConnectorsDrawer.js` | Not built |
| Thread restore on reload | FRONTEND_VISUAL_BEHAVIOR_CONTRACT | Not implemented |
| Down/jump to latest button | FRONTEND_VISUAL_BEHAVIOR_CONTRACT | Not built |

---

## 6. Frontend / UX Reference Rules

1. **Inspect before building.** Before building or modifying any surface, read the relevant screenshot(s) and Emergent component(s) listed in section 5.
2. **Preserve behavior, not code.** Extract behavioral contracts from Emergent. Write clean TypeScript/React in caosai.net — do not paste Emergent JS.
3. **Visual family rules (from FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md):**
   - Dark mode primary. Light mode supported.
   - Starfield remains visible through all surfaces.
   - Foreground surfaces use glass/translucent layering.
   - Message bubbles must not be opaque blocks.
   - User and assistant bubbles belong to the same visual family — no harsh opaque user slab.
4. **Feature parity rule:** Do not silently drop features. If a feature is intentionally deferred, record the divergence here.
5. **Screenshot provenance:** Any implementation justified by a screenshot must cite the screenshot filename, origin (Emergent/Base44/current build), and what it proves.

---

## 7. Voice / TTS / STT Reference Rules

**Do not build TTS/STT until explicitly tasked.** When tasked, use this reference.

### Confirmed Emergent behavior (from `voice_service.py` and `useVoiceIO.js`)

**TTS (text-to-speech / read-aloud):**
- **Primary:** Browser's native `speechSynthesis` API — instant, zero API cost
- **Secondary:** OpenAI TTS via direct API (`gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`) if `OPENAI_API_KEY` is set
- Markdown is stripped before TTS playback (asterisks, code fences, etc.)
- Stop/cancel playback uses `window.speechSynthesis.cancel()` with an `activeUtteranceRef` to prevent overlap

**STT (speech-to-text / microphone transcription):**
- OpenAI Whisper transcription: `gpt-4o-transcribe` → `gpt-4o-mini-transcribe` → `whisper-1` in preference order
- Direct OpenAI API preferred over any proxy
- Silence hallucination detection: known Whisper phantom phrases filtered out
- Repetition collapse: Whisper silence loops (e.g., "X. X. X. X.") collapsed to single instance
- Two transcription paths: full-audio and chunk-based (partial transcription with prior prompt context)

**Known failure modes (from support tickets and FEATURE_LOCK_AND_REGRESSION_CONTRACT.md):**
- TTS Read Aloud button didn't toggle to Stop — fixed by `activeUtteranceRef` + explicit cancel
- Voice list loading delay — must await `onvoiceschanged` before rendering
- Silence hallucinations — must filter before displaying transcription
- Overlapping playback — must cancel existing utterance before starting new one
- Ubuntu: requires `speech-dispatcher` for voice list to populate

**Rebuild requirement:** Any TTS implementation must pass the stop-button test before acceptance. Any STT implementation must include silence filtering.

---

## 8. Attachment / File / Artifact Reference Rules

**Do not build attachments/artifacts until explicitly tasked.** When tasked, use this reference.

### Confirmed Emergent behavior (from screenshots, LIVE_PROTOTYPE_MANUAL)

**Artifact taxonomy observed:**
- Files (PDF, txt, etc.)
- Photos
- Links
- Receipts (8 in screenshot)
- Memory artifacts (12 in screenshot)
- Summaries
- Seeds

**Storage behavior:** Files uploaded to server (`backend/uploads/` in Emergent). User-scoped by email. Not stored in MongoDB — filesystem or object storage.

**Artifact vault numbers observed:** 66 total stored items in one screenshot session.

**Rebuild requirements:**
- User-scoped artifact storage
- Generated vs uploaded provenance
- Artifact type taxonomy matching observed categories
- Browse/filter by type
- Receipts as first-class artifacts

---

## 9. Memory / Thread Reference Rules

### Memory console (confirmed from screenshots and VISUAL_EVIDENCE_MANIFEST)

**Category bins (14 observed):**
Identity, Projects, Governance, Preferences, Relationship, Domains, Tech State, Behavioral, Traits, Learning, Real-world, Risk, Counter, Unclassified

**Atom metadata fields:**
- Source type: USER-STATED or DERIVED
- Confidence percentage
- Evidence count
- Priority (P95 observed)
- Date

**Atom controls:** Confirm, Reclassify, Forget

**Atom count in live system:** 329–352 atoms observed in screenshots

**Rebuild requirements:**
- MongoDB-backed atom schema with all observed metadata fields
- Category bins matching observed taxonomy
- Confirm/reclassify/forget workflow — no silent memory promotion
- USER-STATED vs DERIVED provenance distinction
- Confidence and evidence count visible in UI

### Thread behavior (confirmed from screenshots and Emergent `PreviousThreadsPanel.js`)

**Thread persistence:** Required. Already built in caosai.net with MongoDB.

**Thread search:**
- Within-thread search (search this thread) — showing match count (227 matches observed) and snippets
- Cross-thread search — search across all saved threads with title + content matching
- Fuzzy/non-exact matching required: "users should not need exact wording to recover a thread"

**Thread restore on reload:** Must restore last active thread and scroll to last message position.

---

## 10. Required Report Format for Future Claude Tasks

Every task report that touches a surface listed in section 5 must include:

```
## Reference Sources Consulted

| Source | File/Screenshot | Behavior Observed |
|---|---|---|
| Emergent repo | frontend/src/components/caos/XXX.js | [what was found] |
| Visual evidence | docs/visual-reference/emergent/01-31-03_emergent_reference.png | [what it showed] |
| Behavior docs | docs/LIVE_PROTOTYPE_VISUAL_OPERATING_MANUAL_2026-05-03.md §[section] | [relevant contract] |

## Behavior Disposition

| Behavior | Status | Reason if Diverging |
|---|---|---|
| [specific behavior] | Preserved / Improved / Intentionally diverged | [reason] |
```

If no reference source was consulted because the surface is new (no prior evidence), state:

```
## Reference Sources Consulted
No prior evidence found for this surface. New behavior — no divergence from existing.
```

---

## Appendix: Observed Sidebar Navigation (Emergent, confirmed screenshot 01-31-03)

```
MICHAEL CHAMBERS (user chip)
├── Desktop
├── New Thread
├── Previous Threads
├── Settings
├── Memory Console          [NEW]
├── Quick Capture           [NEW]
├── Engine                  [current: Claude]
├── Agent Swarm             [E2B]
├── Admin Dashboard         [ADMIN]
├── Admin Docs              [ADMIN]
├── Support Tickets
└── Log Out
```

Current caosai.net sidebar has: Threads, Memory, Desktop, Settings, New Thread — a simplified subset. The full role-aware navigation from Emergent is the target.

---

## Appendix: WCW Meter Data Contract (Emergent `WorkingContextStrip.js`)

The WCW component receives a `receipt` prop and renders:

| Field | Source in receipt | Displayed as |
|---|---|---|
| ARC tokens | `active_context_tokens` | `X / budget` |
| Sent | `prompt_tokens` | integer |
| Received | `completion_tokens` | integer |
| Facts | `personal_facts_count` | integer |
| Global | `global_cache_count · global_bin_status` | composite |

The caosai.net receipt already returns `user_tokens`, `assistant_tokens`, and `thread_total_tokens`. The WCW component can be built from these once the UI work is tasked.
