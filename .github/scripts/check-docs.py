#!/usr/bin/env python3
"""Fail-closed source checks for the complete MkDocs documentation tree.

The checker deliberately separates high-confidence failures from migration debt:

* malformed UTF-8, malformed front matter, exposed secrets, and broken local
  references in maintained pages are blocking;
* the same broken references in legacy pages, missing structured metadata, and
  empty image alternative text are reported without making today's repository
  permanently red.

A page is considered maintained when its front matter declares ``doc_type``.
This is a repository policy boundary, not an inference about content quality.
"""

from __future__ import annotations

import argparse
import html.parser
import os
import re
import sys
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from docs_static_baseline import (
    BaselineError,
    fingerprint,
    load_baseline,
    reconcile,
    update_section,
)

FENCE_RE = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})")
REFERENCE_DEF_RE = re.compile(
    r"^[ ]{0,3}\[[^\]\n]+\]:[ \t]*(?:<([^>\n]+)>|([^\s]+))", re.MULTILINE
)
EMPTY_ALT_RE = re.compile(r"!\[\s*\]\(")
SECRET_PATTERNS = (
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{36,255}\b")),
    ("github-fine-grained-token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{70,255}\b")),
)
PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"
    r"(?P<body>.*?)"
    r"-----END (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----",
    re.DOTALL,
)
IGNORED_SCHEMES = {
    "data",
    "ftp",
    "http",
    "https",
    "irc",
    "javascript",
    "mailto",
    "news",
    "ssh",
    "tel",
}
MAX_DETAIL_LINES = 40


@dataclass(frozen=True)
class Finding:
    rule: str
    path: str
    line: int
    message: str
    blocking: bool


@dataclass(frozen=True)
class Reference:
    target: str
    line: int
    kind: str


