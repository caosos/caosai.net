"""Active Relevant Context assembler.

ARC is selected context inside the Working Context Window. This module decides
what is assembled, not how the model speaks.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.schemas.memory import MemoryAtom


@dataclass(frozen=True)
class ArcPacket:
    query: str
    memories: list[MemoryAtom] = field(default_factory=list)
    summaries: list[dict[str, Any]] = field(default_factory=list)
    capability_hints: list[str] = field(default_factory=list)

    def to_prompt_parts(self) -> list[str]:
        parts: list[str] = []

        if self.memories:
            parts.append("Relevant memory:")
            for atom in self.memories:
                parts.append(f"- [{atom.category}] {atom.content}")

        if self.summaries:
            parts.append("Relevant summaries:")
            for summary in self.summaries:
                title = summary.get("title", "summary")
                content = summary.get("content", "")
                parts.append(f"- {title}: {content}")

        if self.capability_hints:
            parts.append("Available relevant capabilities:")
            for hint in self.capability_hints:
                parts.append(f"- {hint}")

        return parts


class ArcAssembler:
    def assemble(
        self,
        *,
        query: str,
        memories: list[MemoryAtom] | None = None,
        summaries: list[dict[str, Any]] | None = None,
        capability_hints: list[str] | None = None,
    ) -> ArcPacket:
        return ArcPacket(
            query=query,
            memories=memories or [],
            summaries=summaries or [],
            capability_hints=capability_hints or [],
        )


arc_assembler = ArcAssembler()
