"""
CAOS-A1 — Public Knowledge Bin (Derived, Non-Authoritative)

- Non-personal, public-source facts only
- TTL-governed
- Content-hash keyed
- Disposable; rebuildable
- NO authority over user truth
"""

import time
import hashlib
from typing import Dict, Any

DEFAULT_TTL_SEC = 60 * 60 * 24 * 7  # 7 days

_store: Dict[str, Dict[str, Any]] = {}

def _hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def put(content: str, source: str, ttl_sec: int = DEFAULT_TTL_SEC) -> str:
    key = _hash(content + source)
    _store[key] = {
        "content": content,
        "source": source,
        "expires_at": time.time() + ttl_sec,
        "created_at": time.time(),
    }
    return key

def get(key: str):
    rec = _store.get(key)
    if not rec:
        return None
    if time.time() > rec["expires_at"]:
        _store.pop(key, None)
        return None
    return rec

def sweep():
    now = time.time()
    expired = [k for k, v in _store.items() if now > v["expires_at"]]
    for k in expired:
        _store.pop(k, None)
    return len(expired)
