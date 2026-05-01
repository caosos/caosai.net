"""Authentication routes for the portable CAOS rebuild."""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import load_settings
from app.core.dev_auth import DevAuthDisabledError, create_dev_session
from app.schemas.auth import DevLoginRequest
from app.schemas.common import ApiEnvelope, DiagnosticReceipt

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/dev-login", response_model=ApiEnvelope)
def dev_login(request: DevLoginRequest) -> ApiEnvelope:
    settings = load_settings()

    try:
        session = create_dev_session(settings, request)
    except DevAuthDisabledError as exc:
        return ApiEnvelope(
            ok=False,
            error_code="DEV_AUTH_DISABLED",
            message=str(exc),
            diagnostic_receipt=DiagnosticReceipt(
                status="blocked",
                phase="foundation",
                detail="Development auth route is disabled by configuration.",
            ),
        )

    return ApiEnvelope(
        ok=True,
        data=session.model_dump(),
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="foundation",
            detail="Development admin session issued.",
        ),
    )
