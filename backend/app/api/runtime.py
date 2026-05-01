"""Runtime inspection routes.

These routes expose configured capability state only. They must not leak
secrets, provider credentials, connection strings, or raw environment values.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import load_settings
from app.core.database import DatabaseHandle
from app.core.runtime_registry import build_runtime_registry
from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.services.receipt_service import action_receipt

router = APIRouter(prefix="/runtime", tags=["runtime"])


@router.get("", response_model=ApiEnvelope)
def runtime_state() -> ApiEnvelope:
    settings = load_settings()
    registry = build_runtime_registry(settings)
    database = DatabaseHandle(settings)
    runtime_data = registry.to_dict()
    database_data = database.state.to_dict()
    receipt = action_receipt(
        event_type="runtime_state_inspected",
        actor_type="system",
        reason="client requested runtime capability state",
        summary="Returned runtime and database configuration state without secrets.",
        outputs={
            "runtime": runtime_data,
            "database": database_data,
            "secrets_returned": False,
            "environment_values_returned": False,
        },
        metrics={
            "mongo_configured": database.state.configured,
            "dev_auth_enabled": settings.dev_auth_enabled,
        },
    )

    return ApiEnvelope(
        ok=True,
        data={
            "runtime": runtime_data,
            "database": database_data,
            "secrets_policy": {
                "secrets_returned": False,
                "environment_values_returned": False,
            },
            "receipt": receipt.model_dump(),
        },
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="foundation",
            detail="Runtime state exposed without secret values and with receipt.",
        ),
    )
