# Handoff to Claude Code — Frontend Build Brief

**Read this file at the start of every Sprint 3 frontend session.**
**Companion file:** `design-system.md` (in same folder) — the source of truth for tokens and components.

---

## 0. Mission

Build the VastuAudit.ai frontend in `apps/web/` so that a non-technical property buyer in Dubai or Mumbai can upload a floor plan, calibrate North, and receive a consultant-grade audit report in under 60 seconds — and a real-estate consultant can white-label that report and resell it.

If you ship a screen that looks like every other AI SaaS, you've failed. The product looks unmistakably **like a financial analytics tool that happens to know Vastu** — not a horoscope site, not a temple website.

---

## 1. Operating Rules — Always Follow

1. **Read `design-system.md` before writing any component.** Every color, spacing, radius, and animation must come from a token. No hardcoded values.
2. **shadcn/ui first.** If shadcn has the primitive, use it. Only build custom for the 9 components listed in `design-system.md` §8.2.
3. **TypeScript strict mode.** No `any`. Every prop typed. Use the shared types from `packages/shared-types`.
4. **Server Components by default.** Use Client Components only when you need state, effects, or interactivity. Mark with `'use client'` at the top.
5. **Accessibility is not optional.** Keyboard-navigable, focus-visible, aria-labeled, color-contrast-passing. WCAG AA minimum.
6. **Mobile-first CSS.** Default styles target mobile; use `md:` and `lg:` to scale up.
7. **Test in EN and AR (RTL).** Every screen must look correct in both. Use `next-intl` from day 1 — don't bolt it on later.
8. **No comments in JSX unless complex.** Code reads itself.
9. **Commit messages: `feat(scope): description` or `fix(scope): description`.** Keep scopes consistent (e.g., `wizard`, `report`, `compass`).

---

## 2. File & Folder Structure (apps/web)

```
apps/web/src/
├── app/
│   ├── (marketing)/
│   │   ├── page.tsx                    # Landing
│   │   ├── pricing/page.tsx
│   │   └── layout.tsx
│   ├── (app)/
│   │   ├── dashboard/page.tsx          # My Audits
│   │   ├── audit/
│   │   │   ├── new/page.tsx            # Wizard
│   │   │   ├── [id]/processing/page.tsx
│   │   │   └── [id]/page.tsx           # Report
│   │   ├── settings/
│   │   │   ├── branding/page.tsx       # Consultant tier
│   │   │   └── billing/page.tsx
│   │   └── layout.tsx
│   ├── api/                            # Edge handlers only
│   ├── layout.tsx                      # Root, fonts, providers
│   └── globals.css
├── components/
│   ├── ui/                             # shadcn/ui (generated)
│   ├── compass/Compass.tsx
│   ├── mandala/MandalaHeatmap.tsx
│   ├── score/ScoreGauge.tsx
│   ├── processing/TerminalLog.tsx
│   ├── severity/SeverityBadge.tsx
│   ├── confidence/ConfidenceMeter.tsx
│   ├── remedies/RemedyCard.tsx
│   ├── tradition/TraditionToggle.tsx
│   ├── upload/UploadZone.tsx
│   └── shared/                         # Layout, nav, footer
├── lib/
│   ├── api.ts                          # API client (typed)
│   ├── streaming.ts                    # SSE helpers
│   └── utils.ts                        # cn(), formatters
├── hooks/                              # Custom React hooks
├── styles/
│   └── tokens.css                      # CSS custom properties
└── i18n/
    ├── en.json
    ├── hi.json
    └── ar.json
```

---

## 3. Build Order — Sprint 3

Build in this order. Don't skip ahead. Each step has a clear DOD.

### Step 1 — Foundation (Day 1–2)
1. Install dependencies: `next-intl`, `framer-motion`, `recharts`, `d3`, `lucide-react`, `react-dropzone`, `zod`, `@tanstack/react-query`
2. Set up shadcn/ui with custom theme: `pnpm dlx shadcn-ui@latest init`
3. Create `tokens.css` with all tokens from `design-system.md` §2
4. Configure Tailwind to consume tokens (extend `theme.colors`, `theme.fontFamily`, `theme.borderRadius`, `theme.boxShadow`)
5. Load fonts via `next/font/google` in root layout
6. Set up `next-intl` with EN/HI/AR locales and middleware
7. Set up Clerk provider and middleware

**DOD:** Empty homepage renders with correct fonts, default dark theme, lang switcher works.

### Step 2 — Custom Components (Day 3–6)
Build in this order, each with Storybook entry + visual smoke test:
1. `<SeverityBadge />` (simplest, validates token pipeline)
2. `<ConfidenceMeter />`
3. `<TraditionToggle />`
4. `<RemedyCard />`
5. `<ScoreGauge />` (uses Recharts)
6. `<TerminalLog />` (uses Framer Motion)
7. `<UploadZone />` (uses react-dropzone)
8. `<Compass />` ⚠️ critical — see §6
9. `<MandalaHeatmap />` ⚠️ critical — see §7

