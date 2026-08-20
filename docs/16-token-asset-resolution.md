# 16. Token and Asset Resolution Rules

Status: SES-010

Tokens provide values and Assets provide referenced resources. Resolution is deterministic, typed by category, and separate from host loading or execution.

## 16.1 Token layers and precedence

Token lookup follows this order from broadest to most specific:

```text
primitive -> semantic -> role -> recipe -> explicit expression override -> resolved value
```

An alias resolves recursively through earlier layers only. A later layer may override a value when the target is expression data and the override is declared by the active Theme, Recipe, or explicit expression context. A token may not override semantic identity, operation identity, accessibility relationships, required content, or business behavior.

The final resolved value records its source layer and alias path. Cycles, ambiguous aliases, and undeclared protected-field overrides are failures.

## 16.2 Token rules

- Primitive tokens are raw values without semantic meaning.
- Semantic tokens represent stable interface meaning such as text, surface, status, and interaction.
- Role tokens represent contextual use such as card surface, heading text, or navigation edge.
- Recipe tokens are target-specific aliases and may express visual topology or appearance values.
- Resolved tokens are host-ready values and retain source provenance.
- Components should consume semantic or role aliases rather than Visual Language-specific primitives.
- Missing required tokens fail resolution; optional tokens may use an explicitly declared fallback.
- Fallbacks are not created implicitly for unknown tokens.

## 16.3 Asset categories

Asset IDs resolve within one declared category:

| Category | Examples | Expression use |
|---|---|---|
| fonts | font families and weights | typography |
| icons | symbolic action or status graphics | signaling and ornament |
| images | content or background imagery | media and surfaces |
| textures | paper, grain, material | layered appearance |
| patterns | halftone, grid, motifs | repeated appearance |
| masks | clipping and compositing shapes | appearance construction |
| edges | targeted edge resources | boundary treatment |
| backgrounds | image or generated surface sources | appearance construction |
| ornaments | non-semantic decoration | presentation only |
| custom | host-declared extensions | namespaced expression only |

An asset referenced as one category may not silently resolve from another category. Category aliases require an explicit registry declaration.

## 16.4 Asset rules

- Recipes reference stable Asset IDs, not implicit filesystem discovery.
- The resolver validates identity, category, required metadata, and declared capability before emitting a reference.
- Asset retrieval, decoding, licensing checks, caching, and host capability checks occur outside the pure resolver boundary.
- Missing required assets fail resolution with source path and category evidence.
- Optional decorative assets may be omitted only when the Projection Contract permits omission.
- Custom assets and filters must be namespaced and cannot introduce semantic identity or executable behavior by convention.

## 16.5 Failure codes

- `ERR_TOKEN_UNRESOLVED`: required token or alias has no definition.
- `ERR_TOKEN_CYCLE`: token aliases form a cycle.
- `ERR_TOKEN_AMBIGUOUS`: multiple definitions claim the same precedence position.
- `ERR_PROTECTED_TOKEN_OVERRIDE`: token resolution attempts to mutate a protected semantic field.
- `ERR_ASSET_NOT_FOUND`: required Asset ID is absent.
- `ERR_ASSET_CATEGORY_MISMATCH`: Asset ID exists only under another category.
- `ERR_ASSET_METADATA_INVALID`: required asset metadata is absent or malformed.
- `ERR_ASSET_CAPABILITY_UNSUPPORTED`: host capability is insufficient for the declared asset use.

Each failure retains the target identity, field path, requested token or Asset ID, category, source layer, and applicable SES-003 check ID.

## 16.6 Scope boundary

SES-010 defines token and Asset resolution semantics only. SES-011 owns full Recipe precedence and conflict handling. This contract does not load files, decode media, execute filters, or implement a host resource provider.
