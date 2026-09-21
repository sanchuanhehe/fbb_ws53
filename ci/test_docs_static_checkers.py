#!/usr/bin/env python3
"""Regression tests for strict documentation-debt reporting."""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPOSITORY_ROOT / ".github" / "scripts"
SOURCE_CHECKER = SCRIPTS_DIR / "check-docs.py"
SUMMARY_SCRIPT = SCRIPTS_DIR / "summarize-docs-reports.py"
WORKFLOW = REPOSITORY_ROOT / ".github" / "workflows" / "docs-pages.yml"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from docs_static_report import build_report, emit_warning_annotations


def write_baseline(
    root: Path,
    *,
    source: list[dict[str, str | int]] | None = None,
    rendered: list[dict[str, str | int]] | None = None,
) -> Path:
    path = root / ".github" / "docs-static-baseline.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "version": 1,
                "source": source or [],
                "rendered": rendered or [],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def run_source_checker(root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SOURCE_CHECKER), "--root", str(root), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )


def load_rendered_checker() -> object:
    spec = importlib.util.spec_from_file_location(
        "check_rendered_site_for_test", SCRIPTS_DIR / "check-rendered-site.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SourceCheckerTests(unittest.TestCase):
    def test_baseline_known_finding_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            (docs / "legacy.md").write_text("legacy\n", encoding="utf-8")
            write_baseline(
                root,
                source=[
                    {
                        "rule": "SRC101",
                        "path": "docs/legacy.md",
                        "line": 1,
                        "message": "legacy page has no structured doc_type metadata",
                    }
                ],
            )
            report = root / "source.json"

            result = run_source_checker(root, "--json-report", str(report))

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["result"], "fail")
            self.assertEqual(payload["summary"]["baseline_known"], 1)
            self.assertEqual(payload["summary"]["baseline_new"], 0)

    def test_zero_current_with_resolved_baseline_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            write_baseline(
                root,
                source=[
                    {
                        "rule": "SRC101",
                        "path": "docs/removed.md",
                        "line": 1,
                        "message": "legacy page has no structured doc_type metadata",
                    }
                ],
            )
            report = root / "source.json"

            result = run_source_checker(root, "--json-report", str(report))

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["result"], "pass")
            self.assertEqual(payload["summary"]["findings"], 0)
            self.assertEqual(payload["summary"]["baseline_resolved"], 1)
            self.assertEqual(len(payload["resolved"]), 1)

    def test_reports_are_not_truncated_after_console_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            docs = root / "docs"
            docs.mkdir()
            body = "---\ndoc_type: how-to\n---\n" + "".join(
                "![](image.png)\n" for _ in range(45)
            )
            (docs / "many.md").write_text(body, encoding="utf-8")
            (docs / "image.png").write_bytes(b"not-used-by-checker")
            write_baseline(root)
            json_report = root / "source.json"
            tsv_report = root / "source.tsv"

            result = run_source_checker(
                root,
                "--json-report",
                str(json_report),
                "--tsv-report",
                str(tsv_report),
            )

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            payload = json.loads(json_report.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["findings"], 45)
            self.assertEqual(len(payload["findings"]), 45)
            self.assertEqual(
                len(tsv_report.read_text(encoding="utf-8").splitlines()), 46
            )
            self.assertIn("additional finding(s) omitted", result.stdout)

    def test_empty_reports_remain_complete(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            write_baseline(root)
            json_report = root / "source.json"
            tsv_report = root / "source.tsv"

            result = run_source_checker(
                root,
                "--json-report",
                str(json_report),
                "--tsv-report",
                str(tsv_report),
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(json_report.read_text(encoding="utf-8"))
            self.assertEqual(payload["findings"], [])
            self.assertEqual(payload["resolved"], [])
            self.assertEqual(
                tsv_report.read_text(encoding="utf-8").splitlines(),
                ["state\tclassification\trule\tpath\tline\tmessage"],
            )

    def test_report_write_failure_returns_two(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            write_baseline(root)
            output_directory = root / "not-a-file"
            output_directory.mkdir()

            result = run_source_checker(root, "--json-report", str(output_directory))

            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertIn("SRC006", result.stderr)


class RenderedCheckerTests(unittest.TestCase):
    def test_baseline_known_finding_still_fails(self) -> None:
        checker = load_rendered_checker()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "site"
            site.mkdir()
            finding = checker.Finding(
                "WEB002", "legacy/index.html", 7, "asset is missing", False
            )
            baseline = write_baseline(
                root,
                rendered=[
                    {
                        "rule": finding.rule,
                        "path": finding.path,
                        "line": finding.line,
                        "message": finding.message,
                    }
                ],
            )
            report = root / "rendered.json"
            args = argparse.Namespace(
                site_dir=site,
                root=root,
                site_url="https://example.invalid/",
                baseline=baseline,
                update_baseline=False,
                json_report=report,
                tsv_report=None,
                annotation_limit_per_rule=0,
            )

            with (
                mock.patch.object(checker, "parse_args", return_value=args),
                mock.patch.object(
                    checker, "parse_html_files", return_value=({}, [finding])
                ),
                mock.patch.object(
                    checker, "get_started_contract_findings", return_value=([], 0, 0)
                ),
                mock.patch.object(
                    checker, "maintained_output_paths", return_value=set()
                ),
                contextlib.redirect_stdout(io.StringIO()),
                contextlib.redirect_stderr(io.StringIO()),
            ):
                result = checker.main()

            self.assertEqual(result, 1)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["baseline_known"], 1)
            self.assertEqual(payload["summary"]["result"], "fail")


class AnnotationTests(unittest.TestCase):
    def test_annotations_are_limited_per_rule_and_escaped(self) -> None:
        findings = [
            {
                "rule": "SRC101",
                "path": "docs/a,b:c.md",
                "line": index,
                "message": f"percent % and newline\nitem {index}",
            }
            for index in range(1, 4)
        ] + [
            {
                "rule": "SRC102",
                "path": "docs/image.md",
                "line": index,
                "message": "missing alt",
            }
            for index in range(1, 3)
        ]
        classifications = {
            (item["rule"], item["path"], item["line"], item["message"]): (
                "baseline_known"
            )
            for item in findings
        }
        report = build_report(
            check="source",
            findings=findings,
            classifications=classifications,
            resolved=[],
            context={},
        )
        output = io.StringIO()

        with (
            mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}),
            contextlib.redirect_stderr(output),
        ):
            emit_warning_annotations(report, limit_per_rule=1)

        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 2)
        self.assertTrue(all(line.startswith("::warning ") for line in lines))
        self.assertIn("a%2Cb%3Ac.md", lines[0])
        self.assertIn("%25", lines[0])
        self.assertIn("%0A", lines[0])
        self.assertIn("(3 total)", lines[0])
        self.assertIn("(2 total)", lines[1])


