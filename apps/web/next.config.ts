import path from "node:path";
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Standalone output → minimal node runtime image for Railway.
  output: "standalone",

  // Trace dependencies up to the monorepo root so pnpm workspace deps are
  // included in the standalone bundle.
  outputFileTracingRoot: path.join(__dirname, "../../"),

  reactStrictMode: true,

  // Plan images served from Cloudflare R2 (public bucket OR custom domain).
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "**.r2.cloudflarestorage.com" },
      { protocol: "https", hostname: "**.r2.dev" },
      { protocol: "https", hostname: "plans.vastuaudit.ai" },
      { protocol: "https", hostname: "vastuaudit.ai" },
    ],
  },
};

export default nextConfig;
