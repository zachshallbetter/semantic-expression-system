# 10. Validator-Level Conformance Contract

Status: SES-003

This document defines the checks required beyond JSON Schema shape validation. It specifies inputs, ordering, failure codes, and evidence requirements; it does not implement a validator or renderer.

## 10.1 Inputs

A conformance run receives:

1. A semantic registry containing Elements, Blocks, Slots, Sockets, Compositions, states, and operation identities.
2. A selected Visual Language, Theme, and resolved Recipe set.
3. A Projection Contract for each projected target.
4. Token and Asset registries.
5. A fixture context containing viewport, accessibility mode, reduced-motion preference, and expected semantic baseline.

The validator must distinguish missing input from an empty valid collection. Unknown discriminators and unknown semantic identities are errors; they are not silently ignored or converted to fallback values.

## 10.2 Validation order

Checks execute in dependency order. A later check may depend on an earlier successful result, but must retain the first typed failure and its evidence path.

| Order | Check family | Baseline IDs | Required check |
|---:|---|---|---|
| 1 | Record shape | all | Validate each record against its declared JSON Schema. |
| 2 | Cross-record identity | SEM-01, RES-01 | Resolve every Slot, Socket, Recipe, State, Variant, and Operation reference against the canonical registry. |
| 3 | Slot compatibility | SEM-02 | Check required cardinality, accepted content type, required Slot declarations, and mutually exclusive Slot constraints. |
| 4 | Socket admission | SEM-03 | Check accepted Block identity/capability, multiplicity, min/max bounds, required participation, and variant restrictions. |
| 5 | Composition structure | RSP-01, VAR-01 | Check hierarchy, relation, content priority, repetition, collapse priority, and responsive participation. |
| 6 | Projection contract | PRO-01, PRO-02, PRO-03 | Check that mutations are declared, omissions are permitted, and introduced layers remain presentation-only. |
| 7 | Resource resolution | RES-02, RES-03 | Resolve tokens, aliases, assets, masks, edges, backgrounds, patterns, and morphology references. |
| 8 | Operation exposure | ACT-01, ACT-02 | Check required operation identity, enabled state, exposure, signaling, and reachable invocation path. |
| 9 | Accessibility and state | SEM-04, ACC-01, ACC-02 | Check accessible name, role, logical order, keyboard order, focus visibility, state feedback, and fallback behavior. |
| 10 | Responsive reachability | RSP-01 | Check required content, required operations, overflow, clipping, collapse, and reachability at each declared viewport context. |

Visual comparison is downstream of this contract. A visually similar render cannot convert a failed semantic or interaction check into a pass.

## 10.3 Cross-record identity checks

- `CHK-IDENTITY-001`: every referenced semantic ID exists exactly once.
- `CHK-IDENTITY-002`: expression recipes target an existing Element, Block, Socket, Composition, State, or Variant.
- `CHK-IDENTITY-003`: Slot and Socket IDs are not reused for different semantic roles within one registry.
- `CHK-IDENTITY-004`: required operation IDs remain identical between source semantics and projection.

Failure codes: `ERR_IDENTITY_UNKNOWN`, `ERR_IDENTITY_DUPLICATE`, `ERR_RECIPE_TARGET_UNKNOWN`, `ERR_OPERATION_ID_CHANGED`.

## 10.4 Slot and Socket checks

- `CHK-SLOT-001`: required Slot cardinality is satisfied.
- `CHK-SLOT-002`: inserted content matches the Slot's accepted element, Block, or content type.
- `CHK-SLOT-003`: mutually exclusive Slot constraints are not violated.
- `CHK-SOCKET-001`: admitted Block matches an accepted identity, variant, or declared capability.
- `CHK-SOCKET-002`: multiplicity and min/max constraints are satisfied.
- `CHK-SOCKET-003`: required Socket participation is present at every required composition level.

