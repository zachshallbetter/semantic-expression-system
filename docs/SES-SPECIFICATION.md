# 1. Canonical Definition

## 1.1 Semantic Expression System

The Semantic Expression System is a semantic composition architecture in which Elements provide atomic behavior, Slots define named content relationships inside reusable Blocks, Sockets define typed participation boundaries for Blocks inside larger structures, and Compositions define screen-level semantic organization.

Visual Languages provide replaceable graphical grammars. Themes configure those grammars. Recipes map semantic objects to presentation. Morphology controls structural visual organization. Appearance controls layered graphical construction. Tokens and assets provide the resolved values and resources used by the renderer.

A Projection Contract sits between semantic structure and visual expression. It declares which properties must be preserved, which may be transformed, which may be omitted, which presentation-only properties may be introduced, which operations must remain exposed, and which conditions invalidate the projection.

## 1.2 Goal

SES is designed for extreme visual mutation without semantic or behavioral fragmentation.

The same semantic interface may be expressed as a restrained digital product, printed editorial system, dense technical console, handmade paper interface, high-key futurist product, or another visual language without branching into language-specific application screens.

## 1.3 Invariants

The following are semantic by default and should remain stable across Visual Languages unless a contract explicitly permits otherwise:

- semantic role
- data identity
- Block identity
- Slot identity
- Socket identity
- operation identity
- required content
- accessibility relationships
- state meaning
- business behavior
- routing intent
- responsive importance
- content priority

## 1.4 Mutable expression

The following are expression concerns and may vary radically:

- color
- typography
- spacing
- density
- shape
- radius
- clipping
- internal layout
- media placement
- container backgrounds
- layered backgrounds
- custom imagery
- surface material
- targeted edges
- partial edges
- edge imagery
- textures
- patterns
- masks
- blend modes
- ornament
- image treatment
- icon family
- shadow and glow
- section framing
- navigation appearance
- motion
- responsive visual topology

## 1.5 Governing rule

If Neo-Edo, Western Comics, Cybernetic Minimalism, Neo-Capsule Futurism, and MangaVerse Core could reasonably disagree about a visual property, that property belongs in a token, recipe, morphology rule, appearance rule, or Visual Language grammar rather than being hard-coded into a semantic Element or Block.
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
# 3. Expression Model

## 3.1 Visual Language

A Visual Language is the highest-level 2D graphical grammar in SES.

It defines the coherent rules by which semantic structure is expressed, including palette, typography, spacing, morphology, shape, surface, edge, texture, pattern, image treatment, iconography, depth, ornament, controls, navigation, and motion.

A Visual Language is broader than a palette or conventional design-system theme.

## 3.2 Theme

A Theme is a concrete configuration of a Visual Language.

Example:

```text
Visual Language: Neo-Edo
Themes:
  Neo-Edo / Ink
  Neo-Edo / Vermilion
  Neo-Edo / Moon
  Neo-Edo / Winter
```

A Theme may override tokens and selected Recipes, but should preserve the defining grammar of its Visual Language. If a configuration replaces most of the typography, surface philosophy, shape grammar, image treatment, edge system, morphology, and motion character, it is likely a separate Visual Language.

## 3.3 Recipe

A Recipe maps a semantic target to presentation behavior.

Recipe targets may include:

- Elements
- Blocks
- Sockets
- Compositions
- Slots within Blocks
- States and Variants

A Recipe may define layout, morphology, appearance, typography roles, image treatment, responsive behavior, and state overrides.

Recipes should be declarative data where practical. Theme-specific JSX branches are an anti-pattern.

## 3.4 Morphology

Morphology describes the structural visual organization of an interface independently from its decorative appearance.

Morphology may define:

- hierarchy
- topology
- density
- rhythm
- alignment
- symmetry
- enclosure
- continuity
- direction
- visual weight
- overlap
- fragmentation
- stacking
- grouping

