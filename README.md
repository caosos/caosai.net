# CAOS Linode Clean Rebuild

This repository is the clean server-target rebuild for CAOS.

Source reference repo:
- `caosos/emergent-caos-build`

Working rules:
- no direct edits to source repo required for migration
- no merge to `main` without Michael approval
- no production deploy without Michael approval

Initial purpose:
- reconstruct a clean monorepo for Ubuntu/Linode deployment
- separate portable app code from platform-coupled runtime pieces
- preserve the ability to add multiple model providers later
