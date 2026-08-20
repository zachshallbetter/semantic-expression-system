# 25. Accountability and Implementation Readiness

Status: Reconciled 2026-08-16; SES-040 candidate qualified locally

This record maps the lessons from the IEPE/SES baseline to canonical artifacts, evidence, limitations, and next authorized work. It distinguishes documented contracts from implemented or empirically validated behavior.

## 25.1 Lesson-to-accountability matrix

| Lesson | Canonical account | Current maturity | Remaining responsibility |
|---|---|---|---|
| SES is an interface intermediate representation, not a design system | `docs/01-definition.md`, `docs/11-resolver-boundary.md`, `docs/19-renderer-neutral-output.md` | implemented locally | keep runtime APIs renderer-neutral |
| Tokens cannot express all topology changes | `docs/03-expression-model.md`, `docs/17-recipe-precedence.md` | implemented locally | expand morphology coverage without semantic branching |
| Projection Contracts govern expression freedom | `docs/05-projection-contract.md`, `docs/13-projection-equivalence.md` | locally tested | add independent host evaluation |
| Conformance needs evidence, not assertions | `docs/09-conformance-baseline.md`, `docs/10-validator-contract.md`, `docs/conformance/result.schema.json` | locally tested | retain failures and obtain independent evaluator evidence |
| Accessibility and responsiveness are invariants | `docs/14-responsive-invariants.md`, `docs/15-accessibility-expression.md` | metadata locally tested | exercise host-renderer and assistive-technology paths |
| Renderer neutrality is required | `docs/19-renderer-neutral-output.md` | DOM/CSS adapter locally tested | add a second host and compare semantics |
| Host applications own external concerns | `docs/24-protocol-neutral-adoption.md`, `docs/23-authoring-boundaries.md` | adapter boundary locally tested | record each production adapter's authority and version boundary |
| IEPE requires bounded, evidence-backed work | `.iepe/protocol-reference.json`, `PROJECT_PROFILE.json`, `work/GRAPH.md`, `evidence/` | operational layer installed | preserve issue/evidence linkage for implementation work |
| Security and performance precede runtime adoption | `docs/21-security-trust-boundaries.md`, `docs/22-performance-budgets.md` | provisional contracts documented | convert limits and trust checks into executable gates |

## 25.2 Maturity statement

The repository has a **locally qualified implementation candidate** with a documented specification baseline, machine-readable fixtures, result formats, an executable resolver/validator path, a DOM/CSS adapter, local performance measurements, and cross-runtime summary checks. It does not claim production accessibility behavior, production performance, or empirical cross-framework equivalence.

Evidence must promote those dimensions independently:

```text
documented -> implemented -> tested -> empirically validated
```

No later stage may be inferred from an earlier stage's artifact existence.

## 25.3 Responsible implementation gates

Before promoting runtime work beyond the local candidate, the coordinator must require:

1. A pure resolver implementation against `docs/11-resolver-boundary.md` and `docs/19-renderer-neutral-output.md`.
2. A validator implementation that emits `docs/conformance/result.schema.json` records and preserves negative results.
3. At least one host renderer adapter with stable semantic and operation identity.
4. Accessibility and responsive execution evidence from the selected host environment.
5. Security checks for executable expression inputs, unsafe assets, and custom sources.
6. Measurements against provisional budgets, with environment and method recorded before promotion.
7. A framework-neutral adapter test proving application transport, persistence, synchronization, authorization, and navigation remain outside SES.

These are future implementation gates, not claims that the current repository has completed them.

## 25.4 Current material unknowns

- The first host renderer and runtime language are not selected.
- The independent validator implementation boundary is not selected.
- Performance budgets have no empirical calibration environment.
- Accessibility evidence requires a named host platform and evaluator.
- Promotion authority remains `unassigned` in `PROJECT_PROFILE.json`.

These unknowns do not block the specification baseline, but they block implementation-maturity or release-readiness claims.

## 25.5 Next bounded work

SES-040 records the current candidate. The next promotion requires an assigned promotion authority and independent browser/accessibility, production-load, and framework-integration evaluation; those actions remain outside the current local authorization.
