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
