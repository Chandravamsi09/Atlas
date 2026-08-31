'use client';

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAuth } from "@/context/auth-context";
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
  BarChart3,
  LogOut,
  UserCircle
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
  const pathname = usePathname();
  const { user, organization, logout } = useAuth();

  return (
    <aside className="w-64 border-r border-slate-800 bg-[#0d1322] flex flex-col justify-between p-4 h-screen sticky top-0 shrink-0">
      <div className="overflow-y-auto">
        <div className="flex items-center gap-3 px-3 py-4 border-b border-slate-800/80 mb-6">
          <div className="h-8 w-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white shadow-lg shadow-indigo-500/30">
            A
          </div>
          <div>
            <h1 className="font-semibold text-white tracking-wide">Atlas AI</h1>
            <p className="text-xs text-slate-400">Enterprise LLMOps</p>
          </div>
        </div>

        <nav className="space-y-1">
          {NAV_ITEMS.map((item) => {
            const isActive = pathname === item.href;
            return (
              <Link
                key={item.name}
                href={item.href}
                className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors ${
                  isActive
                    ? "bg-indigo-600 text-white font-medium shadow-sm"
                    : "text-slate-300 hover:bg-slate-800/60 hover:text-white"
                }`}
              >
                <item.icon className={`h-4 w-4 ${isActive ? "text-white" : "text-slate-400"}`} />
                <span>{item.name}</span>
              </Link>
            );
          })}
        </nav>
      </div>

      <div className="border-t border-slate-800 pt-4 px-2 space-y-3">
        <div className="flex items-center justify-between text-xs text-slate-400">
          <div className="flex items-center gap-2 truncate">
            <UserCircle className="h-4 w-4 text-slate-400 shrink-0" />
            <span className="truncate font-medium text-slate-300">{user?.full_name || "Admin"}</span>
          </div>
          <span className="h-2 w-2 rounded-full bg-emerald-500 shrink-0" title="Connected"></span>
        </div>
        <div className="text-[11px] text-slate-500 truncate">
          Tenant: {organization?.name || "Acme Corp"} ({organization?.role || "owner"})
        </div>
        <button
          onClick={logout}
          className="w-full flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg bg-slate-800/60 hover:bg-rose-500/10 hover:text-rose-400 text-xs text-slate-400 transition"
        >
          <LogOut className="h-3.5 w-3.5" /> Sign Out
        </button>
      </div>
    </aside>
  );
}
