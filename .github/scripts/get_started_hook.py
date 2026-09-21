"""Compatibility wrapper for the repository-level MkDocs hook."""

from __future__ import annotations

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.docs.get_started.mkdocs_hook import (  # noqa: E402,F401
    CLI_PAGE,
    on_page_markdown,
)
