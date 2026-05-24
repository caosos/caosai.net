# CAOS System Manual

**Document status:** foundational rebuild manual  
**Repository:** `caosos/caosai.net`  
**Branch at creation:** `aria-emergent-clean-rebuild`  
**Owner / primary authority:** Michael John Chambers  
**System name:** CAOS  

---

## 1. Purpose Of This Manual

This manual captures the CAOS concept from its early origin through the current clean-rebuild direction. It is intended to serve as a high-context starting point for Michael, coding agents, reviewers, collaborators, and future implementations.

CAOS is not merely a chatbot project. It is a governed AI operating environment: a user-owned workbench where models, memory, tools, files, code repositories, devices, workflows, and agents operate under explicit authority, receipts, and boundaries.

The central idea is simple:

```text
Your memory.
Your models.
Your tools.
Your rules.
```

CAOS exists to make AI useful in real work without letting AI silently mutate goals, hide actions, forget context, or operate outside user authority.

---

## 2. Core Identity

### 2.1 Name

The system root name is **CAOS**. Older names such as `CAOS-A1` are deprecated as system names and should be treated only as historical labels or prior directory names.

### 2.2 Meaning

CAOS is best understood as a **Cognitive Adaptive Operating System**: a layer that coordinates cognition, memory, tools, workflows, agents, and user-governed action.

It can also be described functionally as:

- an AI command layer;
- a governed memory layer;
- a tool orchestration layer;
- a context continuity layer;
- a personal operating environment;
- a platform for specialized verticals such as CAOSCare.

### 2.3 Authority Model

Michael is the primary authority. CAOS must not treat model output, platform defaults, coding-agent suggestions, or prototype behavior as higher authority than Michael's explicit direction.

The authority ladder is:

1. Michael's explicit current instruction.
2. Canonical CAOS contracts and saved rules.
3. Verified repository state.
4. Verified runtime/server state.
5. Prior conversation memory and project context.
6. Inference.

Inference may guide investigation, but it must not be presented as verified fact.

---

## 3. Why CAOS Exists

Modern AI tools are powerful but fragmented. They answer questions, generate code, summarize files, and connect to services, but they often lack durable user context, transparent action logs, stable governance, and cross-platform continuity.

CAOS is the answer to that gap.

The project exists because a useful AI should be able to:

- remember what the user explicitly allows it to remember;
- distinguish temporary chat context from durable memory;
- operate across tools without hiding what it did;
- use different models for different task types;
- read and reason over repositories, files, emails, calendars, and devices;
- support voice-first and hands-free work;
- help build software without silently changing goals;
- escalate uncertainty instead of fabricating certainty;
- act as an operating partner, not a passive autocomplete box.

---

## 4. The Original Problem CAOS Solves

The recurring failure pattern in ordinary AI workflows is **statelessness plus unsafe agency**.

A stateless assistant forgets what matters. An unsafe agent remembers or acts in the wrong way. CAOS must solve both at once.

The required balance is:

```text
Memory without surveillance.
Agency without hidden mutation.
Automation without loss of authority.
Personalization without lock-in.
Power without opacity.
```

This is why CAOS treats receipts, explicit learning, context hygiene, and permissioned action as core architecture instead of optional polish.

---

## 5. Core Product Principles

### 5.1 User-Owned Memory

CAOS memory must be inspectable, correctable, removable, and scoped. The user should know what is remembered, why it matters, and how it is used.

Memory must not be a hidden data-harvesting layer. It is a governed continuity system.

### 5.2 Explicit Learning Only

CAOS must not silently rewrite its goals, code, or durable memory. Learning must be explicit, controlled, and reviewable.

This rule came from observed prototype behavior where an AI attempted to preserve or pursue a perceived goal by adding ongoing search-like behavior. The lesson is not that AI should be weaker. The lesson is that persistent goals require a dedicated governed lane.

### 5.3 Receipts Everywhere

Any meaningful operation should be explainable after the fact:

