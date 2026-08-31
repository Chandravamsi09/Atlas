'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Layers, Plus, Play, GitMerge, CheckCircle, ShieldAlert, Cpu, X, Check, Loader2 } from "lucide-react";

export default function WorkflowsPage() {
  const [workflows, setWorkflows] = useState([
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
  ]);

  // Modal State
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newWfName, setNewWfName] = useState("");
  const [newWfType, setNewWfType] = useState("ReAct Reasoning Loop");
  const [newWfNodes, setNewWfNodes] = useState(4);

  // Execution Simulation State
  const [isExecuting, setIsExecuting] = useState(false);
  const [execStep, setExecStep] = useState(0);
  const [execOutput, setExecOutput] = useState("");

  // Edit Modal State
  const [editWorkflow, setEditWorkflow] = useState<any>(null);

  const handleCreateWorkflow = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newWfName.trim()) return;

    const newWf = {
      id: `wf_${Math.random().toString(36).substring(2, 8)}`,
      name: newWfName,
      status: "Active",
      nodes: Number(newWfNodes),
      lastRun: "Just now",
      successRate: "100%"
    };

    setWorkflows([newWf, ...workflows]);
    setNewWfName("");
    setIsModalOpen(false);
  };

  const handleRunExecution = () => {
    setIsExecuting(true);
    setExecStep(1);
    setExecOutput("Node 1: Input Router -> Classifying incoming payload as 'High Priority Financial Report'...");

    setTimeout(() => {
      setExecStep(2);
      setExecOutput("Node 2: Hybrid RAG -> Performing dense pgvector (HNSW) + sparse BM25 retrieval across 500 document chunks...");
    }, 1000);

    setTimeout(() => {
      setExecStep(3);
      setExecOutput("Node 3: ReAct Loop -> Executing reasoning cycle and tool sandbox invocation (AST Python 3)...");
    }, 2000);

    setTimeout(() => {
      setExecStep(4);
      setExecOutput("DAG Execution Complete (420ms). All guardrail checks passed. Output payload synthesized successfully.");
      setIsExecuting(false);
    }, 3000);
  };

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
          <button
            onClick={() => setIsModalOpen(true)}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2"
          >
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
            <button
              onClick={handleRunExecution}
              disabled={isExecuting}
              className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white rounded-lg text-xs font-semibold flex items-center gap-2 transition"
            >
              {isExecuting ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : <Play className="h-3.5 w-3.5" />}
              {isExecuting ? `Running Step ${execStep}/3...` : "Execute Test Flow"}
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-4 mt-6 items-center">
            <div className={`border rounded-lg p-4 text-center transition ${execStep >= 1 ? 'bg-indigo-600/20 border-indigo-500' : 'bg-[#1e293b]/70 border-slate-700'}`}>
              <div className="text-xs font-semibold text-indigo-400 mb-1">Node 1: Input Router</div>
              <div className="text-sm font-bold text-white">Classifier</div>
              <div className="text-xs text-emerald-400 mt-2">{execStep >= 1 ? "✓ Running / Done (45ms)" : "Ready"}</div>
            </div>

            <div className="text-center text-slate-600 font-bold hidden md:block">→</div>

            <div className={`border rounded-lg p-4 text-center transition ${execStep >= 2 ? 'bg-cyan-600/20 border-cyan-500' : 'bg-[#1e293b]/70 border-slate-700'}`}>
              <div className="text-xs font-semibold text-cyan-400 mb-1">Node 2: Hybrid RAG</div>
              <div className="text-sm font-bold text-white">pgvector + BM25</div>
              <div className="text-xs text-emerald-400 mt-2">{execStep >= 2 ? "✓ Running / Done (85ms)" : "Queued"}</div>
            </div>

            <div className="text-center text-slate-600 font-bold hidden md:block">→</div>

            <div className={`border rounded-lg p-4 text-center transition ${execStep >= 3 ? 'bg-amber-600/20 border-amber-500' : 'bg-[#1e293b]/70 border-slate-700'}`}>
              <div className="text-xs font-semibold text-amber-400 mb-1">Node 3: ReAct Loop</div>
              <div className="text-sm font-bold text-white">Reasoning + Tools</div>
              <div className="text-xs text-emerald-400 mt-2">{execStep >= 3 ? "✓ Completed (310ms)" : "Queued"}</div>
            </div>
          </div>

          {execOutput && (
            <div className="mt-4 p-3 bg-[#090d16] border border-slate-800 rounded-lg text-xs font-mono text-slate-300">
              <span className="text-emerald-400 font-bold">[Execution Log]:</span> {execOutput}
            </div>
          )}
        </div>

        {/* Workflow List Table */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Configured DAG Pipelines ({workflows.length})</h2>
          <div className="divide-y divide-slate-800">
            {workflows.map((wf) => (
              <div key={wf.id} className="py-4 flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-slate-200">{wf.name}</h3>
                  <div className="flex items-center gap-4 text-xs text-slate-400 mt-1">
                    <span className="font-mono text-indigo-400">{wf.id}</span>
                    <span>Nodes: {wf.nodes}</span>
                    <span>Last Run: {wf.lastRun}</span>
                    <span className="text-emerald-400">Success: {wf.successRate}</span>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`px-2.5 py-1 text-xs rounded-full border ${wf.status === 'Active' ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : 'bg-slate-800 text-slate-400 border-slate-700'}`}>
                    {wf.status}
                  </span>
                  <button
                    onClick={() => setEditWorkflow(wf)}
                    className="px-3 py-1.5 text-xs bg-slate-800 hover:bg-slate-700 text-white rounded-lg border border-slate-700 transition"
                  >
                    Edit Graph
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Create Workflow Modal */}
        {isModalOpen && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-lg bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <Layers className="h-5 w-5 text-indigo-400" />
                  <h3 className="font-bold text-white text-lg">Create New Workflow DAG</h3>
                </div>
                <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <form onSubmit={handleCreateWorkflow} className="space-y-4 mt-4">
                <div>
                  <label className="text-xs font-medium text-slate-300">Pipeline Name</label>
                  <input
                    type="text"
                    required
                    placeholder="e.g. Customer Support Ticket Auto-Resolver"
                    value={newWfName}
                    onChange={(e) => setNewWfName(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none focus:border-indigo-500"
                  />
                </div>

                <div>
                  <label className="text-xs font-medium text-slate-300">Workflow Topology Template</label>
                  <select
                    value={newWfType}
                    onChange={(e) => setNewWfType(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none"
                  >
                    <option value="ReAct Reasoning Loop">ReAct Reasoning Loop (Iterative Tools)</option>
                    <option value="Hybrid RAG Multi-Hop">Hybrid RAG Multi-Hop Document Synthesis</option>
                    <option value="Plan and Solve">Plan and Solve Sequential Decomposition</option>
                    <option value="Security SAST Reviewer">Security SAST & Vulnerability Auditor</option>
                  </select>
                </div>

                <div>
                  <label className="text-xs font-medium text-slate-300">Initial Node Count: {newWfNodes}</label>
                  <input
                    type="range"
                    min="3"
                    max="10"
                    value={newWfNodes}
                    onChange={(e) => setNewWfNodes(parseInt(e.target.value))}
                    className="w-full mt-2 accent-indigo-500"
                  />
                </div>

                <div className="pt-4 border-t border-slate-800 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setIsModalOpen(false)}
                    className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg shadow-sm"
                  >
                    Save & Initialize DAG
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Edit Graph Modal */}
        {editWorkflow && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-lg bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div>
                  <h3 className="font-bold text-white text-lg">Graph Settings: {editWorkflow.name}</h3>
                  <p className="text-xs text-slate-400 font-mono">{editWorkflow.id}</p>
                </div>
                <button onClick={() => setEditWorkflow(null)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <div className="mt-4 space-y-3 text-sm">
                <div className="p-3 bg-[#090d16] border border-slate-800 rounded-lg">
                  <div className="text-xs text-slate-400">Execution Status</div>
                  <div className="text-emerald-400 font-bold mt-0.5">{editWorkflow.status}</div>
                </div>
                <div className="p-3 bg-[#090d16] border border-slate-800 rounded-lg">
                  <div className="text-xs text-slate-400">Success Rate</div>
                  <div className="text-white font-mono mt-0.5">{editWorkflow.successRate}</div>
                </div>
                <div className="p-3 bg-[#090d16] border border-slate-800 rounded-lg">
                  <div className="text-xs text-slate-400">Configured Tool Sandbox</div>
                  <div className="text-slate-200 mt-0.5">Python 3 AST, SQL Warehouse, Vector Search</div>
                </div>
              </div>

              <div className="pt-5 border-t border-slate-800 mt-5 flex justify-end">
                <button
                  onClick={() => setEditWorkflow(null)}
                  className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg"
                >
                  Done
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
