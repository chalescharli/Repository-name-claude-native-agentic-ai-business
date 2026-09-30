import React, { useState } from 'react';
import { useSearchParams } from 'react-router-dom';

export const TeamPage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const currentTeam = searchParams.get('team') || 'revops';

  const teams = [
    { id: 'revops', name: 'RevOps', icon: '📊', title: 'Revenue Operations & Pipeline Intelligence' },
    { id: 'marketing', name: 'Marketing', icon: '🚀', title: 'AI Marketing & Campaign Automation' },
    { id: 'it', name: 'IT & Ops', icon: '💻', title: 'IT Infrastructure & Security Policy Control' },
    { id: 'hr', name: 'HR & People', icon: '👥', title: 'Talent Acquisition & Employee Onboarding' },
    { id: 'sales', name: 'Sales', icon: '🎯', title: 'Sales Prospecting & Follow-up Workflows' },
    { id: 'support', name: 'Customer Support', icon: '🛠️', title: '24/7 Support Ticket Resolution & SOP RAG' },
    { id: 'leaders', name: 'Executive Leaders', icon: '👑', title: 'Strategic Business Summaries & KPIs' },
    { id: 'ea', name: 'Executive Assistants', icon: '📅', title: 'Calendar & Meeting Coordination' }
  ];

  const activeTeamInfo = teams.find(t => t.id === currentTeam) || teams[0];

  return (
    <div className="space-y-8">
      <section className="text-center space-y-3 max-w-2xl mx-auto pt-6">
        <h1 className="text-4xl font-black text-[#1E1E1E] dark:text-white">
          Solutions by <span className="text-[#0EA5E9]">Team & Department</span>
        </h1>
        <p className="text-sm font-semibold text-[#5A574F] dark:text-gray-300">
          Deploy pre-configured AI workforce teams tailored for your department goals.
        </p>
      </section>

      {/* Team Tabs */}
      <div className="flex flex-wrap justify-center gap-2 border-b border-gray-200 dark:border-zinc-800 pb-4">
        {teams.map(team => (
          <button
            key={team.id}
            onClick={() => setSearchParams({ team: team.id })}
            className={`px-4 py-2 rounded-2xl text-xs font-extrabold transition flex items-center space-x-1.5 ${
              currentTeam === team.id
                ? 'bg-[#0EA5E9] text-white shadow-md'
                : 'bg-white dark:bg-zinc-800 text-[#5A574F] dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-zinc-700'
            }`}
          >
            <span>{team.icon}</span>
            <span>{team.name}</span>
          </button>
        ))}
      </div>

      {/* Selected Department Overview */}
      <section className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-8 shadow-xl space-y-6">
        <div className="flex items-center space-x-4 border-b border-gray-100 dark:border-zinc-800 pb-4">
          <span className="text-5xl">{activeTeamInfo.icon}</span>
          <div>
            <h2 className="text-2xl font-black text-[#1E1E1E] dark:text-white">{activeTeamInfo.title}</h2>
            <p className="text-xs font-bold text-[#0EA5E9] uppercase tracking-wider">Dedicated AI Agent Suite</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="p-5 rounded-2xl bg-sky-50/60 dark:bg-zinc-800 border border-sky-100 dark:border-zinc-700 space-y-2">
            <h3 className="font-extrabold text-[#1E1E1E] dark:text-white text-sm">Key Department Capabilities</h3>
            <ul className="space-y-2 text-xs font-semibold text-[#5A574F] dark:text-gray-300">
              <li className="flex items-center space-x-2"><span className="text-[#0EA5E9]">✓</span><span>Automated data sync across CRM, TrekkSoft & M365</span></li>
              <li className="flex items-center space-x-2"><span className="text-[#0EA5E9]">✓</span><span>Risk-evaluated action execution with Human approval</span></li>
              <li className="flex items-center space-x-2"><span className="text-[#0EA5E9]">✓</span><span>Real-time executive logging & audit trail compliance</span></li>
            </ul>
          </div>

          <div className="p-5 rounded-2xl bg-gray-50 dark:bg-zinc-800 border border-gray-200 dark:border-zinc-700 space-y-2">
            <h3 className="font-extrabold text-[#1E1E1E] dark:text-white text-sm">Target Agent Workflows</h3>
            <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400">
              Orchestrate customized system prompts, specialized tools, and knowledge RAG collections for {activeTeamInfo.name}.
            </p>
            <button className="mt-2 bg-[#0EA5E9] text-white px-4 py-2 rounded-xl font-bold text-xs shadow-md">
              Deploy {activeTeamInfo.name} AI Team 🚀
            </button>
          </div>
        </div>
      </section>
    </div>
  );
};
