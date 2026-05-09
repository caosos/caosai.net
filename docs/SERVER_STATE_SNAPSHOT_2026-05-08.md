# Server State Snapshot — 2026-05-08

## Purpose

This document records the server cleanup/quarantine state so future work does not repeatedly rediscover the same old CAOS directories.

## Server

```text
Host: caos-o-s
User: michael-chambers
Home: /home/michael-chambers
OS: Ubuntu 24.04.4 LTS
Python: 3.12.3
Node: v18.19.1
npm: 9.2.0
Nginx: installed/running
Open ports observed: 22, 80
Docker: not present in inspection output
```

## Decision

Old CAOS server material was not deleted. It was quarantined into one dated salvage folder so the home directory is clean enough for the forward build.

## Salvage folder

```text
/home/michael-chambers/CAOS_SALVAGE_2026-05-08
```

## Moved into salvage

```text
/home/michael-chambers/caos-a1
/home/michael-chambers/caos-a1_BACKUP_20251222_0013
/home/michael-chambers/caos-a1_BACKUP_20251222_0014
/home/michael-chambers/CAOS-A1_CANONICAL_2025-12-29
/home/michael-chambers/CAOS-A1_CANONICAL_2025-12-29 (2)
/home/michael-chambers/CAOS-A1_CANONICAL_2025-12-29.tar.gz
/home/michael-chambers/Downloads/caos-os-A1-main
/home/michael-chambers/Downloads/caos_captures
/home/michael-chambers/.local/state/caos-bridge
/home/michael-chambers/caos_rf_bridge.py
```

## Confirmed salvage contents after move

```text
CAOS_SALVAGE_2026-05-08/
  caos-a1/
  caos-a1_BACKUP_20251222_0013/
  caos-a1_BACKUP_20251222_0014/
  CAOS-A1_CANONICAL_2025-12-29/
  CAOS-A1_CANONICAL_2025-12-29 (2)/
  CAOS-A1_CANONICAL_2025-12-29.tar.gz
  caos-bridge/
  caos_captures/
  caos-os-A1-main/
  caos_rf_bridge.py
```

## Forward rule

Do not treat `/home/michael-chambers/CAOS_SALVAGE_2026-05-08` as the active runtime.

It is salvage/reference only.

The active forward checkout should be:

```text
/home/michael-chambers/linode-repo
```

The forward repo should come from:

```text
https://github.com/caosos/linode-repo.git
```

Branch:

```text
aria-emergent-clean-rebuild
```

## Current next step

Clone or verify `/home/michael-chambers/linode-repo`, then run the documented local smoke test from the real checkout.

No future agent should repeat broad home-directory rediscovery unless this snapshot is superseded or contradicted by new evidence.
