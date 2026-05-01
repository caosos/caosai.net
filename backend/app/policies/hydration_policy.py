"""Hydration policy for CAOS.

Hydration decides what should be loaded into ARC. Capability awareness is
lightweight by default; full tool/context hydration happens only when relevant.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class HydrationDecision:
    load_memory: bool = False
    load_thread_history: bool = False
    load_summaries: bool = False
    load_connectors: bool = False
    load_admin_context: bool = False
    capability_hints: list[str] = field(default_factory=list)
    reason: str = "default minimal hydration"

    def to_dict(self) -> dict[str, object]:
        return {
            "load_memory": self.load_memory,
            "load_thread_history": self.load_thread_history,
            "load_summaries": self.load_summaries,
            "load_connectors": self.load_connectors,
            "load_admin_context": self.load_admin_context,
            "capability_hints": self.capability_hints,
            "reason": self.reason,
        }


class HydrationPolicy:
    def decide(self, *, message: str, is_admin: bool = False) -> HydrationDecision:
        lower = message.lower()
        hints: list[str] = []

        wants_memory = any(term in lower for term in ("remember", "memory", "preference", "what do you know"))
        wants_files = any(term in lower for term in ("file", "photo", "image", "artifact", "upload"))
        wants_connectors = any(term in lower for term in ("email", "gmail", "drive", "calendar", "github", "slack", "mcp"))
        wants_admin = any(term in lower for term in ("admin", "diagnostic", "ticket", "dashboard", "receipt"))
        wants_history = any(term in lower for term in ("earlier", "previous", "thread", "summary", "recap"))

        if wants_files:
            hints.append("artifact/file surfaces available when relevant")
        if wants_connectors:
            hints.append("connector tools available when explicitly relevant")
        if wants_admin and is_admin:
            hints.append("admin diagnostics available for admin context")

        return HydrationDecision(
            load_memory=wants_memory or wants_history,
            load_thread_history=wants_history,
            load_summaries=wants_history,
            load_connectors=wants_connectors,
            load_admin_context=wants_admin and is_admin,
            capability_hints=hints,
            reason="selective hydration based on message intent",
        )


hydration_policy = HydrationPolicy()
