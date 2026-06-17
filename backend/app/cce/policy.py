"""Deterministic CCE v0.1 policy selection.

This module intentionally performs no provider calls, no tool execution, and no
runtime worker orchestration. It only returns the policy/data-contract decision
that future CCE runtime layers can consume.
"""

from __future__ import annotations

from app.cce.types import CcePolicyDecision, CcePolicyInput, RiskLevel

LOCKDOWN_STOP_CONDITIONS = [
    "no_ai_final_authority",
    "human_escalation_required",
]


RISK_ORDER: dict[str, int] = {
    "low": 0,
    "unknown": 1,
    "medium": 1,
    "high": 2,
    "critical": 3,
}


def _risk_from_hint(risk_hint: str) -> RiskLevel:
    if risk_hint == "critical":
        return "critical"
    if risk_hint == "high":
        return "high"
    if risk_hint == "medium":
        return "medium"
    return "low"


def _max_risk(current: RiskLevel, candidate: RiskLevel) -> RiskLevel:
    return candidate if RISK_ORDER[candidate] > RISK_ORDER[current] else current


def select_cce_policy(policy_input: CcePolicyInput) -> CcePolicyDecision:
    """Select the CCE mode using deterministic v0.1 baseline rules."""

    risk_level = _risk_from_hint(policy_input.risk_hint)

    if policy_input.medical_or_emergency_boundary:
        return CcePolicyDecision(
            cce_mode="lockdown",
            risk_level="critical",
            reason_for_mode=(
                "Medical, emergency, or autonomous authority boundary requires "
                "lockdown and human escalation."
            ),
            worker_roles=[],
            requires_verifier=True,
            requires_human_escalation=True,
            stop_conditions=LOCKDOWN_STOP_CONDITIONS,
        )

    if policy_input.requires_action and not policy_input.action_safety_clear:
        if RISK_ORDER[policy_input.risk_hint] >= RISK_ORDER["high"]:
            return CcePolicyDecision(
                cce_mode="lockdown",
                risk_level="critical",
                reason_for_mode=(
                    "Action request has unclear safety at high or critical risk; "
                    "block AI action and escalate to a human."
                ),
                worker_roles=[],
                requires_verifier=True,
                requires_human_escalation=True,
                stop_conditions=LOCKDOWN_STOP_CONDITIONS + ["unsafe_action_boundary"],
            )

        risk_level = _max_risk(risk_level, "medium")
        return CcePolicyDecision(
            cce_mode="verified",
            risk_level=risk_level,
            reason_for_mode="Action request has unclear safety and needs verifier review.",
            worker_roles=["primary", "verifier"],
            requires_verifier=True,
            requires_human_escalation=False,
            stop_conditions=["do_not_execute_action_without_clear_policy"],
        )

    if policy_input.admin_requested_council:
        risk_level = _max_risk(risk_level, "medium")
        return CcePolicyDecision(
            cce_mode="council",
            risk_level=risk_level,
            reason_for_mode="Admin explicitly requested council-mode review.",
            worker_roles=["primary", "opposition", "bias_framing", "synthesizer", "verifier"],
            requires_verifier=True,
            requires_human_escalation=False,
        )

    if policy_input.care_related and policy_input.privacy_sensitive:
        risk_level = _max_risk(risk_level, "medium")
        return CcePolicyDecision(
            cce_mode="verified",
            risk_level=risk_level,
            reason_for_mode="Privacy-sensitive care workflow requires at least verified mode.",
            worker_roles=["primary", "domain_safety", "verifier"],
            requires_verifier=True,
            requires_human_escalation=False,
            stop_conditions=["no_private_data_exposure", "no_autonomous_medical_authority"],
        )

    if policy_input.requires_sources:
        if risk_level in {"high", "critical"}:
            return CcePolicyDecision(
                cce_mode="council",
                risk_level=risk_level,
                reason_for_mode="High-risk source-heavy request needs council review.",
                worker_roles=["primary", "research", "opposition", "synthesizer", "verifier"],
                requires_verifier=True,
                requires_human_escalation=False,
            )

        risk_level = _max_risk(risk_level, "medium")
        return CcePolicyDecision(
            cce_mode="verified",
            risk_level=risk_level,
            reason_for_mode="Source-heavy request needs verifier review.",
            worker_roles=["primary", "research", "verifier"],
            requires_verifier=True,
            requires_human_escalation=False,
        )

    return CcePolicyDecision(
        cce_mode="fast",
        risk_level=risk_level,
        reason_for_mode="Low-risk request can use fast mode.",
        worker_roles=["primary"],
        requires_verifier=False,
        requires_human_escalation=False,
    )
