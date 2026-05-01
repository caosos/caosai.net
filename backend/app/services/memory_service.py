"""Memory service boundary.

Phase 1/2 implementation keeps an in-process store so contracts can be tested
before Mongo persistence is wired. This is not final production storage.
"""

from __future__ import annotations

from app.schemas.memory import MemoryAtom, MemoryCreateRequest, MemoryEvidence, MemoryListRequest


class MemoryService:
    def __init__(self) -> None:
        self._atoms: dict[str, MemoryAtom] = {}

    def create_atom(self, request: MemoryCreateRequest) -> MemoryAtom:
        atom = MemoryAtom(
            user_id=request.user_id,
            category=request.category,
            content=request.content,
            confidence=request.confidence,
            priority=request.priority,
            metadata=request.metadata,
            evidence=[
                MemoryEvidence(
                    source_type=request.source_type,
                    source_ref=request.source_ref,
                    quote=request.content,
                )
            ],
        )
        self._atoms[atom.memory_id] = atom
        return atom

    def list_atoms(self, request: MemoryListRequest) -> list[MemoryAtom]:
        atoms = [
            atom for atom in self._atoms.values()
            if atom.user_id == request.user_id
        ]

        if request.category is not None:
            atoms = [atom for atom in atoms if atom.category == request.category]

        if not request.include_forgotten:
            atoms = [atom for atom in atoms if atom.status != "forgotten"]

        atoms.sort(key=lambda atom: (atom.priority, atom.created_at), reverse=True)
        return atoms[: request.limit]


memory_service = MemoryService()
