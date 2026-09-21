"""Execute the Windows/Linux non-HIL Get Started path and capture evidence."""

from __future__ import annotations

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
from typing import Sequence

from tools.docs.get_started.contract import (
    ARTIFACTS,
    CHIP,
    CLI_COMMIT,
    CLI_REPOSITORY,
    CLI_VERSION,
    COMMAND_GROUPS,
    CONFIG_PATH,
    EXPECTED_IMAGE_OS_PREFIXES,
    EXPECTED_MACHINES,
    EXPECTED_RUNNER_LABELS,
    PLATFORM_COMPILERS,
    SDK_BRANCH,
    SDK_REMOTE_COMMAND,
    SDK_REPOSITORY,
    SDK_VERSION,
    SDK_VERSION_SOURCE,
    TARGET,
    TOOLCHAIN_VERSION,
    Command,
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
    """Run the pinned non-HIL path and always write ``summary.json``."""
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
