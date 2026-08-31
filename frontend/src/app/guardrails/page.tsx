'use client';

import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { ShieldAlert, Check, AlertTriangle, ShieldCheck, Sliders } from "lucide-react";

export default function GuardrailsPage() {
  const rules = [
    { name: "PII Scrubber (SSN, Passports, National IDs)", status: "Active (Block & Mask)", framework: "GDPR / HIPAA", hits: 142 },
    { name: "Prompt Injection & Jailbreak Defense", status: "Active (Heuristic + Classifier)", framework: "OWASP LLM01", hits: 89 },
    { name: "Financial Card & CVV Data Loss Prevention", status: "Active (PCI-DSS Redact)", framework: "PCI-DSS v4.0", hits: 24 },
    { name: "Toxicity & Content Moderation Filter", status: "Active (Threshold 0.85)", framework: "Enterprise Safety", hits: 12 }
  ];

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <ShieldAlert className="h-6 w-6 text-emerald-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Guardrails & Safety Control Plane</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Real-time PII anonymization, adversarial injection defense, and regulatory compliance enforcement.</p>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Security Block Rate</span>
              <ShieldCheck className="h-4 w-4 text-emerald-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">99.98%</div>
            <div className="mt-2 text-xs text-emerald-400">Zero data leakages reported</div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Injections Intercepted (30d)</span>
              <AlertTriangle className="h-4 w-4 text-amber-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">267</div>
            <div className="mt-2 text-xs text-slate-400">Across 18 enterprise tenants</div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Inspection Latency</span>
              <Sliders className="h-4 w-4 text-cyan-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">&lt; 8ms</div>
            <div className="mt-2 text-xs text-slate-400">Zero bottleneck streaming overhead</div>
          </div>
        </div>

        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Active Compliance Profiles</h2>
          <div className="divide-y divide-slate-800">
            {rules.map((r, i) => (
              <div key={i} className="py-4 flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-slate-200">{r.name}</h3>
                  <p className="text-xs text-slate-400 mt-0.5">Framework: {r.framework} • Total Blocks: {r.hits}</p>
                </div>
                <span className="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                  {r.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
