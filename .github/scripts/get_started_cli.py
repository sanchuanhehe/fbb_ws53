#!/usr/bin/env python3
"""Single source of truth for the non-HIL CLI Get Started path.

The command groups below serve two consumers:

* ``get_started_hook.py`` injects them into the rendered MkDocs page.
* ``run`` executes the same argv on Windows or Linux in nightly CI.

This intentionally stops after a clean firmware build.  It never discovers a
serial port, flashes a board, opens a monitor, or claims Smoke/HIL coverage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform as platform_module
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


CLI_REPOSITORY = "https://gitcode.com/HiSpark/hs-fbb-cli"
CLI_COMMIT = "d0722a37e421b0844f8d28bc59dd3e2fe7bfa578"
CLI_VERSION = "1.2.1"
SDK_REPOSITORY = "https://gitcode.com/HiSpark/fbb_ws53.git"
SDK_BRANCH = "master"
SDK_VERSION = "1.10.106"
CHIP = "ws53"
TARGET = "ws53_liteos_app"
TOOLCHAIN_VERSION = "7.3.0-20240618"

CONFIG_PATH = Path(
    "build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config"
)
SDK_VERSION_SOURCE = Path("build/config/target_config/ws53/target_config.py")
ARTIFACTS = (
    Path("output/ws53/acore/ws53_liteos_app/application.elf"),
    Path(
        "output/ws53/fwpkg/pack_all_core/ws53_liteos_app/"
        "ws53_liteos_app_all_in_one.fwpkg"
    ),
)
PLATFORM_COMPILERS = {
    "linux": Path(
        "tools/bin/compiler/riscv/cc_riscv32_musl_b010/cc_riscv32_musl/"
        "libexec/gcc/riscv32-linux-musl/7.3.0/cc1"
    ),
    "windows": Path(
        "tools/bin/compiler/riscv/cc_riscv32_musl_b010/cc_riscv32_musl_win/"
        "libexec/gcc/riscv32-linux-musl/7.3.0/cc1.exe"
    ),
}
EXPECTED_RUNNER_LABELS = {
    "linux": "ubuntu-24.04",
    "windows": "windows-2025",
}
EXPECTED_MACHINES = {
    "linux": {"x86_64", "amd64"},
    "windows": {"amd64", "x86_64"},
}
EXPECTED_IMAGE_OS_PREFIXES = {
    "linux": "ubuntu24",
    "windows": "win25",
}


@dataclass(frozen=True)
class Command:
    command_id: str
    argv: tuple[str, ...]
    timeout_seconds: int
    expected_stdout: str | None = None

    @property
    def display(self) -> str:
        """Render the portable command form used by the documentation."""
        return " ".join(self.argv)


SDK_REMOTE_COMMAND = Command(
    "sdk-remote-branch",
    ("git", "ls-remote", SDK_REPOSITORY, f"refs/heads/{SDK_BRANCH}"),
    120,
    rf"^[0-9a-f]{{40}}\s+refs/heads/{re.escape(SDK_BRANCH)}$",
)


COMMAND_GROUPS: dict[str, tuple[Command, ...]] = {
    "version": (
        Command("fbb-version", ("fbb", "-V"), 30, rf"^fbb {re.escape(CLI_VERSION)}$"),
    ),
    "setup": (
        Command("fbb-setup", ("fbb", "setup", "--sdk-dir", "."), 1800),
        Command("fbb-doctor", ("fbb", "doctor"), 120),
        Command("fbb-describe", ("fbb", "describe", "--json"), 120),
    ),
    "clean-config": (
        Command(
            "target-config-clean",
            ("git", "diff", "--exit-code", "--", CONFIG_PATH.as_posix()),
            30,
        ),
    ),
    "configure": (
        Command(
            "config-sample-enable",
            ("fbb", "config", "set", "CONFIG_SAMPLE_ENABLE=y", "--target", TARGET),
            120,
        ),
        Command(
            "config-bt-disable",
            ("fbb", "config", "unset", "CONFIG_ENABLE_BT_SAMPLE", "--target", TARGET),
            120,
        ),
        Command(
            "config-peripheral-enable",
            (
                "fbb", "config", "set", "CONFIG_ENABLE_PERIPHERAL_SAMPLE=y",
                "--target", TARGET,
            ),
            120,
        ),
        Command(
            "config-helloworld-enable",
            (
                "fbb", "config", "set", "CONFIG_SAMPLE_SUPPORT_HELLOWORLD=y",
                "--target", TARGET,
            ),
            120,
        ),
    ),
    "verify-config": (
        Command(
            "verify-sample-enable",
            ("fbb", "config", "get", "CONFIG_SAMPLE_ENABLE", "--target", TARGET),
            120,
            r"^y$",
        ),
        Command(
            "verify-bt-disable",
            ("fbb", "config", "get", "CONFIG_ENABLE_BT_SAMPLE", "--target", TARGET),
            120,
            r"^n$",
        ),
        Command(
            "verify-peripheral-enable",
            (
                "fbb", "config", "get", "CONFIG_ENABLE_PERIPHERAL_SAMPLE",
                "--target", TARGET,
            ),
            120,
            r"^y$",
        ),
        Command(
            "verify-helloworld-enable",
            (
                "fbb", "config", "get", "CONFIG_SAMPLE_SUPPORT_HELLOWORLD",
                "--target", TARGET,
            ),
            120,
            r"^y$",
        ),
    ),
    "build": (
        Command("clean-build", ("fbb", "build", "--clean", TARGET), 3600),
    ),
}

GENERATED_SECTIONS = (
    "checkout",
    "sdk-platform-checks",
    *COMMAND_GROUPS.keys(),
    "artifacts",
    "artifact-checks",
)


def _marker(section: str, edge: str) -> str:
    return f"<!-- get-started-cli:{section}:{edge} -->"


def _indent(text: str, spaces: int = 4) -> str:
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" if line else "" for line in text.splitlines())


def _windows_path(path: Path) -> str:
    return ".\\" + path.as_posix().replace("/", "\\")


def _render_checkout() -> str:
    return "\n".join(
        (
            "```console",
            "git lfs install",
            f"git clone --branch {SDK_BRANCH} --single-branch {SDK_REPOSITORY}",
            "cd fbb_ws53",
            "git lfs pull",
            "```",
        )
    )


def _render_sdk_platform_checks() -> str:
    windows_compiler = _windows_path(Path("src") / PLATFORM_COMPILERS["windows"])
    linux_compiler = (Path("src") / PLATFORM_COMPILERS["linux"]).as_posix()
    windows = "\n".join(
        (
            "```powershell",
            f"$compiler = Get-Item {windows_compiler}",
            'if ($compiler.Length -lt 1MB) { throw "Git LFS objects are not hydrated" }',
            "cd src",
            "Test-Path .\\build.py",
            (
                "Select-String -Path "
                ".\\build\\config\\target_config\\ws53\\target_config.py "
                f"-Pattern 'SDK_VERSION.*{re.escape(SDK_VERSION)}'"
            ),
            "```",
        )
    )
    linux = "\n".join(
        (
            "```bash",
            f"size=$(wc -c < ./{linux_compiler})",
            'if [ "$size" -ge 1048576 ] && cd src && test -f ./build.py; then',
            '  echo "Git LFS objects: OK"',
            '  echo "SDK root: OK"',
            (
                "  grep -n "
                f"'SDK_VERSION.*{re.escape(SDK_VERSION)}' "
                "./build/config/target_config/ws53/target_config.py"
            ),
            "else",
            '  echo "SDK checkout is incomplete; stop before build" >&2',
            "  false",
            "fi",
            "```",
        )
    )
    return "\n".join(
        (
            '=== "Windows"',
            "",
            _indent(windows),
            "",
            '=== "Linux"',
            "",
            _indent(linux),
        )
    )


def _render_artifact_checks() -> str:
    windows_lines = ["```powershell"]
    windows_lines.extend(f"Test-Path {_windows_path(path)}" for path in ARTIFACTS)
    windows_lines.append("```")
    linux_lines = ["```bash"]
    linux_lines.extend(
        (
            f'test -f ./{ARTIFACTS[0].as_posix()} && echo "ELF: OK"',
            f'test -f ./{ARTIFACTS[1].as_posix()} && echo "FWPKG: OK"',
        )
    )
    linux_lines.append("```")
    return "\n".join(
        (
            '=== "Windows"',
            "",
            _indent("\n".join(windows_lines)),
            "",
            '=== "Linux"',
            "",
            _indent("\n".join(linux_lines)),
        )
    )


def render_section(section: str) -> str:
    """Render one generated Markdown section from the executable contract."""
    if section == "checkout":
        return _render_checkout()
    if section == "sdk-platform-checks":
        return _render_sdk_platform_checks()
    if section == "artifacts":
        body = "\n".join(path.as_posix() for path in ARTIFACTS)
        return f"```text\n{body}\n```"
    if section == "artifact-checks":
        return _render_artifact_checks()
    commands = COMMAND_GROUPS.get(section)
    if commands is None:
        raise KeyError(f"unknown generated section: {section}")
    body = "\n".join(command.display for command in commands)
    return f"```console\n{body}\n```"


def render_document(markdown: str) -> str:
    """Replace every generated region, failing closed on missing/duplicate markers."""
    rendered = markdown
    for section in GENERATED_SECTIONS:
        begin = _marker(section, "begin")
        end = _marker(section, "end")
        if rendered.count(begin) != 1 or rendered.count(end) != 1:
            raise ValueError(
                f"section {section!r} must contain exactly one begin and one end marker"
            )
        pattern = re.compile(
            rf"{re.escape(begin)}.*?{re.escape(end)}",
            flags=re.DOTALL,
        )
        replacement = f"{begin}\n\n{render_section(section)}\n\n{end}"
        rendered, count = pattern.subn(lambda _match: replacement, rendered)
        if count != 1:
            raise ValueError(f"could not render generated section {section!r}")
    return rendered


def validate_document_source(markdown: str) -> None:
    """Ensure commands are owned by generated regions rather than hand-copied."""
    rendered = render_document(markdown)
    for section in GENERATED_SECTIONS:
        begin = _marker(section, "begin")
        end = _marker(section, "end")
        match = re.search(
            rf"{re.escape(begin)}(?P<body>.*?){re.escape(end)}",
            markdown,
            flags=re.DOTALL,
        )
        if match is None or match.group("body").strip():
            raise ValueError(
                f"generated section {section!r} must be empty between its source markers"
            )
    for group, commands in COMMAND_GROUPS.items():
        begin = rendered.index(_marker(group, "begin"))
        end = rendered.index(_marker(group, "end"), begin)
        region = rendered[begin:end]
        for command in commands:
            if region.count(command.display) != 1:
                raise ValueError(
                    f"generated command must appear exactly once in {group}: {command.display}"
                )
            outside = rendered[:begin] + rendered[end:]
            if re.search(rf"(?m)^{re.escape(command.display)}\s*$", outside):
                raise ValueError(
                    f"generated command is also hand-written outside {group}: {command.display}"
                )


@dataclass
class StepEvidence:
    command_id: str
    argv: list[str]
    exit_code: int
    duration_seconds: float
    stdout_log: str
    stderr_log: str


class ValidationFailure(RuntimeError):
    """A deterministic failure in the non-HIL build path."""


class StepExecutionFailure(ValidationFailure):
    """A failed command that still carries its evidence record."""

    def __init__(self, message: str, evidence: StepEvidence) -> None:
        super().__init__(message)
        self.evidence = evidence


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _host_platform() -> str:
    if os.name == "nt":
        return "windows"
    if sys.platform.startswith("linux"):
        return "linux"
    return sys.platform


def _safe_log_name(command_id: str, suffix: str) -> str:
    return f"{re.sub(r'[^A-Za-z0-9_.-]+', '-', command_id)}.{suffix}.log"


def _run_command(
    command: Command,
    *,
    cwd: Path,
    evidence_dir: Path,
    environment: dict[str, str],
) -> tuple[StepEvidence, str]:
    started = time.monotonic()
    print(f"::group::{command.command_id}: {command.display}", flush=True)
    try:
        result = subprocess.run(
            list(command.argv),
            cwd=cwd,
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=command.timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        result_code = 124
        timeout_message = (
            f"command timed out after {command.timeout_seconds}s: {command.display}"
        )
        stderr = f"{stderr}\n{timeout_message}\n"
    else:
        stdout = result.stdout
        stderr = result.stderr
        result_code = result.returncode

    if stdout:
        print(stdout, end="" if stdout.endswith("\n") else "\n")
    if stderr:
        print(stderr, file=sys.stderr, end="" if stderr.endswith("\n") else "\n")
    print("::endgroup::", flush=True)

    stdout_name = _safe_log_name(command.command_id, "stdout")
    stderr_name = _safe_log_name(command.command_id, "stderr")
    (evidence_dir / stdout_name).write_text(stdout, encoding="utf-8")
    (evidence_dir / stderr_name).write_text(stderr, encoding="utf-8")
    evidence = StepEvidence(
        command_id=command.command_id,
        argv=list(command.argv),
        exit_code=result_code,
        duration_seconds=round(time.monotonic() - started, 3),
        stdout_log=stdout_name,
        stderr_log=stderr_name,
    )
    if result_code != 0:
        raise StepExecutionFailure(
            f"{command.command_id} exited {result_code}: {command.display}",
            evidence,
        )
    combined = stdout.strip()
    if command.expected_stdout and not re.fullmatch(
        command.expected_stdout, combined, flags=re.MULTILINE
    ):
        raise StepExecutionFailure(
            f"{command.command_id} output did not match {command.expected_stdout!r}: "
            f"{combined!r}",
            evidence,
        )
    return evidence, stdout


def _run_dependency(
    command_id: str,
    argv: Sequence[str],
    *,
    cwd: Path,
    evidence_dir: Path,
    environment: dict[str, str],
    timeout_seconds: int = 300,
) -> StepEvidence:
    evidence, _ = _run_command(
        Command(command_id, tuple(argv), timeout_seconds),
        cwd=cwd,
        evidence_dir=evidence_dir,
        environment=environment,
    )
    return evidence


def _validate_describe(payload: str) -> None:
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as error:
        raise ValidationFailure(f"fbb describe did not emit valid JSON: {error}") from error
    sdk = data.get("sdk") or {}
    chips = sdk.get("chips") or []
    targets = sdk.get("targets") or []
    pins = (sdk.get("requires") or {}).get("pins") or {}
    if CHIP not in chips:
        raise ValidationFailure(f"fbb describe did not report chip {CHIP!r}: {chips!r}")
    if TARGET not in targets:
        raise ValidationFailure(
            f"fbb describe did not report target {TARGET!r}: {targets!r}"
        )
    if pins.get("hcc") != TOOLCHAIN_VERSION:
        raise ValidationFailure(f"unexpected hcc pin: {pins.get('hcc')!r}")


def run_validation(
    *,
    root: Path,
    expected_platform: str,
    runner_label: str | None,
    evidence_dir: Path,
) -> int:
    root = root.resolve()
    sdk = root / "src"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    actual_platform = _host_platform()
    started_at = _utc_now()
    steps: list[StepEvidence] = []
    artifact_evidence: list[dict[str, object]] = []
    error_message: str | None = None
    status = "failed"
    sdk_commit: str | None = None

    environment = os.environ.copy()
    environment.setdefault("PYTHONUTF8", "1")
    environment.setdefault("PYTHONIOENCODING", "utf-8")
    environment.setdefault("FBB_NO_COLOR", "1")
    environment.setdefault("NO_COLOR", "1")

    original_config: bytes | None = None
    config_file = sdk / CONFIG_PATH
    try:
        if actual_platform != expected_platform:
            raise ValidationFailure(
                f"runner platform is {actual_platform!r}, expected {expected_platform!r}"
            )
        machine = platform_module.machine().casefold()
        if machine not in EXPECTED_MACHINES[expected_platform]:
            raise ValidationFailure(
                f"runner architecture is {machine!r}, expected x86_64/AMD64"
            )
        if runner_label is not None and (
            runner_label != EXPECTED_RUNNER_LABELS[expected_platform]
        ):
            raise ValidationFailure(
                f"runner label is {runner_label!r}, expected "
                f"{EXPECTED_RUNNER_LABELS[expected_platform]!r}"
            )
        image_os = os.environ.get("ImageOS")
        if runner_label is not None and (
            not image_os
            or not image_os.casefold().startswith(
                EXPECTED_IMAGE_OS_PREFIXES[expected_platform]
            )
        ):
            raise ValidationFailure(
                f"runner ImageOS is {image_os!r}, expected prefix "
                f"{EXPECTED_IMAGE_OS_PREFIXES[expected_platform]!r}"
            )
        if not (sdk / "build.py").is_file():
            raise ValidationFailure(f"invalid SDK root: {sdk}")
        if shutil.which("fbb") is None:
            raise ValidationFailure("fbb executable is not on PATH")

        steps.append(
            _run_dependency(
                "git-version", ("git", "--version"), cwd=root,
                evidence_dir=evidence_dir, environment=environment, timeout_seconds=30,
            )
        )
        remote_evidence, _ = _run_command(
            SDK_REMOTE_COMMAND,
            cwd=root,
            evidence_dir=evidence_dir,
            environment=environment,
        )
        steps.append(remote_evidence)
        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
        )
        if revision.returncode != 0 or not re.fullmatch(
            r"[0-9a-fA-F]{40}", revision.stdout.strip()
        ):
            raise ValidationFailure("could not resolve the SDK checkout commit")
        sdk_commit = revision.stdout.strip().lower()
        steps.append(
            _run_dependency(
                "git-lfs-version", ("git", "lfs", "version"), cwd=root,
                evidence_dir=evidence_dir, environment=environment, timeout_seconds=30,
            )
        )
        steps.append(
            _run_dependency(
                "git-lfs-install", ("git", "lfs", "install"), cwd=root,
                evidence_dir=evidence_dir, environment=environment, timeout_seconds=30,
            )
        )
        steps.append(
            _run_dependency(
                "git-lfs-pull", ("git", "lfs", "pull"), cwd=root,
                evidence_dir=evidence_dir, environment=environment, timeout_seconds=600,
            )
        )

        compiler = sdk / PLATFORM_COMPILERS[expected_platform]
        if not compiler.is_file() or compiler.stat().st_size < 1024 * 1024:
            raise ValidationFailure(
                f"Git LFS compiler is missing or still a pointer: {compiler}"
            )
        if expected_platform == "linux" and not os.access(compiler, os.X_OK):
            raise ValidationFailure(f"Linux compiler is not executable: {compiler}")
        version_source = sdk / SDK_VERSION_SOURCE
        if not version_source.is_file() or re.search(
            rf'SDK_VERSION=\\?"{re.escape(SDK_VERSION)}\\?"',
            version_source.read_text(encoding="utf-8"),
        ) is None:
            raise ValidationFailure(
                f"SDK version {SDK_VERSION!r} is not declared by {version_source}"
            )

        if not config_file.is_file():
            raise ValidationFailure(f"target config is missing: {config_file}")
        original_config = config_file.read_bytes()

        for group in (
            "version",
            "setup",
            "clean-config",
            "configure",
            "verify-config",
        ):
            for command in COMMAND_GROUPS[group]:
                evidence, stdout = _run_command(
                    command,
                    cwd=sdk,
                    evidence_dir=evidence_dir,
                    environment=environment,
                )
                steps.append(evidence)
                if command.command_id == "fbb-describe":
                    _validate_describe(stdout)

        build_started_ns = time.time_ns()
        for command in COMMAND_GROUPS["build"]:
            evidence, _ = _run_command(
                command,
                cwd=sdk,
                evidence_dir=evidence_dir,
                environment=environment,
            )
            steps.append(evidence)

        for relative in ARTIFACTS:
            artifact = sdk / relative
            if not artifact.is_file() or artifact.stat().st_size <= 0:
                raise ValidationFailure(f"expected artifact was not generated: {artifact}")
            if artifact.stat().st_mtime_ns < build_started_ns:
                raise ValidationFailure(f"artifact predates this build: {artifact}")
            artifact_evidence.append(
                {
                    "path": relative.as_posix(),
                    "size_bytes": artifact.stat().st_size,
                    "sha256": _sha256(artifact),
                }
            )
        status = "passed"
    except Exception as error:  # Write evidence even for unexpected failures.
        if isinstance(error, StepExecutionFailure):
            if not steps or steps[-1].command_id != error.evidence.command_id:
                steps.append(error.evidence)
        error_message = f"{type(error).__name__}: {error}"
        print(f"::error title=Get Started {expected_platform} build::{error_message}")
    finally:
        if original_config is not None:
            try:
                config_file.write_bytes(original_config)
            except OSError as restore_error:
                status = "failed"
                restore_message = f"could not restore {CONFIG_PATH}: {restore_error}"
                error_message = (
                    f"{error_message}; {restore_message}" if error_message else restore_message
                )

        summary = {
            "schema_version": 1,
            "status": status,
            "platform": expected_platform,
            "host": {
                "system": platform_module.system(),
                "release": platform_module.release(),
                "machine": platform_module.machine(),
                "python": platform_module.python_version(),
                "runner_label": runner_label,
                "runner_image_os": os.environ.get("ImageOS"),
                "runner_image_version": os.environ.get("ImageVersion"),
            },
            "started_at": started_at,
            "finished_at": _utc_now(),
            "cli": {
                "repository": CLI_REPOSITORY,
                "commit": CLI_COMMIT,
                "version": CLI_VERSION,
            },
            "sdk": {
                "documented_repository": SDK_REPOSITORY,
                "documented_branch": SDK_BRANCH,
                "version": SDK_VERSION,
                "chip": CHIP,
                "target": TARGET,
                "commit": sdk_commit,
            },
            "coverage": {
                "source_static": "not_run_by_this_script",
                "documented_repository_branch": "passed" if status == "passed" else "failed",
                "repository_checkout": (
                    "passed_by_github_actions" if status == "passed" else "failed"
                ),
                "environment": "passed" if status == "passed" else "failed",
                "configure": "passed" if status == "passed" else "failed",
                "firmware_build": "passed" if status == "passed" else "failed",
                "flash": "not_run",
                "serial_monitor": "not_run",
                "smoke": "not_run",
                "hil": "not_run",
            },
            "steps": [asdict(step) for step in steps],
            "artifacts": artifact_evidence,
            "error": error_message,
        }
        (evidence_dir / "summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if status == "passed" else 1


def _expected_step_argv() -> dict[str, list[str]]:
    expected = {
        "git-version": ["git", "--version"],
        SDK_REMOTE_COMMAND.command_id: list(SDK_REMOTE_COMMAND.argv),
        "git-lfs-version": ["git", "lfs", "version"],
        "git-lfs-install": ["git", "lfs", "install"],
        "git-lfs-pull": ["git", "lfs", "pull"],
    }
    for group in (
        "version",
        "setup",
        "clean-config",
        "configure",
        "verify-config",
        "build",
    ):
        for command in COMMAND_GROUPS[group]:
            expected[command.command_id] = list(command.argv)
    return expected


def validate_evidence(
    *,
    summary_path: Path,
    expected_platform: str,
    expected_sdk_commit: str,
    expected_runner_label: str,
) -> None:
    """Fail closed when a non-HIL evidence bundle is incomplete or overstated."""
    try:
        data = json.loads(summary_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValidationFailure(f"cannot read evidence summary {summary_path}: {error}") from error

    def require(condition: bool, message: str) -> None:
        if not condition:
            raise ValidationFailure(message)

    require(data.get("schema_version") == 1, "unexpected evidence schema_version")
    require(data.get("status") == "passed", "evidence status is not passed")
    require(data.get("platform") == expected_platform, "evidence platform mismatch")
    require(data.get("error") is None, "passed evidence must not contain an error")

    host = data.get("host") or {}
    require(
        str(host.get("machine", "")).casefold() in EXPECTED_MACHINES[expected_platform],
        "evidence machine is not x86_64/AMD64",
    )
    require(host.get("runner_label") == expected_runner_label, "runner label mismatch")
    require(
        expected_runner_label == EXPECTED_RUNNER_LABELS[expected_platform],
        "runner label does not match the canonical platform matrix",
    )
    require(host.get("runner_image_os"), "runner image OS is missing")
    require(
        str(host.get("runner_image_os")).casefold().startswith(
            EXPECTED_IMAGE_OS_PREFIXES[expected_platform]
        ),
        "runner image OS does not match the canonical platform matrix",
    )
    require(host.get("runner_image_version"), "runner image version is missing")

    cli = data.get("cli") or {}
    require(cli.get("repository") == CLI_REPOSITORY, "FBB CLI repository mismatch")
    require(cli.get("commit") == CLI_COMMIT, "FBB CLI commit mismatch")
    require(cli.get("version") == CLI_VERSION, "FBB CLI version mismatch")
    sdk = data.get("sdk") or {}
    require(sdk.get("documented_repository") == SDK_REPOSITORY, "SDK repository mismatch")
    require(sdk.get("documented_branch") == SDK_BRANCH, "SDK branch mismatch")
    require(sdk.get("version") == SDK_VERSION, "SDK version mismatch")
    require(sdk.get("chip") == CHIP, "SDK chip mismatch")
    require(sdk.get("target") == TARGET, "SDK target mismatch")
    require(
        sdk.get("commit") == expected_sdk_commit.casefold(),
        "SDK evidence commit does not match the workflow commit",
    )

    expected_coverage = {
        "source_static": "not_run_by_this_script",
        "documented_repository_branch": "passed",
        "repository_checkout": "passed_by_github_actions",
        "environment": "passed",
        "configure": "passed",
        "firmware_build": "passed",
        "flash": "not_run",
        "serial_monitor": "not_run",
        "smoke": "not_run",
        "hil": "not_run",
    }
    require(data.get("coverage") == expected_coverage, "coverage boundary mismatch")

    expected_steps = _expected_step_argv()
    steps = data.get("steps") or []
    require(isinstance(steps, list), "steps must be a list")
    require(
        [step.get("command_id") for step in steps] == list(expected_steps),
        "step order or command set differs from the canonical contract",
    )
    for step in steps:
        command_id = step["command_id"]
        require(step.get("argv") == expected_steps[command_id], f"argv mismatch: {command_id}")
        require(step.get("exit_code") == 0, f"nonzero evidence exit code: {command_id}")
        for log_key in ("stdout_log", "stderr_log"):
            log_name = step.get(log_key)
            require(isinstance(log_name, str) and log_name, f"missing {log_key}: {command_id}")
            require(
                (summary_path.parent / log_name).is_file(),
                f"missing evidence log {log_name!r}: {command_id}",
            )

    artifacts = data.get("artifacts") or []
    require(isinstance(artifacts, list), "artifacts must be a list")
    require(
        [item.get("path") for item in artifacts]
        == [path.as_posix() for path in ARTIFACTS],
        "artifact path set or order differs from the canonical contract",
    )
    for artifact in artifacts:
        require(
            isinstance(artifact.get("size_bytes"), int) and artifact["size_bytes"] > 0,
            f"artifact is empty: {artifact.get('path')}",
        )
        require(
            re.fullmatch(r"[0-9a-f]{64}", str(artifact.get("sha256", ""))) is not None,
            f"artifact SHA-256 is invalid: {artifact.get('path')}",
        )


def _default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    render_parser = subparsers.add_parser("render", help="render generated Markdown")
    render_parser.add_argument("--section", choices=GENERATED_SECTIONS)
    render_parser.add_argument(
        "--document",
        type=Path,
        help="render all marked regions in this Markdown document",
    )

    check_parser = subparsers.add_parser(
        "check-document", help="validate generated markers and ownership"
    )
    check_parser.add_argument("document", type=Path)

    subparsers.add_parser(
        "install-cli",
        help="install the exact FBB CLI revision declared by this contract",
    )

    run_parser = subparsers.add_parser(
        "run", help="execute the Windows/Linux non-HIL build path"
    )
    run_parser.add_argument("--root", type=Path, default=_default_root())
    run_parser.add_argument(
        "--platform", choices=("windows", "linux"), required=True
    )
    run_parser.add_argument(
        "--runner-label",
        choices=tuple(EXPECTED_RUNNER_LABELS.values()),
        help="GitHub-hosted runner label recorded in evidence",
    )
    run_parser.add_argument("--evidence-dir", type=Path, required=True)

    evidence_parser = subparsers.add_parser(
        "validate-evidence", help="validate a completed non-HIL evidence bundle"
    )
    evidence_parser.add_argument("--summary", type=Path, required=True)
    evidence_parser.add_argument(
        "--platform", choices=("windows", "linux"), required=True
    )
    evidence_parser.add_argument("--sdk-commit", required=True)
    evidence_parser.add_argument(
        "--runner-label", choices=tuple(EXPECTED_RUNNER_LABELS.values()), required=True
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.command == "render":
        if bool(args.section) == bool(args.document):
            raise SystemExit("render requires exactly one of --section or --document")
        if args.section:
            print(render_section(args.section))
        else:
            print(render_document(args.document.read_text(encoding="utf-8")))
        return 0
    if args.command == "check-document":
        text = args.document.read_text(encoding="utf-8")
        validate_document_source(text)
        print(
            f"PASS generated command contract: {len(COMMAND_GROUPS)} groups, "
            f"{sum(len(group) for group in COMMAND_GROUPS.values())} commands"
        )
        return 0
    if args.command == "install-cli":
        requirement = f"git+{CLI_REPOSITORY}.git@{CLI_COMMIT}"
        print(f"Installing pinned FBB CLI {CLI_VERSION} ({CLI_COMMIT})")
        return subprocess.call(
            [sys.executable, "-m", "pip", "install", requirement]
        )
    if args.command == "run":
        return run_validation(
            root=args.root,
            expected_platform=args.platform,
            runner_label=args.runner_label,
            evidence_dir=args.evidence_dir,
        )
    if args.command == "validate-evidence":
        validate_evidence(
            summary_path=args.summary,
            expected_platform=args.platform,
            expected_sdk_commit=args.sdk_commit,
            expected_runner_label=args.runner_label,
        )
        print(
            f"PASS validated {args.platform} non-HIL evidence: "
            f"{len(_expected_step_argv())} steps, {len(ARTIFACTS)} artifacts"
        )
        return 0
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
