import React, { useState } from 'react';

interface UserProfileModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSave: () => void;
}

export const UserProfileModal: React.FC<UserProfileModalProps> = ({ isOpen, onClose, onSave }) => {
  const [name, setName] = useState(() => localStorage.getItem('rishan_user_name') || 'Rishan');
  const [email, setEmail] = useState(() => localStorage.getItem('rishan_user_email') || 'rishan@rishan.ai');
  const [role, setRole] = useState(() => localStorage.getItem('rishan_user_role') || 'Business Owner');
  const [avatar, setAvatar] = useState(() => localStorage.getItem('rishan_user_avatar') || '👤');

  if (!isOpen) return null;

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    localStorage.setItem('rishan_user_name', name);
    localStorage.setItem('rishan_user_email', email);
    localStorage.setItem('rishan_user_role', role);
    localStorage.setItem('rishan_user_avatar', avatar);
    onSave();
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-fade-in">
      <div className="bg-white dark:bg-[#1E1E1E] border border-[#E8E4DB] dark:border-[#2D2D30] rounded-3xl max-w-md w-full p-6 shadow-2xl space-y-6">
        <div className="flex justify-between items-center border-b border-gray-100 dark:border-[#2D2D30] pb-4">
          <h3 className="text-xl font-extrabold text-[#1E1E1E] dark:text-white flex items-center space-x-2">
            <span>⚙️</span>
            <span>User Profile & Settings</span>
          </h3>
          <button onClick={onClose} className="text-gray-400 hover:text-[#0EA5E9] font-bold p-1">✕</button>
        </div>

        <form onSubmit={handleSave} className="space-y-4 text-xs font-semibold">
          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Full Name</label>
            <input
              type="text"
              value={name}
              onChange={e => setName(e.target.value)}
              className="w-full p-2.5 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
              required
            />
          </div>

          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Work Email</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full p-2.5 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
              required
            />
          </div>

          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Role / Department</label>
            <select
              value={role}
              onChange={e => setRole(e.target.value)}
              className="w-full p-2.5 rounded-xl border border-gray-200 dark:border-zinc-700 bg-gray-50 dark:bg-zinc-800 text-[#1E1E1E] dark:text-white font-bold"
            >
              <option value="Business Owner">Business Owner / Executive</option>
              <option value="RevOps Lead">RevOps & Operations Lead</option>
              <option value="Marketing Manager">Marketing Specialist</option>
              <option value="IT Director">IT & Security Director</option>
              <option value="Sales Operations">Sales Manager</option>
            </select>
          </div>

          <div>
            <label className="block text-[#5A574F] dark:text-gray-300 mb-1">Avatar Emoji</label>
            <div className="flex space-x-2">
              {['👤', '⚡', '🤖', '🚀', '💼', '🎯'].map(emoji => (
                <button
                  type="button"
                  key={emoji}
                  onClick={() => setAvatar(emoji)}
                  className={`p-2 text-xl rounded-xl border transition ${avatar === emoji ? 'border-[#0EA5E9] bg-[#0EA5E9]/10' : 'border-gray-200 dark:border-zinc-700'}`}
                >
                  {emoji}
                </button>
              ))}
            </div>
          </div>

          <div className="flex space-x-3 pt-4 border-t border-gray-100 dark:border-[#2D2D30]">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 py-2.5 rounded-xl border border-gray-300 dark:border-zinc-700 text-[#5A574F] dark:text-gray-300 font-bold hover:bg-gray-100 dark:hover:bg-zinc-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="flex-1 py-2.5 rounded-xl bg-[#0EA5E9] hover:bg-[#0284C7] text-white font-bold shadow-md"
            >
              Save Profile
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
