# CAOS Visual Reference Evidence

## Purpose

This directory contains visual-reference evidence for the CAOS clean rebuild.

Visual evidence is allowed only when it is indexed, labeled by origin, and tied to a requirement or behavior contract.

## Required origin categories

```text
base44/
emergent/
current-build/
```

## Rules

- Do not place screenshots at repository root.
- Do not use screenshots as vague inspiration only.
- Every screenshot should have an origin, date, source branch or PR when available, and what it proves.
- Base44 screenshots are visual and behavior reference only. Do not use Base44 code.
- Emergent screenshots are current full-stack visual and behavior reference. Do not copy monoliths.
- Current-build screenshots are implementation-target and defect-comparison evidence.

## Current cleanup note

PR #1, `Emergent visual reference`, added 25 PNG screenshots directly at repository root. Those files are valid visual evidence but are in the wrong location.

Target location for those files:

```text
docs/visual-reference/emergent/
```

Until the binary move is completed, treat the root PNG files as misplaced evidence requiring relocation.
