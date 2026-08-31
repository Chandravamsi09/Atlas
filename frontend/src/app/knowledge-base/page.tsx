import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Database, UploadCloud, Search, CheckCircle2 } from "lucide-react";

export default function KnowledgeBasePage() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16]">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Enterprise Knowledge Bases & Vector Stores</h1>
            <p className="text-sm text-slate-400">Manage vector embeddings, document chunking pipelines, and hybrid search indexes.</p>
          </div>
          <Button className="flex items-center gap-2">
            <UploadCloud className="h-4 w-4" /> Ingest Documents
          </Button>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-base">
                <span>Product Documentation</span>
                <span className="h-2.5 w-2.5 rounded-full bg-emerald-500"></span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-xs text-slate-400 space-y-2">
                <p>Chunks: 4,120</p>
                <p>Embedding: text-embedding-3-small (1536d)</p>
                <p>Index: HNSW + BM25 Reciprocal Rank Fusion</p>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-base">
                <span>Legal & Compliance Corpus</span>
                <span className="h-2.5 w-2.5 rounded-full bg-emerald-500"></span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-xs text-slate-400 space-y-2">
                <p>Chunks: 12,840</p>
                <p>Embedding: Cohere-embed-v3 (1024d)</p>
                <p>Index: Cross-Encoder Rerank Active</p>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-base">
                <span>Internal Engineering Wikis</span>
                <span className="h-2.5 w-2.5 rounded-full bg-emerald-500"></span>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-xs text-slate-400 space-y-2">
                <p>Chunks: 8,950</p>
                <p>Embedding: BAAI/bge-large-en-v1.5</p>
                <p>Index: Hierarchical Parent-Child</p>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
}
