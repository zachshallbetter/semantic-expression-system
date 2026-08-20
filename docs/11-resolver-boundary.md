# 11. Resolver Boundary

Status: SES-004

The SES resolver is a pure boundary between stable semantic meaning and replaceable expression. It selects and combines expression data for one semantic projection. It does not render, execute operations, fetch resources, mutate state, or decide business behavior.

## 11.1 Pure contract

Conceptually:

```ts
resolveExpression(input: ResolutionInput): ResolvedExpression | ResolutionFailure
```

For the same canonical input, the resolver returns the same result. The input contains all context required for the decision; ambient time, randomness, network state, filesystem discovery, and mutable global state are not resolver inputs.

## 11.2 Inputs

`ResolutionInput` contains:

- semantic target: Composition, Socket, Block, Slot, Element, Variant, and State identities;
- semantic definition registry and instance content metadata;
- selected Visual Language and Theme definitions;
- applicable Recipe layers;
- token and Asset registries already available to the caller;
- viewport and responsive context;
- accessibility context, including high contrast and reduced motion;
- explicitly supplied user or instance expression options;
- Projection Contract governing the target.

The resolver receives registries as values or immutable references. Resource loading, asset fetching, authentication, and capability discovery occur outside this boundary.

## 11.3 Output

`ResolvedExpression` contains:

- unchanged semantic identity references for every projected target;
- resolved morphology and layout instructions;
- resolved appearance layers;
- resolved typography, image, icon, token, and asset references;
- state and responsive expression decisions;
- accessibility-preserving expression instructions;
- required operation exposure metadata;
- the applied Recipe layer trace;
- conformance warnings, if permitted by the caller's policy.

The output is renderer-neutral. It describes what the host must express, not how a DOM, native tree, canvas, or CSS engine performs that work.

## 11.4 Resolution cascade

The resolver evaluates layers in this fixed order:

```text
Visual Language
-> Theme
-> explicit user style options
-> Composition Recipe
-> Socket Recipe
-> Block Recipe
-> Variant Recipe
-> Slot Recipe
-> Element Recipe
-> semantic State Recipe
-> responsive Recipe
-> accessibility overrides
```

Later layers may replace expression fields only when the Projection Contract permits the mutation. They may not replace semantic identity, required content, operation identity, accessibility relationships, or business behavior.

Precedence and conflict-resolution details are reserved for SES-011. Until then, a conflicting required semantic field is a hard resolution failure rather than an implicit winner.

## 11.5 Invariants

- `RESOLVE-001`: semantic IDs in the output equal the IDs in the input semantic target.
- `RESOLVE-002`: required Slots, Sockets, content, and operations are not removed by expression resolution.
- `RESOLVE-003`: every output mutation is attributable to a declared recipe layer and Projection Contract permission.
- `RESOLVE-004`: all required token and asset references are resolved or returned as typed failures.
- `RESOLVE-005`: accessibility and responsive constraints remain represented in the output.
- `RESOLVE-006`: the same canonical input produces the same output and failure ordering.
- `RESOLVE-007`: resolution has no side effects and does not invoke renderer or operation behavior.

## 11.6 Failure model

Resolution returns a typed failure for:

- unknown semantic identity;
- incompatible Slot or Socket content;
- missing required Recipe;
- conflicting protected semantic field;
- undeclared projection mutation;
- unresolved required token or asset;
- invalid state or responsive expression;
- missing required accessibility or operation exposure instruction.

Failures include the target identity, source layer, field path, typed error code, and the applicable SES-003 check ID. Unknowns are not silently replaced with fallback expression.

## 11.7 Boundary ownership

| Concern | Resolver | Caller or host |
|---|---|---|
| Semantic identity preservation | owns validation | observes result |
| Recipe and token cascade | owns resolution | supplies immutable inputs |
| Asset retrieval | does not perform | asset provider |
| Operation invocation | does not perform | interaction runtime |
| DOM/native/canvas realization | does not perform | renderer |
| Business logic and navigation | does not perform | application |
| Persistence, transport, synchronization | does not perform | protocol or host application |

## 11.8 Scope boundary

SES-004 defines the pure resolver boundary and its invariants only. It does not implement a resolver, choose a renderer, define final recipe conflict precedence, or add application behavior.
