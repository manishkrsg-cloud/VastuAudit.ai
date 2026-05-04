"""Health & readiness probes."""

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text

from src.api.deps import DbSession
from src.config import settings
from src.redis_client import get_redis

router = APIRouter()


@router.get("/health", summary="Liveness probe")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "owner": settings.app_owner,
        "env": settings.app_env,
        "version": "0.1.0",
    }


@router.get("/health/ready", summary="Readiness probe (DB + Redis)")
async def readiness(db: DbSession) -> dict[str, bool | str]:
    db_ok = False
    redis_ok = False
    try:
        result = await db.execute(text("SELECT 1"))
        db_ok = result.scalar_one() == 1
    except Exception:
        db_ok = False
    try:
        redis_ok = bool(await get_redis().ping())
    except Exception:
        redis_ok = False

    payload: dict[str, bool | str] = {
        "database": db_ok,
        "redis": redis_ok,
        "status": "ok" if (db_ok and redis_ok) else "degraded",
    }
    if not (db_ok and redis_ok):
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail=payload)
    return payload
