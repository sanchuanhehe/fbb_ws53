"""Tests for fail-closed validation of non-HIL evidence bundles."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from tools.docs.get_started import contract, evidence
from tools.docs.get_started.runner import ValidationFailure


SDK_COMMIT = "a" * 40


def valid_payload(directory: Path) -> dict[str, object]:
    steps = []
    for command_id, argv in evidence._expected_step_argv().items():
        stdout_log = f"{command_id}.stdout.log"
        stderr_log = f"{command_id}.stderr.log"
        (directory / stdout_log).write_text("", encoding="utf-8")
        (directory / stderr_log).write_text("", encoding="utf-8")
        steps.append(
            {
                "command_id": command_id,
                "argv": argv,
                "exit_code": 0,
                "duration_seconds": 0.1,
                "stdout_log": stdout_log,
                "stderr_log": stderr_log,
            }
        )
    return {
        "schema_version": 1,
        "status": "passed",
        "platform": "linux",
        "host": {
            "system": "Linux",
            "release": "test",
            "machine": "x86_64",
            "python": "3.12.0",
            "runner_label": "ubuntu-24.04",
            "runner_image_os": "ubuntu24",
            "runner_image_version": "test",
        },
        "started_at": "2026-09-22T00:00:00Z",
        "finished_at": "2026-09-22T00:01:00Z",
        "cli": {
            "repository": contract.CLI_REPOSITORY,
            "commit": contract.CLI_COMMIT,
            "version": contract.CLI_VERSION,
        },
        "sdk": {
            "documented_repository": contract.SDK_REPOSITORY,
            "documented_branch": contract.SDK_BRANCH,
            "version": contract.SDK_VERSION,
            "chip": contract.CHIP,
            "target": contract.TARGET,
            "commit": SDK_COMMIT,
        },
        "coverage": {
            "source_static": "not_run_by_this_script",
            "documented_repository_branch": "passed",
            "repository_checkout": "passed_by_github_actions",
            "environment": "passed",
            "configure": "passed",
            "firmware_build": "passed",
            "flash": "not_run",
            "serial_monitor": "not_run",
            "smoke": "not_run",
            "hil": "not_run",
        },
        "steps": steps,
        "artifacts": [
            {
                "path": path.as_posix(),
                "size_bytes": 1,
                "sha256": "b" * 64,
            }
            for path in contract.ARTIFACTS
        ],
        "error": None,
    }


def write_summary(directory: Path, payload: dict[str, object]) -> Path:
    summary = directory / "summary.json"
    summary.write_text(json.dumps(payload), encoding="utf-8")
    return summary


class EvidenceTests(unittest.TestCase):
    def test_complete_non_hil_bundle_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            summary = write_summary(directory, valid_payload(directory))

            evidence.validate_evidence(
                summary_path=summary,
                expected_platform="linux",
                expected_sdk_commit=SDK_COMMIT.upper(),
                expected_runner_label="ubuntu-24.04",
            )

    def test_hil_or_smoke_overclaim_is_rejected(self) -> None:
        for key in ("flash", "serial_monitor", "smoke", "hil"):
            with self.subTest(key=key):
                with tempfile.TemporaryDirectory() as directory_name:
                    directory = Path(directory_name)
                    payload = valid_payload(directory)
                    payload["coverage"][key] = "passed"  # type: ignore[index]
                    summary = write_summary(directory, payload)

                    with self.assertRaisesRegex(
                        ValidationFailure, "coverage boundary"
                    ):
                        evidence.validate_evidence(
                            summary_path=summary,
                            expected_platform="linux",
                            expected_sdk_commit=SDK_COMMIT,
                            expected_runner_label="ubuntu-24.04",
                        )

    def test_missing_log_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            payload = valid_payload(directory)
            missing = payload["steps"][0]["stdout_log"]  # type: ignore[index]
            (directory / missing).unlink()
            summary = write_summary(directory, payload)

            with self.assertRaisesRegex(ValidationFailure, "missing evidence log"):
                evidence.validate_evidence(
                    summary_path=summary,
                    expected_platform="linux",
                    expected_sdk_commit=SDK_COMMIT,
                    expected_runner_label="ubuntu-24.04",
                )

    def test_step_reordering_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            payload = valid_payload(directory)
            steps = copy.deepcopy(payload["steps"])
            steps[0], steps[1] = steps[1], steps[0]
            payload["steps"] = steps
            summary = write_summary(directory, payload)

            with self.assertRaisesRegex(ValidationFailure, "step order"):
                evidence.validate_evidence(
                    summary_path=summary,
                    expected_platform="linux",
                    expected_sdk_commit=SDK_COMMIT,
                    expected_runner_label="ubuntu-24.04",
                )

    def test_wrong_runner_label_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory_name:
            directory = Path(directory_name)
            payload = valid_payload(directory)
            payload["host"]["runner_label"] = "windows-2025"  # type: ignore[index]
            summary = write_summary(directory, payload)

            with self.assertRaisesRegex(ValidationFailure, "runner label"):
                evidence.validate_evidence(
                    summary_path=summary,
                    expected_platform="linux",
                    expected_sdk_commit=SDK_COMMIT,
                    expected_runner_label="ubuntu-24.04",
                )


if __name__ == "__main__":
    unittest.main()
