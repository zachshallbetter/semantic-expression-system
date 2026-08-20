"""Pure token and asset resolution for SES-025."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping


class ResourceResolutionError(ValueError):
    def __init__(self, code: str, message: str, field_path: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


TOKEN_LAYERS = ("primitive", "semantic", "role", "recipe", "explicit")


def resolve_token(name: str, registry: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Resolve one token through the fixed SES layer order with alias tracing."""
    visited: list[str] = []

    def visit(token_name: str) -> dict[str, Any]:
        if token_name in visited:
            raise ResourceResolutionError("ERR_TOKEN_CYCLE", f"token cycle at {token_name}", token_name)
        visited.append(token_name)
        matches = [(layer, registry.get(layer, {}).get(token_name)) for layer in TOKEN_LAYERS]
        matches = [(layer, value) for layer, value in matches if value is not None]
        if not matches:
            raise ResourceResolutionError("ERR_TOKEN_UNRESOLVED", f"unknown token {token_name}", token_name)
        layer, value = matches[-1]
        if isinstance(value, Mapping) and "alias" in value:
            resolved = visit(str(value["alias"]))
            return {"id": token_name, "value": resolved["value"], "sourceLayer": layer, "aliasPath": [token_name] + resolved["aliasPath"]}
        return {"id": token_name, "value": deepcopy(value), "sourceLayer": layer, "aliasPath": [token_name]}

    return visit(name)


def resolve_asset(asset_id: str, category: str, registry: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Resolve an asset ID within its declared category without loading it."""
    category_records = registry.get(category, {})
    record = category_records.get(asset_id)
    if record is None:
        if any(asset_id in records for records in registry.values()):
            raise ResourceResolutionError("ERR_ASSET_CATEGORY_MISMATCH", f"{asset_id} is not a {category} asset", asset_id)
        raise ResourceResolutionError("ERR_ASSET_NOT_FOUND", f"unknown asset {asset_id}", asset_id)
    if not isinstance(record, Mapping) or record.get("category") != category:
        raise ResourceResolutionError("ERR_ASSET_METADATA_INVALID", f"invalid metadata for {asset_id}", asset_id)
    return {"id": asset_id, "category": category, "metadata": deepcopy(dict(record))}
