# 12. Canonical Vocabulary

Status: SES-005

These terms are normative across the SES specification, schemas, fixtures, validator contract, and resolver boundary. Implementations may use local aliases internally, but public artifacts should use the canonical terms.

| Term | Canonical meaning | Not synonymous with |
|---|---|---|
| Semantic identity | The stable identity of an interface meaning, including its declared Element, Block, Slot, Socket, Composition, State, Variant, or Operation identity | CSS selector, DOM node, component class, visual label |
| Semantic model | The definitions of what exists, what content participates, what behavior and relationships are stable, and what operations are available | Application business logic, renderer tree |
| Expression model | The replaceable graphical realization of semantic structure through Visual Languages, Themes, Recipes, Morphology, Appearance, Tokens, Assets, and Motion | Semantic meaning, business behavior |
| Visual Language | A coherent graphical grammar governing presentation, topology, typography, surface, imagery, iconography, and motion | Theme, palette, brand guide |
| Theme | A concrete configuration of a Visual Language, usually through token and selected Recipe overrides | Complete Visual Language replacement |
| Recipe | Declarative expression instructions for a semantic target, state, variant, responsive condition, or layer | Semantic component definition, arbitrary renderer branch |
| Morphology | The spatial and structural organization of expression, including topology, direction, density, hierarchy, enclosure, overlap, and rhythm | Decorative surface treatment |
| Appearance | Layered graphical construction, including backgrounds, textures, patterns, edges, masks, clips, bleed, blending, and decoration | Semantic state or accessibility meaning |
| Projection | One expression of a semantic target under a selected Visual Language, Theme, Recipe set, context, and Projection Contract | Permanent mutation of the semantic model |
| Projection Contract | The explicit boundary declaring what a projection preserves, transforms, omits, introduces, constrains, and rejects | Renderer configuration alone |
| Preserve | A property that must remain semantically equivalent across projection | Same pixels or same DOM arrangement |
| Transform | A declared presentation mutation permitted by the Projection Contract | Permission to change semantic identity or behavior |
| Omit | Removal of optional content or presentation explicitly permitted by `mayOmit` | Silent removal of required content |
| Introduce | Addition of presentation-only content explicitly permitted by `mayIntroduce` | Creation of new semantic meaning or operation |
| Operation identity | The stable identity of an action the interface exposes | Its icon, label, position, or invocation result |
| Operation exposure | The condition that a required operation is reachable through the projected interface | Operation existence, signaling, invocation, or success |
| Conformance | Evidence that a semantic/expression result satisfies its declared schema, invariants, Projection Contract, and failure conditions | Visual similarity or artifact existence |
| Validation | An evaluation performed against a declared check or rule | Qualification or promotion by itself |
| Failure condition | A declared condition that invalidates a projection or result | A warning or stylistic preference |
| Invariance profile | The configured requirement level for a conformance dimension: `required`, `bounded`, or `free` | A fixed visual layout |
| Required | The property must be preserved or satisfied | Merely recommended |
| Bounded | The property may vary only within declared limits | Unconstrained variation |
| Free | The property may vary without a fixed topology constraint, subject to other required invariants | Permission to change semantics or behavior |

## 12.1 Usage rules

1. Use **semantic identity** when referring to stable meaning across representations.
2. Use **operation exposure** when referring specifically to reachability of a required action; use operation identity, signaling, invocation, and outcome for the other lifecycle states.
3. Use **projection** for the result of expressing semantics, and **Projection Contract** for the rules governing that result.
4. Use **Morphology** for spatial organization and **Appearance** for layered graphical construction.
5. Use **conformance** for the governed result and **validation** for the check that produces evidence about it.
6. Use **Theme** only for configuration of a Visual Language; a substantially different graphical grammar is a separate Visual Language.
7. Do not use visual-language names, theme names, renderer names, or product names as semantic identities or variants.

## 12.2 Canonical distinction

```text
semantic identity
  -> semantic model
  -> Projection Contract
  -> projection
  -> expression model
  -> renderer-neutral resolved expression
  -> host realization
```

The semantic identity remains stable while expression may vary radically. Conformance concerns whether the governed meaning and required behavior survive that variation.

## 12.3 Scope boundary

SES-005 normalizes terminology only. It does not rename existing IDs, change schemas, implement aliases, or alter semantic or expression behavior.
