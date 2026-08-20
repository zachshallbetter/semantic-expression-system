#!/usr/bin/env python3
"""Resolve the canonical SES reference fixture without rendering."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from ses_resolver import ResolutionError, resolve_projection


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "docs/conformance/reference-pack"


def main() -> int:
    semantic = json.loads((REFERENCE / "media-card.json").read_text(encoding="utf-8"))
    expression = json.loads((REFERENCE / "appearance-neo-edo.json").read_text(encoding="utf-8"))
    resolved = resolve_projection(semantic, expression, context={"viewport": "wide"})
    print(json.dumps(resolved, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError, ResolutionError) as error:
        print(f"resolve-reference-fixture: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
