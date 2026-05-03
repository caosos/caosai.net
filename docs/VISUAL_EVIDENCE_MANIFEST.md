# CAOS Visual Evidence Manifest

## Purpose

This manifest preserves visual/behavioral evidence Michael provided during the CAOS ownership-build discussion.

The next agent must inspect this manifest before making assumptions about existing CAOS behavior, UI surfaces, admin tools, memory systems, context meters, or migration/refactor strategy.

This document does not replace screenshots. It records the observed visual evidence and identifies which surfaces require screenshot/file preservation and future visual inspection.

## Required next-agent instruction

Before modifying architecture, docs, or code, the next agent must review:

```text
docs/VISUAL_EVIDENCE_MANIFEST.md
docs/OWNERSHIP_MIGRATION_MAP.md
docs/BUILD_EXECUTION_CHECKLIST.md
docs/CONTEXT_METER_AND_ARBITRATION_CONTRACT.md
docs/THIN_STATE_SNAPSHOT_AND_RECALL_CONTRACT.md
docs/MEMORY_RANKING_AND_CONTEXT_GOVERNOR_CONTRACT.md
docs/MEMORY_EVICTION_AND_ANTI_DUPLICATION_CONTRACT.md
```

The next agent must treat the screenshots Michael shared as behavioral evidence, not decoration.

## Important correction

Michael already built working CAOS systems.

The task is not to pretend the system does not exist. The task is to own it, extract proven behavior, rebuild clean modules, and avoid dragging Emergent-specific platform contamination into the final Linode-owned architecture.

## Visual evidence summary

### 1. CAOS main chat shell — Base44-style build

Observed surface:

```text
Domain shown: caos-chat-9c5683d8.base44.app/Chat
Main shell: CAOS starfield background
Header: CAOS / Cognitive Adaptive Operating System
Left dropdown menu under MICHAEL
Bottom composer with TTS, file/plus, mic, send
Engine selector chips: OpenAI, MER, Swarm
Action cards: Create Image, Upload File, Continue Thread, Multi-Model
```

Observed menu items:

```text
Desktop
New Thread
Previous Threads
Settings
Engine
Agent Swarm
Admin Dashboard
Admin Docs
Work Mode
Support Tickets
Log Out
```

Behavioral implication:

```text
The clean CAOS build must preserve the concept of a central chat shell with engine switching, memory/desktop/admin/work surfaces, bottom composer, and role-aware admin features.
```

### 2. CAOS current owned/frontier shell — caososa/caosos.com style

Observed surface:

```text
Domain shown: caosos.com
Left menu under MICHAEL CHAMBERS
Dark purple/black starfield shell
Menu includes Memory Console, Quick Capture, Engine, Agent Swarm, Admin Dashboard, Admin Docs, Support Tickets
Bottom composer with engine chip and full voice mode
Top-right working context/window meter
```

Observed labels:

```text
Memory Console — NEW
Quick Capture — NEW
Engine — Claude / OpenAI depending screenshot
Agent Swarm — E2B
Admin Dashboard — ADMIN
Admin Docs — ADMIN
Support Tickets
```

Behavioral implication:

```text
This is an already-working UX direction. The clean build should preserve the role-aware shell, admin docs, support tickets, memory console, quick capture, and context/window meter concepts.
```

### 3. Support Tickets surface

Observed surface:

```text
Title: SUPPORT TICKETS
Subtitle: Admin view · all users
Status filters:
- All · 25
- Open · 12
- In progress · 0
- Resolved · 13
- Closed · 0
```

Observed tickets:

```text
TTS Read Aloud button doesn't toggle to Stop
Core Engine Optimization: Context Cap and UI Sync
Hardcoded 3K Context Cap and Aggressive Sanitization
```

Behavioral implication:

```text
Support tickets are an existing admin/diagnostic surface. The future system must preserve ticket states, bug reports, timestamps, categories, user attribution, and admin filtering.
```

### 4. Admin Docs / Project Blueprints surface

Observed surface:

```text
Title: Admin Docs · Project Blueprints
Left file list includes:
- CAOS_CARE_PLAYBOOK.md
- CHANGELOG.md
- CONNECTORS_SPRINT_PLAN.md
- CONNECTOR_BLUEPRINT.md
- EMERGENT_MEETING_NOTES.md
- FORK_HANDOFF_2026_04_26.md
- MASTER_IMPLEMENTATION_CHECKLIST.md
- PLATFORM_PAIN_POINTS.md
- PRD.md
- ROADMAP.md
- SystemBlueprint.md
- TIER1_SPEC.md
- TROUBLESHOOTING_BULLETIN.md
- TSB_LOG.md
- UX_BLUEPRINT.md
- test_credentials.md
```

Observed doc examples:

```text
CHANGELOG.md
PLATFORM_PAIN_POINTS.md
test_credentials.md
```

Behavioral implication:

```text
Admin Docs is an existing internal documentation viewer. The clean build should preserve an admin-only docs browser that can expose blueprints, changelog, pain points, credentials/test-only notes, troubleshooting material, and implementation checklists.
```

### 5. Working Context Window / meter surface

Observed surface:

```text
Top-right meter near thread title/search.
Tooltip: Working Context Window — click to inspect what's in context
Displayed example: 13.9K / 200.0K, later 16.0K / 200.0K
Expanded panel includes fields:
- Facts
- Global cache
- ARC tokens
- Sent
- Received
- Thread tokens
- History
- Memory
- Continuity
- Global cache
- Meter source: provider usage
```

Observed numbers from screenshot:

