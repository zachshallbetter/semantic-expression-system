# 18. Semantic Branch Prohibition

Status: SES-012

An implementation must not create Visual Language-specific semantic or business-logic branches. One semantic definition must remain the source for all conforming expressions.

## 18.1 Prohibited branches

The following patterns are non-conforming:

- branching a Block, Slot, Socket, Composition, Operation, or State identity by Visual Language name;
- changing required content, accepted content, operation identity, routing intent, or business behavior by Theme or Recipe;
- maintaining separate language-specific semantic trees that duplicate application logic;
- using decorative variants such as `westernButton`, `edoCard`, or `cyberBadge` as semantic identities;
- hiding or replacing required operations because a Visual Language does not provide a preferred visual treatment;
- embedding Visual Language conditionals in semantic Element or Block behavior when the difference belongs in expression data.

## 18.2 Allowed variation

Expression branches are allowed when they are declarative, target an existing semantic identity, and are governed by a Projection Contract. Permitted variation includes:

- layout topology and morphology;
- typography and token selection;
- media placement and image treatment;
- backgrounds, textures, patterns, edges, masks, bleed, and ornament;
- density, enclosure, alignment, overlap, and responsive arrangement;
- state and operation signaling while preserving exposure and meaning;
- host-specific realization after the renderer-neutral expression boundary.

An expression branch must not add new semantic identity or implicit business behavior. Host extensions are namespaced and remain downstream of canonical SES semantics.

## 18.3 Review checks

- `BRANCH-001`: every semantic target is defined once in the canonical registry.
- `BRANCH-002`: Visual Language and Theme identifiers appear only in expression selection or presentation data.
- `BRANCH-003`: required operations and routing intent are independent of expression selection.
- `BRANCH-004`: language-specific differences are represented by Recipes, tokens, assets, morphology, or appearance.
- `BRANCH-005`: all cross-language vectors use the same semantic fixture and invariant set.
- `BRANCH-006`: host-specific extensions do not redefine canonical semantic fields.

## 18.4 Failure conditions

- `ERR_SEMANTIC_LANGUAGE_BRANCH`: semantic structure changes by Visual Language or Theme.
- `ERR_BUSINESS_LANGUAGE_BRANCH`: business behavior or routing changes by expression selection.
- `ERR_DUPLICATE_SEMANTIC_TREE`: equivalent semantic definitions are forked per language.
- `ERR_OPERATION_LANGUAGE_BRANCH`: required operation identity or exposure depends on language selection.
- `ERR_UNNAMESPACED_HOST_EXTENSION`: host-specific extension enters canonical SES fields without a namespace.

## 18.5 Scope boundary

SES-012 governs architectural review and conformance checks. It does not refactor an implementation, prescribe a programming language, or prohibit legitimate application-level differences that are outside SES expression selection.
