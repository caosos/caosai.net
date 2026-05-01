"""Receipt schemas for CAOS actions."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field

ActorType = Literal["user", "assistant", "system", "admin", "worker", "connector"]
ReceiptStatus = Literal["ok", "blocked", "failed", "degraded", "pending"]


def new_receipt_id() -> str:
    return f"rcpt_{uuid4().hex}"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class ApprovalState(BaseModel):
    required: bool = False
    present: bool = False
    reason: str | None = None


class ActionReceipt(BaseModel):
    receipt_id: str = Field(default_factory=new_receipt_id)
    event_type: str
    actor_type: ActorType
    actor_id: str | None = None
    reason: str
    status: ReceiptStatus = "ok"
    created_at: str = Field(default_factory=utc_now_iso)
    summary: str
    metrics: dict[str, Any] = Field(default_factory=dict)
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    changes: list[dict[str, Any]] = Field(default_factory=list)
    memory_refs: list[str] = Field(default_factory=list)
    context_refs: list[str] = Field(default_factory=list)
    model_ref: dict[str, Any] | None = None
    approval: ApprovalState = Field(default_factory=ApprovalState)
    error: dict[str, Any] | None = None