```text
ARC tokens: 13896
Sent: 20526
Received: 1030
Thread tokens: 140950
History: 13513
Memory: 293
Continuity: 81
Global cache: 9
```

Behavioral implication:

```text
A context meter already exists visually/behaviorally. The new clean build must not only define a context meter in doctrine; it must preserve and improve this user/admin-visible inspection behavior.
```

### 6. Memory Console surface

Observed surface:

```text
Title: Memory Console
Example atom count: 351 or 352 atoms
Categories/bins include:
- Identity
- Projects
- Governance
- Preferences
- Relationship
- Domains
- Tech State
- Behavioral
- Traits
- Learning
- Real-world
- Risk
- Counter
- Unclassified
```

Observed memory atom controls:

```text
Confirm
Reclassify
Forget
```

Observed metadata chips:

```text
USER-STATED
DERIVED
confidence percentage
1 evidence
P95
date
```

Observed example atoms:

```text
User name: Aria (as used by the user to address the assistant).
User name is Michael.
User experiences skin sensitivity/breakouts triggered by specific water sources.
User notes their skin sensitivity/profile may be changing due to aging.
User views themselves as uniquely qualified for building CAOS.
```

Behavioral implication:

```text
The memory console is not hypothetical. It already expresses the bins, atom metadata, confirmation/reclassification/forget loop, evidence count, confidence, and review workflow Michael wants preserved and improved.
```

### 7. Settings surface

Observed surface:

```text
User: Michael
Role: Admin
Email shown in platform screenshots
Member since date
Assistant name: Aria
Birthday field
Permanent Memories count
Remember Conversations enabled
Game Mode admin access
Developer Mode split-screen
Multi-Agent Mode collaboration
System Console monitor metrics
Aria Mode: Fact · temp 0.1 with F/B/C toggles
Voice & Speech: nova · 1.00x
Ambient Mode
Scroll step
Bubble transparency
Connectors list
Pricing / tokens link
Delete Account
```

Behavioral implication:

```text
Settings is already a multi-control admin/user preference surface. The clean build must preserve role-aware settings, assistant naming, memory toggles, mode switches, voice settings, connector status, and admin/dev features.
```

### 8. Quick Capture surface

Observed surface:

```text
Title: Quick Capture
Counters: 0 new · 0 promoted
API key generator for Apple Shortcut, Bee pendant, scripts
Text box: Dump a thought... (Ctrl/Cmd+Enter to capture)
Tabs: New, Promoted, Dismissed, All
```

Behavioral implication:

```text
Quick Capture exists as a capture/intake workflow for thoughts, shortcuts, pendant/scripts, and later promotion into memory/workflow. The clean build should preserve the concept of external ingestion + review/promote/dismiss pipeline.
```

### 9. Previous Threads / search surface

Observed surface:

```text
Previous Threads drawer
Search all messages field
Thread cards with title, snippet, age, title match marker
Search can return no results for exact terms and multiple results for partial terms
```

Behavioral implication:

```text
Thread search is an existing feature and must be preserved/improved. It should support title search, within-thread search, snippets, age, match reason, and future semantic/fuzzy retrieval.
```

### 10. Mobile/UI bug ticket evidence

Observed support-ticket/result evidence:

```text
Title: Mobile UI broken — header overlaps, thread pill overflows
Category: UX
Description: Header layout uses desktop flexbox with no mobile breakpoint at phone widths (375–428px). Thread pill has 260px min-width that overflows on small screens. WCW meter takes up space unnecessarily. Needs @media (max-width: 480px) rules to stack header vertically and scale elements down.
```

Behavioral implication:

```text
Mobile responsiveness issues and support-ticket receipts must be treated as evidence. The clean build should include responsive header constraints and avoid desktop-only shell assumptions.
```

### 11. Emergent GitHub save modal visual reference

Observed surface:

```text
Emergent modal: Save to Github / Connecting Github
Visual style: dark modal, Matrix-like falling code background
Flow: connect GitHub, show branch/conflict options, create branch and push
```

Behavioral implication:

```text
CAOS should eventually implement a governed Commit Workspace to GitHub feature inspired by this flow, but with Michael's stricter receipts, diff review, approval gates, and no silent push.
```

## Current screenshot preservation gap

At the time this manifest was created, the assistant had not uploaded the raw screenshots into GitHub.

The next agent should preserve raw visuals if available by adding them under a path like:

```text
docs/visual-evidence/
```

Recommended filenames:

```text
caos-main-shell-base44.png
caos-main-shell-caosos.png
support-tickets-admin.png
admin-docs-changelog.png
admin-docs-platform-pain-points.png
admin-docs-test-credentials.png
working-context-window-meter.png
settings-panel-admin.png
quick-capture-panel.png
previous-threads-search.png
emergent-github-save-modal.png
```

If raw screenshots are not available, do not pretend they were saved. Use this manifest as the minimum evidence record and ask Michael for a screenshot packet or export.

## Required future behavior

When a future agent starts work, it must not say:

```text
There is no existing working UX.
```

Correct statement:

```text
Michael has working CAOS UX surfaces already. Use screenshots, repo source, docs, support tickets, and live behavior descriptions as evidence. Rebuild clean owned modules while preserving proven behavior.
```

## Non-negotiable

Visual evidence matters.

CAOS is not only backend architecture. It is also a working operational interface with admin tools, context meter, memory console, support tickets, docs browser, quick capture, settings, thread search, and engine/mode controls.

The clean build must preserve the useful behavior of those surfaces while removing platform-specific contamination and reducing monolith risk.
