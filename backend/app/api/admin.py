"""Admin routes for the portable CAOS backend."""

from __future__ import annotations

from fastapi import APIRouter

from app.policies.admin_boundary_policy import AdminAccessDeniedError, admin_boundary_state, require_admin
from app.schemas.admin import AdminProbeRequest, AdminProbeResponse
from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.services.receipt_service import action_receipt

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/probe", response_model=ApiEnvelope)
def admin_probe(request: AdminProbeRequest) -> ApiEnvelope:
    try:
        require_admin(is_admin=request.is_admin)
    except AdminAccessDeniedError as exc:
        receipt = action_receipt(
            event_type="admin_probe_blocked",
            actor_type="user",
            actor_id=request.user_id,
            reason="non-admin attempted admin boundary probe",
            summary="Admin policy blocked access.",
            status="blocked",
            inputs=request.model_dump(),
            outputs={"admin_access": False},
            approval_required=True,
            approval_present=False,
            approval_reason="admin capability requires server-side role authorization",
            error={"code": "ADMIN_ACCESS_DENIED", "message": str(exc)},
        )
        return ApiEnvelope(
            ok=False,
            data={"receipt": receipt.model_dump()},
            error_code="ADMIN_ACCESS_DENIED",
            message=str(exc),
            diagnostic_receipt=DiagnosticReceipt(
                status="blocked",
                phase="admin-boundary",
                detail="Admin policy blocked non-admin access with receipt.",
            ),
        )

    state = admin_boundary_state(is_admin=request.is_admin)
    response = AdminProbeResponse(
        user_id=request.user_id,
        admin_access=bool(state["admin_access"]),
        enforced_by=str(state["enforced_by"]),
    )
    receipt = action_receipt(
        event_type="admin_probe_allowed",
        actor_type="admin",
        actor_id=request.user_id,
        reason="admin boundary probe requested by authorized admin context",
        summary="Admin access permitted by server policy.",
        inputs=request.model_dump(),
        outputs=response.model_dump(),
        approval_required=True,
        approval_present=True,
        approval_reason="admin role flag satisfied server-side policy probe",
    )

    return ApiEnvelope(
        ok=True,
        data={"admin": response.model_dump(), "receipt": receipt.model_dump()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="admin-boundary",
            detail="Admin access permitted by server policy with receipt.",
        ),
    )
