'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Key, Plus, Copy, Check, Shield } from "lucide-react";

export default function ApiKeysPage() {
  const [copied, setCopied] = useState(false);
  const apiKey = "atl_live_local_dev_key";

  const handleCopy = () => {
    navigator.clipboard.writeText(apiKey);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Key className="h-6 w-6 text-indigo-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">API Keys & Token Quotas</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Multi-tenant authentication keys, RBAC permission scopes, and rate limits.</p>
          </div>
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2">
            <Plus className="h-4 w-4" /> Generate New API Key
          </button>
        </header>

        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Active Organization Keys (Acme Corp)</h2>
          <div className="bg-[#090d16] border border-slate-800 rounded-lg p-4 flex items-center justify-between">
            <div>
              <div className="font-semibold text-slate-200">Production Live Key</div>
              <div className="font-mono text-xs text-indigo-400 mt-1">{apiKey}</div>
              <div className="text-xs text-slate-400 mt-1">Scopes: models:read, models:invoke, prompts:write • RPS Limit: 500</div>
            </div>
            <button
              onClick={handleCopy}
              className="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded-lg border border-slate-700 transition flex items-center gap-1.5"
            >
              {copied ? <Check className="h-3.5 w-3.5 text-emerald-400" /> : <Copy className="h-3.5 w-3.5" />}
              {copied ? "Copied" : "Copy Key"}
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
