# Feature Lock and Regression Contract

## Purpose

CAOS must not degrade working features while adding new ones. Once a feature reaches an accepted behavior baseline, it becomes locked. Future work must identify possible regression risk before touching files in or near that feature lane.

This contract exists because prior builds showed feature and behavior degradation, especially around TTS/STT and UI behavior.

## Core rule

Do not improve one lane by silently breaking another.

Every feature addition or refactor must answer:

- What feature lane is being touched?
- What existing behaviors could regress?
- What files are in the blast radius?
- What acceptance checks prove the old behavior still works?
- What receipt documents the change?

## Feature lock definition

A feature is locked when it has:

1. documented expected behavior
2. known files/modules
3. acceptance criteria
4. smoke or regression checks
5. receipts for future changes
6. owner lane or agent assignment

Locked does not mean frozen forever. It means changes must be intentional, tested, and documented.

## Regression risk procedure

Before modifying a locked or adjacent feature, the agent must record:

```text
Feature lane:
Files to modify:
Files indirectly affected:
Existing behavior to preserve:
Possible regression:
Regression check:
Rollback plan:
Receipt required:
```

## Initial locked-feature candidates

These lanes require extra caution:

- TTS / read-aloud behavior
- STT / microphone transcription
- chat composer and input controls
- message bubble rendering
- scroll-to-latest/down button behavior
- thread restore and previous-thread search
- WCW meter and engine selector
- memory capture/review/reclassify/forget
- receipts and diagnostic envelopes
- admin boundary and support-ticket actions
- artifacts/files/photos/links surfaces

## TTS/STT special caution

TTS and STT have historically regressed easily. Before touching them, agents must inspect Michael's logs/notes when available and document known failure modes.

Known categories to capture when logs are provided:

- browser speech API failures
- idle/background silent failure
- wrong voice/rate settings key
- click-outside/menu issues
- audio chunk sequencing
- emoji spoken aloud instead of stripped
- microphone permission failures
- transcription punctuation/format issues
- overlapping playback or stale audio element cleanup

## Acceptance checks

Each locked feature should eventually have one or more checks:

- unit/contract test
- route smoke test
- UI behavior checklist
- screenshot/video reference
- manual acceptance script
- regression note in Troubleshooting Vault

## Troubleshooting Vault link

When a regression is found and fixed, the problem and prevention rule must be added to:

`docs/TROUBLESHOOTING_VAULT.md`

## Non-negotiable

No feature should be considered complete if it breaks a previously accepted behavior without documenting that change and receiving approval where required.