**DOD:** All 9 components in Storybook, RTL-tested, keyboard-tested, screenshot regression captured.

### Step 3 — Screens (Day 7–10)
1. **Landing page** (`/`) — hero, value prop, "Try free" CTA
2. **Audit Wizard** (`/audit/new`) — upload + calibrate + form
3. **Processing** (`/audit/[id]/processing`) — terminal stream, redirects on completion
4. **Audit Report** (`/audit/[id]`) — score gauge, mandala heatmap, drill-down, remedies, export
5. **Dashboard** (`/dashboard`) — list of past audits, empty state
6. **Branding Settings** (`/settings/branding`) — Consultant tier only

**DOD:** All screens rendered with mock data, mobile + desktop + RTL tested.

### Step 4 — Wiring (Day 11–12)
1. Connect API client (`lib/api.ts`) to FastAPI endpoints
2. Wire Clerk auth gates
3. Wire SSE for processing stream
4. Wire Stripe portal links
5. End-to-end test: upload → process → report → PDF download

**DOD:** Real audit can be run end-to-end on staging.

---

## 4. Definition of Done — Per Screen

A screen is "done" when:
- ✅ Renders correctly desktop + tablet + mobile
- ✅ Renders correctly LTR + RTL
- ✅ Renders correctly dark + (future) light theme
- ✅ All text comes from i18n files (no hardcoded strings)
- ✅ All colors/spacing from tokens (no magic values)
- ✅ Keyboard navigable (Tab, Shift-Tab, Enter, Escape)
- ✅ Screen reader tested (VoiceOver or NVDA)
- ✅ Loading state, empty state, error state all handled
- ✅ Lighthouse score: Performance 90+, Accessibility 95+
- ✅ No console errors or warnings
- ✅ TypeScript: zero errors, strict mode
- ✅ Visual regression snapshot captured

---

## 5. The 4 Hero Screens — Spec Highlights

### 5.1 Audit Wizard (`/audit/new`)

**Layout:** 2-column desktop (form left, compass overlay right). Single-column mobile.

**Behavior:**
- Drag-drop or click upload → image preview appears in compass overlay area
- Compass rose overlays the plan; user rotates to align North
- Form: Property Type (select), Facing Direction (auto-set from compass, editable), Tradition toggle
- "Next" button disabled until upload complete + compass calibrated

**Edge cases:**
- File too large (>10MB) → toast + retry
- Unsupported format → toast with allowed list
- User skips compass calibration → modal: "We'll auto-detect, but accuracy improves with your input"

### 5.2 Processing (`/audit/[id]/processing`)

**Layout:** Full-screen, centered. AI x-ray scan effect on the uploaded image. Terminal log below.

**Behavior:**
- Subscribe to SSE stream from `/api/v1/audits/:id/stream`
- Each event = new line in terminal log, typewriter render
- Stages: `LOADING ARCHITECTURE` → `ANALYZING ZONES` → `IDENTIFYING DOSHAS` → `GENERATING REMEDIES` → `FINALIZING SCORE`
- On completion, redirect to `/audit/[id]` with smooth crossfade
- "Powered by Qadr AI Agency Dubai" footer (pin: not "Gadr")

**Edge cases:**
- Stream timeout (>90s) → fallback polling, surface message "Taking longer than usual..."
- Stream error → retry button + escalation to email support

### 5.3 Audit Report (`/audit/[id]`)

**Layout:**
- **Top bar:** Score gauge, overall verdict, Tradition toggle, Download PDF (gated by tier), Share link (gated)
- **Left rail:** Zone list (9 directions + center), filterable by severity
- **Center:** MandalaHeatmap on floor plan, click zone → drill-down
- **Right rail:** Selected zone details — issue, severity, confidence %, list of remedies with AED price + add-to-plan CTA

**Behavior:**
- Score animates from 0 to value on load
- Heatmap zones fade in staggered (60ms each)
- Click zone → smooth scroll right rail into focus
- Tradition toggle → re-render heatmap with that tradition's zone math

**Tier gating:**
- Free: see report, see ~3 remedies, no PDF
- Pro: full PDF, all remedies, save audit
- Consultant: all of Pro + white-label PDF + share link with own branding

### 5.4 Branding Settings (`/settings/branding`) — Consultant tier

**Layout:** Form left, live PDF preview right.

**Behavior:**
- Logo upload → R2, displayed in preview header
- Accent color picker (limited to a curated palette to avoid ugly outputs — provide 12 brand-safe options)
- Typography preset (3 choices: Modern / Classical / Editorial)
- Custom header text (max 80 chars)
- Digital signature/seal upload (PNG, max 1MB)
- PDF watermark toggle
- Language preset (EN / AR / HI / Auto-match audit)
- "Save & set as default" button

**Tier gate:** Block view + show upgrade modal if user is Free/Pro.

---

## 6. The Compass Component — Detailed Brief

This is the product's signature component. It must feel premium.

**Tech:** Pure SVG + Framer Motion. No third-party compass libraries.

