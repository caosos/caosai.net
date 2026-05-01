#!/usr/bin/env bash
set -e

echo "== missing auth (expect 401) =="
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST http://127.0.0.1:8000/recall \
  -H "Content-Type: application/json" \
  -d '{ "policy": "allow", "anchors": ["session:demo-session"] }'

echo "== missing policy (expect 403) =="
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST http://127.0.0.1:8000/recall \
  -H "Content-Type: application/json" \
  -d '{ "auth": { "mode": "dev" }, "anchors": ["session:demo-session"] }'

echo "== malformed anchors (expect 400) =="
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST http://127.0.0.1:8000/recall \
  -H "Content-Type: application/json" \
  -d '{ "auth": { "mode": "dev" }, "policy": "allow", "anchors": "bad" }'
