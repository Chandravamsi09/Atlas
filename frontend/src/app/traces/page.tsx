import React from "react";
import { Sidebar } from "@/components/layout/sidebar";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Activity, Clock, Cpu, CheckCircle2 } from "lucide-react";

export default function TracesPage() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-8 bg-[#090d16]">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">OpenTelemetry Live Traces & Waterfalls</h1>
            <p className="text-sm text-slate-400">Inspect granular execution spans, prompt tokens, tool latency, and provider responses.</p>
          </div>
        </header>

        <div className="mt-8">
          <Card>
            <CardHeader>
              <CardTitle>Recent Request Traces</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="divide-y divide-slate-800">
                <div className="py-3 flex items-center justify-between text-sm">
                  <div>
                    <span className="font-mono text-indigo-400">trace_8a9689da5ca9</span>
                    <span className="ml-3 text-slate-300">POST /api/v1/chat/completions</span>
                  </div>
                  <div className="flex items-center gap-6 text-xs text-slate-400">
                    <span>Model: gpt-4o</span>
                    <span>Duration: 184ms</span>
                    <span>Tokens: 142</span>
                    <span className="text-emerald-400 font-semibold">200 OK</span>
                  </div>
                </div>

                <div className="py-3 flex items-center justify-between text-sm">
                  <div>
                    <span className="font-mono text-indigo-400">trace_3b7189fa9de2</span>
                    <span className="ml-3 text-slate-300">POST /api/v1/workflows/execute</span>
                  </div>
                  <div className="flex items-center gap-6 text-xs text-slate-400">
                    <span>Agent DAG: 4 Nodes</span>
                    <span>Duration: 540ms</span>
                    <span>Tokens: 580</span>
                    <span className="text-emerald-400 font-semibold">200 OK</span>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
}
