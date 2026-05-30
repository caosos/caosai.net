#!/bin/bash
# =============================================================================
# CAOS Deploy Script
# =============================================================================
#
# SOURCE REPO (development):
#   /home/michael-chambers/caosai.net        → github: caosos/caosai.net
#   Branch: aria-emergent-clean-rebuild      (renamed to CLUADE-CODE-CLEAN-BUILD on GitHub)
#
# RUNTIME PATH (backend):
#   /home/michael-chambers/linode-repo/backend/
#   Systemd service: caos-backend
#   Process: uvicorn app.main:app --host 127.0.0.1 --port 8000
#   .venv and .env live ONLY in linode-repo/backend/ — never in caosai.net/
#
# FRONTEND WEBROOT:
#   /var/www/caosai.net/
#   Served by nginx, proxied through https://caosai.net
#
# WHAT THIS SCRIPT DOES:
#   1. Pulls latest code from caosai.net (source of truth)
#   2. Rsyncs backend Python app files to linode-repo/backend/
#      - Preserves: .venv, .env, .env.clean, __pycache__, *.pyc, *.egg-info
#      - Overwrites: all app/ source files
#   3. Builds the React frontend from caosai.net/frontend/
#   4. Copies built frontend to /var/www/caosai.net/
#   5. Restarts caos-backend via systemd
#
# PRESERVED FILES (never overwritten by rsync):
#   linode-repo/backend/.venv/      — Python virtualenv
#   linode-repo/backend/.env        — environment variables and API keys
#   linode-repo/backend/.env.clean  — env template (no values)
#
# SECRETS:
#   This script contains NO secrets. All API keys live in .env on the server
#   at /home/michael-chambers/linode-repo/backend/.env (not tracked in git).
#
# VALIDATION COMMAND (run after deploy to confirm receipt-truth):
#   curl -s -X POST https://caosai.net/api/chat/turn \
#     -H "Content-Type: application/json" \
#     -d '{"message":"ping","user_id":"dev_user","provider":"anthropic","model":"claude-sonnet-4-6"}' \
#     | python3 -c "
#   import json,sys; d=json.load(sys.stdin)
#   o=d['data']['receipt']['outputs']
#   print('provider_called:', o['provider_called'])
#   print('persistence_written:', o['persistence_written'])
#   "
#   Expected: provider_called: True, persistence_written: True
#
# INSTALL:
#   This tracked copy lives at ops/deploy.sh in the caosai.net repo.
#   The active copy that runs is at ~/deploy.sh on the server.
#   To install/update the active copy from this tracked version:
#     cp /home/michael-chambers/caosai.net/ops/deploy.sh ~/deploy.sh
#     chmod +x ~/deploy.sh
#
# =============================================================================

set -e

# 1. Pull latest from caosai.net (source of truth)
cd /home/michael-chambers/caosai.net
git pull origin aria-emergent-clean-rebuild

# 2. Sync backend Python app to runtime location (preserve .venv and .env)
rsync -a \
  --exclude='.venv' \
  --exclude='.env' \
  --exclude='.env.clean' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='*.egg-info' \
  /home/michael-chambers/caosai.net/backend/ \
  /home/michael-chambers/linode-repo/backend/

# 3. Build frontend from caosai.net
cd /home/michael-chambers/caosai.net/frontend
npm run build

# 4. Deploy frontend to webroot
sudo cp -r build/* /var/www/caosai.net/

# 5. Restart backend service
sudo systemctl restart caos-backend
echo "Deploy complete."
