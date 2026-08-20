"""Pure SES-036 security and trust-boundary validation."""

from __future__ import annotations

from typing import Any, Mapping
from urllib.parse import urlparse


class SecurityValidationError(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


EXECUTABLE_KEYS = {"code", "script", "eval", "function", "handler", "onClick", "shader", "expression"}
UNSAFE_SCHEMES = {"javascript", "data", "file", "vbscript"}
SAFE_SCHEMES = {"fixture", "https"}
CUSTOM_KEYS = {"customSource", "customFilter", "customAsset"}


def validate_expression_security(expression: Mapping[str, Any]) -> dict[str, Any]:
    def walk(value: Any, path: str) -> None:
        if isinstance(value, Mapping):
            for key, child in value.items():
                child_path = f"{path}.{key}" if path else str(key)
                if key in EXECUTABLE_KEYS:
                    raise SecurityValidationError("ERR_EXECUTABLE_EXPRESSION_INPUT", child_path, f"executable input {key} is not accepted")
                if key in CUSTOM_KEYS:
                    if not isinstance(child, str) or not child.startswith("custom:") or ":" not in child[7:]:
                        raise SecurityValidationError("ERR_CUSTOM_SOURCE_UNNAMESPACED", child_path, "custom source must use a namespaced custom: value")
                if key == "source" and isinstance(child, str):
                    scheme = urlparse(child).scheme.lower()
                    if scheme in UNSAFE_SCHEMES or scheme not in SAFE_SCHEMES:
                        raise SecurityValidationError("ERR_ASSET_SOURCE_UNSAFE", child_path, f"source scheme {scheme or 'missing'} is not allowed")
                walk(child, child_path)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")
    walk(expression, "")
    return {"result": "pass", "trust": "data-only", "executableInputs": False}