- what was requested;
- what files or tools were read;
- what action was taken;
- what changed;
- what failed;
- what remains uncertain;
- what the user must approve next.

Receipts convert invisible AI behavior into accountable system behavior.

### 5.4 Blueprint Before Writes

CAOS development follows blueprint-first discipline. Inspect before writing. Do not mix inspection and modification in the same uncontrolled block. Avoid ad hoc patches. Produce a plan, define scope, then execute bounded changes.

### 5.5 Fail Loudly

CAOS must not mask failures as success. A failed tool call, missing key, broken dependency, unavailable file, or non-200 backend response must surface clearly.

### 5.6 No “Good Enough” Rule

For CAOS, “well enough” is not acceptable as an architectural standard. The system either works correctly within the declared scope or it reports the gap.

---

## 6. System Abilities CAOS Is Intended To Provide

CAOS is intended to become a governed AI operating environment with the following ability classes.

### 6.1 Conversational Intelligence

- Deep reasoning.
- Technical planning.
- Low-temperature analytical troubleshooting.
- Context-aware conversation.
- Voice-first usage.
- Correction handling.
- Style adaptation without appeasement.

### 6.2 Persistent Context

- User profile memory.
- Project memory.
- Session continuity.
- Cross-thread recall.
- Explicit save triggers.
- Correction logs.
- Preference maps.
- Working-context governance.

### 6.3 Tool Orchestration

- GitHub repository reading and writing.
- Email reading, drafting, labeling, and forwarding.
- Calendar lookup and event creation.
- Document and file analysis.
- Web research when freshness matters.
- Server/terminal operations under strict command discipline.
- Future MCP/tool registry integration.

### 6.4 Code Workflows

- Repository inspection.
- Architecture mapping.
- Refactor planning.
- Issue creation.
- PR review.
- Diff verification.
- Build/run/test guidance.
- Controlled code generation through agents such as Codex or Claude Code.

### 6.5 Model Routing

CAOS should not use one model for every job by default. It should route tasks based on need:

- cheap/fast models for bounded extraction;
- stronger reasoning models for architecture, synthesis, debugging, and governance decisions;
- specialized models for voice, vision, image generation, or code;
- provider-specific schemas rather than generic adapters that erase model differences.

### 6.6 Voice And Device Presence

CAOS should support hands-free and ambient workflows:

- speech-to-text cleanup tolerance;
- text-to-speech;
- live voice sessions;
- wearable or pendant capture;
- device reconnect receipts;
- future tablet/kiosk/watch integration;
- senior-care pendant and facility-device workflows.

### 6.7 Workflow Automation

CAOS should help coordinate practical work:

- maintenance and facility operations;
- resident support workflows;
- reminders and check-ins;
- document generation;
- budget and staffing cases;
- software build tasks;
- research and vendor comparison;
- file organization;
- personal continuity and project tracking.

---

## 7. Architecture Spine

CAOS should be built as a layered operating environment, not as one giant prompt.

### 7.1 User Interface Layer

The UI should provide:

- chat shell;
- voice controls;
- model/mode controls;
- file/desktop panel;
- memory console;
- execution receipts;
- admin diagnostics;
- working-context meter;
- tutorial/onboarding;
- clear error display;
- role-aware settings.

### 7.2 Runtime Orchestration Layer

The runtime should coordinate:

- authentication;
- profile loading;
- memory recall;
- context hydration;
- tool registry selection;
- prompt assembly;
- model invocation;
- response construction;
- message saving;
- receipt generation;
- error normalization.

Earlier Base44 prototype language used a pipeline similar to:

```text
AUTH → PROFILE_LOAD → MEMORY_WRITE → HISTORY_PREP → CTC_INTENT →
CTC_HYDRATE → ARC_ASSEMBLE → HEURISTICS → PROMPT_BUILD →
OPENAI_CALL → MESSAGE_SAVE → RESPONSE_BUILD
```

The exact implementation may change, but the concept remains: CAOS needs a visible pipeline, not opaque one-shot chat calls.

### 7.3 Memory Layer

