# Build Status

_Last updated: 2026-05-07 by Claude Code_

**How to use:** This file is the running ledger of what's actually shipped vs. [development-plan.md](development-plan.md). Update at the end of every working session: flip statuses, append to the commit log, refresh "Next actions." Keep it terse — links and tables, not prose.

**Status legend:** ✅ Done & verified · 🟢 Done, unverified · 🟡 Partial · ⏸️ Not started · ❌ Blocked / decision needed

---

## Today's position

- **Plan target:** Sprint 1.A Day 1 — `/health` returns 200 on Railway
- **Reality:** ✅ **DONE.** API live at <https://vastuaudit-api-production.up.railway.app>, `/api/v1/health` returns 200 with `env=production`.
- **Day 2 gate:** held by Manish — do not start until lifted.

## Workflow note (2026-05-04)

**Deploy-only.** No local Docker, no local uvicorn, no OrbStack. Railway is the only execution environment. Verification happens against the production URL.

## Live infrastructure (Railway)

| Resource | Status | ID / URL |
|---|---|---|
| Project `vastuaudit` | ✅ active | `865353e2-0ac8-458d-b521-4009b4c924e5` |
| Service `vastuaudit-api` | ✅ running, healthy | `2ace0d58-81ce-4925-8de2-aae53d902205` |
| API URL | ✅ live | <https://vastuaudit-api-production.up.railway.app> |
| Healthcheck | ✅ 200 | `/api/v1/health` (liveness, no DB) |
| Service env vars | partial | `APP_ENV=production` set; secrets not yet (Anthropic, Clerk, Stripe, R2, Resend) |
| Postgres add-on | ⏸️ not provisioned | Day 2 |
| Redis add-on | ⏸️ not provisioned | Day 2 |
| `vastuaudit-worker` service | ⏸️ not created | Sprint 2 Day 20 |
| Auto-deploy from `main` | ⏸️ not wired | currently using `railway up` from CLI |
| Project `vastuaudit-prototype` (separate) | ✅ active, online | static HTML prototype |

---

## Commits on `main` (newest first)

| SHA | Date | Message |
|---|---|---|
| `14b0d6f` | 2026-05-07 | fix(api): drop startCommand from railway.json — use Dockerfile CMD |
| `f5108e5` | 2026-05-07 | fix(api): drop preDeployCommand until Postgres provisioned (Day 2) |
| `def2cc5` | 2026-05-07 | fix(api): keep README.md in Docker context for hatchling build |
| `ade7f7d` | 2026-05-07 | fix(api): drop BuildKit cache mounts (Railway builder incompatible) |
| `0297838` | 2026-05-07 | fix(api): add id= to Dockerfile uv cache mounts |
| `91626c7` | 2026-05-04 | chore(api): clean ruff debt before Day 1 ship |
| `2a6cd56` | 2026-05-02 | feat(deploy): containerize api + web for Railway, swap Celery→RQ |
| `e9c53cf` | 2026-05-02 | feat(prototype): add Railway-deployable prototype + UX specs |
| `b51fd7c` | Day 0 | feat: scaffold Next.js 15 web app + monorepo plumbing |
| `ea2dc36` | Day 0 | feat: initial backend skeleton (Sprint 1.1) |

---

## Sprint 1.A — API Foundation (Week 1)

| Day | Task | Status | Notes |
|---|---|---|---|
| 1 | Bootstrap FastAPI, settings, Docker, Railway | ✅ | Live at production URL; ruff clean; tests pass; build via Dockerfile (not Nixpacks); Redis ping warning expected |
| 2 | SQLAlchemy 2 async + Alembic + Postgres | 🟡 | Code exists (`database.py`, `alembic/versions/20260502_…_initial.py`); Postgres NOT provisioned on Railway; `preDeployCommand` removed from railway.json (must restore) |
| 3 | Models: User, Audit, AuditFile, Finding, Remedy | 🟡 | Have `user.py`, `audit.py`. **Missing:** `audit_file.py`, `finding.py`, `remedy.py` |
| 4 | Clerk JWT + `/api/v1/me` | 🟡 | `api/v1/auth.py` exists (webhook handler); `/api/v1/me` endpoint unverified; CLERK_* secrets not set on Railway |
| 5 | R2 client + `/api/v1/audits/upload-url` | ⏸️ | No `services/r2.py`; R2_* secrets not set on Railway |
| 6 | `/api/v1/audits` CRUD | 🟡 | `api/v1/audits.py` exists; content unaudited; depends on Day 3 models being complete |
| 7 | Buffer / cleanup / docs | ⏸️ | — |

