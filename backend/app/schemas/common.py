"""Common API response schemas."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DiagnosticReceipt(BaseModel):
    status: str = Field(description="Machine-readable operation status.")
    phase: str = Field(description="Current rebuild/runtime phase.")
    detail: str | None = Field(default=None)


class ApiEnvelope(BaseModel):
    ok: bool
    data: dict[str, Any] | None = None
    error_code: str | None = None
    message: str | None = None
    diagnostic_receipt: DiagnosticReceipt
