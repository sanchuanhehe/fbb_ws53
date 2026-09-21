#!/usr/bin/env python3
"""Render documentation checker JSON reports as a GitHub job summary.

The checkers remain the source of truth for pass/fail.  This script validates
their machine-readable reports, recomputes the classification counts, and
creates a compact Markdown index for people reviewing the Actions run.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

CURRENT_CLASSIFICATIONS = (
    "hard_blocking",
    "baseline_known",
    "baseline_new",
)
RESOLVED_CLASSIFICATION = "baseline_resolved"


class ReportError(ValueError):
    """Raised when a checker report is missing or internally inconsistent."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "reports",
        nargs="+",
        type=Path,
        help="checker JSON reports to summarize",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="write Markdown here instead of stdout",
    )
    return parser.parse_args()


def require_non_negative_int(value: Any, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ReportError(f"{field} must be a non-negative integer")
    return value


def validate_finding(
    value: Any,
    *,
    report_path: Path,
    index: int,
    allowed: set[str],
    collection: str,
) -> dict[str, Any]:
    prefix = f"{report_path}:{collection}[{index}]"
    if not isinstance(value, dict):
        raise ReportError(f"{prefix} must be an object")
    for field in ("classification", "rule", "path", "message"):
        if not isinstance(value.get(field), str) or not value[field]:
            raise ReportError(f"{prefix}.{field} must be a non-empty string")
    require_non_negative_int(value.get("line"), f"{prefix}.line")
    if value["line"] < 1:
        raise ReportError(f"{prefix}.line must be at least 1")
    if value["classification"] not in allowed:
        raise ReportError(f"{prefix}.classification must be one of {sorted(allowed)!r}")
    return value


def load_report(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ReportError(f"report not found: {path}") from error
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ReportError(f"cannot read report {path}: {error}") from error

    if not isinstance(data, dict):
        raise ReportError(f"{path}: report root must be an object")
    if data.get("schema_version") != 1:
        raise ReportError(
            f"{path}: schema_version must be 1, got {data.get('schema_version')!r}"
        )
    check = data.get("check")
    if not isinstance(check, str) or not check:
        raise ReportError(f"{path}: check must be a non-empty string")
    summary = data.get("summary")
    findings = data.get("findings")
    resolved = data.get("resolved")
    if not isinstance(summary, dict):
        raise ReportError(f"{path}: summary must be an object")
    if not isinstance(findings, list):
        raise ReportError(f"{path}: findings must be an array")
    if not isinstance(resolved, list):
        raise ReportError(f"{path}: resolved must be an array")

    current = [
        validate_finding(
            value,
            report_path=path,
            index=index,
            allowed=set(CURRENT_CLASSIFICATIONS),
            collection="findings",
        )
        for index, value in enumerate(findings)
    ]
    improvements = [
        validate_finding(
            value,
            report_path=path,
            index=index,
            allowed={RESOLVED_CLASSIFICATION},
            collection="resolved",
        )
        for index, value in enumerate(resolved)
    ]
    counts = Counter(item["classification"] for item in current)
    expected_summary = {
        "findings": len(current),
        "hard_blocking": counts["hard_blocking"],
        "baseline_known": counts["baseline_known"],
        "baseline_new": counts["baseline_new"],
        "baseline_resolved": len(improvements),
    }
    for field, expected in expected_summary.items():
        actual = require_non_negative_int(summary.get(field), f"{path}:summary.{field}")
        if actual != expected:
            raise ReportError(
                f"{path}: summary.{field} is {actual}, recomputed value is {expected}"
            )
    expected_result = "fail" if current else "pass"
    if summary.get("result") != expected_result:
        raise ReportError(
            f"{path}: summary.result must be {expected_result!r} for "
            f"{len(current)} current finding(s)"
        )

    return {
        "path": path.as_posix(),
        "check": check,
        "result": expected_result,
        "findings": current,
        "resolved": improvements,
        "counts": expected_summary,
    }


def markdown_cell(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("|", "\\|")


def render(reports: list[dict[str, Any]]) -> str:
    lines = [
        "## Documentation quality gate",
        "",
        "> Any current finding, including known historical debt, fails this gate.",
        "",
        "| Check | Result | Current findings | Hard blocking | Known historical | New baseline debt | Resolved baseline |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for report in reports:
        counts = report["counts"]
        result = "FAIL" if report["result"] == "fail" else "PASS"
        lines.append(
            "| "
            + " | ".join(
                markdown_cell(value)
                for value in (
                    report["check"],
                    result,
                    counts["findings"],
                    counts["hard_blocking"],
                    counts["baseline_known"],
                    counts["baseline_new"],
                    counts["baseline_resolved"],
                )
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "### Current findings by rule",
            "",
            "| Check | Rule | Hard blocking | Known historical | New baseline debt | Total |",
            "| --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    rows = 0
    for report in reports:
        by_rule: dict[str, Counter[str]] = defaultdict(Counter)
        for finding in report["findings"]:
            by_rule[finding["rule"]][finding["classification"]] += 1
        for rule in sorted(by_rule):
            counts = by_rule[rule]
            total = sum(counts.values())
            lines.append(
                "| "
                + " | ".join(
                    markdown_cell(value)
                    for value in (
                        report["check"],
                        rule,
                        counts["hard_blocking"],
                        counts["baseline_known"],
                        counts["baseline_new"],
                        total,
                    )
                )
                + " |"
            )
            rows += 1
    if rows == 0:
        lines.append("| - | - | 0 | 0 | 0 | 0 |")

    lines.extend(
        [
            "",
            "Complete, untruncated finding details are available in the uploaded JSON and TSV reports:",
            "",
        ]
    )
    for report in reports:
        json_path = report["path"]
        tsv_path = str(Path(json_path).with_suffix(".tsv"))
        lines.append(f"- `{json_path}`")
        lines.append(f"- `{tsv_path}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        reports = [load_report(path) for path in args.reports]
        markdown = render(reports)
    except ReportError as error:
        markdown = "\n".join(
            (
                "## Documentation quality gate",
                "",
                f"> **REPORT ERROR:** {error}",
                "",
                "The gate must fail because complete checker evidence is unavailable.",
                "",
            )
        )
        status = 1
    else:
        status = 0

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
