CAOS-A1 — ARE Wiring Plan (v0.1)

Goal:
- Hook ARE into Python memory service so every /message and /recall emits events.
- Expose weights to runtime correlator via endpoint or direct client call.
- Ensure receipts are returned in _meta and logged.

Planned wiring points (do not implement until inspected):
1) In /message handler:
   - build AREEvent(op="write", profile_id, lane_id, session_id, anchors, ts_ms)
   - call AREngine.apply_event(event)
   - include receipt under response["_meta"]["are_write_receipt"]

2) In /recall handler:
   - build AREEvent(op="recall", ...)
   - call apply_event
   - include receipt under response["_meta"]["are_recall_receipt"]

3) Provide "GET /are/weights?profile_id=...&lane_id=...&top_n=..."
   - returns { weights: {anchor: weight}, _meta:{...} }

DB location recommendation:
- memory-anchors/state/are/are.sqlite3 (durable, WAL enabled)

Hard rules:
- ARE never invents anchors
- ARE never changes payload or stored records
- ARE only tracks + scores anchors and returns receipts
