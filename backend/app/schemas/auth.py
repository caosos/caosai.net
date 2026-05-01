"""Authentication/session schemas."""

from __future__ import annotations

from pydantic import BaseModel, Field


class DevLoginRequest(BaseModel):
    requested_name: str | None = Field(default=None)


class SessionUser(BaseModel):
    user_id: str
    display_name: str
    role: str
    is_admin: bool


class DevLoginResponse(BaseModel):
    session_id: str
    user: SessionUser
    token: str
    auth_mode: str = "development"