This distinction allows two themes to use identical colors and still differ substantially because their spatial organization, enclosure, rhythm, and hierarchy differ.

## 3.5 Appearance

Appearance is the layered graphical construction of a resolved semantic object.

Appearance must support full and custom construction rather than only flat surface aliases.

An Appearance Recipe may contain:

```text
background layers
surface material
texture layers
pattern layers
edge layers
decoration layers
image treatment
mask
clip
bleed
overflow
blend modes
opacity
z-order
filtering
backdrop effects
```

### Backgrounds

Backgrounds are ordered layers. A container may combine color, gradients, textures, patterns, images, generated artwork, or custom assets.

Backgrounds must be available at Composition, Socket, Block, Slot, and Element levels when the active grammar permits them.

### Textures

Textures describe material character, such as paper fiber, grain, noise, canvas, metal, scratches, ink bleed, or scan artifacts.

### Patterns

Patterns describe intentional repeated graphical structure, such as halftone, screentone, crosshatch, grid, stripes, dots, waves, speedlines, or cultural geometric motifs.

Texture and pattern are separate concepts and may be layered independently.

### Edges

Edges are first-class layered structures rather than simple borders.

An edge layer may target all sides or any subset of top, right, bottom, and left. It may be solid, hairline, double, dashed, ink, brush, deckle, torn, technical, engraved, glowing, embossed, image-based, offset, partial, or custom.

Multiple edge layers may exist simultaneously.

### Decorations

Decorations are non-semantic graphical additions such as seals, brush marks, registration marks, ticks, flourishes, corner graphics, panel numbers, rivets, engraving, or custom illustrations.

Decorations must not create accessibility meaning by themselves.

### Bleed

A Recipe may intentionally allow background, media, edge, or decoration layers to extend beyond a nominal container boundary. Bleed behavior must be explicit and must not obscure required interaction or focus indicators.
# 4. Token System

SES uses a layered token architecture. Tokens provide values. Recipes decide where and how those values are used.

## 4.1 Token levels

```text
Primitive Tokens
      |
Semantic Tokens
      |
Role Tokens
      |
Recipe Tokens
      |
Resolved Tokens
```

## 4.2 Primitive tokens

Primitive tokens are raw values with no interface semantics.

Examples:

```text
color.violet.600
space.4
radius.16
font.outfit
duration.200
shadow.3
```

Semantic components should not consume primitive tokens directly except in low-level infrastructure.

## 4.3 Semantic tokens

Semantic tokens describe stable meaning:

```text
color.canvas
color.surface
color.text.primary
color.text.secondary
color.accent.interaction
color.status.success
color.status.warning
color.status.danger
```

## 4.4 Role tokens

Role tokens describe interface context:

```text
surface.page
surface.navigation
surface.card
surface.card.featured
edge.card
edge.input
edge.navigation
text.heading
text.card.title
space.section
space.card
space.control
```

## 4.5 Recipe tokens

Recipe tokens are aliases introduced for specific semantic targets:

```text
media-card.surface
media-card.edge
media-card.gap
media-card.media.aspect
button.primary.surface
button.primary.edge
button.primary.shape
```

These may be generated or resolved from the active Visual Language and Theme.

## 4.6 Resolved tokens

Resolved tokens are host-ready values emitted after the cascade is complete. In a web renderer they may become CSS custom properties. In another host they may become a typed style object or native resource table.

## 4.7 Assets

A Visual Language may provide an asset registry for:

- fonts
- icons
- textures
- patterns
- masks
- edge images
- background images
- ornaments
- custom illustrations
- SVG fragments
- shaders or filters where supported by the renderer

Recipes reference asset IDs rather than arbitrary file paths when portability matters.

## 4.8 Token rules

1. Components consume semantic or role aliases, not theme-specific raw values.
2. Tokens should not encode full component topology.
3. Recipes may derive aliases from primitives and semantic tokens.
4. Theme overrides must resolve deterministically.
5. Missing required token references are conformance failures.
6. Accessibility overrides have higher precedence than ordinary theme styling.
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
# 6. Runtime and Rendering

