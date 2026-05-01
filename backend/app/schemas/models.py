"""Model and WCW contract schemas."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ModelContextSpec(BaseModel):
    provider: str
    model: str
    display_name: str
    context_window_tokens: int = Field(gt=0)
    usable_context_tokens: int = Field(gt=0)
    reserved_output_tokens: int = Field(ge=0)
    reserved_system_tokens: int = Field(ge=0)
    wcw_policy: str
    enabled: bool = True


class ModelSelectionRequest(BaseModel):
    provider: str
    model: str


class ModelSelectionResponse(BaseModel):
    active_model: ModelContextSpec
    available_models: list[ModelContextSpec]
