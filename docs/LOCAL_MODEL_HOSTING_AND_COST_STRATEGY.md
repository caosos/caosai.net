# Local Model Hosting and Cost Strategy

## Purpose

CAOS must support both cloud/API inference and local/server-hosted inference so Michael can control cost, latency, privacy, and provider choice.

## Core distinction

### Cloud/API model

CAOS sends the request to an external provider API.

```text
CAOS backend -> provider adapter -> provider API -> response
```

Benefits:

- minimal server hardware requirement
- best frontier models available quickly
- provider handles model hosting and scaling

Costs/risks:

- API usage can become expensive quickly during heavy build work
- provider latency and rate limits are external dependencies
- secrets and billing require careful governance

### Local/server-hosted model

CAOS sends the request to a model runner on Michael's own server.

```text
CAOS backend -> local model adapter -> local model runtime -> response
```

Benefits:

- potential low marginal cost after server/GPU cost
- better control over runtime and data path
- useful for high-volume utility work, summaries, classification, extraction, draft work, and background jobs

Costs/risks:

- requires suitable CPU/GPU/RAM/storage
- model quality may be lower than premium frontier APIs
- operations, updates, quantization choices, and runtime tuning become Michael's responsibility
- not automatically cheap if GPU server cost is high or underutilized

## Local model runner examples

CAOS should support local runners through adapters rather than hardcoding one runtime.

Potential local/runtime adapter targets:

- Ollama-style local HTTP runtime
- llama.cpp-style local runtime
- vLLM-style server runtime
- other OpenAI-compatible local endpoints

## Cost strategy

Use premium cloud models for:

- high-stakes reasoning
- final architectural decisions
- complex coding synthesis
- multimodal/vision tasks when needed
- tasks requiring the strongest available model

Use local/lower-cost models for:

- summaries
- classification
- memory candidate extraction
- log parsing
- first-pass document cleanup
- routine transformations
- background indexing
- draft generation
- low-risk utility tasks

## Routing implication

The provider router should eventually support task-aware routing:

```text
Task type -> required capability -> cost/latency policy -> selected model
```

Examples:

- memory extraction -> cheap/local model if quality passes threshold
- final user-facing answer -> selected premium/default model
- large log summarization -> local/cheap model first, premium model only for synthesis if needed
- code modification -> strong coding model or selected primary model

## Latency expectations

Local/server-hosted inference can be fast when the server has appropriate hardware and the model size/quantization fits the machine.

Local/server-hosted inference can also be slow if:

- the model is too large for the GPU/RAM
- it falls back to CPU
- context is too large
- the runtime is not tuned
- the server is overloaded

Local does not automatically mean faster. It means controllable.

## Installation model note

Modern command-line installers usually work by using package repositories, registries, or install scripts that fetch software from remote servers, verify/install it locally, and register executable commands or services.

Examples by category:

- OS package manager: `apt install ...`
- Python package registry: `pip install ...`
- Node package registry: `npm install ...`
- Git repository: `git clone ...`
- Model registry/runtime: model pull commands that download model weights locally

## CAOS requirement

CAOS should support both:

1. cloud provider adapters
2. local/server-hosted model adapters

The user-facing UI should remain clean. The admin/provider catalog may expose the detailed capability/cost/latency matrix.

## Non-negotiable

Provider choice must be governed by capability, cost, latency, truth quality, and receipts. CAOS should not burn money unnecessarily when local or cheaper models can safely perform the task.