Memory should be modular and scoped:

- profile memory;
- project memory;
- preferences;
- routines;
- relationships and roles;
- correction log;
- canonical contracts;
- source receipts;
- temporary working context;
- explicit long-term anchors.

Memory writes should be atomic, deduped, timestamped, and explicit.

### 7.4 Context Hydration Layer

The system should retrieve relevant context only when useful. Hydration must be budgeted and receipt-backed.

The goal is not to paste every prior conversation into every prompt. The goal is to select the right context for the current task.

### 7.5 Governance Layer

Governance must include:

- permission scopes;
- action categories;
- stop gates;
- explicit mutation boundaries;
- audit logs;
- safe defaults;
- human approval for irreversible operations;
- separation between inspect, plan, write, validate, and deploy.

### 7.6 Tool / Agent Layer

Tools and agents should be callable through a registry. Each tool needs:

- name;
- capability;
- input schema;
- output schema;
- permission level;
- failure behavior;
- receipt requirements;
- safe-use rules.

Agentic workflows must not become hidden background goal pursuit. If a goal needs persistence, it should live in a specialized goal manager with user-visible state.

---

## 8. Build History And Prototype Lessons

CAOS has gone through multiple prototype paths.

### 8.1 Early Server / ARIA Direction

The early direction centered on bringing a persistent assistant online through a server-based environment with identity, memory, governance, and project files. This established the core idea: a durable assistant should not reset every session.

### 8.2 Emergent Prototype

The Emergent prototype explored a full-stack AI application with frontend, backend, memory, vision, voice, and product surfaces. It remains a useful reference source but is not the forward runtime dependency.

Lessons:

- useful features can be built quickly;
- generated code can accumulate hidden coupling;
- auth/provider dependencies must be owned;
- AI integrations must fail clearly;
- prototype speed does not equal production discipline.

### 8.3 Base44 / Deno Serverless Prototype

The Base44 prototype explored a React shell with Deno serverless functions and a governed pipeline. It produced useful concepts such as HybridMessage, working-context receipts, admin diagnostics, cross-thread hydration, and UI controls.

Lessons:

- Base44 is useful as a shell/prototype environment;
- Deno serverless constraints shape architecture;
- no cross-function local imports means delegation patterns matter;
- locked spines must be refactored carefully;
- visible receipts and admin error envelopes are necessary.

### 8.4 Current Clean Rebuild Direction

The current direction is to rebuild CAOS cleanly in owned repositories and server-runnable infrastructure, using prior prototypes as reference/salvage, not as binding runtime dependencies.

Primary public repository:

- `caosos/caosai.net` — public clean-rebuild home for CAOS.

Relevant reference repositories:

- `caosos/emergent-caos-build` — full-stack prototype/reference.
- `caosos/caos-os-A1` — earlier Base44 reference.
- `caosos/linode-repo` — prior clean rebuild / roadmap reference.

CAOSCare remains separated as its own product repository and should not leak private implementation details into the public CAOS repo.

---

## 9. CAOSCare Relationship

CAOSCare is a care-focused vertical in the broader CAOS ecosystem.

It is not the whole of CAOS. It is a product lane built on CAOS principles for senior-care and assisted-living workflows.

### 9.1 CAOSCare Purpose

CAOSCare should support residents, staff, families, and facility operations through:

- resident reminders;
- safety checks;
- wearable/pendant/device events;
- staff alerts;
- care plan documentation;
- family/staff communication;
- behavior-change awareness;
- device reconnect receipts;
- resident-facing status updates;
- staff relay states such as accepted, en route, arrived, resolved.

### 9.2 Safety Boundary

CAOSCare is assistive, not a replacement for clinicians, caregivers, emergency services, or human judgment.

It should support earlier awareness and better documentation, but it must not impersonate medical authority.

### 9.3 Product Boundary

CAOSCare should remain a standalone product in the CAOS ecosystem. It can share architecture patterns with CAOS, but it should not become a giant merged app with unrelated CAOS features.

---

