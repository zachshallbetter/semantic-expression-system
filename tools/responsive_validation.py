"""Pure SES-034 responsive reachability and state-transition validation."""

from __future__ import annotations

from typing import Any, Mapping


class ResponsiveError(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


def validate_responsive(record: Mapping[str, Any]) -> dict[str, Any]:
    required_content = set(record.get("requiredContent", []))
    required_operations = set(record.get("requiredOperations", []))
    contexts = record.get("contexts", [])
    if not contexts:
        raise ResponsiveError("ERR_RESPONSIVE_CONTEXT_MISSING", "contexts", "at least one responsive context is required")
    checked = []
    for index, context in enumerate(contexts):
        path = f"contexts[{index}]"
        if context.get("overflow", False):
            raise ResponsiveError("ERR_COMPOSITION_OVERFLOW", path, "responsive context overflows")
        if set(context.get("clippedContent", [])) & required_content:
            raise ResponsiveError("ERR_CONTENT_CLIPPED", path, "required content is clipped")
        if set(context.get("hiddenContent", [])) & required_content:
            raise ResponsiveError("ERR_CONTENT_UNREACHABLE", path, "required content is hidden")
        if not required_operations.issubset(set(context.get("reachableOperations", []))):
            raise ResponsiveError("ERR_CONTENT_UNREACHABLE", path, "required operation is unreachable")
        checked.append(context.get("id", path))
    transitions = record.get("stateTransitions", {})
    for source, targets in transitions.items():
        if not isinstance(targets, list) or any(target not in record.get("states", []) for target in targets):
            raise ResponsiveError("ERR_STATE_TRANSITION_INVALID", f"stateTransitions.{source}", "transition target is not a declared state")
    return {"result": "pass", "contexts": checked, "transitionCount": sum(len(targets) for targets in transitions.values())}
