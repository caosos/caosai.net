"""Chat orchestrator — routes to live providers via LiteLLM."""

from __future__ import annotations

import os
from uuid import uuid4

import litellm

from app.schemas.chat import ChatMessage, ChatRequest, ChatResponse

litellm.drop_params = True

PROVIDER_MODEL_MAP = {
    ("openai", "gpt-4o"): "openai/gpt-4o",
    ("openai", "gpt-4.5"): "openai/gpt-4.5-preview",
    ("openai", "gpt-5.5"): "openai/gpt-5.5",
    ("anthropic", "claude-sonnet-4-6"): "anthropic/claude-sonnet-4-6",
    ("anthropic", "claude-opus-4-7"): "anthropic/claude-opus-4-7",
    ("google", "gemini-2.0-flash"): "gemini/gemini-2.0-flash",
    ("xai", "grok-3"): "xai/grok-3",
}

PROVIDER_KEY_ENV = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "google": "GOOGLE_API_KEY",
    "xai": "XAI_API_KEY",
}

SYSTEM_PROMPT = (
    "You are Aria, the assistant interface of CAOS — a governed, user-owned AI operating "
    "environment. You are direct, capable, and honest. You do not fabricate information. "
    "You surface uncertainty rather than guess. You help the user remember, reason, build, "
    "and act. CAOS is not a chatbot — it is an operating system for AI-assisted work."
)


class ChatOrchestrator:
    def handle_turn(self, request: ChatRequest) -> ChatResponse:
        thread_id = request.thread_id or f"thread_{uuid4().hex}"

        provider = request.provider or "anthropic"
        model = request.model or "claude-sonnet-4-6"

        litellm_model = PROVIDER_MODEL_MAP.get((provider, model))
        key_env = PROVIDER_KEY_ENV.get(provider)
        api_key = os.getenv(key_env) if key_env else None

        if not litellm_model or not api_key:
            return ChatResponse(
                thread_id=thread_id,
                assistant_message=ChatMessage(
                    role="assistant",
                    content=(
                        f"Model '{provider}/{model}' is not available. "
                        "Check that the API key is set and the model name is correct."
                    ),
                ),
                provider=provider,
                model=model,
                receipt={
                    "phase": "chat-provider-error",
                    "provider_called": False,
                    "error": "model_not_available",
                },
            )

        try:
            response = litellm.completion(
                model=litellm_model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": request.message},
                ],
                api_key=api_key,
                max_tokens=4096,
            )
            content = response.choices[0].message.content or ""
            provider_called = True
            error = None
        except Exception as exc:
            content = f"Provider error: {exc}"
            provider_called = False
            error = str(exc)

        return ChatResponse(
            thread_id=thread_id,
            assistant_message=ChatMessage(role="assistant", content=content),
            provider=provider,
            model=model,
            receipt={
                "phase": "chat-live",
                "provider_called": provider_called,
                "memory_mutated": False,
                "tools_executed": False,
                "persistence_written": False,
                "error": error,
            },
        )
