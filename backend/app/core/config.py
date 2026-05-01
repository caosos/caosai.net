"""Runtime configuration for the CAOS backend.

This module is intentionally small and dependency-light. It must not import
FastAPI, database clients, provider SDKs, or application services.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str
    environment: str
    log_level: str
    dev_auth_enabled: bool
    mongo_uri: str
    mongo_db_name: str

    @property
    def is_development(self) -> bool:
        return self.environment.lower() in {"dev", "development", "local"}


def _bool_env(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def load_settings() -> Settings:
    return Settings(
        app_name=os.getenv("CAOS_APP_NAME", "CAOS"),
        environment=os.getenv("CAOS_ENV", "development"),
        log_level=os.getenv("CAOS_LOG_LEVEL", "INFO"),
        dev_auth_enabled=_bool_env("CAOS_DEV_AUTH_ENABLED", True),
        mongo_uri=os.getenv("MONGO_URI", ""),
        mongo_db_name=os.getenv("MONGO_DB_NAME", "caos"),
    )
