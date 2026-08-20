# 7. Conformance

SES uses layered conformance. Passing one layer does not imply another.

## S - Semantic Conformance

Checks that Element, Slot, Block, Socket, Composition, Variant, State, and Operation contracts are valid.

Examples:

- required Slots exist
- Socket admission is valid
- required operations are declared
- semantic identity is stable
- accessibility relationships exist

## C - Composition Conformance

Checks hierarchy, content priorities, repetition, responsive importance, and structural constraints.

## R - Recipe Conformance

Checks that every referenced Recipe, token, asset, morphology rule, and appearance rule resolves.

## A - Appearance Conformance

Checks backgrounds, textures, patterns, edges, masks, clipping, bleed, compositing, and decoration for valid construction and renderer support.

## I - Interaction Conformance

Checks keyboard interaction, focus order, focus visibility, operation exposure, disabled states, errors, recovery paths, and state behavior.

## V - Visual Validation

Checks reference renders, intended language fidelity, clipping, overlap, typography, density, and responsive rendering.

Visual validation does not prove semantic or interaction conformance.

## 7.1 Negative fixtures

The test suite should intentionally include invalid languages and themes.

Required negative cases include:

```text
missing required Slot
unknown Block in Socket
required operation hidden
unknown token
unknown asset
invalid edge target
mask covers focus state
background layer references missing source
mobile horizontal overflow
required content clipped
semantic order replaced by decorative order
state variant missing accessibility fallback
```

## 7.2 Language completeness

A language validator should be able to report coverage such as:

```text
Elements covered
Blocks covered
Sockets covered
Compositions covered
Token references valid
Assets valid
Required states covered
Reduced motion covered
High contrast fallback covered
Responsive recipes valid
```

## 7.3 Reference vectors

A project should maintain a small stable set of semantic Compositions rendered through multiple Visual Languages.

For example:

```text
Home + Core
Home + Neo-Edo
Home + Western Comics
Home + Cybernetic Minimalism
```

All must pass the same semantic and operation invariants even when their pixels and morphology differ substantially.

## 7.4 Canonical baseline

The traceable invariant matrix, fixture inventory, validation order, and scope boundary for this conformance model are defined in [09-conformance-baseline.md](09-conformance-baseline.md).

## 7.4 Canonical Matrix Artifact

The active invariant baseline and negative fixture plan is tracked in the repository artifact:
- [`docs/conformance/ses-001-matrix.json`](file://$HOME/Projects/Semantic-Expression-System/docs/conformance/ses-001-matrix.json)
