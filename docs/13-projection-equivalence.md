# 13. Projection Equivalence Vectors

Status: SES-007

Projection-equivalence testing evaluates multiple expressions of one semantic contract. It does not require pixel equality. It requires semantic, behavioral, action, accessibility, and required-content invariants to remain equivalent while declared morphology and visual properties may vary.

## 13.1 Equivalence relation

Two projections are equivalent for a fixture when they share:

- the same Composition, Socket, Block, Slot, Element, State, Variant, and Operation identities;
- the same required content and content priority;
- the same required operation identity, enabled state, exposure, and reachable invocation path;
- the same accessible names, roles, relationships, and logical order;
- the same responsive reachability obligations;
- no undeclared semantic mutation or prohibited omission.

They may differ in orientation, topology, enclosure, spacing, media placement, background, edge, texture, pattern, typography, ornament, density, and other expression properties listed by their Projection Contracts.

## 13.2 Reference vector

The canonical vector uses `Home` with `home.hero` and `home.trending`:

```text
semantic identities:
  home
  home.hero
  home.trending
  hero
  media-rail | media-grid | ranked-collection

required operations:
  enter-world
  open-media
  view-all

required preserved properties:
  identity
  content-priority
  primary-action
  accessibility-order
  operation-exposure
  required-content-reachability
```

## 13.3 Expression diversity

| Vector | Visual Language | Permitted expression difference |
|---|---|---|
| `valid-home-core` | Core | restrained orientation, enclosure, spacing, and alignment changes |
| `valid-home-neo-edo` | Neo-Edo | asymmetric placement, layered paper texture, targeted brush edges, pattern, ornament |
| `valid-home-western-comics` | Western Comics | panel topology, halftone, bold edges, speech-like annotation, high-contrast grouping |
| `valid-home-cybernetic-minimalism` | Cybernetic Minimalism | technical grid, sparse enclosure, glow, data-like alignment, dense responsive reflow |

Each vector must be evaluated against the same semantic fixture. Language-specific recipe data may change expression, but it may not introduce language-specific semantic branches or operation identities.

## 13.4 Equivalence checks

- `EQUIV-001`: semantic identity sets are equal across all vectors.
- `EQUIV-002`: required operation sets and exposure obligations are equal across all vectors.
- `EQUIV-003`: required Slot and Socket participation is equal across all vectors.
- `EQUIV-004`: accessible names, relationships, state meaning, and logical order remain equivalent.
- `EQUIV-005`: required content remains reachable at each declared responsive context.
- `EQUIV-006`: every expression difference is declared by the relevant Projection Contract.
- `EQUIV-007`: no vector contains a Visual Language-specific semantic or business-logic branch.

Failure codes use the SES-003 contract: `ERR_IDENTITY_UNKNOWN`, `ERR_OPERATION_ID_CHANGED`, `ERR_OPERATION_NOT_EXPOSED`, `ERR_REQUIRED_CONTENT_OMITTED`, `ERR_KEYBOARD_ORDER_MISMATCH`, `ERR_CONTENT_UNREACHABLE`, and `ERR_TRANSFORM_UNDECLARED`.

## 13.5 Scope boundary

SES-007 defines equivalence fixtures and checks. It does not render the vectors, claim visual fidelity, or implement a regression runner.
