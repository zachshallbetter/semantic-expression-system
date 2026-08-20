# 21. Security and Trust Boundaries

Status: SES-016

SES expression data may control presentation, but it must not silently become executable code, an authority channel, or a path around host security policy. The host decides how untrusted input is loaded, sanitized, sandboxed, and executed.

## 21.1 Trust classes

| Class | Examples | Default treatment |
|---|---|---|
| Declarative data | tokens, layout values, morphology, colors, typography roles, asset IDs | schema validation and bounded resolution |
| Referenced resources | images, fonts, icons, textures, patterns, masks, edge assets | category validation, metadata validation, host policy |
| Constrained custom expression | namespaced custom appearance or host extension | explicit capability declaration, allowlist, isolation, and provenance |
| Executable behavior | scripts, arbitrary code, event handlers, shader code, dynamic imports | outside canonical SES; rejected unless a separately governed host protocol authorizes it |
| Authority-bearing input | navigation target, credential, permission, payment, deployment, persistence command | outside SES expression; never inferred from a Recipe or Asset |

## 21.2 Expression safety rules

- Tokens and Recipes are data, not code.
- Asset IDs resolve through declared registries; arbitrary filesystem or network discovery is not implied.
- Custom sources, filters, blend modes, shaders, and SVG fragments are namespaced and capability-gated by the host.
- A Recipe cannot introduce event handlers, navigation, data mutation, authentication, authorization, persistence, or network requests.
- An Asset cannot create semantic identity, operation identity, accessibility meaning, or business behavior by appearance alone.
- Host adapters validate MIME type, size, dimensions, decoding policy, and supported capabilities before use.
- Remote or user-supplied resources require an external trust and delivery policy; SES records references, not trust.
- Failure is closed: unknown custom types, unsupported capabilities, unsafe references, and malformed metadata fail rather than falling back to execution.

## 21.3 Resource constraints

Hosts define bounded limits for:

- payload size and nesting depth;
- image pixels, animation frames, font tables, and decoded memory;
- filter, mask, blend, and layer complexity;
- custom extension execution time and permissions;
- remote fetch count, origin, protocol, redirect, and timeout policy;
- logging and diagnostic redaction.

SES conformance verifies that a declaration is explicit and typed. Host security policy determines whether the declaration is permitted in a particular environment.

## 21.4 Trust and provenance

Every custom expression, Asset, filter, or host extension retains:

- source identity and category;
- declaring Visual Language, Theme, Recipe, or adapter;
- capability required;
- integrity or version reference when supplied by the host;
- validation and limitation records.

The resolver must not manufacture trust, signatures, authorization, or provenance. Those belong to the delivery or host protocol.

## 21.5 Failure codes

- `ERR_UNTRUSTED_EXECUTABLE_EXPRESSION`
- `ERR_CUSTOM_CAPABILITY_UNDECLARED`
- `ERR_RESOURCE_POLICY_REJECTED`
- `ERR_RESOURCE_METADATA_LIMIT`
- `ERR_RESOURCE_ORIGIN_REJECTED`
- `ERR_HOST_EXTENSION_UNAUTHORIZED`
- `ERR_AUTHORITY_BEHAVIOR_IN_EXPRESSION`
- `ERR_ASSET_DECODE_REJECTED`

## 21.6 Scope boundary

SES-016 defines expression trust boundaries and host obligations. It does not implement sanitization, sandboxing, content security policy, authentication, authorization, remote delivery, signing, or a security adapter.
