import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { ShieldAlert, Lock, CheckCircle2, AlertTriangle } from "lucide-react";

export default function GuardrailsPage() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16]">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Security Guardrails & Safety Policies</h1>
            <p className="text-sm text-slate-400">Configure PII anonymizers, prompt injection defense, and content safety filters.</p>
          </div>
        </header>

        <div className="mt-8 space-y-4">
          <Card>
            <CardContent className="flex items-center justify-between p-6">
              <div className="flex items-center gap-4">
                <Lock className="h-6 w-6 text-indigo-400" />
                <div>
                  <h3 className="font-semibold text-white">PII Redaction Engine</h3>
                  <p className="text-xs text-slate-400">Automatically masks SSNs, Credit Cards, API Keys, Emails, and Phone Numbers.</p>
                </div>
              </div>
              <span className="px-3 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">Active (Enforcing)</span>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="flex items-center justify-between p-6">
              <div className="flex items-center gap-4">
                <ShieldAlert className="h-6 w-6 text-amber-400" />
                <div>
                  <h3 className="font-semibold text-white">Adversarial Prompt Injection Classifier</h3>
                  <p className="text-xs text-slate-400">Blocks jailbreaks, DAN vectors, and unauthorized system prompt extraction attempts.</p>
                </div>
              </div>
              <span className="px-3 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">Active (Enforcing)</span>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
}
