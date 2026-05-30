import React, { useState } from 'react';
import './styles/globals.css';
import Starfield from './components/shell/Starfield';
import Header from './components/shell/Header';
import Sidebar from './components/sidebar/Sidebar';
import ChatPane from './components/chat/ChatPane';
import Composer from './components/chat/Composer';
import AgentPlayground from './components/agent/AgentPlayground';
import { SidebarView } from './types';
import { useChat } from './hooks/useChat';
import { useModels } from './hooks/useModels';

const SIDEBAR_WIDTH = 200;

export default function App() {
  const [activeView, setActiveView] = useState<SidebarView>('threads');

  const { threads, activeThread, activeThreadId, loading, lastLatencyMs, totalTokens, lastReceipt, newThread, selectThread, sendMessage } =
    useChat();
  const { availableModels, activeModel, selectModel } = useModels();

  const messages = activeThread?.messages ?? [];

  const handleSend = (text: string) => {
    sendMessage(text, activeModel?.provider, activeModel?.model);
  };

  const displayTokens = totalTokens || messages.reduce(
    (acc, m) => acc + Math.ceil(m.content.length / 3.8),
    0
  );

  return (
    <div style={{ height: '100vh', width: '100vw', position: 'relative', overflow: 'hidden' }}>
      <Starfield />

      <Sidebar
        activeView={activeView}
        onViewChange={setActiveView}
        threads={threads}
        activeThreadId={activeThreadId}
        onSelectThread={selectThread}
        onNewThread={newThread}
      />

      {/* Main content area — offset by sidebar width */}
      <div style={{
        position: 'fixed',
        top: 0,
        left: SIDEBAR_WIDTH,
        right: 0,
        bottom: 0,
        display: 'flex',
        flexDirection: 'column',
        zIndex: 10,
      }}>
        <Header
          threadTitle={activeThread?.title}
          activeModel={activeModel}
          tokensUsed={displayTokens}
          onNewThread={newThread}
          receipt={lastReceipt}
        />

        {activeView === 'agent_playground' ? (
          <AgentPlayground />
        ) : (
          <>
            {/* Chat area */}
            <div style={{
              flex: 1,
              paddingTop: 48,
              paddingBottom: 90,
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
            }}>
              <ChatPane messages={messages} loading={loading} onPrompt={handleSend} />
            </div>

            <Composer
              onSend={handleSend}
              disabled={loading}
              activeModel={activeModel}
              availableModels={availableModels}
              onSelectModel={selectModel}
              tokensUsed={displayTokens}
              lastLatencyMs={lastLatencyMs}
            />
          </>
        )}
      </div>
    </div>
  );
}
