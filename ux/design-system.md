# VastuAudit.ai — Design System v1.0

**Status:** Locked for Sprint 3 frontend build
**Owner:** Qadr AI Agency Dubai
**Last updated:** 2026-05-02

---

## 1. Brand North Star

> "A Bloomberg-grade analytics tool that respects tradition."

Modern, calm, premium. Never mystical. Never decorative. Every pixel earns its place.

**Voice:** Confident, clear, never alarming. Vastu findings are presented as analysis, not prophecy.

---

## 2. Design Tokens

All tokens live in `apps/web/src/styles/tokens.css` as CSS custom properties and are mapped to Tailwind via `tailwind.config.ts` extend block. **Never hardcode colors or spacing in components.**

### 2.1 Color — Surface (Dark theme, default)

| Token | Hex | Use |
|---|---|---|
| `--color-bg-base` | `#0A0E1A` | Page background |
| `--color-bg-elevated` | `#11172A` | Section background |
| `--color-bg-card` | `#1A2138` | Cards, panels |
| `--color-bg-overlay` | `rgba(10, 14, 26, 0.85)` | Modal scrim |
| `--color-border-subtle` | `#2A3148` | Card borders |
| `--color-border-strong` | `#3B4566` | Active/focus borders |

### 2.2 Color — Text

| Token | Hex | Use |
|---|---|---|
| `--color-text-primary` | `#F5F1E8` | Body, headlines |
| `--color-text-secondary` | `#B8B0A0` | Labels, captions |
| `--color-text-muted` | `#6E6A60` | Disabled, placeholder |
| `--color-text-inverse` | `#0A0E1A` | On gold/light surfaces |

### 2.3 Color — Brand

| Token | Hex | Use |
|---|---|---|
| `--color-gold-primary` | `#D4A857` | Primary CTA, score gauge |
| `--color-gold-soft` | `#E8C988` | Hover, glow |
| `--color-gold-deep` | `#A8843E` | Pressed state |
| `--color-sand-base` | `#C9B89A` | Secondary accents |
| `--color-sand-deep` | `#8B7A5C` | Borders on light surfaces |

### 2.4 Color — Severity (4-tier, matches Smita's framework)

| Token | Hex | Severity | Use |
|---|---|---|---|
| `--color-severity-1` | `#4ADE80` | Mild | Auspicious zones |
| `--color-severity-2` | `#FACC15` | Moderate | Watchlist zones |
| `--color-severity-3` | `#FB923C` | Significant | Priority remedies |
| `--color-severity-4` | `#EF4444` | Severe | Strong remedies needed |

**Accessibility rule:** Never communicate severity by color alone. Always pair with an icon or pattern (e.g., 🟢 dot, 🟡 hatched, 🟠 striped, 🔴 solid + alert glyph).

### 2.5 Color — Confidence

| Token | Hex (rgba) | Range |
|---|---|---|
| `--color-confidence-high` | `rgba(74, 222, 128, 0.9)` | 80–100% |
| `--color-confidence-mid` | `rgba(212, 168, 87, 0.9)` | 60–79% |
| `--color-confidence-low` | `rgba(251, 146, 60, 0.9)` | <60% |

---

## 3. Typography

### 3.1 Font Stack

| Role | Font | Source | Weights |
|---|---|---|---|
| Display | **Fraunces** | Google Fonts (variable) | 300, 500, 600, 700 |
| UI | **Inter** | Google Fonts (variable) | 400, 500, 600, 700 |
| Sanskrit | **Tiro Devanagari Hindi** | Google Fonts | 400 |
| Mono | **JetBrains Mono** | Google Fonts | 400, 500 |

Load via `next/font` with `display: 'swap'` and `subsets: ['latin', 'devanagari']`.

### 3.2 Type Scale

