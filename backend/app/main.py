"""CAOS backend entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from app.api.admin import router as admin_router
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.memory import router as memory_router
from app.api.models import router as models_router
from app.api.runtime import router as runtime_router
from app.core.config import load_settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    settings = load_settings()
    configure_logging(settings)

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0-foundation",
        description="Portable CAOS backend foundation.",
    )

    app.include_router(health_router, prefix="/api")
    app.include_router(auth_router, prefix="/api")
    app.include_router(runtime_router, prefix="/api")
    app.include_router(chat_router, prefix="/api")
    app.include_router(admin_router, prefix="/api")
    app.include_router(memory_router, prefix="/api")
    app.include_router(models_router, prefix="/api")

    return app


app = create_app()
