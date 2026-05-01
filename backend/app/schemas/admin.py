"""Admin contract schemas."""

from __future__ import annotations

from pydantic import BaseModel


class AdminProbeRequest(BaseModel):
    user_id: str | None = None
    is_admin: bool = False


class AdminProbeResponse(BaseModel):
    user_id: str | None
    admin_access: bool
    enforced_by: str
