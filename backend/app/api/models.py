"""Model catalog and WCW routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.schemas.models import ModelSelectionRequest
from app.services.model_selection_service import model_selection_service
from app.services.receipt_service import action_receipt

router = APIRouter(prefix="/models", tags=["models"])


@router.get("", response_model=ApiEnvelope)
def list_models() -> ApiEnvelope:
    selection = model_selection_service.select()
    receipt = action_receipt(
        event_type="model_catalog_listed",
        actor_type="system",
        reason="frontend or client requested model/WCW catalog",
        summary="Returned model catalog with engine-specific WCW metadata.",
        outputs={"model_count": len(selection.available_models)},
        model_ref=selection.active_model.model_dump(),
    )

    return ApiEnvelope(
        ok=True,
        data={**selection.model_dump(), "receipt": receipt.model_dump()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="model-selection",
            detail="Model catalog returned with WCW metadata and receipt.",
        ),
    )


@router.post("/select", response_model=ApiEnvelope)
def select_model(request: ModelSelectionRequest) -> ApiEnvelope:
    selection = model_selection_service.select(request)
    matched = (
        selection.active_model.provider == request.provider
        and selection.active_model.model == request.model
    )
    receipt = action_receipt(
        event_type="model_selected",
        actor_type="user",
        reason="user or client selected inference engine",
        summary="Resolved active model and usable WCW metadata.",
        status="ok" if matched else "degraded",
        inputs=request.model_dump(),
        outputs={"matched_requested_model": matched},
        changes=[
            {
                "field": "active_model",
                "provider": selection.active_model.provider,
                "model": selection.active_model.model,
                "usable_context_tokens": selection.active_model.usable_context_tokens,
            }
        ],
        model_ref=selection.active_model.model_dump(),
    )

    return ApiEnvelope(
        ok=True,
        data={**selection.model_dump(), "receipt": receipt.model_dump()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="model-selection",
            detail="Model selection resolved with active WCW metadata and receipt.",
        ),
    )
