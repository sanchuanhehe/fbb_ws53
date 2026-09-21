"""MkDocs hook that renders the executable CLI Get Started contract."""

from __future__ import annotations

from get_started_cli import render_document


CLI_PAGE = "zh-CN/get-started/cli.md"


def on_page_markdown(markdown: str, page, **_kwargs) -> str | None:
    if page.file.src_uri != CLI_PAGE:
        return None
    return render_document(markdown)
