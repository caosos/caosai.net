"""
CAOS-A1 — Anchor Maps (Derived Index)

ROLE
----
Derived, non-authoritative anchor index for recall acceleration.

INVARIANTS
----------
- Plane B is authoritative
- Index is disposable and rebuildable
- Best-effort writes only
- Fail-closed reads
- Exact-string anchors only
"""

from __future__ import annotations

import sqlite3
import time
import json
from pathlib import Path
from typing import Iterable, List, Dict, Any, Set


class AnchorMaps:
    """
    Derived anchor index.

    This index exists solely to accelerate recall candidate discovery.
    """

    def __init__(self, root: Path):
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)
        self._db_path = self._root / "anchor_index.sqlite3"

        self._conn = sqlite3.connect(
            self._db_path,
            isolation_level=None,
            check_same_thread=False,
        )

        self._configure()
        self._schema()

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def _configure(self) -> None:
        cur = self._conn.cursor()
        cur.execute("PRAGMA journal_mode=WAL;")
        cur.execute("PRAGMA synchronous=NORMAL;")
        cur.execute("PRAGMA temp_store=MEMORY;")
        cur.close()

    # ------------------------------------------------------------------
    # Schema
    # ------------------------------------------------------------------

    def _schema(self) -> None:
        cur = self._conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS anchor_postings (
                anchor    TEXT NOT NULL,
                record_id TEXT NOT NULL,
                ts_ms     INTEGER NOT NULL,
                PRIMARY KEY (anchor, record_id)
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS record_anchors (
                record_id TEXT NOT NULL,
                anchor    TEXT NOT NULL,
                ts_ms     INTEGER NOT NULL,
                PRIMARY KEY (record_id, anchor)
            )
            """
        )

        cur.close()

    # ------------------------------------------------------------------
    # Write-side (best-effort)
    # ------------------------------------------------------------------

    def index_record_best_effort(
        self,
        record_id: str,
        anchors: Iterable[str],
    ) -> None:
        ts = int(time.time() * 1000)
        anchors_set: Set[str] = set(a.strip() for a in anchors if a.strip())

        cur = self._conn.cursor()
        try:
            cur.execute("BEGIN;")

            cur.execute(
                "DELETE FROM record_anchors WHERE record_id = ?",
                (record_id,),
            )

            for a in anchors_set:
                cur.execute(
                    """
                    INSERT OR REPLACE INTO record_anchors
                    (record_id, anchor, ts_ms)
                    VALUES (?, ?, ?)
                    """,
                    (record_id, a, ts),
                )
                cur.execute(
                    """
                    INSERT OR REPLACE INTO anchor_postings
                    (anchor, record_id, ts_ms)
                    VALUES (?, ?, ?)
                    """,
                    (a, record_id, ts),
                )

            cur.execute("COMMIT;")
        except Exception:
            cur.execute("ROLLBACK;")
        finally:
            cur.close()

    def remove_record_best_effort(self, record_id: str) -> None:
        cur = self._conn.cursor()
        try:
            cur.execute("BEGIN;")
            cur.execute(
                "DELETE FROM record_anchors WHERE record_id = ?",
                (record_id,),
            )
            cur.execute(
                "DELETE FROM anchor_postings WHERE record_id = ?",
                (record_id,),
            )
            cur.execute("COMMIT;")
        except Exception:
            cur.execute("ROLLBACK;")
        finally:
            cur.close()

    # ------------------------------------------------------------------
    # Read-side (index-only)
    # ------------------------------------------------------------------

    def query_any(self, anchors: Iterable[str], limit: int) -> List[str]:
        try:
            cur = self._conn.cursor()
            q = """
                SELECT DISTINCT record_id
                FROM anchor_postings
                WHERE anchor IN ({})
                LIMIT ?
            """.format(
                ",".join("?" for _ in anchors)
            )
            rows = cur.execute(q, [*anchors, limit]).fetchall()
            cur.close()
            return [r[0] for r in rows]
        except Exception:
            return []

    def query_all(self, anchors: Iterable[str], limit: int) -> List[str]:
        try:
            cur = self._conn.cursor()
            rows = cur.execute(
                """
                SELECT record_id
                FROM anchor_postings
                WHERE anchor IN ({})
                GROUP BY record_id
                HAVING COUNT(DISTINCT anchor) = ?
                LIMIT ?
                """.format(
                    ",".join("?" for _ in anchors)
                ),
                [*anchors, len(list(anchors)), limit],
            ).fetchall()
            cur.close()
            return [r[0] for r in rows]
        except Exception:
            return []
