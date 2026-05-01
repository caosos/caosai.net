"""Model catalog and WCW metadata.

Values here are configurable product defaults. They should be verified against
provider documentation before production release and can later move to DB/admin
configuration.
"""

from __future__ import annotations

from app.schemas.models import ModelContextSpec


class ModelCatalog:
    def __init__(self) -> None:
        self._models: list[ModelContextSpec] = [
            ModelContextSpec(
                provider="openai",
                model="gpt-5.5-thinking",
                display_name="GPT-5.5 Thinking",
                context_window_tokens=200_000,
                usable_context_tokens=180_000,
                reserved_output_tokens=12_000,
                reserved_system_tokens=8_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="anthropic",
                model="claude-placeholder",
                display_name="Claude Placeholder",
                context_window_tokens=200_000,
                usable_context_tokens=180_000,
                reserved_output_tokens=12_000,
                reserved_system_tokens=8_000,
                wcw_policy="placeholder_verify_before_production",
                enabled=False,
            ),
            ModelContextSpec(
                provider="google",
                model="gemini-placeholder",
                display_name="Gemini Placeholder",
                context_window_tokens=1_000_000,
                usable_context_tokens=900_000,
                reserved_output_tokens=32_000,
                reserved_system_tokens=68_000,
                wcw_policy="placeholder_verify_before_production",
                enabled=False,
            ),
        ]

    def list_models(self, *, include_disabled: bool = True) -> list[ModelContextSpec]:
        if include_disabled:
            return list(self._models)
        return [model for model in self._models if model.enabled]

    def get_model(self, *, provider: str, model: str) -> ModelContextSpec | None:
        for spec in self._models:
            if spec.provider == provider and spec.model == model:
                return spec
        return None

    def default_model(self) -> ModelContextSpec:
        return self._models[0]


model_catalog = ModelCatalog()
