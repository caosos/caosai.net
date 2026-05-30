"""Chat orchestrator — live providers, thread history, token counting, latency tracking.

Per-turn discipline ledger is integrated here. The orchestrator records one
turn_ledger per chat turn and refuses to make more than one model call. Tool
calls, retries, hydration, and silent memory mutation are NOT performed by
this orchestrator; their counters stay at zero.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Optional
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


class MultipleModelCallsError(Exception):
    """Raised when a single chat turn attempts more than one model call.

    Token-discipline policy: one user turn = at most one provider model call.
    If a code path tries a second call, this raises rather than silently doing
    it. The orchestrator catches this, records the failure in the ledger, and
    returns a structured error to the caller — never a generic 500.
    """

    code = "MULTIPLE_LLM_CALLS_NOT_AUTHORIZED"


def _count_tokens(text: str) -> int:
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return max(1, len(text) // 4)


@dataclass
class TurnLedger:
    """Per-turn discipline ledger.

    Tracks the cognitive cost of a single chat turn. Surfaces in the receipt
    so the UI can render a discipline chip and so policy violations are
    visible rather than buried.
    """

    turn_id: str = field(default_factory=lambda: f"turn_{uuid4().hex[:12]}")
    started_monotonic: float = field(default_factory=time.monotonic)

    model_calls: int = 0
    tool_calls: int = 0
    retries: int = 0
    memory_read: bool = False
    memory_written: bool = False
    hydration_size_tokens: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    failure_state: str = "ok"
    mode_decision: str = "direct_answer"

    def assert_can_call_model(self) -> None:
        """Single-call policy guard. Call BEFORE every provider request."""
        if self.model_calls >= 1:
            raise MultipleModelCallsError(
                "Token-discipline policy: only one model call per chat turn is "
                "authorized. A second call was attempted in turn "
                f"{self.turn_id}."
            )

    def record_model_call(self) -> None:
        self.model_calls += 1

    def finalize(self, estimated_cost_usd: Optional[float] = None) -> dict:
        elapsed_ms = int((time.monotonic() - self.started_monotonic) * 1000)
        total_tokens = self.input_tokens + self.output_tokens
        memory_state = "no memory"
        if self.memory_read and self.memory_written:
            memory_state = "read+written"
        elif self.memory_read:
            memory_state = "read"
        elif self.memory_written:
            memory_state = "written"
        return {
            "turn_id": self.turn_id,
            "model_calls": self.model_calls,
            "tool_calls": self.tool_calls,
            "retries": self.retries,
            "elapsed_ms": elapsed_ms,
            "memory_read": self.memory_read,
            "memory_written": self.memory_written,
            "memory_state": memory_state,
            "hydration_size_tokens": self.hydration_size_tokens,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": total_tokens,
            "failure_state": self.failure_state,
            "mode_decision": self.mode_decision,
            "estimated_cost_usd": estimated_cost_usd,
        }


class ChatOrchestrator:
    def handle_turn(self, request: ChatRequest) -> ChatResponse:
        ledger = TurnLedger()
        user_id = request.user_id or "dev_user"
        provider = request.provider or "anthropic"
        model = request.model or "claude-sonnet-4-6"

        litellm_model = PROVIDER_MODEL_MAP.get((provider, model))
        key_env = PROVIDER_KEY_ENV.get(provider)
        api_key = os.getenv(key_env) if key_env else None

        if not litellm_model or not api_key:
            ledger.failure_state = "config_error"
            ledger.mode_decision = "config_error"
            thread = thread_service.get_or_create_thread(request.thread_id, user_id)
            return ChatResponse(
                thread_id=thread.thread_id,
                assistant_message=ChatMessage(
                    role="assistant",
                    content=f"Model '{provider}/{model}' is not available. Check that the API key is set.",
                ),
                provider=provider,
                model=model,
                receipt={
                    "phase": "chat-provider-error",
                    "provider_called": False,
                    "turn_ledger": ledger.finalize(),
                },
            )

        thread = thread_service.get_or_create_thread(request.thread_id, user_id)

        prior = thread_service.get_thread_messages(thread.thread_id, limit=40)
        history = [{"role": m.role, "content": m.content} for m in prior]

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)
        messages.append({"role": "user", "content": request.message})

        if thread.message_count == 0:
            title = thread_service.generate_title(request.message)
            thread_service.update_thread(thread.thread_id, user_id, title=title)

        user_tokens = _count_tokens(request.message)
        thread_service.save_message(MessageRecord(
            thread_id=thread.thread_id,
            user_id=user_id,
            role="user",
            content=request.message,
            token_count=user_tokens,
        ))

        # Hydration size = system prompt + prior history tokens (no memory
        # injection in this orchestrator).
        ledger.hydration_size_tokens = _count_tokens(SYSTEM_PROMPT) + sum(
            _count_tokens(m["content"]) for m in history
        )
        ledger.input_tokens = ledger.hydration_size_tokens + user_tokens

        t_start = time.monotonic()
        try:
            ledger.assert_can_call_model()
            ledger.record_model_call()
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
        except MultipleModelCallsError as policy_exc:
            latency_ms = int((time.monotonic() - t_start) * 1000)
            content = (
                f"⚠️ {policy_exc.code}: a second model call was blocked by "
                "token-discipline policy. This turn was halted to prevent "
                "silent token consumption."
            )
            provider_called = False
            error = policy_exc.code
            ledger.failure_state = "policy_violation_multiple_calls"
            ledger.mode_decision = "policy_violation_multiple_calls"
        except Exception as exc:
            latency_ms = int((time.monotonic() - t_start) * 1000)
            content = f"Provider error: {exc}"
            provider_called = False
            error = str(exc)
            ledger.failure_state = "provider_error"
            ledger.mode_decision = "provider_error"

        assistant_tokens = _count_tokens(content)
        ledger.output_tokens = assistant_tokens

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
                "turn_ledger": ledger.finalize(),
            },
        )
