# 15. Accessibility-Preserving Expression

Status: SES-009

Visual Languages may change presentation radically, but accessibility semantics and interaction access remain governed by the semantic model and Projection Contract.

## 15.1 Preserved accessibility contract

Every projected target must preserve or explicitly satisfy:

- accessible name and description requirements;
- semantic role and state meaning;
- relationships between labels, controls, descriptions, groups, and errors;
- logical reading order and keyboard order;
- operation reachability and signaling;
- focus visibility and target distinguishability;
- disabled, selected, pressed, loading, error, and expanded state communication;
- reduced-motion and high-contrast fallbacks.

Decorative layers, texture, pattern, edge, mask, image, ornament, and motion do not create accessibility meaning by themselves.

## 15.2 Expression freedoms and constraints

| Expression change | Permitted freedom | Required preservation |
|---|---|---|
| Typography and scale | May vary by Visual Language | readable hierarchy, names, labels, and state distinctions |
| Spatial reorder | May vary visually | logical reading/keyboard order, unless explicitly contracted |
| Enclosure and surface | May be removed, layered, or transformed | grouping, boundaries, focus, and target distinction |
| Media placement and crop | May move, bleed, or become background | alternative text, content priority, and control access |
| Decoration and ornament | May be introduced freely as presentation | no fabricated semantic or accessibility role |
| Motion | May vary by state and language | reduced-motion equivalent and state comprehension |
| Contrast treatment | May vary within theme grammar | high-contrast and focus/state perceivability |

## 15.3 Required checks

- `A11Y-001`: required accessible names are present and stable.
- `A11Y-002`: roles and relationships correspond to semantic identity.
- `A11Y-003`: reading and keyboard order remain coherent after visual topology changes.
- `A11Y-004`: every required operation has a reachable, perceivable control path.
- `A11Y-005`: focus is visible, not covered, and remains associated with the active target.
- `A11Y-006`: state changes are communicated without depending on color, texture, motion, or decoration alone.
- `A11Y-007`: reduced-motion expression preserves state transitions and operation feedback without required animation.
- `A11Y-008`: high-contrast expression preserves names, roles, focus, state, and operation signaling.

## 15.4 Failure conditions

- `ERR_ACCESSIBLE_NAME_MISSING`
- `ERR_ROLE_RELATIONSHIP_INVALID`
- `ERR_KEYBOARD_ORDER_MISMATCH`
- `ERR_OPERATION_NOT_EXPOSED`
- `ERR_FOCUS_INDICATOR_OBSTRUCTED`
- `ERR_STATE_SIGNALING_INSUFFICIENT`
- `ERR_A11Y_FALLBACK_MISSING`
- `ERR_REDUCED_MOTION_UNSUPPORTED`
- `ERR_HIGH_CONTRAST_FALLBACK_MISSING`

Failure occurs when a required contract is absent, unreachable, obscured, or dependent on a presentation cue the declared accessibility context does not guarantee.

## 15.5 Evaluation contexts

Accessibility fixtures evaluate at minimum:

1. keyboard-only navigation;
2. focus-visible state;
3. reduced-motion preference;
4. high-contrast or forced-colors mode;
5. non-color state distinction;
6. narrow responsive layout;
7. required operation exposure and invocation path.

The evaluator records unavailable contexts as limitations or inconclusive results; it does not convert missing evaluation into a pass.

## 15.6 Scope boundary

SES-009 defines accessibility-preserving expression rules and evaluation obligations. It does not prescribe a host framework, DOM implementation, ARIA template, or automated accessibility tool.
