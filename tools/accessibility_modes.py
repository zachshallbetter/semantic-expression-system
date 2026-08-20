"""Pure SES-035 reduced-motion and high-contrast expression handling."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping


class AccessibilityModeError(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


def apply_accessibility_modes(output: Mapping[str, Any], context: Mapping[str, Any]) -> dict[str, Any]:
    result = deepcopy(dict(output))
    expression = result.setdefault("expression", {})
    motion = expression.get("motion", {})
    if context.get("reducedMotion", False):
        if not isinstance(motion, Mapping):
            raise AccessibilityModeError("ERR_MOTION_METADATA_INVALID", "expression.motion", "motion metadata must be an object")
        fallback = motion.get("reducedMotion")
        if fallback is None and motion.get("enabled", False):
            raise AccessibilityModeError("ERR_REDUCED_MOTION_FALLBACK_MISSING", "expression.motion.reducedMotion", "motion lacks reduced-motion fallback")
        expression["motion"] = {"enabled": False, "mode": "reduced", "fallback": deepcopy(fallback)}
    if context.get("highContrast", False):
        contrast = expression.get("highContrast")
        if not isinstance(contrast, Mapping) or not contrast.get("enabled", False):
            raise AccessibilityModeError("ERR_HIGH_CONTRAST_FALLBACK_MISSING", "expression.highContrast", "high-contrast expression is missing")
        expression["highContrast"] = deepcopy(dict(contrast))
    result["accessibility"] = {**dict(result.get("accessibility", {})), "reducedMotion": bool(context.get("reducedMotion", False)), "highContrast": bool(context.get("highContrast", False))}
    return result
