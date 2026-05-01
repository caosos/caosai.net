"""Receipt helpers for CAOS backend operations."""

from __future__ import annotations

from app.schemas.common import DiagnosticReceipt


def foundation_receipt(detail: str, *, status: str = "ok") -> DiagnosticReceipt:
    return DiagnosticReceipt(
        status=status,
        phase="foundation",
        detail=detail,
    )


def chat_receipt(detail: str, *, status: str = "ok") -> DiagnosticReceipt:
    return DiagnosticReceipt(
        status=status,
        phase="chat-contract",
        detail=detail,
    )
