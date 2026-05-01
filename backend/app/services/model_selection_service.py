"""Model selection service.

Keeps active model/WCW selection logic out of route files and UI components.
"""

from __future__ import annotations

from app.schemas.models import ModelContextSpec, ModelSelectionRequest, ModelSelectionResponse
from app.services.model_catalog import model_catalog


class ModelSelectionService:
    def select(self, request: ModelSelectionRequest | None = None) -> ModelSelectionResponse:
        active: ModelContextSpec

        if request is None:
            active = model_catalog.default_model()
        else:
            found = model_catalog.get_model(provider=request.provider, model=request.model)
            active = found or model_catalog.default_model()

        return ModelSelectionResponse(
            active_model=active,
            available_models=model_catalog.list_models(include_disabled=True),
        )


model_selection_service = ModelSelectionService()
