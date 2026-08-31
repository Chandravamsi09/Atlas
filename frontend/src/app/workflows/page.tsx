'use client';

import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Layers, Plus, Play, GitMerge, CheckCircle, ShieldAlert, Cpu } from "lucide-react";

export default function WorkflowsPage() {
  const workflows = [
    {
      id: "wf_legal_01",
      name: "Legal Contract Risk & NDA Reviewer",
      status: "Active",
      nodes: 5,
      lastRun: "2 mins ago",
      successRate: "99.4%"
    },
    {
      id: "wf_rag_02",
      name: "Multi-Hop Enterprise RAG Synthesis",
      status: "Active",
      nodes: 7,
      lastRun: "15 mins ago",
      successRate: "98.8%"
    },
    {
      id: "wf_finance_03",
      name: "10-K SEC Filing Financial Extractor",
      status: "Paused",
      nodes: 4,
      lastRun: "3 hours ago",
      successRate: "100%"
    }
  ];

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Layers className="h-6 w-6 text-indigo-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Agent DAG Workflows</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Multi-step autonomous agent DAG graphs with branching, human-in-the-loop, and sandboxed tool execution.</p>
          </div>
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2">
            <Plus className="h-4 w-4" /> New Workflow DAG
          </button>
        </header>

        {/* Visual Graph Preview Card */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <div className="flex items-center justify-between pb-4 border-b border-slate-800">
            <div>
              <h2 className="text-lg font-semibold text-white">Active DAG Execution Graph (Visual Canvas)</h2>
              <p className="text-xs text-slate-400">Live topological node state machine.</p>
            </div>
            <button className="px-3 py-1.5 bg-emerald-600/20 text-emerald-400 border border-emerald-500/30 rounded-lg text-xs font-semibold flex items-center gap-1.5">
              <Play className="h-3.5 w-3.5" /> Execute Test Flow
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mt-6 items-center">
            <div className="bg-[#1e293b]/70 border border-indigo-500/50 rounded-lg p-4 text-center">
              <div className="text-xs font-semibold text-indigo-400 mb-1">Node 1: Input Router</div>
              <div className="text-sm font-bold text-white">Classifier</div>
              <div className="text-xs text-emerald-400 mt-2">✓ Completed (45ms)</div>
            </div>

            <div className="text-center text-slate-600 font-bold hidden md:block">→</div>

            <div className="bg-[#1e293b]/70 border border-cyan-500/50 rounded-lg p-4 text-center">
              <div className="text-xs font-semibold text-cyan-400 mb-1">Node 2: Hybrid RAG</div>
              <div className="text-sm font-bold text-white">pgvector + BM25</div>
              <div className="text-xs text-emerald-400 mt-2">✓ Completed (85ms)</div>
            </div>

            <div className="text-center text-slate-600 font-bold hidden md:block">→</div>

            <div className="bg-[#1e293b]/70 border border-amber-500/50 rounded-lg p-4 text-center">
              <div className="text-xs font-semibold text-amber-400 mb-1">Node 3: ReAct Loop</div>
              <div className="text-sm font-bold text-white">Reasoning + Tools</div>
              <div className="text-xs text-emerald-400 mt-2">✓ Completed (310ms)</div>
            </div>
          </div>
        </div>

        {/* Workflow List Table */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Configured DAG Pipelines</h2>
          <div className="divide-y divide-slate-800">
            {workflows.map((wf) => (
              <div key={wf.id} className="py-4 flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-slate-200">{wf.name}</h3>
                  <div className="flex items-center gap-4 text-xs text-slate-400 mt-1">
                    <span>ID: {wf.id}</span>
                    <span>Nodes: {wf.nodes}</span>
                    <span>Last Run: {wf.lastRun}</span>
                    <span className="text-emerald-400">Success: {wf.successRate}</span>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`px-2.5 py-1 text-xs rounded-full border ${wf.status === 'Active' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : 'bg-slate-800 text-slate-400 border-slate-700'}`}>
                    {wf.status}
                  </span>
                  <button className="px-3 py-1.5 text-xs bg-slate-800 hover:bg-slate-700 text-white rounded-lg border border-slate-700 transition">
                    Edit Graph
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
