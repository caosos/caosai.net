import React, { useState } from 'react';
import './styles/globals.css';
import Starfield from './components/shell/Starfield';
import Header from './components/shell/Header';
import Sidebar from './components/sidebar/Sidebar';
import ChatPane from './components/chat/ChatPane';
import Composer from './components/chat/Composer';
import { SidebarView } from './types';
import { useChat } from './hooks/useChat';
import { useModels } from './hooks/useModels';

export default function App() {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [activeView, setActiveView] = useState<SidebarView>('threads');

  const { threads, activeThread, activeThreadId, loading, newThread, selectThread, sendMessage } =
    useChat();
  const { availableModels, activeModel, selectModel } = useModels();

  const messages = activeThread?.messages ?? [];

  const handleSend = (text: string) => {
    sendMessage(text, activeModel?.provider, activeModel?.model);
  };

  const estimatedTokens = messages.reduce(
    (acc, m) => acc + Math.ceil(m.content.length / 3.8),
    0
  );

  const mainLeft = sidebarOpen ? 'var(--caos-sidebar-width)' : '0';

  return (
    <div style={{ height: '100vh', width: '100vw', position: 'relative', overflow: 'hidden' }}>
      <Starfield />

      <Sidebar
        open={sidebarOpen}
        activeView={activeView}
        onViewChange={setActiveView}
        onClose={() => setSidebarOpen(false)}
        threads={threads}
        activeThreadId={activeThreadId}
        onSelectThread={(id) => {
          selectThread(id);
          setActiveView('threads');
        }}
        onNewThread={() => {
          newThread();
          setActiveView('threads');
        }}
      />

      <div
        style={{
          position: 'fixed',
          top: 0,
          left: mainLeft,
          right: 0,
          bottom: 0,
          display: 'flex',
          flexDirection: 'column',
          transition: 'left var(--caos-transition)',
          zIndex: 10,
        }}
      >
        <Header
          threadTitle={activeThread?.title}
          activeModel={activeModel}
          tokensUsed={estimatedTokens}
          sidebarOpen={sidebarOpen}
          onToggleSidebar={() => setSidebarOpen(true)}
          activeView={activeView}
        />

        <div
          style={{
            flex: 1,
            paddingTop: 'var(--caos-header-height)',
            paddingBottom: 'calc(var(--caos-composer-height) + 32px)',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <ChatPane messages={messages} loading={loading} onPrompt={handleSend} />
        </div>

        <Composer
          onSend={handleSend}
          disabled={loading}
          activeModel={activeModel}
          availableModels={availableModels}
          onSelectModel={selectModel}
        />
      </div>
    </div>
  );
}
