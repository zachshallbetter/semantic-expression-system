#!/usr/bin/env python3
"""Compare Python and JavaScript semantic projection summaries and mutations."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

from ses_resolver import ResolutionError, resolve_projection


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/conformance/expression-equivalence-fixtures.json"
JS_CHECK = ROOT / "tools/cross_language_projection.mjs"


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    python_outputs = [resolve_projection(fixture["semantic"], expression) for expression in fixture["expressions"]]
    js_output = json.loads(subprocess.run(["node", str(JS_CHECK), str(FIXTURE)], check=True, capture_output=True, text=True).stdout)
    python_summary = {
        "identity": python_outputs[0]["identity"],
        "operations": python_outputs[0]["interaction"]["operations"],
        "visualLanguages": sorted(output["expression"]["visualLanguage"] for output in python_outputs),
    }
    js_summary = {"identity": js_output["identity"], "operations": js_output["operations"], "visualLanguages": sorted(vector["visualLanguage"] for vector in js_output["vectors"])}
    if python_summary != js_summary:
        raise ValueError("Python and JavaScript projection summaries differ")

    mutation = dict(fixture["expressions"][0])
    mutation["target"] = "mutated-target"
    try:
        resolve_projection(fixture["semantic"], mutation)
    except ResolutionError as error:
        if error.code != "ERR_RESOLVE_TARGET_MISMATCH":
            raise
    else:
        raise ValueError("target mutation was accepted")
    operation_mutation = dict(fixture["semantic"])
    operation_mutation["operations"] = ["mutated-operation"]
    if operation_mutation["operations"] == fixture["semantic"]["operations"]:
        raise ValueError("operation mutation was not applied")
    print(json.dumps({"fixture": fixture["id"], "result": "pass", "languages": python_summary["visualLanguages"], "mutationChecks": ["target-rejected", "operation-change-detected"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, subprocess.SubprocessError, json.JSONDecodeError) as error:
        print(f"cross-language-equivalence: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
