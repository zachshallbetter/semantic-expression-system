# 19. Renderer-Neutral Output Contract

Status: SES-014

The renderer-neutral output is the boundary product of SES resolution and the input contract for a host renderer. It preserves semantic inspection and required behavior while carrying expression instructions without assuming DOM, CSS, native views, canvas, or a specific framework.

## 19.1 Output sections

Every resolved projection exposes these sections:

```text
identity
semantic
projection
expression
resources
interaction
accessibility
responsive
trace
diagnostics
```

### Identity and semantic

- Composition, Socket, Block, Slot, Element, Variant, and State IDs;
- semantic roles and stable data identities;
- content participation and required/optional status;
- operation identities and required exposure;
- semantic relationships and logical order.

### Projection

- Projection Contract identity and invariance profile;
- preserved, transformed, omitted, and introduced properties;
- applied failure conditions and permitted mutations.

### Expression

- resolved morphology and layout instructions;
- appearance layer instructions;
- typography and image treatment;
- resolved token values or typed token references;
- resolved Asset IDs and category metadata;
- state, variant, and responsive expression decisions;
- motion instructions with reduced-motion alternatives.

### Interaction and accessibility

- operation exposure and signaling metadata;
- enabled/disabled state;
- accessible name, role, relationships, and logical order;
- focus and state-visibility requirements;
- keyboard and reduced-motion obligations.

### Responsive

- active viewport/context;
- applicable responsive rules;
- allowed reorder, collapse, hide, overflow, and reachability behavior;
- required-content and required-operation obligations.

### Trace and diagnostics

- Recipe layer trace;
- token and Asset provenance;
- conformance check references;
- warnings, limitations, and typed failures.

## 19.2 Host neutrality rules

- No output field requires a DOM node, CSS property, React component, native class, canvas primitive, or framework lifecycle.
- Host adapters may map output fields to platform primitives but may not change semantic identity or required operations.
- Host-specific extensions are namespaced and must be declared in the adapter contract.
- Data attributes, ARIA, CSS classes, native accessibility APIs, and event handlers are host realization concerns, not canonical output fields.
- Resource loading and operation invocation remain outside the output contract.

## 19.3 Required invariants

- `OUTPUT-001`: every output semantic identity maps to exactly one source semantic identity.
- `OUTPUT-002`: required content and operation exposure metadata are present.
- `OUTPUT-003`: expression fields are separate from semantic fields.
- `OUTPUT-004`: every resolved token, Asset, and Recipe mutation has provenance.
- `OUTPUT-005`: accessibility and responsive obligations are present even when the host cannot yet realize them.
- `OUTPUT-006`: output is deterministic for the same resolver input.
- `OUTPUT-007`: host extensions cannot overwrite canonical fields.

## 19.4 Failure conditions

- `ERR_OUTPUT_IDENTITY_MISSING`
- `ERR_OUTPUT_REQUIRED_METADATA_MISSING`
- `ERR_OUTPUT_SEMANTIC_EXPRESSION_MIXED`
- `ERR_OUTPUT_PROVENANCE_MISSING`
- `ERR_OUTPUT_ACCESSIBILITY_METADATA_MISSING`
- `ERR_OUTPUT_HOST_EXTENSION_COLLISION`
- `ERR_OUTPUT_UNRESOLVED_RESOURCE`

## 19.5 Scope boundary

SES-014 defines the renderer-neutral output contract only. It does not define a renderer, host adapter, DOM structure, CSS vocabulary, native widget mapping, resource loader, or operation runtime.
