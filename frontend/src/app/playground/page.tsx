import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Play, Sparkles, Sliders, RefreshCw } from "lucide-react";

export default function PlaygroundPage() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16] flex flex-col">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Side-by-Side Model Playground</h1>
            <p className="text-sm text-slate-400">Compare model latency, output quality, and token costs in real-time.</p>
          </div>
          <button className="flex items-center gap-2 px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold rounded-lg shadow-lg shadow-indigo-600/30 transition">
            <Play className="h-4 w-4" /> Run Inference
          </button>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8 flex-1">
          {/* Model A */}
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-6 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <span className="font-semibold text-indigo-400">Model A: GPT-4o</span>
                <span className="text-xs text-slate-400">Temp: 0.7 | Max: 2048</span>
              </div>
              <div className="mt-4 p-4 rounded-lg bg-slate-900/60 border border-slate-800 text-sm text-slate-300 min-h-[300px]">
                <p className="text-slate-500 italic">Waiting for prompt execution...</p>
              </div>
            </div>
            <div className="mt-4 pt-4 border-t border-slate-800 flex justify-between text-xs text-slate-400">
              <span>Tokens: 0</span>
              <span>Latency: 0ms</span>
              <span>Cost: $0.0000</span>
            </div>
          </div>

          {/* Model B */}
          <div className="bg-[#111827] border border-slate-800 rounded-xl p-6 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <span className="font-semibold text-sky-400">Model B: Claude 3.5 Sonnet</span>
                <span className="text-xs text-slate-400">Temp: 0.7 | Max: 2048</span>
              </div>
              <div className="mt-4 p-4 rounded-lg bg-slate-900/60 border border-slate-800 text-sm text-slate-300 min-h-[300px]">
                <p className="text-slate-500 italic">Waiting for prompt execution...</p>
              </div>
            </div>
            <div className="mt-4 pt-4 border-t border-slate-800 flex justify-between text-xs text-slate-400">
              <span>Tokens: 0</span>
              <span>Latency: 0ms</span>
              <span>Cost: $0.0000</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
