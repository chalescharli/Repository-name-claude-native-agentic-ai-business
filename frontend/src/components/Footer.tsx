import React from 'react';
import { Link } from 'react-router-dom';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-[#FAF8F5] dark:bg-[#1A1A1D] border-t border-[#E8E4DB] dark:border-[#2D2D30] py-12 mt-20 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0 text-xs text-[#6E6A60] dark:text-gray-400">
        <div className="flex items-center space-x-2">
          <span className="text-[#0EA5E9] font-black text-xl">_</span>
          <span className="font-bold text-[#1E1E1E] dark:text-white">rishan AI Agents</span>
          <span>© {new Date().getFullYear()} Enterprise Agentic Business Platform</span>
        </div>
        <div className="flex items-center space-x-6 font-semibold">
          <Link to="/dashboard" className="hover:text-[#0EA5E9] transition">Dashboard</Link>
          <Link to="/team?team=revops" className="hover:text-[#0EA5E9] transition">Team Solutions</Link>
          <Link to="/explore" className="hover:text-[#0EA5E9] transition">Explore Apps</Link>
          <Link to="/enterprise" className="hover:text-[#0EA5E9] transition">Enterprise</Link>
          <Link to="/resources" className="hover:text-[#0EA5E9] transition">Resources</Link>
        </div>
      </div>
    </footer>
  );
};
