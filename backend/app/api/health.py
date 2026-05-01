"""Health and runtime inspection routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import load_settings
from app.core.runtime_registry import build_runtime_registry
from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.services.receipt_service import action_receipt

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=ApiEnvelope)
def health() -> ApiEnvelope:
    settings = load_settings()
    registry = build_runtime_registry(settings)
    runtime_data = registry.to_dict()
    receipt = action_receipt(
        event_type="health_checked",
        actor_type="system",
        reason="client requested backend health state",
        summary="CAOS backend skeleton is reachable.",
        outputs={"runtime": runtime_data},
        metrics={"healthy": True},
    )

    return ApiEnvelope(
        ok=True,
        data={"runtime": runtime_data, "receipt": receipt.model_dump()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="foundation",
            detail="CAOS backend skeleton is reachable with receipt.",
        ),
    )
