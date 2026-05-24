import React from 'react';

const CAPABILITIES = [
  {
    icon: '🧠',
    title: 'Persistent Memory',
    desc: 'Remembers what you tell it. Categorized, governed, yours.',
  },
  {
    icon: '⚡',
    title: 'Multi-Model Routing',
    desc: 'Right model for the job — GPT, Claude, Gemini, more.',
  },
  {
    icon: '📁',
    title: 'Desktop & Files',
    desc: 'Upload files, save links, access them across sessions.',
  },
  {
    icon: '🔍',
    title: 'Context Hygiene',
    desc: 'Hydrates relevant context. Sanitizes what\'s not needed.',
  },
  {
    icon: '🛡️',
    title: 'Governed Actions',
    desc: 'Every action receipted. Nothing hidden. You approve.',
  },
  {
    icon: '🔧',
    title: 'Tool Orchestration',
    desc: 'GitHub, email, calendar, web — connected and controllable.',
  },
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
      padding: '40px 24px',
      gap: 32,
    }}>
      <div style={{ textAlign: 'center' }}>
        <div style={{
          fontSize: 38,
          fontWeight: 800,
          letterSpacing: '0.12em',
          background: 'linear-gradient(135deg, #a78bfa 0%, #7c5cbf 50%, #c4b5fd 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          backgroundClip: 'text',
          marginBottom: 8,
        }}>
          CAOS
        </div>
        <div style={{
          fontSize: 14,
          color: 'var(--caos-text-dim)',
          letterSpacing: '0.04em',
        }}>
          Your memory. Your models. Your rules.
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
        gap: 12,
        width: '100%',
        maxWidth: 680,
      }}>
        {CAPABILITIES.map((cap) => (
          <div
            key={cap.title}
            className="glass-2"
            style={{
              padding: '16px',
              borderRadius: 'var(--caos-radius)',
              cursor: 'default',
            }}
          >
            <div style={{ fontSize: 22, marginBottom: 8 }}>{cap.icon}</div>
            <div style={{ fontSize: 13, fontWeight: 600, marginBottom: 4, color: 'var(--caos-text)' }}>
              {cap.title}
            </div>
            <div style={{ fontSize: 12, color: 'var(--caos-text-dim)', lineHeight: 1.5 }}>
              {cap.desc}
            </div>
          </div>
        ))}
      </div>

      <div style={{
        fontSize: 12,
        color: 'var(--caos-text-muted)',
        textAlign: 'center',
      }}>
        Start typing below to begin a conversation with Aria.
      </div>
    </div>
  );
}
