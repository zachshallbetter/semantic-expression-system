"""Minimal pure SES semantic-to-expression resolver.

The resolver accepts already-loaded immutable records. It does not read files,
load assets, render, invoke operations, or mutate application state.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from resource_resolution import resolve_asset, resolve_token


class ResolutionError(ValueError):
    """Typed failure for an invalid minimal resolution input."""

    def __init__(self, code: str, message: str, field_path: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


def _require(record: Mapping[str, Any], key: str, field_path: str) -> Any:
    if key not in record:
        raise ResolutionError("ERR_RESOLVE_REQUIRED_INPUT", f"missing {field_path}", field_path)
    return record[key]


def resolve_projection(
    semantic: Mapping[str, Any],
    expression: Mapping[str, Any],
    *,
    context: Mapping[str, Any] | None = None,
    token_registry: Mapping[str, Mapping[str, Any]] | None = None,
    asset_registry: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Resolve one reference projection into renderer-neutral output.

    The minimal implementation resolves the canonical semantic identity,
    operations, invariance, expression layers, and context. Expression data
    cannot replace semantic identity or operations.
    """
    semantic_id = semantic.get("composition") or _require(semantic, "block", "semantic.block")
    expression_target = _require(expression, "target", "expression.target")
    if expression_target != semantic_id and expression_target != semantic.get("block"):
        raise ResolutionError(
            "ERR_RESOLVE_TARGET_MISMATCH",
            f"expression target {expression_target!r} does not match {semantic_id!r}",
            "expression.target",
        )

    operations = list(_require(semantic, "operations", "semantic.operations"))
    projection = deepcopy(expression.get("projection", {}))
    morphology = deepcopy(expression.get("morphology", {}))
    appearance = deepcopy(expression.get("appearance", {}))
    active_context = deepcopy(dict(context or {}))
    tokens: list[dict[str, Any]] = []
    assets: list[dict[str, Any]] = []
    if token_registry is not None:
        for token_name in sorted({item["token"] for group in appearance.values() if isinstance(group, list) for item in group if isinstance(item, Mapping) and "token" in item}):
            tokens.append(resolve_token(token_name, token_registry))
    if asset_registry is not None:
        group_categories = {"background": "backgrounds", "patterns": "patterns", "edges": "edges", "decorations": "ornaments"}
        type_categories = {"texture": "textures", "pattern": "patterns", "seal": "ornaments", "edge": "edges"}
        asset_requests = sorted({(item["asset"], item.get("category", "") or type_categories.get(item.get("type"), group_categories.get(group_name, ""))) for group_name, group in appearance.items() if isinstance(group, list) for item in group if isinstance(item, Mapping) and "asset" in item})
        category_by_type = {"texture": "textures", "pattern": "patterns", "seal": "ornaments", "edge": "edges"}
        for asset_name, declared_category in asset_requests:
            category = declared_category or next((category_by_type.get(item.get("type"), "") for group in appearance.values() if isinstance(group, list) for item in group if isinstance(item, Mapping) and item.get("asset") == asset_name), "")
            assets.append(resolve_asset(asset_name, category, asset_registry))

    return {
        "identity": {
            "composition": semantic_id,
            "target": expression_target,
        },
        "semantic": {
            "sockets": deepcopy(semantic.get("sockets", [])),
            "operations": operations,
            "invariance": deepcopy(semantic.get("invariance", {})),
        },
        "projection": {
            "preserve": list(projection.get("preserve", [])),
            "transform": list(projection.get("transform", [])),
            "omit": list(projection.get("omit", [])),
            "introduce": list(projection.get("introduce", [])),
        },
        "expression": {
            "visualLanguage": expression.get("visualLanguage"),
            "morphology": morphology,
            "appearance": appearance,
        },
        "resources": {
            "tokens": tokens,
            "assets": assets,
            "resolution": "caller-supplied registries",
        },
        "interaction": {"operations": operations},
        "accessibility": {"required": True, "source": "semantic-contract"},
        "responsive": {"context": active_context, "rules": []},
        "trace": {
            "layers": ["Visual Language", "Theme", "Recipe"],
            "source": expression.get("source"),
        },
        "diagnostics": {"warnings": [], "failures": []},
    }
