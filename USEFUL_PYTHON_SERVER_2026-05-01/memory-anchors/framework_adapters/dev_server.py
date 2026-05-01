"""
CAOS-A1 — Explicit Dev Server (Message + Recall)

ROLE
----
Minimal, explicit server runner for development only.
Two POST routes. No magic. No inference.
"""

from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time

from caos_api.server_entrypoint import (
    handle_post_message,
    handle_post_recall,
)
from caos_api.auth_envelope import AuthEnvelopeError
from caos_api.autopolicy_gate import PolicyDeniedError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

def _guard(fn, request_json):
    try:
        return fn(request_json=request_json)
    except AuthEnvelopeError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except PolicyDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "memory-anchors",
        "capabilities": ["message", "recall", "anchors"],
        "version": "A1",
        "ts": int(time.time() * 1000),
    }

@app.post("/message")
def post_message(request_json: Dict[str, Any]):
    return _guard(handle_post_message, request_json)

@app.post("/recall")
def post_recall(request_json: Dict[str, Any]):
    return _guard(handle_post_recall, request_json)

def run():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    run()
