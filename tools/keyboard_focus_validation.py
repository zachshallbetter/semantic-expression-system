"""Pure SES-033 keyboard order and focus validation."""

from __future__ import annotations

from typing import Any, Mapping


class KeyboardFocusError(ValueError):
    def __init__(self, code: str, field_path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.field_path = field_path


def validate_keyboard_focus(record: Mapping[str, Any]) -> dict[str, Any]:
    semantic_order = record.get("semanticOrder", [])
    keyboard_order = record.get("keyboardOrder", [])
    if semantic_order != keyboard_order:
        raise KeyboardFocusError("ERR_KEYBOARD_ORDER_MISMATCH", "keyboardOrder", "keyboard order differs from semantic order")
    if not record.get("focusVisible", False):
        raise KeyboardFocusError("ERR_FOCUS_INDICATOR_OBSTRUCTED", "focusVisible", "focus indication is not visible")
    controls = record.get("controls", [])
    for index, control in enumerate(controls):
        if not isinstance(control, Mapping) or not control.get("id"):
            raise KeyboardFocusError("ERR_KEYBOARD_CONTROL_ID_MISSING", f"controls[{index}]", "keyboard control needs stable ID")
        if not control.get("keyboardReachable", False):
            raise KeyboardFocusError("ERR_KEYBOARD_CONTROL_UNREACHABLE", f"controls[{index}]", "keyboard control is unreachable")
        if control.get("tabIndex", 0) < 0:
            raise KeyboardFocusError("ERR_KEYBOARD_CONTROL_UNREACHABLE", f"controls[{index}].tabIndex", "control is removed from keyboard order")
    return {"result": "pass", "order": list(keyboard_order), "focusVisible": True, "controlCount": len(controls)}
