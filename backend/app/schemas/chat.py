"""Chat contract schemas for the portable CAOS backend."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(description="Message role: user, assistant, system, or tool.")
    content: str


class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None
    session_id: str | None = None
    user_id: str | None = None
    provider: str | None = None
    model: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    thread_id: str
    assistant_message: ChatMessage
    provider: str
    model: str
    receipt: dict[str, Any]
