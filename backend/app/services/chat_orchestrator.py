"""Minimal chat orchestrator.

This is the first contract stub for chat. It preserves the orchestrator shape
without provider calls, persistence, memory mutation, or tool execution.
"""

from __future__ import annotations

from uuid import uuid4

from app.schemas.chat import ChatMessage, ChatRequest, ChatResponse


class ChatOrchestrator:
    def handle_turn(self, request: ChatRequest) -> ChatResponse:
        thread_id = request.thread_id or f"dev-thread-{uuid4().hex}"

        return ChatResponse(
            thread_id=thread_id,
            assistant_message=ChatMessage(
                role="assistant",
                content=(
                    "CAOS chat contract is online. Provider inference, memory, "
                    "tools, and persistence are intentionally not wired yet."
                ),
            ),
            provider=request.provider or "local-contract",
            model=request.model or "foundation-stub",
            receipt={
                "phase": "chat-contract",
                "provider_called": False,
                "memory_mutated": False,
                "tools_executed": False,
                "persistence_written": False,
            },
        )
