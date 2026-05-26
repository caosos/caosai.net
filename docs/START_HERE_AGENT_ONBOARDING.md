# START HERE — CAOS Agent Onboarding

## Read this first

You are entering the CAOS Linode rebuild. Do not start by coding. Start by orienting.

This repository is the clean rebuild surface for CAOS. The current working branch is:

```text
aria-emergent-clean-rebuild
```

The source/reference repos and branches are:

```text
Emergent behavior reference:
caosos/emergent-caos-build

Legacy Python salvage reference:
caosos/linode-repo branch legacy-python-server-salvage-2026-05-01

Clean destination branch:
caosos/linode-repo branch aria-emergent-clean-rebuild
```

## Prime directive

CAOS is not just a chat app. It is a user-owned AI operating platform: memory-aware, tool-capable, provider-flexible, receipt-backed, truth-disciplined, and eventually capable of helping users operate documents, systems, machines, homes, care workflows, and real work under permission gates.

## Michael's operating intent

Michael John Chambers is the system designer. He wants CAOS to become his long-term AI platform: an assistant that remembers what matters, uses tools like this build session, works across providers/connectors, helps build software, manages context intelligently, produces receipts, and eventually helps with real-world machine/process guidance without reckless autonomy.

Safe high-level biography and system intent are documented in:

```text
docs/SYSTEM_BLUEPRINT.md
```

## Non-negotiables

- Do not use Base44 code.
- Base44 screenshots may be used as visual reference only.
- Emergent is the current behavior/reference build, not a monolith to copy.
- Legacy Python server is salvage/reference, not the new runtime foundation.
- Do not write to `main`.
- Do not deploy production.
- Do not expose or request real secrets.
- Do not create God files.
- Do not silently rewrite behavior.
- Do not degrade accepted features.
- Every meaningful action gets a receipt.
- Shared-file edits require orchestrator/crosswire discipline.

## Required first read order

Read these before making changes:

1. `docs/CONTRACTS_TABLE_OF_CONTENTS.md`
2. `docs/DOCUMENTATION_INDEX.md`
3. `docs/BUILD_STATUS.md`
4. `docs/REBUILD_CONTRACT.md`
5. `docs/BUILD_DECISIONS_AND_INCIDENTS.md`
6. `docs/AGENT_BASELINE_DIRECTIVES.md`
7. `docs/PARALLEL_AGENT_WORKFLOW.md`
8. `docs/CROSSWIRE_INTEGRATION_LEDGER.md`
9. `docs/SOURCE_TO_TARGET_MAP.md`
10. lane-specific contract docs

## Current architecture posture

The rebuild is foundation-first. Current backend skeleton includes:

- FastAPI app entrypoint
- config loader
- logging setup
- runtime registry
- database boundary
- development auth
- health route
- runtime route
- model catalog and WCW metadata
- minimal chat contract route
- admin boundary probe
- memory contract routes
- receipt schemas and action receipt service
- memory capture/review/relevance/ARC scaffolds
- hydration policy, sanitizer, prompt budget scaffolds

## Current backend routes

```text
GET  /api/health
GET  /api/runtime
POST /api/auth/dev-login
GET  /api/models
POST /api/models/select
POST /api/chat/turn
POST /api/admin/probe
POST /api/memory/atoms
POST /api/memory/atoms/query
```

## Critical product doctrines

### Receipts everywhere

Every meaningful state change, model selection, memory action, hydration decision, connector call, admin action, artifact update, tool call, error, or degraded response must have a receipt.

Read:

```text
docs/RECEIPT_EVERYWHERE_CONTRACT.md
```

### Memory / ARC / WCW

Memory is not keyword search and not a prompt dump. WCW is the working context window. ARC is the active relevant context selected inside WCW. Hydration decides what enters ARC. Sanitization bounds and cleans context without destroying truth.

Read:

```text
docs/MEMORY_ARC_HYDRATION_CONTRACT.md
```

### Model-specific WCW

WCW differs by provider/model. The UI must represent model-specific context capacity in the profile/settings dropdown, response bubble/receipt area, and bottom composer model selector.

Read:

```text
docs/WCW_ENGINE_CONTEXT_CONTRACT.md
```

### Aria personality

Aria should feel like the working ChatGPT 5.5 build partner style Michael approved: direct, technical, truth-first, proactive by default for low-risk useful work, careful-gated for high-risk actions, receipt-oriented, fast without being shallow.

Read:

```text
docs/ARIA_PERSONALITY_AND_LATENCY_CONTRACT.md
```

