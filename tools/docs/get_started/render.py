"""Render executable Get Started contract values into Markdown."""

from __future__ import annotations

import re
from pathlib import Path

from tools.docs.get_started.contract import (
    ARTIFACTS,
    COMMAND_GROUPS,
    GENERATED_SECTIONS,
    PLATFORM_COMPILERS,
    SDK_BRANCH,
    SDK_REPOSITORY,
    SDK_VERSION,
)


MARKER_PREFIX = "get-started-cli"


def placeholder(section: str) -> str:
    """Return the single source placeholder for a generated section."""
    return f"<!-- {MARKER_PREFIX}:{section} -->"


def boundary_marker(section: str, edge: str) -> str:
    """Return a rendered ownership marker.

    Boundaries are emitted only into rendered output.  Source Markdown must use
    the single placeholder returned by :func:`placeholder`.
    """
    if edge not in {"begin", "end"}:
        raise ValueError(f"unknown generated boundary: {edge!r}")
    return f"<!-- {MARKER_PREFIX}:{section}:{edge} -->"


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


def _source_markers(markdown: str) -> list[str]:
    """Parse every comment that appears to claim generated ownership.

    Looking for the raw prefix first ensures truncated and otherwise malformed
    comments cannot disappear from validation merely because a stricter regex
    did not match them.
    """
    raw_markers = [
        line
        for line in markdown.splitlines()
        if MARKER_PREFIX in line
    ]
    values: list[str] = []
    marker_pattern = re.compile(
        rf"<!--\s*{re.escape(MARKER_PREFIX)}:([^>]+?)\s*-->"
    )
    for raw_marker in raw_markers:
        match = marker_pattern.fullmatch(raw_marker.strip())
        if match is None:
            raise ValueError(f"malformed generated placeholder: {raw_marker.strip()!r}")
        values.append(match.group(1))
    return values


def _validate_placeholders(markdown: str) -> None:
    expected = set(GENERATED_SECTIONS)
    observed: list[str] = []
    for raw_value in _source_markers(markdown):
        value = raw_value.strip()
        if value.endswith(":begin") or value.endswith(":end"):
            raise ValueError(
                "source Markdown must use single generated placeholders; "
                f"rendered boundary found: {value!r}"
            )
        if ":" in value:
            raise ValueError(f"malformed generated placeholder: {value!r}")
        if value not in expected:
            raise ValueError(f"unknown generated section placeholder: {value!r}")
        observed.append(value)

    for section in GENERATED_SECTIONS:
        count = observed.count(section)
        if count != 1:
            raise ValueError(
                f"section {section!r} must contain exactly one source placeholder; "
                f"found {count}"
            )
    if len(observed) != len(GENERATED_SECTIONS):
        raise ValueError("generated placeholder set differs from the executable contract")

    expected_order = list(GENERATED_SECTIONS)
    if observed != expected_order:
        raise ValueError(
            "generated placeholders must follow contract order: "
            f"expected {expected_order!r}, found {observed!r}"
        )


def render_document(markdown: str) -> str:
    """Replace each source placeholder with a bounded generated region.

    This operation is intentionally not idempotent: passing already-rendered
    content fails closed instead of silently accepting stale generated output.
    """
    _validate_placeholders(markdown)
    rendered = markdown
    for section in GENERATED_SECTIONS:
        source = placeholder(section)
        replacement = "\n\n".join(
            (
                boundary_marker(section, "begin"),
                render_section(section),
                boundary_marker(section, "end"),
            )
        )
        rendered, count = re.subn(
            re.escape(source), lambda _match: replacement, rendered, count=1
        )
        if count != 1:
            raise ValueError(f"could not render generated section {section!r}")
    return rendered


def _managed_content_lines(section: str) -> tuple[str, ...]:
    """Return generated lines that must not be duplicated in source Markdown."""
    ignored = {"else", "fi"}
    lines: list[str] = []
    for line in render_section(section).splitlines():
        value = line.strip()
        if (
            not value
            or value in ignored
            or value.startswith("```")
            or value.startswith("=== ")
        ):
            continue
        lines.append(value)
    return tuple(lines)


def validate_document_source(markdown: str) -> None:
    """Ensure generated commands are owned by placeholders, never hand-copied."""
    _validate_placeholders(markdown)
    source_lines = [line.strip() for line in markdown.splitlines()]
    for section in GENERATED_SECTIONS:
        for managed_line in _managed_content_lines(section):
            if managed_line in source_lines:
                line_number = source_lines.index(managed_line) + 1
                raise ValueError(
                    f"generated content is hand-written outside {section} on line "
                    f"{line_number}: {managed_line}"
                )

    rendered = render_document(markdown)
    for group, commands in COMMAND_GROUPS.items():
        begin_marker = boundary_marker(group, "begin")
        end_marker = boundary_marker(group, "end")
        begin = rendered.index(begin_marker)
        end = rendered.index(end_marker, begin)
        region = rendered[begin:end]
        for command in commands:
            if region.count(command.display) != 1:
                raise ValueError(
                    f"generated command must appear exactly once in {group}: "
                    f"{command.display}"
                )
            outside = rendered[:begin] + rendered[end:]
            if re.search(rf"(?m)^{re.escape(command.display)}\s*$", outside):
                raise ValueError(
                    f"generated command is also hand-written outside {group}: "
                    f"{command.display}"
                )
