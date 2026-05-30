import React from 'react';

interface MarkdownRendererProps {
  content: string;
}

type Block =
  | { kind: 'paragraph'; lines: string[] }
  | { kind: 'heading'; level: 1 | 2 | 3; text: string }
  | { kind: 'code'; lang: string | null; lines: string[] }
  | { kind: 'list'; ordered: boolean; items: string[] }
  | { kind: 'hr' };

function parseBlocks(src: string): Block[] {
  const lines = src.replace(/\r\n/g, '\n').split('\n');
  const blocks: Block[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block
    const fence = line.match(/^```\s*([\w+.-]*)\s*$/);
    if (fence) {
      const lang = fence[1] || null;
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !/^```\s*$/.test(lines[i])) {
        codeLines.push(lines[i]);
        i++;
      }
      // Skip closing fence if present
      if (i < lines.length) i++;
      blocks.push({ kind: 'code', lang, lines: codeLines });
      continue;
    }

    // Horizontal rule
    if (/^\s*---\s*$/.test(line)) {
      blocks.push({ kind: 'hr' });
      i++;
      continue;
    }

    // Heading
    const heading = line.match(/^(#{1,3})\s+(.*)$/);
    if (heading) {
      const level = heading[1].length as 1 | 2 | 3;
      blocks.push({ kind: 'heading', level, text: heading[2] });
      i++;
      continue;
    }

    // Blank line — paragraph break
    if (/^\s*$/.test(line)) {
      i++;
      continue;
    }

    // Ordered list group
    if (/^\s*\d+\.\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*\d+\.\s+/, ''));
        i++;
      }
      blocks.push({ kind: 'list', ordered: true, items });
      continue;
    }

    // Unordered list group
    if (/^\s*[-*]\s+/.test(line)) {
      const items: string[] = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*]\s+/, ''));
        i++;
      }
      blocks.push({ kind: 'list', ordered: false, items });
      continue;
    }

    // Paragraph (collect consecutive non-blank, non-special lines)
    const paraLines: string[] = [];
    while (
      i < lines.length &&
      !/^\s*$/.test(lines[i]) &&
      !/^```/.test(lines[i]) &&
      !/^\s*---\s*$/.test(lines[i]) &&
      !/^#{1,3}\s+/.test(lines[i]) &&
      !/^\s*\d+\.\s+/.test(lines[i]) &&
      !/^\s*[-*]\s+/.test(lines[i])
    ) {
      paraLines.push(lines[i]);
      i++;
    }
    if (paraLines.length) {
      blocks.push({ kind: 'paragraph', lines: paraLines });
    }
  }

  return blocks;
}

// Inline parser: handles `code`, **bold**, *italic*, _italic_
function renderInline(text: string, keyPrefix: string): React.ReactNode[] {
  const out: React.ReactNode[] = [];
  let i = 0;
  let buf = '';
  let key = 0;

  const flush = () => {
    if (buf) {
      out.push(<React.Fragment key={`${keyPrefix}-t-${key++}`}>{buf}</React.Fragment>);
      buf = '';
    }
  };

  while (i < text.length) {
    const ch = text[i];

    // Inline code: `...`
    if (ch === '`') {
      const end = text.indexOf('`', i + 1);
      if (end !== -1) {
        flush();
        out.push(
          <code
            key={`${keyPrefix}-c-${key++}`}
            style={{
              fontFamily: 'ui-monospace, SFMono-Regular, Menlo, monospace',
              fontSize: '0.92em',
              padding: '1px 5px',
              borderRadius: 4,
              background: 'rgba(255, 255, 255, 0.06)',
              color: 'var(--caos-accent-bright, #b8a4ff)',
            }}
          >
            {text.slice(i + 1, end)}
          </code>
        );
        i = end + 1;
        continue;
      }
    }

    // Bold: **...**
    if (ch === '*' && text[i + 1] === '*') {
      const end = text.indexOf('**', i + 2);
      if (end !== -1) {
        flush();
        out.push(
          <strong key={`${keyPrefix}-b-${key++}`} style={{ fontWeight: 600 }}>
            {renderInline(text.slice(i + 2, end), `${keyPrefix}-b${key}`)}
          </strong>
        );
        i = end + 2;
        continue;
      }
    }

    // Italic: *...* (single)
    if (ch === '*' && text[i + 1] !== '*' && text[i - 1] !== '*') {
      const end = text.indexOf('*', i + 1);
      if (end !== -1 && text[end + 1] !== '*') {
        flush();
        out.push(
          <em key={`${keyPrefix}-i-${key++}`}>
            {renderInline(text.slice(i + 1, end), `${keyPrefix}-i${key}`)}
          </em>
        );
        i = end + 1;
        continue;
      }
    }

    // Italic: _..._
    if (ch === '_' && text[i + 1] !== '_') {
      const end = text.indexOf('_', i + 1);
      if (end !== -1) {
        flush();
        out.push(
          <em key={`${keyPrefix}-u-${key++}`}>
            {renderInline(text.slice(i + 1, end), `${keyPrefix}-u${key}`)}
          </em>
        );
        i = end + 1;
        continue;
      }
    }

    buf += ch;
    i++;
  }

  flush();
  return out;
}

