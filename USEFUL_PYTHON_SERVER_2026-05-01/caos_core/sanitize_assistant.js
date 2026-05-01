"use strict";

/**
 * CAOS-A1 — Header Sanitizer (Deterministic)
 *
 * PURPOSE:
 * - Remove render-time headers from assistant text before storage/recall
 * - Prevent header duplication across recall + UI render layers
 *
 * RULES:
 * - Deterministic
 * - Fail-closed (non-string -> "")
 * - No inference
 */

const HEADER_PATTERNS = [
  // Timestamp header line (standard marker is 🕒, but also strip legacy ⏰)
  /^\s*[🕒⏰].*$/,

  // Optional label header (legacy compatibility)
  /^\s*Server\s+ARIA:\s*$/i
];

function sanitize_assistant_text(text) {
  if (typeof text !== "string") return "";

  const lines = text.split(/\r?\n/);
  const cleaned = [];

  for (const line of lines) {
    let isHeader = false;
    for (const rx of HEADER_PATTERNS) {
      if (rx.test(line)) { isHeader = true; break; }
    }
    if (isHeader) continue;
    cleaned.push(line);
  }

  // left-trim only (preserve internal newlines)
  return cleaned.join("\n").replace(/^\s+/, "");
}

module.exports = { sanitize_assistant_text };
