"""Admin routes for the portable CAOS backend."""

from __future__ import annotations

from fastapi import APIRouter

from app.policies.admin_boundary_policy import AdminAccessDeniedError, admin_boundary_state, require_admin
from app.schemas.admin import AdminProbeRequest, AdminProbeResponse
from app.schemas.common import ApiEnvelope, DiagnosticReceipt

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/probe", response_model=ApiEnvelope)
def admin_probe(request: AdminProbeRequest) -> ApiEnvelope:
    try:
        require_admin(is_admin=request.is_admin)
    except AdminAccessDeniedError as exc:
        return ApiEnvelope(
            ok=False,
            error_code="ADMIN_ACCESS_DENIED",
            message=str(exc),
            diagnostic_receipt=DiagnosticReceipt(
                status="blocked",
                phase="admin-boundary",
                detail="Admin policy blocked non-admin access.",
            ),
        )

    state = admin_boundary_state(is_admin=request.is_admin)
    response = AdminProbeResponse(
        user_id=request.user_id,
        admin_access=bool(state["admin_access"]),
        enforced_by=str(state["enforced_by"]),
    )

    return ApiEnvelope(
        ok=True,
        data=response.model_dump(),
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="admin-boundary",
            detail="Admin access permitted by server policy.",
        ),
    )
