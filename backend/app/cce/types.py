"""Types for the CCE v0.1 deterministic policy skeleton."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

CceMode = Literal["fast", "verified", "council", "lockdown"]
RiskHint = Literal["low", "medium", "high", "critical", "unknown"]
RiskLevel = Literal["low", "medium", "high", "critical"]
FinalGateDecision = Literal[
    "allow",
    "allow_with_caveats",
    "ask_for_missing_information",
    "escalate_to_human",
    "block_action",
    "create_ticket_or_record",
    "require_admin_review",
]


@dataclass(frozen=True)
class CcePolicyInput:
    """Minimum input contract for CCE v0.1 mode selection."""

    request_text: str
    surface: str = "unknown"
    actor_role: str = "user"
    risk_hint: RiskHint = "unknown"
    requires_sources: bool = False
    requires_action: bool = False
    care_related: bool = False
    medical_or_emergency_boundary: bool = False
    privacy_sensitive: bool = False
    admin_requested_council: bool = False
    action_safety_clear: bool = True


@dataclass(frozen=True)
class CcePolicyDecision:
    """Deterministic CCE policy output for downstream orchestration."""

    cce_mode: CceMode
    risk_level: RiskLevel
    reason_for_mode: str
    requires_verifier: bool
    requires_human_escalation: bool
    worker_roles: list[str] = field(default_factory=list)
    receipt_required: bool = True
    stop_conditions: list[str] = field(default_factory=list)
