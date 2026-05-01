"""Chat routes for the portable CAOS rebuild."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.schemas.common import ApiEnvelope
from app.services.chat_orchestrator import ChatOrchestrator
from app.services.receipt_service import chat_receipt

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/turn", response_model=ApiEnvelope)
def chat_turn(request: ChatRequest) -> ApiEnvelope:
    orchestrator = ChatOrchestrator()
    response = orchestrator.handle_turn(request)

    return ApiEnvelope(
        ok=True,
        data=response.model_dump(),
        diagnostic_receipt=chat_receipt(
            "Minimal chat contract responded without provider, memory, tools, or persistence."
        ),
    )
