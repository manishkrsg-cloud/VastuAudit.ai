# VastuAudit.ai — Prototype Deploy (Railway)

A self-contained static-site deployment of the VastuAudit.ai design prototype. Pushes to Railway in under 5 minutes. Use to validate the UX with stakeholders before the real Next.js app ships.

---

## What's in this folder

| File | Purpose |
|---|---|
| `index.html` | The full 4-screen prototype (Wizard, Processing, Report, Branding) |
| `package.json` | Defines `start` script using `serve` static server |
| `railway.json` | Railway build/deploy config (Nixpacks builder, port binding) |
| `.gitignore` | Standard Node ignores |
| `README.md` | This file |

---

## Deploy to Railway — Two paths

### Path A — Same repo (recommended)

If your VastuAudit.ai monorepo is already on GitHub and connected to Railway, add a **new service** that points to this `prototype-deploy/` subdirectory. Best for keeping prototype + production in one place.

**Steps:**

1. **Commit + push** this folder to your GitHub repo:
   ```bash
   cd ~/iCloud/CodeOS/VastuAudit.ai
   git add prototype-deploy/
   git commit -m "feat(prototype): add Railway-deployable static prototype"
   git push origin main
   ```

2. **Open Railway** → your VastuAudit.ai project → **+ New** → **GitHub Repo** → pick the same repo.

3. **Configure the service:**
   - **Service name:** `vastuaudit-prototype`
   - **Settings → Source → Root Directory:** `prototype-deploy`
   - **Settings → Build → Builder:** Nixpacks (default)
   - **Settings → Networking → Generate Domain** → click to get a `*.up.railway.app` URL
   - **Settings → Deploy → Start Command:** (leave default — Railway reads `package.json` start script)

4. **Trigger first deploy:** Railway auto-builds on the push. Watch the Deploy logs.

5. **Open the live URL** (from Networking) — should show the prototype.

---

### Path B — Standalone repo (cleanest)

Better if the prototype is throwaway and you don't want it cluttering the production repo.

**Steps:**

1. **Create new GitHub repo** `vastuaudit-prototype`:
   - Go to github.com/new
   - Name: `vastuaudit-prototype`
   - Private (your choice)
   - Don't initialize with README

2. **Push this folder as its own repo:**
   ```bash
   cd ~/iCloud/CodeOS/VastuAudit.ai/prototype-deploy
   git init
   git add .
   git commit -m "Initial prototype"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/vastuaudit-prototype.git
   git push -u origin main
   ```

3. **Open Railway** → **+ New** → **GitHub Repo** → pick `vastuaudit-prototype`.

4. Railway auto-detects Node, builds with Nixpacks, runs `npm start`.

5. **Settings → Networking → Generate Domain** → get the live URL.

---

## Custom domain (optional)

Once you're happy with the prototype:

1. Buy or use existing domain (e.g., `prototype.vastuaudit.ai`)
2. Railway service → **Settings → Networking → Custom Domain**
3. Add CNAME record at your DNS provider pointing to the Railway domain
4. Railway provisions Let's Encrypt cert automatically

---

## Local testing

Before pushing, sanity-check locally:

```bash
cd prototype-deploy
npm install
npm run dev
# open http://localhost:3000
```

---

## How it works under the hood

- `package.json` declares `serve` as a dependency
- `npm start` runs `serve -s . -l ${PORT:-3000}` — Railway injects `$PORT`
- `serve -s` flag enables single-page-app fallback (any route → index.html)
- `railway.json` tells Railway to use Nixpacks builder, healthcheck on `/`, and restart on failure 3x

---

## Troubleshooting

**Build fails with "Cannot find module 'serve'":**
Railway didn't run `npm install`. Force a fresh deploy: Settings → Redeploy → "Build from scratch."

**404 on the live URL:**
Root Directory misconfigured. Settings → Source → Root Directory must be exactly `prototype-deploy` (no leading slash).

**Slow first load:**
Static `serve` is single-threaded; for production the real Next.js app will use Railway's optimized Node runtime. This prototype is fine for stakeholder review.

**Want HTTP/2 + edge cache:**
Put Cloudflare in front (Cloudflare → Add Site → orange-cloud the CNAME).

---

## Next step after the prototype is live

Once stakeholders sign off on the prototype:

1. Hand the live URL + `ux/design-system.md` + `ux/handoff-to-claude-code.md` to Claude Code
2. Claude Code starts Sprint 3 (Foundation → Components → Screens → Wiring)
3. The real Next.js app deploys to Railway as a separate service in the same project
4. The prototype service can be paused (Settings → Pause) or kept as a reference build

---

**Powered by Qadr AI Agency Dubai**
