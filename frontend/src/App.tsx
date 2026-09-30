import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { UserProfileModal } from './components/UserProfileModal';
import { DashboardPage } from './pages/DashboardPage';
import { ExplorePage } from './pages/ExplorePage';
import { TeamPage } from './pages/TeamPage';
import { EnterprisePage } from './pages/EnterprisePage';
import { ResourcesPage } from './pages/ResourcesPage';
import { LoginPage } from './pages/LoginPage';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

export const App: React.FC = () => {
  const [isProfileOpen, setIsProfileOpen] = useState(false);

  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen flex flex-col justify-between bg-[#FFFDF9] dark:bg-[#121212] text-[#1E1E1E] dark:text-gray-100 transition-colors duration-300">
          <div>
            <Navbar onOpenProfile={() => setIsProfileOpen(true)} />
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
              <Routes>
                <Route path="/" element={<Navigate to="/login" replace />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/dashboard" element={<DashboardPage />} />
                <Route path="/explore" element={<ExplorePage />} />
                <Route path="/team" element={<TeamPage />} />
                <Route path="/enterprise" element={<EnterprisePage />} />
                <Route path="/resources" element={<ResourcesPage />} />
              </Routes>
            </main>
          </div>
          <Footer />

          <UserProfileModal
            isOpen={isProfileOpen}
            onClose={() => setIsProfileOpen(false)}
            onSave={() => {}}
          />
        </div>
      </Router>
    </QueryClientProvider>
  );
};

export default App;
