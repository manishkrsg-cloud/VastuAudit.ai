# syntax=docker/dockerfile:1.7
# ---------------------------------------------------------------------------
# VastuAudit.ai web — Railway image (Next.js standalone)
# Build context: REPO ROOT (so pnpm-lock.yaml + workspace metadata are visible).
# Set Railway service Root Directory to "/" and Dockerfile Path to
# "apps/web/Dockerfile".
# ---------------------------------------------------------------------------

ARG NODE_VERSION=22-alpine

# ----- deps stage --------------------------------------------------------
FROM node:${NODE_VERSION} AS deps
RUN apk add --no-cache libc6-compat
RUN corepack enable && corepack prepare pnpm@10.32.1 --activate
WORKDIR /repo

COPY pnpm-lock.yaml pnpm-workspace.yaml package.json ./
COPY apps/web/package.json ./apps/web/
# When more workspace packages exist (packages/shared-types etc.), copy
# their package.json files here too.

RUN --mount=type=cache,id=pnpm,target=/pnpm-store \
    pnpm config set store-dir /pnpm-store && \
    pnpm install --frozen-lockfile --filter @vastuaudit/web...

# ----- build stage -------------------------------------------------------
FROM node:${NODE_VERSION} AS builder
RUN corepack enable && corepack prepare pnpm@10.32.1 --activate
WORKDIR /repo

COPY --from=deps /repo/node_modules ./node_modules
COPY --from=deps /repo/apps/web/node_modules ./apps/web/node_modules
COPY . .

ENV NEXT_TELEMETRY_DISABLED=1

WORKDIR /repo/apps/web
RUN pnpm build

# ----- runner stage ------------------------------------------------------
FROM node:${NODE_VERSION} AS runner
WORKDIR /app

ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1 \
    PORT=3000 \
    HOSTNAME=0.0.0.0

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

# Standalone output (with outputFileTracingRoot=monorepo root) lands at
# apps/web/.next/standalone/ and contains a slimmed node_modules tree plus
# apps/web/server.js.
COPY --from=builder --chown=nextjs:nodejs /repo/apps/web/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /repo/apps/web/.next/static ./apps/web/.next/static
COPY --from=builder --chown=nextjs:nodejs /repo/apps/web/public ./apps/web/public

USER nextjs

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:${PORT}/api/health || exit 1

CMD ["node", "apps/web/server.js"]
