import React from "react";
import "./globals.css";
import { AuthProvider } from "@/context/auth-context";

export const metadata = {
  title: "Atlas AI Platform - Enterprise LLMOps & Orchestration",
  description: "Unified multi-tenant AI Platform, intelligent LLM routing, prompt ops, agent DAGs, and evaluation engine.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[#090d16] text-slate-100 antialiased">
        <AuthProvider>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
