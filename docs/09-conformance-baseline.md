# 9. Canonical Conformance Baseline

Status: SES-001

This baseline defines the minimum conformance boundary connecting the semantic model, projection contract, expression model, schemas, and conformance documentation. It does not define a renderer or product implementation.

## Invariant matrix

| ID | Invariant | Authority | Evidence | Negative fixture |
|---|---|---|---|---|
| SEM-01 | Element, Block, Slot, Socket, and Composition identities remain stable | `02-semantic-model.md`; `schemas/ses-schema.ts` | IDs match between semantic input and every expression | `unknown-semantic-identity` |
| SEM-02 | Required Slots exist and receive compatible content | `BlockDefinition`; `SlotDefinition` | Cardinality and accepted content validate | `missing-required-slot`; `incompatible-slot-content` |
| SEM-03 | Socket admission, multiplicity, and bounds are valid | `SocketDefinition` | Accepted Block, multiplicity, and min/max validate | `unknown-socket-block`; `invalid-multiplicity` |
| SEM-04 | State meaning remains stable | `SemanticState`; semantic model | Declared states remain representable | `missing-state-fallback` |
| ACT-01 | Required operation identity remains stable | Projection contract; `OperationContract` | Required operation IDs remain attached | `required-operation-removed` |
| ACT-02 | Required operations remain exposed and signaled | Projection contract §5.4 | Exposure and signaling are independently verifiable | `required-operation-hidden` |
| ACC-01 | Accessibility names, relationships, and reading order remain valid | Projection contract; semantic model | Name, role, order, and focus path remain available | `accessibility-name-lost`; `semantic-order-replaced` |
| ACC-02 | Focus and state feedback are not obscured | Projection contract §5.5 | Focus, disabled, error, and selected states remain perceivable | `focus-obscured` |
| PRO-01 | Only declared properties are transformed | `ProjectionContract.transform` | Every topology or appearance mutation maps to a declared transform | `undeclared-semantic-transform` |
| PRO-02 | Omission is explicit | `ProjectionContract.mayOmit` | Omitted content is listed and non-required | `undeclared-omission` |
| PRO-03 | Introduced layers remain presentation-only | `ProjectionContract.mayIntroduce` | Decorations do not create semantic meaning | `decorative-layer-creates-meaning` |
| RES-01 | Recipe targets resolve to semantic identities | Expression model; `VisualLanguage.recipes` | Every target exists | `unknown-recipe-target` |
| RES-02 | Token and asset references resolve | `TokenRegistry`; `AssetRegistry` | All referenced resources exist | `unknown-token`; `unknown-asset` |
| RES-03 | Appearance layers are structurally valid | `ses.schema.json`; expression model | Backgrounds, edges, masks, clipping, bleed, and opacity validate | `invalid-edge-target`; `invalid-background-layer` |
| RSP-01 | Required content and operations survive responsive expression | Projection responsive rules; `07-conformance.md` | Required content is not clipped, unreachable, or overflowed | `required-content-clipped`; `mobile-overflow` |
| VAR-01 | Multiple Visual Languages share one semantic baseline | `07-conformance.md` §7.3 | Same semantic fixture passes through multiple languages | `language-specific-semantic-branch` |

JSON Schema validates record shape only. Cross-record identity, compatibility, reference resolution, accessibility, operation exposure, and responsive behavior require conformance-level validation.

## Fixture plan

### Positive reference vectors

- `valid-home-core`
- `valid-home-neo-edo`
- `valid-home-western-comics`
- `valid-home-cybernetic-minimalism`

Each uses the same `Home` composition and verifies `home.hero` and `home.trending`, including `enter-world`, `open-media`, and `view-all`. Expressions may freely differ in orientation, enclosure, media placement, texture, pattern, edges, and ornament where the Projection Contract permits.

### Negative fixtures

- `invalid-missing-required-slot`
- `invalid-incompatible-slot-content`
- `invalid-unknown-socket-block`
- `invalid-required-operation-hidden`
- `invalid-unknown-token`
- `invalid-unknown-asset`
- `invalid-unknown-recipe-target`
- `invalid-focus-obscured`
- `invalid-semantic-order`
- `invalid-required-content-clipped`
- `invalid-mobile-overflow`
- `invalid-missing-state-fallback`

Each negative fixture maps to one baseline ID and fails at the earliest applicable validation layer.

## Validation order

1. **Shape:** validate records against `schemas/ses.schema.json`.
2. **Semantic:** validate identity, Slot compatibility, Socket admission, cardinality, states, and operations.
3. **Projection:** validate `preserve`, `transform`, `mayOmit`, `mayIntroduce`, and failure conditions.
4. **Resolution:** validate recipe targets, tokens, and assets.
5. **Accessibility and responsive:** validate exposure, focus, order, reachability, and overflow.
6. **Visual:** inspect reference renders only after layers 1–5 pass.

## Scope boundary

SES-001 establishes the conformance contract and fixture inventory only. It does not implement a renderer, runtime resolver, validator, product screen, transport, persistence layer, or external integration.
