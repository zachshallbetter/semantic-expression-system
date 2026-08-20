"""Pure SES-027 Projection Contract enforcement."""

from __future__ import annotations

from typing import Any, Mapping


class ProjectionViolation(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


def enforce_projection(
    contract: Mapping[str, Any],
    mutations: Mapping[str, Any],
    *,
    semantic_before: Mapping[str, Any] | None = None,
    semantic_after: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Check declared projection permissions and required semantic invariants."""
    preserve = set(contract.get("preserve", []))
    transform = set(contract.get("transform", []))
    may_omit = set(contract.get("mayOmit", contract.get("omit", [])))
    may_introduce = set(contract.get("mayIntroduce", contract.get("introduce", [])))
    classifications: list[dict[str, str]] = []
    for field, kind in mutations.items():
        if kind == "preserve":
            if field not in preserve:
                raise ProjectionViolation("ERR_PROJECTION_CLASSIFICATION_MISSING", field, f"{field} is not declared preserve")
            classifications.append({"field": field, "classification": kind})
        elif kind == "transform":
            if field not in transform:
                raise ProjectionViolation("ERR_TRANSFORM_UNDECLARED", field, f"{field} is not declared transform")
            classifications.append({"field": field, "classification": kind})
        elif kind == "omit":
            if field not in may_omit:
                raise ProjectionViolation("ERR_REQUIRED_CONTENT_OMITTED", field, f"{field} is not permitted to omit")
            classifications.append({"field": field, "classification": kind})
        elif kind == "introduce":
            if field not in may_introduce:
                raise ProjectionViolation("ERR_INTRODUCED_SEMANTIC_MEANING", field, f"{field} is not presentation-only")
            classifications.append({"field": field, "classification": kind})
        else:
            raise ProjectionViolation("ERR_PROJECTION_CLASSIFICATION_UNKNOWN", field, f"unknown classification {kind}")

    before = semantic_before or {}
    after = semantic_after or before
    for field in sorted(preserve):
        if field in before and field in after and before[field] != after[field]:
            raise ProjectionViolation("ERR_PRESERVED_SEMANTIC_CHANGED", field, f"preserved field {field} changed")
    return {"result": "pass", "classifications": classifications, "preserved": sorted(preserve)}
