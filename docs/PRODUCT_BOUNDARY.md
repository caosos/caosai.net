# Product Boundary

Status: active repository boundary
Authority: Michael Chambers

## CAOS AI

`caosos/caosai.net` is the CAOS AI server/core/runtime repository.

It owns the platform-level brain and governed runtime concepts:

- orchestration;
- memory architecture;
- model routing;
- tool and connector policy;
- receipts;
- bounded worker agents;
- API contracts;
- server runtime discipline;
- shared intelligence services for CAOS ecosystem products.

CAOS AI must not become a giant senior-care application. Domain products should consume CAOS AI through defined interfaces instead of absorbing or duplicating the whole platform.

## CAOS Care

`caosos/CAOSCARE.COM` is the CAOS Care product repository.

It owns the senior-care product surface:

- residents;
- rooms/apartments;
- staff workflows;
- care plans;
- alerts;
- wearable/pendant/tablet/kiosk flows;
- family/staff dashboards;
- care documentation;
- predictive behavior-change awareness.

CAOS Care should not absorb the full CAOS AI brain. It should call into CAOS AI through APIs/contracts where shared intelligence, memory, orchestration, receipts, or model routing are needed.

## Prototype boundaries

- `caosos/emergent-caos-build` is prototype/source/salvage.
- `caosos/caos-os-A1` is Base44 reference only.
- The old `caosos/linode-repo` name is historical only after the repo rename to `caosos/caosai.net`.

## Deployment boundary

Recommended clean deployment targets:

```text
/opt/caosai
/opt/caoscare
```

The current Linode contains legacy/salvage material under `/home/michael-chambers/CAOS_LINODE_SALVAGE_2026-05-09`. That path is salvage-only and should not be treated as the forward runtime target.

## Rule

CAOS AI is the brain/platform.
CAOS Care is a product powered by the brain.
They are separate repos, separate deploy targets, and one ecosystem.
