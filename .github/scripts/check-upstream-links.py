#!/usr/bin/env python3
"""Validate documentation ``upstream_refs`` and probe their unique URLs.

This checker intentionally reads only the ``upstream_refs`` contract from YAML
front matter.  It does not turn every hyperlink in the documentation body into
a nightly availability dependency.

The parser is deliberately small and strict: ``upstream_refs`` must be a block
list whose entries contain non-empty ``project``, ``version``, and ``url``
scalars.  The rest of the front matter is left to the documentation metadata
checker.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import socket
import ssl
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen


USER_AGENT = (
    "HiSpark-Documentation-Upstream-Check/1.0 "
    "(+https://github.com/sanchuanhehe/fbb_ws53)"
)
REQUIRED_FIELDS = ("project", "version", "url")
RETRYABLE_STATUS = {408, 425, 429}
BLOCKED_STATUS = {401, 403, 407, 429}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    file: str | None = None
    line: int | None = None


@dataclass(frozen=True)
class Reference:
    file: str
    line: int
    project: str
    version: str
    url: str


@dataclass(frozen=True)
class RequestResult:
    method: str
    ok: bool
    status_code: int | None
    final_url: str | None
    elapsed_ms: int
    error: str | None


def _strip_yaml_comment(value: str) -> str:
    """Strip a YAML plain-scalar comment without corrupting quoted ``#``."""

    single_quoted = False
    double_quoted = False
    escaped = False
    for index, character in enumerate(value):
        if double_quoted and character == "\\" and not escaped:
            escaped = True
            continue
        if character == '"' and not single_quoted and not escaped:
            double_quoted = not double_quoted
        elif character == "'" and not double_quoted:
            single_quoted = not single_quoted
        elif (
            character == "#"
            and not single_quoted
            and not double_quoted
            and (index == 0 or value[index - 1].isspace())
        ):
            return value[:index].rstrip()
        escaped = False
    return value.strip()


def _parse_scalar(raw_value: str) -> tuple[str | None, str | None]:
    value = _strip_yaml_comment(raw_value).strip()
    if not value:
        return None, "value is empty"
    if value[0] in "|>":
        return None, "multi-line YAML scalars are not supported in upstream_refs"
    if value.startswith('"'):
        if not value.endswith('"') or len(value) < 2:
            return None, "double-quoted value is not closed"
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as error:
            return None, f"invalid double-quoted value: {error.msg}"
        if not isinstance(parsed, str):
            return None, "quoted value must be a string"
        value = parsed
    elif value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            return None, "single-quoted value is not closed"
        value = value[1:-1].replace("''", "'")
    elif value.endswith(('"', "'")):
        return None, "quoted value has no matching opening quote"

    value = value.strip()
    if not value or value.lower() in {"null", "none", "~"}:
        return None, "value is empty"
    return value, None


def _front_matter(lines: list[str]) -> tuple[list[tuple[int, str]] | None, str | None]:
    if not lines or lines[0].strip() != "---":
        return None, None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return [(line + 1, lines[line]) for line in range(1, index)], None
    return None, "YAML front matter is not closed with ---"


def _validate_url(url: str) -> str | None:
    if any(character.isspace() for character in url):
        return "URL contains whitespace"
    try:
        parsed = urlsplit(url)
        # Accessing these properties performs additional validation (for
        # example, malformed IPv6 brackets and out-of-range ports).
        _ = parsed.hostname, parsed.port
    except ValueError as error:
        return f"URL is malformed: {error}"
    if parsed.scheme not in {"http", "https"}:
        return "URL scheme must be http or https"
    if not parsed.hostname:
        return "URL has no hostname"
    if parsed.username is not None or parsed.password is not None:
        return "URL must not contain credentials"
    return None