## 6.1 Resolver

The resolver is the technical center of SES.

Conceptually:

```ts
resolveExpression({
  language,
  theme,
  composition,
  socket,
  block,
  variant,
  slot,
  element,
  state,
  viewport,
  userStyleOptions,
  accessibility
})
```

The resolver produces a deterministic Resolved Expression containing tokens, layout, morphology, appearance, typography, image rules, motion, and host instructions.

## 6.2 Resolution order

Recommended cascade:

```text
Visual Language
      |
Theme
      |
User Style Options
      |
Composition Recipe
      |
Socket Recipe
      |
Block Recipe
      |
Variant Recipe
      |
Slot Recipe
      |
Element Recipe
      |
Semantic State
      |
Responsive State
      |
Accessibility Overrides
```

Later layers may alter expression. They may not rewrite semantic contracts.

## 6.3 Renderer

The renderer realizes the Resolved Expression in a host.

Possible hosts include:

- DOM + CSS
- React Native
- native desktop view trees
- game UI frameworks
- canvas or retained-mode 2D renderers

SES does not require DOM or CSS, though the web is a reference implementation target.

## 6.4 Web DOM contract

A web renderer should keep the semantic structure inspectable.

Example:

```html
<main
  data-composition="home"
  data-language="neo-edo"
  data-theme="vermilion"
>
  <section data-socket="trending" data-importance="primary">
    <article data-block="media-card" data-variant="featured">
      <div data-slot="media"></div>
      <div data-slot="title"></div>
      <div data-slot="meta"></div>
    </article>
  </section>
</main>
```

These attributes are inspection and styling hooks. Accessibility must continue to use correct native semantics and ARIA rather than relying on data attributes.

## 6.5 Compilation

Where possible, static portions of Visual Languages and Themes should be compiled ahead of runtime into:

- CSS variables
- classes
- style sheets
- lookup tables
- asset manifests
- recipe indexes

Runtime resolution should handle state, viewport, instance overrides, and dynamic content without recomputing the entire language.

## 6.6 Component implementation

Component is an implementation category, not an SES semantic level.

A React codebase may contain:

```text
components/elements
components/blocks
components/infrastructure
```

A component implementing an Element or Block should own semantic behavior, accessible structure, event handling, and stable data hooks. Visual Language conditionals should remain outside the component whenever they can be expressed through Recipes and tokens.
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
# 8. Protocol and Implementation Boundary

SES defines interface semantics and expression. It intentionally does not define a transport or synchronization protocol.

A separate protocol may define how SES definitions, instances, assets, state changes, or resolved expressions move between processes, repositories, tools, runtimes, or devices.

## 8.1 SES owns

- canonical semantic types
- Slot and Socket contracts
- Block and Composition definitions
- Visual Language structure
- Theme structure
- Recipe model
- Morphology model
- Appearance model
- token semantics
- asset references
- projection contracts
- resolver semantics
- conformance rules

## 8.2 A separate protocol may own

- serialization format
- transport
- remote references
- capability negotiation
- version negotiation
- patching and deltas
- persistence
- synchronization
- authoring messages
- asset delivery
- cache policy
- signatures
- authentication and authorization

## 8.3 IV implementation boundary

IV should be treated as a downstream implementation of SES, not the definition of SES.

The recommended relationship is:

```text
SES Specification
      |
SES Protocol
      |
IV Adapter / Runtime
      |
IV Components and Screens
```

The implementation may expose optimizations or host-specific extensions, but those extensions should be namespaced and must not silently redefine canonical SES semantics.

## 8.4 Versioning

Version independently:

```text
SES semantic schema
SES expression schema
SES protocol
Visual Languages
Themes
Renderer
IV implementation
```

Equal version numbers do not imply compatibility. Compatibility should be declared explicitly.
