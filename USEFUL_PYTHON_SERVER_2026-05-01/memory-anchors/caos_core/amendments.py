"""
CAOS-A1 — Amendments & Lineage

ROLE
----
Correction and compliance without mutating truth.

INVARIANTS
----------
- No deletes
- No overwrites
- Corrections are append-only (data)
- Full lineage preserved (A → B → C)
- latest_valid always points to the most recent valid record
- Amendment application is atomic with Plane B
"""

from __future__ import annotations

import json
from typing import Dict, Any, Iterable

from caos_core.plane_b import PlaneB


class Amendments:
    """
    Append-only correction layer.

    This class records corrective amendments while preserving
    full, auditable lineage.
    """

    def __init__(self, plane_b: PlaneB):
        self._pb = plane_b

    # ------------------------------------------------------------------
    # Apply amendment
    # ------------------------------------------------------------------

    def apply(
        self,
        amendment_id: str,
        supersedes: str,
        payload: Dict[str, Any],
        anchors: Iterable[str],
    ) -> None:
        """
        Apply a corrective amendment.

        The superseded record is never modified or deleted.
        """
        ts = self._pb._now_ms()

        payload_blob = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        anchors_blob = json.dumps(list(anchors), separators=(",", ":"), sort_keys=True)

        cur = self._pb._conn.cursor()
        try:
            cur.execute("BEGIN;")

            cur.execute(
                """
                INSERT INTO amendments (
                    amendment_id,
                    supersedes,
                    payload,
                    anchors,
                    ts_ms
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (amendment_id, supersedes, payload_blob, anchors_blob, ts),
            )

            # Update latest_valid to point to the amendment
            cur.execute(
                """
                INSERT OR REPLACE INTO latest_valid (logical_id, record_id)
                VALUES (?, ?)
                """,
                (supersedes, amendment_id),
            )

            cur.execute("COMMIT;")
        except Exception:
            cur.execute("ROLLBACK;")
            raise
        finally:
            cur.close()