def _parse_upstream_block(
    *,
    relative_path: str,
    block: list[tuple[int, str]],
    key_index: int,
) -> tuple[list[Reference], list[Finding], int]:
    key_line, key_text = block[key_index]
    key_match = re.fullmatch(r"upstream_refs\s*:\s*(.*)", key_text)
    assert key_match is not None
    suffix = _strip_yaml_comment(key_match.group(1)).strip()

    findings: list[Finding] = []
    references: list[Reference] = []
    if suffix:
        findings.append(
            Finding(
                "UPSTREAM_REFS_NOT_BLOCK_LIST",
                "upstream_refs must use a YAML block list, not an inline value",
                relative_path,
                key_line,
            )
        )

    entries: list[tuple[int, dict[str, tuple[str, int]]]] = []
    current: tuple[int, dict[str, tuple[str, int]]] | None = None
    cursor = key_index + 1
    while cursor < len(block):
        line_number, text = block[cursor]
        if text.strip() and not text.lstrip().startswith("#") and not text[0].isspace():
            break
        stripped = text.strip()
        if not stripped or stripped.startswith("#"):
            cursor += 1
            continue

        item_match = re.fullmatch(r"\s+-\s*(.*)", text)
        if item_match:
            if current is not None:
                entries.append(current)
            current = (line_number, {})
            remainder = item_match.group(1).strip()
            if not remainder:
                cursor += 1
                continue
            field_match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)", remainder)
            if not field_match:
                findings.append(
                    Finding(
                        "UPSTREAM_REF_INVALID_ITEM",
                        "each upstream_refs item must be a mapping",
                        relative_path,
                        line_number,
                    )
                )
            else:
                field, raw_value = field_match.groups()
                value, error = _parse_scalar(raw_value)
                if error:
                    findings.append(
                        Finding(
                            "UPSTREAM_REF_INVALID_VALUE",
                            f"{field}: {error}",
                            relative_path,
                            line_number,
                        )
                    )
                elif value is not None:
                    current[1][field] = (value, line_number)
            cursor += 1
            continue

        field_match = re.fullmatch(
            r"\s+([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)", text
        )
        if not field_match:
            findings.append(
                Finding(
                    "UPSTREAM_REF_INVALID_LINE",
                    "invalid line in upstream_refs block",
                    relative_path,
                    line_number,
                )
            )
            cursor += 1
            continue
        if current is None:
            findings.append(
                Finding(
                    "UPSTREAM_REF_FIELD_WITHOUT_ITEM",
                    "upstream_refs fields must follow a '- project: ...' list item",
                    relative_path,
                    line_number,
                )
            )
            cursor += 1
            continue

        field, raw_value = field_match.groups()
        if field in current[1]:
            findings.append(
                Finding(
                    "UPSTREAM_REF_DUPLICATE_FIELD",
                    f"duplicate field: {field}",
                    relative_path,
                    line_number,
                )
            )
            cursor += 1
            continue
        value, error = _parse_scalar(raw_value)
        if error:
            findings.append(
                Finding(
                    "UPSTREAM_REF_INVALID_VALUE",
                    f"{field}: {error}",
                    relative_path,
                    line_number,
                )
            )
        elif value is not None:
            current[1][field] = (value, line_number)
        cursor += 1

    if current is not None:
        entries.append(current)
    if not entries:
        findings.append(
            Finding(
                "UPSTREAM_REFS_EMPTY",
                "upstream_refs must contain at least one item",
                relative_path,
                key_line,
            )
        )

    for item_line, fields in entries:
        missing = [field for field in REQUIRED_FIELDS if field not in fields]
        if missing:
            findings.append(
                Finding(
                    "UPSTREAM_REF_MISSING_FIELDS",
                    f"upstream_refs item is missing: {', '.join(missing)}",
                    relative_path,
                    item_line,
                )
            )
            continue
        project = fields["project"][0]
        version = fields["version"][0]
        url, url_line = fields["url"]
        url_error = _validate_url(url)
        if url_error:
            findings.append(
                Finding(
                    "UPSTREAM_REF_INVALID_URL",
                    url_error,
                    relative_path,
                    url_line,
                )
            )
            continue
        references.append(
            Reference(
                file=relative_path,
                line=item_line,
                project=project,
                version=version,
                url=url,
            )
        )
    return references, findings, cursor


