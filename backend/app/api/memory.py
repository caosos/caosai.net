"""Memory routes for the portable CAOS rebuild."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.schemas.memory import MemoryCreateRequest, MemoryListRequest
from app.services.memory_service import memory_service
from app.services.receipt_service import action_receipt

router = APIRouter(prefix="/memory", tags=["memory"])


@router.post("/atoms", response_model=ApiEnvelope)
def create_memory_atom(request: MemoryCreateRequest) -> ApiEnvelope:
    atom = memory_service.create_atom(request)
    receipt = action_receipt(
        event_type="memory_atom_created",
        actor_type="assistant",
        actor_id=request.user_id,
        reason="memory-worthy material was submitted for capture",
        summary="Created governed memory atom in temporary in-process store.",
        inputs={
            "user_id": request.user_id,
            "category": request.category,
            "source_type": request.source_type,
            "confidence": request.confidence,
            "priority": request.priority,
        },
        outputs={"memory_id": atom.memory_id, "status": atom.status},
        changes=[
            {
                "field": "memory_atom",
                "action": "created",
                "memory_id": atom.memory_id,
                "category": atom.category,
            }
        ],
        memory_refs=[atom.memory_id],
    )

    return ApiEnvelope(
        ok=True,
        data={"atom": atom.model_dump(), "receipt": receipt.model_dump()},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="memory-contract",
            detail="Memory atom captured with action receipt in temporary in-process store.",
        ),
    )


@router.post("/atoms/query", response_model=ApiEnvelope)
def list_memory_atoms(request: MemoryListRequest) -> ApiEnvelope:
    atoms = memory_service.list_atoms(request)
    receipt = action_receipt(
        event_type="memory_atoms_queried",
        actor_type="system",
        actor_id=request.user_id,
        reason="memory atoms requested for review or ARC selection",
        summary="Listed governed memory atoms from temporary in-process store.",
        inputs=request.model_dump(),
        outputs={"count": len(atoms)},
        memory_refs=[atom.memory_id for atom in atoms],
    )

    return ApiEnvelope(
        ok=True,
        data={
            "atoms": [atom.model_dump() for atom in atoms],
            "count": len(atoms),
            "receipt": receipt.model_dump(),
        },
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="memory-contract",
            detail="Memory atoms listed with action receipt from temporary in-process store.",
        ),
    )
