"""Pure SES operation exposure validation and event routing."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping


class OperationRoutingError(ValueError):
    def __init__(self, code: str, message: str, operation_id: str) -> None:
        super().__init__(message)
        self.code = code
        self.operation_id = operation_id


def validate_operation_exposure(
    required_operations: list[str],
    exposure: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    results = []
    for operation_id in required_operations:
        record = exposure.get(operation_id)
        if record is None or not record.get("exposed", False):
            raise OperationRoutingError("ERR_OPERATION_NOT_EXPOSED", f"operation {operation_id} is not exposed", operation_id)
        if not record.get("signaled", False):
            raise OperationRoutingError("ERR_OPERATION_NOT_SIGNALED", f"operation {operation_id} is not signaled", operation_id)
        results.append({"id": operation_id, "exposed": True, "signaled": True, "enabled": bool(record.get("enabled", True))})
    return {"result": "pass", "operations": results}


def route_event(event: Mapping[str, Any], exposure: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Return a host-routable operation envelope; never invoke the operation."""
    operation_id = event.get("operationId")
    if not isinstance(operation_id, str) or not operation_id:
        raise OperationRoutingError("ERR_OPERATION_ID_MISSING", "event has no operation identity", "")
    record = exposure.get(operation_id)
    if record is None or not record.get("exposed", False):
        raise OperationRoutingError("ERR_OPERATION_NOT_EXPOSED", f"operation {operation_id} is not exposed", operation_id)
    if not record.get("enabled", True):
        raise OperationRoutingError("ERR_OPERATION_DISABLED", f"operation {operation_id} is disabled", operation_id)
    return {
        "operationId": operation_id,
        "sourceIdentity": deepcopy(event.get("sourceIdentity")),
        "payload": deepcopy(event.get("payload", {})),
        "dispatch": "host-owned",
    }
