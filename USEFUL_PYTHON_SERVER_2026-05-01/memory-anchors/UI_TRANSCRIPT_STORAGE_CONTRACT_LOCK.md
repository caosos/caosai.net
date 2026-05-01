CAOS-A1 — UI Transcript Storage Contract (LOCKED)

STATUS
------
LOCKED

PURPOSE
-------
Keep raw chat transcripts out of kernel cognition to prevent densification and drift.

CANONICAL RULES
---------------
1) UI OWNS RAW TRANSCRIPT
   - The UI stores full conversation scrollback/transcripts.
   - Transcript storage is UX/history, NOT cognition.

2) KERNEL NEVER INGESTS FULL TRANSCRIPT
   - Kernel inputs are single-turn message payload + explicit anchors + explicit recall only.
   - No silent “use the whole chat” behavior.

3) PLANE B IS SOLE AUTHORITY FOR TRUTH
   - Kernel writes only through Plane B.
   - Plane B persists deterministic anchors.
   - Session is an anchor class: "session:<session_id>" MUST be present on every record.

4) EXPLICIT RECALL ONLY
   - Any retrieval beyond the current turn requires an explicit recall operation.
   - No implicit context bleed from UI transcript into kernel.

5) FAILURE MODE
   - Any ambiguity or missing envelope/policy must fail-closed.

IMPLEMENTATION NOTES (CURRENT)
------------------------------
- /message writes a record to Plane B.
- UI can keep the full transcript without changing kernel cognition rules.