function renderBlock(block: Block, idx: number): React.ReactNode {
  const k = `b-${idx}`;
  switch (block.kind) {
    case 'heading': {
      const sizes: Record<1 | 2 | 3, number> = { 1: 20, 2: 17, 3: 15 };
      const headingStyle: React.CSSProperties = {
        fontSize: sizes[block.level],
        fontWeight: 600,
        margin: '14px 0 6px',
        color: 'var(--caos-text)',
        lineHeight: 1.3,
      };
      const inner = renderInline(block.text, k);
      if (block.level === 1) return <h1 key={k} style={headingStyle}>{inner}</h1>;
      if (block.level === 2) return <h2 key={k} style={headingStyle}>{inner}</h2>;
      return <h3 key={k} style={headingStyle}>{inner}</h3>;
    }
    case 'hr':
      return (
        <hr
          key={k}
          style={{
            border: 'none',
            borderTop: '1px solid rgba(255, 255, 255, 0.08)',
            margin: '12px 0',
          }}
        />
      );
    case 'code':
      return (
        <pre
          key={k}
          style={{
            background: 'rgba(0, 0, 0, 0.25)',
            border: '1px solid rgba(255, 255, 255, 0.06)',
            borderRadius: 8,
            padding: '10px 12px',
            margin: '8px 0',
            overflowX: 'auto',
            fontFamily: 'ui-monospace, SFMono-Regular, Menlo, monospace',
            fontSize: 12.5,
            lineHeight: 1.5,
            color: 'var(--caos-text)',
          }}
        >
          {block.lang && (
            <div
              style={{
                fontSize: 10,
                letterSpacing: '0.06em',
                textTransform: 'uppercase',
                color: 'var(--caos-text-muted)',
                marginBottom: 6,
              }}
            >
              {block.lang}
            </div>
          )}
          <code>{block.lines.join('\n')}</code>
        </pre>
      );
    case 'list': {
      const listStyle: React.CSSProperties = { margin: '6px 0', paddingLeft: 22 };
      const items = block.items.map((item, j) => (
        <li key={`${k}-${j}`} style={{ margin: '2px 0' }}>
          {renderInline(item, `${k}-${j}`)}
        </li>
      ));
      return block.ordered ? (
        <ol key={k} style={listStyle}>{items}</ol>
      ) : (
        <ul key={k} style={listStyle}>{items}</ul>
      );
    }
    case 'paragraph': {
      const parts: React.ReactNode[] = [];
      block.lines.forEach((line, j) => {
        if (j > 0) parts.push(<br key={`${k}-br-${j}`} />);
        parts.push(
          <React.Fragment key={`${k}-l-${j}`}>
            {renderInline(line, `${k}-l${j}`)}
          </React.Fragment>
        );
      });
      return (
        <p key={k} style={{ margin: '6px 0' }}>
          {parts}
        </p>
      );
    }
  }
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
  const blocks = parseBlocks(content);
  return <>{blocks.map(renderBlock)}</>;
}