class WorkflowContractTests(unittest.TestCase):
    def test_checker_failures_stay_visible_while_evidence_collection_continues(
        self,
    ) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        documentation_job = workflow.split("  upstream_links:", 1)[0]

        def step_block(name: str) -> str:
            marker = f"      - name: {name}\n"
            start = documentation_job.index(marker)
            end = documentation_job.find("\n      - name: ", start + len(marker))
            return (
                documentation_job[start:] if end < 0 else documentation_job[start:end]
            )

        self.assertNotIn("continue-on-error:", documentation_job)
        for step_name in (
            "Check Get Started source and executable contract",
            "Run documentation gate unit tests",
            "Build documentation strictly",
            "Check rendered links, anchors, and assets",
        ):
            self.assertIn("if: ${{ !cancelled() }}", step_block(step_name))
        for step_name in (
            "Summarize findings and validation boundary",
            "Upload documentation evidence",
            "Enforce documentation quality gate",
        ):
            self.assertIn("if: always()", step_block(step_name))
        self.assertIn(
            "steps.documentation_summary.outcome == 'success'",
            documentation_job,
        )
        self.assertLess(
            documentation_job.index("- name: Upload documentation evidence"),
            documentation_job.index("- name: Enforce documentation quality gate"),
        )


class SummaryTests(unittest.TestCase):
    @staticmethod
    def report() -> dict[str, object]:
        return {
            "schema_version": 1,
            "check": "source",
            "summary": {
                "result": "fail",
                "findings": 2,
                "hard_blocking": 0,
                "baseline_known": 1,
                "baseline_new": 1,
                "baseline_resolved": 0,
                "by_rule": {"SRC101": 1, "SRC102": 1},
            },
            "context": {},
            "findings": [
                {
                    "classification": "baseline_known",
                    "rule": "SRC101",
                    "path": "docs/legacy.md",
                    "line": 1,
                    "message": "missing metadata",
                },
                {
                    "classification": "baseline_new",
                    "rule": "SRC102",
                    "path": "docs/new.md",
                    "line": 9,
                    "message": "empty alt text",
                },
            ],
            "resolved": [],
        }

    def test_summary_recomputes_classification_counts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "source.json"
            output = root / "summary.md"
            report.write_text(json.dumps(self.report()), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SUMMARY_SCRIPT),
                    str(report),
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            markdown = output.read_text(encoding="utf-8")
            self.assertIn("| source | FAIL | 2 | 0 | 1 | 1 | 0 |", markdown)
            self.assertIn("| source | SRC101 | 0 | 1 | 0 | 1 |", markdown)
            self.assertIn("| source | SRC102 | 0 | 0 | 1 | 1 |", markdown)

    def test_summary_fails_closed_on_inconsistent_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.report()
            payload["summary"]["findings"] = 3
            report = root / "source.json"
            output = root / "summary.md"
            report.write_text(json.dumps(payload), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SUMMARY_SCRIPT),
                    str(report),
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("REPORT ERROR", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
