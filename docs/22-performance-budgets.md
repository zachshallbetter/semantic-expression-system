# 22. Performance Budgets

Status: SES-017

SES performance budgets bound expression resolution and host handoff without turning the protocol into a renderer-specific benchmark. These are provisional design budgets for a warm, local resolution path; implementations must record actual measurements before claiming qualification.

## 22.1 Baseline budgets

| Surface | Budget | Measurement boundary |
|---|---:|---|
| Pure semantic/expression resolution | 5 ms p95 | resolver entry to renderer-neutral output, excluding resource I/O |
| Token and alias resolution | 1 ms p95 | token lookup and alias expansion, excluding network or disk |
| Asset metadata resolution | 2 ms p95 | registry lookup and metadata validation, excluding decode/fetch |
| Recipe layer count | 12 layers | one output target across the declared cascade |
| Recipe merge depth | 16 nested expression levels | one target resolution |
| Appearance layer count | 32 layers | one resolved target before host realization |
| Responsive recomputation | 8 ms p95 | existing resolved context to changed viewport output, excluding render/layout |
| Motion metadata resolution | 1 ms p95 | state-to-motion instruction selection, excluding playback |
| Renderer-neutral output size | 256 KiB typical target | serialized resolved output excluding external resources |

Budgets are guardrails, not evidence that an implementation meets them. A host may declare a different profile, but it must name the profile, record the rationale, and retain comparable measurements.

## 22.2 Required measurements

Implementations measuring SES performance record:

- semantic target and fixture ID;
- Visual Language, Theme, state, viewport, and accessibility context;
- cold/warm/cache state;
- input size and layer counts;
- p50, p95, and p99 latency where timing is applicable;
- output size and resource counts;
- retries, failures, and budget violations;
- host and runtime conditions;
- limitations and measurement method.

## 22.3 Degradation rules

- Exceeding a budget is a typed performance warning or failure according to the declared profile; it does not authorize semantic simplification.
- Required content, operations, accessibility, and responsive reachability may not be dropped to meet a budget.
- Optional decoration, redundant appearance layers, precomputation, caching, and compilation may be optimized when their Projection Contract permits it.
- Resource fetch or decode time is measured by the host/resource provider, not attributed to pure resolver latency.
- Budget changes are governed changes and require SES-015 review.

## 22.4 Failure codes

- `ERR_RESOLUTION_BUDGET_EXCEEDED`
- `ERR_TOKEN_LOOKUP_BUDGET_EXCEEDED`
- `ERR_ASSET_METADATA_BUDGET_EXCEEDED`
- `ERR_RECIPE_DEPTH_EXCEEDED`
- `ERR_APPEARANCE_LAYER_BUDGET_EXCEEDED`
- `ERR_RESPONSIVE_RECOMPUTE_BUDGET_EXCEEDED`
- `ERR_OUTPUT_SIZE_BUDGET_EXCEEDED`

## 22.5 Scope boundary

SES-017 establishes provisional measurement boundaries and budgets. It does not benchmark a runtime, prescribe hardware, optimize a renderer, or treat unmeasured performance as validated.