def parse_args() -> argparse.Namespace:
    script_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=script_root,
        help="repository root (default: inferred from this script)",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs"),
        help="documentation directory, relative to --root unless absolute",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=Path(".github/docs-static-baseline.json"),
        help="baseline JSON, relative to --root unless absolute",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="replace the source section with current report-only findings",
    )
    return parser.parse_args()


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def mask_non_content(text: str) -> str:
    """Mask fenced code, inline code, and HTML comments without moving lines."""

    chars = list(text)
    lines = text.splitlines(keepends=True)
    offset = 0
    fence_char = ""
    fence_length = 0
    for line in lines:
        match = FENCE_RE.match(line)
        in_fence = bool(fence_char)
        if not in_fence and match:
            marker = match.group(1)
            fence_char, fence_length = marker[0], len(marker)
            in_fence = True
        elif in_fence and re.match(
            rf"^[ ]{{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*$",
            line.rstrip("\r\n"),
        ):
            fence_char = ""
            fence_length = 0
        if in_fence or match:
            for index in range(offset, offset + len(line)):
                if chars[index] not in "\r\n":
                    chars[index] = " "
        offset += len(line)

    masked = "".join(chars)

    def blank(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    masked = re.sub(r"<!--.*?-->", blank, masked, flags=re.DOTALL)
    # Markdown inline-code spans can contain link-like examples.  Do this after
    # fencing so a long code block cannot make the expression pathological.
    masked = re.sub(r"(`+)([^\n]*?)\1", blank, masked)
    return masked


def markdown_inline_references(text: str) -> Iterator[Reference]:
    """Extract inline Markdown destinations with balanced parentheses."""

    index = 0
    while True:
        marker = text.find("](", index)
        if marker < 0:
            return
        line_start = text.rfind("\n", 0, marker) + 1
        is_image = bool(re.search(r"!\[[^\]\n]*$", text[line_start:marker]))
        cursor = marker + 2
        while cursor < len(text) and text[cursor] in " \t":
            cursor += 1
        if cursor >= len(text):
            return
        if text[cursor] == "<":
            end = text.find(">", cursor + 1)
            if end < 0:
                index = marker + 2
                continue
            destination = text[cursor + 1 : end]
            cursor = end + 1
        else:
            start = cursor
            depth = 0
            escaped = False
            while cursor < len(text):
                char = text[cursor]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char in " \t\r\n" and depth == 0:
                    break
                cursor += 1
            destination = text[start:cursor]
        destination = re.sub(r"\\([() ])", r"\1", destination)
        if destination:
            yield Reference(
                target=destination,
                line=line_number(text, marker),
                kind="image" if is_image else "link",
            )
        index = max(cursor + 1, marker + 2)


class SourceHTMLReferences(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[Reference] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._handle(tag, attrs)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._handle(tag, attrs)

    def _handle(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line, _ = self.getpos()
        for attribute in ("href", "src", "poster"):
            value = values.get(attribute)
            if value:
                kind = "image" if tag.lower() in {"img", "source", "video"} else "link"
                self.references.append(Reference(value, line, kind))
        srcset = values.get("srcset")
        if srcset:
            for item in srcset.split(","):
                value = item.strip().split()[0] if item.strip() else ""
                if value:
                    self.references.append(Reference(value, line, "image"))


def extract_references(masked: str) -> list[Reference]:
    references = list(markdown_inline_references(masked))
    for match in REFERENCE_DEF_RE.finditer(masked):
        target = match.group(1) or match.group(2)
        if target:
            references.append(
                Reference(target, line_number(masked, match.start()), "reference")
            )
    parser = SourceHTMLReferences()
    try:
        parser.feed(masked)
    except html.parser.HTMLParseError:
        # HTMLParseError is retained for compatibility with older Python, even
        # though current HTMLParser is intentionally tolerant.
        pass
    references.extend(parser.references)
    return references


def split_front_matter(text: str) -> tuple[str | None, str, int | None]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None, text, None
    for index in range(1, len(lines)):
        if lines[index].rstrip("\r\n") == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1 :]), index + 1
    return "".join(lines[1:]), "", 1


def fallback_front_matter_check(data: str) -> tuple[dict[str, Any] | None, str | None]:
    """Validate the conservative YAML subset used by repository metadata."""

    def scalar_error(value: str) -> str | None:
        if value[0] in {'"', "'"} and (
            len(value) < 2 or value[-1] != value[0]
        ):
            return "unterminated quoted scalar"
        pairs = {"[": "]", "{": "}"}
        if value[0] in pairs and value[-1:] != pairs[value[0]]:
            return f"unterminated flow collection starting with {value[0]!r}"
        return None

    result: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any] | list[Any]]] = [(-1, result)]
    lines = data.splitlines()
    for number, raw in enumerate(lines, 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            return None, f"line {number}: tabs are not valid indentation"
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            return None, f"line {number}: indentation must use two-space levels"
        value = raw.strip()
        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value.startswith("- "):
            if not isinstance(parent, list):
                return None, f"line {number}: list item has no sequence parent"
            item = value[2:].strip()
            if not item:
                child: dict[str, Any] = {}
                parent.append(child)
                stack.append((indent, child))
            elif re.match(r"^[^:#][^:]*:\s*", item):
                key, scalar = item.split(":", 1)
                scalar = scalar.strip()
                if scalar and (error := scalar_error(scalar)):
                    return None, f"line {number}: {error}"
                child = {key.strip(): scalar.strip() or {}}
                parent.append(child)
                stack.append((indent, child))
            else:
                parent.append(item)
            continue
        if ":" not in value:
            return None, f"line {number}: expected a 'key: value' mapping entry"
        key, scalar = value.split(":", 1)
        key = key.strip()
        if not key:
            return None, f"line {number}: empty mapping key"
        if not isinstance(parent, dict):
            return None, f"line {number}: mapping entry has a sequence parent"
        if key in parent:
            return None, f"line {number}: duplicate key {key!r}"
        scalar = scalar.strip()
        if scalar:
            if error := scalar_error(scalar):
                return None, f"line {number}: {error}"
            parent[key] = scalar
            continue
        # Infer list vs mapping from the next significant, more-indented line.
        child_kind: dict[str, Any] | list[Any] = {}
        for later in lines[number:]:
            if not later.strip() or later.lstrip().startswith("#"):
                continue
            later_indent = len(later) - len(later.lstrip(" "))
            if later_indent <= indent:
                break
            if later.strip().startswith("- "):
                child_kind = []
            break
        parent[key] = child_kind
        stack.append((indent, child_kind))
    return result, None


def parse_front_matter(data: str) -> tuple[dict[str, Any] | None, str | None, str]:
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        parsed, error = fallback_front_matter_check(data)
        return parsed, error, "stdlib-fallback"

    class UniqueKeyLoader(yaml.SafeLoader):
        pass

    def construct_mapping(
        loader: Any, node: Any, deep: bool = False
    ) -> dict[Any, Any]:
        mapping: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeyLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )
    try:
        parsed = yaml.load(data, Loader=UniqueKeyLoader)
    except yaml.YAMLError as error:
        return None, str(error).replace("\n", " "), "PyYAML"
    if parsed is None:
        return {}, None, "PyYAML"
    if not isinstance(parsed, dict):
        return None, "front matter root must be a mapping", "PyYAML"
    return parsed, None, "PyYAML"