---

## Sprint 1.B — Vastu Engine + PDF (Week 2) · ⏸️ not started

Knowledge base (`apps/api/knowledge/`), rules engine (`services/vastu_engine.py`), WeasyPrint PDF (`services/pdf.py` + `templates/`), 47-dosha + 89-remedy JSON ports — all blocked on Sprint 1.A close.

---

## Sprint 2 — AI Integration (Week 3) · ⏸️ not started

`src/workers/rq_worker.py` is stubbed (no-op) until Day 20. Anthropic SDK, Claude Vision prompts, pgvector knowledge embedding, SSE stream endpoint, RQ worker — all not started.

---

## Sprint 3.A — Frontend Foundation (Week 4) · ⏸️ not started

Web app has only: default Next.js page, one shadcn `Button`, `/api/health` route. **Missing:** tokens.css, fonts (Fraunces/Inter/Tiro/JetBrains), `next-intl` middleware, Clerk provider, all 9 custom components, Storybook.

**Sprint 3 caveats:**

- Tailwind v4 in `package.json` → tokens wire via `@theme` in CSS, not `tailwind.config.ts` extend (design-system.md §2 needs updating).
- [`apps/web/AGENTS.md`](../apps/web/AGENTS.md) flags Next 16 has breaking changes vs my training data — must read `node_modules/next/dist/docs/` before writing frontend code.

---

## Sprint 3.B / 4 / Beta / Launch · ⏸️ not started

---

## What's pending — full picture

### Immediate (Day 2 – Day 7, Sprint 1.A)

1. **Provision Postgres on Railway** (`railway add -d postgres`) — autosets `DATABASE_URL`
2. **Provision Redis on Railway** (`railway add -d redis`) — autosets `REDIS_URL`
3. **Restore `preDeployCommand: alembic upgrade head`** in `apps/api/railway.json`
4. **Run `alembic upgrade head`** — first migration applies cleanly to Railway Postgres
5. **Verify `/api/v1/health/ready`** returns 200 (db + redis both reachable)
6. **Day 3:** add missing models — `AuditFile`, `Finding`, `Remedy`; new alembic migration
7. **Day 4:** Clerk JWT verification dep + `/api/v1/me` endpoint; set `CLERK_*` secrets on Railway
8. **Day 5:** R2 service module + presigned upload URL endpoint; set `R2_*` secrets
9. **Day 6:** `/api/v1/audits` full CRUD scoped by current_user
10. **Day 7:** test suite, OpenAPI doc cleanup, no TODOs

### Sprint 1.B (Days 8–14)

- Knowledge base structure (`apps/api/knowledge/{zones,doshas,remedies,deities,principles}.json`)
- Port Smita's 47-dosha catalogue + 89-remedy library to JSON
- Rules engine (`services/vastu_engine.py`)
- `/api/v1/audits/{id}/run` endpoint (sync, no AI yet)
- WeasyPrint PDF renderer + Jinja2 templates
- `/api/v1/audits/{id}/pdf` endpoint
- Test fixture: Villa C135 audit must match Smita's manual output

### Sprint 2 (Days 15–21)

- Anthropic SDK + `/api/v1/test/claude` smoke endpoint
- Claude Vision (Sonnet 4.6) zone detection
- pgvector knowledge embedding (47 doshas + 89 remedies)
- Claude Opus reasoning chain
- `/api/v1/audits/{id}/stream` SSE endpoint
- RQ worker service on Railway (sister Dockerfile, different start cmd)
- Per-audit cost logging

### Sprint 3.A (Days 22–25, Foundation)

