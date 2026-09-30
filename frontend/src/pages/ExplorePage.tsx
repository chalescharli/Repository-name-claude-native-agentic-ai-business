import React, { useState } from 'react';

export const ExplorePage: React.FC = () => {
  const [search, setSearch] = useState('');

  const apps = [
    { name: 'Salesforce', category: 'CRM & Sales', icon: '☁️', desc: 'Sync leads, contacts, and opportunities with SalesAgent.' },
    { name: 'Microsoft 365', category: 'Productivity', icon: '🟦', desc: 'Create Word drafts, SharePoint SOP search, and Outlook mail.' },
    { name: 'TrekkSoft', category: 'Booking & Tours', icon: '🎫', desc: 'Retrieve live tour availability and customer reservations.' },
    { name: 'Brevo', category: 'Marketing', icon: '📈', desc: 'Stage email newsletters and automated marketing campaigns.' },
    { name: 'HubSpot', category: 'CRM', icon: '🟧', desc: 'Manage deals and customer support tickets seamlessly.' },
    { name: 'Slack', category: 'Communication', icon: '💬', desc: 'Post daily automated agent updates into team channels.' },
    { name: 'Zendesk', category: 'Support', icon: '🛠️', desc: 'Auto-route support tickets to OperationsAgent.' },
    { name: 'Snowflake', category: 'Data Cloud', icon: '❄️', desc: 'Query data warehouse with ManagementAgent.' }
  ];

  const filteredApps = apps.filter(a =>
    a.name.toLowerCase().includes(search.toLowerCase()) ||
    a.category.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-8">
      <section className="text-center space-y-3 max-w-2xl mx-auto pt-6">
        <h1 className="text-4xl font-black text-[#1E1E1E] dark:text-white">
          Explore <span className="text-[#0EA5E9]">9,000+ Apps & Integrations</span>
        </h1>
        <p className="text-sm font-semibold text-[#5A574F] dark:text-gray-300">
          Connect your favorite business software to the Rishan AI Agentic Workforce via Model Context Protocol (MCP).
        </p>

        {/* Search Input */}
        <div className="pt-4 max-w-md mx-auto">
          <input
            type="text"
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Search integrations (e.g. Salesforce, TrekkSoft, Slack)..."
            className="w-full p-3 rounded-2xl border border-gray-200 dark:border-zinc-700 bg-white dark:bg-zinc-800 text-sm font-semibold focus:outline-none focus:ring-2 focus:ring-[#0EA5E9]"
          />
        </div>
      </section>

      {/* App Grid */}
      <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {filteredApps.map((app, idx) => (
          <div key={idx} className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-2xl p-5 shadow-sm hover:shadow-xl hover:border-[#0EA5E9] transition space-y-3">
            <div className="flex justify-between items-center">
              <span className="text-3xl">{app.icon}</span>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-50 dark:bg-zinc-800 text-[#0EA5E9]">
                {app.category}
              </span>
            </div>
            <h3 className="text-base font-extrabold text-[#1E1E1E] dark:text-white">{app.name}</h3>
            <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400">{app.desc}</p>
            <button className="w-full py-2 rounded-xl bg-gray-100 dark:bg-zinc-800 hover:bg-[#0EA5E9] hover:text-white text-xs font-bold transition">
              Connect Integration
            </button>
          </div>
        ))}
      </section>
    </div>
  );
};
