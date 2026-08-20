"""Minimal DOM/CSS host adapter for renderer-neutral SES output."""

from __future__ import annotations

from html import escape
from typing import Any, Mapping


class RenderError(ValueError):
    pass


def render_dom_css(output: Mapping[str, Any]) -> dict[str, str]:
    """Map resolved SES output to escaped HTML and CSS host artifacts."""
    identity = output.get("identity", {})
    semantic = output.get("semantic", {})
    expression = output.get("expression", {})
    if not identity.get("target"):
        raise RenderError("ERR_OUTPUT_IDENTITY_MISSING")
    operations = semantic.get("operations", [])
    if not isinstance(operations, list):
        raise RenderError("ERR_OUTPUT_REQUIRED_METADATA_MISSING")

    target = escape(str(identity["target"]), quote=True)
    visual_language = escape(str(expression.get("visualLanguage", "default")), quote=True)
    operation_markup = "".join(
        f'<button type="button" data-ses-operation="{escape(str(operation), quote=True)}">{escape(str(operation))}</button>'
        for operation in operations
    )
    html = (
        f'<article class="ses-{target}" data-ses-identity="{target}" '
        f'data-ses-visual-language="{visual_language}" aria-busy="false">'
        f'<div data-ses-semantic-target="{target}">{operation_markup}</div>'
        "</article>"
    )
    css = (
        f'.ses-{target} {{\n'
        "  display: block;\n"
        "  box-sizing: border-box;\n"
        "}\n"
        f'.ses-{target} [data-ses-operation] {{\n'
        "  cursor: pointer;\n"
        "}\n"
        f'.ses-{target} [data-ses-operation]:focus-visible {{\n'
        "  outline: 3px solid currentColor;\n"
        "  outline-offset: 2px;\n"
        "}\n"
    )
    return {"html": html, "css": css}
