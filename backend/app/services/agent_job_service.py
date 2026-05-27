"""Agent playground v0 service using in-process non-production storage."""

from __future__ import annotations

from datetime import datetime, timezone

from app.schemas.agent_jobs import AgentJobCreateRequest, AgentJobPacket, AgentJobResponse
from app.services.receipt_service import action_receipt

# v0 non-production storage: in-memory dictionary cleared on process restart.
_AGENT_JOBS: dict[str, AgentJobPacket] = {}


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_job(payload: AgentJobCreateRequest) -> AgentJobResponse:
    job = AgentJobPacket(**payload.model_dump())
    job.updated_at = _utc_now_iso()
    _AGENT_JOBS[job.job_id] = job

    receipt = action_receipt(
        event_type="agent_job.created",
        actor_type="system",
        reason="Created read-only playground job packet.",
        summary="Agent job packet stored in v0 in-process service store.",
        inputs={"project_id": job.project_id, "agent_role": job.agent_role},
        outputs={"job_id": job.job_id, "status": job.status},
        changes=[{"created": "agent_job_packet", "job_id": job.job_id}],
        metrics={"job_count": len(_AGENT_JOBS)},
    )
    return AgentJobResponse(job=job, receipt=receipt)


def list_jobs() -> AgentJobResponse:
    jobs = list(_AGENT_JOBS.values())
    receipt = action_receipt(
        event_type="agent_job.listed",
        actor_type="system",
        reason="Listed read-only playground job packets.",
        summary="Returned agent job packets from v0 in-process service store.",
        outputs={"count": len(jobs)},
        metrics={"job_count": len(jobs)},
    )
    return AgentJobResponse(jobs=jobs, receipt=receipt)


def get_job(job_id: str) -> AgentJobResponse:
    job = _AGENT_JOBS.get(job_id)
    status = "ok" if job else "failed"
    receipt = action_receipt(
        event_type="agent_job.retrieved",
        actor_type="system",
        reason="Retrieved read-only playground job packet.",
        summary="Returned requested agent job packet from v0 in-process service store."
        if job
        else "Requested agent job packet not found in v0 in-process service store.",
        status=status,
        inputs={"job_id": job_id},
        outputs={"found": bool(job)},
        error=None if job else {"code": "agent_job_not_found", "message": "Agent job not found."},
    )
    return AgentJobResponse(job=job, receipt=receipt)
