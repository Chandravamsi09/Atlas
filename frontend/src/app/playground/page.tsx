'use client';

import React, { useState } from "react";
import Link from "next/link";
import { Sidebar } from "@/components/layout/sidebar";
import { api } from "@/lib/api";
import { Bot, Send, Sparkles, AlertCircle, ArrowUpRight, Activity } from "lucide-react";

export default function ModelPlaygroundPage() {
  const [model, setModel] = useState("mock-gpt-4o");
  const [temperature, setTemperature] = useState(0.7);
  const [inputMessage, setInputMessage] = useState("");
  const [messages, setMessages] = useState<Array<{ role: string; content: string; meta?: any }>>([
    {
      role: "assistant",
      content: "Hello! I am connected to the live Atlas AI Gateway. Enter a prompt below to run an inference request through smart routing, safety guardrails, and telemetry logging."
    }
  ]);
  const [isSending, setIsSending] = useState(false);
  const [lastMeta, setLastMeta] = useState<any>(null);
  const [error, setError] = useState("");

  const handleSend = async () => {
    if (!inputMessage.trim() || isSending) return;
    const userMsg = { role: "user", content: inputMessage };
    const newHistory = [...messages, userMsg];
    setMessages(newHistory);
    setInputMessage("");
    setIsSending(true);
    setError("");

    try {
      const response = await api.chat.completions({
        model,
        messages: newHistory.map((m) => ({ role: m.role, content: m.content })),
        temperature,
        enable_cache: true
      });

      const assistantText = response.choices?.[0]?.message?.content || "No response received";
      const usage = response.usage || {};

      const meta = {
        model: response.model || model,
        tokens: usage.total_tokens || 42,
        latency_ms: usage.latency_ms || 210,
        cost_usd: usage.cost_usd || 0.00001,
        trace_id: response.id || `tr_${Math.random().toString(36).substring(2, 9)}`
      };

      setLastMeta(meta);
      setMessages((prev) => [...prev, { role: "assistant", content: assistantText, meta }]);
    } catch (err: any) {
      setError(err.message || "Failed to communicate with Atlas Gateway.");
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: `[Gateway Error]: ${err.message || "Could not route request. Verify the backend is running on http://localhost:8000."}`
        }
      ]);
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className="flex min-h-screen bg-[#090d16] text-slate-100">
      <Sidebar />
      <main className="flex-1 p-8 flex flex-col h-screen overflow-hidden">
        <header className="flex items-center justify-between pb-6 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <Bot className="h-6 w-6 text-cyan-400" />
              <h1 className="text-2xl font-bold text-white tracking-tight">Model Playground</h1>
            </div>
            <p className="text-sm text-slate-400 mt-1">Real-time gateway inference with token metrics, smart routing, and trace generation.</p>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 bg-[#111827] border border-slate-800 rounded-lg px-3 py-1.5">
              <span className="text-xs text-slate-400">Model:</span>
              <select
                value={model}
                onChange={(e) => setModel(e.target.value)}
                className="bg-transparent text-sm text-white focus:outline-none"
              >
                <option value="mock-gpt-4o" className="bg-[#111827]">Local Mock Engine (mock-gpt-4o)</option>
                <option value="mock-claude-3.5" className="bg-[#111827]">Local Mock Engine (mock-claude-3.5)</option>
                <option value="gpt-4o" className="bg-[#111827]">OpenAI (gpt-4o)</option>
                <option value="gpt-4o-mini" className="bg-[#111827]">OpenAI (gpt-4o-mini)</option>
                <option value="claude-3-5-sonnet" className="bg-[#111827]">Anthropic (Claude 3.5 Sonnet)</option>
              </select>
            </div>
            <div className="flex items-center gap-2 bg-[#111827] border border-slate-800 rounded-lg px-3 py-1.5">
              <span className="text-xs text-slate-400">Temp: {temperature}</span>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={temperature}
                onChange={(e) => setTemperature(parseFloat(e.target.value))}
                className="w-20 accent-indigo-500"
              />
            </div>
          </div>
        </header>

        {/* Chat Stream Area */}
        <div className="flex-1 bg-[#111827] border border-slate-800 rounded-xl mt-6 flex flex-col overflow-hidden">
          <div className="flex-1 p-6 overflow-y-auto space-y-4">
            {messages.map((msg, i) => (
              <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div
                  className={`max-w-2xl rounded-xl p-4 text-sm ${
                    msg.role === 'user'
                      ? 'bg-indigo-600 text-white shadow-sm'
                      : 'bg-[#1e293b]/70 border border-slate-800 text-slate-200'
                  }`}
                >
                  <div className="whitespace-pre-wrap">{msg.content}</div>
                  {msg.meta && (
                    <div className="mt-3 pt-3 border-t border-slate-700/60 flex items-center justify-between text-[11px] text-slate-400 font-mono">
                      <span>Model: {msg.meta.model} • {msg.meta.tokens} tokens ({msg.meta.latency_ms.toFixed(1)}ms)</span>
                      <Link href="/traces" className="text-indigo-400 hover:text-indigo-300 flex items-center gap-1">
                        <Activity className="h-3 w-3" /> View in Traces
                      </Link>
                    </div>
                  )}
                </div>
              </div>
            ))}
            {isSending && (
              <div className="flex justify-start">
                <div className="bg-[#1e293b]/70 border border-slate-800 rounded-xl p-4 text-sm text-slate-400 flex items-center gap-2">
                  <Sparkles className="h-4 w-4 animate-spin text-indigo-400" />
                  Routing request via Atlas Gateway...
                </div>
              </div>
            )}
          </div>

          {/* Input Box */}
          <div className="p-4 border-t border-slate-800 bg-[#0d1322]">
            <div className="flex gap-3">
              <input
                type="text"
                className="flex-1 bg-[#090d16] border border-slate-800 rounded-lg px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
                placeholder="Ask anything or simulate high-load concurrent queries..."
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSend()}
              />
              <button
                onClick={handleSend}
                disabled={isSending || !inputMessage.trim()}
                className="px-5 py-3 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white rounded-lg font-medium transition flex items-center gap-2"
              >
                <Send className="h-4 w-4" /> Send
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
