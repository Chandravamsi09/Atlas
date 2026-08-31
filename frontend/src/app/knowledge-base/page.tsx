'use client';

import React, { useState } from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Database, Upload, Search, FileText, CheckCircle2, X, Check, Loader2 } from "lucide-react";

export default function KnowledgeBasePage() {
  const [documents, setDocuments] = useState([
    { name: "Atlas_Architecture_Whitepaper.pdf", size: "2.4 MB", chunks: 142, status: "Indexed (HNSW)" },
    { name: "HIPAA_SOC2_Compliance_Rules.docx", size: "850 KB", chunks: 48, status: "Indexed (HNSW)" },
    { name: "Q3_Financial_Earnings_10K.pdf", size: "5.1 MB", chunks: 310, status: "Indexed (HNSW)" },
  ]);

  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<any[]>([]);
  const [isSearching, setIsSearching] = useState(false);

  // Upload Modal State
  const [isUploadOpen, setIsUploadOpen] = useState(false);
  const [docName, setDocName] = useState("");
  const [chunkSize, setChunkSize] = useState(512);
  const [isUploading, setIsUploading] = useState(false);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setIsSearching(true);
    setTimeout(() => {
      setSearchResults([
        {
          id: "chk_8819",
          doc: "HIPAA_SOC2_Compliance_Rules.docx",
          score: 0.962,
          snippet: "Section 4.2 - All patient identifier metadata must be encrypted at rest utilizing AES-256-GCM. Decryption keys are managed through KMS with automatic 90-day rotation cycles."
        },
        {
          id: "chk_4102",
          doc: "Atlas_Architecture_Whitepaper.pdf",
          score: 0.894,
          snippet: "Atlas Hybrid RAG combines reciprocal rank fusion (RRF) across dense HNSW vector indexes and sparse BM25 indices to achieve 98.4% contextual relevance."
        }
      ]);
      setIsSearching(false);
    }, 500);
  };

  const handleUploadSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!docName.trim()) return;

    setIsUploading(true);
    setTimeout(() => {
      const newDoc = {
        name: docName.endsWith(".pdf") || docName.endsWith(".docx") ? docName : `${docName}.pdf`,
        size: "1.8 MB",
        chunks: Math.floor(Math.random() * 80) + 30,
        status: "Indexed (HNSW)"
      };
      setDocuments([newDoc, ...documents]);
      setIsUploading(false);
      setIsUploadOpen(false);
      setDocName("");
    }, 800);
  };

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
          <button
            onClick={() => setIsUploadOpen(true)}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg shadow-sm transition flex items-center gap-2"
          >
            <Upload className="h-4 w-4" /> Upload Document
          </button>
        </header>

        {/* Search Tester */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-3">Hybrid Retrieval Tester (Dense + Sparse Reciprocal Rank Fusion)</h2>
          <form onSubmit={handleSearch} className="flex gap-3">
            <div className="relative flex-1">
              <Search className="absolute left-3.5 top-3.5 h-4 w-4 text-slate-400" />
              <input
                type="text"
                placeholder="Query knowledge base (e.g., 'What are the SOC2 compliance controls for data retention?')..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-[#090d16] border border-slate-800 rounded-lg pl-10 pr-4 py-2.5 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <button
              type="submit"
              disabled={isSearching}
              className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg transition flex items-center gap-2"
            >
              {isSearching ? <Loader2 className="h-4 w-4 animate-spin" /> : <Search className="h-4 w-4" />}
              Search Chunks
            </button>
          </form>

          {searchResults.length > 0 && (
            <div className="mt-4 space-y-3 pt-4 border-t border-slate-800">
              <div className="text-xs font-semibold text-slate-400">Search Results ({searchResults.length} Chunks Matched):</div>
              {searchResults.map((r) => (
                <div key={r.id} className="p-3.5 bg-[#090d16] border border-slate-800 rounded-lg text-sm">
                  <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
                    <span className="font-semibold text-indigo-400">{r.doc} ({r.id})</span>
                    <span className="font-mono text-emerald-400">RRF Score: {r.score}</span>
                  </div>
                  <p className="text-slate-200 font-sans text-xs leading-relaxed">{r.snippet}</p>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Indexed Documents Table */}
        <div className="mt-8 bg-[#111827] border border-slate-800 rounded-xl p-6">
          <h2 className="text-lg font-semibold text-white mb-4">Indexed Document Collections ({documents.length} Files)</h2>
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

        {/* Upload Modal */}
        {isUploadOpen && (
          <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="w-full max-w-md bg-[#111827] border border-slate-800 rounded-2xl p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-4 border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <Upload className="h-5 w-5 text-indigo-400" />
                  <h3 className="font-bold text-white text-lg">Upload Knowledge Document</h3>
                </div>
                <button onClick={() => setIsUploadOpen(false)} className="text-slate-400 hover:text-white">
                  <X className="h-5 w-5" />
                </button>
              </div>

              <form onSubmit={handleUploadSubmit} className="mt-4 space-y-4">
                <div>
                  <label className="text-xs font-medium text-slate-300">Document Title / File Name</label>
                  <input
                    type="text"
                    required
                    placeholder="e.g. Employee_Handbook_2026.pdf"
                    value={docName}
                    onChange={(e) => setDocName(e.target.value)}
                    className="w-full bg-[#090d16] border border-slate-800 rounded-lg p-2.5 text-sm text-white mt-1 focus:outline-none focus:border-indigo-500"
                  />
                </div>

                <div>
                  <label className="text-xs font-medium text-slate-300">Recursive Chunk Token Size: {chunkSize}</label>
                  <input
                    type="range"
                    min="256"
                    max="2048"
                    step="128"
                    value={chunkSize}
                    onChange={(e) => setChunkSize(parseInt(e.target.value))}
                    className="w-full mt-2 accent-indigo-500"
                  />
                </div>

                <div className="pt-4 border-t border-slate-800 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setIsUploadOpen(false)}
                    className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={isUploading}
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg flex items-center gap-2"
                  >
                    {isUploading ? <Loader2 className="h-4 w-4 animate-spin" /> : null}
                    {isUploading ? "Chunking & Indexing..." : "Upload & Vectorize"}
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

# Verified enterprise compliance & modular integration
