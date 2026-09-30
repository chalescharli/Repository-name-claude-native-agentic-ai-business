import React from 'react';

export const EnterprisePage: React.FC = () => {
  return (
    <div className="space-y-12">
      <section className="text-center space-y-3 max-w-2xl mx-auto pt-6">
        <span className="inline-block bg-[#0EA5E9]/10 text-[#0EA5E9] font-black px-4 py-1.5 rounded-full text-xs">
          Enterprise Security & Governance
        </span>
        <h1 className="text-4xl font-black text-[#1E1E1E] dark:text-white">
          Built for <span className="text-[#0EA5E9]">Enterprise Security & HITL Safety</span>
        </h1>
        <p className="text-sm font-semibold text-[#5A574F] dark:text-gray-300">
          Scale AI adoption safely with risk classification, RBAC, human approval gateways, and complete audit trails.
        </p>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 shadow-sm space-y-3">
          <div className="text-3xl">🛡️</div>
          <h3 className="text-lg font-black text-[#1E1E1E] dark:text-white">Human-in-the-Loop Gateway</h3>
          <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400">
            High-risk tool execution (e.g. sending emails, cancelling bookings) requires explicit approval before firing.
          </p>
        </div>

        <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 shadow-sm space-y-3">
          <div className="text-3xl">🔐</div>
          <h3 className="text-lg font-black text-[#1E1E1E] dark:text-white">Data Privacy & Zero Training</h3>
          <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400">
            Your proprietary business data is never used to train public LLM models. Encrypted in transit and at rest.
          </p>
        </div>

        <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 shadow-sm space-y-3">
          <div className="text-3xl">📜</div>
          <h3 className="text-lg font-black text-[#1E1E1E] dark:text-white">Audit Trail & Compliance</h3>
          <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400">
            Every agent action, tool input, approval comment, and response is recorded in centralized structured logs.
          </p>
        </div>
      </section>
    </div>
  );
};
