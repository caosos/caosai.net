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

## Non-negotiable

If a problem is solved once, the fix and prevention rule belong here. The system should become harder to break over time.
