"""v1 API router aggregator."""

from fastapi import APIRouter

from src.api.v1 import audits, auth, health

router = APIRouter()
router.include_router(health.router, tags=["health"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(audits.router, prefix="/audits", tags=["audits"])

__all__ = ["router"]
