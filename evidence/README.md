# Evidence Model

Evidence supports the trace:

```text
intent -> issue -> artifact -> evaluation -> evidence -> qualification -> promotion
```

## Evidence record

Each material result records:

- `id`: stable local evidence identifier
- `issue`: authorized work item
- `claim`: the bounded claim being evaluated
- `source`: artifact, command, fixture, or observation that produced the result
- `method`: how the evidence was obtained
- `result`: pass, fail, partial, or inconclusive
- `limitations`: known gaps or conditions
- `recordedAt`: timestamp supplied by the recording workflow
- `authority`: person or process authorized to qualify the result

Artifact existence is not evidence of implementation, testing, or empirical validation. Negative and inconclusive results remain retained under `docs/NEGATIVE_RESULTS.md`.

## SES evidence classes

- **Specification:** traceability from SES definitions to schemas and conformance rules.
- **Structural validation:** JSON Schema and machine-readable fixture checks.
- **Conformance:** invariant and failure-condition results for a semantic/expression pair.
- **Accessibility:** name, role, order, focus, keyboard, and state-preservation results.
- **Responsive:** reachability, overflow, collapse, and required-operation results.
- **Visual:** reference-render comparison after semantic and interaction checks pass.

## Promotion boundary

IEPE-002 creates only local operating records. It does not qualify SES conformance, publish a release, or promote an implementation. Promotion authority is currently `unassigned` in `PROJECT_PROFILE.json`.
