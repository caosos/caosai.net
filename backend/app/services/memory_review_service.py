"""Memory review service.

User-governed memory controls live here: confirm, reclassify, forget, and
supersede. Persistence will be wired behind this boundary later.
"""

from __future__ import annotations

from app.schemas.memory import MemoryAtom, MemoryCategory, utc_now_iso


class MemoryNotFoundError(Exception):
    """Raised when a requested memory atom does not exist."""


class MemoryReviewService:
    def confirm(self, atom: MemoryAtom) -> MemoryAtom:
        atom.status = "active"
        atom.updated_at = utc_now_iso()
        atom.metadata["review_action"] = "confirmed"
        return atom

    def reclassify(self, atom: MemoryAtom, category: MemoryCategory) -> MemoryAtom:
        atom.category = category
        atom.updated_at = utc_now_iso()
        atom.metadata["review_action"] = "reclassified"
        return atom

    def forget(self, atom: MemoryAtom) -> MemoryAtom:
        atom.status = "forgotten"
        atom.updated_at = utc_now_iso()
        atom.metadata["review_action"] = "forgotten"
        return atom


memory_review_service = MemoryReviewService()
