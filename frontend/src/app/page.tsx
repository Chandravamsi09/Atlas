'use client';

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { Sidebar } from "@/components/layout/sidebar";
import { api } from "@/lib/api";
import { Activity, Zap, Cpu, DollarSign, ArrowUpRight, CheckCircle2, Play, RefreshCw } from "lucide-react";

export default function DashboardPage() {
  const [metrics, setMetrics] = useState<any>(null);
  const [providers, setProviders] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchOverview = async () => {
    setLoading(true);
    try {
      const res = await api.metrics.getOverview();
      if (res.success) {
        setMetrics(res.metrics);
        setProviders(res.providers);
      }
    } catch (err) {
      console.error("Failed to fetch live metrics:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOverview();
  }, []);

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16] overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Enterprise AI Overview</h1>
            <p className="text-sm text-slate-400 mt-1">Live telemetry, model gateway throughput, and cluster health.</p>
          </div>
          <div className="flex gap-3">
            <button
              onClick={fetchOverview}
              className="px-3.5 py-2 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg border border-slate-700 transition flex items-center gap-1.5"
            >
              <RefreshCw className={`h-3.5 w-3.5 ${loading ? 'animate-spin' : ''}`} /> Refresh
            </button>
            <Link
              href="/prompt-studio"
              className="px-4 py-2 text-sm bg-indigo-600 hover:bg-indigo-500 text-white font-medium rounded-lg shadow-sm transition"
            >
              New Prompt
            </Link>
          </div>
        </header>

        {/* Real Metrics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-8">
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Total Requests</span>
              <Activity className="h-4 w-4 text-indigo-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white font-mono">
              {metrics ? metrics.total_requests.toLocaleString() : "0"}
            </div>
            <div className="mt-2 text-xs text-slate-400">
              {metrics && metrics.total_requests > 0 ? "Live requests tracked" : "No requests recorded yet"}
            </div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Token Consumption</span>
              <Cpu className="h-4 w-4 text-cyan-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white font-mono">
              {metrics ? metrics.total_tokens.toLocaleString() : "0"}
            </div>
            <div className="mt-2 text-xs text-slate-400">
              Cache Hit Rate: {metrics ? `${metrics.cache_hit_rate_pct}%` : "0.0%"}
            </div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>P95 Latency</span>
              <Zap className="h-4 w-4 text-amber-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white font-mono">
              {metrics ? `${metrics.p95_latency_ms}ms` : "0ms"}
            </div>
            <div className="mt-2 text-xs text-emerald-400">
              {metrics && metrics.avg_latency_ms > 0 ? `Avg: ${metrics.avg_latency_ms}ms` : "Smart router active"}
            </div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Total Gateway Spend</span>
              <DollarSign className="h-4 w-4 text-emerald-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white font-mono">
              {metrics ? `$${metrics.total_spend_usd}` : "$0.00"}
            </div>
            <div className="mt-2 text-xs text-slate-400">Tracked in Token Ledger</div>
          </div>
        </div>

        {/* Empty state prompt if 0 requests */}
        {metrics && metrics.total_requests === 0 && (
          <div className="mt-8 bg-indigo-950/20 border border-indigo-500/20 rounded-xl p-6 flex items-center justify-between">
            <div>
              <h3 className="font-semibold text-white">Ready for live testing?</h3>
              <p className="text-sm text-slate-400 mt-1">
                Open the Model Playground to execute a query. Live latency, token usage, and distributed traces will appear here in real time.
              </p>
            </div>
            <Link
              href="/playground"
              className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg transition flex items-center gap-2 shrink-0"
            >
              <Play className="h-4 w-4" /> Open Model Playground
            </Link>
          </div>
        )}

        {/* Model Gateway Status */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white">Active Model Providers & Dynamic Routers</h2>
          <div className="mt-4 divide-y divide-slate-800/80">
            {providers.map((p, idx) => (
              <div key={idx} className="py-3.5 flex items-center justify-between">
                <div>
                  <p className="font-medium text-slate-200">{p.name}</p>
                  <p className="text-xs text-slate-400">Route: {p.route} | Base Latency: {p.latency_ms}ms</p>
                </div>
                <span className={`px-2.5 py-1 text-xs rounded-full border ${p.is_mock ? 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20' : 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20'}`}>
                  {p.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
