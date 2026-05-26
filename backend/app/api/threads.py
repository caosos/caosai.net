"""Thread persistence routes."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.schemas.threads import ThreadListRequest, ThreadCreateRequest
from app.services.thread_service import thread_service

router = APIRouter(prefix="/threads", tags=["threads"])


@router.post("/list", response_model=ApiEnvelope)
def list_threads(request: ThreadListRequest) -> ApiEnvelope:
    threads = thread_service.list_threads(request)
    return ApiEnvelope(
        ok=True,
        data={"threads": [t.model_dump(mode="json") for t in threads], "count": len(threads)},
        diagnostic_receipt=DiagnosticReceipt(status="ok", phase="threads", detail="Thread list returned."),
    )


@router.get("/{thread_id}/messages", response_model=ApiEnvelope)
def get_thread_messages(thread_id: str, user_id: str = "dev_user") -> ApiEnvelope:
    messages = thread_service.get_thread_messages(thread_id)
    return ApiEnvelope(
        ok=True,
        data={"messages": [m.model_dump(mode="json") for m in messages], "count": len(messages)},
        diagnostic_receipt=DiagnosticReceipt(status="ok", phase="threads", detail="Thread messages returned."),
    )
