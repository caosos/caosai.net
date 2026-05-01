import re

HEADER_PATTERNS = [
    r'^\s*🕒.*?$',
    r'^\s*Server ARIA:\s*$',
]

def sanitize_assistant_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    lines = text.splitlines()
    cleaned = []

    for line in lines:
        if any(re.match(p, line) for p in HEADER_PATTERNS):
            continue
        cleaned.append(line)

    return "\n".join(cleaned).lstrip()
