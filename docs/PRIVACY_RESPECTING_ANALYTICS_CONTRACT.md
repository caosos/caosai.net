# Privacy-Respecting Analytics Contract

## Purpose

CAOS needs analytics to improve the product, measure reliability, understand feature adoption, detect regressions, and control cost. Analytics must be privacy-respecting and product-metric focused.

CAOS must not use an ad-surveillance model.

## Core rule

Measure the product. Do not profile the person for advertising.

Analytics should help answer:

- Which features are used?
- Which features fail?
- Which flows are confusing?
- Which routes are slow?
- Which providers/models are expensive or unreliable?
- Which UI surfaces need improvement?
- Which errors or regressions repeat?
- Which onboarding paths convert or stall?

Analytics should not be used for:

- selling user data
- third-party behavioral profiling
- ad targeting
- hidden cross-site tracking
- invasive surveillance
- exposing private memory/thread/file contents

## Allowed analytics categories

Product metrics:

- page/screen visits
- feature adoption
- route latency
- error rates
- degraded-mode rates
- model/provider selection counts
- WCW/context budget usage
- connector enabled/disabled state counts
- support ticket volumes/statuses
- onboarding funnel progress
- session duration at coarse level
- retention/cohort metrics where privacy-safe

Operational metrics:

- backend route success/failure
- provider latency
- provider timeout rates
- model cost class/estimated usage
- memory capture/review counts
- artifact creation counts
- search success/no-result rates
- TTS/STT failure categories

## Disallowed analytics categories

Do not collect for analytics unless explicitly required by user-visible product function and safely scoped:

- raw message content
- raw memory contents
- raw files/photos/emails/documents
- secrets or credentials
- full connector payloads
- sensitive personal details
- precise unnecessary location tracking
- cross-site advertising identifiers

## Event design rule

Analytics events should be structured, minimal, and purpose-bound.

Example event shape:

```text
event_name
user_scope_hash or account_id if appropriate
session_id if appropriate
timestamp
feature_area
status
latency_ms
error_code
provider/model metadata when relevant
non-sensitive counts/flags
```

## Receipt relationship

Receipts and analytics are related but not identical.

- Receipts explain specific meaningful actions to the user/system.
- Analytics aggregate product behavior for improvement and reliability.

Analytics should reference receipt IDs where useful, but must not duplicate private receipt payloads into analytics systems unnecessarily.

## User trust requirements

CAOS should provide a privacy explanation that states:

- what is measured
- why it is measured
- what is not sold
- what is not used for ads
- how private content is protected
- what controls the user has

## Launch requirements

Before launch, define:

- analytics event taxonomy
- privacy page language
- opt-out or settings strategy where appropriate
- retention policy
- access controls for analytics dashboards
- no-ad-surveillance policy

## Non-negotiable

No ad-surveillance model. No selling user data. No third-party behavioral profiling. Analytics exist to improve CAOS, not to exploit users.
