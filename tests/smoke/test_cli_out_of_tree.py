"""WS53 CLI out-of-tree build smoke test.

This test intentionally stops after resolving the firmware package that
``fbb flash`` would use.  It does not access a serial port or a board.

Run it with the Python environment that owns the CLI under test, for example::

    $env:FBB_EXE = "<hs-fbb-cli>/.venv/Scripts/fbb.exe"
    $env:FBB_SMOKE_WORK_ROOT = "D:/fbb-smoke"  # short path on Windows
    python -m pytest tests/smoke/test_cli_out_of_tree.py -q

The SDK checkout must be clean of generated ``src/output`` content so the
test can prove that an out-of-tree build does not write back into the SDK.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import time
import tomllib
from pathlib import Path
from typing import Sequence

import pytest

from hs_fbb_cli.flash import _find_fwpkg


SDK_REPOSITORY = Path(__file__).resolve().parents[2]
DEFAULT_SDK_DIR = SDK_REPOSITORY / "src"
CHIP = "ws53"
TARGET = "ws53_liteos_app"


def _resolve_fbb() -> Path:
    configured = os.environ.get("FBB_EXE")
    candidate = Path(configured) if configured else None
    if candidate is None:
        discovered = shutil.which("fbb")
        candidate = Path(discovered) if discovered else None
    if candidate is None or not candidate.is_file():
        pytest.fail(
            "fbb executable not found; set FBB_EXE to the hs-fbb-cli "
            "executable under test"
        )
    return candidate.resolve()


def _resolve_sdk() -> Path:
    configured = os.environ.get("FBB_WS53_SDK_DIR")
    sdk_dir = Path(configured).resolve() if configured else DEFAULT_SDK_DIR
    if not (sdk_dir / "build.py").is_file():
        pytest.fail(f"invalid WS53 SDK directory: {sdk_dir}")
    return sdk_dir


def _run_fbb(
    fbb: Path,
    arguments: Sequence[str],
    *,
    cwd: Path,
    timeout: int,
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.setdefault("PYTHONUTF8", "1")
    environment.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        result = subprocess.run(
            [str(fbb), *arguments],
            cwd=cwd,
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        pytest.fail(
            f"fbb {' '.join(arguments)} timed out after {timeout}s\n"
            f"stdout:\n{error.stdout or ''}\n"
            f"stderr:\n{error.stderr or ''}"
        )
    assert result.returncode == 0, (
        f"fbb {' '.join(arguments)} failed with exit {result.returncode}\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    return result


def test_default_project_clean_build_and_flash_package_resolution(
    request: pytest.FixtureRequest,
) -> None:
    """Exercise the real WS53 template, build entry and CLI package resolver."""

    fbb = _resolve_fbb()
    sdk_dir = _resolve_sdk()
    sdk_output = sdk_dir / "output"
    assert not sdk_output.exists(), (
        f"clean SDK required: move or remove generated directory {sdk_output}"
    )

    configured_root = os.environ.get("FBB_SMOKE_WORK_ROOT")
    work_root = (
        Path(configured_root).resolve()
        if configured_root
        else Path(tempfile.gettempdir()).resolve()
    )
    work_root.mkdir(parents=True, exist_ok=True)

    # Keep the project path short: WS53 can otherwise exceed Windows object
    # path and command-line limits before CLI path shortening takes effect.
    workspace_dir = Path(tempfile.mkdtemp(prefix="f53_", dir=work_root))
    request.addfinalizer(lambda: shutil.rmtree(workspace_dir, ignore_errors=True))
    project_name = "p"
    project_dir = workspace_dir / project_name

    _run_fbb(
        fbb,
        [
            "create-project",
            project_name,
            "--path",
            str(workspace_dir),
            "--chip",
            CHIP,
            "--sdk-dir",
            str(sdk_dir),
        ],
        cwd=workspace_dir,
        timeout=60,
    )

    manifest = tomllib.loads(
        (project_dir / "fbb-project.toml").read_text(encoding="utf-8")
    )
    assert manifest["project"]["chip"] == CHIP
    assert manifest["project"]["target"] == TARGET
    assert not (project_dir / "output").exists()

    build_started_ns = time.time_ns()
    _run_fbb(
        fbb,
        ["build", "--clean", "--sdk-dir", str(sdk_dir), TARGET, "-j4"],
        cwd=project_dir,
        timeout=600,
    )

    package = (
        project_dir
        / "output"
        / CHIP
        / "fwpkg"
        / TARGET
        / f"{TARGET}_all.fwpkg"
    )
    assert package.is_file(), f"firmware package not generated: {package}"
    assert package.stat().st_size > 0
    assert package.stat().st_mtime_ns >= build_started_ns

    resolved = _find_fwpkg(project_dir, CHIP, TARGET, load_only=False)
    assert resolved is not None
    assert resolved.resolve() == package.resolve()

    assert not sdk_output.exists(), (
        f"out-of-tree build leaked generated content into SDK: {sdk_output}"
    )
