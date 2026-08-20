# Semantic Expression System

Version: 1.0.0 Draft Standard
Status: Protocol-neutral architecture specification with locally qualified implementation candidate

The Semantic Expression System (SES) is a 2D interface architecture for extreme visual variation without semantic or behavioral fragmentation.

SES separates what an interface means from how it is expressed. Elements, Slots, Blocks, Sockets, Compositions, Variants, States, and Operations define the stable semantic interface representation. Visual Languages, Themes, Recipes, Morphology, Appearance, Tokens, and Assets define replaceable expression. A resolver combines both sides into a concrete rendered interface.

The system is intentionally protocol-neutral and application-neutral. A transport, synchronization, authoring, persistence, or remote rendering protocol can be defined separately. A project such as IV can implement SES without becoming the source of truth for SES itself.

## Governing principle

If a visual decision can reasonably differ between radically different interface languages, it must not be hard-coded into a semantic Element or Block.

Visual variation may include color, typography, geometry, spacing, internal layout, surface construction, background composition, targeted edges, textures, patterns, masks, image treatment, iconography, ornament, density, motion, and responsive presentation.

Semantic identity, data contracts, operation identity, accessibility relationships, required content, state meaning, and business behavior remain governed by the semantic model.

## Architecture

```text
APPLICATION DATA
      |
      v
SEMANTIC INTERFACE REPRESENTATION
  Element
  Slot
  Block
  Socket
  Composition
  Variant
  State
  Operation
      |
      v
PROJECTION CONTRACT
  preserve
  transform
  omit
  introduce
  invariants
  operation exposure
  failure conditions
      |
      v
EXPRESSION SYSTEM
  Visual Language
  Theme
  Recipe
  Morphology
  Appearance
  Tokens
  Assets
      |
      v
RESOLVER / COMPILER
      |
      v
RENDERER
  DOM
  CSS
  native view tree
  other 2D host
```

## Documents

- `01-definition.md` - canonical definition and terminology
- `02-semantic-model.md` - Element, Slot, Block, Socket, Composition, Variant, State, Operation
- `03-expression-model.md` - Visual Language, Theme, Recipe, Morphology, Appearance
- `04-token-system.md` - token layers, aliases, resolution, assets
- `05-projection-contract.md` - preservation and transformation boundary
- `06-runtime-and-rendering.md` - resolver, cascade, DOM contract, compilation
- `07-conformance.md` - validation levels, failure conditions, tests
- `08-implementation-boundary.md` - protocol and IV implementation boundary
- `schemas/ses-schema.ts` - TypeScript canonical schema
- `schemas/ses.schema.json` - JSON Schema interchange draft
- `examples/home-example.ts` - complete semantic and expression example

## Naming

SES is the umbrella architecture.

"Component" is an implementation term, not a semantic layer. A React component can implement an Element, Block, Socket renderer, Composition host, or infrastructure provider.

"Theme" is not the whole expression system. A Theme configures a Visual Language. The Visual Language defines the broader graphical grammar.

"Slot" and "Socket" are intentionally distinct. A Slot receives content inside a Block. A Socket receives compatible Blocks inside a larger semantic structure.
