"""Shared baseline handling for the documentation static checkers."""

from __future__ import annotations

import json
import os
import tempfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

BASELINE_VERSION = 1
SECTIONS = ("source", "rendered")
FINGERPRINT_FIELDS = ("rule", "path", "line", "message")


class BaselineError(ValueError):
    """Raised when the checked-in baseline is absent or malformed."""


def fingerprint(item: Any) -> tuple[str, str, int, str]:
    """Return the stable rule/path/line/message identity for one finding."""

    if isinstance(item, Mapping):
        values = tuple(item.get(field) for field in FINGERPRINT_FIELDS)
    else:
        values = tuple(getattr(item, field) for field in FINGERPRINT_FIELDS)
    rule, path, line, message = values
    if not isinstance(rule, str) or not rule:
        raise BaselineError("finding rule must be a non-empty string")
    if not isinstance(path, str) or not path:
        raise BaselineError("finding path must be a non-empty string")
    if not isinstance(line, int) or isinstance(line, bool) or line < 1:
        raise BaselineError("finding line must be a positive integer")
    if not isinstance(message, str) or not message:
        raise BaselineError("finding message must be a non-empty string")
    return rule, path, line, message


def as_entry(item: Any) -> dict[str, str | int]:
    rule, path, line, message = fingerprint(item)
    return {"rule": rule, "path": path, "line": line, "message": message}


def empty_baseline() -> dict[str, Any]:
    return {"version": BASELINE_VERSION, "source": [], "rendered": []}


def load_baseline(path: Path, *, allow_missing: bool = False) -> dict[str, Any]:
    if not path.is_file():
        if allow_missing:
            return empty_baseline()
        raise BaselineError(
            f"baseline not found: {path}; run the checker with --update-baseline"
        )
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise BaselineError(f"cannot read baseline {path}: {error}") from error
    if not isinstance(data, dict):
        raise BaselineError("baseline root must be a JSON object")
    if data.get("version") != BASELINE_VERSION:
        raise BaselineError(
            f"baseline version must be {BASELINE_VERSION}, got {data.get('version')!r}"
        )
    normalized = empty_baseline()
    for section in SECTIONS:
        entries = data.get(section)
        if not isinstance(entries, list):
            raise BaselineError(f"baseline section {section!r} must be a list")
        unique: dict[tuple[str, str, int, str], dict[str, str | int]] = {}
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                raise BaselineError(
                    f"baseline {section}[{index}] must be a JSON object"
                )
            try:
                identity = fingerprint(entry)
            except BaselineError as error:
                raise BaselineError(
                    f"invalid baseline {section}[{index}]: {error}"
                ) from error
            if identity in unique:
                raise BaselineError(
                    f"duplicate baseline fingerprint in {section}: {identity!r}"
                )
            unique[identity] = as_entry(entry)
        normalized[section] = [unique[key] for key in sorted(unique)]
    return normalized


def identities(entries: Iterable[Any]) -> set[tuple[str, str, int, str]]:
    return {fingerprint(item) for item in entries}


def reconcile(
    current: Iterable[Any], baseline_entries: Iterable[Mapping[str, Any]]
) -> tuple[
    set[tuple[str, str, int, str]],
    set[tuple[str, str, int, str]],
    set[tuple[str, str, int, str]],
]:
    current_set = identities(current)
    baseline_set = identities(baseline_entries)
    return (
        current_set & baseline_set,
        current_set - baseline_set,
        baseline_set - current_set,
    )


def update_section(path: Path, section: str, findings: Iterable[Any]) -> int:
    if section not in SECTIONS:
        raise BaselineError(f"unknown baseline section: {section!r}")
    data = load_baseline(path, allow_missing=True)
    entries = {fingerprint(item): as_entry(item) for item in findings}
    data[section] = [entries[key] for key in sorted(entries)]
    path.parent.mkdir(parents=True, exist_ok=True)
    output_mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.chmod(temporary, output_mode)
        os.replace(temporary, path)
    except OSError as error:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
        raise BaselineError(f"cannot update baseline {path}: {error}") from error
    return len(entries)
