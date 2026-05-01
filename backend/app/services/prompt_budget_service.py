"""Prompt budget service.

WCW is the outer budget. ARC must fit inside that budget with receipts showing
what was included and excluded.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PromptBudgetResult:
    budget_chars: int
    used_chars: int
    remaining_chars: int
    included_labels: list[str] = field(default_factory=list)
    excluded_labels: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "budget_chars": self.budget_chars,
            "used_chars": self.used_chars,
            "remaining_chars": self.remaining_chars,
            "included_labels": self.included_labels,
            "excluded_labels": self.excluded_labels,
        }


class PromptBudgetService:
    def fit(self, *, parts: list[tuple[str, str]], budget_chars: int = 24000) -> PromptBudgetResult:
        used = 0
        included: list[str] = []
        excluded: list[str] = []

        for label, content in parts:
            size = len(content or "")
            if used + size <= budget_chars:
                used += size
                included.append(label)
            else:
                excluded.append(label)

        return PromptBudgetResult(
            budget_chars=budget_chars,
            used_chars=used,
            remaining_chars=max(budget_chars - used, 0),
            included_labels=included,
            excluded_labels=excluded,
        )


prompt_budget_service = PromptBudgetService()