### Feature locks and regression prevention

Accepted features must be locked with behavior, files, acceptance checks, and regression awareness. TTS/STT, scrolling, search, WCW, memory, receipts, artifacts, and admin boundaries are high-risk regression lanes.

Read:

```text
docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md
docs/TROUBLESHOOTING_VAULT.md
```

## Visual/UI references

Base44 and Emergent screenshots are reference evidence. Base44 is visual-only; Emergent is visual and behavior reference depending on feature. Screenshot/photo provenance is mandatory when using images for implementation guidance.

Important visual requirements already captured:

- starfield remains visible behind translucent chat surfaces
- message bubbles should be translucent, not opaque blocks
- user bubble should not be harsh opaque blue/purple
- dark mode is preferred primary mode
- light mode must exist
- translucent header is desired
- restore last active thread on refresh
- scroll to latest/last meaningful position
- down/jump button must reliably return to latest
- previous thread search must support fuzzy/non-exact search
- settings/profile menu layout can be referenced, but colors should be refined

Read:

```text
docs/FRONTEND_VISUAL_BEHAVIOR_CONTRACT.md
docs/BEHAVIOR_SNAPSHOT_FROM_SCREENSHOTS.md
```

## Parallel-agent rules

Agents are lane workers, not free agents. Work in your lane. Do not casually edit shared files. If you need shared wiring, record it in the crosswire ledger for orchestrator integration.

Shared files requiring coordination include:

- `backend/app/main.py`
- `backend/requirements.txt`
- `backend/app/core/config.py`
- `backend/app/core/database.py`
- `backend/app/services/receipt_service.py`
- `frontend/package.json`
- app-level frontend route/layout files
- key documentation index/status/map files

## If evidence is missing

Do not invent. Mark it pending source review.

Michael has TSV logs, screenshots, support-ticket evidence, and build history that may not all be visible yet. Treat referenced evidence as important and ask the orchestrator/Michael for the relevant artifact only when needed.

## CURRENT SESSION STATE — 2026-05-26

### What was completed in the last session

- Real LiteLLM provider calls wired (OpenAI, Anthropic, Google, xAI)
- Thread persistence via MongoDB
- Token counting and latency tracking in `chat_orchestrator.py`
- Receipt returns: `latency_ms`, `user_tokens`, `assistant_tokens`, `thread_total_tokens`
- Frontend shell rebuilt: permanent sidebar, welcome carousel, composer with model selector
- `docs/RUNTIME_SOURCE_OF_TRUTH.md` and `ops/deploy.sh` created
- `docs/BUILD_BASELINE_AND_FIX_LEDGER.md` created (FIX-001 through FIX-003)
- **`docs/REFERENCE_SOURCE_MAP.md` created** — required reading before any frontend surface work
- `frontend/src/types/index.ts` updated: `ChatMessage` now has `latency_ms?: number`, and `ChatReceipt` interface added

### What the frontend currently has

Source files in `frontend/src/`:

- `App.tsx` — shell orchestrator
- `components/chat/ChatPane.tsx` — message list, jump-to-bottom button
- `components/chat/Composer.tsx` — textarea, model selector chip, send button
- `components/chat/MessageBubble.tsx` — renders messages (plain text only, no markdown yet)
- `components/chat/WelcomeScreen.tsx` — welcome hero and capability cards
- `components/shell/Header.tsx` — header bar (no WCW meter yet)
- `components/shell/Starfield.tsx` — animated starfield
- `components/sidebar/Sidebar.tsx` — nav rail: Threads, Memory, Desktop, Settings, New Thread
- `hooks/useChat.ts` — chat state, thread loading, send, latency/token tracking
- `hooks/useModels.ts` — model catalog from backend
- `types/index.ts` — all types including `ChatMessage` (with `latency_ms?`) and `ChatReceipt`
- `styles/globals.css` — CSS variables and glass utility classes

### NEXT TASK — Four UI surfaces to build

These are the only approved next tasks. Do not add anything else. Read `docs/REFERENCE_SOURCE_MAP.md` before touching any of these.

---

#### Surface 1 — Markdown rendering in chat messages

**File to create:** `frontend/src/components/chat/MarkdownRenderer.tsx`

No external markdown libraries. Custom renderer only (Emergent used a custom `MarkdownMessage.js`).

