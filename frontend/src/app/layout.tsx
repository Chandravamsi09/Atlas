import React from "react";
import "./globals.css";

export const metadata = {
  title: "Atlas AI Platform - Enterprise LLMOps & Orchestration",
  description: "Unified multi-tenant AI Platform, intelligent LLM routing, prompt ops, agent DAGs, and evaluation engine.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[#090d16] text-slate-100 antialiased selection:bg-indigo-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
