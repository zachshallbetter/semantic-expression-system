#!/usr/bin/env python3
"""Validate SES-021 output against the SES-022 canonical fixture."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/conformance/resolved-output-fixtures.json"


class ValidationFailure(ValueError):
    def __init__(self, code: str, path: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.path = path


def _read_path(value: Any, path: str) -> Any:
    matches = re.finditer(r"([^.\[\]]+)|\[(\d+)\]", path)
    tokens = [match.group(1) if match.group(1) is not None else int(match.group(2)) for match in matches]
    current = value
    for token in tokens:
        key: Any = token if isinstance(token, int) else token
        try:
            current = current[key]
        except (KeyError, IndexError, TypeError) as error:
            raise ValidationFailure("ERR_OUTPUT_PATH_MISSING", path, str(error)) from error
    return current


def validate(output: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    for section in fixture["requiredSections"]:
        if section not in output:
            failures.append({"code": "ERR_OUTPUT_SECTION_MISSING", "path": section})
    for path, expected in fixture["expectations"].items():
        try:
            actual = _read_path(output, path)
        except ValidationFailure as error:
            failures.append({"code": error.code, "path": error.path})
            continue
        if actual != expected:
            failures.append({"code": "ERR_OUTPUT_EXPECTATION_MISMATCH", "path": path})
    for field in fixture["forbiddenHostFields"]:
        if field in output:
            failures.append({"code": "ERR_OUTPUT_HOST_FIELD_PRESENT", "path": field})
    return {
        "fixture": fixture["id"],
        "result": "pass" if not failures else "fail",
        "failureCount": len(failures),
        "failures": failures,
    }


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    output = json.loads(sys.stdin.read())
    result = validate(output, fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["result"] == "pass" else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"validate-resolved-output: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
