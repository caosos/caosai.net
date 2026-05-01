"""Development-only authentication adapter.

This module exists to make the rebuild testable before production OAuth is
selected. It must never be treated as production security.
"""

from __future__ import annotations

from uuid import uuid4

from app.schemas.auth import DevLoginRequest, DevLoginResponse, SessionUser
from .config import Settings


class DevAuthDisabledError(Exception):
    """Raised when development auth is requested while disabled."""


def create_dev_session(settings: Settings, request: DevLoginRequest) -> DevLoginResponse:
    if not settings.dev_auth_enabled:
        raise DevAuthDisabledError("development auth is disabled")

    display_name = (request.requested_name or "Michael").strip() or "Michael"

    return DevLoginResponse(
        session_id=f"dev-session-{uuid4().hex}",
        token=f"dev-token-{uuid4().hex}",
        user=SessionUser(
            user_id="local-michael-admin",
            display_name=display_name,
            role="admin",
            is_admin=True,
        ),
    )
