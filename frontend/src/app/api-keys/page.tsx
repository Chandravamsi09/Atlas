'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Key, Plus, Copy, Check, Shield, X } from "lucide-react";

export default function ApiKeysPage() {
  const [keys, setKeys] = useState([
    { id: "key_prod_01", name: "Production Gateway Live Key", key: "atl_live_sample_key_9981a7b", rps: 500, scopes: "models:invoke, prompts:write" }
  ]);
  const [copiedId, setCopiedId] = useState<string | null>(null);

  // Modal State
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [keyName, setKeyName] = useState("");
  const [keyRps, setKeyRps] = useState(500);

  const handleCopy = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleCreateKey = (e: React.FormEvent) => {
    e.preventDefault();
    if (!keyName.trim()) return;

    const newKey = {
      id: `key_${Math.random().toString(36).substring(2, 8)}`,
      name: keyName,
      key: `atl_live_${Math.random().toString(36).substring(2, 16)}`,
      rps: keyRps,
      scopes: "models:read, models:invoke, prompts:read"
    };

    setKeys([newKey, ...keys]);
    setKeyName("");
    setIsModalOpen(false);
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
          <button
            onClick={() => setIsModalOpen(true)}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2"
          >
            <Plus className="h-4 w-4" /> Generate New API Key
          </button>
        </header>

        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Active Organization Keys ({keys.length})</h2>
          <div className="space-y-3">
            {keys.map((k) => (
              <div key={k.id} className="bg-[#090d16] border border-slate-800 rounded-lg p-4 flex items-center justify-between">
                <div>
                  <div className="font-semibold text-slate-200">{k.name}</div>
                  <div className="font-mono text-xs text-indigo-400 mt-1">{k.key}</div>
                  <div className="text-xs text-slate-400 mt-1">Scopes: {k.scopes} • RPS Limit: {k.rps}</div>
                </div>
                <button
                  onClick={() => handleCopy(k.id, k.key)}
                  className="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded-lg border border-slate-700 transition flex items-center gap-1.5"
                >
                  {copiedId === k.id ? <Check className="h-3.5 w-3.5 text-emerald-400" /> : <Copy className="h-3.5 w-3.5" />}
                  {copiedId === k.id ? "Copied" : "Copy Key"}
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Modal */}
        {isModalOpen && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-md bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <Key className="h-5 w-5 text-indigo-400" />
                  <h3 className="font-bold text-white text-lg">Generate New API Key</h3>
                </div>
                <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <form onSubmit={handleCreateKey} className="mt-4 space-y-4">
                <div>
                  <label className="text-xs font-medium text-slate-300">Key Name</label>
                  <input
                    type="text"
                    required
                    placeholder="e.g. Staging Integration Service"
                    value={keyName}
                    onChange={(e) => setKeyName(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none focus:border-indigo-500"
                  />
                </div>

                <div>
                  <label className="text-xs font-medium text-slate-300">Rate Limit Quota (RPS): {keyRps}</label>
                  <input
                    type="range"
                    min="50"
                    max="1000"
                    step="50"
                    value={keyRps}
                    onChange={(e) => setKeyRps(parseInt(e.target.value))}
                    className="w-full mt-2 accent-indigo-500"
                  />
                </div>

                <div className="pt-4 border-t border-slate-800 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setIsModalOpen(false)}
                    className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg"
                  >
                    Create Key
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
