#!/usr/bin/env bash
curl -s -X POST http://127.0.0.1:8000/recall \
  -H "Content-Type: application/json" \
  -d '{
    "auth": { "mode": "dev" },
    "policy": "allow",
    "anchors": ["session:demo-session"]
  }' | jq .
