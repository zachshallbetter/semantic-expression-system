# 23. Authoring Boundaries

Status: SES-018

SES authoring remains coherent when each concern is written in its canonical layer. The same fact must not be duplicated across semantic definitions, Recipes, host components, and external protocols with competing authority.

## 23.1 Ownership matrix

| Authoring surface | Owns | Must not own |
|---|---|---|
| Element | atomic semantic role, interaction behavior, accessibility requirements, content requirements | Visual Language identity, topology, theme-specific styling |
| Slot | named content relationship, cardinality, accepted content, priority | coordinates, crop, fixed geometry, visual placement |
| Block | semantic composition, Slots, states, variants, operations, behavior, relationships | theme-specific branches, renderer markup, business transport |
| Socket | typed participation, accepted Blocks, multiplicity, importance, invariants, projection permissions | CSS grid area, pixel coordinates, renderer layout implementation |
| Composition | screen/page semantic organization, hierarchy, priority, participation | fixed pixels, host navigation implementation, transport |
| Projection Contract | preserve/transform/omit/introduce permissions, invariance, failures, required exposure | recipe values, business rules, external authorization |
| Visual Language | graphical grammar, morphology, appearance, typography, image treatment, motion character | semantic identity, operation identity, application data behavior |
| Theme | concrete Visual Language configuration, token overrides, selected Recipe overrides | replacement semantic tree, transport, product navigation |
| Recipe | declarative expression mapping for an existing target, state, variant, responsive context | arbitrary code, semantic branch, ungoverned side effect |
| Token registry | typed values and aliases with provenance | full topology, semantic identity, business behavior |
| Asset registry | stable resource identity, category, metadata, capability declaration | implicit execution, authority, semantic meaning by decoration |
| Resolver | deterministic combination into renderer-neutral output | rendering, loading, operation invocation, persistence |
| Host renderer | platform realization, loading, native accessibility mapping, operation wiring | canonical semantic redefinition, unreviewed behavior changes |
| External protocol/application | transport, persistence, synchronization, auth, business logic, product navigation | redefining SES invariants without an explicit adapter or change record |

## 23.2 Authoring routing rules

1. If a property must remain stable across Visual Languages, author it in the semantic model or Projection Contract.
2. If a property may differ between Visual Languages, author it in Visual Language, Theme, Recipe, Morphology, Appearance, Token, Asset, or Motion data.
3. If a property concerns movement of SES data or resolved expressions, author it in an external protocol.
4. If a property concerns business behavior, persistence, navigation, authorization, or synchronization, author it in the host application or protocol.
5. If a host needs an extension, namespace it and record its capability, provenance, and compatibility boundary.
6. Do not duplicate semantic identity in a renderer component, Theme name, Asset ID, or language-specific variant.

## 23.3 Conflict handling

When two authoring surfaces claim the same field:

- canonical semantic definitions and Projection Contracts govern semantic authority;
- expression layers govern only permitted presentation fields;
- host implementations cannot override canonical output fields;
- external protocols cannot redefine SES meaning by serialization or transport shape;
- unresolved authority is recorded as a conflict, not silently merged.

## 23.4 Scope boundary

SES-018 routes authoring responsibility and authority. It does not reorganize a codebase, choose a repository layout, define a transport schema, or prohibit application concerns outside SES scope.
