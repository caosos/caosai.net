# CAOS Linode Migration Manifest

## Source and destination

- Source reference: `caosos/emergent-caos-build`
- Destination rebuild: `caosos/linode-repo`
- Working branch: `aria-emergent-clean-rebuild`

## Operating intent

Build a clean Ubuntu/Linode-ready monorepo while leaving the Emergent source repo intact.

## Target layout

```text
frontend/   React application
backend/    Python API/services runtime
docs/       migration notes, architecture, contracts
scripts/    local/dev/deploy helper scripts
infra/      optional deployment/systemd/nginx/docker assets
```

## What is portable from the source repo

### Frontend
- `frontend/package.json`
- `frontend/craco.config.js`
- `frontend/src/...`
- frontend static/config files

### Backend
- `backend/requirements.txt`
- `backend/app/...`
- backend route/service/model files

### Documentation
- repo maps
- latency/turntrace docs
- architecture notes needed for rebuild

## What must be re-created outside source control
- environment variables
- provider/API secrets
- database connection strings
- file/object storage credentials
- deployment/runtime server configuration

## Current migration rule set
- read from source repo
- write only into destination repo
- no merge to `main` without Michael approval
- no production deploy without Michael approval
- no destructive deletion of major systems without explicit approval
