# Work Graph Proposal

Provider: `local`

This is the proposed dependency graph for the next bounded work. Existing SES documents remain the source of truth for specification content; this graph governs execution state only.

```text
SES-001 (canonical conformance baseline) [completed]
  -> SES-002 (formalize conformance fixtures) [completed — structurally validated]
      -> SES-003 (close schema/conformance gaps) [completed — contract defined]
          -> SES-006 (conformance result format) [completed — format defined]
          -> SES-019 (cross-language regression coverage) [completed — semantic regression check added]
  -> SES-004 (resolver boundary) [completed — contract defined]
      -> SES-007 (projection equivalence vectors) [completed — vector contract defined]
      -> SES-010 (token and asset resolution rules) [completed — contract defined]
      -> SES-011 (recipe precedence and conflict handling) [completed — contract defined]
      -> SES-014 (renderer-neutral output contract) [completed — contract defined]
```

Cross-cutting documentation goal SES-020 is completed as protocol-neutral adoption guidance. SES-005 is completed as a vocabulary-only contract.

SES-008 is completed as a responsive expression contract.
SES-009 is completed as an accessibility expression contract.
SES-012 is completed as a semantic branch prohibition contract.
SES-015 is completed as a change-governance contract.
SES-016 is completed as a security and trust-boundary contract.
SES-017 is completed as a provisional performance contract.
SES-018 is completed as an authoring-boundaries contract.
SES-013 is completed as a reference fixture pack.
SES-020 is completed as a host/application boundary contract.
SES-021 is completed as a local pure resolver; SES-022 is completed as canonical resolved-output fixtures; SES-023 is completed as the first validator implementation; SES-024 is completed as declarative negative-fixture execution; SES-025 is completed as pure token and asset resolution; SES-026 is completed as deterministic recipe precedence and conflict detection; SES-027 is completed as projection-contract enforcement; SES-028 is completed as deterministic serialization and snapshot comparison; SES-029 is completed as a minimal DOM/CSS renderer adapter; SES-030 is completed as semantic identity equivalence across expressions; SES-031 is completed as operation exposure and host routing; SES-032 is completed as accessibility metadata validation; SES-033 is completed as keyboard/focus metadata validation; SES-034 is completed as responsive reachability/state validation; SES-035 is completed as reduced-motion/high-contrast handling; SES-036 is completed as security trust-boundary validation; SES-037 is completed as local performance measurement; SES-038 is completed as framework-neutral host adapter; SES-039 is completed as cross-language summary and mutation testing; SES-040 is completed as a locally qualified implementation candidate.

## State rules

- `ready` means bounded, reversible, locally authorized, and evaluable.
- `blocked` means a declared dependency or authority is missing.
- `completed` means the artifact exists and its acceptance evidence is recorded.
- `verified` requires independent qualification beyond documentation existence.
