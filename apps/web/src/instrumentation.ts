// Server + Edge runtime instrumentation hook (Next.js App Router).
// No-op when SENTRY_DSN is unset — safe to ship before a real DSN exists.
// Dynamic import keeps the Sentry SDK out of the bundle when disabled.
export async function register() {
  if (!process.env.SENTRY_DSN) return;
  const Sentry = await import("@sentry/nextjs");
  Sentry.init({
    dsn: process.env.SENTRY_DSN,
    tracesSampleRate: 0.1,
    environment: process.env.NODE_ENV,
  });
}