- Add deps: `next-intl`, `framer-motion`, `recharts`, `d3`, `react-dropzone`, more shadcn
- `tokens.css` from design-system.md
- Tailwind v4 `@theme` wiring
- Fonts via `next/font/google` (Fraunces, Inter, Tiro Devanagari, JetBrains Mono)
- `next-intl` EN/HI/AR locales + middleware
- Clerk provider + middleware
- (Days 26–30) 9 custom components in priority order: SeverityBadge → ConfidenceMeter → TraditionToggle → RemedyCard → ScoreGauge → TerminalLog → UploadZone → Compass → MandalaHeatmap

### Sprint 3.B (Days 31–38, Screens)

- Landing, Audit Wizard, Processing, Audit Report, Dashboard, Branding Settings
- API client, Clerk auth gates, SSE streaming, Stripe portal links
- E2E test: real audit on staging

### Sprint 4 (Days 39–45, Monetization)

- Stripe products/prices/webhook + customer portal
- Tier gating middleware (audit/mo limits, PDF access, API access)
- White-label PDF rendering
- Public API v1 + rate limits + OpenAPI
- Resend transactional emails (5 templates)

### Beta + Launch (Weeks 7–8)

- 10 Dubai consultants + 5 power users → 50 audits → bug bash
- Product Hunt launch
- MENA real-estate outreach
- Closed-beta → public MVP

### Cross-cutting / not yet wired

- Auto-deploy from `main` (currently using `railway up` from CLI; should be GitHub-triggered)
- Web service on Railway (`apps/web/` Dockerfile ready, service not created)
- Custom domain (`vastuaudit.ai` → Railway)
- Sentry DSN, PostHog API key
- DB backup cron to R2 (launch checklist)

---

## Verification gaps (current)

- [x] ~~`uv sync` runs cleanly~~
- [x] ~~`ruff check` + `ruff format --check` pass~~
- [x] ~~`pytest` passes~~ (2/2)
- [x] ~~Railway service exists for `apps/api/`~~ (`vastuaudit-api`)
- [x] ~~Production `/api/v1/health` returns 200 with correct JSON~~
- [x] ~~Production `env=production`~~
- [x] ~~Railway logs show clean startup (only expected redis warning)~~
- [ ] Postgres add-on provisioned + `DATABASE_URL` set
- [ ] Redis add-on provisioned + `REDIS_URL` set
- [ ] Alembic migration runs on Railway Postgres
- [ ] `/api/v1/health/ready` returns 200
- [ ] All Sprint 1.A endpoints exist and have tests
- [ ] GitHub `main` branch → Railway auto-deploy is wired
- [ ] Railway service exists for `apps/web/`
- [ ] Custom domain configured

---

## Next 3 actions

1. **Lift Day 2 gate** — Manish confirms ready to proceed past Day 1.
2. **Provision Postgres + Redis** on Railway (`railway add -d postgres && railway add -d redis`), set `DATABASE_URL`/`REDIS_URL` (auto), restore `preDeployCommand` in railway.json, redeploy.
3. **Run first migration end-to-end** — verify alembic migration runs on Railway Postgres, `/api/v1/health/ready` returns 200.

---

## Resolved decisions

- ✅ **Spec/code layout drift** (2026-05-04) — `apps/api/CLAUDE.md` updated to match the existing flatter scaffold; reality won on every row (`config.py`, `api/v1/`, `database.py + models/`, RQ over arq, `api/v1/auth.py` over `auth/clerk.py`). No code refactor required.
- ✅ **Workflow** (2026-05-04) — deploy-only via Railway. Local Docker abandoned. Verification against production URL.
- ✅ **Railway project name** (2026-05-06) — `vastuaudit` (lowercase). Two duplicate `VastuAudit.ai` projects deleted.

---

## Parked / orphan files (cleaned 2026-05-03)

- ~~repo-root `Dockerfile`, `.dockerignore`, `compose.yaml`, `compose.debug.yaml`~~ — VS Code "Add Docker Files" boilerplate, deleted (untracked, never committed). Real Docker setup is per-service under `apps/api/Dockerfile` and `apps/web/Dockerfile`.
