"""Health and runtime inspection routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import load_settings
from app.core.runtime_registry import build_runtime_registry
from app.schemas.common import ApiEnvelope, DiagnosticReceipt

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=ApiEnvelope)
def health() -> ApiEnvelope:
    settings = load_settings()
    registry = build_runtime_registry(settings)

    return ApiEnvelope(
        ok=True,
        data={"runtime": registry.to_dict()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="foundation",
            detail="CAOS backend skeleton is reachable.",
        ),
    )
