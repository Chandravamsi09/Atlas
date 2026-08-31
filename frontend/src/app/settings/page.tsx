'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Settings, Save, Lock, Building, Check } from "lucide-react";

export default function SettingsPage() {
  const [saved, setSaved] = useState(false);

  const handleSave = () => {
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Settings className="h-6 w-6 text-slate-300" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Platform Settings</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Configure tenant identity, model provider credentials, and SSO SAML integrations.</p>
          </div>
          <button
            onClick={handleSave}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2"
          >
            {saved ? <Check className="h-4 w-4 text-emerald-300" /> : <Save className="h-4 w-4" />}
            {saved ? "Saved Successfully!" : "Save Configuration"}
          </button>
        </header>

        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-6">
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              <Building className="h-5 w-5 text-indigo-400" /> Organization Profile
            </h2>
            <div className="space-y-4">
              <div>
                <label className="text-xs text-slate-400">Organization Name</label>
                <input
                  type="text"
                  defaultValue="Atlas Demo Organization"
                  className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1"
                />
              </div>
              <div>
                <label className="text-xs text-slate-400">Tenant Identifier</label>
                <input
                  type="text"
                  disabled
                  defaultValue="org_atlas_demo_01"
                  className="w-full bg-[#090d16]/50 border border-slate-800 rounded-lg p-2.5 text-sm text-slate-500 mt-1 font-mono"
                />
              </div>
            </div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-6">
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              <Lock className="h-5 w-5 text-emerald-400" /> Model Provider Vault
            </h2>
            <div className="space-y-4">
              <div>
                <label className="text-xs text-slate-400">OpenAI API Key (Encrypted at rest)</label>
                <input
                  type="password"
                  defaultValue="sk-proj-********************************"
                  className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 font-mono"
                />
              </div>
              <div>
                <label className="text-xs text-slate-400">Anthropic API Key (Encrypted at rest)</label>
                <input
                  type="password"
                  defaultValue="sk-ant-********************************"
                  className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 font-mono"
                />
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
