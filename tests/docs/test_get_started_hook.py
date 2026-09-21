"""Tests for the narrow MkDocs adapter."""

from __future__ import annotations

import importlib.util
import os
import tempfile
import types
import unittest
from pathlib import Path

from tools.docs.get_started.contract import GENERATED_SECTIONS
from tools.docs.get_started.mkdocs_hook import on_page_markdown


def source_document() -> str:
    return "\n".join(
        f"<!-- get-started-cli:{section} -->" for section in GENERATED_SECTIONS
    ) + "\n"


def page(path: str) -> object:
    return types.SimpleNamespace(file=types.SimpleNamespace(src_uri=path))


class MkDocsHookTests(unittest.TestCase):
    def test_hook_can_be_loaded_by_file_path_outside_repo_cwd(self) -> None:
        hook_path = (
            Path(__file__).resolve().parents[2]
            / "tools"
            / "docs"
            / "get_started"
            / "mkdocs_hook.py"
        )
        spec = importlib.util.spec_from_file_location("mkdocs_arbitrary_hook", hook_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        original_cwd = Path.cwd()
        try:
            with tempfile.TemporaryDirectory() as directory:
                os.chdir(directory)
                spec.loader.exec_module(module)
        finally:
            os.chdir(original_cwd)
        self.assertTrue(callable(module.on_page_markdown))

    def test_target_page_is_rendered(self) -> None:
        result = on_page_markdown(
            source_document(),
            page("zh-CN/get-started/cli.md"),
            config=None,
            files=None,
        )

        self.assertIn("<!-- get-started-cli:checkout:begin -->", result)
        self.assertIn("fbb build --clean ws53_liteos_app", result)

    def test_other_pages_are_not_intercepted(self) -> None:
        markdown = "<!-- get-started-cli:malformed:begin -->\n"
        result = on_page_markdown(
            markdown,
            page("zh-CN/get-started/vscode.md"),
            config=None,
            files=None,
        )
        self.assertIsNone(result)

    def test_target_page_fails_closed_on_bad_source(self) -> None:
        with self.assertRaises(ValueError):
            on_page_markdown(
                "<!-- get-started-cli:checkout -->\n",
                page("zh-CN/get-started/cli.md"),
                config=None,
                files=None,
            )


if __name__ == "__main__":
    unittest.main()
