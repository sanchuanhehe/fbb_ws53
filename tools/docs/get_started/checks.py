#!/usr/bin/env python3
"""Offline, deterministic source checks for the WS53 Get Started path.

This gate intentionally verifies documentation structure and mappings to files
that are present in the checkout.  It does not build firmware, flash a board,
open a serial port, or claim Smoke/HIL coverage.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable

from tools.docs.get_started import contract as cli_contract
from tools.docs.get_started.render import render_document, validate_document_source


GET_STARTED = PurePosixPath("docs/zh-CN/get-started")
INDEX = GET_STARTED / "index.md"
CLI = GET_STARTED / "cli.md"
VSCODE = GET_STARTED / "vscode.md"
EXPECTED_PAGES = (INDEX, CLI, VSCODE)
WORKFLOW = PurePosixPath(".github/workflows/docs-pages.yml")

TARGET = cli_contract.TARGET
SDK_VERSION = cli_contract.SDK_VERSION
TOOLCHAIN_VERSION = cli_contract.TOOLCHAIN_VERSION
ELF_PATH, FWPKG_PATH = (path.as_posix() for path in cli_contract.ARTIFACTS)

TARGET_JSON = PurePosixPath(
    f"src/build/config/target_config/{cli_contract.CHIP}/{cli_contract.CHIP}.json"
)
TARGET_CONFIG = PurePosixPath("src") / PurePosixPath(
    cli_contract.SDK_VERSION_SOURCE.as_posix()
)
DEFAULT_CONFIG = PurePosixPath("src") / PurePosixPath(
    cli_contract.CONFIG_PATH.as_posix()
)
APP_KCONFIG = PurePosixPath("src/application/Kconfig")
SAMPLES_KCONFIG = PurePosixPath("src/application/samples/Kconfig")
PERIPHERAL_KCONFIG = PurePosixPath(
    "src/application/samples/peripheral/Kconfig"
)
PERIPHERAL_CMAKE = PurePosixPath(
    "src/application/samples/peripheral/CMakeLists.txt"
)
HELLO_SOURCE = PurePosixPath(
    "src/application/samples/peripheral/helloworld/helloworld.c"
)

FBB_CLI_URL = cli_contract.CLI_REPOSITORY
GIT_URL = "https://git-scm.com/downloads/"
GIT_LFS_URL = "https://git-lfs.com/"
VSCODE_URL = "https://code.visualstudio.com/Download"
DEV_DRIVE_URL = "https://learn.microsoft.com/windows/dev-drive/"
WSL_URL = "https://learn.microsoft.com/windows/wsl/filesystems"


class CheckFailure(AssertionError):
    """A human-readable gate failure."""


@dataclass(frozen=True)
class Check:
    check_id: str
    label: str
    run: Callable[[], str]


class Repository:
    def __init__(self, root: Path) -> None:
        self.root = root

    def path(self, relative: PurePosixPath | str) -> Path:
        parts = PurePosixPath(relative).parts
        return self.root.joinpath(*parts)

    def read(self, relative: PurePosixPath | str) -> str:
        path = self.path(relative)
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            raise CheckFailure(f"cannot read {PurePosixPath(relative)}: {error}") from error

    def require_exact_path(self, relative: PurePosixPath | str) -> Path:
        """Require a path with exact component casing on every host platform."""
        relative = PurePosixPath(relative)
        if relative.is_absolute() or ".." in relative.parts:
            raise CheckFailure(f"path must stay inside the repository: {relative}")

        current = self.root
        for part in relative.parts:
            try:
                children = {child.name: child for child in current.iterdir()}
            except OSError as error:
                raise CheckFailure(f"cannot inspect {relative}: {error}") from error
            if part not in children:
                case_matches = sorted(
                    name for name in children if name.casefold() == part.casefold()
                )
                if case_matches:
                    raise CheckFailure(
                        f"path case mismatch in {relative}: expected {part!r}, "
                        f"found {case_matches[0]!r}"
                    )
                raise CheckFailure(f"missing repository path: {relative}")
            current = children[part]
        return current


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def require_contains(text: str, needle: str, context: str) -> None:
    require(needle in text, f"{context} does not contain {needle!r}")


def markdown_parts(text: str, page: PurePosixPath) -> tuple[str, str]:
    lines = text.splitlines()
    require(lines and lines[0] == "---", f"{page} has no opening front-matter marker")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise CheckFailure(f"{page} has no closing front-matter marker") from error
    return "\n".join(lines[1:end]), "\n".join(lines[end + 1 :])


def scalar(front_matter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", front_matter)
    return match.group(1).strip("\"'") if match else None


def nested_scalar(front_matter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s+{re.escape(key)}:\s*(.*?)\s*$", front_matter)
    return match.group(1).strip("\"'") if match else None


def front_list(front_matter: str, key: str) -> list[str]:
    lines = front_matter.splitlines()
    start: int | None = None
    base_indent = 0
    for index, line in enumerate(lines):
        match = re.match(rf"^(\s*){re.escape(key)}:\s*$", line)
        if match:
            start = index + 1
            base_indent = len(match.group(1))
            break
    if start is None:
        return []

    values: list[str] = []
    for line in lines[start:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= base_indent:
            break
        match = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if match and indent == base_indent + 2:
            values.append(match.group(1).strip("\"'"))
    return values


def metadata_urls(front_matter: str) -> set[str]:
    return set(re.findall(r"(?m)^\s+url:\s*(\S+)\s*$", front_matter))


def section(text: str, heading: str, level: int = 2) -> str:
    marker = "#" * level
    match = re.search(
        rf"(?ms)^{re.escape(marker)}\s+{re.escape(heading)}\s*$\n"
        rf"(.*?)(?=^#{{1,{level}}}\s+|\Z)",
        text,
    )
    if not match:
        raise CheckFailure(f"missing section {marker} {heading}")
    return match.group(1)


def kconfig_block(text: str, symbol: str) -> str:
    match = re.search(
        rf"(?ms)^config\s+{re.escape(symbol)}\s*$\n(.*?)(?=^config\s+|\Z)",
        text,
    )
    if not match:
        raise CheckFailure(f"missing Kconfig symbol {symbol}")
    return match.group(1)


def normalized_repo_path(value: str) -> str:
    value = value.replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return value


def check_inputs(repo: Repository) -> str:
    required = (
        "mkdocs.yml",
        ".github/mkdocs_base.yml",
        *EXPECTED_PAGES,
        TARGET_JSON,
        TARGET_CONFIG,
        DEFAULT_CONFIG,
        APP_KCONFIG,
        SAMPLES_KCONFIG,
        PERIPHERAL_KCONFIG,
        PERIPHERAL_CMAKE,
        HELLO_SOURCE,
        "tools/__init__.py",
        "tools/docs/__init__.py",
        "tools/docs/get_started/__init__.py",
        "tools/docs/get_started/__main__.py",
        "tools/docs/get_started/contract.py",
        "tools/docs/get_started/render.py",
        "tools/docs/get_started/runner.py",
        "tools/docs/get_started/evidence.py",
        "tools/docs/get_started/checks.py",
        "tools/docs/get_started/mkdocs_hook.py",
    )
    for path in required:
        resolved = repo.require_exact_path(path)
        require(resolved.is_file(), f"required input is not a regular file: {path}")
    return f"{len(required)}/{len(required)} required inputs exist with exact casing"


def check_page_budget(repo: Repository) -> str:
    get_started = repo.require_exact_path(GET_STARTED)
    actual = sorted(
        PurePosixPath(path.relative_to(repo.root).as_posix())
        for path in get_started.rglob("*.md")
    )
    expected = sorted(EXPECTED_PAGES)
    require(
        actual == expected,
        "Get Started Markdown page set differs from the approved budget: "
        f"expected {[str(path) for path in expected]}, "
        f"found {[str(path) for path in actual]}",
    )

    cli_text = repo.read(CLI)
    vscode_text = repo.read(VSCODE)
    cli_steps = re.findall(r"(?m)^##\s+([1-9][0-9]*)\.\s+", cli_text)
    vscode_steps = re.findall(
        r"(?m)^###\s+步骤([一二三四五六七八九十]+)[：:]", vscode_text
    )
    require(cli_steps == [str(index) for index in range(1, 8)],
            f"CLI main steps must be 1..7, found {cli_steps}")
    require(
        vscode_steps == list("一二三四五六七"),
        f"VS Code main steps must be 一..七, found {vscode_steps}",
    )

    cli_prerequisites = re.findall(
        r"(?m)^([1-9][0-9]*)\.\s+", section(cli_text, "前置条件")
    )
    vscode_prerequisites = re.findall(
        r"(?m)^([1-9][0-9]*)\.\s+", section(vscode_text, "前置条件")
    )
    require(cli_prerequisites == list("12345"),
            f"CLI prerequisite budget is not exactly 5: {cli_prerequisites}")
    require(vscode_prerequisites == list("12345"),
            f"VS Code prerequisite budget is not exactly 5: {vscode_prerequisites}")

    for label, text in (("CLI", cli_text), ("VS Code", vscode_text)):
        require(
            "暂不承诺完成时间" in text or re.search(r"(?:不超过|≤)\s*30\s*分钟", text),
            f"{label} must either keep the unverified time boundary or state the <=30 minute budget",
        )
    return "3 pages; CLI 7 steps/5 prerequisites; VS Code 7 steps/5 prerequisites"


def check_quick_start_removed(repo: Repository) -> str:
    retired = GET_STARTED / "quick-start.md"
    require(not repo.path(retired).exists(), f"retired page still exists: {retired}")
    get_started = repo.require_exact_path(GET_STARTED)
    retired_names = sorted(
        path.relative_to(repo.root).as_posix()
        for path in get_started.rglob("quick-start.md")
    )
    require(not retired_names, f"retired quick-start pages still exist: {retired_names}")

    docs_root = repo.require_exact_path("docs")
    source_paths = [repo.path("mkdocs.yml"), *sorted(docs_root.rglob("*.md"))]
    references = [
        path.relative_to(repo.root).as_posix()
        for path in source_paths
        if "quick-start.md" in path.read_text(encoding="utf-8")
    ]
    require(
        not references,
        f"retired quick-start.md still has references: {references}",
    )
    return "quick-start.md is absent and unreferenced"


def check_navigation(repo: Repository) -> str:
    mkdocs = repo.read("mkdocs.yml")
    require_contains(mkdocs, "INHERIT: .github/mkdocs_base.yml", "mkdocs.yml")
    lines = mkdocs.splitlines()
    starts = [
        index for index, line in enumerate(lines) if line == "  - 快速入门:"
    ]
    require(len(starts) == 1, f"expected one 快速入门 nav entry, found {len(starts)}")
    start = starts[0]
    end = next(
        (index for index in range(start + 1, len(lines))
         if re.match(r"^  - \S", lines[index])),
        len(lines),
    )
    nav_block = "\n".join(lines[start:end])
    paths = re.findall(r"zh-CN/get-started/[A-Za-z0-9_-]+\.md", nav_block)
    expected = [str(path).removeprefix("docs/") for path in EXPECTED_PAGES]
    require(paths == expected, f"快速入门 nav must be {expected}, found {paths}")
    all_get_started_paths = re.findall(
        r"zh-CN/get-started/[A-Za-z0-9_/-]+\.md", mkdocs
    )
    require(
        all_get_started_paths == expected,
        f"mkdocs.yml must contain only the approved Get Started targets: {all_get_started_paths}",
    )
    for path in expected:
        require(
            mkdocs.count(path) == 1,
            f"Get Started nav target must appear exactly once: {path}",
        )
    return "one 快速入门 nav entry routes to index, CLI, and VS Code exactly once"


def check_entry_branch(repo: Repository) -> str:
    index_text = repo.read(INDEX)
    front, body = markdown_parts(index_text, INDEX)
    require(scalar(front, "doc_type") == "tutorial", "entry doc_type must be tutorial")
    require_contains(body, "环境准备、配置、构建、烧录和运行验证都属于 Get Started", str(INDEX))
    require_contains(body, "只选择一个页面", str(INDEX))
    links = re.findall(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)", body)
    require(links == ["cli.md", "vscode.md"],
            f"entry must expose only CLI and VS Code tutorial links, found {links}")
    require(body.count("选择一次操作方式") == 1,
            "entry must describe exactly one development-mode decision")
    require("(vscode.md" not in repo.read(CLI), "CLI tutorial must not branch to VS Code")
    require("(cli.md" not in repo.read(VSCODE), "VS Code tutorial must not branch to CLI")
    return "one entry decision exposes two mutually exclusive, self-contained tutorials"


def check_metadata(repo: Repository) -> str:
    expected_hosts = {
        INDEX: ("Windows 10/11 x86_64", "Linux x86_64"),
        CLI: ("Windows 10/11 x86_64", "Linux x86_64"),
        VSCODE: ("Windows 10/11 x86_64",),
    }
    expected_verification_levels = {
        INDEX: "static",
        CLI: "build",
        VSCODE: "static",
    }
    for page in EXPECTED_PAGES:
        front, _ = markdown_parts(repo.read(page), page)
        require(scalar(front, "title"), f"{page} has no title")
        require(scalar(front, "doc_type") == "tutorial", f"{page} doc_type must be tutorial")
        require(
            scalar(front, "product") == cli_contract.CHIP.upper(),
            f"{page} product must be {cli_contract.CHIP.upper()}",
        )
        require(scalar(front, "status") == "draft", f"{page} status must remain draft")
        require(scalar(front, "owner") == "WS53 SDK Maintainers", f"{page} owner changed or is missing")
        expected_level = expected_verification_levels[page]
        require(scalar(front, "verification_level") == expected_level,
                f"{page} verification_level must be {expected_level}")
        require(nested_scalar(front, "sdk") == SDK_VERSION,
                f"{page} applies_to.sdk must be {SDK_VERSION}")
        require(nested_scalar(front, "branch") == cli_contract.SDK_BRANCH,
                f"{page} applies_to.branch must be {cli_contract.SDK_BRANCH}")
        require(nested_scalar(front, "target") == TARGET,
                f"{page} applies_to.target must be {TARGET}")
        for host in expected_hosts[page]:
            require_contains(front, host, f"{page} host scope")
        if page == VSCODE:
            host_lines = front_list(front, "host")
            require(not host_lines, "VS Code host must remain a single Windows scalar")
    return "3/3 pages keep explicit scope; CLI=build, entry/VS Code=static"


def check_cli_tabs(repo: Repository) -> str:
    base = repo.read(".github/mkdocs_base.yml")
    cli = render_document(repo.read(CLI))
    require_contains(base, "- content.tabs.link", ".github/mkdocs_base.yml")
    labels = re.findall(r'(?m)^===\s+"([^"]+)"\s*$', cli)
    require(labels, "CLI page has no operating-system tab groups")
    require(len(labels) % 2 == 0, f"CLI tab count must be even, found {len(labels)}")
    pairs = [labels[index:index + 2] for index in range(0, len(labels), 2)]
    require(
        all(pair == ["Windows", "Linux"] for pair in pairs),
        f"every CLI tab group must be Windows/Linux in that order, found {pairs}",
    )
    require_contains(cli, "其他同名标签会自动切换到同一系统", str(CLI))
    return f"content.tabs.link enabled; {len(pairs)} Windows/Linux groups use identical labels"


def check_source_refs(repo: Repository) -> str:
    expected_critical = {
        CLI: {
            "tools/docs/get_started/contract.py",
            "tools/docs/get_started/render.py",
            "tools/docs/get_started/runner.py",
            "tools/docs/get_started/evidence.py",
            "tools/docs/get_started/mkdocs_hook.py",
            ".github/workflows/docs-pages.yml",
            str(TARGET_JSON), str(DEFAULT_CONFIG), str(APP_KCONFIG),
            str(SAMPLES_KCONFIG), str(PERIPHERAL_KCONFIG), str(HELLO_SOURCE),
        },
        VSCODE: {
            str(TARGET_JSON), str(DEFAULT_CONFIG), str(APP_KCONFIG),
            str(SAMPLES_KCONFIG), str(PERIPHERAL_KCONFIG), str(HELLO_SOURCE),
        },
    }
    total = 0
    for page in EXPECTED_PAGES:
        front, _ = markdown_parts(repo.read(page), page)
        refs = front_list(front, "source_refs")
        require(refs, f"{page} has no source_refs")
        require(len(refs) == len(set(refs)), f"{page} has duplicate source_refs")
        for value in refs:
            resolved = repo.require_exact_path(value)
            require(resolved.is_file(), f"{page} source_ref is not a regular file: {value}")
            total += 1
        if page in expected_critical:
            missing = sorted(expected_critical[page] - set(refs))
            require(not missing, f"{page} is missing critical source_refs: {missing}")
    return f"{total}/{total} source_refs resolve with exact casing"


def check_target_mapping(repo: Repository) -> str:
    try:
        config = json.loads(repo.read(TARGET_JSON))
    except json.JSONDecodeError as error:
        raise CheckFailure(f"{TARGET_JSON} is invalid JSON: {error}") from error

    require(
        config.get("chipName") == cli_contract.CHIP,
        f"ws53.json chipName must be {cli_contract.CHIP}",
    )
    require(
        config.get("board") == cli_contract.CHIP,
        f"ws53.json board must be {cli_contract.CHIP}",
    )
    min_cli_version = config.get("requires", {}).get("min_cli_version")
    require(
        isinstance(min_cli_version, str) and bool(min_cli_version.strip()),
        "ws53.json min_cli_version must be a non-empty string",
    )
    require(
        {item.get("name"): item.get("version") for item in config["requires"]["toolchains"]}
        == {"hcc": TOOLCHAIN_VERSION},
        "ws53.json toolchain declaration changed",
    )
    require(config.get("compile", {}).get("custom_build_command") == TARGET,
            f"ws53.json build command must be {TARGET}")
    require(config.get("target_default") == "WS53-LITEOS-APP",
            "ws53.json target_default must be WS53-LITEOS-APP")
    nested = config["target"]["WS53"]["WS53-LITEOS-APP"]["cmake"]
    require(nested["build"]["build_argv"] == TARGET,
            f"VS Code build target must map to {TARGET}")
    require(nested["kconfig"]["menu_config_build_target"] == TARGET,
            f"VS Code Kconfig target must map to {TARGET}")
    require(
        re.search(rf'SDK_VERSION=\\?"{re.escape(SDK_VERSION)}\\?"', repo.read(TARGET_CONFIG)),
        f"target_config.py does not declare SDK_VERSION {SDK_VERSION}",
    )
    for page in EXPECTED_PAGES:
        text = repo.read(page)
        require_contains(text, TARGET, str(page))
        require_contains(text, SDK_VERSION, str(page))
    for page in (CLI, VSCODE):
        text = repo.read(page)
        require_contains(text, TOOLCHAIN_VERSION, str(page))
    cli_front, _ = markdown_parts(repo.read(CLI), CLI)
    cli_scope = nested_scalar(cli_front, "cli") or ""
    require_contains(cli_scope, cli_contract.CLI_VERSION, f"{CLI} applies_to.cli")
    require_contains(cli_scope, min_cli_version, f"{CLI} applies_to.cli")
    return (
        f"SDK {SDK_VERSION}, Target {TARGET}, CLI validated {cli_contract.CLI_VERSION} "
        f"(SDK minimum {min_cli_version}), hcc {TOOLCHAIN_VERSION} agree"
    )


def check_kconfig_mapping(repo: Repository) -> str:
    sample_enable = kconfig_block(repo.read(APP_KCONFIG), "SAMPLE_ENABLE")
    bt_enable = kconfig_block(repo.read(SAMPLES_KCONFIG), "ENABLE_BT_SAMPLE")
    peripheral_enable = kconfig_block(repo.read(SAMPLES_KCONFIG), "ENABLE_PERIPHERAL_SAMPLE")
    hello_enable = kconfig_block(repo.read(PERIPHERAL_KCONFIG), "SAMPLE_SUPPORT_HELLOWORLD")

    require_contains(sample_enable, "default n", "SAMPLE_ENABLE")
    require_contains(bt_enable, "depends on SAMPLE_ENABLE", "ENABLE_BT_SAMPLE")
    require_contains(peripheral_enable, "depends on SAMPLE_ENABLE", "ENABLE_PERIPHERAL_SAMPLE")
    require_contains(hello_enable, "depends on ENABLE_PERIPHERAL_SAMPLE", "SAMPLE_SUPPORT_HELLOWORLD")

    default_config = repo.read(DEFAULT_CONFIG)
    require(re.search(r"(?m)^CONFIG_SAMPLE_ENABLE=y$", default_config) is not None,
            "default target config must enable SAMPLE_ENABLE")
    require(re.search(r"(?m)^CONFIG_ENABLE_BT_SAMPLE=y$", default_config) is not None,
            "default target config must enable ENABLE_BT_SAMPLE")
    require(re.search(r"(?m)^# CONFIG_ENABLE_PERIPHERAL_SAMPLE is not set$", default_config) is not None,
            "default target config must leave ENABLE_PERIPHERAL_SAMPLE disabled")

    cli = render_document(repo.read(CLI))
    cli_commands = tuple(
        command.display for command in cli_contract.COMMAND_GROUPS["configure"]
    )
    for command in cli_commands:
        require(cli.count(command) == 1, f"CLI config command must occur once: {command}")

    vscode = repo.read(VSCODE)
    for line in (
        "CONFIG_SAMPLE_ENABLE=y",
        "# CONFIG_ENABLE_BT_SAMPLE is not set",
        "CONFIG_ENABLE_PERIPHERAL_SAMPLE=y",
        "CONFIG_SAMPLE_SUPPORT_HELLOWORLD=y",
    ):
        require_contains(vscode, line, str(VSCODE))
    return "4 documented config transitions match Kconfig dependencies and target defaults"


def check_executable_cli_contract(repo: Repository) -> str:
    cli_source = repo.read(CLI)
    try:
        validate_document_source(cli_source)
        rendered = render_document(cli_source)
    except (KeyError, ValueError) as error:
        raise CheckFailure(f"invalid generated CLI contract: {error}") from error

    require_contains(cli_source, cli_contract.CLI_COMMIT[:7], str(CLI))

    base = repo.read(".github/mkdocs_base.yml")
    require(
        re.search(
            r"(?m)^hooks:\s*$\n(?:^[ \t]+.*\n)*?^  - tools/docs/get_started/mkdocs_hook\.py\s*$",
            base,
        ) is not None,
        "MkDocs does not register tools/docs/get_started/mkdocs_hook.py",
    )
    hook = repo.read("tools/docs/get_started/mkdocs_hook.py")
    require_contains(
        hook,
        "from tools.docs.get_started.render import render_document",
        "Get Started hook",
    )
    require_contains(hook, 'CLI_PAGE = "zh-CN/get-started/cli.md"', "Get Started hook")
    require_contains(hook, "return render_document(markdown)", "Get Started hook")
    for group, commands in cli_contract.COMMAND_GROUPS.items():
        for command in commands:
            require(
                len(re.findall(rf"(?m)^{re.escape(command.display)}\s*$", rendered)) == 1,
                f"rendered CLI page must contain one {group} command: {command.display}",
            )
    for artifact in cli_contract.ARTIFACTS:
        require_contains(rendered, artifact.as_posix(), "rendered CLI artifacts")
    return (
        f"{len(cli_contract.GENERATED_SECTIONS)} generated sections, "
        f"{len(cli_contract.COMMAND_GROUPS)} executable groups, and "
        f"{sum(len(group) for group in cli_contract.COMMAND_GROUPS.values())} "
        "executable commands share one source"
    )


def check_ci_matrix(repo: Repository) -> str:
    workflow = repo.read(WORKFLOW)
    try:
        build_job = workflow.split("\n  get_started_build:\n", 1)[1].split(
            "\n  nightly_result:\n", 1
        )[0]
        nightly_job = workflow.split("\n  nightly_result:\n", 1)[1].split(
            "\n  deploy:\n", 1
        )[0]
    except (IndexError, ValueError) as error:
        raise CheckFailure("workflow is missing a Get Started or nightly job") from error

    matrix_entries = re.findall(
        r"(?m)^\s+- label:\s*(\S+)\s*$\n"
        r"\s+platform:\s*(\S+)\s*$\n"
        r"\s+runner:\s*(\S+)\s*$",
        build_job,
    )
    expected_entries = [
        (platform.title(), platform, runner)
        for platform, runner in cli_contract.EXPECTED_RUNNER_LABELS.items()
    ]
    require(
        matrix_entries == expected_entries,
        "Get Started runner matrix differs from the executable contract: "
        f"expected {expected_entries!r}, found {matrix_entries!r}",
    )
    for command in ("install-cli", "run", "validate-evidence"):
        require_contains(
            build_job,
            f"python -m tools.docs.get_started {command}",
            str(WORKFLOW),
        )
    require_contains(nightly_job, "- get_started_build", str(WORKFLOW))
    matrix_summary = " and ".join(
        f"{label}/{runner}" for label, _platform, runner in expected_entries
    )
    return f"{matrix_summary} share the module runner"


def check_artifact_mapping(repo: Repository) -> str:
    config = json.loads(repo.read(TARGET_JSON))
    elf = normalized_repo_path(config["debug"]["elf_path"])
    fwpkg = normalized_repo_path(config["upload"]["bin_path"])
    nested = config["target"]["WS53"]["WS53-LITEOS-APP"]["cmake"]
    nested_fwpkg = normalized_repo_path(nested["upload"]["upload_partitions"])
    require(elf == ELF_PATH, f"ws53.json ELF path changed to {elf}")
    require(fwpkg == FWPKG_PATH, f"ws53.json firmware path changed to {fwpkg}")
    require(nested_fwpkg == FWPKG_PATH,
            f"VS Code upload firmware path changed to {nested_fwpkg}")
    require(config["console"]["baud"] == "115200", "console baud must be 115200")
    require(config["flash"]["signalbaud"] == 921600, "flash baud must be 921600")
    for page in (CLI, VSCODE):
        text = repo.read(page)
        if page == CLI:
            text = render_document(text)
        for value in (ELF_PATH, FWPKG_PATH, "921600", "115200"):
            require_contains(text, value, str(page))
    return "ELF, all-in-one firmware, flash 921600, and console 115200 map to ws53.json"


def check_hello_source_mapping(repo: Repository) -> str:
    cmake = repo.read(PERIPHERAL_CMAKE)
    source = repo.read(HELLO_SOURCE)
    require(
        re.search(
            r"if\(DEFINED CONFIG_SAMPLE_SUPPORT_HELLOWORLD\)\s*"
            r"add_subdirectory_if_exist\(helloworld\)\s*endif\(\)",
            cmake,
        ) is not None,
        "peripheral CMake does not map CONFIG_SAMPLE_SUPPORT_HELLOWORLD to helloworld",
    )
    for value in (
        'osal_printk("start helloworld sample\\r\\n")',
        'osal_printk("hello world\\r\\n")',
        "#define DELAYS_MS                       1000",
        "app_run(helloworld_entry)",
    ):
        require_contains(source, value, str(HELLO_SOURCE))
    for page in (CLI, VSCODE):
        text = repo.read(page)
        require_contains(text, "start helloworld sample", str(page))
        require(text.count("hello world") >= 2,
                f"{page} must state the repeated hello world marker")
    return "Kconfig -> CMake -> helloworld.c and documented log markers agree"


def check_platform_sources(repo: Repository) -> str:
    windows_compiler = PurePosixPath("src") / PurePosixPath(
        cli_contract.PLATFORM_COMPILERS["windows"].as_posix()
    )
    linux_compiler = PurePosixPath("src") / PurePosixPath(
        cli_contract.PLATFORM_COMPILERS["linux"].as_posix()
    )
    repo.require_exact_path(windows_compiler)
    repo.require_exact_path(linux_compiler)
    cli = render_document(repo.read(CLI))
    require_contains(cli, str(windows_compiler).replace("/", "\\"), str(CLI))
    require_contains(cli, f"./{linux_compiler}", str(CLI))
    return "Windows and Linux compiler source paths exist and match CLI checks"


def check_upstream_baseline(repo: Repository) -> str:
    cli_front, cli_body = markdown_parts(repo.read(CLI), CLI)
    vscode_front, vscode_body = markdown_parts(repo.read(VSCODE), VSCODE)
    require(
        metadata_urls(cli_front)
        == {FBB_CLI_URL, GIT_URL, GIT_LFS_URL, DEV_DRIVE_URL, WSL_URL},
        f"CLI upstream_refs URL set changed: {sorted(metadata_urls(cli_front))}",
    )
    require(
        metadata_urls(vscode_front)
        == {VSCODE_URL, GIT_URL, GIT_LFS_URL, DEV_DRIVE_URL, WSL_URL},
        f"VS Code upstream_refs URL set changed: {sorted(metadata_urls(vscode_front))}",
    )
    for value in (FBB_CLI_URL, GIT_URL, GIT_LFS_URL):
        require_contains(cli_body, value, str(CLI))
    for value in (VSCODE_URL, GIT_URL, GIT_LFS_URL):
        require_contains(vscode_body, value, str(VSCODE))
    fbb_urls = set(
        re.findall(r"https://gitcode\.com/HiSpark/[^\s)\]]*(?:fbb-cli|fbb_cli)[^\s)\]]*", cli_body)
    )
    require(fbb_urls == {FBB_CLI_URL}, f"FBB CLI links must use only {FBB_CLI_URL}, found {sorted(fbb_urls)}")
    return "FBB CLI, Git, Git LFS, VS Code, Dev Drive, and WSL URL baselines match"


def check_performance_links_are_follow_up(repo: Repository) -> str:
    for page in (CLI, VSCODE):
        _, body = markdown_parts(repo.read(page), page)
        heading = body.find("构建较慢时")
        require(heading >= 0, f"{page} has no build-performance follow-up section")
        for url in (DEV_DRIVE_URL, WSL_URL):
            positions = [match.start() for match in re.finditer(re.escape(url), body)]
            require(positions, f"{page} does not link {url}")
            require(all(position > heading for position in positions),
                    f"{page} uses {url} before the build-performance follow-up")
        require(
            "不是首次成功的前置条件" in body or "都不是本教程的前置条件" in body,
            f"{page} must state that Dev Drive/WSL are not prerequisites",
        )
        require_contains(
            body,
            "../guides/sdk-development/build/index.md#build-performance",
            str(page),
        )
    return "Dev Drive and WSL appear only after the main path and link to the build How-to"


def check_validation_boundary(repo: Repository) -> str:
    required_boundary_terms = {
        INDEX: ("Nightly Build", "VS Code", "Smoke", "HIL", "verification_level: static"),
        CLI: (
            "Ubuntu 24.04",
            "Windows Server 2025",
            "verification_level: build",
            "python -m tools.docs.get_started",
            "烧录",
            "Smoke",
            "HIL",
            "not_run",
        ),
        VSCODE: ("干净构建", "目标板 HIL", "draft", "verification_level: static"),
    }
    for page, terms in required_boundary_terms.items():
        text = repo.read(page)
        require_contains(text, "当前验证边界", str(page))
        for term in terms:
            require_contains(text, term, str(page))
    return "CLI credits Build only; entry/VS Code stay static; flash, Smoke, and HIL stay uncredited"


def github_escape(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def parse_args(argv: list[str]) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="repository root (defaults to the directory containing .github)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo = Repository(args.root.resolve())
    checks = (
        Check("GS001", "required repository inputs", lambda: check_inputs(repo)),
        Check("GS002", "page, step, prerequisite, and time budget", lambda: check_page_budget(repo)),
        Check("GS003", "retired quick-start page", lambda: check_quick_start_removed(repo)),
        Check("GS004", "unique MkDocs navigation entry", lambda: check_navigation(repo)),
        Check("GS005", "single development-mode decision", lambda: check_entry_branch(repo)),
        Check("GS006", "page metadata and declared scope", lambda: check_metadata(repo)),
        Check("GS007", "linked Windows/Linux tab groups", lambda: check_cli_tabs(repo)),
        Check("GS008", "source_refs resolution", lambda: check_source_refs(repo)),
        Check("GS009", "SDK, Target, CLI, and toolchain mapping", lambda: check_target_mapping(repo)),
        Check("GS010", "Kconfig transition mapping", lambda: check_kconfig_mapping(repo)),
        Check("GS010A", "executable CLI/document contract", lambda: check_executable_cli_contract(repo)),
        Check("GS010B", "Windows/Linux Nightly matrix", lambda: check_ci_matrix(repo)),
        Check("GS011", "ELF, firmware, and baud mapping", lambda: check_artifact_mapping(repo)),
        Check("GS012", "Hello World source mapping", lambda: check_hello_source_mapping(repo)),
        Check("GS013", "Windows/Linux compiler source mapping", lambda: check_platform_sources(repo)),
        Check("GS014", "official upstream-link baseline", lambda: check_upstream_baseline(repo)),
        Check("GS015", "performance content is follow-up only", lambda: check_performance_links_are_follow_up(repo)),
        Check("GS016", "declared verification boundary", lambda: check_validation_boundary(repo)),
    )

    print("Get Started source/static gate")
    print("Scope: offline source consistency only; firmware build, flash, serial, Smoke, and HIL are NOT RUN.")

    passed = 0
    failed = 0
    for check in checks:
        try:
            detail = check.run()
        except Exception as error:  # Fail closed on assertions and unexpected parser errors.
            failed += 1
            detail = f"{type(error).__name__}: {error}"
            print(f"FAIL {check.check_id} | {check.label} | {detail}")
            if os.environ.get("GITHUB_ACTIONS", "").lower() == "true":
                title = github_escape(f"Get Started {check.check_id}: {check.label}")
                print(f"::error title={title}::{github_escape(detail)}")
        else:
            passed += 1
            print(f"PASS {check.check_id} | {check.label} | {detail}")

    result = "PASS" if failed == 0 else "FAIL"
    print(f"SUMMARY result={result} passed={passed} failed={failed} total={len(checks)}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
