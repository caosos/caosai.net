import React, { useState, useRef, useCallback } from 'react';
import { ModelContextSpec } from '../../types';

interface ComposerProps {
  onSend: (message: string) => void;
  disabled?: boolean;
  activeModel?: ModelContextSpec;
  availableModels?: ModelContextSpec[];
  onSelectModel?: (provider: string, model: string) => void;
}

export default function Composer({
  onSend,
  disabled,
  activeModel,
  availableModels = [],
  onSelectModel,
}: ComposerProps) {
  const [text, setText] = useState('');
  const [showModels, setShowModels] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const submit = useCallback(() => {
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText('');
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  }, [text, disabled, onSend]);

  const onKey = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  };

  const onInput = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(e.target.value);
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 160) + 'px';
  };

  return (
    <div
      className="glass"
      style={{
        position: 'fixed',
        bottom: 0,
        left: 'var(--caos-sidebar-open, 0px)',
        right: 0,
        padding: '12px 16px',
        borderTop: '1px solid var(--caos-border)',
        borderLeft: 'none',
        borderRight: 'none',
        borderBottom: 'none',
        borderRadius: 0,
        zIndex: 40,
        display: 'flex',
        flexDirection: 'column',
        gap: 10,
      }}
    >
      {/* Model selector dropdown */}
      {showModels && (
        <div
          className="glass"
          style={{
            position: 'absolute',
            bottom: '100%',
            left: 16,
            marginBottom: 8,
            borderRadius: 'var(--caos-radius)',
            overflow: 'hidden',
            minWidth: 220,
          }}
        >
          {availableModels.map((m) => (
            <button
              key={`${m.provider}/${m.model}`}
              onClick={() => {
                onSelectModel?.(m.provider, m.model);
                setShowModels(false);
              }}
              style={{
                width: '100%',
                padding: '10px 14px',
                textAlign: 'left',
                fontSize: 12,
                color: m.enabled ? 'var(--caos-text)' : 'var(--caos-text-muted)',
                background:
                  activeModel?.model === m.model
                    ? 'rgba(124,92,191,0.2)'
                    : 'transparent',
                borderBottom: '1px solid var(--caos-border)',
                display: 'flex',
                flexDirection: 'column',
                gap: 2,
              }}
            >
              <span style={{ fontWeight: 500 }}>{m.display_name}</span>
              <span style={{ fontSize: 10, color: 'var(--caos-text-muted)' }}>
                {(m.usable_context_tokens / 1000).toFixed(0)}K ctx · {m.provider}
                {!m.enabled && ' · key needed'}
              </span>
            </button>
          ))}
        </div>
      )}

      <div style={{ display: 'flex', alignItems: 'flex-end', gap: 10 }}>
        {/* Attachment */}
        <button
          title="Attach file"
          style={{
            fontSize: 18,
            padding: '6px',
            color: 'var(--caos-text-muted)',
            flexShrink: 0,
            opacity: 0.7,
          }}
        >
          📎
        </button>

        {/* Text input */}
        <textarea
          ref={textareaRef}
          value={text}
          onChange={onInput}
          onKeyDown={onKey}
          placeholder="Message Aria…"
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
            maxHeight: 160,
            overflowY: 'auto',
          }}
        />

        {/* Model selector button */}
        <button
          onClick={() => setShowModels((s) => !s)}
          title="Select model"
          style={{
            fontSize: 11,
            color: showModels ? 'var(--caos-accent-bright)' : 'var(--caos-text-muted)',
            padding: '6px 8px',
            background: showModels ? 'rgba(124,92,191,0.15)' : 'transparent',
            border: '1px solid var(--caos-border)',
            borderRadius: 'var(--caos-radius-sm)',
            flexShrink: 0,
            maxWidth: 100,
            overflow: 'hidden',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
          }}
        >
          {activeModel?.display_name ?? 'Model'}
        </button>

        {/* Voice toggle */}
        <button
          title="Voice input"
          style={{
            fontSize: 18,
            padding: '6px',
            color: 'var(--caos-text-muted)',
            flexShrink: 0,
            opacity: 0.7,
          }}
        >
          🎙️
        </button>

        {/* Send */}
        <button
          onClick={submit}
          disabled={!text.trim() || disabled}
          style={{
            width: 38,
            height: 38,
            borderRadius: '50%',
            background: text.trim() && !disabled
              ? 'var(--caos-accent)'
              : 'rgba(124,92,191,0.15)',
            border: '1px solid var(--caos-border)',
            fontSize: 16,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            flexShrink: 0,
            transition: 'all var(--caos-transition)',
            opacity: text.trim() && !disabled ? 1 : 0.5,
          }}
        >
          ↑
        </button>
      </div>

      <div style={{
        fontSize: 10,
        color: 'var(--caos-text-muted)',
        textAlign: 'center',
        letterSpacing: '0.04em',
      }}>
        Shift+Enter for new line · Enter to send · API keys needed for live responses
      </div>
    </div>
  );
}
