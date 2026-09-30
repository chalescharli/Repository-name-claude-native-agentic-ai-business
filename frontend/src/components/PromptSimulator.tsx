import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { apiClient } from '../services/apiClient';

export const PromptSimulator: React.FC = () => {
  const [prompt, setPrompt] = useState("Show me today's tour bookings from TrekkSoft.");
  const [provider, setProvider] = useState<'anthropic' | 'openai' | 'gemini'>('anthropic');

  const queryMutation = useMutation({
    mutationFn: (userQuery: string) => apiClient.queryAgent({ query: userQuery, provider }),
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim()) return;
    queryMutation.mutate(prompt);
  };

  const examplePrompts = [
    "Show me today's tour bookings from TrekkSoft.",
    "What is our procedure for handling a cancelled tour in SharePoint?",
    "Prepare follow-up emails for yesterday's customers.",
    "Prepare a Brevo email campaign for previous customers.",
    "Give me an executive summary of today's business activity."
  ];

  return (
    <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-6 sm:p-8 shadow-xl space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h3 className="text-xl font-extrabold text-[#1E1E1E] dark:text-white flex items-center space-x-2">
            <span>⚡</span>
            <span>Live Agentic AI Prompt Workstation</span>
          </h3>
          <p className="text-xs font-semibold text-[#6E6A60] dark:text-gray-400 mt-1">
            Test prompt routing across BookingAgent, SalesAgent, MarketingAgent, OperationsAgent & ManagementAgent.
          </p>
        </div>

        {/* LLM Provider Picker */}
        <div className="flex items-center space-x-2 text-xs font-bold">
          <span className="text-[#5A574F] dark:text-gray-300">Model Provider:</span>
          <select
            value={provider}
            onChange={e => setProvider(e.target.value as any)}
            className="p-2 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
          >
            <option value="anthropic">Claude 3.5 Sonnet</option>
            <option value="openai">OpenAI GPT-4o</option>
            <option value="gemini">Google Gemini 1.5 Pro</option>
          </select>
        </div>
      </div>

      {/* Preset Buttons */}
      <div className="flex flex-wrap gap-2">
        {examplePrompts.map((p, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => setPrompt(p)}
            className="text-[11px] font-bold px-3 py-1.5 rounded-full border border-sky-200 dark:border-zinc-700 bg-sky-50/60 dark:bg-zinc-800 text-[#0EA5E9] hover:bg-[#0EA5E9] hover:text-white transition"
          >
            {p}
          </button>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="relative">
          <textarea
            value={prompt}
            onChange={e => setPrompt(e.target.value)}
            rows={3}
            className="w-full p-4 rounded-2xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-semibold text-sm focus:outline-none focus:ring-2 focus:ring-[#0EA5E9]"
            placeholder="Ask your AI workforce to perform tasks..."
          />
          <button
            type="submit"
            disabled={queryMutation.isPending}
            className="absolute bottom-4 right-4 bg-[#0EA5E9] hover:bg-[#0284C7] disabled:opacity-50 text-white font-bold px-5 py-2 rounded-xl text-xs shadow-md transition flex items-center space-x-1"
          >
            <span>{queryMutation.isPending ? 'Routing...' : 'Execute Prompt 🚀'}</span>
          </button>
        </div>
      </form>

      {/* Execution Results */}
      {queryMutation.isPending && (
        <div className="p-4 rounded-2xl bg-sky-50 dark:bg-zinc-800 border border-sky-200 text-xs font-bold text-[#0EA5E9] animate-pulse">
          ⏳ Router analyzing prompt intent and selecting target agent...
        </div>
      )}

      {queryMutation.isError && (
        <div className="p-4 rounded-2xl bg-red-50 dark:bg-red-950/40 border border-red-200 text-xs font-bold text-red-600 dark:text-red-400">
          ❌ Error executing query: {(queryMutation.error as Error).message}
        </div>
      )}

      {queryMutation.isSuccess && (
        <div className="p-6 rounded-2xl bg-gray-50 dark:bg-zinc-800/80 border border-gray-200 dark:border-zinc-700 space-y-4 text-xs font-semibold">
          <div className="flex items-center justify-between border-b border-gray-200 dark:border-zinc-700 pb-3">
            <span className="font-extrabold text-[#1E1E1E] dark:text-white text-sm">Target Agent:</span>
            <span className="bg-[#0EA5E9]/10 text-[#0EA5E9] font-black px-3 py-1 rounded-full text-xs">
              🤖 {queryMutation.data.data.routed_to}
            </span>
          </div>

          <div>
            <span className="block font-bold text-[#5A574F] dark:text-gray-400 mb-1">Execution Payload:</span>
            <pre className="p-4 rounded-xl bg-gray-900 text-green-400 font-mono text-[11px] overflow-x-auto">
              {JSON.stringify(queryMutation.data.data.execution, null, 2)}
            </pre>
          </div>
        </div>
      )}
    </div>
  );
};
