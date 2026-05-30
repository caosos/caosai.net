"""Agent playground v0 job packet schemas (read-only, non-executing)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, Field

from app.schemas.receipts import ActionReceipt

AgentJobStatus = Literal["pending", "planned", "blocked", "completed", "failed"]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_job_id() -> str:
    return f"job_{uuid4().hex}"


class AgentToolScope(BaseModel):
    allowed_tools: list[str] = Field(default_factory=list)
    forbidden_tools: list[str] = Field(default_factory=list)


class AgentLimits(BaseModel):
    max_runtime_seconds: int = 600
    max_tool_calls: int = 10
    max_tokens: int = 4000
    max_spawned_agents: int = 0


class AgentJobPacket(BaseModel):
    job_id: str = Field(default_factory=new_job_id)
    project_id: str
    agent_role: str
    task_summary: str
    read_scope: list[str] = Field(default_factory=list)
    write_scope: list[str] = Field(default_factory=list)
    network_scope: list[str] = Field(default_factory=list)
    connector_scope: list[str] = Field(default_factory=list)
    memory_bins_available: list[str] = Field(default_factory=list)
    secret_access_allowed: bool = False
    tools: AgentToolScope = Field(default_factory=AgentToolScope)
    limits: AgentLimits = Field(default_factory=AgentLimits)
    approval_required_for: list[str] = Field(default_factory=list)
    stop_conditions: list[str] = Field(default_factory=list)
    status: AgentJobStatus = "pending"
    created_at: str = Field(default_factory=utc_now_iso)
    updated_at: str = Field(default_factory=utc_now_iso)


class AgentJobCreateRequest(BaseModel):
    project_id: str
    agent_role: str
    task_summary: str
    read_scope: list[str] = Field(default_factory=list)
    write_scope: list[str] = Field(default_factory=list)
    network_scope: list[str] = Field(default_factory=list)
    connector_scope: list[str] = Field(default_factory=list)
    memory_bins_available: list[str] = Field(default_factory=list)
    secret_access_allowed: bool = False
    tools: AgentToolScope = Field(default_factory=AgentToolScope)
    limits: AgentLimits = Field(default_factory=AgentLimits)
    approval_required_for: list[str] = Field(default_factory=list)
    stop_conditions: list[str] = Field(default_factory=list)
    status: AgentJobStatus = "pending"


class AgentJobResponse(BaseModel):
    job: AgentJobPacket | None = None
    jobs: list[AgentJobPacket] = Field(default_factory=list)
    receipt: ActionReceipt
