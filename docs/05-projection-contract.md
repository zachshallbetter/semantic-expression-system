# 5. Projection Contract

The Projection Contract governs the boundary between semantic structure and visual expression.

It exists to make radical mutation explicit and testable.

## 5.1 Responsibilities

A Projection Contract declares:

- semantic target
- identity and authority
- properties that must be preserved
- properties that may be transformed
- optional properties that may be omitted
- presentation-only properties that may be introduced
- required operations
- required operation exposure
- accessibility constraints
- responsive constraints
- tolerance where applicable
- failure conditions

## 5.2 Typed invariance

Preservation is typed. A projection may be semantically invariant while visually and morphologically different.

Recommended UI invariance dimensions:

```text
semantic
behavioral
actionIdentity
structural
morphological
visual
```

Each may be:

```text
required
bounded
free
```

A typical expressive application may require semantic, behavioral, and action identity invariance while allowing bounded structural change and free morphological and visual change.

## 5.3 Preserve, transform, omit, introduce

Example:

```ts
projection: {
  preserve: [
    "series-identity",
    "content-priority",
    "view-all-operation",
    "accessibility-order"
  ],

  transform: [
    "orientation",
    "media-placement",
    "enclosure",
    "spacing",
    "alignment",
    "surface",
    "edge",
    "texture"
  ],

  mayOmit: [
    "secondary-decoration",
    "nonessential-caption"
  ],

  mayIntroduce: [
    "ornament",
    "background-art",
    "pattern",
    "section-label-decoration"
  ]
}
```

## 5.4 Operation exposure

SES distinguishes operation existence from operation presentation.

At minimum, the runtime should preserve these distinctions:

```text
operation exists
operation is enabled
operation is exposed
operation is signaled
operation is invoked
operation succeeds or fails
```

A Theme may radically alter signaling. It may not silently remove required exposure.

## 5.5 Failure conditions

A projection is invalid if any declared failure condition occurs.

Common failures include:

- required Slot omitted
- required Socket unfilled
- incompatible Block admitted
- required operation unexposed
- focus indicator obscured
- semantic reading order invalidated
- accessibility name lost
- required content clipped or unreachable
- responsive layout violates minimum visibility
- unresolved token or asset reference
- recipe references unknown semantic identity
- theme-specific implementation changes business behavior
