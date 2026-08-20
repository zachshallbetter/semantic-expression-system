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
