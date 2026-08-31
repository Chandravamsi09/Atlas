'use client';

import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { CheckCircle2, Play, Trophy, Sparkles, Target } from "lucide-react";

export default function EvaluationPage() {
  const benchmarks = [
    { model: "gpt-4o", faithfulness: "96.4%", contextRelevance: "94.2%", answerRelevance: "98.1%", score: 9.6 },
    { model: "claude-3-5-sonnet", faithfulness: "97.1%", contextRelevance: "95.0%", answerRelevance: "97.8%", score: 9.7 },
    { model: "gemini-1.5-pro", faithfulness: "93.8%", contextRelevance: "92.1%", answerRelevance: "94.5%", score: 9.3 },
    { model: "vllm-llama-3-70b", faithfulness: "91.2%", contextRelevance: "89.4%", answerRelevance: "92.0%", score: 9.1 },
  ];

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <CheckCircle2 className="h-6 w-6 text-indigo-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Evaluations & Continuous Benchmarks</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">LLM-as-a-Judge grading rubrics, RAG Triad faithfulness, and model leaderboards.</p>
          </div>
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2">
            <Play className="h-4 w-4" /> Run 100-Sample Benchmark
          </button>
        </header>

        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">RAG Triad Leaderboard (Continuous Golden Dataset)</h2>
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="border-b border-slate-800 text-slate-400 text-xs uppercase">
                <tr>
                  <th className="py-3 px-4">Model Architecture</th>
                  <th className="py-3 px-4">Faithfulness</th>
                  <th className="py-3 px-4">Context Relevance</th>
                  <th className="py-3 px-4">Answer Relevance</th>
                  <th className="py-3 px-4">Composite Score</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800">
                {benchmarks.map((b, i) => (
                  <tr key={i} className="hover:bg-slate-800/40 transition">
                    <td className="py-3.5 px-4 font-semibold text-white flex items-center gap-2">
                      <Trophy className={`h-4 w-4 ${i === 0 ? 'text-amber-400' : 'text-slate-500'}`} />
                      {b.model}
                    </td>
                    <td className="py-3.5 px-4 text-emerald-400 font-mono">{b.faithfulness}</td>
                    <td className="py-3.5 px-4 text-cyan-400 font-mono">{b.contextRelevance}</td>
                    <td className="py-3.5 px-4 text-indigo-400 font-mono">{b.answerRelevance}</td>
                    <td className="py-3.5 px-4 font-bold text-white font-mono">{b.score} / 10.0</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}
