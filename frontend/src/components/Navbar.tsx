import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';

interface NavbarProps {
  onOpenProfile: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenProfile }) => {
  const location = useLocation();
  const [theme, setTheme] = useState<'light' | 'dark'>(() => {
    return (localStorage.getItem('rishan_theme') as 'light' | 'dark') || 'light';
  });

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('rishan_theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'));
  };

  const username = localStorage.getItem('rishan_user_name') || 'Rishan';

  return (
    <header className="sticky top-0 z-40 bg-[#FFFDF9]/90 dark:bg-[#121212]/90 backdrop-blur-md border-b border-[#E8E4DB] dark:border-[#2D2D30] transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand Logo */}
        <Link to="/dashboard" className="flex items-center space-x-2">
          <span className="text-[#0EA5E9] font-black text-3xl">_</span>
          <span className="text-2xl font-black tracking-tight text-[#1E1E1E] dark:text-white">rishan</span>
          <span className="text-[10px] bg-[#0EA5E9]/10 text-[#0EA5E9] px-2 py-0.5 rounded-full font-bold ml-1">Agents</span>
        </Link>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center space-x-6 text-sm font-semibold">
          <Link to="/dashboard" className={`hover:text-[#0EA5E9] transition ${location.pathname === '/dashboard' ? 'text-[#0EA5E9] font-bold' : 'text-[#4A4740] dark:text-gray-300'}`}>
            Dashboard
          </Link>
          <Link to="/team?team=revops" className={`hover:text-[#0EA5E9] transition ${location.pathname === '/team' ? 'text-[#0EA5E9] font-bold' : 'text-[#4A4740] dark:text-gray-300'}`}>
            Team Solutions
          </Link>
          <Link to="/explore" className={`hover:text-[#0EA5E9] transition ${location.pathname === '/explore' ? 'text-[#0EA5E9] font-bold' : 'text-[#4A4740] dark:text-gray-300'}`}>
            Explore Apps (9000+)
          </Link>
          <Link to="/enterprise" className={`hover:text-[#0EA5E9] transition ${location.pathname === '/enterprise' ? 'text-[#0EA5E9] font-bold' : 'text-[#4A4740] dark:text-gray-300'}`}>
            Enterprise
          </Link>
          <Link to="/resources" className={`hover:text-[#0EA5E9] transition ${location.pathname === '/resources' ? 'text-[#0EA5E9] font-bold' : 'text-[#4A4740] dark:text-gray-300'}`}>
            Resources
          </Link>
        </nav>

        {/* Action Controls */}
        <div className="flex items-center space-x-3">
          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className="p-2 rounded-xl bg-gray-100 dark:bg-[#2A2A2D] text-[#1E1E1E] dark:text-gray-200 hover:text-[#0EA5E9] transition text-sm font-bold flex items-center space-x-1"
            title="Toggle Light/Dark Theme"
          >
            <span>{theme === 'dark' ? '🌙 Dark' : '☀️ Light'}</span>
          </button>

          {/* User Profile Button */}
          <button
            onClick={onOpenProfile}
            className="flex items-center space-x-2 p-1.5 px-3 rounded-xl bg-[#0EA5E9]/10 text-[#0EA5E9] hover:bg-[#0EA5E9]/20 transition font-bold text-xs"
          >
            <span>👤</span>
            <span>{username}</span>
          </button>

          <Link
            to="/login"
            className="bg-[#0EA5E9] hover:bg-[#0284C7] text-white px-4 py-2 rounded-xl text-xs font-bold transition shadow-sm"
          >
            Sign In
          </Link>
        </div>
      </div>
    </header>
  );
};
