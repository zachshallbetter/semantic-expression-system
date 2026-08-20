"""Framework-neutral SES host adapter example.

The adapter maps host state to SES inputs and returns resolved output. It does
not own transport, persistence, authorization, navigation, or rendering.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from ses_resolver import resolve_projection


def adapt_application_state(application_state: Mapping[str, Any]) -> dict[str, Any]:
    """Map host-owned state to explicit SES semantic and expression inputs."""
    return {
        "semantic": deepcopy(application_state["semantic"]),
        "expression": deepcopy(application_state["expression"]),
        "context": deepcopy(application_state.get("context", {})),
    }


def resolve_for_host(application_state: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve host input; the returned output is still renderer-neutral."""
    inputs = adapt_application_state(application_state)
    return resolve_projection(inputs["semantic"], inputs["expression"], context=inputs["context"])


def host_operation_envelope(output: Mapping[str, Any], operation_id: str, payload: Mapping[str, Any]) -> dict[str, Any]:
    """Create an explicit host handoff; invocation remains outside this adapter."""
    operations = output.get("interaction", {}).get("operations", [])
    if operation_id not in operations:
        raise ValueError(f"operation not exposed: {operation_id}")
    return {"operationId": operation_id, "payload": deepcopy(dict(payload)), "owner": "host-application"}
