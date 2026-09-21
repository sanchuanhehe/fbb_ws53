#!/usr/bin/env python3
"""Validate internal links, fragments, and assets in a rendered MkDocs site.

This is intentionally an offline checker.  It proves that references inside the
generated site resolve to generated files with exact path spelling; it does not
claim that external HTTP links are reachable.  The baseline retains the
high-confidence/migration-debt classification and drift history, but every
current finding fails the gate.
"""

from __future__ import annotations

import argparse
import html.parser
import os
import re
import sys
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, replace
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from docs_static_baseline import (
    BaselineError,
    fingerprint,
    load_baseline,
    reconcile,
    update_section,
)
from docs_static_report import (
    ReportError,
    build_report,
    emit_warning_annotations,
    write_json_report,
    write_tsv_report,
)
from tools.docs.get_started import GENERATED_SECTIONS, render_section

IGNORED_SCHEMES = {
    "data",
    "ftp",
    "irc",
    "javascript",
    "mailto",
    "news",
    "ssh",
    "tel",
}
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
SITE_URL_RE = re.compile(r"^site_url:\s*['\"]?([^'\"\s#]+)", re.MULTILINE)
MAX_DETAIL_LINES = 40
GET_STARTED_HOOK = "tools/docs/get_started/mkdocs_hook.py"
GET_STARTED_SOURCE_URI = "zh-CN/get-started/cli.md"
# zh-CN is the default folder locale, so mkdocs-static-i18n removes the locale
# prefix from its rendered URL.
GET_STARTED_OUTPUT = Path("get-started/cli/index.html")
FENCED_CODE_RE = re.compile(
    r"^[ \t]*```[^\n]*\n(?P<body>.*?)^[ \t]*```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class WebReference:
    target: str
    line: int
    kind: str


@dataclass(frozen=True)
class Finding:
    rule: str
    path: str
    line: int
    message: str
    blocking: bool = True


class RenderedHTML(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[WebReference] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self._handle(tag, attrs)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self._handle(tag, attrs)

    def _handle(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        line, _ = self.getpos()
        for anchor in (values.get("id"), values.get("name") if tag == "a" else None):
            if anchor:
                self.anchors.add(anchor)
        for attribute in ("href", "src", "poster", "action"):
            target = values.get(attribute)
            if target:
                self.references.append(WebReference(target, line, attribute))
        srcset = values.get("srcset")
        if srcset:
            for item in srcset.split(","):
                target = item.strip().split()[0] if item.strip() else ""
                if target:
                    self.references.append(WebReference(target, line, "srcset"))


class RenderedText(html.parser.HTMLParser):
    """Recover visible text from a rendered fragment, including highlighted code."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    @property
    def text(self) -> str:
        return "".join(self.parts)


def parse_args() -> argparse.Namespace:
    script_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path, help="rendered site directory")
    parser.add_argument(
        "--root",
        type=Path,
        default=script_root,
        help="repository root (default: inferred from this script)",
    )
    parser.add_argument(
        "--site-url",
        help="published site URL; defaults to site_url from mkdocs.yml",
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
        help="replace the rendered section with current migration-debt findings",
    )
    parser.add_argument(
        "--json-report",
        type=Path,
        help="write every finding and resolved baseline entry to this JSON file",
    )
    parser.add_argument(
        "--tsv-report",
        type=Path,
        help="write every finding and resolved baseline entry to this TSV file",
    )
    parser.add_argument(
        "--annotation-limit-per-rule",
        type=int,
        default=2,
        help="GitHub warning annotations per rule (default: 2; 0 disables)",
    )
    args = parser.parse_args()
    if args.annotation_limit_per_rule < 0:
        parser.error("--annotation-limit-per-rule must not be negative")
    return args


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def exact_path_exists(path: Path, anchor: Path) -> bool:
    try:
        parts = path.relative_to(anchor).parts
    except ValueError:
        return False
    current = anchor
    if not current.is_dir():
        return False
    for part in parts:
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


def discover_site_url(root: Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    config = root / "mkdocs.yml"
    if config.is_file():
        try:
            match = SITE_URL_RE.search(config.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            match = None
        if match:
            return match.group(1)
    return "https://rendered.invalid/"


def normalized_base(site_url: str) -> tuple[str, str, str]:
    parsed = urlsplit(site_url)
    scheme = parsed.scheme or "https"
    host = parsed.netloc or "rendered.invalid"
    base = parsed.path or "/"
    if not base.startswith("/"):
        base = "/" + base
    if not base.endswith("/"):
        base += "/"
    return scheme, host.lower(), base


def page_url(relative_path: Path, scheme: str, host: str, base: str) -> str:
    parts = relative_path.as_posix()
    if parts == "index.html":
        suffix = ""
    elif parts.endswith("/index.html"):
        suffix = parts[: -len("index.html")]
    else:
        suffix = parts
    return f"{scheme}://{host}{base}{suffix}"


def map_url_to_file(
    target: str,
    source_url: str,
    site_dir: Path,
    site_host: str,
    base: str,
) -> tuple[Path | None, str | None, str | None]:
    """Return (file, decoded fragment, classification/error)."""

    target = target.strip()
    if not target:
        return None, None, "ignore"
    if any(marker in target for marker in ("{{", "}}", "${", "$}")):
        return None, None, "ignore"
    parsed_raw = urlsplit(target)
    if parsed_raw.scheme.lower() in IGNORED_SCHEMES:
        return None, None, "external"
    if parsed_raw.scheme and parsed_raw.scheme.lower() not in {"http", "https"}:
        return None, None, "external"

    absolute = urlsplit(urljoin(source_url, target))
    if absolute.scheme.lower() not in {"http", "https"}:
        return None, None, "external"
    if absolute.netloc.lower() != site_host:
        return None, None, "external"

    path = unquote(absolute.path)
    base_without_slash = base.rstrip("/") or "/"
    if path == base_without_slash:
        relative_url = ""
    elif path.startswith(base):
        relative_url = path[len(base) :]
    else:
        return None, None, "outside-site-base"
    if "\\" in relative_url:
        return None, unquote(absolute.fragment), "backslash-path"

    lexical = Path(os.path.normpath(os.path.join(site_dir, relative_url)))
    try:
        lexical.relative_to(site_dir)
    except ValueError:
        return None, unquote(absolute.fragment), "outside-site-dir"

    candidates: list[Path] = []
    if relative_url.endswith("/") or lexical.is_dir():
        candidates.append(lexical / "index.html")
    else:
        candidates.append(lexical)
        if not lexical.suffix:
            candidates.extend((lexical.with_suffix(".html"), lexical / "index.html"))
    for candidate in candidates:
        if exact_path_exists(candidate, site_dir) and candidate.is_file():
            return candidate, unquote(absolute.fragment), None
    return candidates[0], unquote(absolute.fragment), "missing"


def parse_html_files(
    site_dir: Path,
) -> tuple[dict[Path, RenderedHTML], list[Finding]]:
    parsed: dict[Path, RenderedHTML] = {}
    findings: list[Finding] = []
    for path in sorted(site_dir.rglob("*.html")):
        rel = relative(path, site_dir)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            findings.append(
                Finding("WEB001", rel, 1, f"generated HTML is not UTF-8: {error}")
            )
            continue
        parser = RenderedHTML()
        try:
            parser.feed(text)
        except html.parser.HTMLParseError as error:
            findings.append(
                Finding("WEB001", rel, error.lineno, f"HTML parser error: {error}")
            )
            continue
        parsed[path] = parser
    return parsed, findings


def maintained_output_paths(root: Path, site_dir: Path) -> set[Path]:
    """Map structured source pages to their expected directory-URL output."""

    docs_dir = root / "docs"
    result: set[Path] = set()
    if not docs_dir.is_dir():
        return result
    for source in docs_dir.rglob("*.md"):
        try:
            text = source.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            continue
        try:
            close = lines.index("---", 1)
        except ValueError:
            continue
        metadata = "\n".join(lines[1:close])
        if not re.search(r"^doc_type:\s*\S+", metadata, re.MULTILINE):
            continue
        rel = source.relative_to(docs_dir)
        # The current static-i18n configuration publishes zh-CN as the default
        # language at the site root.  Other locale folders retain their prefix.
        if rel.parts and rel.parts[0] == "zh-CN":
            rel = Path(*rel.parts[1:])
        if rel.name == "index.md":
            output = rel.with_name("index.html")
        else:
            output = rel.with_suffix("") / "index.html"
        result.add(site_dir / output)
    return result


def css_references(path: Path) -> tuple[list[WebReference], Finding | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        return [], Finding(
            "WEB001", path.as_posix(), 1, f"generated CSS is not UTF-8: {error}"
        )
    references: list[WebReference] = []
    for match in CSS_URL_RE.finditer(text):
        target = match.group(2).strip()
        references.append(
            WebReference(target, text.count("\n", 0, match.start()) + 1, "css-url")
        )
    return references, None


def get_started_contract_findings(
    root: Path, site_dir: Path
) -> tuple[list[Finding], int, int]:
    """Verify the effective hook and its rendered non-HIL command contract."""

    findings: list[Finding] = []
    expected_by_section = {
        section: tuple(
            line.strip()
            for match in FENCED_CODE_RE.finditer(render_section(section))
            for line in match.group("body").splitlines()
            if line.strip()
        )
        for section in GENERATED_SECTIONS
    }
    expected_count = sum(len(values) for values in expected_by_section.values())
    verified_count = 0

    config_path = root / "mkdocs.yml"
    try:
        from mkdocs.config import load_config

        config = load_config(config_file=str(config_path))
    except Exception as error:
        findings.append(
            Finding(
                "WEB006",
                relative(config_path, root),
                1,
                f"cannot load effective MkDocs configuration to verify hooks: {error}",
            )
        )
        return findings, verified_count, expected_count

    hooks = config.get("hooks", {})
    hook = hooks.get(GET_STARTED_HOOK) if isinstance(hooks, dict) else None
    if hook is None:
        findings.append(
            Finding(
                "WEB006",
                relative(config_path, root),
                1,
                f"effective MkDocs hooks do not register {GET_STARTED_HOOK}",
            )
        )
    else:
        hook_file = getattr(hook, "__file__", None)
        expected_hook_file = (root / GET_STARTED_HOOK).resolve()
        if hook_file is None or Path(hook_file).resolve() != expected_hook_file:
            findings.append(
                Finding(
                    "WEB006",
                    relative(config_path, root),
                    1,
                    f"{GET_STARTED_HOOK} resolves to an unexpected module: {hook_file!r}",
                )
            )
        hook_uri = getattr(hook, "CLI_PAGE", None)
        if hook_uri != GET_STARTED_SOURCE_URI:
            findings.append(
                Finding(
                    "WEB006",
                    GET_STARTED_HOOK,
                    1,
                    f"hook target URI must be {GET_STARTED_SOURCE_URI!r}, got {hook_uri!r}",
                )
            )

    output_path = site_dir / GET_STARTED_OUTPUT
    output_rel = GET_STARTED_OUTPUT.as_posix()
    if not exact_path_exists(output_path, site_dir) or not output_path.is_file():
        findings.append(
            Finding(
                "WEB006",
                output_rel,
                1,
                "rendered CLI Get Started page is absent at the default zh-CN URI",
            )
        )
        return findings, verified_count, expected_count
    try:
        rendered = output_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        findings.append(
            Finding(
                "WEB006",
                output_rel,
                1,
                f"cannot inspect rendered CLI contract as UTF-8: {error}",
            )
        )
        return findings, verified_count, expected_count

    for section in GENERATED_SECTIONS:
        source_comment = f"<!-- get-started-cli:{section} -->"
        source_count = rendered.count(source_comment)
        if source_count:
            findings.append(
                Finding(
                    "WEB006",
                    output_rel,
                    1,
                    f"rendered section {section!r} retains {source_count} source "
                    "placeholder(s); the MkDocs hook did not fully consume its input",
                )
            )
        begin_comment = f"<!-- get-started-cli:{section}:begin -->"
        end_comment = f"<!-- get-started-cli:{section}:end -->"
        begin_count = rendered.count(begin_comment)
        end_count = rendered.count(end_comment)
        if begin_count != 1 or end_count != 1:
            findings.append(
                Finding(
                    "WEB006",
                    output_rel,
                    1,
                    f"rendered section {section!r} must contain exactly one begin "
                    f"and end marker (found {begin_count}/{end_count})",
                )
            )
            continue
        begin = rendered.index(begin_comment)
        end = rendered.index(end_comment)
        line = rendered.count("\n", 0, begin) + 1
        if begin >= end:
            findings.append(
                Finding(
                    "WEB006",
                    output_rel,
                    line,
                    f"rendered section {section!r} has reversed markers",
                )
            )
            continue

        parser = RenderedText()
        parser.feed(rendered[begin + len(begin_comment) : end])
        visible_lines = [line.strip() for line in parser.text.splitlines()]
        for value in expected_by_section[section]:
            occurrences = visible_lines.count(value)
            if occurrences == 1:
                verified_count += 1
                continue
            findings.append(
                Finding(
                    "WEB006",
                    output_rel,
                    line,
                    f"rendered section {section!r} must contain managed value "
                    f"exactly once (found {occurrences}): {value}",
                )
            )

    return findings, verified_count, expected_count


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


def print_improvements(resolved: set[tuple[str, str, int, str]]) -> None:
    for rule, path, line, message in sorted(resolved)[:MAX_DETAIL_LINES]:
        print(f"[IMPROVED] {rule} {path}:{line}: {message}")
    omitted = len(resolved) - MAX_DETAIL_LINES
    if omitted > 0:
        print(f"[IMPROVED] ... {omitted} additional resolved finding(s) omitted")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    site_dir = args.site_dir
    if not site_dir.is_absolute():
        site_dir = (root / site_dir).resolve()
    else:
        site_dir = site_dir.resolve()
    if not site_dir.is_dir():
        print(f"[BLOCK] WEB000 rendered site directory not found: {site_dir}", file=sys.stderr)
        return 2
    baseline_path = args.baseline
    if not baseline_path.is_absolute():
        baseline_path = root / baseline_path
    baseline_path = baseline_path.resolve()

    site_url = discover_site_url(root, args.site_url)
    scheme, site_host, base = normalized_base(site_url)
    html_files, findings = parse_html_files(site_dir)
    contract_findings, contract_verified, contract_expected = (
        get_started_contract_findings(root, site_dir)
    )
    findings.extend(contract_findings)
    maintained_pages = maintained_output_paths(root, site_dir)
    external_count = 0
    checked_count = 0
    seen_findings: set[tuple[str, str, int, str]] = set()

    def add_finding(finding: Finding) -> None:
        key = (finding.rule, finding.path, finding.line, finding.message)
        if key not in seen_findings:
            seen_findings.add(key)
            findings.append(finding)

    for source, document in html_files.items():
        source_rel = source.relative_to(site_dir)
        source_url = page_url(source_rel, scheme, site_host, base)
        source_is_maintained = source in maintained_pages
        for reference in document.references:
            target_file, fragment, classification = map_url_to_file(
                reference.target, source_url, site_dir, site_host, base
            )
            if classification in {"external", "ignore"}:
                external_count += int(classification == "external")
                continue
            checked_count += 1
            if classification:
                add_finding(
                    Finding(
                        "WEB002",
                        source_rel.as_posix(),
                        reference.line,
                        f"{reference.kind} {reference.target!r} does not resolve "
                        f"inside the rendered site ({classification})",
                        blocking=source_is_maintained,
                    )
                )
                continue
            if fragment and target_file is not None and target_file.suffix == ".html":
                if fragment.startswith(":~:text="):
                    continue
                target_document = html_files.get(target_file)
                if target_document is None:
                    add_finding(
                        Finding(
                            "WEB003",
                            source_rel.as_posix(),
                            reference.line,
                            f"cannot inspect fragment in {reference.target!r}",
                            blocking=source_is_maintained,
                        )
                    )
                elif fragment not in target_document.anchors:
                    add_finding(
                        Finding(
                            "WEB003",
                            source_rel.as_posix(),
                            reference.line,
                            f"fragment #{fragment} is absent from "
                            f"{target_file.relative_to(site_dir).as_posix()}",
                            blocking=source_is_maintained,
                        )
                    )

    for css_path in sorted(site_dir.rglob("*.css")):
        references, error = css_references(css_path)
        if error:
            add_finding(error)
            continue
        source_rel = css_path.relative_to(site_dir)
        source_url = page_url(source_rel, scheme, site_host, base)
        for reference in references:
            _, _, classification = map_url_to_file(
                reference.target, source_url, site_dir, site_host, base
            )
            if classification in {"external", "ignore"}:
                external_count += int(classification == "external")
                continue
            checked_count += 1
            if classification:
                add_finding(
                    Finding(
                        "WEB004",
                        source_rel.as_posix(),
                        reference.line,
                        f"CSS asset {reference.target!r} does not resolve "
                        f"inside the rendered site ({classification})",
                    )
                )

    hard_blocking = [item for item in findings if item.blocking]
    reports = [item for item in findings if not item.blocking]
    baseline_known = 0
    baseline_new = 0
    baseline_resolved = 0
    resolved: set[tuple[str, str, int, str]] = set()
    classifications = {
        fingerprint(item): "hard_blocking" for item in hard_blocking
    }

    if args.update_baseline:
        print_findings(hard_blocking, True)
        print_findings(reports, False)
        if hard_blocking:
            print(
                "Rendered site baseline was not updated because blocking findings exist.",
                file=sys.stderr,
            )
            return 1
        try:
            count = update_section(baseline_path, "rendered", reports)
        except BaselineError as error:
            print(f"[BLOCK] WEB005 {error}", file=sys.stderr)
            return 2
        print(f"Rendered site baseline updated: {baseline_path} ({count} entries)")
        return 0

    try:
        baseline = load_baseline(baseline_path)
        known, new, resolved = reconcile(reports, baseline["rendered"])
        baseline_known = len(known)
        baseline_new = len(new)
        baseline_resolved = len(resolved)
        findings = hard_blocking + [
            replace(item, blocking=fingerprint(item) in new) for item in reports
        ]
        classifications.update({identity: "baseline_known" for identity in known})
        classifications.update({identity: "baseline_new" for identity in new})
    except BaselineError as error:
        baseline_new = len(reports)
        findings = hard_blocking + [replace(item, blocking=True) for item in reports]
        classifications.update(
            {fingerprint(item): "baseline_new" for item in reports}
        )
        baseline_finding = Finding(
            "WEB005", relative(baseline_path, root), 1, str(error), True
        )
        findings.append(baseline_finding)
        classifications[fingerprint(baseline_finding)] = "hard_blocking"

    blocking = [item for item in findings if item.blocking]
    reports = [item for item in findings if not item.blocking]
    finding_rules = Counter(item.rule for item in findings)
    print_findings(blocking, True)
    print_findings(reports, False)
    print_improvements(resolved)
    report = build_report(
        check="rendered",
        findings=findings,
        classifications=classifications,
        resolved=resolved,
        context={
            "html_files": len(html_files),
            "maintained_pages": len(maintained_pages),
            "get_started_contract_verified": contract_verified,
            "get_started_contract_expected": contract_expected,
            "internal_references": checked_count,
            "external_references_skipped": external_count,
            "site_url": site_url,
            "baseline": relative(baseline_path, root),
        },
    )
    try:
        if args.json_report:
            json_report = args.json_report
            if not json_report.is_absolute():
                json_report = root / json_report
            write_json_report(json_report.resolve(), report)
        if args.tsv_report:
            tsv_report = args.tsv_report
            if not tsv_report.is_absolute():
                tsv_report = root / tsv_report
            write_tsv_report(tsv_report.resolve(), report)
    except ReportError as error:
        print(f"[BLOCK] WEB007 {error}", file=sys.stderr)
        return 2
    emit_warning_annotations(
        report, limit_per_rule=args.annotation_limit_per_rule
    )
    print(
        "Rendered site check: "
        f"html_files={len(html_files)} maintained_pages={len(maintained_pages)} "
        f"get_started_contract={contract_verified}/{contract_expected} "
        f"internal_references={checked_count} "
        f"external_references_skipped={external_count} "
        f"findings={len(findings)} hard_or_new={len(blocking)} "
        f"findings_by_rule={dict(sorted(finding_rules.items()))} "
        f"baseline_known={baseline_known} baseline_new={baseline_new} "
        f"baseline_resolved={baseline_resolved} "
        f"site_url={site_url}"
    )
    if findings:
        print("Rendered site check: FAIL", file=sys.stderr)
        return 1
    print("Rendered site check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
