import React, { useState } from 'react';
import { ChatMessage } from '../../types';
import MarkdownRenderer from './MarkdownRenderer';

interface MessageBubbleProps {
  message: ChatMessage;
}

function formatLatency(ms: number): string {
  if (ms < 1000) return `${Math.round(ms)}ms`;
  return `${(ms / 1000).toFixed(1)}s`;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === 'user';
  const [copied, setCopied] = useState(false);
  const [useful, setUseful] = useState(false);

  const bubbleContent = isUser ? (
    <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
      {message.content}
    </span>
  ) : (
    <MarkdownRenderer content={message.content} />
  );

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // clipboard blocked — silent fail, no fake success
    }
  };

  const actionBase: React.CSSProperties = {
    background: 'none',
    border: 'none',
    padding: 0,
    fontSize: 11,
    fontFamily: 'inherit',
    letterSpacing: '0.02em',
  };
  const activeStyle: React.CSSProperties = {
    ...actionBase,
    color: 'var(--caos-text-dim)',
    cursor: 'pointer',
  };
  const stubStyle: React.CSSProperties = {
    ...actionBase,
    color: 'var(--caos-text-muted)',
    opacity: 0.5,
    cursor: 'default',
  };
  const separator = (
    <span style={{ color: 'var(--caos-text-muted)', fontSize: 11, opacity: 0.6 }}>·</span>
  );

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: isUser ? 'flex-end' : 'flex-start',
      padding: '4px 0',
    }}>
      <div style={{
        fontSize: 10,
        color: 'var(--caos-text-muted)',
        marginBottom: 4,
        letterSpacing: '0.06em',
        textTransform: 'uppercase',
        paddingLeft: isUser ? 0 : 2,
        paddingRight: isUser ? 2 : 0,
      }}>
        {isUser ? 'You' : 'Aria'}
      </div>
      <div
        className={isUser ? '' : 'glass-2'}
        style={{
          maxWidth: '78%',
          padding: '11px 15px',
          borderRadius: isUser
            ? '14px 14px 4px 14px'
            : '4px 14px 14px 14px',
          background: isUser ? 'var(--caos-user-bubble)' : undefined,
          border: isUser ? '1px solid rgba(124, 92, 191, 0.25)' : undefined,
          fontSize: 14,
          lineHeight: 1.65,
          color: 'var(--caos-text)',
        }}
      >
        {bubbleContent}
      </div>
      {!isUser && (
        <div
          data-testid="message-meta"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 8,
            marginTop: 6,
            paddingLeft: 2,
            flexWrap: 'wrap',
          }}
        >
          {typeof message.latency_ms === 'number' && message.latency_ms > 0 && (
            <span
              title="Time to first response"
              style={{
                fontSize: 10,
                color: 'var(--caos-text-muted)',
                padding: '2px 7px',
                borderRadius: 10,
                border: '1px solid var(--caos-border)',
                background: 'rgba(255,255,255,0.03)',
                letterSpacing: '0.04em',
              }}
            >
              {formatLatency(message.latency_ms)}
            </span>
          )}
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <button onClick={handleCopy} style={activeStyle} title="Copy message">
              {copied ? 'Copied!' : 'Copy'}
            </button>
            {separator}
            <button style={stubStyle} title="Re-read aloud (coming soon)">Re-Read</button>
            {separator}
            <button style={stubStyle} title="Send via email (coming soon)">Mail</button>
            {separator}
            <button style={stubStyle} title="Reply with context (coming soon)">Reply</button>
            {separator}
            <button
              onClick={() => setUseful((v) => !v)}
              style={{ ...activeStyle, color: useful ? 'var(--caos-accent-bright, #b8a4ff)' : 'var(--caos-text-dim)' }}
              title="Mark useful"
            >
              {useful ? '✓ Useful' : 'Useful'}
            </button>
            {separator}
            <button style={stubStyle} title="Show reasoning (coming soon)">Why?</button>
          </div>
        </div>
      )}
    </div>
  );
}
