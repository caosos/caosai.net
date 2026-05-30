"""Chat routes for the portable CAOS rebuild."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.schemas.common import ApiEnvelope
from app.services.chat_orchestrator import ChatOrchestrator
from app.services.receipt_service import action_receipt, chat_receipt

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/turn", response_model=ApiEnvelope)
def chat_turn(request: ChatRequest) -> ApiEnvelope:
    orchestrator = ChatOrchestrator()
    response = orchestrator.handle_turn(request)
    orch_receipt = response.receipt or {}
    provider_called = orch_receipt.get("provider_called", False)
    phase = orch_receipt.get("phase", "unknown")
    receipt = action_receipt(
        event_type="chat_turn_completed",
        actor_type="user",
        actor_id=request.user_id,
        reason="user submitted a chat turn",
        summary=f"Chat turn completed via {phase}. Provider called: {provider_called}.",
        inputs={
            "thread_id": request.thread_id,
            "session_id": request.session_id,
            "provider": request.provider,
            "model": request.model,
            "message_chars": len(request.message),
        },
        outputs={
            "thread_id": response.thread_id,
            "assistant_message_chars": len(response.assistant_message.content),
            "provider_called": provider_called,
            "latency_ms": orch_receipt.get("latency_ms"),
            "user_tokens": orch_receipt.get("user_tokens"),
            "assistant_tokens": orch_receipt.get("assistant_tokens"),
            "thread_total_tokens": orch_receipt.get("thread_total_tokens"),
            "memory_mutated": orch_receipt.get("memory_mutated", False),
            "tools_executed": orch_receipt.get("tools_executed", False),
            "persistence_written": provider_called,
            "error": orch_receipt.get("error"),
        },
        changes=[],
        model_ref={"provider": response.provider, "model": response.model},
    )

    return ApiEnvelope(
        ok=True,
        data={**response.model_dump(), "receipt": receipt.model_dump()},
        diagnostic_receipt=chat_receipt(
            f"Chat turn handled by orchestrator. Phase: {phase}. Provider called: {provider_called}."
        ),
    )
