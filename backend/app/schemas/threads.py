"""Thread and message persistence schemas."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def new_thread_id() -> str:
    return f"thread_{uuid4().hex}"


def new_message_id() -> str:
    return f"msg_{uuid4().hex}"


class MessageRecord(BaseModel):
    message_id: str = Field(default_factory=new_message_id)
    thread_id: str
    user_id: str
    role: str
    content: str
    provider: str | None = None
    model: str | None = None
    token_count: int = 0
    latency_ms: int | None = None
    created_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)


class ThreadRecord(BaseModel):
    thread_id: str = Field(default_factory=new_thread_id)
    user_id: str
    title: str = ""
    message_count: int = 0
    total_tokens: int = 0
    last_provider: str | None = None
    last_model: str | None = None
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    metadata: dict[str, Any] = Field(default_factory=dict)


class ThreadListRequest(BaseModel):
    user_id: str
    limit: int = Field(default=50, ge=1, le=200)


class ThreadCreateRequest(BaseModel):
    user_id: str
    title: str = ""
