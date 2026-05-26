"""Model catalog and WCW metadata."""

from __future__ import annotations

from app.schemas.models import ModelContextSpec


class ModelCatalog:
    def __init__(self) -> None:
        self._models: list[ModelContextSpec] = [
            ModelContextSpec(
                provider="anthropic",
                model="claude-sonnet-4-6",
                display_name="Claude Sonnet",
                context_window_tokens=200_000,
                usable_context_tokens=180_000,
                reserved_output_tokens=12_000,
                reserved_system_tokens=8_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="anthropic",
                model="claude-opus-4-7",
                display_name="Claude Opus",
                context_window_tokens=200_000,
                usable_context_tokens=180_000,
                reserved_output_tokens=12_000,
                reserved_system_tokens=8_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="openai",
                model="gpt-4o",
                display_name="GPT-4o",
                context_window_tokens=128_000,
                usable_context_tokens=112_000,
                reserved_output_tokens=8_000,
                reserved_system_tokens=8_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="openai",
                model="gpt-4.5",
                display_name="GPT-4.5",
                context_window_tokens=128_000,
                usable_context_tokens=112_000,
                reserved_output_tokens=8_000,
                reserved_system_tokens=8_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="google",
                model="gemini-2.0-flash",
                display_name="Gemini 2.0 Flash",
                context_window_tokens=1_000_000,
                usable_context_tokens=900_000,
                reserved_output_tokens=32_000,
                reserved_system_tokens=68_000,
                wcw_policy="reserve_output_and_system_v1",
            ),
            ModelContextSpec(
                provider="xai",
                model="grok-3",
                display_name="Grok 3",
                context_window_tokens=131_072,
                usable_context_tokens=120_000,
                reserved_output_tokens=8_000,
                reserved_system_tokens=3_072,
                wcw_policy="reserve_output_and_system_v1",
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
