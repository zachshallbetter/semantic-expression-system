# 14. Responsive Invariants

Status: SES-008

Responsive expression may change spatial arrangement and density, but it may not make required semantic content, operations, accessibility relationships, or priority information unreachable.

## 14.1 Allowed responsive mutations

| Mutation | Default rule | Required condition |
|---|---|---|
| Reorder | Allowed for visual arrangement | Logical reading and keyboard order remain valid, or an explicit accessible reorder contract exists |
| Collapse | Allowed for lower-priority structure | Required content and operations remain reachable through the collapsed representation |
| Hide | Allowed only for optional content or declared responsive omission | The target is not required and omission is permitted by the Projection Contract |
| Transform | Allowed for morphology, orientation, enclosure, density, and media placement | The mutation is declared in `transform` and does not alter semantic identity or behavior |
| Overflow | Allowed only when explicitly declared as wrap, scroll, paginate, or another contract-supported mode | Required content and operations remain reachable and the mode is usable in the target context |
| Clip | Not allowed for required semantic content or focus/operation signaling | Clipping is limited to decorative or explicitly optional expression |

## 14.2 Required invariants

- `RESP-001`: every required Slot, Socket, content item, and operation remains reachable at each declared viewport context.
- `RESP-002`: required operation exposure and accessible naming survive responsive transformation.
- `RESP-003`: content priority and responsive importance determine collapse and hiding order.
- `RESP-004`: a hidden or collapsed target has an explicit replacement path when its meaning or operation remains required.
- `RESP-005`: logical reading order and keyboard order remain coherent after visual reorder.
- `RESP-006`: viewport overflow does not make required content or operations unreachable.
- `RESP-007`: focus indicators, state feedback, and high-contrast/reduced-motion requirements survive responsive expression.
- `RESP-008`: responsive behavior is deterministic for the same semantic target, expression context, and viewport context.

## 14.3 Context matrix

Every responsive fixture declares at least:

| Context | Required evaluation |
|---|---|
| Wide | hierarchy, operation exposure, content priority, and visual topology |
| Narrow | collapse, reordering, wrapping, and required-content reachability |
| Small touch | target reachability, focus/pressed state, operation signaling, and overflow |
| Reduced motion | state transitions remain understandable without required animation |
| High contrast | names, roles, focus, state, and operation signaling remain perceivable |

Projects may add viewport widths or host contexts, but may not remove the required semantic and interaction checks.

## 14.4 Failure conditions

Responsive expression fails when:

- a required Slot, Socket, or operation is hidden without an allowed replacement;
- required content is clipped, covered, or unreachable;
- horizontal or vertical overflow prevents access to required content or operation controls;
- visual reorder changes logical reading or keyboard order without an explicit contract;
- a collapsed control loses its accessible name, state, or operation signaling;
- a responsive state relies on motion that is unavailable or disabled without an equivalent state expression.

Failure codes use `ERR_CONTENT_UNREACHABLE`, `ERR_CONTENT_CLIPPED`, `ERR_COMPOSITION_OVERFLOW`, `ERR_KEYBOARD_ORDER_MISMATCH`, `ERR_OPERATION_NOT_EXPOSED`, and `ERR_A11Y_FALLBACK_MISSING` from SES-003.

## 14.5 Scope boundary

SES-008 defines responsive preservation rules and evaluation contexts. It does not prescribe breakpoint values, CSS, host layouts, or a responsive renderer.
