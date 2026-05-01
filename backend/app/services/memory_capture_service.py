"""Memory capture service.

This service identifies candidate memory atoms. It does not decide long-term
truth alone and does not silently persist durable memory without the caller's
policy path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from app.schemas.memory import MemoryCategory, MemoryCreateRequest


@dataclass(frozen=True)
class MemoryCandidate:
    category: MemoryCategory
    content: str
    confidence: float
    priority: int
    reason: str


PROJECT_TERMS = ("caos", "aria", "linode", "rebuild", "repo", "migration")
GOVERNANCE_TERMS = ("must", "never", "non-negotiable", "contract", "rule", "policy")
PREFERENCE_TERMS = ("i prefer", "i want", "i don't want", "i need", "remember")


class MemoryCaptureService:
    def extract_candidates(self, *, user_id: str, text: str, source_ref: str | None = None) -> list[MemoryCreateRequest]:
        normalized = " ".join(text.strip().split())
        if not normalized:
            return []

        candidates = self._classify(normalized)
        requests: list[MemoryCreateRequest] = []

        for candidate in candidates:
            requests.append(
                MemoryCreateRequest(
                    user_id=user_id,
                    category=candidate.category,
                    content=candidate.content,
                    source_type="conversation_inference",
                    source_ref=source_ref,
                    confidence=candidate.confidence,
                    priority=candidate.priority,
                    metadata={"capture_reason": candidate.reason},
                )
            )

        return requests

    def _classify(self, text: str) -> Iterable[MemoryCandidate]:
        lower = text.lower()

        if any(term in lower for term in PREFERENCE_TERMS):
            yield MemoryCandidate(
                category="preferences",
                content=text,
                confidence=0.72,
                priority=4,
                reason="preference language detected",
            )

        if any(term in lower for term in GOVERNANCE_TERMS):
            yield MemoryCandidate(
                category="governance",
                content=text,
                confidence=0.68,
                priority=4,
                reason="governance language detected",
            )

        if any(term in lower for term in PROJECT_TERMS):
            yield MemoryCandidate(
                category="projects",
                content=text,
                confidence=0.64,
                priority=3,
                reason="project language detected",
            )


memory_capture_service = MemoryCaptureService()
