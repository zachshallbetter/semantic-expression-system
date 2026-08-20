"""Pure SES-026 recipe cascade and conflict detection."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping


class RecipeResolutionError(ValueError):
    def __init__(self, code: str, message: str, field_path: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


LAYER_ORDER = (
    "Visual Language",
    "Theme",
    "explicit user style options",
    "Composition Recipe",
    "Socket Recipe",
    "Block Recipe",
    "Variant Recipe",
    "Slot Recipe",
    "Element Recipe",
    "semantic State Recipe",
    "responsive Recipe",
    "accessibility overrides",
)

PROTECTED_FIELDS = {
    "identity", "composition", "socket", "block", "slot", "element", "variant", "state",
    "operations", "operationIdentity", "semanticRole", "accessibilityRelationship",
    "requiredContent", "acceptedContent", "invariance", "businessBehavior", "routingIntent",
}


def _merge(target: dict[str, Any], source: Mapping[str, Any], layer: str, path: str, trace: list[dict[str, Any]]) -> None:
    for key, value in source.items():
        field_path = f"{path}.{key}" if path else key
        if key in PROTECTED_FIELDS:
            raise RecipeResolutionError("ERR_PROTECTED_FIELD_OVERRIDE", f"protected field {field_path}", field_path)
        if isinstance(value, Mapping) and isinstance(target.get(key), Mapping):
            _merge(target[key], value, layer, field_path, trace)
            continue
        previous = deepcopy(target[key]) if key in target else None
        target[key] = deepcopy(value)
        trace.append({"layer": layer, "fieldPath": field_path, "previous": previous, "result": deepcopy(value), "mergeRule": "replace"})


def resolve_recipe_layers(layers: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Apply the fixed cascade and return expression data plus provenance."""
    unknown = sorted(set(layers) - set(LAYER_ORDER))
    if unknown:
        raise RecipeResolutionError("ERR_RECIPE_LAYER_INVALID", f"unknown recipe layer {unknown[0]}", unknown[0])
    resolved: dict[str, Any] = {}
    trace: list[dict[str, Any]] = []
    for layer in LAYER_ORDER:
        value = layers.get(layer)
        if value is None:
            continue
        if not isinstance(value, Mapping):
            raise RecipeResolutionError("ERR_RECIPE_LAYER_INVALID", f"layer {layer} is not an object", layer)
        _merge(resolved, value, layer, "", trace)
    return {"resolved": resolved, "trace": trace}
