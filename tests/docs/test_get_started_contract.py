"""Regression tests for the executable CLI Get Started contract."""

from __future__ import annotations

import unittest

from tools.docs.get_started import contract


class ContractTests(unittest.TestCase):
    def test_supported_scope_is_exact_and_non_hil(self) -> None:
        self.assertEqual(
            contract.CLI_REPOSITORY,
            "https://gitcode.com/HiSpark/hs-fbb-cli",
        )
        self.assertEqual(contract.CLI_VERSION, "1.2.1")
        self.assertEqual(contract.SDK_BRANCH, "master")
        self.assertEqual(contract.SDK_VERSION, "1.10.106")
        self.assertEqual(contract.CHIP, "ws53")
        self.assertEqual(contract.TARGET, "ws53_liteos_app")
        self.assertEqual(set(contract.PLATFORM_COMPILERS), {"windows", "linux"})

        argv = [
            argument
            for group in contract.COMMAND_GROUPS.values()
            for command in group
            for argument in command.argv
        ]
        self.assertNotIn("flash", argv)
        self.assertNotIn("monitor", argv)

    def test_generated_sections_and_command_ids_are_stable_and_unique(self) -> None:
        self.assertEqual(
            contract.GENERATED_SECTIONS,
            (
                "checkout",
                "sdk-platform-checks",
                "version",
                "setup",
                "clean-config",
                "configure",
                "verify-config",
                "build",
                "artifacts",
                "artifact-checks",
            ),
        )
        command_ids = [
            command.command_id
            for group in contract.COMMAND_GROUPS.values()
            for command in group
        ]
        self.assertEqual(len(command_ids), len(set(command_ids)))

    def test_command_display_is_the_documented_portable_form(self) -> None:
        command = contract.Command(
            "example",
            ("fbb", "build", "--clean", contract.TARGET),
            30,
        )
        self.assertEqual(command.display, "fbb build --clean ws53_liteos_app")


if __name__ == "__main__":
    unittest.main()
