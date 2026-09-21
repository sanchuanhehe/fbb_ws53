"""Machine-readable reports and GitHub annotations for documentation checks."""

from __future__ import annotations

import csv
import json
import os
import sys
import tempfile
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from docs_static_baseline import as_entry, fingerprint

REPORT_SCHEMA_VERSION = 1
CURRENT_CLASSIFICATIONS = (
    "hard_blocking",
    "baseline_known",
    "baseline_new",
)


class ReportError(RuntimeError):
    """Raised when a requested report cannot be written."""


def _classified_entry(item: Any, classification: str) -> dict[str, str | int]:
    return {"classification": classification, **as_entry(item)}


def build_report(
    *,
    check: str,
    findings: Iterable[Any],
    classifications: Mapping[tuple[str, str, int, str], str],
    resolved: Iterable[tuple[str, str, int, str]],
    context: Mapping[str, Any],
) -> dict[str, Any]:
    """Build one complete report without truncating current or resolved items."""

    current_entries: list[dict[str, str | int]] = []
    counts: Counter[str] = Counter()
    rules: Counter[str] = Counter()
    for item in sorted(findings, key=fingerprint):
        identity = fingerprint(item)
        classification = classifications.get(identity, "hard_blocking")
        if classification not in CURRENT_CLASSIFICATIONS:
            raise ReportError(f"unknown finding classification: {classification!r}")
        entry = _classified_entry(item, classification)
        current_entries.append(entry)
        counts[classification] += 1
        rules[str(entry["rule"])] += 1

    resolved_entries = [
        {
            "classification": "baseline_resolved",
            "rule": rule,
            "path": path,
            "line": line,
            "message": message,
        }
        for rule, path, line, message in sorted(resolved)
    ]
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "check": check,
        "summary": {
            "result": "fail" if current_entries else "pass",
            "findings": len(current_entries),
            "hard_blocking": counts["hard_blocking"],
            "baseline_known": counts["baseline_known"],
            "baseline_new": counts["baseline_new"],
            "baseline_resolved": len(resolved_entries),
            "by_rule": dict(sorted(rules.items())),
        },
        "context": dict(context),
        "findings": current_entries,
        "resolved": resolved_entries,
    }


def _atomic_text_write(path: Path, writer: Any) -> None:
    temporary: Path | None = None
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            writer(handle)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except OSError as error:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
        raise ReportError(f"cannot write report {path}: {error}") from error


def write_json_report(path: Path, report: Mapping[str, Any]) -> None:
    def writer(handle: Any) -> None:
        json.dump(report, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    _atomic_text_write(path, writer)


def write_tsv_report(path: Path, report: Mapping[str, Any]) -> None:
    def writer(handle: Any) -> None:
        output = csv.writer(handle, delimiter="\t", lineterminator="\n")
        output.writerow(("state", "classification", "rule", "path", "line", "message"))
        for state in ("findings", "resolved"):
            for item in report.get(state, []):
                output.writerow(
                    (
                        "current" if state == "findings" else "resolved",
                        item["classification"],
                        item["rule"],
                        item["path"],
                        item["line"],
                        item["message"],
                    )
                )

    _atomic_text_write(path, writer)


def _annotation_escape(value: str, *, property_value: bool = False) -> str:
    escaped = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    if property_value:
        escaped = escaped.replace(":", "%3A").replace(",", "%2C")
    return escaped


def emit_warning_annotations(report: Mapping[str, Any], *, limit_per_rule: int) -> None:
    """Emit bounded warning annotations while retaining the full report on disk."""

    if os.environ.get("GITHUB_ACTIONS") != "true" or limit_per_rule <= 0:
        return
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for item in report.get("findings", []):
        grouped[str(item["rule"])].append(item)
    for rule in sorted(grouped):
        items = grouped[rule]
        for item in items[:limit_per_rule]:
            classification = str(item["classification"])
            title = _annotation_escape(
                f"{rule} {classification} ({len(items)} total)",
                property_value=True,
            )
            path = _annotation_escape(str(item["path"]), property_value=True)
            line = int(item["line"])
            message = _annotation_escape(f"[{classification}] {item['message']}")
            print(
                f"::warning file={path},line={line},title={title}::{message}",
                file=sys.stderr,
            )
