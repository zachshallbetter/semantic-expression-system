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
