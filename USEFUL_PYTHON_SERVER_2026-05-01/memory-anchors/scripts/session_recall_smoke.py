"""
CAOS-A1 — Session Recall Smoke Test

ROLE
----
Script-level verification for session recall behavior.
Non-authoritative. Read-only.

EXPECTS
-------
- Deterministic ordering
- Exact session_id filtering
- asc / desc ordering
- limit handling
"""

from pathlib import Path
from caos_core.plane_b import PlaneB
from caos_core.session_recall import recall_session

root = Path("./data/session_recall_smoke")
pb = PlaneB(root)

SESSION = "session_test_001"

pb.insert_record("s1", SESSION, {"text": "first message"}, ["x"])
pb.insert_record("s2", SESSION, {"text": "second message"}, ["x"])

print("ASC:")
for r in recall_session(pb, SESSION, order="asc"):
    print(r["payload"]["text"])

print("\nDESC:")
for r in recall_session(pb, SESSION, order="desc"):
    print(r["payload"]["text"])

print("\nLIMIT=1 (ASC):")
for r in recall_session(pb, SESSION, order="asc", limit=1):
    print(r["payload"]["text"])
