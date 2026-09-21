"""Command-line entry point for the shared CLI Get Started contract.

Invoke this module from the repository root.  The compatibility scripts under
``.github/scripts`` remain available to callers that must start elsewhere.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence

from tools.docs.get_started.contract import (
    ARTIFACTS,
    CLI_COMMIT,
    CLI_REPOSITORY,
    CLI_VERSION,
    COMMAND_GROUPS,
    EXPECTED_RUNNER_LABELS,
    GENERATED_SECTIONS,
)
from tools.docs.get_started.checks import main as run_source_checks
from tools.docs.get_started.evidence import _expected_step_argv, validate_evidence
from tools.docs.get_started.render import (
    render_document,
    render_section,
    validate_document_source,
)
from tools.docs.get_started.runner import run_validation


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    render_parser = subparsers.add_parser("render", help="render generated Markdown")
    render_parser.add_argument("--section", choices=GENERATED_SECTIONS)
    render_parser.add_argument(
        "--document",
        type=Path,
        help="render all generated placeholders in this Markdown document",
    )

    check_parser = subparsers.add_parser(
        "check-document", help="validate generated placeholders and ownership"
    )
    check_parser.add_argument("document", type=Path)

    source_check_parser = subparsers.add_parser(
        "check-source", help="run the complete offline Get Started source gate"
    )
    source_check_parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)

    subparsers.add_parser(
        "install-cli",
        help="install the exact FBB CLI revision declared by this contract",
    )

    run_parser = subparsers.add_parser(
        "run", help="execute the Windows/Linux non-HIL build path"
    )
    run_parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    run_parser.add_argument("--platform", choices=("windows", "linux"), required=True)
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
    evidence_parser.add_argument("--platform", choices=("windows", "linux"), required=True)
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
    if args.command == "check-source":
        return run_source_checks(["--root", str(args.root)])
    if args.command == "install-cli":
        requirement = f"git+{CLI_REPOSITORY}.git@{CLI_COMMIT}"
        print(f"Installing pinned FBB CLI {CLI_VERSION} ({CLI_COMMIT})")
        return subprocess.call([sys.executable, "-m", "pip", "install", requirement])
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
