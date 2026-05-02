# Memory — VastuAudit.ai

_Last updated: 2026-05-02_

## Memory
<!-- Persistent product decisions and context. Only remove or change if Manish asks. -->

### Product
- **Name:** VastuAudit.ai
- **Owner entity:** Qadr AI Agency Dubai
- **Markets:** MENA + APAC
- **Repo location:** `~/iCloud/CodeOS/VastuAudit.ai/` (this folder is both the live repo and the Cowork strategy workspace)

### Tech Stack (locked)
- API: FastAPI (Python 3.11), SQLAlchemy 2 async, Pydantic v2
- Web: Next.js 15, TypeScript, Tailwind, shadcn/ui
- AI: Claude Sonnet 4.6 (vision), Claude Opus 4.7 (reasoning)
- DB: PostgreSQL + pgvector
- Cache/Queue: Redis
- Storage: Cloudflare R2
- Auth: Clerk · Payments: Stripe · Email: Resend
- PDF: WeasyPrint + Jinja2

### Deployment Decision (2026-05-02 — locked)
- **Single-platform Railway.app deploy.** Everything (api + worker + web + Postgres + Redis) on Railway.
- Source code: GitHub.
- Earlier plan was Railway (api) + Vercel (web). Consolidated to Railway-only for simpler ops.
- Manish is on Railway Hobby plan, has one existing project (`nse-trading`).

### Design System (decided)
- Theme: Dark default ("Cosmic Dashboard")
- Palette: Deep navy + gold + sand accents
- Typography: Fraunces (display) + Inter (UI) + Tiro Devanagari (Sanskrit) + JetBrains Mono (terminal log)
- Severity tiers: 4 (mild → severe) — must match Smita's framework
- Score scale: /100 primary (e.g., 72/100), /10 secondary
- Mandala grid: 9×9 for consumer view, 16-pada for Pro/Consultant deep-dive

### Critical UX Decisions Made
1. Compass-first intake (rotation-calibrated)
2. Live AI reasoning stream during 60s processing
3. Confidence % shown per finding
4. AED-priced remedies inline
5. Multi-tradition toggle (North Indian / South Indian / Islamic geomancy / Feng Shui) — non-negotiable for MENA
6. White-label (Consultant tier): logo + accent + typography + signature/seal + language pack

### Known Issues to Fix in v2 Mockups
- Typo "Gadr AI" → should be "Qadr AI"
- Score scale inconsistency (72/100 mockup vs Smita's /10 framework) — locked to /100
- Side panel zone duplicates (placeholder bug)
- Real brand "AL BARARI REALTY" used in mockup — replace with "Falcon Realty Demo"
- 3-tier color coding doesn't match 4-tier severity model
- No mobile variant shown
- No RTL Arabic variant shown
- No empty state for first-run users

### Sprint Roadmap (locked)
- **S1:** Skeleton, schema, R2 upload, Vastu engine v1, PDF, Railway deploy
- **S2:** Claude Vision plan analysis, reasoning remedies, knowledge base, pgvector
- **S3:** Frontend — landing, Clerk auth, audit wizard, results, dashboard
- **S4:** Stripe tiers, customer portal, white-label PDF, public API

### Pricing (locked)
- Free $0 / 1 audit / no PDF
- Pro $19 / 10 audits / full PDF
- Consultant $99 / unlimited / white-label + API
- Enterprise custom / embed

### Live Prototype
- Static HTML prototype: `ux/prototype.html` and `prototype-deploy/index.html` (identical)
- Deployable to Railway via the prototype-deploy folder (see `prototype-deploy/README.md`)
- Purpose: validate UX with stakeholders before Claude Code ships the real Next.js build
