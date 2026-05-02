"""RQ worker entry point.

Picks jobs off the ``default`` Redis queue. The Vastu audit pipeline is
linear (parse plan → AI vision → engine → PDF → notify), so RQ is plenty;
upgrade to Celery only if we later need chains/groups/chords.

Run locally::

    uv run python -m src.workers.rq_worker

In Railway, this is the start command for the ``worker`` service (same
Dockerfile as the api service, different ``startCommand``).
"""

from __future__ import annotations

import sys

from redis import Redis
from rq import Queue, Worker

from src.config import settings
from src.utils.logging import configure_logging, get_logger

QUEUE_NAMES: tuple[str, ...] = ("default",)


def main() -> int:
    configure_logging(settings.log_level)
    log = get_logger(__name__)
    log.info(
        "worker.startup",
        env=settings.app_env,
        queues=list(QUEUE_NAMES),
        redis_url=_safe_redis_url(settings.redis_url),
    )

    connection = Redis.from_url(settings.redis_url)
    queues = [Queue(name, connection=connection) for name in QUEUE_NAMES]
    Worker(queues, connection=connection).work(with_scheduler=True)
    return 0


def _safe_redis_url(url: str) -> str:
    """Strip credentials before logging."""
    if "@" not in url:
        return url
    scheme, rest = url.split("://", 1)
    return f"{scheme}://***@{rest.rsplit('@', 1)[-1]}"


if __name__ == "__main__":
    sys.exit(main())
