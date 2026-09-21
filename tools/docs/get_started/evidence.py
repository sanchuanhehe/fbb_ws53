"""Validate non-HIL Get Started evidence bundles against the shared contract."""

from __future__ import annotations

import json
import re
from pathlib import Path

from tools.docs.get_started.contract import (
    ARTIFACTS,
    CHIP,
    CLI_COMMIT,
    CLI_REPOSITORY,
    CLI_VERSION,
    COMMAND_GROUPS,
    EXPECTED_IMAGE_OS_PREFIXES,
    EXPECTED_MACHINES,
    EXPECTED_RUNNER_LABELS,
    SDK_BRANCH,
    SDK_REMOTE_COMMAND,
    SDK_REPOSITORY,
    SDK_VERSION,
    TARGET,
)
from tools.docs.get_started.runner import ValidationFailure


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
        raise ValidationFailure(
            f"cannot read evidence summary {summary_path}: {error}"
        ) from error

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