Must handle:
- Fenced code blocks (` ``` `) with optional language label
- Inline code (backtick)
- `**bold**` and `*italic*` / `_italic_`
- `#` / `##` / `###` headers
- `---` horizontal rule
- `- ` and `* ` bullet lists
- `1. ` numbered lists
- Plain paragraphs (multi-line collapse with `<br />`)

Styling must fit the CAOS visual system (dark glass, `--caos-accent-bright` for code, translucent code block backgrounds). Do NOT use opaque surfaces inside messages.

**File to edit:** `frontend/src/components/chat/MessageBubble.tsx`

- Import `MarkdownRenderer` and use it for assistant (`role === 'assistant'`) messages only
- User messages stay as `pre-wrap` plain text
- Do not change bubble shape or visual family

---

#### Surface 2 — Per-message latency chip

**File to edit:** `frontend/src/components/chat/MessageBubble.tsx`

- `ChatMessage` already has `latency_ms?: number` in types
- For assistant messages, if `message.latency_ms` is set, show a small pill below the bubble
- Format: `< 1000ms → show as "743ms"`, `≥ 1000ms → show as "4.2s"`
- Style: small, dimmed, pill shape, matching `--caos-text-muted`

**File to edit:** `frontend/src/hooks/useChat.ts`

- When creating the `assistantMsg` after a successful API call, attach `latency_ms: latency` from the receipt
- The receipt already returns `latency_ms`; it is already stored in `lastLatencyMs` state — just also attach it to the message object

---

#### Surface 3 — Message action buttons

**File to edit:** `frontend/src/components/chat/MessageBubble.tsx`

Show a row of action buttons below each **assistant** message only. Match Emergent screenshot `01-31-13` in `docs/visual-reference/emergent/`.

Buttons (in order): `Copy · Re-Read · Mail · Reply · Useful · Why?`

Implementation rules:
- **Copy**: fully functional — `navigator.clipboard.writeText(message.content)`. Show `"Copied!"` for 2s then reset.
- **Useful**: local toggle state only — no backend yet. Visual confirmation is enough.
- **Re-Read, Mail, Reply, Why?**: visual stubs. Present in the UI. `cursor: default`, `opacity: 0.5`, `title` attribute explaining they are coming soon. Do NOT wire fake behavior.
- Separate buttons with `·` separator spans
- Style: `fontSize: 11`, `color: var(--caos-text-dim)` for active, `var(--caos-text-muted)` for stubs
- Do NOT build hover-only visibility — always show the action strip under assistant messages

---

#### Surface 4 — WCW meter in header

**File to edit:** `frontend/src/components/shell/Header.tsx`

Add a compact WCW strip to the left side of the header. It should show token data from the last completed chat turn.

Fields to show (from `ChatReceipt`):
- `SENT` — `userTokens` (prompt tokens for last turn)
- `RECV` — `assistantTokens` (completion tokens for last turn)
- `THREAD` — `threadTotalTokens` (cumulative thread tokens)
- `LAT` — `latencyMs` formatted as `"4.2s"` or `"743ms"`

When no chat has happened yet, the WCW strip should be hidden (only render when `receipt` prop is defined).

**File to edit:** `frontend/src/hooks/useChat.ts`

Add `lastReceipt: ChatReceipt | undefined` to state. After a successful send, populate it from the API receipt fields:
- `userTokens: receipt.user_tokens ?? 0`
- `assistantTokens: receipt.assistant_tokens ?? 0`
- `threadTotalTokens: receipt.thread_total_tokens ?? 0`
- `latencyMs: receipt.latency_ms ?? 0`

Export `lastReceipt` from the hook return.

**File to edit:** `frontend/src/App.tsx`

- Pull `lastReceipt` from `useChat()`
- Pass it to `<Header receipt={lastReceipt} />`

---

### After all four surfaces are built

1. Run `npm run build` in `frontend/` to confirm no TypeScript errors
2. Commit with message: `feat: markdown rendering, WCW meter, latency chip, message action buttons`
3. Update `docs/BUILD_STATUS.md` to mark these four surfaces as complete
4. Report to Michael: what was built, what files were changed, any stubs/deferred items

### Immediate next recommended work (after UI surfaces)

1. Run local smoke test from real checkout
2. Wire hydration/ARC receipt into `/api/chat/turn`
3. Provider/router adapters for remaining models
4. Thread restore on reload (persist last active thread to localStorage)

## Stop conditions

Stop and report if:

- you are about to touch shared files without orchestrator assignment
- you are unsure whether a screenshot/source is Base44 or Emergent
- a change may degrade a locked feature
- source evidence contradicts a contract
- a secret or credential appears
- a production deploy/main merge/destructive action is requested without explicit approval
