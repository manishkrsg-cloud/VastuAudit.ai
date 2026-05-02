"""Async Redis client. Single connection pool managed by the FastAPI lifespan."""

from redis.asyncio import Redis, from_url

from src.config import settings

_redis: Redis | None = None


def get_redis() -> Redis:
    """Return the process-wide async Redis client, creating it on first call."""
    global _redis
    if _redis is None:
        _redis = from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
    return _redis


async def close_redis() -> None:
    global _redis
    if _redis is not None:
        await _redis.aclose()
        _redis = None
