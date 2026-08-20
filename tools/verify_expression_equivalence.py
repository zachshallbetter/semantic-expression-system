#!/usr/bin/env python3
"""Verify semantic identity across multiple SES expression records."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from ses_resolver import resolve_projection


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/conformance/expression-equivalence-fixtures.json"


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    semantic = fixture["semantic"]
    outputs = [resolve_projection(semantic, expression, context={"viewport": "wide"}) for expression in fixture["expressions"]]
    identities = {json.dumps(output["identity"], sort_keys=True) for output in outputs}
    operations = {json.dumps(output["interaction"]["operations"], sort_keys=True) for output in outputs}
    languages = {output["expression"]["visualLanguage"] for output in outputs}
    if len(identities) != 1:
        raise ValueError("semantic identity changed across expressions")
    if len(operations) != 1:
        raise ValueError("operation identity changed across expressions")
    if len(languages) != len(outputs):
        raise ValueError("expressions must use distinct Visual Languages")
    print(json.dumps({
        "fixture": fixture["id"],
        "result": "pass",
        "expressionCount": len(outputs),
        "sharedIdentity": outputs[0]["identity"],
        "sharedOperations": outputs[0]["interaction"]["operations"],
        "visualLanguages": sorted(languages),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"verify-expression-equivalence: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
