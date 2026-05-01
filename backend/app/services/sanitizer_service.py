"""Context sanitizer service.

Sanitization bounds context before it enters ARC. It must preserve meaning and
truth; it must not smooth uncertainty or invent missing details.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SanitizedText:
    text: str
    original_chars: int
    sanitized_chars: int
    truncated: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "original_chars": self.original_chars,
            "sanitized_chars": self.sanitized_chars,
            "truncated": self.truncated,
        }


class SanitizerService:
    def sanitize_text(self, text: str, *, max_chars: int = 8000) -> SanitizedText:
        original = text or ""
        normalized = " ".join(original.split())
        truncated = len(normalized) > max_chars

        if truncated:
            normalized = normalized[: max_chars - 24].rstrip() + " …[TRUNCATED]"

        return SanitizedText(
            text=normalized,
            original_chars=len(original),
            sanitized_chars=len(normalized),
            truncated=truncated,
        )


sanitizer_service = SanitizerService()
