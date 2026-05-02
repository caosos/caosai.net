# Frontend Visual and Behavior Contract

## Purpose

The CAOS rebuild should preserve the useful visible behaviors from the existing builds while improving color, layering, speed, modularity, and reliability.

Base44 and Emergent are both visual/behavior references. They are not code sources for this rebuild.

## Reference rule

- Base44: feature-inventory and behavior evidence, plus visual reference for starfield depth, visible stars behind translucent chat surfaces, and selected menu interaction patterns.
- Emergent: preferred final visual direction, especially darker shell color direction, translucent header, and current working feature set.
- Final CAOS: combine the best behavior of both without copying code or preserving known UI mistakes.

## Hard exclusions

- Do not use Base44 code.
- Do not recreate Base44's harsh opaque user bubble.
- Do not bury the starfield under opaque foreground layers.
- Do not silently drop features from either reference build without documenting intentional divergence.
- Do not build frontend implementation until contracts, provenance, and acceptance criteria are documented.

## Global visual target

- Dark mode is the preferred primary mode.
- Light mode must exist as a supported alternate mode.
- Emergent is the preferred final color direction.
- Starfield/space background must remain visibly alive.
- Foreground surfaces should use glass/translucent layering where readability allows.
- UI should not bury the background under opaque panels unless the surface requires high readability.

## Starfield and layering

Required behavior:

- Stars remain visible behind chat content surfaces.
- Background motion/depth remains perceptible through translucent message bubbles.
- Planets/constellations are allowed only if they do not clutter the UI or reduce readability.
- Header and major shell surfaces may be translucent.
- Message bubbles must not become opaque blocks that kill the depth effect.

## Message bubbles

Preferred:

- User and assistant bubbles should belong to the same visual family.
- User bubble should not be a harsh opaque blue/purple slab.
- Message bubbles should be dark, translucent, readable, and atmospheric.
- User and assistant messages can differ subtly by border, accent, alignment, or label, not by visually heavy opaque fill.

## Thread restore behavior

On refresh/reopen:

- Restore the last active thread.
- Scroll to the last message or last meaningful read position.
- Do not default to the first message unless the user explicitly opens from the beginning.

## Down / jump button behavior

The down button must reliably jump to the latest/current message position.

It should:

- appear when the user is away from the latest message
- disappear or deactivate when already at the latest position
- work after refresh, thread load, streaming, and delayed render
- not require multiple clicks to settle

## Previous threads panel

The previous threads panel should:

- slide/open reliably
- preserve readable thread titles
- expose search across thread title and thread content metadata
- support fuzzy/non-exact search
- not require the user to remember exact wording

## Settings/profile menu

The profile dropdown layout is useful and should remain conceptually similar.

The settings panel layout is acceptable as a reference, but color treatment should be refined:

- prefer darker Emergent-like color direction
- avoid color choices that feel flat, muddy, or visually disconnected from CAOS
- maintain readability and clear grouping
- ensure toggles and controls remain legible in both dark and light modes

## Public vs app surfaces

Some CAOS surfaces will be login-gated. Public marketing/discoverability pages must describe those features without exposing private app data.

Frontend implementation must distinguish:

- public crawlable pages
- authenticated app shell
- admin-only surfaces
- user-private memory/artifacts/tickets/connectors

## Screenshot/photo provenance

Any screenshot used to justify implementation must record:

- reference ID
- origin: Base44, Emergent, current build, concept, or defect
- screen/feature area
- reference type: visual, behavior, or both
- what it proves
- what to keep
- what to change
- target requirement
- acceptance criteria

## Feature parity rule

Existing major features and behaviors must be accounted for, even if redesigned visually.

The rebuild may change colors, layout polish, and implementation, but it must not silently drop features.

## Acceptance criteria

A frontend slice is not accepted unless it documents:

- source reference origin
- behavior preserved
- intentional visual divergence
- regression risk
- receipt/logging behavior where applicable
- dark and light mode expectations
- whether the surface is public, authenticated, or admin-only

## Non-negotiable

Visual references are inputs to the blueprint. They do not authorize copying old code. Behavior parity matters; exact color copying does not.
