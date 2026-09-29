# First Agent Cycle

Operate Semantic Expression System under the pinned IEPE reference in `.iepe/protocol-reference.json` and the local contract in `AGENTS.md`.

Begin with read-only reconciliation. Verify the protocol pin, local profile, authority chain, repository state, work graph, dependencies, evaluators, protected actions, and evidence gaps. Do not implement, claim, create or change work items, push, merge, deploy, publish, spend, or communicate externally during this first cycle unless the user explicitly expands authority.

Return a typed reconciliation result, the material unknowns, and the first candidate Ready issue. If initialization gates are incomplete, stop with the exact authority or evidence needed to continue.
