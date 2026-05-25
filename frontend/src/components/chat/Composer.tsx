import React, { useState, useRef, useCallback } from 'react';
import { ModelContextSpec } from '../../types';

interface ComposerProps {
  onSend: (message: string) => void;
  disabled?: boolean;
  activeModel?: ModelContextSpec;
  availableModels?: ModelContextSpec[];
  onSelectModel?: (provider: string, model: string) => void;
  tokensUsed?: number;
}

export default function Composer({
  onSend,
  disabled,
  activeModel,
  availableModels = [],
  onSelectModel,
  tokensUsed = 0,
}: ComposerProps) {
  const [text, setText] = useState('');
  const [showModels, setShowModels] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const submit = useCallback(() => {
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText('');
    if (textareaRef.current) textareaRef.current.style.height = 'auto';
  }, [text, disabled, onSend]);

  const onKey = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); submit(); }
  };

  const onInput = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(e.target.value);
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 140) + 'px';
  };

  const usable = activeModel?.usable_context_tokens ?? 180000;
  const tokenDisplay = `${(tokensUsed / 1000).toFixed(1)}K / ${(usable / 1000).toFixed(0)}K`;

  return (
    <div style={{
      position: 'fixed',
      bottom: 0,
      left: 200,
      right: 0,
      zIndex: 40,
      background: 'rgba(6,6,15,0.85)',
      backdropFilter: 'blur(20px)',
      borderTop: '1px solid var(--caos-border)',
      padding: '10px 20px 14px',
    }}>
      {/* Model dropdown */}
      {showModels && (
        <div className="glass" style={{
          position: 'absolute',
          bottom: '100%',
          left: 20,
          marginBottom: 8,
          borderRadius: 'var(--caos-radius)',
          overflow: 'hidden',
          minWidth: 240,
        }}>
          {availableModels.map((m) => (
            <button
              key={`${m.provider}/${m.model}`}
              onClick={() => { onSelectModel?.(m.provider, m.model); setShowModels(false); }}
              style={{
                width: '100%',
                padding: '10px 14px',
                textAlign: 'left',
                fontSize: 12,
                color: 'var(--caos-text)',
                background: activeModel?.model === m.model ? 'rgba(124,92,191,0.2)' : 'transparent',
                borderBottom: '1px solid var(--caos-border)',
                display: 'flex',
                flexDirection: 'column',
                gap: 2,
              }}
            >
              <span style={{ fontWeight: 500 }}>{m.display_name}</span>
              <span style={{ fontSize: 10, color: 'var(--caos-text-muted)' }}>
                {(m.usable_context_tokens / 1000).toFixed(0)}K ctx · {m.provider}
              </span>
            </button>
          ))}
        </div>
      )}

      {/* Input row */}
      <div style={{ display: 'flex', alignItems: 'flex-end', gap: 8 }}>
        <button title="Attach" style={{ fontSize: 18, color: 'var(--caos-text-muted)', flexShrink: 0, padding: '6px 4px', opacity: 0.7 }}>
          📎
        </button>

        <textarea
          ref={textareaRef}
          value={text}
          onChange={onInput}
          onKeyDown={onKey}
          placeholder="Ask anything... add and select models and chat with our foundation"
          rows={1}
          disabled={disabled}
          style={{
            flex: 1,
            background: 'rgba(255,255,255,0.04)',
            border: '1px solid var(--caos-border)',
            borderRadius: 'var(--caos-radius)',
            padding: '10px 14px',
            fontSize: 14,
            lineHeight: 1.5,
            resize: 'none',
            outline: 'none',
            color: 'var(--caos-text)',
            maxHeight: 140,
            overflowY: 'auto',
          }}
        />

        <button title="Voice" style={{ fontSize: 18, color: 'var(--caos-text-muted)', flexShrink: 0, padding: '6px 4px', opacity: 0.7 }}>
          🎙️
        </button>

        <button
          onClick={submit}
          disabled={!text.trim() || disabled}
          style={{
            width: 36,
            height: 36,
            borderRadius: '50%',
            background: text.trim() && !disabled ? 'var(--caos-accent)' : 'rgba(124,92,191,0.15)',
            border: '1px solid var(--caos-border)',
            fontSize: 15,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            flexShrink: 0,
            transition: 'all var(--caos-transition)',
            opacity: text.trim() && !disabled ? 1 : 0.45,
            color: '#fff',
          }}
        >
          ↑
        </button>
      </div>

      {/* Bottom bar — model selector + token count + Full Aria */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 10,
        marginTop: 8,
        paddingLeft: 4,
      }}>
        <button
          onClick={() => setShowModels(s => !s)}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            padding: '3px 10px',
            background: showModels ? 'rgba(124,92,191,0.2)' : 'rgba(124,92,191,0.08)',
            border: '1px solid rgba(124,92,191,0.25)',
            borderRadius: 20,
            fontSize: 11,
            color: 'var(--caos-accent-bright)',
            fontWeight: 500,
          }}
        >
          <span style={{ fontSize: 10 }}>◆</span>
          {activeModel?.display_name ?? 'Select model'}
          <span style={{ color: 'var(--caos-text-muted)', fontWeight: 400 }}>·</span>
          <span style={{ color: 'var(--caos-text-muted)', fontWeight: 400 }}>{tokenDisplay}</span>
        </button>

        <button style={{
          padding: '3px 12px',
          background: 'rgba(124,92,191,0.15)',
          border: '1px solid rgba(124,92,191,0.3)',
          borderRadius: 20,
          fontSize: 11,
          color: 'var(--caos-text-dim)',
          fontWeight: 500,
        }}>
          Full Aria
        </button>
      </div>
    </div>
  );
}
