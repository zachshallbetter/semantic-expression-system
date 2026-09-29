# Semantic Expression System Agent Operating Contract

## IEPE authority

This project operates under `IEPE-001`, version `0.2.0`, from `https://github.com/zachshallbetter/IEPE` at immutable revision `56f82de8cca122cc4d347cdd55bb32bdcd31ed27`. The pin is recorded in `.iepe/protocol-reference.json`.

IEPE Core governs claim, context, dispatch, evidence, perturbation, promotion, memory, and stop semantics. Local canonical sources govern this project's intent, experience, architecture, work graph, evaluators, adapters, and protected actions. Local instructions may specialize IEPE but may not weaken its invariants.

Preserve this trace:

```text
intent -> epic -> issue -> claim -> context -> artifact -> evaluation -> evidence -> qualification -> promotion
```

## Authority order

1. `INTENT.md`
2. `docs/EXPERIENCE.md`
3. `docs/ARCHITECTURE.md`
4. `PROJECT_PROFILE.json`
5. Authorized issues and decisions
6. Implementation and operational observations
7. Generated agent context

Conversation and generated files are evidence inputs, not automatic authority.

## Operational loop

```text
reconcile -> select -> validate -> claim -> assemble bounded context -> dispatch -> observe -> evaluate -> stress test when required -> record evidence -> disposition -> release claim -> repeat
```

## Startup

1. Verify `.iepe/protocol-reference.json` and `PROJECT_PROFILE.json` against the pinned IEPE revision.
2. Inspect repository, documentation, work graph, claims, dependencies, tests, and evidence without mutation.
3. Reconcile contradictions and missing authority.
4. Select only a complete Ready issue.
5. Claim bounded scope, assemble minimal context, dispatch, evaluate, record, and release.

The first agent cycle is read-only reconciliation. Do not infer mutation authority from repository access.

## Status honesty

`Documented != Implemented != Tested != Empirically Validated`

Artifact existence, a passing API call, or completion language does not establish qualification.

## Process routing

Use the narrowest procedure under `.agents/skills/`: initialize, reconcile, operate, qualify, stress test, or maintain the package. These procedures are projections from the pinned IEPE revision and cannot expand local authority.

## Protected actions

Read `PROJECT_PROFILE.json`. Protected actions require its named promotion authority and issue-level authorization.

## Stop conditions

Stop and record a typed result when authority, ownership, context, dependencies, permissions, evidence, evaluator availability, provider health, or recovery becomes ambiguous. Stop when capacity or retry limits are exhausted. Silence is not approval.
