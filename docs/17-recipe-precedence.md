# 17. Recipe Precedence and Conflict Handling

Status: SES-011

Recipe resolution combines expression layers without allowing a later expression source to rewrite semantic meaning. Precedence is deterministic, field-specific, and observable in the resolved layer trace.

## 17.1 Precedence order

Layers are applied from lowest to highest precedence:

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

The order is fixed for a resolution run. A missing layer is skipped; its absence is not an error unless the Projection Contract marks the layer or field required.

## 17.2 Merge rules

| Value shape | Default merge rule | Conflict behavior |
|---|---|---|
| Scalar expression value | replace at the highest permitted layer | protected or undeclared replacement fails |
| Token alias | replace alias, then resolve | cycle, ambiguity, or protected override fails |
| Object/map | recursively merge declared expression fields | same-precedence incompatible values fail |
| Ordered layer array | append only when the field declares additive semantics | otherwise highest permitted layer replaces the collection |
| Slot presentation map | merge by Slot ID | unknown Slot target fails |
| State/Variant map | merge by declared State or Variant ID | unknown ID fails |
| Protected semantic field | never merge or replace | hard failure |

The default is replacement for scalar fields and replacement for ordered collections unless a field explicitly declares additive semantics. Recipe precedence does not imply that all appearance arrays concatenate.

## 17.3 Protected fields

No Recipe layer may change:

- Element, Block, Slot, Socket, Composition, State, Variant, or Operation identity;
- required content or accepted content type;
- semantic role or accessibility relationship;
- required operation identity or business behavior;
- Projection Contract invariance level;
- routing intent or application data identity.

Such changes are `ERR_PROTECTED_FIELD_OVERRIDE`, even when supplied by an explicit user style option or accessibility override. Accessibility overrides may change expression needed to preserve access; they may not erase the underlying semantic contract.

## 17.4 Conflict policy

1. Resolve layers in the fixed order.
2. Check Projection Contract permission before applying a mutation.
3. Apply the field-specific merge rule.
4. Record source layer, source path, previous value, and resulting value in the layer trace.
5. If two values at the same precedence cannot be merged deterministically, fail with `ERR_RECIPE_CONFLICT`.
6. If a later value targets a protected field, fail with `ERR_PROTECTED_FIELD_OVERRIDE`.
7. If a mutation is not declared by `transform`, `mayOmit`, or `mayIntroduce`, fail with `ERR_TRANSFORM_UNDECLARED` or the applicable projection failure.

No fallback winner is selected for an unresolved conflict. Unknown or ambiguous fields are hard failures rather than silent defaults.

## 17.5 Trace requirements

The resolved expression trace retains, for every changed field:

- semantic target identity;
- field path;
- source layer and Recipe identity;
- prior value, if any;
- resulting value;
- Projection Contract permission;
- merge rule;
- check and evidence identifiers.

This trace supports deterministic replay, conformance evidence, and later change review.

## 17.6 Failure codes

- `ERR_RECIPE_CONFLICT`: incompatible values exist at one precedence level.
- `ERR_PROTECTED_FIELD_OVERRIDE`: a Recipe attempts to mutate semantic or behavioral authority.
- `ERR_TRANSFORM_UNDECLARED`: expression mutation lacks Projection Contract permission.
- `ERR_RECIPE_TARGET_UNKNOWN`: Recipe target cannot be resolved.
- `ERR_RECIPE_LAYER_INVALID`: layer is malformed or not applicable to the target.
- `ERR_RECIPE_MERGE_INVALID`: field value cannot be combined under its declared merge rule.

## 17.7 Scope boundary

SES-011 defines precedence and conflict semantics. It does not implement the resolver, define host styling, or authorize application-specific overrides of semantic authority.
