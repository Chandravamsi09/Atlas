'use client';

import React, { useEffect, useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { api } from "@/lib/api";
import { Activity, RefreshCw, Layers, CheckCircle2, ChevronRight } from "lucide-react";

export default function TracesPage() {
  const [traces, setTraces] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedTrace, setSelectedTrace] = useState<any>(null);

  const fetchTraces = async () => {
    setLoading(true);
    try {
      const res = await api.traces.list(50);
      if (res.success) {
        setTraces(res.traces);
        if (res.traces.length > 0 && !selectedTrace) {
          setSelectedTrace(res.traces[0]);
        }
      }
    } catch (err) {
      console.error("Failed to fetch traces:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTraces();
  }, []);

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-hidden">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Activity className="h-6 w-6 text-amber-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Traces & Observability</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Live OpenTelemetry request spans, token ledger breakdown, and latency analysis.</p>
          </div>
          <button
            onClick={fetchTraces}
            className="px-3.5 py-2 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg border border-slate-700 transition flex items-center gap-1.5"
          >
            <RefreshCw className={`h-3.5 w-3.5 ${loading ? 'animate-spin' : ''}`} /> Refresh Traces
          </button>
        </header>

        <div className="flex-1 grid grid-cols-1 lg:grid-cols-2 gap-6 mt-6 overflow-hidden">
          {/* Traces List */}
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 flex flex-col overflow-hidden">
            <h2 className="text-sm font-semibold text-slate-200 mb-3">Live Request Spans ({traces.length})</h2>
            <div className="flex-1 overflow-y-auto divide-y divide-slate-800/80 pr-2">
              {traces.length === 0 ? (
                <div className="h-full flex flex-col items-center justify-center text-slate-500 text-sm">
                  <Activity className="h-8 w-8 mb-2 opacity-40" />
                  No traces recorded yet. Send a request from the Model Playground!
                </div>
              ) : (
                traces.map((t) => (
                  <div
                    key={t.id}
                    onClick={() => setSelectedTrace(t)}
                    className={`py-3 px-3 rounded-lg cursor-pointer transition flex items-center justify-between ${
                      selectedTrace?.id === t.id ? 'bg-indigo-600/15 border border-indigo-500/30' : 'hover:bg-slate-800/40'
                    }`}
                  >
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-xs text-indigo-400 font-semibold">{t.id}</span>
                        <span className="text-xs text-slate-300 font-medium">{t.endpoint}</span>
                      </div>
                      <div className="text-[11px] text-slate-400 mt-1">
                        Model: <span className="text-slate-200">{t.model}</span> • {t.created_at || "Just now"}
                      </div>
                    </div>
                    <div className="text-right">
                      <div className="font-mono text-xs text-white">{t.duration_ms}ms</div>
                      <div className="text-[11px] text-emerald-400 font-mono">{t.total_tokens} tok</div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>

          {/* Trace Detail Inspector */}
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 flex flex-col overflow-hidden">
            <h2 className="text-sm font-semibold text-slate-200 mb-3">Span Inspector & Telemetry Payload</h2>
            {selectedTrace ? (
              <div className="flex-1 overflow-y-auto space-y-4 pr-2 font-mono text-xs">
                <div className="bg-[#090d16] border border-slate-800 rounded-lg p-4 space-y-2">
                  <div className="text-slate-400">Trace ID: <span className="text-indigo-400 font-bold">{selectedTrace.id}</span></div>
                  <div className="text-slate-400">Endpoint: <span className="text-white">{selectedTrace.endpoint}</span></div>
                  <div className="text-slate-400">Provider: <span className="text-white">{selectedTrace.provider}</span></div>
                  <div className="text-slate-400">Model: <span className="text-white">{selectedTrace.model}</span></div>
                  <div className="text-slate-400">Status: <span className="text-emerald-400 font-bold">{selectedTrace.status}</span></div>
                  <div className="text-slate-400">Duration: <span className="text-amber-400">{selectedTrace.duration_ms}ms</span></div>
                  <div className="text-slate-400">Tokens: <span className="text-cyan-400">{selectedTrace.total_tokens} (Prompt: {selectedTrace.prompt_tokens}, Completion: {selectedTrace.completion_tokens})</span></div>
                  <div className="text-slate-400">Estimated Cost: <span className="text-emerald-400">${selectedTrace.cost_usd}</span></div>
                </div>

                {selectedTrace.user_prompt && (
                  <div>
                    <div className="text-slate-400 font-sans text-xs font-semibold mb-1">User Prompt:</div>
                    <div className="bg-[#090d16] border border-slate-800 rounded-lg p-3 text-slate-200 whitespace-pre-wrap font-sans text-xs">
                      {selectedTrace.user_prompt}
                    </div>
                  </div>
                )}

                {selectedTrace.model_response && (
                  <div>
                    <div className="text-slate-400 font-sans text-xs font-semibold mb-1">Model Response:</div>
                    <div className="bg-[#090d16] border border-slate-800 rounded-lg p-3 text-slate-200 whitespace-pre-wrap font-sans text-xs">
                      {selectedTrace.model_response}
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <div className="h-full flex items-center justify-center text-slate-500 text-sm font-sans">
                Select a trace from the left panel to inspect span breakdown.
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
