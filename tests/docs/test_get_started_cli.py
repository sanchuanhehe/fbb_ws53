"""Tests for the repository-level Get Started module entry point."""

from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.docs.get_started import __main__ as cli
from tools.docs.get_started.contract import GENERATED_SECTIONS


def source_document() -> str:
    return "\n".join(
        f"<!-- get-started-cli:{section} -->" for section in GENERATED_SECTIONS
    ) + "\n"


class CommandLineTests(unittest.TestCase):
    def test_module_entry_point_renders_a_section(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "tools.docs.get_started",
                "render",
                "--section",
                "version",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("fbb -V", result.stdout)

    def test_check_document_accepts_the_canonical_source_shape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document = Path(directory) / "cli.md"
            document.write_text(source_document(), encoding="utf-8")
            output = io.StringIO()

            with contextlib.redirect_stdout(output):
                exit_code = cli.main(["check-document", str(document)])

        self.assertEqual(exit_code, 0)
        self.assertIn("PASS generated command contract", output.getvalue())

    def test_render_requires_exactly_one_input_kind(self) -> None:
        with self.assertRaisesRegex(SystemExit, "exactly one"):
            cli.main(["render"])

        with tempfile.TemporaryDirectory() as directory:
            document = Path(directory) / "cli.md"
            document.write_text(source_document(), encoding="utf-8")
            with self.assertRaisesRegex(SystemExit, "exactly one"):
                cli.main(
                    [
                        "render",
                        "--section",
                        "version",
                        "--document",
                        str(document),
                    ]
                )

    def test_parser_keeps_the_existing_ci_subcommands(self) -> None:
        cases = (
            ("render", "--section", "version"),
            ("check-document", "cli.md"),
            ("check-source",),
            ("install-cli",),
            (
                "run",
                "--platform",
                "linux",
                "--evidence-dir",
                "evidence",
            ),
            (
                "validate-evidence",
                "--summary",
                "summary.json",
                "--platform",
                "linux",
                "--sdk-commit",
                "a" * 40,
                "--runner-label",
                "ubuntu-24.04",
            ),
        )
        for arguments in cases:
            with self.subTest(command=arguments[0]):
                self.assertEqual(cli.parse_args(arguments).command, arguments[0])


if __name__ == "__main__":
    unittest.main()
