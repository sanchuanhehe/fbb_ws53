"""Pure, shared contract for the CLI Get Started documentation and CI path.

This module deliberately contains no filesystem mutation, subprocess execution,
or MkDocs integration.  Documentation rendering and Windows/Linux nightly
validation both consume the immutable values declared here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


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
