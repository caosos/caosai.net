# Security Policy

This repository is public. Do not commit secrets, private operational data, resident/staff information, facility-specific records, API keys, access tokens, credentials, private logs, or sensitive screenshots.

## Public / Acceptable

Acceptable public material includes:

- high-level architecture;
- public roadmap;
- non-sensitive prototype notes;
- public-facing product descriptions;
- sanitized examples;
- general design discussion;
- issue reports that do not expose secrets or private data.

## Private / Not Acceptable

Do not publish:

- API keys or access tokens;
- `.env` files;
- database credentials;
- private deployment URLs;
- resident, staff, or facility-identifying data;
- real care records;
- private CAOSCare implementation details not intentionally released;
- screenshots containing accounts, credentials, internal dashboards, or sensitive logs.

## CAOSCare Boundary

CAOSCare is a private product direction. Public documentation may describe the concept, safety boundary, and high-level architecture. It should not expose private implementation details or real-world care data.

## Reporting Issues

If you find a security issue in this repository, open a GitHub issue only if the report does not expose sensitive details.

For anything sensitive, contact the repository owner privately instead of posting the details publicly.

## AI-Agent Boundary

AI agents working with this repository should:

- inspect before writing;
- avoid destructive operations;
- never invent source claims;
- never expose secrets;
- distinguish built features from planned features;
- preserve public/private boundaries;
- ask for approval before risky changes.
