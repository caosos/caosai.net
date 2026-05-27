"""Agent playground v0 routes (read-only representation, no execution)."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.agent_jobs import AgentJobCreateRequest
from app.schemas.common import ApiEnvelope
from app.services.agent_job_service import create_job, get_job, list_jobs
from app.services.receipt_service import foundation_receipt

router = APIRouter(tags=["agent-jobs"])


@router.post("/agent-jobs", response_model=ApiEnvelope)
def create_agent_job(payload: AgentJobCreateRequest) -> ApiEnvelope:
    result = create_job(payload)
    return ApiEnvelope(
        ok=True,
        data={"job": result.job.model_dump() if result.job else None, "receipt": result.receipt.model_dump()},
        diagnostic_receipt=foundation_receipt(
            "Agent Playground v0 packet created. Read-only representation only; no autonomous execution."
        ),
    )


@router.get("/agent-jobs", response_model=ApiEnvelope)
def list_agent_jobs() -> ApiEnvelope:
    result = list_jobs()
    return ApiEnvelope(
        ok=True,
        data={"jobs": [job.model_dump() for job in result.jobs], "receipt": result.receipt.model_dump()},
        diagnostic_receipt=foundation_receipt(
            "Agent Playground v0 packets listed. Read-only representation only; no autonomous execution."
        ),
    )


@router.get("/agent-jobs/{job_id}", response_model=ApiEnvelope)
def get_agent_job(job_id: str) -> ApiEnvelope:
    result = get_job(job_id)
    return ApiEnvelope(
        ok=result.job is not None,
        data={"job": result.job.model_dump() if result.job else None, "receipt": result.receipt.model_dump()},
        error_code=None if result.job else "agent_job_not_found",
        message=None if result.job else "Agent job not found.",
        diagnostic_receipt=foundation_receipt(
            "Agent Playground v0 packet fetched. Read-only representation only; no autonomous execution.",
            status="ok" if result.job else "failed",
        ),
    )
