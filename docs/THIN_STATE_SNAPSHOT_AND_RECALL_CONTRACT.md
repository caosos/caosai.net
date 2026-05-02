# Thin State Snapshot and Recall Contract

## Purpose

This contract applies across CAOS builds and verticals, including CAOS Core, CAOS Care, CAOS Connect, and CAOS Tradings.

CAOS must carry enough operational state to stay oriented, truthful, fast, and useful without dragging full history, full documents, full screenshots, or full thread bodies into every turn.

The system must preserve deep recall capability while keeping active context thin.

Core rule:

```text
Do not carry all history. Carry enough state to find the right history instantly.
```

## Product requirement

Michael must be able to talk naturally to Aria and recover important information from vague, partial, old, or cross-thread references.

Examples:

```text
"What was that problem ticket book called?" -> Troubleshooting Vault
"Two years ago, somewhere around there, I bought a couple boats..." -> retrieve relevant memory/thread/evidence
"That thing about the mall directory stands" -> global verified knowledge cache analogy
"The admin login thing from CAOS Care" -> CORS blocked credentialed request; fix commit reference
```

The system must not require exact wording, exact dates, exact thread titles, or exact file names.

## Thin State Snapshot / TSS

A Thin State Snapshot is a compact, structured packet that describes the current operating context.

It should be small enough to carry frequently, ideally kilobytes rather than large context dumps.

TSS should include only the state needed for orientation and retrieval.

Example:

```json
{
  "platform": "caoscare.com",
  "route": "/admin-login",
  "surface": "AdminLogin",
  "role": "anonymous",
  "local_time": "Saturday May 2, 4:51 PM",
  "location": "Conway, Arkansas",
  "active_goal": "migrate CAOS Care off Emergent to Linode",
  "current_rule": "move first, refactor second",
  "last_action": "admin_login_submit",
  "last_error": "CORS blocked credentialed request",
  "retrieval_cues": ["CAOS Care", "admin login", "CORS", "Emergent migration"],
  "forbidden": ["do not use CAOS A1 as parent", "do not pay Emergent"]
}
```

## History inside state

CAOS must carry history inside state by retaining retrieval handles, not full historical bulk.

A mature state packet should include:

- current goal
- recent decisions
- active constraints
- last confirmed error
- source/receipt pointers
- relevant memory/bin cues
- thread/file/doc identifiers
- branch/repo/commit references when applicable
- unresolved questions
- next action

Bad pattern:

```text
Load the entire old thread every turn.
```

Good pattern:

```text
Carry a compact pointer: "CAOS Care CORS login defect, commit 25dea609..., inspect backend/server.py and DevTools evidence if needed."
```

## Seed and anchor lineage

The CAOS memory model evolved from seeds into anchors and now into governed memory bins, state snapshots, metadata, and recall services.

The historical seed idea remains valid as a conceptual lineage:

### Level 1 — Thin seed

A minimal cue. It is small enough to carry often.

Example:

```text
"CAOS Care migration: move first, refactor second, no Emergent spend."
```

### Level 2 — Anchor seed

A richer summary with enough context to orient the system.

Example:

```text
"CAOS Care is a functional Emergent-built care platform being migrated to Michael-controlled Linode. Current blocker was deployed CORS misconfiguration on admin login. Repo-side fix committed. Do not nest under CAOS A1."
```

### Level 3 — Full source / evidence

The full thread, file, doc, receipt, screenshot, test log, commit, or artifact.

This is not carried by default. It is hydrated only when needed.

## Memory bins

CAOS must support bins/categories that let Aria keep the right kind of information near the surface.

Memory bins are not decoration. They are routing and retrieval structure.

Required bin concept examples:

- identity
- projects
- governance
- preferences
- relationship
- domains
- tech state
- behavioral
- traits
- learning
- real-world
- risk
- counter/corrections
- unclassified

Bins should be used to decide what becomes active, what stays standby, and what can be retrieved when mentioned.

## Recall behavior

CAOS recall must support:

- exact search
- fuzzy semantic search
- thread title search
- within-thread search
- project search
- file/document search
- metadata search
- date/time range search
- event search
- entity/person/place search
- alias search
- correction/counter-memory search
- receipt search

The user should be able to say:

```text
"Find the thing from around two years ago when I bought those boats."
```

CAOS should search using:

- approximate date
- entity/object: boats
- user event memory
- threads
- titles
- messages
- receipts
- images/files if relevant
- location/time metadata
- related aliases or descriptions

