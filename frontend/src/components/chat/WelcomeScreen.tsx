import React, { useState } from 'react';

const CARDS = [
  { icon: '🔍', title: 'Search Anything', desc: 'Find answers with context-aware search' },
  { icon: '📊', title: 'Analyze Data', desc: 'Pull insights from files and receipts' },
  { icon: '✍️', title: 'Generate Content', desc: 'Draft fast with memory-aware prompting' },
  { icon: '🎨', title: 'Create & Design', desc: 'Work across media without leaving CAOS' },
  { icon: '🧠', title: 'Persistent Memory', desc: 'Remembers what matters, forgets what doesn\'t' },
  { icon: '⚡', title: 'Multi-Model Routing', desc: 'Right model for every job, automatically' },
];

const VISIBLE = 4;

interface WelcomeScreenProps {
  onPrompt: (text: string) => void;
}

export default function WelcomeScreen({ onPrompt }: WelcomeScreenProps) {
  const [offset, setOffset] = useState(0);
  const maxOffset = CARDS.length - VISIBLE;

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100%',
      padding: '0 40px',
      gap: 36,
      userSelect: 'none',
    }}>
      {/* Hero text */}
      <div style={{ textAlign: 'center' }}>
        <h1 style={{
          fontSize: 48,
          fontWeight: 700,
          color: 'var(--caos-text)',
          margin: '0 0 12px',
          letterSpacing: '-0.01em',
        }}>
          Welcome to CAOS
        </h1>
        <p style={{
          fontSize: 15,
          color: 'var(--caos-text-dim)',
          margin: '0 0 6px',
          fontWeight: 300,
        }}>
          Search the web, analyze data, generate content, and get instant answers.
        </p>
        <p style={{ fontSize: 13, color: 'var(--caos-text-muted)' }}>
          Try these to see what's possible
        </p>
      </div>

      {/* Card carousel */}
      <div style={{ width: '100%', maxWidth: 860, position: 'relative' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <button
            onClick={() => setOffset(o => Math.max(0, o - 1))}
            disabled={offset === 0}
            style={{
              width: 28,
              height: 28,
              borderRadius: '50%',
              background: offset === 0 ? 'rgba(255,255,255,0.04)' : 'rgba(124,92,191,0.2)',
              border: '1px solid var(--caos-border)',
              color: offset === 0 ? 'var(--caos-text-muted)' : 'var(--caos-accent-bright)',
              fontSize: 14,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
              cursor: offset === 0 ? 'default' : 'pointer',
            }}
          >
            ‹
          </button>

          <div style={{
            flex: 1,
            display: 'grid',
            gridTemplateColumns: `repeat(${VISIBLE}, 1fr)`,
            gap: 12,
            overflow: 'hidden',
          }}>
            {CARDS.slice(offset, offset + VISIBLE).map((card) => (
              <div
                key={card.title}
                className="glass-2"
                style={{
                  padding: '20px 16px',
                  borderRadius: 'var(--caos-radius)',
                  cursor: 'pointer',
                  transition: 'border-color var(--caos-transition), background var(--caos-transition)',
                }}
                onMouseEnter={e => {
                  e.currentTarget.style.borderColor = 'rgba(124,92,191,0.45)';
                  e.currentTarget.style.background = 'rgba(20,16,42,0.8)';
                }}
                onMouseLeave={e => {
                  e.currentTarget.style.borderColor = '';
                  e.currentTarget.style.background = '';
                }}
                onClick={() => onPrompt(card.title)}
              >
                <div style={{ fontSize: 24, marginBottom: 10 }}>{card.icon}</div>
                <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--caos-text)', marginBottom: 6 }}>
                  {card.title}
                </div>
                <div style={{ fontSize: 12, color: 'var(--caos-text-dim)', lineHeight: 1.5 }}>
                  {card.desc}
                </div>
              </div>
            ))}
          </div>

          <button
            onClick={() => setOffset(o => Math.min(maxOffset, o + 1))}
            disabled={offset >= maxOffset}
            style={{
              width: 28,
              height: 28,
              borderRadius: '50%',
              background: offset >= maxOffset ? 'rgba(255,255,255,0.04)' : 'rgba(124,92,191,0.2)',
              border: '1px solid var(--caos-border)',
              color: offset >= maxOffset ? 'var(--caos-text-muted)' : 'var(--caos-accent-bright)',
              fontSize: 14,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
              cursor: offset >= maxOffset ? 'default' : 'pointer',
            }}
          >
            ›
          </button>
        </div>

        {/* Dots */}
        <div style={{ display: 'flex', justifyContent: 'center', gap: 5, marginTop: 14 }}>
          {Array.from({ length: maxOffset + 1 }).map((_, i) => (
            <div
              key={i}
              onClick={() => setOffset(i)}
              style={{
                width: i === offset ? 16 : 5,
                height: 5,
                borderRadius: 3,
                background: i === offset ? 'var(--caos-accent)' : 'rgba(124,92,191,0.25)',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
              }}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
