"""Memory relevance service.

Selects candidate memory atoms for ARC. This is not keyword-only recall; the
initial implementation is intentionally conservative until embeddings/ranking
are wired.
"""

from __future__ import annotations

from app.schemas.memory import MemoryAtom


class MemoryRelevanceService:
    def select_for_arc(self, *, query: str, atoms: list[MemoryAtom], limit: int = 8) -> list[MemoryAtom]:
        query_terms = {term for term in query.lower().split() if len(term) > 3}

        scored: list[tuple[float, MemoryAtom]] = []
        for atom in atoms:
            content_terms = set(atom.content.lower().split())
            overlap = len(query_terms & content_terms)
            score = atom.priority + atom.confidence + overlap
            scored.append((score, atom))

        scored.sort(key=lambda item: (item[0], item[1].updated_at), reverse=True)
        return [atom for _, atom in scored[:limit]]


memory_relevance_service = MemoryRelevanceService()
