# Search and Retrieval Behavior Contract

## Purpose

Search and retrieval in CAOS must behave like a useful memory/relevance system, not like brittle exact string matching.

This contract defines what "not exact-match only" means in practical, testable behavior.

## Core requirement

When a user searches previous threads, memory, artifacts, support tickets, documents, or other stored records, the system should return relevant results even when the query is incomplete, out of order, partially remembered, misspelled, or semantically related.

## Required retrieval behavior

CAOS search should support:

- exact title match
- partial title match
- multi-keyword title match
- body/content match
- metadata match
- fuzzy spelling tolerance
- semantic similarity when model/search infrastructure supports it
- recency and relevance ranking
- category/source filtering when available

## Example: previous thread search

If a thread title is:

```text
Hello Aria, tomorrow is my birthday
```

The search should return it for queries like:

```text
hello birthday
birthday tomorrow
helo birthday
tomorow birthday
aria birthday
```

The user should not need to remember the exact title or exact word order.

## Ranking expectations

When multiple results match, ranking should prefer:

1. stronger title matches
2. stronger phrase/keyword overlap
3. semantic relevance
4. recent active threads when relevance is close
5. user-pinned or high-priority items when available

## Memory retrieval expectation

Memory retrieval must go beyond keyword lookup.

Example user query:

```text
Do you remember that boat I bought about two years ago from that guy down in southeast Arkansas?
```

Expected system behavior:

- identify likely memory clusters about boats
- consider time references around "two years ago"
- consider place references such as southeast Arkansas
- detect that multiple boat-related memories may exist
- return a differentiated answer instead of a blob
- explain uncertainty if more than one match is plausible
- surface related facts, people, conversations, parts, repairs, and relevant context when available

## Native model capability rule

When using an inference engine with strong native reasoning/retrieval capability, CAOS should not fight that capability with brittle rules.

The platform should provide structured, well-scoped candidate context and let the capable model perform relevance reasoning inside the governed response path.

The implementation should avoid over-constraining the model into exact-match behavior when the selected model can reason semantically.

## Implementation strategy

The retrieval stack may combine:

- database text indexes
- normalized keyword matching
- fuzzy matching
- embeddings/vector search
- metadata filters
- recency weighting
- model-assisted reranking
- ARC/hydration policy

These mechanisms are implementation details. The product behavior requirement is relevant recall, not exact string matching.

## Acceptance criteria

A search implementation is not accepted unless it can demonstrate:

- partial remembered title returns expected thread
- misspelled query still returns likely match
- body text can be found even if title does not match
- multiple plausible memories are separated and explained
- irrelevant blob dumps are avoided
- uncertainty is stated when needed

## Non-negotiable

No feature should ship where previous-thread search or memory retrieval requires the user to remember exact wording.
