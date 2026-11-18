# Security Policy

## Reporting a vulnerability

Report it privately through GitHub: [report a vulnerability](https://github.com/zachshallbetter/semantic-expression-system/security/advisories/new).
Please don't open a public issue, pull request or discussion for it. Include the affected document, schema or tool,
the version, and steps to reproduce.

This project has a solo maintainer. Reports are handled on a best-effort basis, with no response-time guarantee (no SLA).

## Scope

This repository is a specification, its JSON and TypeScript schemas and a conformance corpus with validation tools. It
runs no service and handles no user data. The tools in `tools/` are local scripts that read fixtures in this
repository.

In scope:

- A flaw in the specification or schemas that lets expression data become executable code, an authority channel or a
  path around host security policy, against the rules in
  [`docs/21-security-trust-boundaries.md`](docs/21-security-trust-boundaries.md).
- A validator or resolver in `tools/` that accepts a fixture the specification says must fail, in a way that weakens
  those rules.
- A vulnerability in a script in `tools/` or `scripts/`, such as unsafe handling of a crafted fixture.
- Secrets or personal data committed to the repository.

Whether a declaration is permitted in a particular environment is decided by the host's security policy; the
specification does not set it.

## Supported versions

The latest tagged release. Update to it before reporting.
