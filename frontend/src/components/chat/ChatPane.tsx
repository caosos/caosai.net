import React, { useEffect, useRef, useState } from 'react';
import { ChatMessage } from '../../types';
import MessageBubble from './MessageBubble';
import WelcomeScreen from './WelcomeScreen';

interface ChatPaneProps {
  messages: ChatMessage[];
  loading?: boolean;
  onPrompt: (text: string) => void;
}

export default function ChatPane({ messages, loading, onPrompt }: ChatPaneProps) {
  const bottomRef = useRef<HTMLDivElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);
  const [showJump, setShowJump] = useState(false);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const onScroll = () => {
    const el = scrollRef.current;
    if (!el) return;
    const distFromBottom = el.scrollHeight - el.scrollTop - el.clientHeight;
    setShowJump(distFromBottom > 120);
  };

  const jumpToBottom = () => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const isEmpty = messages.length === 0;

  return (
    <div style={{ position: 'relative', height: '100%', display: 'flex', flexDirection: 'column' }}>
      <div
        ref={scrollRef}
        onScroll={onScroll}
        style={{
          flex: 1,
          overflowY: 'auto',
          padding: isEmpty ? 0 : '20px 24px 16px',
          display: 'flex',
          flexDirection: 'column',
          gap: 8,
        }}
      >
        {isEmpty ? (
          <WelcomeScreen onPrompt={onPrompt} />
        ) : (
          messages.map((msg, i) => <MessageBubble key={i} message={msg} />)
        )}

        {loading && (
          <div style={{ display: 'flex', alignItems: 'flex-start', padding: '4px 0' }}>
            <div
              className="glass-2"
              style={{
                padding: '11px 16px',
                borderRadius: '4px 14px 14px 14px',
                display: 'flex',
                gap: 5,
                alignItems: 'center',
              }}
            >
              {[0, 1, 2].map((i) => (
                <span
                  key={i}
                  style={{
                    width: 6,
                    height: 6,
                    borderRadius: '50%',
                    background: 'var(--caos-accent-bright)',
                    display: 'inline-block',
                    animation: `pulse 1.2s ease-in-out ${i * 0.2}s infinite`,
                    opacity: 0.7,
                  }}
                />
              ))}
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {showJump && (
        <button
          onClick={jumpToBottom}
          style={{
            position: 'absolute',
            bottom: 12,
            right: 16,
            width: 34,
            height: 34,
            borderRadius: '50%',
            background: 'var(--caos-surface)',
            border: '1px solid var(--caos-border)',
            fontSize: 14,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 4px 16px rgba(0,0,0,0.4)',
          }}
          title="Jump to latest"
        >
          ↓
        </button>
      )}

      <style>{`
        @keyframes pulse {
          0%, 80%, 100% { transform: scale(0.7); opacity: 0.4; }
          40% { transform: scale(1); opacity: 1; }
        }
      `}</style>
    </div>
  );
}
