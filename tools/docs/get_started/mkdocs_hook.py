"""MkDocs adapter for the executable CLI Get Started contract."""

from __future__ import annotations

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.docs.get_started.render import render_document  # noqa: E402


CLI_PAGE = "zh-CN/get-started/cli.md"


def on_page_markdown(markdown: str, page, **_kwargs) -> str | None:
    if page.file.src_uri != CLI_PAGE:
        return None
    return render_document(markdown)
