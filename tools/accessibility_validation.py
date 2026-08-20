"""Pure SES-032 accessible-name, role, and relationship validation."""

from __future__ import annotations

from typing import Any, Mapping


class AccessibilityError(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


ALLOWED_ROLES = {"article", "button", "heading", "img", "group", "region", "text"}


def validate_accessibility(record: Mapping[str, Any]) -> dict[str, Any]:
    name = record.get("accessibleName")
    if not isinstance(name, str) or not name.strip():
        raise AccessibilityError("ERR_ACCESSIBLE_NAME_MISSING", "accessibleName", "accessible name is required")
    role = record.get("role")
    if role not in ALLOWED_ROLES:
        raise AccessibilityError("ERR_ACCESSIBLE_ROLE_INVALID", "role", f"unsupported role {role!r}")
    relationships = record.get("relationships", [])
    if not isinstance(relationships, list):
        raise AccessibilityError("ERR_ACCESSIBLE_RELATIONSHIP_INVALID", "relationships", "relationships must be a list")
    ids = set(record.get("knownIds", []))
    for index, relationship in enumerate(relationships):
        target = relationship.get("target") if isinstance(relationship, Mapping) else None
        if not isinstance(target, str) or target not in ids:
            raise AccessibilityError("ERR_ACCESSIBLE_RELATIONSHIP_BROKEN", f"relationships[{index}].target", f"unknown relationship target {target!r}")
    operations = record.get("operations", [])
    for index, operation in enumerate(operations):
        if not isinstance(operation, Mapping) or not operation.get("id") or not operation.get("accessibleName"):
            raise AccessibilityError("ERR_OPERATION_ACCESSIBLE_NAME_MISSING", f"operations[{index}]", "operation needs stable ID and accessible name")
    return {
        "result": "pass",
        "accessibleName": name,
        "role": role,
        "relationshipCount": len(relationships),
        "operationCount": len(operations),
    }
