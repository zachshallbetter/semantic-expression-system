# Agent and Contributor Operating Contract

This repository holds the Semantic Expression System (SES) specification, schemas, types, and conformance corpus.
This contract applies to human and AI contributors alike. It restates rules that live elsewhere in the repository and
adds none: where it and a source it cites disagree, the source wins.

## Authority order

Resolve conflicts in the order [`PROJECT_PROFILE.json`](PROJECT_PROFILE.json) declares:

1. [`INTENT.md`](INTENT.md)
2. [`docs/EXPERIENCE.md`](docs/EXPERIENCE.md)
3. [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
4. [`PROJECT_PROFILE.json`](PROJECT_PROFILE.json)
5. This file

The numbered specification chapters in [`docs/`](docs) and the schemas in [`docs/schemas/`](docs/schemas) are the
normative text. Generated context (`.agents/llms*.txt`) is a projection of them and is never authoritative.

## Intent and Evidence Project Engine

This project operates under `IEPE-001` from the source and immutable revision recorded in `.iepe/protocol-reference.json`.

Intent governs implementation. Canonical documentation defines authority. Issues authorize committed work. The project graph owns live status and native dependencies. The coordinator claims ready work, assembles bounded context, dispatches worker agents, and routes results through evaluation. Agents may explore within their granted environment but may not promote, publish, deploy, spend, communicate externally, or alter authoritative state without explicit authority.

Preserve traceability:

`intent -> epic -> issue -> artifact -> evidence -> qualification -> promotion`

Continue while authority, context, ownership, dependencies, permissions, and evidence remain valid. Stop at unverified boundaries.

## Work

- Issues live in [`work/`](work) (`SES-nnn.md`) and the graph in [`work/GRAPH.md`](work/GRAPH.md). A committed change
  traces to an issue.
- Evidence for an issue is recorded in [`evidence/`](evidence). Negative results go in
  [`docs/NEGATIVE_RESULTS.md`](docs/NEGATIVE_RESULTS.md); they are kept, not removed.
- Normative changes follow [`docs/20-change-governance.md`](docs/20-change-governance.md): change the specification
  and the schemas together, and record the change in [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

## Checks

Run every tool in [`tools/`](tools) before opening a pull request, with the loop in the README's
[Verification](README.md#verification) section. CI runs the same loop. These are structural and conformance checks,
not an empirical evaluation.

## Claims

Keep the four states apart: documented, implemented, tested, empirically validated. Do not state or imply
conformance, an implementation, or an external review that the evidence in this repository does not show. The
current limits are in the README's [Status and limitations](README.md#status-and-limitations) section and
[`docs/25-accountability-and-readiness.md`](docs/25-accountability-and-readiness.md).

## Commits and pull requests

Follow [`CONTRIBUTING.md`](CONTRIBUTING.md): short descriptive commit titles with an optional prefix or issue
identifier, no AI assistant co-author trailers, and pull requests merged by the maintainer.

## Stop conditions

Stop, and hand the decision to the maintainer, before any of the protected actions
[`PROJECT_PROFILE.json`](PROJECT_PROFILE.json) lists:

- external publication
- production deployment
- spending
- a destructive migration
- a credential or IAM change
- a change to authoritative intent ([`INTENT.md`](INTENT.md))
- external communication

Stop as well when:

- the work has no issue, or the issue lacks acceptance criteria or evidence requirements;
- a check in [`tools/`](tools) fails and the fix would change normative text, a schema, or a fixture's expected
  result;
- a change would raise a status claim (for example from tested to empirically validated) or cut a release;
- authority, context, ownership, dependencies, permissions, or evidence can no longer be verified.

Report what was done, what was not, and the decision that is waiting. Do not work around a stop condition.
