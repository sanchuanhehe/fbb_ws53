"""Fail-closed tests for generated Get Started Markdown."""

from __future__ import annotations

import unittest

from tools.docs.get_started.contract import COMMAND_GROUPS, GENERATED_SECTIONS
from tools.docs.get_started.render import (
    render_document,
    render_section,
    validate_document_source,
)


def placeholder(section: str) -> str:
    return f"<!-- get-started-cli:{section} -->"


def source_document() -> str:
    return "# Test\n\n" + "\n\n".join(
        placeholder(section) for section in GENERATED_SECTIONS
    ) + "\n"


class RenderTests(unittest.TestCase):
    def test_valid_source_renders_owned_boundaries_and_content(self) -> None:
        source = source_document()
        validate_document_source(source)

        rendered = render_document(source)

        for section in GENERATED_SECTIONS:
            self.assertNotIn(placeholder(section), rendered)
            self.assertEqual(
                rendered.count(f"<!-- get-started-cli:{section}:begin -->"), 1
            )
            self.assertEqual(
                rendered.count(f"<!-- get-started-cli:{section}:end -->"), 1
            )
            self.assertIn(render_section(section), rendered)

    def test_missing_placeholder_is_rejected(self) -> None:
        source = source_document().replace(placeholder("build"), "")
        with self.assertRaisesRegex(ValueError, "build"):
            validate_document_source(source)

    def test_duplicate_placeholder_is_rejected(self) -> None:
        source = source_document() + placeholder("build") + "\n"
        with self.assertRaisesRegex(ValueError, "build"):
            validate_document_source(source)

    def test_out_of_order_placeholders_are_rejected(self) -> None:
        source = source_document()
        checkout = placeholder("checkout")
        platform_checks = placeholder("sdk-platform-checks")
        source = source.replace(checkout, "__swap__", 1)
        source = source.replace(platform_checks, checkout, 1)
        source = source.replace("__swap__", platform_checks, 1)
        with self.assertRaisesRegex(ValueError, "order"):
            validate_document_source(source)

    def test_unknown_placeholder_is_rejected(self) -> None:
        source = source_document() + placeholder("mystery") + "\n"
        with self.assertRaisesRegex(ValueError, "mystery|unknown"):
            validate_document_source(source)

    def test_malformed_placeholder_is_rejected(self) -> None:
        malformed = (
            "<!-- get-started-cli:build:wat -->",
            "<!-- get-started-cli:unclosed",
            "<!-- get-started-cli -->",
            "get-started-cli:mystery",
        )
        for marker in malformed:
            with self.subTest(marker=marker):
                source = source_document() + marker + "\n"
                with self.assertRaisesRegex(ValueError, "malformed|unknown|marker"):
                    validate_document_source(source)

    def test_legacy_rendered_markers_are_rejected_in_source(self) -> None:
        source = source_document().replace(
            placeholder("build"),
            "<!-- get-started-cli:build:begin -->\n"
            "<!-- get-started-cli:build:end -->",
        )
        with self.assertRaisesRegex(ValueError, "build|rendered|marker"):
            validate_document_source(source)

    def test_placeholder_must_be_the_only_content_on_its_line(self) -> None:
        for replacement in (
            "prefix " + placeholder("build"),
            placeholder("build") + " suffix",
        ):
            with self.subTest(replacement=replacement):
                source = source_document().replace(
                    placeholder("build"), replacement
                )
                with self.assertRaisesRegex(ValueError, "line|malformed|placeholder"):
                    validate_document_source(source)

    def test_rendering_an_already_rendered_document_is_rejected(self) -> None:
        rendered = render_document(source_document())
        with self.assertRaises(ValueError):
            render_document(rendered)

    def test_hand_written_managed_command_is_rejected(self) -> None:
        command = COMMAND_GROUPS["build"][0].display
        source = source_document() + f"\n```console\n{command}\n```\n"
        with self.assertRaisesRegex(ValueError, "hand-written|outside|managed"):
            validate_document_source(source)

    def test_hand_written_non_command_content_is_rejected(self) -> None:
        managed_lines = (
            "git clone --branch master --single-branch "
            "https://gitcode.com/HiSpark/fbb_ws53.git",
            "output/ws53/acore/ws53_liteos_app/application.elf",
            "Test-Path .\\build.py",
        )
        for managed_line in managed_lines:
            with self.subTest(managed_line=managed_line):
                source = source_document() + f"\n```console\n{managed_line}\n```\n"
                with self.assertRaisesRegex(
                    ValueError, "hand-written|outside|generated content"
                ):
                    validate_document_source(source)

    def test_unknown_section_cannot_be_rendered(self) -> None:
        with self.assertRaises(KeyError):
            render_section("mystery")


if __name__ == "__main__":
    unittest.main()
