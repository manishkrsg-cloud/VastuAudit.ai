"""VastuAudit.ai API entry point.

Run locally with::

    uv run uvicorn src.main:app --reload --port 8000
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1 import router as api_v1_router
from src.config import settings
from src.database import dispose_engine
from src.redis_client import close_redis, get_redis
from src.utils.logging import configure_logging, get_logger

configure_logging(settings.log_level)
log = get_logger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Init resources on startup, dispose on shutdown."""
    log.info(
        "api.startup",
        app=settings.app_name,
        owner=settings.app_owner,
        env=settings.app_env,
    )
    try:
        await get_redis().ping()
    except Exception as exc:
        log.warning("redis.ping.failed", err=str(exc))
    yield
    log.info("api.shutdown")
    await close_redis()
    await dispose_engine()


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description=(
        f"{settings.app_name} — AI-powered Vastu audits. "
        f"By {settings.app_owner}. Tagline: "
        "Professional Vastu audits in 60 seconds. AI-powered. Consultant-grade."
    ),
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "owner": settings.app_owner,
        "tagline": "Professional Vastu audits in 60 seconds. AI-powered. Consultant-grade.",
        "docs": "/docs",
        "health": "/api/v1/health",
        "version": "0.1.0",
    }
