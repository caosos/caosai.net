# Local Smoke Test

## Purpose

Validate the portable backend foundation from a real checkout before starting the chat spine.

## Setup

From a clean checkout of `caosos/linode-repo` on branch `aria-emergent-clean-rebuild`:

```bash
cd backend || exit 1
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
cd backend || exit 1
source .venv/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Verify routes

In a second terminal:

```bash
curl -s http://127.0.0.1:8000/api/health | python3 -m json.tool
curl -s http://127.0.0.1:8000/api/runtime | python3 -m json.tool
curl -s -X POST http://127.0.0.1:8000/api/auth/dev-login \
  -H 'Content-Type: application/json' \
  -d '{"requested_name":"Michael"}' | python3 -m json.tool
```

## Expected behavior

- `/api/health` returns `ok: true`.
- `/api/runtime` returns runtime and database state without secret values.
- `/api/auth/dev-login` returns a development admin user when `CAOS_DEV_AUTH_ENABLED=true`.
- No real secret values are returned.
- App starts without Emergent OAuth.
- App starts without Base44 SDK/runtime.
- App can start without a Mongo URI during foundation phase.

## Failure handling

Record failures in `docs/BUILD_DECISIONS_AND_INCIDENTS.md` before retrying if the issue affects architecture, dependency choices, environment setup, or migration assumptions.
