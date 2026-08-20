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
