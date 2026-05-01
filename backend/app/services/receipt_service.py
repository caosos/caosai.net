"""Receipt helpers for CAOS backend operations."""

from __future__ import annotations

from typing import Any

from app.schemas.common import DiagnosticReceipt
from app.schemas.receipts import ActionReceipt, ActorType, ApprovalState, ReceiptStatus


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


def action_receipt(
    *,
    event_type: str,
    actor_type: ActorType,
    reason: str,
    summary: str,
    actor_id: str | None = None,
    status: ReceiptStatus = "ok",
    metrics: dict[str, Any] | None = None,
    inputs: dict[str, Any] | None = None,
    outputs: dict[str, Any] | None = None,
    changes: list[dict[str, Any]] | None = None,
    memory_refs: list[str] | None = None,
    context_refs: list[str] | None = None,
    model_ref: dict[str, Any] | None = None,
    approval_required: bool = False,
    approval_present: bool = False,
    approval_reason: str | None = None,
    error: dict[str, Any] | None = None,
) -> ActionReceipt:
    return ActionReceipt(
        event_type=event_type,
        actor_type=actor_type,
        actor_id=actor_id,
        reason=reason,
        status=status,
        summary=summary,
        metrics=metrics or {},
        inputs=inputs or {},
        outputs=outputs or {},
        changes=changes or [],
        memory_refs=memory_refs or [],
        context_refs=context_refs or [],
        model_ref=model_ref,
        approval=ApprovalState(
            required=approval_required,
            present=approval_present,
            reason=approval_reason,
        ),
        error=error,
    )
