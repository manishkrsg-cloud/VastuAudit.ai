# VastuAudit.ai

> Professional Vastu audits in 60 seconds. AI-powered. Consultant-grade.

A SaaS platform that generates AI-powered Vastu audit reports for property buyers, builders, and consultants across MENA + APAC.

**Owner:** Qadr AI Agency Dubai · **Trading name:** VastuAudit.ai by Qadr AI

## Repo layout

This is a `pnpm` + `turbo` monorepo with two deployable apps and a shared knowledge base.

```
apps/
  api/           FastAPI backend (Railway)         — Python 3.11, SQLAlchemy 2, Pydantic v2
  web/           Next.js 15 frontend (Vercel)      — TypeScript, Tailwind, shadcn/ui
packages/
  shared-types/  TS types shared between api & web
docs/            Architecture, API, deployment, methodology
reference/       Reference Python script for Vastu PDF v2.0 (legacy, being modularised)
```

The `apps/api/knowledge/` directory is the **brain of the product** — git-tracked, auditable, multi-traditional Vastu rules. See [docs/vastu_methodology.md](docs/vastu_methodology.md).

## Quick start (local dev)

```bash
# 1. Spin up Postgres + Redis
docker compose up -d

# 2. API
cd apps/api
uv sync
cp .env.example .env   # fill in secrets
uv run alembic upgrade head
uv run uvicorn src.main:app --reload --port 8000

# 3. Web (later sprints)
cd apps/web
pnpm install
pnpm dev
```

Health check: <http://localhost:8000/api/v1/health>

## Tech stack

| Layer        | Choice                                                  |
|--------------|---------------------------------------------------------|
| API          | FastAPI · SQLAlchemy 2 (async) · Pydantic v2            |
| Web          | Next.js 15 · TypeScript · Tailwind · shadcn/ui          |
| AI           | Anthropic Claude (Sonnet 4.6 vision · Opus 4.7 reasoning) |
| Database     | PostgreSQL + pgvector (Railway-managed)                 |
| Cache/Queue  | Redis (Railway-managed)                                 |
| Storage      | Cloudflare R2                                           |
| Auth         | Clerk                                                   |
| Payments     | Stripe                                                  |
| Email        | Resend                                                  |
| PDF          | WeasyPrint + Jinja2                                     |
| Deploy       | Railway (api/worker) · Vercel (web)                     |

## Sprint roadmap

- **Sprint 1** — Core MVP: skeleton, schema, R2 upload, Vastu engine v1, PDF, Railway deploy
- **Sprint 2** — AI: Claude Vision plan analysis, reasoning remedies, knowledge base, pgvector
- **Sprint 3** — Frontend: landing, Clerk auth, audit wizard, results, dashboard
- **Sprint 4** — Monetisation: Stripe tiers, customer portal, white-label PDF, public API

## Pricing tiers

| Tier        | Price      | Audits/mo  | Features                                    |
|-------------|------------|------------|---------------------------------------------|
| Free        | $0         | 1          | Basic report (no PDF)                       |
| Pro         | $19/mo     | 10         | Full PDF, all remedies                      |
| Consultant  | $99/mo     | Unlimited  | White-label, branding, API access           |
| Enterprise  | Custom     | Custom     | Embed in real estate platforms              |

---

Powered by Qadr AI Agency Dubai.