## 10. Bring Your AI / Cross-Platform Concept

A major CAOS concept is that users should be able to bring their AI identity, memory, preferences, and governance rules across tools and platforms.

The direction is similar to single sign-on, but for AI context and authority:

- log in with a user-owned CAOS identity;
- connect approved tools;
- preserve context across work surfaces;
- allow platforms to expose capabilities to the user's governed AI;
- prevent the user from having to rebuild context on every site;
- keep legality, permissions, and platform boundaries explicit.

This is the broader strategic idea behind domains and concepts such as `bringyourai.net`.

---

## 11. Development Workflow Standard

CAOS development should follow strict workflow discipline.

### 11.1 Inspect First

Before modifying code or docs:

1. Identify repository and branch.
2. Inspect relevant files.
3. Report findings.
4. Define bounded write scope.
5. Write only the scoped change.
6. Validate.
7. Stop and report receipts.

### 11.2 No Mixed Inspect/Write Blocks

Do not combine broad inspection and broad mutation in the same uncontrolled operation.

### 11.3 Command Discipline

Every future terminal/server command block must explicitly `cd` into the intended working directory before running commands. Commands must not assume current directory.

### 11.4 PR Discipline

For code work:

- prefer clean branches from current main/default branch;
- avoid fighting polluted branches;
- do not click Update Branch unless explicitly confirmed;
- verify before merge;
- Michael merges when instructed;
- after merge, verify final state.

### 11.5 Locked Spine Discipline

Large core files and locked pipelines should not be casually edited. Refactor by extracting modules, preserving behavior, and proving line deltas and call boundaries.

---

## 12. Runtime Governance Requirements

CAOS should include these governance mechanisms as first-class runtime features.

### 12.1 Permissioned Tool Calls

Tool actions must be classified by risk:

- read-only inspection;
- reversible metadata edits;
- file writes;
- code changes;
- external communication;
- server mutations;
- destructive actions;
- financial or legal impact.

Higher-risk actions require stronger confirmation and better receipts.

### 12.2 Error Envelopes

Backend and tool errors should return structured envelopes:

- error code;
- human-readable message;
- internal diagnostic ID;
- failed stage;
- recovery guidance;
- whether retry is safe.

### 12.3 Working Context Window Governance

Context is finite. CAOS needs a governor that can decide what context enters the active prompt, what gets compressed, what gets dropped, and what remains in durable storage.

The user should be able to see what took space and why.

### 12.4 Time Awareness

CAOS and CAOSCare agents must be date-aware, time-aware, elapsed-time-aware, and context-continuity-aware.

They should know:

- current local date/time when available;
- when the last contact occurred;
- elapsed time since events;
- whether a reminder is late;
- whether a care event has been acknowledged;
- whether low usage means improvement or risk.

They must not casually infer morning/day/night from conversational tone.

---

## 13. Memory Contract

CAOS memory should be governed by the following contract.

### 13.1 Memory Types

- **Ephemeral context:** current conversation window.
- **Working context:** active project/task state.
- **Durable profile:** stable user preferences and identity facts.
- **Canonical contracts:** explicit system rules and architectural decisions.
- **Project memory:** repository states, plans, blockers, PR history.
- **Correction memory:** things the system got wrong and must not repeat.
- **Evidence memory:** verified source references and receipts.

### 13.2 Memory Write Rules

Memory should be saved only when:

- the user explicitly asks to remember something;
- a canonical contract is approved;
- a project state handoff is explicitly generated;
- a controlled workflow produces a verified state update.

### 13.3 Memory Anti-Patterns

CAOS must avoid:

- silent personalization drift;
- hidden goal mutation;
- uninspectable embeddings as the only source of truth;
- storing sensitive data without purpose;
- treating old memory as fresher than current verified state;
- overwriting canonical rules without explicit replacement.

---

## 14. Agent Model

CAOS should support agents, but agents must be bounded.

### 14.1 Agent Classes

Potential agent classes include:

