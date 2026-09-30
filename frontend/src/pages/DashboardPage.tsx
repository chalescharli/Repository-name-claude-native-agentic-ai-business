import React from 'react';
import { PromptSimulator } from '../components/PromptSimulator';

export const DashboardPage: React.FC = () => {
  const agentCards = [
    { title: "BookingAgent", role: "TrekkSoft Tour Reservations & Schedules", badge: "TrekkSoft MCP", icon: "🎫" },
    { title: "SalesAgent", role: "Lead Follow-ups & Email Automation", badge: "M365 Email", icon: "💼" },
    { title: "OperationsAgent", role: "SharePoint SOP Knowledge & Refund Rules", badge: "SharePoint RAG", icon: "⚙️" },
    { title: "MarketingAgent", role: "Brevo Email Campaigns & Customer Segments", badge: "Brevo MCP", icon: "📈" },
    { title: "ManagementAgent", role: "Executive Daily Activity Summaries", badge: "Analytics MCP", icon: "📊" }
  ];

  return (
    <div className="space-y-12">
      {/* Hero Header */}
      <section className="text-center space-y-4 max-w-3xl mx-auto pt-6">
        <span className="inline-block bg-[#0EA5E9]/10 text-[#0EA5E9] font-black px-4 py-1.5 rounded-full text-xs">
          Enterprise Agentic AI Workforce v1.0
        </span>
        <h1 className="text-4xl sm:text-5xl font-black text-[#1E1E1E] dark:text-white tracking-tight">
          Meet your new <span className="text-[#0EA5E9]">AI Business Teammates</span>
        </h1>
        <p className="text-base text-[#5A574F] dark:text-gray-300 font-semibold leading-relaxed">
          Orchestrate specialized AI agents across TrekkSoft, Microsoft 365, SharePoint, Brevo, and custom tools with built-in Risk-Based Human-in-the-Loop safety controls.
        </p>
      </section>

      {/* Prompt Simulator */}
      <section>
        <PromptSimulator />
      </section>

      {/* Active Agent Cards */}
      <section className="space-y-6">
        <h2 className="text-2xl font-black text-[#1E1E1E] dark:text-white">Active AI Workforce Agents</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {agentCards.map((agent, idx) => (
            <div key={idx} className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 shadow-sm hover:shadow-xl hover:border-[#0EA5E9] transition group space-y-3">
              <div className="flex justify-between items-start">
                <span className="text-3xl">{agent.icon}</span>
                <span className="bg-sky-50 dark:bg-zinc-800 text-[#0EA5E9] text-[10px] font-black px-2.5 py-1 rounded-full border border-sky-200 dark:border-zinc-700">
                  {agent.badge}
                </span>
              </div>
              <h3 className="text-lg font-black text-[#1E1E1E] dark:text-white group-hover:text-[#0EA5E9] transition">
                {agent.title}
              </h3>
              <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400 leading-relaxed">
                {agent.role}
              </p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