Then CAOS should return the likely result with confidence and source evidence.

## Metadata requirements

Every memory atom, anchor, state packet, receipt, thread summary, and artifact should carry metadata when possible.

Important metadata:

- id
- type
- bin/category
- title/label
- source type
- source pointer
- created_at
- updated_at
- event_at when different from created_at
- confidence
- importance
- user scope
- platform/domain
- project
- thread id/title
- file path
- commit SHA
- route/page/surface
- involved people/entities
- tags
- aliases
- retrieval cues
- correction/supersession state
- receipt references

Metadata is what allows fast recall without stuffing everything into context.

## Receipts everywhere

Every meaningful action should create or reference a receipt.

Receipt-worthy events include:

- file created
- file changed
- commit made
- memory created
- memory confirmed
- memory forgotten
- memory reclassified
- error observed
- error fixed
- command run
- migration step completed
- deployment restarted
- tool invoked
- screenshot/visual evidence inspected
- UI route/state changed when relevant
- user correction received

Receipt fields should include:

- what happened
- who/what did it
- when
- why
- source/evidence
- affected platform/project
- before/after when applicable
- status
- next action

## UI, code, and behavior comparison

CAOS must be able to reason across three evidence types:

### Code evidence

What the source files say should happen.

Examples:

- route definitions
- API client base URL
- auth logic
- CORS configuration
- component structure
- seeded users

### Visual evidence

What screenshots or live UI state show.

Examples:

- page layout
- visible controls
- error toast
- Network tab status
- admin dashboard shape
- route currently active

### Behavioral evidence

What actually happens when the user clicks, submits, runs a command, or tests a route.

Examples:

- login fails
- browser blocks CORS
- API returns 403
- seed runs on startup
- health endpoint returns db up

The system must compare these layers and not rely on one alone when evidence conflicts.

## Page/workspace awareness

Every CAOS platform should expose a compact UI-state packet to Aria when appropriate.

Fields may include:

- domain/platform
- route
- page/surface
- user role
- active mode
- visible panels
- open drawers/modals
- selected item
- active form
- last action
- last error
- feature flags
- local date/time
- user-declared location

This gives Aria practical workspace awareness without requiring large screenshots every turn.

## Optional visual snapshot

When UI-state metadata is insufficient, CAOS may provide a low-cost visual snapshot.

Requirements:

- use the smallest sufficient visual representation
- avoid high-resolution screenshots unless needed
- prefer structured UI state over image context
- attach screenshot only when visual layout/error evidence matters
- receipt the screenshot/source when used

Goal:

```text
Enough visual awareness to help, not enough visual bulk to slow the system down.
```

## Hydration policy

CAOS should hydrate deeper context only when thin state is insufficient.

Hydration triggers include:

- user asks for deep history
- exact source verification needed
- code modification required
- conflicting evidence found
- high-risk action requested
- memory ambiguity detected
- recall confidence too low
- deployment/runtime debugging needed

Hydration must be selective and receipted.

## Performance doctrine

CAOS must be fast.

Preferred behavior:

- carry kilobyte-scale state packets
- retrieve/hydrate only what is needed
- cache verified search/research results
- preserve retrieval handles
- avoid repeated research when cached information is fresh
- avoid loading full history by default
- avoid huge screenshot/image context unless necessary

Target experience:

```text
Normal turns: as close to instant as possible, target under 3 seconds.
Tool/debug turns: bounded, with explicit receipts and no unnecessary repeated work.
```

## Global applicability

This contract applies to:

- CAOS Core
- CAOS Care
- CAOS Connect
- CAOS Tradings
- future CAOS verticals
- admin helpers
- user-facing helpers
- build agents
- memory agents
- QA/checker agents

Every platform should be capable of supplying thin state to Aria, and every Aria should be capable of using thin state to retrieve deeper context when needed.

## Implementation direction

Suggested modules/services:

- thin_state_service
- state_snapshot_service
- memory_relevance_service
- recall_assist_service
- alias_resolution_service
- thread_search_service
- receipt_service
- ui_state_service
- visual_snapshot_service
- hydration_policy
- context_lineage_service
- metadata_index_service
- global_verified_cache_service

## Non-negotiable

CAOS must not become slow because it carries everything.

CAOS must not become dumb because it carries too little.

The correct architecture is thin state plus powerful retrieval:

```text
small active state
+ rich metadata
+ bins/anchors/seeds
+ receipts
+ selective hydration
= fast, truthful, long-term operational memory
```
