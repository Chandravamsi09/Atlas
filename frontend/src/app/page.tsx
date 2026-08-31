import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Activity, Zap, Cpu, DollarSign, ArrowUpRight } from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16]">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Enterprise AI Overview</h1>
            <p className="text-sm text-slate-400">Real-time model gateway metrics, token usage, and system health.</p>
          </div>
          <div className="flex gap-3">
            <button className="px-4 py-2 text-sm bg-indigo-600 hover:bg-indigo-500 text-white font-medium rounded-lg shadow-sm transition">
              New Prompt
            </button>
          </div>
        </header>

        {/* Top Metric Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-8">
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Total Requests (24h)</span>
              <Activity className="h-4 w-4 text-indigo-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">1,482,900</div>
            <div className="mt-2 text-xs text-emerald-400 flex items-center gap-1">
              <ArrowUpRight className="h-3 w-3" /> +14.2% from yesterday
            </div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Token Consumption</span>
              <Cpu className="h-4 w-4 text-cyan-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">48.6M</div>
            <div className="mt-2 text-xs text-slate-400">Cache Hit Rate: 34.2%</div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>P95 Latency</span>
              <Zap className="h-4 w-4 text-amber-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">245ms</div>
            <div className="mt-2 text-xs text-emerald-400">-18ms smart routing gain</div>
          </div>

          <div className="bg-[#111827] border border-slate-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-center justify-between text-slate-400 text-sm">
              <span>Current Spend (MTD)</span>
              <DollarSign className="h-4 w-4 text-emerald-400" />
            </div>
            <div className="mt-3 text-3xl font-bold text-white">$412.80</div>
            <div className="mt-2 text-xs text-slate-400">Budget: $1,000.00 (41.2%)</div>
          </div>
        </div>

        {/* Model Gateway Status */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white">Active Model Providers & Circuit Breakers</h2>
          <div className="mt-4 divide-y divide-slate-800/80">
            <div className="py-3 flex items-center justify-between">
              <div>
                <p className="font-medium text-slate-200">OpenAI (gpt-4o, gpt-4o-mini)</p>
                <p className="text-xs text-slate-400">Route: Direct Primary | Latency: 210ms</p>
              </div>
              <span className="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Operational</span>
            </div>
            <div className="py-3 flex items-center justify-between">
              <div>
                <p className="font-medium text-slate-200">Anthropic (Claude 3.5 Sonnet)</p>
                <p className="text-xs text-slate-400">Route: Fallback Secondary | Latency: 320ms</p>
              </div>
              <span className="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Operational</span>
            </div>
            <div className="py-3 flex items-center justify-between">
              <div>
                <p className="font-medium text-slate-200">Local vLLM Cluster</p>
                <p className="text-xs text-slate-400">Route: High Throughput Batch | Latency: 85ms</p>
              </div>
              <span className="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Operational</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
