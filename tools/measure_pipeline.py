#!/usr/bin/env python3
"""Measure the local SES resolver and DOM/CSS adapter."""

from __future__ import annotations

import json
import platform
from pathlib import Path
import statistics
import sys
import time

from dom_css_renderer import render_dom_css
from ses_resolver import resolve_projection


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "docs/conformance/reference-pack"


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, int((len(ordered) - 1) * fraction))
    return ordered[index]


def main() -> int:
    semantic = json.loads((REFERENCE / "media-card.json").read_text(encoding="utf-8"))
    expression = json.loads((REFERENCE / "appearance-neo-edo.json").read_text(encoding="utf-8"))
    sample_count = 1000
    resolver_times: list[float] = []
    renderer_times: list[float] = []
    for _ in range(sample_count):
        start = time.perf_counter_ns()
        output = resolve_projection(semantic, expression, context={"viewport": "wide"})
        resolver_times.append((time.perf_counter_ns() - start) / 1_000_000)
        start = time.perf_counter_ns()
        render_dom_css(output)
        renderer_times.append((time.perf_counter_ns() - start) / 1_000_000)
    result = {
        "fixture": "media-card/neo-edo",
        "sampleCount": sample_count,
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "units": "milliseconds",
        "resolver": {"p50": statistics.median(resolver_times), "p95": percentile(resolver_times, 0.95), "budgetP95": 5.0},
        "rendererAdapter": {"p50": statistics.median(renderer_times), "p95": percentile(renderer_times, 0.95)},
        "method": "perf_counter_ns around pure local calls; process warm-up not separately discarded",
    }
    result["result"] = "pass" if result["resolver"]["p95"] <= result["resolver"]["budgetP95"] else "inconclusive"
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"measure-pipeline: fail: {error}", file=sys.stderr)
        raise SystemExit(1)
