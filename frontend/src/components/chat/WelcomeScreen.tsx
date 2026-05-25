import React from 'react';

const CAPABILITIES = [
  { icon: '🧠', title: 'Persistent Memory', desc: 'Remembers what you tell it. Categorized, governed, yours to control.' },
  { icon: '⚡', title: 'Multi-Model Routing', desc: 'Right model for the job — GPT, Claude, Gemini, Grok, and more.' },
  { icon: '📁', title: 'Desktop & Files', desc: 'Upload files, save links, access them across every session.' },
  { icon: '🔍', title: 'Context Hygiene', desc: 'Pulls in what matters. Removes what doesn\'t. Zero wasted tokens.' },
  { icon: '🛡️', title: 'Governed Actions', desc: 'Every action receipted. Nothing hidden. You approve what matters.' },
  { icon: '🔧', title: 'Tool Orchestration', desc: 'GitHub, email, calendar, web — connected and under your control.' },
];

interface WelcomeScreenProps {
  onPrompt: (text: string) => void;
}

export default function WelcomeScreen({ onPrompt }: WelcomeScreenProps) {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100%',
      padding: '48px 32px 32px',
      gap: 40,
      overflowY: 'auto',
    }}>
      {/* Hero */}
      <div style={{ textAlign: 'center', maxWidth: 560 }}>
        <div style={{
          fontSize: 52,
          fontWeight: 900,
          letterSpacing: '0.14em',
          background: 'linear-gradient(135deg, #c4b5fd 0%, #a78bfa 40%, #7c5cbf 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          backgroundClip: 'text',
          marginBottom: 16,
          lineHeight: 1,
        }}>
          CAOS
        </div>
        <div style={{
          fontSize: 18,
          color: 'var(--caos-text-dim)',
          letterSpacing: '0.03em',
          marginBottom: 8,
          fontWeight: 300,
        }}>
          Cognitive Adaptive Operating System
        </div>
        <div style={{
          fontSize: 13,
          color: 'var(--caos-text-muted)',
          letterSpacing: '0.06em',
        }}>
          Your memory. Your models. Your rules.
        </div>
      </div>

      {/* Capability cards */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
        gap: 16,
        width: '100%',
        maxWidth: 760,
      }}>
        {CAPABILITIES.map((cap) => (
          <div
            key={cap.title}
            className="glass-2"
            style={{
              padding: '20px 18px',
              borderRadius: 'var(--caos-radius)',
              cursor: 'default',
              transition: 'border-color var(--caos-transition)',
            }}
            onMouseEnter={e => (e.currentTarget.style.borderColor = 'rgba(124,92,191,0.4)')}
            onMouseLeave={e => (e.currentTarget.style.borderColor = '')}
          >
            <div style={{ fontSize: 26, marginBottom: 10 }}>{cap.icon}</div>
            <div style={{
              fontSize: 14,
              fontWeight: 600,
              marginBottom: 6,
              color: 'var(--caos-text)',
              letterSpacing: '0.02em',
            }}>
              {cap.title}
            </div>
            <div style={{
              fontSize: 12,
              color: 'var(--caos-text-dim)',
              lineHeight: 1.6,
            }}>
              {cap.desc}
            </div>
          </div>
        ))}
      </div>

      <div style={{
        fontSize: 12,
        color: 'var(--caos-text-muted)',
        textAlign: 'center',
        letterSpacing: '0.04em',
      }}>
        Start typing below to begin a conversation with Aria
      </div>
    </div>
  );
}
