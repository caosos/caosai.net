"""Memory routes for the portable CAOS rebuild."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import ApiEnvelope, DiagnosticReceipt
from app.schemas.memory import MemoryCreateRequest, MemoryListRequest
from app.services.memory_service import memory_service

router = APIRouter(prefix="/memory", tags=["memory"])


@router.post("/atoms", response_model=ApiEnvelope)
def create_memory_atom(request: MemoryCreateRequest) -> ApiEnvelope:
    atom = memory_service.create_atom(request)
    return ApiEnvelope(
        ok=True,
        data=atom.model_dump(),
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="memory-contract",
            detail="Memory atom captured in temporary in-process store.",
        ),
    )


@router.post("/atoms/query", response_model=ApiEnvelope)
def list_memory_atoms(request: MemoryListRequest) -> ApiEnvelope:
    atoms = memory_service.list_atoms(request)
    return ApiEnvelope(
        ok=True,
        data={"atoms": [atom.model_dump() for atom in atoms], "count": len(atoms)},
        diagnostic_receipt=DiagnosticReceipt(
            status="ok",
            phase="memory-contract",
            detail="Memory atoms listed from temporary in-process store.",
        ),
    )
