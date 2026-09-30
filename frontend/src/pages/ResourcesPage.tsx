import React from 'react';

export const ResourcesPage: React.FC = () => {
  const articles = [
    { title: "3-Phase AI Playbook for Enterprise Teams", cat: "Strategic Guide", readTime: "5 min read" },
    { title: "Model Context Protocol (MCP) Integration Specification", cat: "Technical Doc", readTime: "8 min read" },
    { title: "Building RAG Knowledge Stores with SharePoint", cat: "Architecture", readTime: "6 min read" },
    { title: "Configuring Risk-Based Human-in-the-Loop Gateways", cat: "Security", readTime: "4 min read" }
  ];

  return (
    <div className="space-y-8">
      <section className="text-center space-y-3 max-w-2xl mx-auto pt-6">
        <h1 className="text-4xl font-black text-[#1E1E1E] dark:text-white">
          Resources & <span className="text-[#0EA5E9]">Knowledge Hub</span>
        </h1>
        <p className="text-sm font-semibold text-[#5A574F] dark:text-gray-300">
          Guides, playbooks, API documentation, and tutorials for building enterprise agentic systems.
        </p>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {articles.map((art, idx) => (
          <div key={idx} className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 shadow-sm hover:shadow-xl hover:border-[#0EA5E9] transition space-y-3">
            <div className="flex justify-between items-center text-xs font-bold">
              <span className="bg-sky-50 dark:bg-zinc-800 text-[#0EA5E9] px-2.5 py-1 rounded-full">{art.cat}</span>
              <span className="text-gray-400">{art.readTime}</span>
            </div>
            <h3 className="text-lg font-black text-[#1E1E1E] dark:text-white">{art.title}</h3>
            <button className="text-xs font-extrabold text-[#0EA5E9] hover:underline flex items-center space-x-1">
              <span>Read Full Playbook</span>
              <span>➔</span>
            </button>
          </div>
        ))}
      </section>
    </div>
  );
};
