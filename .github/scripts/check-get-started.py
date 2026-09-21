#!/usr/bin/env python3
"""Compatibility entry point for the repository-level Get Started checks."""

from __future__ import annotations

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.docs.get_started.checks import main


if __name__ == "__main__":
    raise SystemExit(main())