def exact_path_exists(path: Path, anchor: Path) -> bool:
    """Check existence while enforcing spelling on case-insensitive hosts."""

    try:
        relative_parts = path.relative_to(anchor).parts
    except ValueError:
        return False
    current = anchor
    if not current.exists():
        return False
    for part in relative_parts:
        if part in {"", "."}:
            continue
        if part == "..":
            return False
        try:
            entries = os.listdir(current)
        except OSError:
            return False
        if part not in entries:
            return False
        current = current / part
    return current.exists()


def target_candidates(
    target: str, source: Path, root: Path, docs_dir: Path
) -> tuple[list[Path], str | None]:
    target = target.strip()
    if not target or target.startswith("#"):
        return [], None
    if any(marker in target for marker in ("{{", "}}", "${", "$}")):
        return [], None
    parsed = urlsplit(target)
    if parsed.scheme.lower() in IGNORED_SCHEMES or parsed.netloc:
        return [], None
    if parsed.scheme and len(parsed.scheme) > 1:
        return [], None
    decoded = unquote(parsed.path).replace("\\ ", " ")
    if not decoded:
        return [], None
    if "\\" in decoded:
        return [], "uses a backslash in a URL path"
    base = docs_dir if decoded.startswith("/") else source.parent
    decoded = decoded.lstrip("/") if decoded.startswith("/") else decoded
    candidate = Path(os.path.normpath(os.path.join(base, decoded)))
    try:
        candidate.relative_to(root)
    except ValueError:
        return [], "escapes the repository root"
    candidates = [candidate]
    if not candidate.suffix:
        candidates.extend((candidate.with_suffix(".md"), candidate / "index.md"))
    return candidates, None


def check_document(
    path: Path, root: Path, docs_dir: Path
) -> tuple[list[Finding], bool, str]:
    rel = relative(path, root)
    findings: list[Finding] = []
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        findings.append(
            Finding("SRC001", rel, 1, f"not valid UTF-8: {error}", True)
        )
        return findings, False, "not-read"

    if text.startswith("\ufeff"):
        findings.append(
            Finding("SRC001", rel, 1, "UTF-8 BOM is unnecessary", False)
        )

    front_matter, body, closing_line = split_front_matter(text)
    metadata: dict[str, Any] = {}
    metadata_valid = True
    parser_name = "none"
    if front_matter is not None:
        if closing_line == 1:
            metadata_valid = False
            findings.append(
                Finding("SRC002", rel, 1, "front matter has no closing ---", True)
            )
        else:
            parsed, error, parser_name = parse_front_matter(front_matter)
            if error:
                metadata_valid = False
                findings.append(
                    Finding("SRC002", rel, 1, f"invalid front matter: {error}", True)
                )
            elif parsed is not None:
                metadata = parsed

    maintained = bool(metadata.get("doc_type"))
    if metadata_valid and not maintained:
        findings.append(
            Finding(
                "SRC101",
                rel,
                1,
                "legacy page has no structured doc_type metadata",
                False,
            )
        )

    for name, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    "SRC003",
                    rel,
                    line_number(text, match.start()),
                    f"high-confidence {name} material detected",
                    True,
                )
            )
    for match in PRIVATE_KEY_RE.finditer(text):
        key_body = match.group("body")
        placeholder = re.search(
            r"\*{3,}|\.{3,}|<[^>]*(?:key|private|填充)[^>]*>|"
            r"(?:your|example|dummy|replace)[_-]?(?:private[_-]?)?key",
            key_body,
            re.IGNORECASE,
        )
        base64_material = "".join(re.findall(r"[A-Za-z0-9+/=]", key_body))
        if not placeholder and len(base64_material) >= 80:
            findings.append(
                Finding(
                    "SRC003",
                    rel,
                    line_number(text, match.start()),
                    "high-confidence private-key material detected",
                    True,
                )
            )

    masked = mask_non_content(body)
    body_line_offset = closing_line or 0
    for reference in extract_references(masked):
        candidates, error = target_candidates(reference.target, path, root, docs_dir)
        if error:
            findings.append(
                Finding(
                    "SRC004",
                    rel,
                    reference.line + body_line_offset,
                    f"{reference.kind} target {reference.target!r} {error}",
                    maintained,
                )
            )
            continue
        if candidates and not any(exact_path_exists(item, root) for item in candidates):
            findings.append(
                Finding(
                    "SRC004",
                    rel,
                    reference.line + body_line_offset,
                    f"{reference.kind} target is missing or has wrong case: {reference.target}",
                    maintained,
                )
            )

    for match in EMPTY_ALT_RE.finditer(masked):
        findings.append(
            Finding(
                "SRC102",
                rel,
                line_number(masked, match.start()) + body_line_offset,
                "image has empty alternative text",
                False,
            )
        )
    return findings, maintained, parser_name


