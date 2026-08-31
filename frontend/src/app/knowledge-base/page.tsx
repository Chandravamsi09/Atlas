'use client';

import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Database, Upload, Search, FileText, CheckCircle2 } from "lucide-react";

export default function KnowledgeBasePage() {
  const documents = [
    { name: "Atlas_Architecture_Whitepaper.pdf", size: "2.4 MB", chunks: 142, status: "Indexed (HNSW)" },
    { name: "HIPAA_SOC2_Compliance_Rules.docx", size: "850 KB", chunks: 48, status: "Indexed (HNSW)" },
    { name: "Q3_Financial_Earnings_10K.pdf", size: "5.1 MB", chunks: 310, status: "Indexed (HNSW)" },
  ];

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-y-auto">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Database className="h-6 w-6 text-cyan-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Knowledge Base & Hybrid RAG</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Multi-modal document parser, recursive chunking, pgvector HNSW indexing, and Cross-Encoder reranking.</p>
          </div>
          <button className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2">
            <Upload className="h-4 w-4" /> Upload Document
          </button>
        </header>

        {/* Search Tester */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-3">Hybrid Retrieval Tester (Dense + Sparse Reciprocal Rank Fusion)</h2>
          <div className="flex gap-3">
            <div className="relative flex-1">
              <Search className="absolute left-3.5 top-3.5 h-4 w-4 text-slate-400" />
              <input
                type="text"
                placeholder="Query knowledge base (e.g., 'What are the SOC2 compliance controls for data retention?')..."
                className="w-full bg-[#090d16] border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <button className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg transition">
              Search Chunks
            </button>
          </div>
        </div>

        {/* Indexed Documents Table */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Indexed Document Collections (500 Chunks Total)</h2>
          <div className="divide-y divide-slate-800">
            {documents.map((doc, idx) => (
              <div key={idx} className="py-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <FileText className="h-5 w-5 text-indigo-400" />
                  <div>
                    <h3 className="font-semibold text-slate-200">{doc.name}</h3>
                    <p className="text-xs text-slate-400">{doc.size} • {doc.chunks} Semantic Chunks</p>
                  </div>
                </div>
                <span className="px-2.5 py-1 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 flex items-center gap-1">
                  <CheckCircle2 className="h-3 w-3" /> {doc.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
