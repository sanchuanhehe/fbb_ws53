"""Unit tests for the non-HIL Get Started runner."""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import tempfile
import types
import unittest
from collections.abc import Sequence
from pathlib import Path
from unittest import mock

from tools.docs.get_started.contract import Command, TARGET, TOOLCHAIN_VERSION
from tools.docs.get_started import runner


class RunnerTests(unittest.TestCase):
    def test_run_command_captures_complete_logs(self) -> None:
        completed = types.SimpleNamespace(
            stdout="expected output\n",
            stderr="diagnostic\n",
            returncode=0,
        )
        command = Command("test/output", ("tool", "arg"), 30, r"^expected output$")
        with tempfile.TemporaryDirectory() as directory:
            evidence_dir = Path(directory)
            with mock.patch.object(runner.subprocess, "run", return_value=completed):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                    io.StringIO()
                ):
                    evidence, stdout = runner._run_command(
                        command,
                        cwd=evidence_dir,
                        evidence_dir=evidence_dir,
                        environment={"NO_COLOR": "1"},
                    )

            self.assertEqual(stdout, "expected output\n")
            self.assertEqual(evidence.exit_code, 0)
            self.assertEqual(
                (evidence_dir / evidence.stdout_log).read_text(encoding="utf-8"),
                "expected output\n",
            )
            self.assertEqual(
                (evidence_dir / evidence.stderr_log).read_text(encoding="utf-8"),
                "diagnostic\n",
            )

    def test_run_command_preserves_evidence_on_nonzero_exit(self) -> None:
        completed = types.SimpleNamespace(stdout="", stderr="failed\n", returncode=7)
        command = Command("failed-step", ("tool",), 30)
        with tempfile.TemporaryDirectory() as directory:
            evidence_dir = Path(directory)
            with mock.patch.object(runner.subprocess, "run", return_value=completed):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                    io.StringIO()
                ):
                    with self.assertRaises(runner.StepExecutionFailure) as raised:
                        runner._run_command(
                            command,
                            cwd=evidence_dir,
                            evidence_dir=evidence_dir,
                            environment={},
                        )

            self.assertEqual(raised.exception.evidence.exit_code, 7)
            self.assertTrue(
                (evidence_dir / raised.exception.evidence.stderr_log).is_file()
            )

    def test_timeout_fails_closed_with_exit_124_and_logs(self) -> None:
        command = Command("slow-step", ("tool",), 1)
        timeout = subprocess.TimeoutExpired(
            command.argv,
            command.timeout_seconds,
            output=b"partial",
            stderr=b"waiting",
        )
        with tempfile.TemporaryDirectory() as directory:
            evidence_dir = Path(directory)
            with mock.patch.object(runner.subprocess, "run", side_effect=timeout):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(
                    io.StringIO()
                ):
                    with self.assertRaises(runner.StepExecutionFailure) as raised:
                        runner._run_command(
                            command,
                            cwd=evidence_dir,
                            evidence_dir=evidence_dir,
                            environment={},
                        )

            self.assertEqual(raised.exception.evidence.exit_code, 124)
            stderr = (
                evidence_dir / raised.exception.evidence.stderr_log
            ).read_text(encoding="utf-8")
            self.assertIn("timed out", stderr)

    def test_describe_requires_chip_target_and_toolchain_pin(self) -> None:
        payload = json.dumps(
            {
                "sdk": {
                    "chips": ["ws53"],
                    "targets": [TARGET],
                    "requires": {"pins": {"hcc": TOOLCHAIN_VERSION}},
                }
            }
        )
        runner._validate_describe(payload)

        invalid = json.dumps(
            {
                "sdk": {
                    "chips": ["ws53"],
                    "targets": [TARGET],
                    "requires": {"pins": {"hcc": "wrong"}},
                }
            }
        )
        with self.assertRaisesRegex(runner.ValidationFailure, "hcc"):
            runner._validate_describe(invalid)

    def test_platform_mismatch_writes_failed_non_hil_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence_dir = root / "evidence"
            with mock.patch.object(runner, "_host_platform", return_value="windows"):
                with mock.patch.object(runner.subprocess, "run") as run:
                    with contextlib.redirect_stdout(io.StringIO()):
                        result = runner.run_validation(
                            root=root,
                            expected_platform="linux",
                            runner_label=None,
                            evidence_dir=evidence_dir,
                        )

            run.assert_not_called()
            self.assertEqual(result, 1)
            summary = json.loads(
                (evidence_dir / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(summary["status"], "failed")
            self.assertEqual(summary["platform"], "linux")
            self.assertEqual(summary["coverage"]["flash"], "not_run")
            self.assertEqual(summary["coverage"]["serial_monitor"], "not_run")
            self.assertEqual(summary["coverage"]["smoke"], "not_run")
            self.assertEqual(summary["coverage"]["hil"], "not_run")

    def test_command_failure_restores_the_original_target_config(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sdk = root / "src"
            evidence_dir = root / "evidence"
            (sdk / "build.py").parent.mkdir(parents=True)
            (sdk / "build.py").write_text("# test\n", encoding="utf-8")

            compiler = sdk / runner.PLATFORM_COMPILERS["linux"]
            compiler.parent.mkdir(parents=True)
            compiler.write_bytes(b"x" * (1024 * 1024))
            compiler.chmod(0o755)

            version_source = sdk / runner.SDK_VERSION_SOURCE
            version_source.parent.mkdir(parents=True, exist_ok=True)
            version_source.write_text(
                f'SDK_VERSION="{runner.SDK_VERSION}"\n', encoding="utf-8"
            )
            config_file = sdk / runner.CONFIG_PATH
            config_file.parent.mkdir(parents=True, exist_ok=True)
            original_config = b"original target config\n"
            config_file.write_bytes(original_config)

            def dependency(
                command_id: str,
                argv: Sequence[str],
                **_kwargs: object,
            ) -> runner.StepEvidence:
                return runner.StepEvidence(
                    command_id, list(argv), 0, 0.0, "stdout.log", "stderr.log"
                )

            def command(
                specification: Command,
                **_kwargs: object,
            ) -> tuple[runner.StepEvidence, str]:
                record = runner.StepEvidence(
                    specification.command_id,
                    list(specification.argv),
                    0,
                    0.0,
                    "stdout.log",
                    "stderr.log",
                )
                if specification.command_id == "fbb-describe":
                    payload = json.dumps(
                        {
                            "sdk": {
                                "chips": ["ws53"],
                                "targets": [TARGET],
                                "requires": {"pins": {"hcc": TOOLCHAIN_VERSION}},
                            }
                        }
                    )
                    return record, payload
                if specification.command_id == "config-sample-enable":
                    config_file.write_bytes(b"mutated target config\n")
                    raise runner.StepExecutionFailure("forced failure", record)
                return record, ""

            revision = types.SimpleNamespace(returncode=0, stdout="a" * 40)
            with (
                mock.patch.object(runner, "_host_platform", return_value="linux"),
                mock.patch.object(runner.platform_module, "machine", return_value="x86_64"),
                mock.patch.object(runner.shutil, "which", return_value="/test/fbb"),
                mock.patch.object(runner, "_run_dependency", side_effect=dependency),
                mock.patch.object(runner, "_run_command", side_effect=command),
                mock.patch.object(runner.subprocess, "run", return_value=revision),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                result = runner.run_validation(
                    root=root,
                    expected_platform="linux",
                    runner_label=None,
                    evidence_dir=evidence_dir,
                )

            self.assertEqual(result, 1)
            self.assertEqual(config_file.read_bytes(), original_config)
            summary = json.loads(
                (evidence_dir / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(summary["status"], "failed")
            self.assertIn("forced failure", summary["error"])


if __name__ == "__main__":
    unittest.main()
