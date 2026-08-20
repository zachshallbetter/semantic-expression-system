# 20. Change Governance

Status: SES-015

SES changes are governed by explicit scope, compatibility evidence, conformance impact, and documented authority. A change is not complete merely because a file or schema parses.

## 20.1 Version boundaries

Version independently:

- semantic model and semantic schema;
- expression model and expression schema;
- Projection Contract vocabulary;
- conformance and result schemas;
- resolver and renderer-neutral output contracts;
- Visual Languages and Themes;
- host renderers and downstream implementations;
- transport or synchronization protocols outside SES.

Equal version numbers do not imply compatibility. Each release or draft records which boundaries changed.

## 20.2 Change classes

| Class | Examples | Required review |
|---|---|---|
| Documentation | terminology clarification, examples, non-normative prose | source and vocabulary consistency |
| Additive | new optional field, new expression layer, new fixture | schema compatibility and conformance impact |
| Conformance-tightening | new required check, failure condition, invariant | fixture coverage, migration path, authority review |
| Breaking semantic | identity, Slot, Socket, Operation, state, or required-content change | explicit semantic version change and equivalence review |
| Breaking expression | incompatible output or Recipe contract change | output compatibility and host impact review |
| Deprecation | retiring field, layer, asset category, or rule | replacement, timeline, warning, and removal release |

## 20.3 Required change record

Every normative change records:

- change ID and affected version boundary;
- intent and reason;
- established behavior before the change;
- proposed behavior after the change;
- compatibility class;
- affected schemas, fixtures, validators, resolvers, and host adapters;
- conformance and migration impact;
- evidence and limitations;
- authority and disposition.

## 20.4 Conformance-impact review

Before accepting a normative change, review:

1. SES-001 invariant matrix and affected baseline IDs;
2. positive and negative fixtures;
3. result schema and failure codes;
4. projection-equivalence vectors;
5. responsive and accessibility contracts;
6. resolver and renderer-neutral output contracts;
7. downstream implementation boundary;
8. changelog and deprecation records.

Changes that alter required semantic or behavioral invariants require updated evidence from every affected dependent layer. Missing evidence yields `inconclusive`, not pass.

## 20.5 Deprecation

Deprecation records the deprecated identifier, replacement, first deprecated version, planned removal version or condition, compatibility behavior, and migration evidence. Deprecated semantic identities remain resolvable during the declared compatibility window unless a breaking change is explicitly authorized.

Silent aliases, undocumented removals, and fallback behavior that changes semantic meaning are prohibited.

## 20.6 Changelog requirements

`docs/CHANGELOG.md` records normative changes by version or draft revision. Each entry identifies semantic, expression, schema, conformance, resolver, or implementation-boundary impact. Generated artifacts and local evidence reference the change ID rather than becoming the changelog source of truth.

## 20.7 Scope boundary

SES-015 defines governance and review obligations. It does not assign external release authority, publish packages, modify downstream implementations, or choose a versioning tool.
