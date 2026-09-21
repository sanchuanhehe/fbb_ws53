#!/usr/bin/env python3
"""Compatibility entry point for ``python -m tools.docs.get_started``.

New callers should import the repository package or invoke its module entry
point. This wrapper remains temporarily so existing local commands do not
break during the migration.
"""

from __future__ import annotations

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.docs.get_started import *  # noqa: E402,F403
from tools.docs.get_started.__main__ import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
