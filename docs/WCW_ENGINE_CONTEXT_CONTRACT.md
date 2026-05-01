# WCW Engine Context Contract

## Purpose

The Working Context Window (WCW) is not a single global number. WCW depends on the selected inference provider/model. The UI must reflect the active engine's usable context wherever engine selection or response receipts are shown.

## Required UI surfaces

WCW/model context state must be represented in at least three places:

1. Profile/settings dropdown with engine/options controls.
2. Assistant response bubble/receipt area.
3. Bottom composer/inference-engine selector.

Changing the selected inference engine must update the displayed available/usable working context.

## Required backend contract

The backend must expose model context metadata as part of runtime/model selection and chat receipts.

Required fields:

```text
provider
model
context_window_tokens
usable_context_tokens
reserved_output_tokens
reserved_system_tokens
wcw_policy
```

## Definitions

### context_window_tokens

The model's nominal maximum context window.

### usable_context_tokens

The portion of the context window CAOS allows for working context after reserving output, system/developer instructions, receipts, and safety overhead.

### reserved_output_tokens

Tokens reserved for the assistant response.

### reserved_system_tokens

Tokens reserved for system/developer/personality/tooling and required operational context.

### wcw_policy

A named policy explaining how CAOS computes usable WCW for the selected model.

## UI behavior

When the user changes inference engine:

- active model changes
- WCW meter recalculates
- composer selector updates
- profile/settings model display updates
- next response bubble receipt records the selected provider/model and WCW budget

## Non-negotiable

Never hard-code one WCW number as universal. Different inference engines may have different context windows, reserved-token policies, costs, latency behavior, and output limits.
