import React, { useState } from 'react';
import { SidebarView, Thread } from '../../types';

interface SidebarProps {
  activeView: SidebarView;
  onViewChange: (v: SidebarView) => void;
  threads: Thread[];
  activeThreadId?: string;
  onSelectThread: (id: string) => void;
  onNewThread: () => void;
}

const NAV_ITEMS: { id: SidebarView | string; label: string; icon: string; view?: SidebarView }[] = [
  { id: 'desktop', label: 'Desktop', icon: '🖥️', view: 'artifacts' },
  { id: 'new-thread', label: 'New Thread', icon: '✏️' },
  { id: 'threads', label: 'Previous Threads', icon: '💬', view: 'threads' },
  { id: 'memory', label: 'Memory Console', icon: '🧠', view: 'memory' },
  { id: 'settings', label: 'Settings', icon: '⚙️', view: 'settings' },
  { id: 'divider1', label: '', icon: '' },
  { id: 'search', label: 'Quick Capture', icon: '⚡' },
  { id: 'agent-search', label: 'Agent Search', icon: '🤖' },
  { id: 'divider2', label: '', icon: '' },
  { id: 'admin', label: 'Admin Dashboard', icon: '🛡️', view: 'admin' },
  { id: 'admin-docs', label: 'Admin Docs', icon: '📋' },
  { id: 'tickets', label: 'Support Tickets', icon: '🎫' },
];

interface ThreadsDrawerProps {
  threads: Thread[];
  activeThreadId?: string;
  onSelect: (id: string) => void;
  onClose: () => void;
}

