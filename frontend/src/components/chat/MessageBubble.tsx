import React from 'react';
import { ChatMessage } from '../../types';
import MarkdownRenderer from './MarkdownRenderer';

interface MessageBubbleProps {
  message: ChatMessage;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === 'user';

  const bubbleContent = isUser ? (
    <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
      {message.content}
    </span>
  ) : (
    <MarkdownRenderer content={message.content} />
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
            marginTop: 4,
            paddingLeft: 2,
            minHeight: 0,
          }}
        >
          {/* M2 latency chip + M3 action buttons will populate here */}
        </div>
      )}
    </div>
  );
}
