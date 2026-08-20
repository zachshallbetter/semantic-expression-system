# 2. Semantic Model

## 2.1 Element

An Element is the smallest semantically meaningful interface object.

Examples include Button, IconButton, Heading, Text, Image, Avatar, Badge, Tag, Input, Select, Checkbox, Switch, Progress, Divider, Rating, and Price.

An Element owns semantics, accessibility, interaction behavior, and content requirements. It should own as little visual identity as possible.

A Button knows that it is actionable and may be primary, destructive, disabled, loading, focused, or pressed. It does not inherently know that it is a pill, ink strip, chrome capsule, square plate, or paper tab.

## 2.2 Slot

A Slot is a named semantic insertion point inside a Block.

A Slot answers: what kind of content belongs here?

Examples include media, title, subtitle, eyebrow, description, leading, trailing, meta, badge, status, actions, footer, overlay, avatar, icon, progress, and price.

A Slot does not prescribe presentation. `slot="media"` means that the content is primary media for the Block. It does not require a specific position, crop, aspect ratio, border, or enclosure.

## 2.3 Block

A Block is a reusable semantic composition of Elements and Slots.

Examples include MediaCard, Hero, Stat, NavigationItem, SearchField, Post, SeriesItem, WorldItem, ActivityItem, SectionHeader, PriceBlock, ProfileSummary, and ProgressSummary.

A Block defines:

- semantic role
- supported Slots
- required and optional content
- semantic ordering
- behaviors
- variants
- states
- operation relationships
- responsive importance
- accessibility relationships

A Block does not completely prescribe its graphical topology.

## 2.4 Socket

A Socket is a named, typed participation boundary within a Block or Composition.

A Socket declares the semantic role of a region, the Blocks it may receive, multiplicity, importance, required operations, invariants, and the transformations permitted during visual projection.

A Slot governs content participation inside a Block. A Socket governs Block participation inside a larger semantic structure.

A Socket is not a coordinate, column, card shell, or CSS grid area. Those are presentation decisions supplied by a Recipe.

A Socket may declare:

- accepted Block identities or capabilities
- single, optional, or repeating participation
- minimum and maximum participants
- content importance
- semantic and behavioral invariants
- structural and morphological freedom
- required operation exposure
- responsive preservation rules
- projection failure conditions

## 2.5 Composition

A Composition is the semantic arrangement and relationship of Sockets for a screen, page, shell, flow, or section.

A Composition defines information hierarchy and participation, not a fixed pixel layout.

A Home Composition might declare Sockets for navigation, utility, hero, statistics, journey, trending, worlds, activity, community, library, closing action, and footer. A Visual Language may render those as rails, panels, printed fields, overlapping editorial regions, or borderless sections while preserving their semantic contracts.

## 2.6 Variant

A Variant is a semantic specialization of an Element or Block.

Examples:

```text
Button
  primary
  secondary
  destructive
  quiet

Card
  default
  featured
  promotional
  interactive

Badge
  status
  category
  live
```

Variants must not encode Visual Language identity. `westernButton`, `edoCard`, and `cyberBadge` are invalid architectural patterns.

## 2.7 State

A State represents interaction or application condition.

Canonical state vocabulary may include:

```text
default
hover
focus
pressed
selected
active
disabled
loading
error
success
warning
read
unread
owned
locked
```

States have stable semantic meaning. The active Visual Language determines how each state is expressed.

## 2.8 Operation

An Operation is a semantic action exposed by the interface.

Examples include open-series, save, purchase, continue-reading, view-all, dismiss, search, submit, and navigate-home.

Operation identity must remain separate from visual signaling. A projection may alter how an operation is signaled, but required operations may not silently disappear because of theme styling.
