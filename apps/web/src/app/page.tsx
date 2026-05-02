import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-1 flex-col items-center justify-center bg-zinc-50 dark:bg-zinc-950 px-6 py-24">
      <div className="max-w-2xl text-center space-y-8">
        <p className="inline-flex items-center gap-2 rounded-full border border-emerald-200 bg-emerald-50 px-3 py-1 text-xs font-medium uppercase tracking-wide text-emerald-700 dark:border-emerald-900 dark:bg-emerald-950 dark:text-emerald-300">
          <span className="size-1.5 rounded-full bg-emerald-600" />
          Sprint 1 — building
        </p>

        <h1 className="font-heading text-5xl sm:text-6xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50">
          <span className="text-brand-green">VastuAudit</span>
          <span className="text-zinc-400">.ai</span>
        </h1>

        <p className="text-lg sm:text-xl text-zinc-600 dark:text-zinc-300 leading-relaxed">
          Professional Vastu audits in 60 seconds.
          <br />
          AI-powered. Consultant-grade.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-4">
          <Link
            href="/api/health"
            className="inline-flex h-11 items-center justify-center rounded-full bg-brand-green px-6 text-sm font-medium text-white transition-colors hover:bg-emerald-700"
          >
            API status
          </Link>
          <a
            href="https://github.com/manishkrsg-cloud/VastuAudit.ai"
            className="inline-flex h-11 items-center justify-center rounded-full border border-zinc-300 px-6 text-sm font-medium text-zinc-700 transition-colors hover:bg-zinc-100 dark:border-zinc-700 dark:text-zinc-200 dark:hover:bg-zinc-800"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </a>
        </div>
      </div>

      <footer className="absolute bottom-6 inset-x-0 text-center text-xs text-zinc-500">
        Powered by{" "}
        <span className="font-medium text-zinc-700 dark:text-zinc-300">
          Qadr AI Agency Dubai
        </span>
      </footer>
    </main>
  );
}