def collect_references(root: Path) -> tuple[list[Reference], list[Finding], int]:
    docs_root = root / "docs"
    if not docs_root.is_dir():
        return [], [Finding("DOCS_ROOT_MISSING", "docs directory does not exist", "docs", 1)], 0

    references: list[Reference] = []
    findings: list[Finding] = []
    documents_scanned = 0
    for path in sorted(docs_root.rglob("*.md")):
        documents_scanned += 1
        relative_path = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            findings.append(
                Finding(
                    "DOCUMENT_READ_ERROR",
                    f"cannot read UTF-8 Markdown: {error}",
                    relative_path,
                    1,
                )
            )
            continue
        lines = text.splitlines()
        front_matter, front_matter_error = _front_matter(lines)
        if front_matter_error:
            findings.append(
                Finding(
                    "FRONT_MATTER_UNCLOSED",
                    front_matter_error,
                    relative_path,
                    1,
                )
            )
            continue
        if front_matter is None:
            continue

        key_indices = [
            index
            for index, (_, line) in enumerate(front_matter)
            if re.fullmatch(r"upstream_refs\s*:\s*.*", line)
        ]
        if len(key_indices) > 1:
            for duplicate_index in key_indices[1:]:
                findings.append(
                    Finding(
                        "UPSTREAM_REFS_DUPLICATE_KEY",
                        "front matter contains more than one upstream_refs key",
                        relative_path,
                        front_matter[duplicate_index][0],
                    )
                )
        if key_indices:
            parsed, parse_findings, _ = _parse_upstream_block(
                relative_path=relative_path,
                block=front_matter,
                key_index=key_indices[0],
            )
            references.extend(parsed)
            findings.extend(parse_findings)
    return references, findings, documents_scanned


def _request(url: str, method: str, timeout: float) -> RequestResult:
    target_url, _ = urldefrag(url)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.1",
        "Accept-Encoding": "identity",
        "User-Agent": USER_AGENT,
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = Request(target_url, headers=headers, method=method)
    started = time.monotonic()
    try:
        with urlopen(request, timeout=timeout) as response:  # noqa: S310 - validated URL
            status = response.getcode() or 200
            final_url = response.geturl()
        return RequestResult(
            method=method,
            ok=200 <= status < 400,
            status_code=status,
            final_url=final_url,
            elapsed_ms=round((time.monotonic() - started) * 1000),
            error=None if 200 <= status < 400 else f"HTTP {status}",
        )
    except HTTPError as error:
        try:
            final_url = error.geturl()
        finally:
            error.close()
        return RequestResult(
            method=method,
            ok=False,
            status_code=error.code,
            final_url=final_url,
            elapsed_ms=round((time.monotonic() - started) * 1000),
            error=f"HTTP {error.code}",
        )
    except (
        URLError,
        TimeoutError,
        socket.timeout,
        ssl.SSLError,
        OSError,
        ValueError,
        UnicodeError,
    ) as error:
        reason = getattr(error, "reason", error)
        return RequestResult(
            method=method,
            ok=False,
            status_code=None,
            final_url=None,
            elapsed_ms=round((time.monotonic() - started) * 1000),
            error=f"{type(reason).__name__}: {reason}",
        )


def _classification(result: RequestResult) -> str:
    if result.ok:
        return "reachable"
    status = result.status_code
    if status in {404, 410}:
        return "missing"
    if status in BLOCKED_STATUS:
        return "blocked"
    if status is not None and status >= 500:
        return "server_error"
    if status is not None:
        return "http_error"
    if result.error and "timed out" in result.error.lower():
        return "timeout"
    return "network_error"


def _retryable(result: RequestResult) -> bool:
    status = result.status_code
    return status is None or status in RETRYABLE_STATUS or (status is not None and status >= 500)


def probe_url(
    url: str,
    *,
    timeout: float,
    retries: int,
    retry_delay: float,
) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    final_result: RequestResult | None = None
    for attempt_number in range(1, retries + 2):
        head = _request(url, "HEAD", timeout)
        attempt: dict[str, Any] = {"attempt": attempt_number, "head": asdict(head)}
        final_result = head
        if not head.ok:
            get = _request(url, "GET", timeout)
            attempt["get"] = asdict(get)
            final_result = get
        attempts.append(attempt)
        if final_result.ok or not _retryable(final_result) or attempt_number > retries:
            break
        time.sleep(retry_delay * (2 ** (attempt_number - 1)))

    assert final_result is not None
    classification = _classification(final_result)
    return {
        "url": url,
        "ok": final_result.ok,
        "classification": classification,
        "status_code": final_result.status_code,
        "final_url": final_result.final_url,
        "method": final_result.method,
        "error": final_result.error,
        "attempts": attempts,
    }


def _annotation_escape(value: str, *, property_value: bool = False) -> str:
    escaped = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    if property_value:
        escaped = escaped.replace(":", "%3A").replace(",", "%2C")
    return escaped


