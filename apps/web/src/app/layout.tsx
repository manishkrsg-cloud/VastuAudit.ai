import type { Metadata } from "next";
import { Inter, Lora, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

const lora = Lora({
  variable: "--font-heading",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: "VastuAudit.ai — Professional Vastu audits in 60 seconds",
    template: "%s · VastuAudit.ai",
  },
  description:
    "AI-powered Vastu audit reports for property buyers, builders, and consultants. Consultant-grade. Powered by Qadr AI Agency Dubai.",
  metadataBase: new URL(
    process.env.NEXT_PUBLIC_APP_URL ?? "https://vastuaudit.ai",
  ),
  openGraph: {
    title: "VastuAudit.ai — Professional Vastu audits in 60 seconds",
    description:
      "AI-powered Vastu audit reports. Consultant-grade. By Qadr AI Agency Dubai.",
    siteName: "VastuAudit.ai",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${lora.variable} ${jetbrainsMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
