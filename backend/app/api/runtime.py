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

router = APIRouter(prefix="/runtime", tags=["runtime"])


@router.get("", response_model=ApiEnvelope)
def runtime_state() -> ApiEnvelope:
    settings = load_settings()
    registry = build_runtime_registry(settings)
    database = DatabaseHandle(settings)

    return ApiEnvelope(
        ok=True,
        data={
            "runtime": registry.to_dict(),
            "database": database.state.to_dict(),
            "secrets_policy": {
                "secrets_returned": False,
                "environment_values_returned": False,
            },
        },
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="foundation",
            detail="Runtime state exposed without secret values.",
        ),
    )
