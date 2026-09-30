import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('rishan@rishan.ai');
  const [password, setPassword] = useState('••••••••');
  const navigate = useNavigate();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    localStorage.setItem('rishan_user_logged_in', 'true');
    localStorage.setItem('rishan_user_email', email);
    navigate('/dashboard');
  };

  return (
    <div className="max-w-md mx-auto pt-10">
      <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl p-8 shadow-2xl space-y-6">
        <div className="text-center space-y-2">
          <div className="text-4xl">🔐</div>
          <h2 className="text-2xl font-black text-[#1E1E1E] dark:text-white">Welcome Back</h2>
          <p className="text-xs font-semibold text-[#5A574F] dark:text-gray-400">
            Sign in to access your Rishan AI Business Platform.
          </p>
        </div>

        <form onSubmit={handleLogin} className="space-y-4 text-xs font-semibold">
          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Email Address</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full p-3 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
              required
            />
          </div>

          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Password</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full p-3 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full py-3 rounded-xl bg-[#0EA5E9] hover:bg-[#0284C7] text-white font-extrabold text-sm shadow-md transition"
          >
            Sign In to Workstation 🚀
          </button>
        </form>
      </div>
    </div>
  );
};