def emit_finding(finding: Finding) -> None:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        properties = [f"title={_annotation_escape(finding.code, property_value=True)}"]
        if finding.file:
            properties.insert(0, f"file={_annotation_escape(finding.file, property_value=True)}")
        if finding.line:
            properties.append(f"line={finding.line}")
        message = _annotation_escape(finding.message)
        print(f"::error {','.join(properties)}::{message}", file=sys.stderr)
    else:
        location = ""
        if finding.file:
            location = finding.file
            if finding.line:
                location += f":{finding.line}"
            location += ": "
        print(f"[ERROR] {location}{finding.code}: {finding.message}", file=sys.stderr)


def _write_json(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as temporary:
        json.dump(report, temporary, ensure_ascii=False, indent=2, sort_keys=True)
        temporary.write("\n")
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, path)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root (default: current directory)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="path for the machine-readable JSON report",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="timeout in seconds for each HTTP request (default: 10)",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=2,
        help="retries after the first URL attempt (default: 2)",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=1.0,
        help="initial exponential-backoff delay in seconds (default: 1)",
    )
    parser.add_argument(
        "--min-refs",
        type=int,
        default=1,
        help="minimum expected number of upstream_refs entries (default: 1)",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="validate and report metadata only; explicitly skip HTTP probes",
    )
    args = parser.parse_args(argv)
    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")
    if args.retries < 0:
        parser.error("--retries must not be negative")
    if args.retry_delay < 0:
        parser.error("--retry-delay must not be negative")
    if args.min_refs < 0:
        parser.error("--min-refs must not be negative")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.expanduser().resolve()
    output = args.output.expanduser().resolve()

    references, findings, documents_scanned = collect_references(root)
    if len(references) < args.min_refs:
        findings.append(
            Finding(
                "UPSTREAM_REFS_BELOW_MINIMUM",
                f"found {len(references)} valid references; expected at least {args.min_refs}",
                "docs",
                1,
            )
        )

    references_by_url: dict[str, list[Reference]] = {}
    for reference in references:
        references_by_url.setdefault(reference.url, []).append(reference)

    url_checks: list[dict[str, Any]] = []
    if not args.offline:
        for url in sorted(references_by_url):
            check = probe_url(
                url,
                timeout=args.timeout,
                retries=args.retries,
                retry_delay=args.retry_delay,
            )
            check["references"] = [
                {"file": reference.file, "line": reference.line, "project": reference.project}
                for reference in references_by_url[url]
            ]
            url_checks.append(check)
            if not check["ok"]:
                first_reference = references_by_url[url][0]
                status = (
                    f"HTTP {check['status_code']}"
                    if check["status_code"] is not None
                    else check["error"] or "request failed"
                )
                findings.append(
                    Finding(
                        "UPSTREAM_URL_UNREACHABLE",
                        f"{url} is {check['classification']} ({status})",
                        first_reference.file,
                        first_reference.line,
                    )
                )

    failed_urls = sum(1 for check in url_checks if not check["ok"])
    reachable_urls = sum(1 for check in url_checks if check["ok"])
    passed = not findings and (args.offline or failed_urls == 0)
    report: dict[str, Any] = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "mode": "offline" if args.offline else "network",
        "summary": {
            "result": "pass" if passed else "fail",
            "documents_scanned": documents_scanned,
            "references": len(references),
            "unique_urls": len(references_by_url),
            "reachable_urls": reachable_urls,
            "failed_urls": failed_urls,
            "findings": len(findings),
            "network_skipped": bool(args.offline),
        },
        "references": [asdict(reference) for reference in references],
        "url_checks": url_checks,
        "findings": [asdict(finding) for finding in findings],
    }
    _write_json(output, report)

    for finding in findings:
        emit_finding(finding)
    if passed:
        if args.offline:
            print(
                f"[PASS] parsed {len(references)} upstream_refs across "
                f"{len(references_by_url)} unique URLs; network explicitly skipped",
                file=sys.stderr,
            )
        else:
            print(
                f"[PASS] {len(references)} upstream_refs; "
                f"{reachable_urls}/{len(references_by_url)} unique URLs reachable",
                file=sys.stderr,
            )
        return 0

    print(
        f"[FAIL] {len(findings)} finding(s); "
        f"{reachable_urls}/{len(references_by_url)} unique URLs reachable",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