| Token | Font | Size / Line | Weight | Use |
|---|---|---|---|---|
| `text-display-xl` | Fraunces | 56 / 64 | 600 | Hero score numbers |
| `text-display-l` | Fraunces | 40 / 48 | 500 | Section heroes |
| `text-h1` | Inter | 32 / 40 | 600 | Page titles |
| `text-h2` | Inter | 24 / 32 | 600 | Section titles |
| `text-h3` | Inter | 18 / 26 | 600 | Card titles |
| `text-body-l` | Inter | 16 / 24 | 400 | Default body |
| `text-body` | Inter | 14 / 22 | 400 | Compact body |
| `text-caption` | Inter | 12 / 16 | 500 | Labels (track 0.04em) |
| `text-mono` | JetBrains | 13 / 20 | 400 | Terminal log |
| `text-sanskrit` | Tiro Dev. | 16 / 24 | 400 | Vastu terms |

---

## 4. Spacing & Layout

- Base unit: 4px
- Scale: `0, 1, 2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96` (multiplied by 4px)
- Container max-width: `1280px` (xl), `1440px` (2xl)
- Gutter: 24px (mobile), 32px (tablet), 48px (desktop)
- Use Tailwind's default spacing scale — do not invent new values.

---

## 5. Radius

| Token | Value | Use |
|---|---|---|
| `radius-sm` | 4px | Chips, badges |
| `radius-md` | 8px | Inputs, buttons |
| `radius-lg` | 12px | Cards |
| `radius-xl` | 20px | Modals, hero panels |
| `radius-full` | 9999px | Compass, score gauge frame |

---

## 6. Shadow & Glow

Dark theme = subtle glow over heavy drop shadow.

| Token | Value | Use |
|---|---|---|
| `shadow-glow-gold` | `0 0 24px rgba(212, 168, 87, 0.15)` | Active CTA, focus |
| `shadow-glow-severity-3` | `0 0 32px rgba(251, 146, 60, 0.25)` | Active processing zone |
| `shadow-card` | `0 4px 24px rgba(0, 0, 0, 0.4)` | Default card |
| `shadow-elevated` | `0 12px 48px rgba(0, 0, 0, 0.6)` | Modals |

---

## 7. Motion

**Tone: calm, deliberate, never bouncy.** Vastu is serious; the UI moves with intent.

| Pattern | Duration | Easing |
|---|---|---|
| Default transition | 280ms | `cubic-bezier(0.32, 0.72, 0.24, 1.0)` |
| Reveal/entrance | 600ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Compass rotation | 800ms | `ease-in-out` |
| Score counter reveal | 1400ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| Terminal stream | 24ms/char | linear |
| Heatmap zone fade-in | 320ms (staggered 60ms) | ease-out |

Use **Framer Motion** for orchestration. Respect `prefers-reduced-motion` — fall back to instant transitions.

---

## 8. Component Inventory

### 8.1 Base (shadcn/ui)
Use shadcn primitives unmodified for: Button, Input, Select, Dialog, Tabs, Tooltip, Popover, Toast, Sheet, Card, Badge, Separator. Override only via tokens in CSS.

### 8.2 Custom Components (build from scratch)

| Component | Path | Purpose |
|---|---|---|
| `<Compass />` | `components/compass/Compass.tsx` | Rotation-calibrated compass overlay on uploaded plan |
| `<MandalaHeatmap />` | `components/mandala/MandalaHeatmap.tsx` | 9×9 (or 16-pada) zone overlay, click → drill-down |
| `<ScoreGauge />` | `components/score/ScoreGauge.tsx` | Radial gauge, animated counter, 0–100 |
| `<TerminalLog />` | `components/processing/TerminalLog.tsx` | Streaming AI reasoning, typewriter render |
| `<SeverityBadge />` | `components/severity/SeverityBadge.tsx` | Tier-based badge, icon + color + label |
| `<ConfidenceMeter />` | `components/confidence/ConfidenceMeter.tsx` | % bar with band classification |
| `<RemedyCard />` | `components/remedies/RemedyCard.tsx` | Title, severity, AED price, action CTA |
| `<TraditionToggle />` | `components/tradition/TraditionToggle.tsx` | Switch: North Indian / South Indian / Islamic / Feng Shui |
| `<UploadZone />` | `components/upload/UploadZone.tsx` | Drag-drop + compass icon |

