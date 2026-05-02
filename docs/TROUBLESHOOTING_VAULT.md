# Troubleshooting Vault

## Purpose

The Troubleshooting Vault preserves solved problems, failed attempts, root causes, fixes, receipts, and prevention notes so CAOS builders do not repeat the same mistakes.

This vault is build evidence. It should be used by agents before attempting fixes in the same area.

## Entry format

```text
ID:
Date:
Area:
Origin:
Symptom:
Impact:
Root cause:
Failed attempts:
Final fix:
Files affected:
Commits/receipts:
Verification:
Prevention rule:
Related docs:
```

## Required use

Agents must check this vault when working on:

- repeated bugs
- UI behavior mismatches
- failed route imports
- auth/session problems
- memory retrieval issues
- WCW/context issues
- provider/model issues
- connector/tool issues
- frontend scroll/search/layout defects
- deployment/runtime failures
- STT / Whisper transcription anomalies
- TTS / read-aloud regressions

## Initial known troubleshooting categories

### Git and repository setup

- Wrong remote risk.
- Missing Git author identity.
- Accidentally staging runtime data.
- GitHub connector search false negatives.

### UI and behavior

- Starfield visibility lost behind opaque layers.
- User bubble too opaque/bright.
- Previous thread search too exact.
- Last active thread/last message restore required.
- Down button must reliably jump to latest message.

### Memory and context

- Memory must not be keyword-only.
- ARC must hydrate selectively.
- Sanitization must preserve meaning and truth.
- WCW must be model-specific.

### Receipts

- Every meaningful state change requires a receipt.
- Model selection, memory writes, context hydration, connector calls, admin actions, and errors must be receipted.

### TTS / STT

- STT/Whisper may introduce unintended names, actors, tools, repos, branches, or authority claims into dictated text.
- Newly introduced actors in a tightly scoped workflow must be treated as possible transcription errors until context confirms them.
- TTS/STT defects are build-relevant regressions, not casual chat noise.

## Recorded incidents

### STT-001 — Whisper introduced an unintended actor into CAOS build workflow

```text
ID: STT-001
Date: 2026-05-02
Area: STT / Whisper transcription / actor identity integrity
Origin: Michael dictated a CAOS build-status handoff message; transcript introduced or preserved an unintended actor name in the phrase "message that I got from Ed".
Symptom: The assistant accepted the transcribed actor as real and referred to "Ed" as a separate worker/agent.
Impact: The build conversation temporarily gained a false actor identity. This created confusion in a governed workflow where Michael + Aria / Agent Aria / build partner are the same operational head unless Michael explicitly defines a separate actor.
Root cause: STT transcription anomaly plus model synthesis failure. Whisper/STT produced text inconsistent with known CAOS context; the assistant failed to mark it suspicious before using it as fact.
Failed attempts: The assistant initially carried the false actor forward in later status language.
Final fix: Document this as a required STT anomaly guard and future regression case.
Files affected: docs/TROUBLESHOOTING_VAULT.md; docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md
Commits/receipts: Pending commit for this documentation update.
Verification: Future STT/composer handling must mark new unexpected actor/name/tool/repo/branch/authority references as POSSIBLE_TRANSCRIPTION_ERROR when they conflict with established CAOS workflow context.
Prevention rule: If dictated text introduces a new actor, name, tool, repo, branch, instruction, or authority that conflicts with established CAOS context, do not silently accept it. Mark it as POSSIBLE_TRANSCRIPTION_ERROR and resolve from context or ask Michael for confirmation before using it as fact.
Related docs: docs/FEATURE_LOCK_AND_REGRESSION_CONTRACT.md
```

## Non-negotiable

If a problem is solved once, the fix and prevention rule belong here. The system should become harder to break over time.
