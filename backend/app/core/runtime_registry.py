"""Runtime capability registry for CAOS backend.

The registry reports what the current process is configured to do. It does
not perform external calls and does not imply provider availability.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

from .config import Settings


@dataclass(frozen=True)
class RuntimeRegistry:
    app_name: str
    environment: str
    dev_auth_enabled: bool
    mongo_configured: bool
    base44_runtime_enabled: bool = False
    emergent_oauth_enabled: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_runtime_registry(settings: Settings) -> RuntimeRegistry:
    return RuntimeRegistry(
        app_name=settings.app_name,
        environment=settings.environment,
        dev_auth_enabled=settings.dev_auth_enabled,
        mongo_configured=bool(settings.mongo_uri.strip()),
    )