Failure codes: `ERR_SLOT_REQUIRED_MISSING`, `ERR_SLOT_CONTENT_INCOMPATIBLE`, `ERR_SLOT_CONSTRAINT_VIOLATED`, `ERR_SOCKET_ADMISSION_DENIED`, `ERR_SOCKET_CARDINALITY_INVALID`, `ERR_SOCKET_REQUIRED_MISSING`.

## 10.5 Projection checks

- `CHK-PROJECTION-001`: every semantic change is classified as preserve, transform, omit, or introduce.
- `CHK-PROJECTION-002`: preserved identity, required content, operation identity, and accessibility relationships are unchanged.
- `CHK-PROJECTION-003`: omitted content appears in `mayOmit` and is not required by the semantic contract.
- `CHK-PROJECTION-004`: introduced layers are non-semantic and cannot create an accessibility or operation identity.
- `CHK-PROJECTION-005`: declared failure conditions are evaluated explicitly.

Failure codes: `ERR_TRANSFORM_UNDECLARED`, `ERR_REQUIRED_CONTENT_OMITTED`, `ERR_INTRODUCED_SEMANTIC_MEANING`, `ERR_PROJECTION_FAILURE_CONDITION`.

## 10.6 Resource and recipe checks

- `CHK-RESOURCE-001`: token references resolve through the declared token layers.
- `CHK-RESOURCE-002`: asset references resolve in the declared asset category.
- `CHK-RESOURCE-003`: edge targets refer to valid boundaries and sides.
- `CHK-RESOURCE-004`: masks, clips, backgrounds, patterns, and appearance sources are present and structurally valid.
- `CHK-RESOURCE-005`: morphology and layout values remain expression data and do not alter semantic identity.

Failure codes: `ERR_TOKEN_UNRESOLVED`, `ERR_ASSET_NOT_FOUND`, `ERR_EDGE_TARGET_INVALID`, `ERR_APPEARANCE_SOURCE_INVALID`, `ERR_MORPHOLOGY_SEMANTIC_MUTATION`.

## 10.7 Operation, accessibility, and responsive checks

- `CHK-INTERACTION-001`: every required operation is exposed through at least one reachable interaction path.
- `CHK-INTERACTION-002`: required operation signaling is present when `requireSignaling` is true.
- `CHK-A11Y-001`: accessible name and role survive expression.
- `CHK-A11Y-002`: logical reading and keyboard order preserve the declared semantic order unless an explicit accessible reorder contract exists.
- `CHK-A11Y-003`: focus indication remains visible and is not covered by appearance layers.
- `CHK-A11Y-004`: disabled, error, selected, loading, reduced-motion, and high-contrast states have an accessible fallback where required.
- `CHK-RESPONSIVE-001`: required content and required operations remain reachable at every declared viewport.
- `CHK-RESPONSIVE-002`: overflow, clipping, hiding, and collapse obey Socket and Projection Contract rules.

Failure codes: `ERR_OPERATION_NOT_EXPOSED`, `ERR_OPERATION_NOT_SIGNALED`, `ERR_ACCESSIBLE_NAME_MISSING`, `ERR_KEYBOARD_ORDER_MISMATCH`, `ERR_FOCUS_INDICATOR_OBSTRUCTED`, `ERR_A11Y_FALLBACK_MISSING`, `ERR_CONTENT_UNREACHABLE`, `ERR_CONTENT_CLIPPED`, `ERR_COMPOSITION_OVERFLOW`.

## 10.8 Evidence requirements

Each check result must retain:

- fixture ID and SES-001 baseline ID;
- check ID and failure code, if any;
- stable path to the source records involved;
- expected value and observed value where comparison is applicable;
- validation layer and execution order;
- limitations, including unavailable renderer or accessibility evaluator.

The result envelope is intentionally left to SES-006. SES-003 defines the evidence fields required by that future format but does not prescribe its final serialization.

## 10.9 Scope boundary

SES-003 defines validator obligations only. It does not add runtime code, alter the JSON Schema contract, implement rendering, infer business behavior, or authorize promotion.
