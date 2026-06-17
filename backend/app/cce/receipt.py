"""CCE v0.1 receipt shape and builder."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field

from app.cce.types import CcePolicyDecision, FinalGateDecision


@dataclass(frozen=True)
class CceReceipt:
    """Minimum CCE receipt fields for audit-visible decisions."""

    cce_mode: str
    risk_level: str
    worker_roles_used: list[str]
    reason_for_mode: str
    human_escalation_required: bool
    confidence: float
    final_gate_decision: FinalGateDecision
    claims_checked: list[str] = field(default_factory=list)
    contradictions_found: list[str] = field(default_factory=list)
    bias_or_framing_flags: list[str] = field(default_factory=list)
    safety_flags: list[str] = field(default_factory=list)

    def model_dump(self) -> dict[str, object]:
        """Return a dict using the same call shape as Pydantic models."""

        return asdict(self)


def build_cce_receipt(
    decision: CcePolicyDecision,
    *,
    claims_checked: list[str] | None = None,
    contradictions_found: list[str] | None = None,
    bias_or_framing_flags: list[str] | None = None,
    safety_flags: list[str] | None = None,
    confidence: float | None = None,
    final_gate_decision: FinalGateDecision | None = None,
) -> CceReceipt:
    """Build a CCE receipt with v0.1 defaults for unimplemented workers."""

    default_gate: FinalGateDecision = (
        "escalate_to_human" if decision.requires_human_escalation else "allow_with_caveats"
    )

    return CceReceipt(
        cce_mode=decision.cce_mode,
        risk_level=decision.risk_level,
        worker_roles_used=list(decision.worker_roles),
        reason_for_mode=decision.reason_for_mode,
        claims_checked=claims_checked or [],
        contradictions_found=contradictions_found or [],
        bias_or_framing_flags=bias_or_framing_flags or [],
        safety_flags=safety_flags or list(decision.stop_conditions),
        human_escalation_required=decision.requires_human_escalation,
        confidence=0.0 if confidence is None else confidence,
        final_gate_decision=final_gate_decision or default_gate,
    )
