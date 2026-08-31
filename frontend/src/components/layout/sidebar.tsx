import React from "react";
import Link from "next/link";
import { 
  Bot, 
  Terminal, 
  Layers, 
  Database, 
  ShieldAlert, 
  CheckCircle2, 
  Activity, 
  Key, 
  Settings, 
  BarChart3 
} from "lucide-react";

const NAV_ITEMS = [
  { name: "Overview", href: "/", icon: BarChart3 },
  { name: "Prompt Studio", href: "/prompt-studio", icon: Terminal },
  { name: "Model Playground", href: "/playground", icon: Bot },
  { name: "Workflow Canvas", href: "/workflows", icon: Layers },
  { name: "Knowledge Base", href: "/knowledge-base", icon: Database },
  { name: "Guardrails & Safety", href: "/guardrails", icon: ShieldAlert },
  { name: "Evaluations & Benchmarks", href: "/evaluation", icon: CheckCircle2 },
  { name: "Traces & Observability", href: "/traces", icon: Activity },
  { name: "API Keys & Quotas", href: "/api-keys", icon: Key },
  { name: "Settings", href: "/settings", icon: Settings },
];

export function Sidebar() {
  return (
    <aside className="w-64 border-r border-slate-800 bg-[#0d1322] flex flex-col justify-between p-4 h-screen sticky top-0">
      <div>
        <div className="flex items-center gap-3 px-3 py-4 border-b border-slate-800/80 mb-6">
          <div className="h-8 w-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-indigo-500/30">
            A
          </div>
          <div>
            <h1 className="font-semibold text-white tracking-wide">Atlas AI</h1>
            <p className="text-xs text-slate-400">Enterprise LLMOps</p>
          </div>
        </div>

        <nav className="space-y-1.5">
          {NAV_ITEMS.map((item) => (
            <Link
              key={item.name}
              href={item.href}
              className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-indigo-600/10 hover:text-indigo-400 transition-colors"
            >
              <item.icon className="h-4 w-4" />
              <span>{item.name}</span>
            </Link>
          ))}
        </nav>
      </div>

      <div className="border-t border-slate-800 pt-4 px-2">
        <div className="flex items-center justify-between text-xs text-slate-400">
          <span>Tenant: Acme Corp</span>
          <span className="h-2 w-2 rounded-full bg-emerald-500"></span>
        </div>
      </div>
    </aside>
  );
}
