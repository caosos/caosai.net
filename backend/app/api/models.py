"""Model catalog and WCW routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.schemas.models import ModelSelectionRequest
from app.services.model_selection_service import model_selection_service

router = APIRouter(prefix="/models", tags=["models"])


@router.get("", response_model=ApiEnvelope)
def list_models() -> ApiEnvelope:
    selection = model_selection_service.select()
    return ApiEnvelope(
        ok=True,
        data=selection.model_dump(),
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="model-selection",
            detail="Model catalog returned with WCW metadata.",
        ),
    )


@router.post("/select", response_model=ApiEnvelope)
def select_model(request: ModelSelectionRequest) -> ApiEnvelope:
    selection = model_selection_service.select(request)
    return ApiEnvelope(
        ok=True,
        data=selection.model_dump(),
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="model-selection",
            detail="Model selection resolved with active WCW metadata.",
        ),
    )