function ThreadsDrawer({ threads, activeThreadId, onSelect, onClose }: ThreadsDrawerProps) {
  const [search, setSearch] = useState('');
  const filtered = threads.filter(t =>
    t.title.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="glass" style={{
      position: 'fixed',
      top: 0,
      left: 200,
      bottom: 0,
      width: 240,
      zIndex: 55,
      display: 'flex',
      flexDirection: 'column',
      borderTop: 'none',
      borderBottom: 'none',
      borderLeft: 'none',
      borderRadius: 0,
    }}>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '14px 14px 10px',
        borderBottom: '1px solid var(--caos-border)',
        flexShrink: 0,
      }}>
        <span style={{ fontSize: 12, fontWeight: 600, color: 'var(--caos-text-dim)', letterSpacing: '0.06em', textTransform: 'uppercase' }}>
          Previous Threads
        </span>
        <button onClick={onClose} style={{ color: 'var(--caos-text-muted)', fontSize: 14 }}>✕</button>
      </div>
      <div style={{ padding: '8px 10px', flexShrink: 0 }}>
        <input
          value={search}
          onChange={e => setSearch(e.target.value)}
          placeholder="Search threads..."
          style={{
            width: '100%',
            background: 'rgba(255,255,255,0.05)',
            border: '1px solid var(--caos-border)',
            borderRadius: 6,
            padding: '7px 10px',
            fontSize: 12,
            color: 'var(--caos-text)',
            outline: 'none',
          }}
        />
      </div>
      <div style={{ flex: 1, overflowY: 'auto', padding: '4px 8px 8px' }}>
        {filtered.length === 0 && (
          <div style={{ textAlign: 'center', color: 'var(--caos-text-muted)', fontSize: 12, padding: 20 }}>
            No threads yet
          </div>
        )}
        {filtered.map(t => (
          <button
            key={t.thread_id}
            onClick={() => { onSelect(t.thread_id); onClose(); }}
            style={{
              width: '100%',
              textAlign: 'left',
              padding: '9px 10px',
              marginBottom: 2,
              borderRadius: 6,
              background: activeThreadId === t.thread_id ? 'rgba(124,92,191,0.18)' : 'transparent',
              border: activeThreadId === t.thread_id ? '1px solid rgba(124,92,191,0.3)' : '1px solid transparent',
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
              {t.message_count} msg{t.message_count !== 1 ? 's' : ''}
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}

export default function Sidebar({
  activeView,
  onViewChange,
  threads,
  activeThreadId,
  onSelectThread,
  onNewThread,
}: SidebarProps) {
  const [threadsOpen, setThreadsOpen] = useState(false);

  const handleNavClick = (item: typeof NAV_ITEMS[0]) => {
    if (item.id === 'new-thread') { onNewThread(); return; }
    if (item.id === 'threads') { setThreadsOpen(s => !s); return; }
    if (item.view) { onViewChange(item.view); setThreadsOpen(false); }
  };

  return (
    <>
      <aside style={{
        position: 'fixed',
        top: 0,
        left: 0,
        bottom: 0,
        width: 200,
        zIndex: 60,
        display: 'flex',
        flexDirection: 'column',
        background: 'rgba(8, 6, 20, 0.88)',
        backdropFilter: 'blur(24px)',
        borderRight: '1px solid var(--caos-border)',
      }}>
        {/* User avatar */}
        <div style={{
          padding: '16px 14px 12px',
          borderBottom: '1px solid var(--caos-border)',
          flexShrink: 0,
          display: 'flex',
          alignItems: 'center',
          gap: 10,
        }}>
          <div style={{
            width: 32,
            height: 32,
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #7c5cbf, #a78bfa)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: 13,
            fontWeight: 700,
            color: '#fff',
            flexShrink: 0,
          }}>
            M
          </div>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--caos-text)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              Michael Chambers
            </div>
            <div style={{ fontSize: 10, color: 'var(--caos-accent-bright)' }}>Admin</div>
          </div>
        </div>

        {/* Nav */}
        <nav style={{ flex: 1, overflowY: 'auto', padding: '6px 0' }}>
          {NAV_ITEMS.map((item, i) => {
            if (item.id.startsWith('divider')) {
              return <div key={i} style={{ height: 1, background: 'var(--caos-border)', margin: '6px 14px' }} />;
            }
            const isActive = item.view && activeView === item.view && item.id !== 'threads';
            const isThreadsOpen = item.id === 'threads' && threadsOpen;
            return (
              <button
                key={item.id}
                onClick={() => handleNavClick(item)}
                style={{
                  width: '100%',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 9,
                  padding: '8px 14px',
                  fontSize: 12,
                  fontWeight: (isActive || isThreadsOpen) ? 600 : 400,
                  color: (isActive || isThreadsOpen) ? 'var(--caos-accent-bright)' : 'var(--caos-text-dim)',
                  background: (isActive || isThreadsOpen) ? 'rgba(124,92,191,0.12)' : 'transparent',
                  textAlign: 'left',
                  transition: 'all var(--caos-transition)',
                  borderLeft: (isActive || isThreadsOpen) ? '2px solid var(--caos-accent)' : '2px solid transparent',
                }}
              >
                <span style={{ fontSize: 14, flexShrink: 0 }}>{item.icon}</span>
                <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{item.label}</span>
              </button>
            );
          })}
        </nav>

        {/* Log out */}
        <div style={{ borderTop: '1px solid var(--caos-border)', flexShrink: 0 }}>
          <button style={{
            width: '100%',
            display: 'flex',
            alignItems: 'center',
            gap: 9,
            padding: '11px 14px',
            fontSize: 12,
            color: 'var(--caos-text-muted)',
            textAlign: 'left',
          }}>
            <span style={{ fontSize: 14 }}>↩️</span>
            Log Out
          </button>
        </div>
      </aside>

      {/* Threads drawer */}
      {threadsOpen && (
        <ThreadsDrawer
          threads={threads}
          activeThreadId={activeThreadId}
          onSelect={onSelectThread}
          onClose={() => setThreadsOpen(false)}
        />
      )}

      {/* Overlay to close threads drawer */}
      {threadsOpen && (
        <div
          onClick={() => setThreadsOpen(false)}
          style={{ position: 'fixed', inset: 0, zIndex: 54 }}
        />
      )}
    </>
  );
}
