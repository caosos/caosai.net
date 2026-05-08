# CAOSCare Product Preview

CAOSCare is the first major product direction planned around the CAOS architecture.

It is focused on assisted-living and senior-care workflows where staff need better context, faster response support, cleaner documentation, and practical alert routing.

## Product Goal

CAOSCare is intended to help care teams manage routine and urgent resident-support workflows with better memory, documentation, and response coordination.

It is not intended to replace caregivers, nurses, physicians, emergency services, or clinical judgment.

## Core Use Cases

### Resident Request Support

A resident activates a pendant, tablet, or other approved input device.

CAOSCare can help:

- identify the resident/context;
- log the request time;
- route the request to staff;
- preserve the interaction history;
- escalate repeated or unresolved requests;
- support staff with relevant context.

### Staff Notes and Observations

Staff can capture short notes during real work.

Examples:

- “Room 212 refused lunch.”
- “Resident seemed dizzy after standing.”
- “Housekeeping request completed.”
- “Maintenance issue in bathroom sink.”

CAOSCare can structure the note, route it to the correct bin, and make it searchable later.

### Care Plan Documentation

CAOSCare can support tracking:

- what care was provided;
- who provided it;
- when it happened;
- whether follow-up is needed;
- whether repeated patterns are emerging.

### Repeated Call Escalation

Many existing pendant systems throttle repeated alerts. CAOSCare can add value by tracking repeated activations and unresolved requests.

Example:

```text
Resident pressed pendant 3 times in 4 minutes.
No documented staff response yet.
Escalate visibility.
```

### Tablet / Receiver Bridge

The near-term practical direction is to use existing pendant infrastructure where possible, with a tablet or small receiver-connected device acting as the bridge into the CAOSCare software layer.

## Safety Boundary

CAOSCare should be framed as:

- response support;
- workflow routing;
- documentation support;
- reminder support;
- escalation support;
- context recall.

CAOSCare should not be framed as:

- autonomous medical diagnosis;
- emergency-service replacement;
- independent clinical decision-maker;
- staff replacement.

## Architecture Direction

```text
Pendant / tablet / voice note
  -> event capture
  -> CAOSCare backend
  -> resident/staff/context bin
  -> workflow routing
  -> staff dashboard / response layer
  -> receipt and follow-up record
```

## Why CAOSCare Fits CAOS

CAOSCare needs exactly the capabilities CAOS is being built around:

- persistent memory;
- structured bins;
- context rehydration;
- speech-friendly interaction;
- low-friction note capture;
- tool-connected workflows;
- safe escalation rules;
- explainable receipts;
- model routing for cost control.

## Current Position

CAOSCare is a private product direction. This public document describes the concept and safety boundary without exposing private implementation details, facility-specific data, or sensitive operational information.
