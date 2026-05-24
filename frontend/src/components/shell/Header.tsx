import React from 'react';
import { ModelContextSpec, SidebarView } from '../../types';

interface HeaderProps {
  threadTitle?: string;
  activeModel?: ModelContextSpec;
  tokensUsed: number;
  sidebarOpen: boolean;
  onToggleSidebar: () => void;
  activeView: SidebarView;
}

export default function Header({
  threadTitle,
  activeModel,
  tokensUsed,
  sidebarOpen,
  onToggleSidebar,
  activeView,
}: HeaderProps) {
  const usable = activeModel?.usable_context_tokens ?? 200000;
  const pct = Math.min(100, (tokensUsed / usable) * 100);

  const wcwColor =
    pct > 80 ? '#f87171' : pct > 55 ? '#fbbf24' : 'var(--caos-accent-bright)';

  return (
    <header
      className="glass"
      style={{
        position: 'fixed',
        top: 0,
        left: sidebarOpen ? 'var(--caos-sidebar-width)' : 0,
        right: 0,
        height: 'var(--caos-header-height)',
        zIndex: 50,
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        padding: '0 16px',
        transition: 'left var(--caos-transition)',
        borderTop: 'none',
        borderLeft: 'none',
        borderRight: 'none',
        borderRadius: 0,
      }}
    >
      {!sidebarOpen && (
        <button
          onClick={onToggleSidebar}
          style={{ opacity: 0.7, fontSize: 18, lineHeight: 1, padding: '4px 6px' }}
          title="Open sidebar"
        >
          ☰
        </button>
      )}

      <div style={{ display: 'flex', alignItems: 'center', gap: 8, flex: 1, minWidth: 0 }}>
        <span style={{
          fontWeight: 600,
          fontSize: 13,
          letterSpacing: '0.08em',
          color: 'var(--caos-accent-bright)',
          textTransform: 'uppercase',
          flexShrink: 0,
        }}>
          CAOS
        </span>
        {threadTitle && (
          <>
            <span style={{ color: 'var(--caos-text-muted)', fontSize: 12 }}>/</span>
            <span style={{
              fontSize: 13,
              color: 'var(--caos-text-dim)',
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap',
            }}>
              {threadTitle}
            </span>
          </>
        )}
      </div>

      {/* WCW meter */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, flexShrink: 0 }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 3 }}>
          <span style={{ fontSize: 10, color: 'var(--caos-text-muted)', letterSpacing: '0.06em' }}>
            CONTEXT
          </span>
          <span style={{ fontSize: 11, color: wcwColor, fontVariantNumeric: 'tabular-nums' }}>
            {(tokensUsed / 1000).toFixed(1)}K / {(usable / 1000).toFixed(0)}K
          </span>
        </div>
        <div style={{
          width: 60,
          height: 4,
          background: 'rgba(255,255,255,0.08)',
          borderRadius: 2,
          overflow: 'hidden',
        }}>
          <div style={{
            width: `${pct}%`,
            height: '100%',
            background: wcwColor,
            borderRadius: 2,
            transition: 'width 0.4s ease, background 0.4s ease',
          }} />
        </div>
      </div>

      {activeModel && (
        <div style={{
          fontSize: 11,
          color: 'var(--caos-text-muted)',
          padding: '3px 8px',
          background: 'rgba(124,92,191,0.12)',
          borderRadius: 6,
          border: '1px solid var(--caos-border)',
          flexShrink: 0,
        }}>
          {activeModel.display_name}
        </div>
      )}
    </header>
  );
}
