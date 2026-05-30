import React from 'react';
import { ChatReceipt, ModelContextSpec } from '../../types';

interface HeaderProps {
  threadTitle?: string;
  activeModel?: ModelContextSpec;
  tokensUsed: number;
  onNewThread: () => void;
  receipt?: ChatReceipt;
}

function formatLat(ms: number): string {
  if (!ms) return '—';
  if (ms < 1000) return `${Math.round(ms)}ms`;
  return `${(ms / 1000).toFixed(1)}s`;
}

export default function Header({ threadTitle, activeModel, tokensUsed, onNewThread, receipt }: HeaderProps) {
  const now = new Date();
  const dateStr = now.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

  return (
    <header style={{
      position: 'fixed',
      top: 0,
      left: 200,
      right: 0,
      height: 48,
      zIndex: 50,
      display: 'flex',
      alignItems: 'center',
      padding: '0 16px',
      background: 'rgba(6,6,15,0.7)',
      backdropFilter: 'blur(20px)',
      borderBottom: '1px solid var(--caos-border)',
    }}>
      {/* Left — WCW strip (only after first chat turn) */}
      {receipt && (
        <div
          data-testid="wcw-strip"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 12,
            fontSize: 10,
            color: 'var(--caos-text-muted)',
            letterSpacing: '0.06em',
            textTransform: 'uppercase',
          }}
        >
          <span><span style={{ opacity: 0.7 }}>SENT</span> <span style={{ color: 'var(--caos-text-dim)' }}>{receipt.userTokens}</span></span>
          <span><span style={{ opacity: 0.7 }}>RECV</span> <span style={{ color: 'var(--caos-text-dim)' }}>{receipt.assistantTokens}</span></span>
          <span><span style={{ opacity: 0.7 }}>THREAD</span> <span style={{ color: 'var(--caos-text-dim)' }}>{receipt.threadTotalTokens}</span></span>
          <span><span style={{ opacity: 0.7 }}>LAT</span> <span style={{ color: 'var(--caos-text-dim)' }}>{formatLat(receipt.latencyMs)}</span></span>
        </div>
      )}

      {/* Center — CAOS brand */}
      <div style={{
        position: 'absolute',
        left: '50%',
        transform: 'translateX(-50%)',
        fontSize: 13,
        fontWeight: 700,
        letterSpacing: '0.18em',
        color: 'var(--caos-text-dim)',
        textTransform: 'uppercase',
      }}>
        CAOS
      </div>

      {/* Right — thread controls */}
      <div style={{
        marginLeft: 'auto',
        display: 'flex',
        alignItems: 'center',
        gap: 8,
      }}>
        <button
          onClick={onNewThread}
          style={{
            fontSize: 11,
            color: 'var(--caos-text-dim)',
            padding: '5px 10px',
            background: 'rgba(255,255,255,0.05)',
            border: '1px solid var(--caos-border)',
            borderRadius: 6,
            letterSpacing: '0.04em',
            display: 'flex',
            alignItems: 'center',
            gap: 5,
          }}
        >
          <span>✏️</span> New Thread
        </button>
        <button style={{
          fontSize: 11,
          color: 'var(--caos-text-dim)',
          padding: '5px 10px',
          background: 'rgba(255,255,255,0.05)',
          border: '1px solid var(--caos-border)',
          borderRadius: 6,
          letterSpacing: '0.04em',
          display: 'flex',
          alignItems: 'center',
          gap: 5,
        }}>
          <span>🔍</span> Search this thread
        </button>
        <span style={{ fontSize: 11, color: 'var(--caos-text-muted)', marginLeft: 4 }}>
          {dateStr}
        </span>
      </div>
    </header>
  );
}
