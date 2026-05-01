"""Database boundary for the portable CAOS backend.

This module defines the database wiring contract without forcing every route to
require Mongo during early foundation work.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from .config import Settings


@dataclass(frozen=True)
class DatabaseState:
    configured: bool
    database_name: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "configured": self.configured,
            "database_name": self.database_name,
        }


class DatabaseHandle:
    def __init__(self, settings: Settings):
        self._settings = settings
        self._client: AsyncIOMotorClient | None = None
        self._database: AsyncIOMotorDatabase | None = None

    @property
    def state(self) -> DatabaseState:
        return DatabaseState(
            configured=bool(self._settings.mongo_uri.strip()),
            database_name=self._settings.mongo_db_name,
        )

    def connect(self) -> AsyncIOMotorDatabase | None:
        if not self._settings.mongo_uri.strip():
            return None

        if self._client is None:
            self._client = AsyncIOMotorClient(self._settings.mongo_uri)
            self._database = self._client[self._settings.mongo_db_name]

        return self._database

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
        self._client = None
        self._database = None
