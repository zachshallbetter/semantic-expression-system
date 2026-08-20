#!/usr/bin/env python3
"""Validate the renderer-neutral invariants of the SES-007 vectors."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/conformance/projection-equivalence.json"


def main() -> int:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    vectors = fixture["vectors"]
    semantic = fixture["semantic"]

    if len(vectors) != 4:
        raise ValueError(f"expected 4 projection vectors, found {len(vectors)}")

    vector_ids = [vector["id"] for vector in vectors]
    if len(set(vector_ids)) != len(vector_ids):
        raise ValueError("projection vector IDs must be unique")

    if not semantic["identities"]:
        raise ValueError("shared semantic identity set must not be empty")
    if not semantic["operations"]:
        raise ValueError("shared operation set must not be empty")

    for vector in vectors:
        if not vector["visualLanguage"]:
            raise ValueError(f"{vector['id']} has no Visual Language")
        if not vector["allowedMutations"]:
            raise ValueError(f"{vector['id']} has no declared expression mutations")

    print(json.dumps({
        "fixture": fixture["id"],
        "result": "pass",
        "vectorCount": len(vectors),
        "sharedIdentityCount": len(semantic["identities"]),
        "sharedOperationCount": len(semantic["operations"]),
        "vectors": vector_ids,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"projection-equivalence: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
