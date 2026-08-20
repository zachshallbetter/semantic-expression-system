# 24. Protocol-Neutral Adoption Guidance

Status: SES-020

SES is consumed as a semantic interface representation and governed expression system. An application may use SES without making SES responsible for transport, persistence, synchronization, or product navigation.

## 24.1 Integration boundary

```text
application data and intent
        |
        v
host adapter: map application state to SES semantic input
        |
        v
SES resolver: validate and resolve semantic + expression inputs
        |
        v
renderer adapter: realize renderer-neutral output
        |
        v
host events and operation results
```

The host owns application state, authorization, transport, persistence, synchronization, and navigation. SES owns semantic structure, projection permissions, expression resolution, conformance rules, and renderer-neutral output.

## 24.2 Consumption steps

1. Define or select the SES semantic model: Elements, Slots, Blocks, Sockets, Compositions, Variants, States, and Operations.
2. Declare the Projection Contract, including preserved identities, permitted transformations, omission and introduction rules, constraints, required operations, and failure conditions.
3. Supply content and application state through a host-owned adapter. The adapter maps into SES inputs; it does not move business rules into Recipes or Visual Languages.
4. Select a Visual Language and resolve Theme, Recipe, Morphology, Appearance, Tokens, Assets, Motion, and responsive context through the deterministic resolver boundary.
5. Validate the resolved output and consume it through a renderer adapter for DOM/CSS, native views, or another host platform.
6. Route user operations back to the host through stable operation identity. The host decides authorization, side effects, persistence, and result handling.

## 24.3 Explicit non-responsibilities

| Concern | Owner | SES boundary |
|---|---|---|
| transport and API calls | host application or external protocol | provide data and receive operation outcomes through an adapter |
| persistence and database state | host application | do not store application records or become a system of record |
| synchronization and conflict resolution | host application or external protocol | resolve only the supplied semantic/expression inputs |
| authentication and authorization | host application or external protocol | expose required operation identity; do not infer authority from presentation |
| product navigation | host application | express composition and operation meaning without owning routes |
| rendering | platform renderer adapter | consume renderer-neutral output without redefining semantic meaning |

## 24.4 Adapter rules

- Keep the adapter boundary explicit and versioned.
- Map legacy or application-specific data once at the boundary; downstream SES records use canonical vocabulary.
- Treat unknown semantic discriminators, unsupported capabilities, missing required content, and projection violations as failures.
- Do not branch semantic or business behavior on Visual Language, Theme, Recipe, or renderer identity.
- Keep external protocol payloads separate from canonical SES definitions unless an explicit mapping is recorded.
- Preserve stable semantic and operation identities across all expressions and host renderers.
- Let the host handle retries, idempotency, authorization, and side effects; SES resolution remains pure and local.

## 24.5 Minimal host contract

An adopting application needs only these responsibilities:

| Host responsibility | Required input/output |
|---|---|
| input mapping | application state and intent -> SES semantic input |
| expression selection | approved Visual Language, Theme, Recipe, and context |
| resolution invocation | canonical semantic and expression inputs -> renderer-neutral output |
| rendering | renderer-neutral output -> platform interface |
| operation routing | stable operation identity + host event -> application result |
| lifecycle | validation, logging, retries, persistence, and authorization outside SES |

Adoption is therefore an integration choice, not a transfer of application ownership to SES. A host may adopt only the semantic model, only the resolver contract, or the complete semantic-to-renderer path, provided the declared boundaries and invariants remain intact.

## 24.6 Acceptance boundary

SES-020 is documentation-complete when an adopter can identify the host adapter, resolver, renderer adapter, and operation route; assign transport, persistence, synchronization, authorization, and navigation to the host; and preserve SES semantic identity and projection invariants while changing expression systems.
