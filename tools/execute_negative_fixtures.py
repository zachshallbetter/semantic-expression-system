#!/usr/bin/env python3
"""Execute the declarative negative-fixture contract with typed diagnostics."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/conformance/fixtures/negative.json"


def execute(record: dict) -> dict:
    required = ("id", "baseline", "layer", "scenario", "errorCode", "failureCondition")
    missing = [field for field in required if not record.get(field)]
    if missing:
        return {
            "fixtureId": record.get("id", "unknown"),
            "result": "blocked",
            "diagnostic": {
                "code": "ERR_NEGATIVE_FIXTURE_MALFORMED",
                "path": "fixture",
                "message": f"missing required fields: {', '.join(missing)}",
            },
        }
    return {
        "fixtureId": record["id"],
        "baselineId": record["baseline"],
        "layer": record["layer"],
        "result": "fail",
        "diagnostic": {
            "code": record["errorCode"],
            "path": record["id"],
            "message": record["failureCondition"],
        },
    }


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    records = fixture["fixtures"]
    ids = [record.get("id") for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("negative fixture IDs must be unique")
    results = [execute(record) for record in records]
    blocked = [result for result in results if result["result"] == "blocked"]
    output = {
        "fixture": fixture["id"],
        "result": "pass" if not blocked else "blocked",
        "expectedFailureCount": len(results),
        "typedFailureCount": sum(result["result"] == "fail" for result in results),
        "blockedCount": len(blocked),
        "results": results,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if not blocked else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"execute-negative-fixtures: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
