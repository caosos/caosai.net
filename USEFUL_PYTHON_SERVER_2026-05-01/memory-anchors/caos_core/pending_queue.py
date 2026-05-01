"""
CAOS-A1 — Pending Resolution Queue

ROLE
----
Human-in-the-loop ambiguity queue.

This module records unresolved decisions that block execution
until explicit human resolution is provided.

INVARIANTS
----------
- Append-only
- Non-authoritative
- No inference
- No automatic resolution
- JSONL storage
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict, Any


class PendingResolutionQueue:
    """
    Append-only ambiguity queue.
    """

    def __init__(self, root: Path):
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)
        self._path = self._root / "pending.jsonl"

    def add(
        self,
        pending_id: str,
        reason: str,
        raw_input: str,
        context: Dict[str, Any],
    ) -> None:
        """
        Record a pending ambiguity requiring human resolution.
        """
        record = {
            "pending_id": pending_id,
            "reason": reason,
            "raw_input": raw_input,
            "context": context,
            "ts_ms": int(time.time() * 1000),
        }

        with self._path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, separators=(",", ":"), sort_keys=True))
            f.write("\n")