**Visual:**
- Outer ring: thin gold stroke, dotted at cardinal points
- Inner rose: 8-point star, gold, with N/E/S/W labels in Inter 600
- Center: small navigation dot
- When inactive: 60% opacity, subtle pulse animation
- When active (drag): full opacity, gold glow

**Interaction:**
- Drag with mouse or touch → rotates the rose
- Keyboard: Arrow keys rotate by 5°, Shift-Arrow by 1°
- Snaps to 15° increments unless Shift held during release
- Double-click center: reset to 0°
- Emits `onCalibrate(degrees: number)` on commit

**Layered over uploaded plan:**
- The plan image stays fixed; the compass rotates above it
- Semi-transparent gold overlay shows the calibration arc
- Live readout below: "North aligned at 47°"

**Accessibility:**
- `role="slider"`, `aria-valuemin={0}`, `aria-valuemax={359}`, `aria-valuenow={degrees}`
- Text alternative: input field where user can type degrees directly

---

## 7. The MandalaHeatmap Component — Detailed Brief

**Tech:** D3 + SVG. Not canvas — we need clickable zones.

**Visual:**
- 9×9 grid (consumer view) overlays the floor plan at 50% opacity
- Each cell colored by severity token
- Cell border: 1px `--color-border-subtle`
- Hover: cell border becomes `--color-gold-primary` + subtle glow
- Selected cell: gold border, drops opacity of unselected cells to 30%

**Toggle to 16-pada (Pro/Consultant):**
- Recomputes grid as 4×4 macro-zones, each subdivided into pada
- Available via icon toggle top-right of heatmap

**Interaction:**
- Click cell → opens right-rail drill-down with smooth animation
- Hover cell → tooltip with zone name + dominant element + severity label

**Accessibility:**
- Each cell is a `<button>` with aria-label like "Zone South-West, severity Significant, 2 remedies"
- Listed in DOM order N → NE → E → SE → S → SW → W → NW → Center
- Provide text-list alternative below the heatmap

---

## 8. AI Streaming — Implementation

The processing screen consumes a Server-Sent Events stream from FastAPI.

**Endpoint:** `GET /api/v1/audits/:id/stream` (SSE, returns `text/event-stream`)

**Event format:**
```
event: stage
data: {"stage": "ANALYZING_ZONES", "progress": 0.4}

event: reasoning
data: {"text": "South-east quadrant aligned with Agni element..."}

event: finding
data: {"zone": "SW", "severity": 3, "confidence": 0.87}

event: complete
data: {"audit_id": "abc123", "score": 72}
```

**Client implementation:**
- Use native `EventSource` (don't add a library)
- Buffer reasoning text, render via TerminalLog typewriter
- On `complete` event, prefetch the report page, then `router.push()`
- On error, show retry button after 3s

---

## 9. Critical UX Rules — Don't Break These

1. **Score: /100 primary, /10 secondary.** Show "72/100" prominently; "8.0/10" as smaller secondary label.
2. **Severity is 4-tier.** Mild / Moderate / Significant / Severe. Match Smita's framework. Never collapse to 3.
3. **Every finding shows confidence %.** No exceptions. Trust collapses without it.
4. **Every remedy shows AED cost.** Format: `AED 250 – 450`. Always a range, not a single number.
5. **Tradition toggle is always visible** on report screens. Default North Indian.
6. **No fearmongering copy.** "Severe" → "Strong remedies recommended." Never "danger," "bad luck," "avoid this property."
7. **PDF preview is real, not lorem ipsum.** Render actual data in the preview pane.
8. **"Powered by Qadr AI Agency Dubai"** — exact spelling. Not Gadr. Not Quadr.
9. **No religious imagery** outside the data heatmap. No deities, no om symbols, no temples in marketing.
10. **Replace "AL BARARI REALTY"** in any mockup with `Falcon Realty Demo` until we have written permission.

---

## 10. What to Ask Manish — Don't Assume

Before each screen, if any of these are unclear, **ask**:
- Tier-gating behavior for the screen
- Copy variations for AR / HI
- Empty state messaging
- What happens on payment failure
- Whether a feature is S3 or pushed to S4

Ask in the existing Cowork session, not in the code repo.

---

## 11. References

- `design-system.md` — tokens, typography, components (this folder)
- `../../SMITA_SINGH_VASTU_CONSULTANT/CLAUDE.md` — methodology source of truth (severity tiers, doshas, remedies)
- `apps/api/knowledge/` (in repo) — backend Vastu rules engine
- `docs/vastu_methodology.md` (in repo) — multi-traditional rules

---

## 12. When You're Stuck

1. Re-read `design-system.md` — the answer is usually a token you missed.
2. Check shadcn/ui — they probably have the primitive.
3. Check `MEMORY.md` for past decisions.
4. Ask Manish, with a specific question and 2 proposed options. Don't ask open-ended.

---

**Last word:** This product is for a Dubai property buyer who is anxious about a multi-million dirham decision and a Mumbai consultant who needs to look like a pro. Treat them with respect. Don't ship anything that looks like a horoscope app.