def print_findings(findings: Iterable[Finding], blocking: bool) -> None:
    selected = sorted(
        (item for item in findings if item.blocking is blocking),
        key=lambda item: (item.rule, item.path, item.line, item.message),
    )
    label = "BLOCK" if blocking else "REPORT"
    rules = sorted({item.rule for item in selected})
    per_rule = max(1, MAX_DETAIL_LINES // max(1, len(rules)))
    for rule in rules:
        group = [item for item in selected if item.rule == rule]
        for item in group[:per_rule]:
            print(
                f"[{label}] {item.rule} {item.path}:{item.line}: {item.message}",
                file=sys.stderr if blocking else sys.stdout,
            )
        omitted = len(group) - per_rule
        if omitted > 0:
            print(f"[{label}] {rule} ... {omitted} additional finding(s) omitted")


def print_improvements(
    resolved: set[tuple[str, str, int, str]], label: str = "IMPROVED"
) -> None:
    for rule, path, line, message in sorted(resolved)[:MAX_DETAIL_LINES]:
        print(f"[{label}] {rule} {path}:{line}: {message}")
    omitted = len(resolved) - MAX_DETAIL_LINES
    if omitted > 0:
        print(f"[{label}] ... {omitted} additional resolved finding(s) omitted")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    docs_dir = args.docs_dir
    if not docs_dir.is_absolute():
        docs_dir = root / docs_dir
    docs_dir = docs_dir.resolve()
    baseline_path = args.baseline
    if not baseline_path.is_absolute():
        baseline_path = root / baseline_path
    baseline_path = baseline_path.resolve()
    if not docs_dir.is_dir():
        print(f"[BLOCK] SRC000 documentation directory not found: {docs_dir}", file=sys.stderr)
        return 2

    markdown_files = sorted(docs_dir.rglob("*.md"))
    findings: list[Finding] = []
    maintained_count = 0
    parser_names: set[str] = set()
    for path in markdown_files:
        document_findings, maintained, parser_name = check_document(
            path, root, docs_dir
        )
        findings.extend(document_findings)
        maintained_count += int(maintained)
        parser_names.add(parser_name)

    hard_blocking = [item for item in findings if item.blocking]
    reports = [item for item in findings if not item.blocking]
    baseline_known = 0
    baseline_new = 0
    baseline_resolved = 0
    resolved: set[tuple[str, str, int, str]] = set()

    if args.update_baseline:
        print_findings(hard_blocking, True)
        print_findings(reports, False)
        if hard_blocking:
            print(
                "Source documentation baseline was not updated because blocking "
                "findings exist.",
                file=sys.stderr,
            )
            return 1
        try:
            count = update_section(baseline_path, "source", reports)
        except BaselineError as error:
            print(f"[BLOCK] SRC005 {error}", file=sys.stderr)
            return 2
        print(f"Source documentation baseline updated: {baseline_path} ({count} entries)")
        return 0

    try:
        baseline = load_baseline(baseline_path)
        known, new, resolved = reconcile(reports, baseline["source"])
        baseline_known = len(known)
        baseline_new = len(new)
        baseline_resolved = len(resolved)
        findings = hard_blocking + [
            replace(item, blocking=fingerprint(item) in new) for item in reports
        ]
    except BaselineError as error:
        findings = hard_blocking + reports + [
            Finding("SRC005", relative(baseline_path, root), 1, str(error), True)
        ]

    blocking = [item for item in findings if item.blocking]
    reports = [item for item in findings if not item.blocking]
    report_rules = Counter(item.rule for item in reports)
    print_findings(blocking, True)
    print_findings(reports, False)
    print_improvements(resolved)
    print(
        "Source documentation check: "
        f"files={len(markdown_files)} maintained={maintained_count} "
        f"blocking={len(blocking)} report_only={len(reports)} "
        f"report_by_rule={dict(sorted(report_rules.items()))} "
        f"baseline_known={baseline_known} baseline_new={baseline_new} "
        f"baseline_resolved={baseline_resolved} "
        f"front_matter_parser={','.join(sorted(parser_names))}"
    )
    if blocking:
        print("Source documentation check: FAIL", file=sys.stderr)
        return 1
    print("Source documentation check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
