import { NextResponse } from "next/server";

// Used by Railway's healthcheck (railway.json → healthcheckPath).
// Lightweight; do NOT call the API or DB from here — Railway pings it
// every few seconds during rolling deploys.
export const dynamic = "force-static";
export const revalidate = false;

export function GET() {
  return NextResponse.json({
    status: "ok",
    app: "VastuAudit.ai",
    owner: "Qadr AI Agency Dubai",
  });
}