### 8.3 Component Patterns

**Compass:**
- Pure SVG + Framer Motion `useMotionValue` for rotation
- Drag handle + keyboard arrow controls
- Snaps to 15° increments unless Shift held
- Emits `onCalibrate(degrees)` on commit

**MandalaHeatmap:**
- D3 + SVG (not canvas — needs click targets per zone)
- Each zone: severity color + icon + tooltip with zone name
- Click → opens drill-down panel with details + remedies
- Hover: subtle gold glow on zone border

**ScoreGauge:**
- Recharts `RadialBarChart` base, custom needle SVG
- Animated counter (0 → score) over 1400ms
- Color of arc transitions through severity bands as it fills

**TerminalLog:**
- Receives SSE stream from `/api/v1/audits/:id/stream`
- Typewriter render at 24ms/char
- Each new line: prefixed with `[####]`, status icon at end
- Auto-scrolls to bottom; user can pin scroll

---

## 9. Multi-Tradition Toggle

Top-right of audit report. Switching tradition:
- Re-renders heatmap with that tradition's zone definitions
- Re-fetches remedies tagged for that tradition
- Persists user choice in localStorage + Clerk user metadata

Order: **North Indian (default)** → South Indian → Islamic Geomancy → Feng Shui (cross-reference only).

---

## 10. Internationalization & RTL

- Use `next-intl` for translations
- Languages at launch: **EN (default), HI, AR**
- AR triggers RTL (`dir="rtl"` on `<html>`)
- Compass and MandalaHeatmap **must** flip directional logic in RTL (West ↔ East labels swap visually but not semantically)
- All custom components must be tested in both LTR and RTL

---

## 11. Accessibility (WCAG AA minimum)

- Color contrast: text on `--color-bg-card` must hit 4.5:1 (Inter 14+) or 3:1 (Inter 18+ semibold)
- All interactive elements: visible focus ring (2px `--color-gold-primary`, offset 2px)
- Severity communicated by icon + color (never color alone)
- All custom components: keyboard navigable
- Compass + Mandala: provide text alternative listing zones and findings
- `prefers-reduced-motion`: skip all entrance animations, keep only state-change transitions

---

## 12. Mobile (≤768px)

- Wizard: single-column, sticky compass at bottom
- Processing: full-screen, terminal log scrolls inline
- Audit Report: tabbed (Overview / Floor Plan / Doshas / Remedies / Action Plan); zone drill-down opens as bottom sheet
- Consultant Dashboard: collapsible sidebar → bottom tab bar

Touch targets minimum 44×44px.

---

## 13. Performance Budgets

| Metric | Budget | Tool |
|---|---|---|
| LCP (mobile 4G) | < 2.5s | Vercel Speed Insights |
| TBT | < 200ms | Lighthouse |
| Bundle (initial JS, gzipped) | < 180KB | `next build` analyze |
| Image (hero) | < 80KB AVIF | next/image |
| Compass component | < 12KB gzipped | Bundle analyzer |

Lazy-load: MandalaHeatmap (only on results screen), Recharts (only on results screen), Framer Motion (split per route).

---

## 14. Anti-Patterns — Reject in PR Review

- ❌ Hardcoded hex colors (must use tokens)
- ❌ Tailwind arbitrary values for spacing (`p-[13px]`) — use scale
- ❌ Decorative emojis in production UI (we're not a horoscope app)
- ❌ Religious imagery, deity illustrations, om symbols, mandala flourishes outside the data heatmap
- ❌ Bouncy spring animations (this is not Notion)
- ❌ Generic stock photos of homes
- ❌ "Auspicious" / "inauspicious" without supporting data — every claim links to a principle
- ❌ Color-only severity indication
- ❌ Custom components when shadcn/ui has it
