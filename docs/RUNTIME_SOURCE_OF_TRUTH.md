# CAOS Runtime Source of Truth

This document is the authoritative map of where CAOS code lives, where it runs, and how changes travel from development to production. Every future agent working on CAOS must read this before touching the deploy chain.

---

## Source Repository (Development)

| Property | Value |
|---|---|
| **Local path** | `/home/michael-chambers/caosai.net/` |
| **GitHub remote** | `https://github.com/caosos/caosai.net` |
| **Active branch** | `aria-emergent-clean-rebuild` (renamed `CLUADE-CODE-CLEAN-BUILD` on GitHub) |
| **Role** | Primary development source. All code changes happen here. |

This is the repo you are reading right now. All backend Python edits, frontend changes, and documentation updates happen in this repo and must be committed here first.

---

## Runtime Repository (Backend Process Host)

| Property | Value |
|---|---|
| **Local path** | `/home/michael-chambers/linode-repo/` |
| **GitHub remote** | `https://github.com/caosos/linode-repo` |
| **Role** | Runtime host only. Holds `.venv` and `.env`. Never edit directly. |

The `caos-backend` systemd service runs from this path. It has its own virtualenv and `.env` file that are **not tracked in git and must not be overwritten by rsync**.

> **Rule:** Never develop in `linode-repo`. Never commit to `linode-repo` manually. It is a runtime sink, not a source.

---

## Systemd Service

| Property | Value |
|---|---|
| **Unit** | `caos-backend.service` |
| **WorkingDirectory** | `/home/michael-chambers/linode-repo/backend/` |
| **ExecStart** | `/home/michael-chambers/linode-repo/backend/.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000` |
| **EnvironmentFile** | `/home/michael-chambers/linode-repo/backend/.env` |
| **Restart** | `always` (RestartSec=5) |

To check service status: `sudo systemctl status caos-backend`  
To check logs: `sudo journalctl -u caos-backend -n 50`  
To restart: `sudo systemctl restart caos-backend`

---

## Frontend Webroot

| Property | Value |
|---|---|
| **Path** | `/var/www/caosai.net/` |
| **Served by** | nginx → https://caosai.net |
| **Source** | Built from `/home/michael-chambers/caosai.net/frontend/` |

The frontend is a React/TypeScript app built with `npm run build`. The compiled output is copied to the webroot during deploy.

---

## Deploy Script

| Property | Value |
|---|---|
| **Active (server)** | `~/deploy.sh` → `/home/michael-chambers/deploy.sh` |
| **Tracked copy** | `ops/deploy.sh` in this repo |
| **No secrets** | Confirmed. All secrets live in `linode-repo/backend/.env` |

To update the active deploy script from the tracked copy:
```bash
cp /home/michael-chambers/caosai.net/ops/deploy.sh ~/deploy.sh
chmod +x ~/deploy.sh
```

To run a deploy:
```bash
bash ~/deploy.sh
```

### What deploy.sh does

1. `git pull origin aria-emergent-clean-rebuild` — pulls latest from `caosai.net`
2. `rsync` backend Python app from `caosai.net/backend/` → `linode-repo/backend/`
   - **Preserved (never overwritten):** `.venv/`, `.env`, `.env.clean`, `__pycache__/`, `*.pyc`, `*.egg-info`
   - **Overwritten:** all `app/` source files, `requirements.txt`, `README.md`
3. `npm run build` — builds frontend from `caosai.net/frontend/`
4. `sudo cp -r build/* /var/www/caosai.net/` — deploys frontend
5. `sudo systemctl restart caos-backend` — restarts the backend service

---

## Secrets Location

API keys and environment variables are stored **only** at:
```
/home/michael-chambers/linode-repo/backend/.env
```

This file is **not tracked in git**. It is **not** in `caosai.net`. It is **not** synced by rsync (explicitly excluded). If this file is lost, API keys must be re-entered manually.

Keys currently configured (as of 2026-05-26):
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`
- `XAI_API_KEY`
- `MONGO_URI`
- `MONGO_DB_NAME`

Do not paste key values here. Do not commit `.env` to any repo.

---

## Post-Deploy Validation

After every deploy, run this command to confirm receipt-truth is live:

```bash
curl -s -X POST https://caosai.net/api/chat/turn \
  -H "Content-Type: application/json" \
  -d '{"message":"ping","user_id":"dev_user","provider":"anthropic","model":"claude-sonnet-4-6"}' \
  | python3 -c "
import json, sys
d = json.load(sys.stdin)
o = d['data']['receipt']['outputs']
print('provider_called:', o['provider_called'])
print('persistence_written:', o['persistence_written'])
print('error:', o.get('error'))
"
```

Expected output:
```
provider_called: True
persistence_written: True
error: None
```

If `provider_called` is `False`, the receipt-truth fix (FIX-001) is not live. Check that the rsync step ran and the service restarted.

---

## Known Risks

| Risk | Mitigation |
|---|---|
| `linode-repo` GitHub drifts from `caosai.net` | Acceptable — `linode-repo` is a runtime sink. Only the local path matters. |
| `.env` lost from server | Re-enter keys manually. Consider secure backup. |
| `deploy.sh` out of sync with `ops/deploy.sh` | Run the install command above to re-sync. |
| New Python dependency added to `requirements.txt` | Must also run `pip install -r requirements.txt` in `linode-repo/backend/.venv/` after rsync. |
| Service crash after deploy | Check `journalctl -u caos-backend -n 50` for the error. |
