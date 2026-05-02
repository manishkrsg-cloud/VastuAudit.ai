# VastuAudit.ai — API

FastAPI backend for VastuAudit.ai. A Qadr AI Agency Dubai product.

## Local development

```bash
# 1. Install Python 3.11 and uv (https://docs.astral.sh/uv/)
uv python install 3.11

# 2. Sync dependencies
uv sync

# 3. Bring up Postgres + Redis
docker compose -f ../../docker-compose.yml up -d

# 4. Configure environment
cp .env.example .env

# 5. Run migrations
uv run alembic upgrade head

# 6. Start the dev server
uv run uvicorn src.main:app --reload --port 8000
```

API root: <http://localhost:8000/api/v1>
Health: <http://localhost:8000/api/v1/health>
OpenAPI docs: <http://localhost:8000/docs>

## Layout

```
src/
  main.py              FastAPI app + lifespan
  config.py            Pydantic settings (env)
  database.py          Async SQLAlchemy engine/session
  redis_client.py      Async Redis client
  api/
    deps.py            Dependency injection
    v1/                Versioned routers
  models/              SQLAlchemy ORM
  schemas/             Pydantic DTOs
  services/            Business logic (Sprint 2+)
  core/                Vastu engine, prompts, PDF (Sprint 1.2+)
  workers/             Background jobs (Sprint 2+)
  utils/               Logging, image processing
knowledge/             Vastu rules + skill files (the BRAIN)
alembic/               Database migrations
tests/                 Pytest suite
```

## Conventions

- All I/O is `async`. No sync DB calls inside request handlers.
- Type hints on every function. Pydantic v2 for DTOs.
- Lint: `uv run ruff check .` · Format: `uv run black .` · Test: `uv run pytest`.
