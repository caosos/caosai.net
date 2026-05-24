import React from 'react';
import { SidebarView, Thread } from '../../types';

interface SidebarProps {
  open: boolean;
  activeView: SidebarView;
  onViewChange: (v: SidebarView) => void;
  onClose: () => void;
  threads: Thread[];
  activeThreadId?: string;
  onSelectThread: (id: string) => void;
  onNewThread: () => void;
}

const NAV: { id: SidebarView; label: string; icon: string }[] = [
  { id: 'threads', label: 'Threads', icon: '💬' },
  { id: 'memory', label: 'Memory', icon: '🧠' },
  { id: 'artifacts', label: 'Desktop', icon: '📁' },
  { id: 'settings', label: 'Settings', icon: '⚙️' },
  { id: 'admin', label: 'Admin', icon: '🛡️' },
];

export default function Sidebar({
  open,
  activeView,
  onViewChange,
  onClose,
  threads,
  activeThreadId,
  onSelectThread,
  onNewThread,
}: SidebarProps) {
  return (
    <aside
      className="glass"
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        bottom: 0,
        width: 'var(--caos-sidebar-width)',
        zIndex: 60,
        display: 'flex',
        flexDirection: 'column',
        transform: open ? 'translateX(0)' : 'translateX(-100%)',
        transition: 'transform var(--caos-transition)',
        borderTop: 'none',
        borderBottom: 'none',
        borderLeft: 'none',
        borderRadius: 0,
      }}
    >
      {/* Sidebar header */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '14px 16px',
        borderBottom: '1px solid var(--caos-border)',
        flexShrink: 0,
      }}>
        <span style={{
          fontWeight: 700,
          fontSize: 15,
          letterSpacing: '0.1em',
          color: 'var(--caos-accent-bright)',
        }}>
          CAOS
        </span>
        <button
          onClick={onClose}
          style={{ opacity: 0.5, fontSize: 16, padding: '2px 6px' }}
          title="Close sidebar"
        >
          ✕
        </button>
      </div>

      {/* Nav */}
      <nav style={{ flexShrink: 0, padding: '8px 0', borderBottom: '1px solid var(--caos-border)' }}>
        {NAV.map((item) => (
          <button
            key={item.id}
            onClick={() => onViewChange(item.id)}
            style={{
              width: '100%',
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '9px 16px',
              fontSize: 13,
              fontWeight: activeView === item.id ? 600 : 400,
              color: activeView === item.id ? 'var(--caos-accent-bright)' : 'var(--caos-text-dim)',
              background: activeView === item.id ? 'rgba(124,92,191,0.12)' : 'transparent',
              borderRadius: 0,
              textAlign: 'left',
              transition: 'all var(--caos-transition)',
            }}
          >
            <span style={{ fontSize: 15 }}>{item.icon}</span>
            {item.label}
          </button>
        ))}
      </nav>

      {/* Content area */}
      <div style={{ flex: 1, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
        {activeView === 'threads' && (
          <ThreadList
            threads={threads}
            activeThreadId={activeThreadId}
            onSelect={onSelectThread}
            onNew={onNewThread}
          />
        )}
        {activeView !== 'threads' && (
          <div style={{
            flex: 1,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--caos-text-muted)',
            fontSize: 12,
            flexDirection: 'column',
            gap: 8,
          }}>
            <span style={{ fontSize: 28 }}>{NAV.find(n => n.id === activeView)?.icon}</span>
            <span>{NAV.find(n => n.id === activeView)?.label}</span>
            <span style={{ fontSize: 11, opacity: 0.6 }}>Coming soon</span>
          </div>
        )}
      </div>

      {/* Footer */}
      <div style={{
        padding: '12px 16px',
        borderTop: '1px solid var(--caos-border)',
        flexShrink: 0,
      }}>
        <div style={{ fontSize: 11, color: 'var(--caos-text-muted)' }}>
          Aria · CAOS v0.1
        </div>
      </div>
    </aside>
  );
}

function ThreadList({
  threads,
  activeThreadId,
  onSelect,
  onNew,
}: {
  threads: Thread[];
  activeThreadId?: string;
  onSelect: (id: string) => void;
  onNew: () => void;
}) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <div style={{ padding: '10px 12px', flexShrink: 0 }}>
        <button
          onClick={onNew}
          style={{
            width: '100%',
            padding: '8px 12px',
            background: 'rgba(124,92,191,0.15)',
            border: '1px solid var(--caos-border)',
            borderRadius: 'var(--caos-radius-sm)',
            color: 'var(--caos-accent-bright)',
            fontSize: 12,
            fontWeight: 600,
            letterSpacing: '0.05em',
          }}
        >
          + New Thread
        </button>
      </div>
      <div style={{ flex: 1, overflowY: 'auto', padding: '0 8px 8px' }}>
        {threads.length === 0 && (
          <div style={{
            textAlign: 'center',
            color: 'var(--caos-text-muted)',
            fontSize: 12,
            padding: '24px 12px',
          }}>
            No threads yet.<br />Start a conversation.
          </div>
        )}
        {threads.map((t) => (
          <button
            key={t.thread_id}
            onClick={() => onSelect(t.thread_id)}
            style={{
              width: '100%',
              textAlign: 'left',
              padding: '9px 10px',
              marginBottom: 2,
              borderRadius: 'var(--caos-radius-sm)',
              background:
                activeThreadId === t.thread_id
                  ? 'rgba(124,92,191,0.18)'
                  : 'transparent',
              border:
                activeThreadId === t.thread_id
                  ? '1px solid rgba(124,92,191,0.3)'
                  : '1px solid transparent',
              transition: 'all var(--caos-transition)',
            }}
          >
            <div style={{
              fontSize: 12,
              color: activeThreadId === t.thread_id ? 'var(--caos-text)' : 'var(--caos-text-dim)',
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap',
              fontWeight: activeThreadId === t.thread_id ? 500 : 400,
            }}>
              {t.title || 'Untitled thread'}
            </div>
            <div style={{ fontSize: 10, color: 'var(--caos-text-muted)', marginTop: 2 }}>
              {t.message_count} message{t.message_count !== 1 ? 's' : ''}
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
