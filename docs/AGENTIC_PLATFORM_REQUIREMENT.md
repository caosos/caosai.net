# Agentic Platform Requirement

## Purpose

A core CAOS requirement is that Aria must be able to work like the current ChatGPT build partner experience: inspect source material, reason over the build, create or modify files, commit changes, preserve receipts, document decisions, and continue bounded implementation without requiring Michael to manually perform every edit.

This is one of the most important requirements in the system.

## Product requirement

CAOS must support an agentic build/work mode where the AI can operate across connected tools and repositories under user-defined governance.

The target behavior includes:

- inspect repositories and documents
- create files
- update files
- produce commits or change proposals
- write documentation
- maintain receipts
- preserve build state
- identify risks before acting
- work in bounded batches
- avoid unnecessary questions when authorized scope is clear
- stop for high-risk actions

## Why this matters

Michael has wanted this capability since first using AI platforms. The goal is not merely conversation. The goal is a served, user-owned CAOS platform where Aria can help build, manage, inspect, and operate real work with tools, memory, receipts, and boundaries.

Current external platforms provide some of this capability, but CAOS must eventually bring this into Michael's own hosted system.

## Near-term reality

Until the clean platform is built and hosted, existing external platforms may continue to be used for working references, testing, and comparison.

There is no rush to force premature deployment. The rebuild should proceed correctly and deliberately.

## Governance requirement

Agentic capability must not mean reckless autonomy.

Low-risk allowed actions may include:

- documentation updates
- source inspection
- bounded branch work
- file creation inside assigned scope
- receipts and status updates
- non-destructive code scaffolding

High-risk actions require explicit approval, including:

- production deployment
- main-branch merge
- destructive deletion
- financial movement
- legal/contractual action
- credential or secret exposure/rotation
- external messages sent as the user
- physical-world or machine-control actions

## Hosting implication

The long-term target is a user-owned hosted CAOS platform, likely on dedicated hosting/server infrastructure, that can expose controlled agent capabilities through safe connectors and tools.

Required platform components include:

- authenticated user session
- tool/capability registry
- permission gates
- receipts/audit log
- repository/file/document connectors
- memory and ARC hydration
- provider router
- secrets stored outside GitHub/chat
- admin observability
- regression/feature locks

## Non-negotiable

CAOS must eventually let Aria do real work like this session demonstrates, but with Michael's governance, receipts, hosted infrastructure, and safety gates.

The goal is not to copy a third-party platform. The goal is to build the CAOS-owned version of this capability cleanly and safely.
