"""
CAOS-A1 — Audit Exporter

ROLE
----
Non-authoritative audit / observability export.

This module exports immutable records from Plane B into
append-only JSONL files for inspection, backup, or compliance.

INVARIANTS
----------
- Read-only with respect to Plane B
- Append-only exports
- Export failure must not affect Plane B
- JSONL format
- Deterministic ordering
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from caos_core.plane_b import PlaneB


class Exporter:
    """
    Append-only audit exporter.
    """

    def __init__(self, plane_b: PlaneB, root: Path):
        self._pb = plane_b
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)
        self._path = self._root / "records.jsonl"

    def export_all(self) -> None:
        """
        Export all Plane B records in deterministic order.

        Best-effort only: failures are swallowed.
        """
        try:
            with self._path.open("a", encoding="utf-8") as f:
                for record in self._pb.iter_records():
                    out = {
                        "record_id": record["record_id"],
                        "payload": record["payload"],
                        "anchors": list(record["anchors"]),
                        "ts_ms": record["ts_ms"],
                        "exported_ts_ms": int(time.time() * 1000),
                    }
                    f.write(json.dumps(out, separators=(",", ":"), sort_keys=True))
                    f.write("\n")
        except Exception:
            # Export must never affect truth
            return
