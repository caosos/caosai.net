"""Chat orchestrator — live providers, thread history, token counting, latency tracking."""

from __future__ import annotations

import os
import time
from uuid import uuid4

import litellm

from app.schemas.chat import ChatMessage, ChatRequest, ChatResponse
from app.schemas.threads import MessageRecord
from app.services.thread_service import thread_service

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


def _count_tokens(text: str) -> int:
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return max(1, len(text) // 4)


class ChatOrchestrator:
    def handle_turn(self, request: ChatRequest) -> ChatResponse:
        user_id = request.user_id or "dev_user"
        provider = request.provider or "anthropic"
        model = request.model or "claude-sonnet-4-6"

        litellm_model = PROVIDER_MODEL_MAP.get((provider, model))
        key_env = PROVIDER_KEY_ENV.get(provider)
        api_key = os.getenv(key_env) if key_env else None

        if not litellm_model or not api_key:
            thread = thread_service.get_or_create_thread(request.thread_id, user_id)
            return ChatResponse(
                thread_id=thread.thread_id,
                assistant_message=ChatMessage(
                    role="assistant",
                    content=f"Model '{provider}/{model}' is not available. Check that the API key is set.",
                ),
                provider=provider,
                model=model,
                receipt={"phase": "chat-provider-error", "provider_called": False},
            )

        # Get or create thread
        thread = thread_service.get_or_create_thread(request.thread_id, user_id)

        # Load prior messages from MongoDB
        prior = thread_service.get_thread_messages(thread.thread_id, limit=40)
        history = [{"role": m.role, "content": m.content} for m in prior]

        # Build messages list
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)
        messages.append({"role": "user", "content": request.message})

        # Generate title from first user message
        if thread.message_count == 0:
            title = thread_service.generate_title(request.message)
            thread_service.update_thread(thread.thread_id, user_id, title=title)

        # Save user message
        user_tokens = _count_tokens(request.message)
        thread_service.save_message(MessageRecord(
            thread_id=thread.thread_id,
            user_id=user_id,
            role="user",
            content=request.message,
            token_count=user_tokens,
        ))

        # Call provider
        t_start = time.monotonic()
        try:
            response = litellm.completion(
                model=litellm_model,
                messages=messages,
                api_key=api_key,
                max_tokens=4096,
            )
            latency_ms = int((time.monotonic() - t_start) * 1000)
            content = response.choices[0].message.content or ""
            provider_called = True
            error = None
        except Exception as exc:
            latency_ms = int((time.monotonic() - t_start) * 1000)
            content = f"Provider error: {exc}"
            provider_called = False
            error = str(exc)

        # Count tokens and save assistant message
        assistant_tokens = _count_tokens(content)
        thread_service.save_message(MessageRecord(
            thread_id=thread.thread_id,
            user_id=user_id,
            role="assistant",
            content=content,
            provider=provider,
            model=model,
            token_count=assistant_tokens,
            latency_ms=latency_ms,
        ))

        # Total tokens in this thread
        updated_thread = thread_service.get_or_create_thread(thread.thread_id, user_id)

        return ChatResponse(
            thread_id=thread.thread_id,
            assistant_message=ChatMessage(role="assistant", content=content),
            provider=provider,
            model=model,
            receipt={
                "phase": "chat-live",
                "provider_called": provider_called,
                "latency_ms": latency_ms,
                "user_tokens": user_tokens,
                "assistant_tokens": assistant_tokens,
                "thread_total_tokens": updated_thread.total_tokens,
                "memory_mutated": False,
                "tools_executed": False,
                "error": error,
            },
        )
