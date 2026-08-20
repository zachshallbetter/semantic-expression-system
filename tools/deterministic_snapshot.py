"""Deterministic SES output serialization and snapshot comparison."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_value(value: Any) -> Any:
    """Return a JSON-compatible value with explicitly ordered object fields."""
    if isinstance(value, dict):
        return {key: canonical_value(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        return [canonical_value(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    raise TypeError(f"unsupported snapshot value: {type(value).__name__}")


def canonical_serialize(value: Any) -> str:
    """Serialize a value with stable object order and no ambient formatting."""
    return json.dumps(canonical_value(value), ensure_ascii=False, separators=(",", ":"))


def snapshot(value: Any) -> dict[str, str]:
    serialized = canonical_serialize(value)
    return {
        "algorithm": "sha256",
        "encoding": "utf-8",
        "serialized": serialized,
        "digest": hashlib.sha256(serialized.encode("utf-8")).hexdigest(),
    }


def compare_snapshots(expected: dict[str, str], value: Any) -> dict[str, Any]:
    actual = snapshot(value)
    return {
        "result": "pass" if expected["digest"] == actual["digest"] else "fail",
        "expectedDigest": expected["digest"],
        "actualDigest": actual["digest"],
    }
