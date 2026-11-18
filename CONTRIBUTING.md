# Contributing

## Scope

This repository holds the Semantic Expression System specification, schemas, types, and conformance corpus.

## Checks

Run the conformance tools in `tools/` before opening a pull request. CI runs each one on every pull request and on
pushes to `main`; the loop it uses is in the README's [Verification](README.md#verification) section. A tool that
needs fixture output is fed by `tools/resolve_reference_fixture.py`, as in that loop.

## Changes

- Prefer normative changes via the specification and schemas together.
- Keep status honesty: documented ≠ implemented ≠ tested ≠ empirically validated.
- Update `docs/CHANGELOG.md` for a change to the specification, schemas or release metadata.
- Commit titles are short and descriptive, with an optional prefix such as `docs:`, `feat:` or `ci:`, or an issue
  identifier such as `SES-041:`. Pull requests are merged by the maintainer.
- Do not add AI assistant co-author trailers to commits.

## Security

Report vulnerabilities privately, as [SECURITY.md](SECURITY.md) describes, not in a public issue.

## Citation

See [`CITATION.cff`](CITATION.cff).
