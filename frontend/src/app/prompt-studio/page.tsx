'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Terminal, Play, Save, GitBranch, Sparkles, Check, X, AlertCircle } from "lucide-react";

export default function PromptStudioPage() {
  const [templateContent, setTemplateContent] = useState(
    `You are an enterprise AI support assistant for {{ company_name }}.\n\nCustomer Query: {{ customer_query }}\nCustomer Tier: {{ user_tier }}\n\nGuidelines:\n1. Always respond politely and professionally.\n2. If customer tier is 'enterprise', escalate critical issues immediately.\n3. Provide step-by-step resolution.`
  );
  const [variables, setVariables] = useState({
    company_name: "Atlas Global",
    customer_query: "How do I configure SAML SSO with Okta?",
    user_tier: "enterprise"
  });
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  // Canary Modal State
  const [isCanaryModalOpen, setIsCanaryModalOpen] = useState(false);
  const [canaryPercent, setCanaryPercent] = useState(10);
  const [canarySaved, setCanarySaved] = useState(false);

  // Save Version Modal State
  const [isSaveModalOpen, setIsSaveModalOpen] = useState(false);
  const [versionTag, setVersionTag] = useState("v2.5");
  const [changelog, setChangelog] = useState("Added multi-tenant compliance guidelines");
  const [versionSaved, setVersionSaved] = useState(false);

  const handleTestRun = async () => {
    setLoading(true);
    setTimeout(() => {
      setOutput(
        `Hello! Thank you for reaching out to Atlas Global Support.\n\nSince you are an Enterprise customer, here is the direct guide to configure SAML 2.0 SSO with Okta:\n\n1. Navigate to Settings > Identity & SSO in your Atlas Dashboard.\n2. Copy the ACS URL: https://api.atlas.ai/auth/saml/callback\n3. In your Okta Admin Console, create a new SAML 2.0 Application and paste the Entity ID and ACS URL.\n4. Upload your Okta IdP Metadata XML file into Atlas.\n\nYour enterprise SLA priority is active. Let us know if you would like our dedicated solution architect to assist!`
      );
      setLoading(false);
    }, 600);
  };

  const handleSaveCanary = (e: React.FormEvent) => {
    e.preventDefault();
    setCanarySaved(true);
    setTimeout(() => {
      setCanarySaved(false);
      setIsCanaryModalOpen(false);
    }, 1000);
  };

  const handleSaveVersion = (e: React.FormEvent) => {
    e.preventDefault();
    setVersionSaved(true);
    setTimeout(() => {
      setVersionSaved(false);
      setIsSaveModalOpen(false);
    }, 1000);
  };

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-hidden">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Terminal className="h-6 w-6 text-indigo-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Prompt Studio</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Dynamic Jinja2 prompt lifecycle compiler, versioning, and canary split.</p>
          </div>
          <div className="flex gap-3">
            <button
              onClick={() => setIsCanaryModalOpen(true)}
              className="px-4 py-2 text-sm bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium rounded-lg border border-slate-700 transition flex items-center gap-2"
            >
              <GitBranch className="h-4 w-4" /> Canary ({canaryPercent}% Traffic)
            </button>
            <button
              onClick={() => setIsSaveModalOpen(true)}
              className="px-4 py-2 text-sm bg-indigo-600 hover:bg-indigo-500 text-white font-medium rounded-lg shadow-sm transition flex items-center gap-2"
            >
              <Save className="h-4 w-4" /> Save Version ({versionTag})
            </button>
          </div>
        </header>

        <div className="flex-1 grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6 overflow-hidden">
          {/* Editor Column */}
          <div className="flex flex-col bg-[#111827] border border-slate-800 rounded-xl p-5 overflow-hidden">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <span className="text-sm font-semibold text-slate-200">Template Editor (Jinja2)</span>
              <span className="text-xs px-2.5 py-0.5 rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">{versionTag} (Active)</span>
            </div>
            <textarea
              className="flex-1 w-full bg-[#090d16] border border-slate-800 rounded-lg p-4 mt-4 font-mono text-sm text-slate-200 focus:outline-none focus:border-indigo-500 resize-none"
              value={templateContent}
              onChange={(e) => setTemplateContent(e.target.value)}
            />
            
            <div className="mt-4 pt-4 border-t border-slate-800">
              <h3 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Test Variables (JSON / Schema)</h3>
              <div className="grid grid-cols-3 gap-3">
                {Object.keys(variables).map((key) => (
                  <div key={key}>
                    <label className="text-xs text-slate-400 font-mono">{key}</label>
                    <input
                      type="text"
                      className="w-full bg-[#090d16] border border-slate-800 rounded px-2.5 py-1.5 text-xs text-slate-200 font-mono mt-1"
                      value={(variables as any)[key]}
                      onChange={(e) => setVariables({ ...variables, [key]: e.target.value })}
                    />
                  </div>
                ))}
              </div>
            </div>

            <div className="mt-4 flex justify-end">
              <button
                onClick={handleTestRun}
                disabled={loading}
                className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2"
              >
                {loading ? <Sparkles className="h-4 w-4 animate-spin" /> : <Play className="h-4 w-4" />}
                Run Test Execution
              </button>
            </div>
          </div>

          {/* Preview Column */}
          <div className="flex flex-col bg-[#111827] border border-slate-800 rounded-xl p-5 overflow-hidden">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <span className="text-sm font-semibold text-slate-200">Execution Output & Gateway Metrics</span>
              {output && <span className="text-xs text-emerald-400 flex items-center gap-1"><Check className="h-3 w-3" /> 200 OK (210ms)</span>}
            </div>

            <div className="flex-1 bg-[#090d16] border border-slate-800 rounded-lg p-4 mt-4 overflow-y-auto font-sans text-sm text-slate-300 whitespace-pre-line">
              {output || (
                <div className="h-full flex flex-col items-center justify-center text-slate-500 text-sm">
                  <Play className="h-8 w-8 mb-2 opacity-40" />
                  Click 'Run Test Execution' to compile template and simulate gateway response.
                </div>
              )}
            </div>

            {output && (
              <div className="mt-4 grid grid-cols-4 gap-2 pt-3 border-t border-slate-800 text-center">
                <div className="bg-[#1e293b]/40 p-2 rounded">
                  <div className="text-xs text-slate-400">Tokens</div>
                  <div className="text-sm font-bold text-white">142</div>
                </div>
                <div className="bg-[#1e293b]/40 p-2 rounded">
                  <div className="text-xs text-slate-400">Cost</div>
                  <div className="text-sm font-bold text-emerald-400">$0.00028</div>
                </div>
                <div className="bg-[#1e293b]/40 p-2 rounded">
                  <div className="text-xs text-slate-400">Latency</div>
                  <div className="text-sm font-bold text-amber-400">210ms</div>
                </div>
                <div className="bg-[#1e293b]/40 p-2 rounded">
                  <div className="text-xs text-slate-400">Router Model</div>
                  <div className="text-sm font-bold text-indigo-400">gpt-4o</div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Canary Traffic Modal */}
        {isCanaryModalOpen && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-md bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <GitBranch className="h-5 w-5 text-indigo-400" />
                  <h3 className="font-bold text-white text-lg">Canary Deployment Traffic Split</h3>
                </div>
                <button onClick={() => setIsCanaryModalOpen(false)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <form onSubmit={handleSaveCanary} className="mt-4 space-y-4">
                <div>
                  <div className="flex items-center justify-between text-sm text-slate-300">
                    <span>Canary Traffic Allocation</span>
                    <span className="font-bold text-indigo-400">{canaryPercent}%</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="100"
                    step="5"
                    value={canaryPercent}
                    onChange={(e) => setCanaryPercent(parseInt(e.target.value))}
                    className="w-full mt-2 accent-indigo-500"
                  />
                  <div className="flex justify-between text-[11px] text-slate-500 mt-1 font-mono">
                    <span>Production Baseline ({100 - canaryPercent}%)</span>
                    <span>New Candidate ({canaryPercent}%)</span>
                  </div>
                </div>

                <div className="pt-4 border-t border-slate-800 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setIsCanaryModalOpen(false)}
                    className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg flex items-center gap-1.5"
                  >
                    {canarySaved ? <Check className="h-4 w-4" /> : null}
                    {canarySaved ? "Saved!" : "Apply Traffic Split"}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Save Version Modal */}
        {isSaveModalOpen && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-md bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <Save className="h-5 w-5 text-indigo-400" />
                  <h3 className="font-bold text-white text-lg">Save New Prompt Version</h3>
                </div>
                <button onClick={() => setIsSaveModalOpen(false)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <form onSubmit={handleSaveVersion} className="mt-4 space-y-4">
                <div>
                  <label className="text-xs font-medium text-slate-300">Version Tag</label>
                  <input
                    type="text"
                    required
                    value={versionTag}
                    onChange={(e) => setVersionTag(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none focus:border-indigo-500 font-mono"
                  />
                </div>

                <div>
                  <label className="text-xs font-medium text-slate-300">Changelog / Release Notes</label>
                  <textarea
                    rows={3}
                    required
                    value={changelog}
                    onChange={(e) => setChangelog(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none focus:border-indigo-500 resize-none"
                  />
                </div>

                <div className="pt-4 border-t border-slate-800 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setIsSaveModalOpen(false)}
                    className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg flex items-center gap-1.5"
                  >
                    {versionSaved ? <Check className="h-4 w-4" /> : null}
                    {versionSaved ? "Published!" : "Publish to Registry"}
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
