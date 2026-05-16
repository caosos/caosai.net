# Migration Sources

Status: active source map
Authority: Michael Chambers

## Primary repositories

```text
caosos/caosai.net
```

CAOS AI server/core/runtime repository. This is the forward home for owned Linode/server work, orchestration, memory, governance, model routing, receipts, tools, and shared platform services.

```text
caosos/CAOSCARE.COM
```

CAOS Care product repository. This is the senior-care product surface and should stay separate from CAOS AI core.

## Prototype and reference repositories

```text
caosos/emergent-caos-build
```

Full-stack prototype/source/salvage. Use for inspection and selective salvage. Do not treat Emergent as the future deployment owner.

```text
caosos/caos-os-A1
```

Base44 reference/prototype only. Use for UX/runtime lessons and reference material when explicitly useful. Do not treat Base44 as the future CAOS AI server runtime.

```text
caosos/linode-repo
```

Historical repository name before rename to `caosos/caosai.net`. Do not use this name for forward product identity except when documenting migration history.

## Server-local sources

```text
/home/michael-chambers/CAOS_LINODE_SALVAGE_2026-05-09
```

Salvage-only local directory on the Linode server. It contains old CAOS material and must not be treated as the forward runtime target.

```text
/home/michael-chambers/linode-repo
```

Existing local clone name on the Linode server from before the GitHub repo rename. It may need its remote updated to `https://github.com/caosos/caosai.net.git` and may later be renamed locally after inspection.

```text
/opt
```

Clean forward deployment root. Use separate deploy targets:

```text
/opt/caosai
/opt/caoscare
```

## Migration rule

Prototype repos and salvage directories are source material. They are not the authority.

Forward authority is GitHub:

```text
caosos/caosai.net
caosos/CAOSCARE.COM
```

Forward runtime is owned server infrastructure under explicit deployment targets.
