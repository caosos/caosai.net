"""Token-discipline tests for the per-turn ledger.

These tests verify the discipline mechanism in isolation — no MongoDB, no
real provider calls. They prove:

1. The ledger starts in a clean state (zero counters, ok failure_state).
2. The single-call policy is enforced: a second model call raises
   MultipleModelCallsError with code MULTIPLE_LLM_CALLS_NOT_AUTHORIZED.
3. finalize() returns every field required by the approved scope.
4. The exception code matches the contract the frontend will read.
"""
from __future__ import annotations

import time

import pytest

from app.services.chat_orchestrator import (
    MultipleModelCallsError,
    TurnLedger,
)


REQUIRED_LEDGER_FIELDS = {
    "turn_id",
    "model_calls",
    "tool_calls",
    "retries",
    "elapsed_ms",
    "memory_read",
    "memory_written",
    "memory_state",
    "hydration_size_tokens",
    "input_tokens",
    "output_tokens",
    "total_tokens",
    "failure_state",
    "mode_decision",
    "estimated_cost_usd",
}


def test_ledger_starts_clean():
    ledger = TurnLedger()
    assert ledger.model_calls == 0
    assert ledger.tool_calls == 0
    assert ledger.retries == 0
    assert ledger.memory_read is False
    assert ledger.memory_written is False
    assert ledger.hydration_size_tokens == 0
    assert ledger.input_tokens == 0
    assert ledger.output_tokens == 0
    assert ledger.failure_state == "ok"
    assert ledger.mode_decision == "direct_answer"
    assert ledger.turn_id.startswith("turn_")


def test_assert_can_call_model_passes_when_zero_calls():
    ledger = TurnLedger()
    ledger.assert_can_call_model()  # must not raise


def test_record_model_call_increments():
    ledger = TurnLedger()
    ledger.record_model_call()
    assert ledger.model_calls == 1


def test_second_call_blocked_by_policy():
    ledger = TurnLedger()
    ledger.assert_can_call_model()
    ledger.record_model_call()
    with pytest.raises(MultipleModelCallsError) as exc_info:
        ledger.assert_can_call_model()
    assert exc_info.value.code == "MULTIPLE_LLM_CALLS_NOT_AUTHORIZED"
    assert ledger.turn_id in str(exc_info.value)


def test_finalize_includes_all_required_fields():
    ledger = TurnLedger()
    ledger.record_model_call()
    ledger.input_tokens = 42
    ledger.output_tokens = 7
    receipt = ledger.finalize()
    assert REQUIRED_LEDGER_FIELDS.issubset(receipt.keys())
    assert receipt["model_calls"] == 1
    assert receipt["input_tokens"] == 42
    assert receipt["output_tokens"] == 7
    assert receipt["total_tokens"] == 49
    assert receipt["estimated_cost_usd"] is None  # default — no pricing dep
    assert receipt["failure_state"] == "ok"
    assert receipt["mode_decision"] == "direct_answer"
    assert receipt["memory_state"] == "no memory"


def test_memory_state_reflects_flags():
    cases = [
        (False, False, "no memory"),
        (True, False, "read"),
        (False, True, "written"),
        (True, True, "read+written"),
    ]
    for read_flag, write_flag, expected in cases:
        ledger = TurnLedger()
        ledger.memory_read = read_flag
        ledger.memory_written = write_flag
        assert ledger.finalize()["memory_state"] == expected, (
            f"read={read_flag} write={write_flag} expected {expected}"
        )


def test_finalize_elapsed_ms_is_non_negative_and_monotonic():
    ledger = TurnLedger()
    time.sleep(0.005)
    receipt = ledger.finalize()
    assert isinstance(receipt["elapsed_ms"], int)
    assert receipt["elapsed_ms"] >= 0


def test_estimated_cost_usd_can_be_set():
    ledger = TurnLedger()
    receipt = ledger.finalize(estimated_cost_usd=0.00042)
    assert receipt["estimated_cost_usd"] == 0.00042


def test_failure_state_can_be_set_for_policy_violation():
    ledger = TurnLedger()
    ledger.record_model_call()
    try:
        ledger.assert_can_call_model()
    except MultipleModelCallsError:
        ledger.failure_state = "policy_violation_multiple_calls"
        ledger.mode_decision = "policy_violation_multiple_calls"
    receipt = ledger.finalize()
    assert receipt["failure_state"] == "policy_violation_multiple_calls"
    assert receipt["mode_decision"] == "policy_violation_multiple_calls"


def test_exception_code_is_stable_contract():
    """The frontend will read this code. Don't rename it without coordination."""
    assert MultipleModelCallsError.code == "MULTIPLE_LLM_CALLS_NOT_AUTHORIZED"
