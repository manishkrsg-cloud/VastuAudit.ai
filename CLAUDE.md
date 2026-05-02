# VASTUAUDIT.AI — PROJECT WORKSPACE + REPO ROOT

**Owner:** Manish Kumar (Qadr AI Agency Dubai)
**Trading name:** VastuAudit.ai by Qadr AI
**Created:** 2026-05-02
**Location:** ~/iCloud/CodeOS/VastuAudit.ai (live repo)

---

## Identity & Purpose

This folder is **both** the live code repository (Claude Code builds inside `apps/`, `packages/`) **and** the Cowork strategy workspace (UX specs, decisions, briefs in `ux/`). The two coexist in one place so Claude Code never has to look elsewhere.

**Tone in this folder:** sharp, structured, real-world. No generic SaaS advice — every recommendation must be implementable in the existing tech stack and tied to a sprint.

---

## Product Snapshot

- **Tagline:** "Professional Vastu audits in 60 seconds. AI-powered. Consultant-grade."
- **Markets:** MENA + APAC (property buyers, builders, consultants)
- **Stack:** FastAPI + Next.js 15 + shadcn/ui + Tailwind + Claude Sonnet 4.6 (vision) + Claude Opus 4.7 (reasoning) + Postgres + pgvector + Redis + R2 + Clerk + Stripe + Resend + WeasyPrint
- **Deploy:** **Railway (single platform — api + worker + web + db + redis)**. GitHub for source.
- **Repo structure:** pnpm + turbo monorepo

## Pricing Tiers

| Tier | Price | Audits/mo | Key features |
|---|---|---|---|
| Free | $0 | 1 | Basic report, no PDF |
| Pro | $19/mo | 10 | Full PDF, all remedies |
| Consultant | $99/mo | Unlimited | White-label, branding, API |
| Enterprise | Custom | Custom | Embed in real estate platforms |

---

## Folder Structure

```
VastuAudit.ai/                      (repo root + Cowork workspace)
├── CLAUDE.md                        (this file — read at session start)
├── MEMORY.md                        (persistent decisions + context)
├── apps/                            (Claude Code builds here)
│   ├── api/                         FastAPI backend
│   └── web/                         Next.js 15 frontend
├── packages/
│   └── shared-types/                TS types shared between api/web
├── ux/                              (Cowork strategy outputs)
│   ├── design-system.md             Tokens, typography, components
│   ├── handoff-to-claude-code.md    Build brief Claude Code reads
│   └── prototype.html               Live HTML preview of all 4 screens
└── prototype-deploy/                Railway-deployable static prototype
    ├── index.html
    ├── package.json
    ├── railway.json
    ├── .gitignore
    └── README.md                    Step-by-step Railway deploy guide
```

---

## Connection to Smita's Workspace

Smita Singh's Vastu Consultant Workspace (in `~/iCloud/Cowork OS/SMITA_SINGH_VASTU_CONSULTANT/`) is the **methodology source of truth.** Her v2.0 audit framework, 47-dosha catalogue, 89-remedy library, severity tiers, and 16-pada zone system are the seed for `apps/api/knowledge/` here.

**Sync rule:** if a Vastu rule changes in Smita's workspace, flag it for sync to `apps/api/knowledge/`. The two must never diverge.

---

## How Claude Code Should Use This Folder

Before any frontend work in `apps/web/`:
1. **Read** `ux/design-system.md` (tokens, typography, 9 custom components)
2. **Read** `ux/handoff-to-claude-code.md` (build order, DOD, screen specs)
3. **Reference** `ux/prototype.html` for visual ground truth

Before any backend work in `apps/api/`:
1. **Read** `MEMORY.md` for stack and architecture decisions
2. **Reference** Smita's workspace for Vastu methodology

---

## MEMORY SYSTEM

- Read MEMORY.md silently at session start
- Memory is user-triggered only — never auto-write
- All entries persistent — only Manish can ask to remove
- Flag contradictions

---

## Operating Principles

1. **Every UX decision traces to a sprint** — if it can't be built in S1–S4, it's a v2 idea.
2. **Knowledge base sync** — UI tier counts (4 severity, /100 score) must match backend schema.
3. **Single-platform deploy** — everything on Railway. No Vercel split.
4. **Output is self-contained** — every spec must work without re-asking.
5. **No fluff** — Manish skims fast; lead with the answer.
