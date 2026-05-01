"""Memory contract schemas for CAOS.

Memory is a governed product surface, not an incidental prompt fragment.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field

MemoryCategory = Literal[
    "identity",
    "projects",
    "governance",
    "preferences",
    "relationship",
    "domains",
    "tech_state",
    "behavioral",
    "traits",
    "learning",
    "real_world",
    "risk",
    "counter",
    "unclassified",
]

MemorySourceType = Literal[
    "explicit_user_statement",
    "conversation_inference",
    "system_event",
    "imported_legacy",
    "admin_entry",
]

MemoryStatus = Literal["active", "pending_confirmation", "forgotten", "superseded"]


def new_memory_id() -> str:
    return f"mem_{uuid4().hex}"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class MemoryEvidence(BaseModel):
    source_type: MemorySourceType
    source_ref: str | None = None
    quote: str | None = None
    captured_at: str = Field(default_factory=utc_now_iso)


class MemoryAtom(BaseModel):
    memory_id: str = Field(default_factory=new_memory_id)
    user_id: str
    category: MemoryCategory
    content: str
    status: MemoryStatus = "active"
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    priority: int = Field(default=3, ge=1, le=5)
    evidence: list[MemoryEvidence] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=utc_now_iso)
    updated_at: str = Field(default_factory=utc_now_iso)


class MemoryCreateRequest(BaseModel):
    user_id: str
    category: MemoryCategory = "unclassified"
    content: str
    source_type: MemorySourceType = "explicit_user_statement"
    source_ref: str | None = None
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    priority: int = Field(default=3, ge=1, le=5)
    metadata: dict[str, Any] = Field(default_factory=dict)


class MemoryListRequest(BaseModel):
    user_id: str
    category: MemoryCategory | None = None
    include_forgotten: bool = False
    limit: int = Field(default=50, ge=1, le=500)