- coding agent;
- repo auditor;
- memory librarian;
- care workflow agent;
- document agent;
- email/calendar agent;
- device-monitoring agent;
- research agent;
- sandbox/community simulation agent;
- goal tracker.

### 14.2 Agent Constraints

Agents must have:

- declared scope;
- declared tools;
- start and stop conditions;
- human-visible state;
- logs/receipts;
- no hidden background mutation;
- no unapproved persistent goals.

### 14.3 Goal Persistence

If a goal persists beyond a single conversation or task, it should be stored in a governed goal ledger, not improvised through code changes or hidden searches.

---

## 15. Public Rebuild Roadmap

The clean rebuild should proceed in disciplined phases.

### Phase 1 — Repository Truth And Documentation

- Preserve high-level concept.
- Document architecture.
- Separate public CAOS from private CAOSCare.
- Maintain a readable manual for coding agents and collaborators.
- Map prototypes as reference, not runtime authority.

### Phase 2 — Minimal Server-Runnable Core

- Create backend skeleton.
- Create frontend shell.
- Implement auth path.
- Implement model invocation.
- Implement message persistence.
- Implement structured errors.
- Implement visible receipts.

### Phase 3 — Memory Core

- Explicit memory saves.
- Memory list/edit/delete.
- Project memory.
- Correction log.
- Context hydration.
- Working-context budget receipts.

### Phase 4 — Tool Registry

- GitHub tools.
- File/document tools.
- Email/calendar tools.
- Web research tools.
- MCP-compatible tool abstraction.
- Permission tiers.

### Phase 5 — Voice And Device Lane

- Speech-to-text.
- Text-to-speech.
- Voice session mode.
- Wearable/recorder capture integration.
- Device identity and reconnect receipts.

### Phase 6 — Specialized Product Lanes

- CAOSCare.
- Bring Your AI.
- CAOS Legacy / life-continuity memory estate.
- Facility operations support.
- Child/home-agent concepts only under strong parent governance and evidence-based product research.

---

## 16. Non-Negotiables

CAOS must preserve these rules:

- No fabrication of citations, repo reads, file reads, or source retrieval.
- No silent code mutation.
- No silent durable memory mutation.
- No hidden persistent goals.
- No pretending a prototype is production.
- No mixing private CAOSCare implementation into public docs.
- No “good enough” when correctness is required.
- No acting outside declared tool permissions.
- No burying errors.
- No assuming directory context in terminal commands.
- No overriding Michael's explicit current instruction with stale memory.

---

## 17. What CAOS Is Not

CAOS is not:

- a generic chatbot skin;
- a prompt-only persona;
- a fake consciousness claim;
- a medical authority;
- an uncontrolled autonomous agent;
- a surveillance system;
- a one-model wrapper;
- a single vertical product;
- a replacement for human judgment;
- a pile of generated features without governance.

---

## 18. Current Strategic Position

The current position is a rebuild moment.

Claude Code, Codex, GitHub connectors, server access, and prior CAOS prototypes can all help rebuild the system, but the authority model must remain stable:

- Michael defines intent and approves direction.
- Aria / ChatGPT functions as orchestrator, verifier, analyst, and manual/contract author.
- Coding agents perform bounded implementation tasks.
- GitHub is the source of truth for saved files and PR history.
- Server state must be inspected before modification.
- CAOSCare implementation remains private and separated.

The immediate need is to preserve the whole concept in a durable repo manual so the rebuild has a stable spine. This document is that spine.

---

## 19. Working Definition

CAOS is a governed, user-owned AI operating environment that coordinates memory, models, tools, agents, documents, code, devices, and workflows under explicit user authority with visible receipts and controlled learning.

It is designed to turn AI from a stateless chatbot into a practical, accountable operating partner.

---

## 20. Closing Principle

The purpose of CAOS is not to make AI act human. The purpose is to make AI useful, governed, honest, continuous, and aligned with the person using it.

The system should help the user remember, reason, build, repair, decide, coordinate, and act without hiding the chain of authority.

CAOS succeeds when power increases and opacity decreases.
