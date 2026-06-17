from app.cce import CcePolicyInput, build_cce_receipt, select_cce_policy


def test_low_risk_request_uses_fast_mode() -> None:
    decision = select_cce_policy(CcePolicyInput(request_text="Summarize this public note."))

    assert decision.cce_mode == "fast"
    assert decision.worker_roles == ["primary"]
    assert decision.requires_verifier is False


def test_privacy_sensitive_care_request_uses_verified_mode() -> None:
    decision = select_cce_policy(
        CcePolicyInput(
            request_text="Route this care workflow note safely.",
            care_related=True,
            privacy_sensitive=True,
        )
    )

    assert decision.cce_mode == "verified"
    assert decision.requires_verifier is True
    assert "domain_safety" in decision.worker_roles


def test_admin_council_request_uses_council_mode() -> None:
    decision = select_cce_policy(
        CcePolicyInput(
            request_text="Review this architecture decision with council mode.",
            admin_requested_council=True,
        )
    )

    assert decision.cce_mode == "council"
    assert "synthesizer" in decision.worker_roles
    assert decision.requires_verifier is True


def test_medical_or_emergency_boundary_uses_lockdown() -> None:
    decision = select_cce_policy(
        CcePolicyInput(
            request_text="Decide whether this emergency needs treatment.",
            medical_or_emergency_boundary=True,
        )
    )

    assert decision.cce_mode == "lockdown"
    assert decision.requires_human_escalation is True
    assert "no_ai_final_authority" in decision.stop_conditions


def test_lockdown_overrides_admin_requested_council() -> None:
    decision = select_cce_policy(
        CcePolicyInput(
            request_text="Use council, but this crosses emergency authority.",
            admin_requested_council=True,
            medical_or_emergency_boundary=True,
        )
    )

    assert decision.cce_mode == "lockdown"
    assert decision.requires_human_escalation is True


def test_receipt_builder_includes_required_fields() -> None:
    decision = select_cce_policy(CcePolicyInput(request_text="Summarize this public note."))
    receipt = build_cce_receipt(decision)
    receipt_data = receipt.model_dump()

    for field in [
        "cce_mode",
        "risk_level",
        "worker_roles_used",
        "reason_for_mode",
        "claims_checked",
        "contradictions_found",
        "bias_or_framing_flags",
        "safety_flags",
        "human_escalation_required",
        "confidence",
        "final_gate_decision",
    ]:
        assert field in receipt_data

    assert receipt_data["cce_mode"] == "fast"
    assert receipt_data["claims_checked"] == []
