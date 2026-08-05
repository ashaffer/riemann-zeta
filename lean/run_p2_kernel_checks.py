#!/usr/bin/env python3
# Copyright (c) 2026 Riemann-Zeta project contributors.
# Released under Apache 2.0 license as described in the repository LICENSE.
"""Run canonical-p=2 Lean source checks and record auditable metrics.

Targets are interpreted relative to ``lean/rhbridge``.  Explicit absolute paths
are also accepted when they resolve inside that package.  Glob patterns are
expanded by Python, never by a shell, and every selected file must be a Lean
source whose basename contains ``P2``.

Examples (quote globs so this program expands them):

    python3 lean/run_p2_kernel_checks.py \
        RHBridge/P2RoundedSphericalOuterCheck5.lean
    python3 lean/run_p2_kernel_checks.py --timeout 2400 \
        'RHBridge/P2RoundedSphericalOuterCheck[5-9].lean'

Before trusting a resume hit or checking a leaf, the runner asks Lake (with
``--rehash --no-build``) to verify that every locally resolvable transitive
import artifact is current.  Thus a direct ``lake env lean SOURCE`` cannot
silently consume a stale local ``.olean``.  ``--with-dependencies`` first asks
Lake to build the transitive p=2 imports in topological order (their own imports
are refreshed by Lake); without it, stale imports are rejected with remediation
rather than rebuilt implicitly.

For each non-skipped leaf the runner executes exactly one recorded check from
``lean/rhbridge``: normally ``lake env lean SOURCE``, or, with
``--with-dependencies``, ``lake --rehash build +MODULE:olean`` so the selected
leaf is not elaborated twice and its ``.olean``/``.ilean`` are current.  GNU
``timeout`` enforces the per-source limit and GNU ``time -v`` records maximum
RSS.  An append-only JSONL log provides resumability.  A previous success is
reused only when the source and its locally resolvable transitive
imports/configuration have the same fingerprint and the import-artifact
preflight succeeds.  Direct-check successes and artifact-building successes are
distinct resume modes; a build-mode hit also requires Lake to certify the
selected target artifact itself as current.

Dependency refresh is always serial.  ``--jobs 2`` is available only with
``--with-dependencies`` and runs at most two dependency-independent timed leaf
builds; the default remains one leaf at a time.

All runner state defaults to ``lean/p2-kernel-check-state``.  Artifact paths are
rejected if they resolve inside any Lean proof package, and output files are
created with unique names.  The runner never edits or deletes Lean sources.
"""

from __future__ import annotations

import argparse
from concurrent.futures import Future, ThreadPoolExecutor, wait, FIRST_COMPLETED
import datetime as dt
import fcntl
import glob
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import uuid
from dataclasses import dataclass
from typing import Sequence, TextIO


SCHEMA_VERSION = 1
FINGERPRINT_VERSION = 1
SCRIPT_PATH = Path(__file__).resolve()
LEAN_DIR = SCRIPT_PATH.parent
PACKAGE_ROOT = LEAN_DIR / "rhbridge"
LOCAL_PACKAGE_ROOTS = (
    PACKAGE_ROOT,
    LEAN_DIR / "glide",
    LEAN_DIR / "weilcert",
)
DEFAULT_STATE_DIR = LEAN_DIR / "p2-kernel-check-state"
DEFAULT_LOG = DEFAULT_STATE_DIR / "checks.jsonl"
DEFAULT_OUTPUT_DIR = DEFAULT_STATE_DIR / "output"
GLOBAL_LOCK = DEFAULT_STATE_DIR / "runner.lock"
CONFIG_NAMES = ("lean-toolchain", "lakefile.toml", "lake-manifest.json")
MODULE_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*$")


class UsageError(Exception):
    """A safe-to-report command-line or target validation error."""


@dataclass(frozen=True)
class Target:
    path: Path
    relative: str


@dataclass(frozen=True)
class LocalModule:
    name: str
    source: Path
    package_root: Path


@dataclass(frozen=True)
class Metrics:
    exit_code: int
    wall_seconds: float
    gnu_time_wall_seconds: float | None
    max_rss_kb: int | None
    time_exit_status: int | None
    timed_out: bool
    watchdog_killed: bool
    cancelled_by_fail_fast: bool


@dataclass(frozen=True)
class LeafPlan:
    ordinal: int
    total: int
    target: Target
    source_sha: str
    dependency_fingerprint: str
    local_dependency_sources: frozenset[Path]


@dataclass(frozen=True)
class RunningLeaf:
    plan: LeafPlan
    output_path: Path
    metrics_path: Path
    started_at: str


class Fingerprinter:
    """Fingerprint a source and all locally resolvable Lean imports."""

    def __init__(self) -> None:
        self._bytes_cache: dict[Path, tuple[tuple[int, ...], str]] = {}
        self._imports_cache: dict[Path, tuple[tuple[int, ...], tuple[str, ...]]] = {}

    @staticmethod
    def _stat_key(path: Path) -> tuple[int, ...]:
        stat = path.stat()
        return (
            stat.st_dev,
            stat.st_ino,
            stat.st_size,
            stat.st_mtime_ns,
            stat.st_ctime_ns,
        )

    def _sha256(self, path: Path) -> str:
        key = self._stat_key(path)
        cached = self._bytes_cache.get(path)
        if cached is not None and cached[0] == key:
            return cached[1]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        self._bytes_cache[path] = (key, digest)
        return digest

    def _imports(self, path: Path) -> tuple[str, ...]:
        key = self._stat_key(path)
        cached = self._imports_cache.get(path)
        if cached is not None and cached[0] == key:
            return cached[1]
        text = path.read_text(encoding="utf-8")
        uncommented = _strip_lean_comments(text)
        modules: list[str] = []
        for line in uncommented.splitlines():
            stripped = line.strip()
            if not stripped.startswith("import "):
                continue
            for token in stripped[len("import ") :].split():
                if MODULE_RE.fullmatch(token):
                    modules.append(token)
        result = tuple(modules)
        self._imports_cache[path] = (key, result)
        return result

    def fingerprint(self, source: Path) -> tuple[str, str]:
        sources: set[Path] = set()
        unresolved: set[str] = set()
        visiting: set[Path] = set()

        def visit(path: Path) -> None:
            path = path.resolve()
            if path in sources or path in visiting:
                return
            visiting.add(path)
            sources.add(path)
            for module in self._imports(path):
                imported = _resolve_local_module(module)
                if imported is None:
                    unresolved.add(module)
                else:
                    visit(imported)
            visiting.remove(path)

        visit(source)
        configs = [
            root / name
            for root in LOCAL_PACKAGE_ROOTS
            for name in CONFIG_NAMES
            if (root / name).is_file()
        ]

        digest = hashlib.sha256()
        digest.update(f"p2-kernel-fingerprint-v{FINGERPRINT_VERSION}\0".encode())
        for path in sorted(sources | set(configs), key=_stable_path_label):
            digest.update(_stable_path_label(path).encode("utf-8"))
            digest.update(b"\0")
            digest.update(self._sha256(path).encode("ascii"))
            digest.update(b"\0")
        for module in sorted(unresolved):
            digest.update(b"external-module\0")
            digest.update(module.encode("utf-8"))
            digest.update(b"\0")
        return self._sha256(source), digest.hexdigest()

    def local_dependencies(self, source: Path) -> tuple[LocalModule, ...]:
        """Return local transitive imports, dependencies first, excluding source."""

        root = source.resolve()
        visited: set[Path] = set()
        visiting: set[Path] = {root}
        ordered: list[LocalModule] = []

        def visit(module: LocalModule) -> None:
            path = module.source.resolve()
            if path in visited or path in visiting:
                return
            visiting.add(path)
            for imported_name in self._imports(path):
                imported = _resolve_local_module_info(imported_name)
                if imported is not None:
                    visit(imported)
            visiting.remove(path)
            visited.add(path)
            ordered.append(module)

        for imported_name in self._imports(root):
            imported = _resolve_local_module_info(imported_name)
            if imported is not None:
                visit(imported)
        return tuple(ordered)


def _strip_lean_comments(text: str) -> str:
    """Remove nested Lean comments while preserving line boundaries."""

    output: list[str] = []
    index = 0
    block_depth = 0
    while index < len(text):
        pair = text[index : index + 2]
        if block_depth:
            if pair == "/-":
                block_depth += 1
                output.extend("  ")
                index += 2
            elif pair == "-/":
                block_depth -= 1
                output.extend("  ")
                index += 2
            else:
                output.append("\n" if text[index] == "\n" else " ")
                index += 1
        elif pair == "/-":
            block_depth = 1
            output.extend("  ")
            index += 2
        elif pair == "--":
            while index < len(text) and text[index] != "\n":
                output.append(" ")
                index += 1
        else:
            output.append(text[index])
            index += 1
    return "".join(output)


def _stable_path_label(path: Path) -> str:
    try:
        return path.resolve().relative_to(LEAN_DIR).as_posix()
    except ValueError:
        return str(path.resolve())


def _resolve_local_module_info(module: str) -> LocalModule | None:
    relative = Path(*module.split(".")).with_suffix(".lean")
    for root in LOCAL_PACKAGE_ROOTS:
        candidate = (root / relative).resolve()
        if candidate.is_file() and _is_within(candidate, root.resolve()):
            return LocalModule(module, candidate, root.resolve())
    return None


def _resolve_local_module(module: str) -> Path | None:
    resolved = _resolve_local_module_info(module)
    return None if resolved is None else resolved.source


def _dependency_plan(
    fingerprinter: Fingerprinter,
    targets: Sequence[Target],
) -> list[LocalModule]:
    """Merge per-leaf topological import orders without losing dependencies."""

    ordered: list[LocalModule] = []
    seen: set[Path] = set()
    for target in targets:
        for module in fingerprinter.local_dependencies(target.path):
            if module.source not in seen:
                ordered.append(module)
                seen.add(module.source)
    return ordered


def _is_p2_module(module: LocalModule) -> bool:
    return "P2" in module.source.stem


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _is_p2_source(path: Path) -> bool:
    try:
        relative = path.relative_to(PACKAGE_ROOT.resolve())
    except ValueError:
        return False
    return (
        path.is_file()
        and path.suffix == ".lean"
        and "P2" in path.stem
        and ".lake" not in relative.parts
    )


def _has_glob_magic(value: str) -> bool:
    return glob.has_magic(value)


def _validate_glob(pattern: str) -> None:
    if not pattern or "\0" in pattern:
        raise UsageError("empty or NUL-containing target pattern")
    path = Path(pattern)
    if path.is_absolute() or pattern.startswith("~"):
        raise UsageError(f"glob must be relative to lean/rhbridge: {pattern!r}")
    if ".." in path.parts:
        raise UsageError(f"glob may not contain '..': {pattern!r}")


def _normalize_candidate(path: Path, original: str) -> Target:
    resolved = path.resolve()
    if not _is_within(resolved, PACKAGE_ROOT.resolve()):
        raise UsageError(f"target escapes lean/rhbridge: {original!r}")
    if not _is_p2_source(resolved):
        raise UsageError(
            f"target is not an existing p=2 Lean source (*P2*.lean): {original!r}"
        )
    relative = resolved.relative_to(PACKAGE_ROOT.resolve()).as_posix()
    return Target(resolved, relative)


def _expand_targets(values: Sequence[str]) -> list[Target]:
    selected: list[Target] = []
    seen: set[Path] = set()
    for value in values:
        if _has_glob_magic(value):
            _validate_glob(value)
            try:
                matches = sorted(PACKAGE_ROOT.glob(value), key=lambda item: item.as_posix())
            except (OSError, ValueError) as error:
                raise UsageError(f"invalid glob {value!r}: {error}") from error
            p2_matches = [path for path in matches if _is_p2_source(path.resolve())]
            if not p2_matches:
                raise UsageError(f"glob matched no p=2 Lean sources: {value!r}")
            candidates = p2_matches
        else:
            raw = Path(value)
            if raw.is_absolute():
                candidates = [raw]
            else:
                cwd_candidate = (Path.cwd() / raw)
                candidates = [cwd_candidate if cwd_candidate.exists() else PACKAGE_ROOT / raw]
        for candidate in candidates:
            target = _normalize_candidate(candidate, value)
            if target.path not in seen:
                selected.append(target)
                seen.add(target.path)
    return selected


def _validate_artifact_path(path: Path, description: str) -> Path:
    resolved = path.expanduser().resolve()
    for package in LOCAL_PACKAGE_ROOTS:
        if _is_within(resolved, package.resolve()):
            raise UsageError(f"{description} may not be inside proof package {package}")
    return resolved


def _record_check_mode(record: dict[str, object]) -> str | None:
    mode = record.get("check_mode")
    if isinstance(mode, str) and mode in {"direct", "lake_build"}:
        return mode
    command = record.get("command")
    if not isinstance(command, list) or not all(
        isinstance(part, str) for part in command
    ):
        return None
    if command[:3] == ["lake", "env", "lean"]:
        return "direct"
    if command[:3] == ["lake", "--rehash", "build"]:
        return "lake_build"
    return None


def _load_successes(log_path: Path) -> set[tuple[str, str, str]]:
    successes: set[tuple[str, str, str]] = set()
    if not log_path.exists():
        return successes
    if not log_path.is_file():
        raise UsageError(f"JSONL log is not a regular file: {log_path}")
    malformed = 0
    with log_path.open("r", encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                malformed += 1
                continue
            if (
                isinstance(record, dict)
                and record.get("schema_version") == SCHEMA_VERSION
                and record.get("status") == "success"
                and record.get("exit_code") == 0
                and isinstance(record.get("source"), str)
                and isinstance(record.get("dependency_fingerprint"), str)
            ):
                mode = _record_check_mode(record)
                if mode is not None:
                    successes.add(
                        (record["source"], record["dependency_fingerprint"], mode)
                    )
    if malformed:
        print(
            f"warning: ignored {malformed} malformed JSONL line(s) in {log_path}",
            file=sys.stderr,
        )
    return successes


def _parse_elapsed(value: str) -> float | None:
    try:
        total = 0.0
        for part in value.strip().split(":"):
            total = total * 60.0 + float(part)
        return total
    except ValueError:
        return None


def _parse_time_metrics(path: Path) -> tuple[float | None, int | None, int | None]:
    elapsed: float | None = None
    max_rss: int | None = None
    exit_status: int | None = None
    if not path.is_file():
        return elapsed, max_rss, exit_status
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if stripped.startswith("Elapsed (wall clock) time"):
            elapsed = _parse_elapsed(stripped.rsplit(": ", 1)[-1])
        elif stripped.startswith("Maximum resident set size (kbytes):"):
            try:
                max_rss = int(stripped.rsplit(":", 1)[1].strip())
            except ValueError:
                pass
        elif stripped.startswith("Exit status:"):
            try:
                exit_status = int(stripped.rsplit(":", 1)[1].strip())
            except ValueError:
                pass
    return elapsed, max_rss, exit_status


def _unique_artifacts(output_dir: Path, target: Target, ordinal: int) -> tuple[Path, Path]:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    safe_stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", Path(target.relative).stem)[:100]
    nonce = uuid.uuid4().hex[:10]
    prefix = f"{stamp}_{ordinal:04d}_{safe_stem}_{nonce}"
    output_path = output_dir / f"{prefix}.log"
    metrics_path = output_dir / f"{prefix}.time"
    output_path.touch(exist_ok=False)
    metrics_path.touch(exist_ok=False)
    return output_path, metrics_path


def _process_group_exists(pgid: int) -> bool:
    """Return whether a process group still has at least one member."""

    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # All runner children have our uid.  Treat an unexpected permission
        # failure conservatively as a live group so cleanup still escalates.
        return True
    return True


def _wait_for_process_group_exit(
    process: subprocess.Popen[bytes], pgid: int, timeout_seconds: float
) -> bool:
    """Wait boundedly for every member of pgid, not merely its leader."""

    deadline = time.monotonic() + timeout_seconds
    while True:
        # Reap the Popen child as soon as it exits.  Otherwise the group leader
        # can remain a zombie and make killpg(pgid, 0) look live forever.
        process.poll()
        if not _process_group_exists(pgid):
            return True
        remaining = deadline - time.monotonic()
        if remaining <= 0.0:
            return False
        time.sleep(min(0.05, remaining))


def _terminate_process_group(
    process: subprocess.Popen[bytes],
    *,
    term_grace_seconds: float = 5.0,
    kill_grace_seconds: float = 5.0,
) -> None:
    """TERM a spawned leaf group, then KILL any surviving descendants."""

    # Every caller starts a new session, so the Popen pid is also the initial
    # process-group id.  Do not return merely because that leader has exited:
    # timeout/lake/lean descendants may still occupy the same group.
    pgid = process.pid
    try:
        os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError:
        process.poll()
        return
    if not _wait_for_process_group_exit(process, pgid, term_grace_seconds):
        try:
            os.killpg(pgid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        else:
            _wait_for_process_group_exit(process, pgid, kill_grace_seconds)
    process.poll()


class ActiveRunController:
    """Track leaf process groups for fail-fast and interrupt cancellation."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._states: dict[int, str] = {}
        self._processes: dict[int, subprocess.Popen[bytes]] = {}

    def reserve(self, key: int) -> None:
        with self._lock:
            self._states[key] = "pending"

    def register(self, key: int, process: subprocess.Popen[bytes]) -> None:
        with self._lock:
            state = self._states.get(key, "pending")
            self._processes[key] = process
            should_cancel = state == "cancelled"
            if not should_cancel:
                self._states[key] = "active"
        if should_cancel:
            _terminate_process_group(process)

    def finish(self, key: int) -> None:
        with self._lock:
            self._processes.pop(key, None)
            if self._states.get(key) != "cancelled":
                self._states[key] = "done"

    def cancel(self, key: int) -> bool:
        """Request cancellation, returning whether work was still outstanding."""

        process: subprocess.Popen[bytes] | None = None
        with self._lock:
            state = self._states.get(key)
            if state in {None, "done", "cancelled"}:
                return False
            process = self._processes.get(key)
            self._states[key] = "cancelled"
        if process is not None:
            _terminate_process_group(process)
        return True

    def cancel_all(self) -> int:
        """Cancel every pending or active leaf and return the request count."""

        with self._lock:
            keys = [
                key
                for key, state in self._states.items()
                if state in {"pending", "active"}
            ]
        return sum(1 for key in keys if self.cancel(key))

    def was_cancelled(self, key: int) -> bool:
        with self._lock:
            return self._states.get(key) == "cancelled"


def _run_lake_action(
    lake_args: Sequence[str],
    package_root: Path,
    timeout_seconds: float,
    *,
    capture_output: bool,
) -> tuple[int, str, bool]:
    """Run one bounded Lake action; callers serialize all such actions."""

    duration = f"{timeout_seconds:.6f}s"
    command = [
        "/usr/bin/timeout",
        "--signal=TERM",
        "--kill-after=10s",
        duration,
        "lake",
        *lake_args,
    ]
    environment = os.environ.copy()
    environment["LC_ALL"] = "C"
    try:
        process = subprocess.Popen(
            command,
            cwd=package_root,
            env=environment,
            stdout=subprocess.PIPE if capture_output else None,
            stderr=subprocess.STDOUT if capture_output else None,
            start_new_session=True,
        )
    except OSError as error:
        raise UsageError(f"could not start Lake in {package_root}: {error}") from error

    watchdog_killed = False
    try:
        output, _ = process.communicate(timeout=timeout_seconds + 30.0)
    except subprocess.TimeoutExpired:
        watchdog_killed = True
        _terminate_process_group(process)
        output, _ = process.communicate()
    except KeyboardInterrupt:
        _terminate_process_group(process)
        raise
    exit_code = process.returncode if process.returncode is not None else 125
    timed_out = watchdog_killed or exit_code == 124
    decoded = output.decode("utf-8", errors="replace") if output is not None else ""
    return exit_code, decoded, timed_out


def _group_by_package(
    modules: Sequence[LocalModule],
) -> list[tuple[Path, list[LocalModule]]]:
    grouped: dict[Path, list[LocalModule]] = {}
    for module in modules:
        grouped.setdefault(module.package_root, []).append(module)
    return list(grouped.items())


def _summarize(values: Sequence[str], limit: int = 8) -> str:
    shown = list(values[:limit])
    if len(values) > limit:
        shown.append(f"... ({len(values) - limit} more)")
    return ", ".join(shown)


def _build_local_dependencies(
    modules: Sequence[LocalModule],
    timeout_seconds: float,
) -> None:
    """Refresh local imports one at a time in dependency-first order."""

    for ordinal, module in enumerate(modules, start=1):
        print(
            f"[dependency {ordinal}/{len(modules)}] BUILD {module.name}",
            flush=True,
        )
        exit_code, output, timed_out = _run_lake_action(
            ["--quiet", "--rehash", "build", f"+{module.name}:olean"],
            module.package_root,
            timeout_seconds,
            capture_output=True,
        )
        if exit_code != 0:
            reason = "timed out" if timed_out else f"exited with status {exit_code}"
            details = output.strip()
            if len(details) > 4000:
                details = "..." + details[-3997:]
            raise UsageError(
                f"dependency build for {module.name} {reason}; "
                "no dependent leaf was checked"
                + (f"\nLake output:\n{details}" if details else "")
            )


def _verify_local_dependency_artifacts(
    modules: Sequence[LocalModule],
    timeout_seconds: float,
) -> None:
    """Use Lake's content hashes/traces to reject stale local import artifacts."""

    for package_root, package_modules in _group_by_package(modules):
        targets = [f"+{module.name}:olean" for module in package_modules]
        exit_code, output, timed_out = _run_lake_action(
            ["--rehash", "--no-build", "build", *targets],
            package_root,
            timeout_seconds,
            capture_output=True,
        )
        if exit_code == 0:
            continue
        module_names = _summarize([module.name for module in package_modules])
        reason = "preflight timed out" if timed_out else "preflight rejected the artifacts"
        details = output.strip()
        if len(details) > 4000:
            details = "..." + details[-3997:]
        if not details:
            details = "Lake emitted no diagnostic output."
        raise UsageError(
            f"{reason} for local imports [{module_names}] in {package_root}.\n"
            "The affected leaf was not checked: direct `lake env lean` could "
            "otherwise consume a stale `.olean`.\n"
            "Remediation: rerun this runner with `--with-dependencies`; the "
            f"dry-run plan lists exact serial build targets for {package_root}.\n"
            f"Lake output:\n{details}"
        )


def _target_module_name(target: Target) -> str:
    return ".".join(Path(target.relative).with_suffix("").parts)


def _check_mode(with_dependencies: bool) -> str:
    return "lake_build" if with_dependencies else "direct"


def _leaf_command(target: Target, with_dependencies: bool) -> list[str]:
    if with_dependencies:
        return [
            "lake",
            "--rehash",
            "build",
            f"+{_target_module_name(target)}:olean",
        ]
    return ["lake", "env", "lean", target.relative]


def _target_artifact_is_current(target: Target, timeout_seconds: float) -> bool:
    """Return false only for Lake's documented no-build/stale exit status."""

    lake_target = f"+{_target_module_name(target)}:olean"
    exit_code, output, timed_out = _run_lake_action(
        ["--rehash", "--no-build", "build", lake_target],
        PACKAGE_ROOT,
        timeout_seconds,
        capture_output=True,
    )
    if exit_code == 0:
        return True
    if exit_code == 3:
        return False
    reason = "timed out" if timed_out else f"exited with status {exit_code}"
    details = output.strip()
    if len(details) > 4000:
        details = "..." + details[-3997:]
    raise UsageError(
        f"could not validate resume artifact {lake_target}: Lake {reason}.\n"
        f"Lake output:\n{details or 'Lake emitted no diagnostic output.'}"
    )


def _prepare_leaf_plan(
    target: Target,
    ordinal: int,
    total: int,
    fingerprinter: Fingerprinter,
    successes: set[tuple[str, str, str]],
    *,
    no_resume: bool,
    with_dependencies: bool,
    check_mode: str,
    timeout_seconds: float,
    verify_dependencies: bool,
) -> LeafPlan | None:
    # Refresh immediately before either trusting a resume hit or scheduling a
    # recorded check; source generation may have happened after initial setup.
    source_sha, dependency_fingerprint = fingerprinter.fingerprint(target.path)
    local_dependencies = fingerprinter.local_dependencies(target.path)
    if verify_dependencies:
        _verify_local_dependency_artifacts(local_dependencies, timeout_seconds)
    skip = (
        not no_resume
        and (target.relative, dependency_fingerprint, check_mode) in successes
    )
    if (
        skip
        and with_dependencies
        and not _target_artifact_is_current(target, timeout_seconds)
    ):
        print(
            f"[{ordinal}/{total}] RESUME MISS {target.relative}: "
            "target artifact is stale or missing",
            flush=True,
        )
        skip = False
    if skip:
        print(f"[{ordinal}/{total}] SKIP {target.relative}")
        return None
    return LeafPlan(
        ordinal=ordinal,
        total=total,
        target=target,
        source_sha=source_sha,
        dependency_fingerprint=dependency_fingerprint,
        local_dependency_sources=frozenset(
            module.source for module in local_dependencies
        ),
    )


def _leaves_independent(left: LeafPlan, right: LeafPlan) -> bool:
    return (
        left.target.path not in right.local_dependency_sources
        and right.target.path not in left.local_dependency_sources
    )


def _run_one(
    target: Target,
    timeout_seconds: float,
    output_path: Path,
    metrics_path: Path,
    with_dependencies: bool,
    controller: ActiveRunController | None = None,
    run_key: int | None = None,
) -> Metrics:
    duration = f"{timeout_seconds:.6f}s"
    leaf_command = _leaf_command(target, with_dependencies)
    command = [
        "/usr/bin/time",
        "-v",
        "-a",
        "-o",
        str(metrics_path),
        "/usr/bin/timeout",
        # Without --foreground GNU timeout creates a second process group
        # beneath the /usr/bin/time session leader.  A runner interrupt would
        # then signal only time and leave timeout/lake/lean running.
        "--foreground",
        "--signal=TERM",
        "--kill-after=10s",
        duration,
        *leaf_command,
    ]
    environment = os.environ.copy()
    environment["LC_ALL"] = "C"
    started = time.monotonic()
    watchdog_killed = False
    with output_path.open("ab", buffering=0) as output:
        process: subprocess.Popen[bytes] | None = None
        try:
            # In one-job mode SIGINT is delivered on this spawning thread.  A
            # tiny Popen-to-register gap would otherwise permit an untracked
            # child.  Restore the mask immediately after registration; a
            # pending SIGINT is then raised inside this cleanup-protected try.
            previous_mask = signal.pthread_sigmask(
                signal.SIG_BLOCK, {signal.SIGINT}
            )
            try:
                process = subprocess.Popen(
                    command,
                    cwd=PACKAGE_ROOT,
                    env=environment,
                    stdout=output,
                    stderr=subprocess.STDOUT,
                    start_new_session=True,
                )
                if controller is not None and run_key is not None:
                    controller.register(run_key, process)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, previous_mask)
            process.wait(timeout=timeout_seconds + 30.0)
        except subprocess.TimeoutExpired:
            watchdog_killed = True
        except BaseException:
            if controller is not None and run_key is not None:
                controller.cancel(run_key)
            raise
        finally:
            # This is intentionally unconditional.  Besides interrupts and
            # watchdog expiry it removes any descendant that outlives a
            # normally exiting time/timeout leader.
            if process is not None:
                _terminate_process_group(process)
            if controller is not None and run_key is not None:
                controller.finish(run_key)
    assert process is not None
    wall_seconds = time.monotonic() - started
    elapsed, max_rss, time_exit_status = _parse_time_metrics(metrics_path)
    exit_code = process.returncode if process.returncode is not None else 125
    timed_out = (
        watchdog_killed
        or exit_code == 124
        or (wall_seconds >= timeout_seconds and exit_code in {137, 143})
    )
    return Metrics(
        exit_code=exit_code,
        wall_seconds=wall_seconds,
        gnu_time_wall_seconds=elapsed,
        max_rss_kb=max_rss,
        time_exit_status=time_exit_status,
        timed_out=timed_out,
        watchdog_killed=watchdog_killed,
        cancelled_by_fail_fast=(
            controller is not None
            and run_key is not None
            and controller.was_cancelled(run_key)
        ),
    )


def _iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def _relative_artifact(path: Path) -> str:
    try:
        return path.relative_to(LEAN_DIR.parent).as_posix()
    except ValueError:
        return str(path)


def _append_record(stream: TextIO, record: dict[str, object]) -> None:
    # The caller holds the global runner lock.  Flush and fsync make a completed
    # success durable enough to resume after a later interrupted check.
    stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
    stream.flush()
    os.fsync(stream.fileno())


def _record_leaf_result(
    running: RunningLeaf,
    metrics: Metrics,
    fingerprinter: Fingerprinter,
    log_stream: TextIO,
    run_id: str,
    timeout_seconds: float,
    with_dependencies: bool,
    check_mode: str,
) -> str:
    plan = running.plan
    after_source_sha, after_fingerprint = fingerprinter.fingerprint(plan.target.path)
    inputs_changed = (
        after_source_sha != plan.source_sha
        or after_fingerprint != plan.dependency_fingerprint
    )
    if metrics.cancelled_by_fail_fast:
        status = "cancelled_by_fail_fast"
    elif inputs_changed:
        status = "inputs_changed"
    elif metrics.timed_out:
        status = "timeout"
    elif metrics.max_rss_kb is None:
        status = "metrics_missing"
    elif metrics.exit_code == 0:
        status = "success"
    else:
        status = "failure"

    record: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "fingerprint_version": FINGERPRINT_VERSION,
        "run_id": run_id,
        "source": plan.target.relative,
        "source_sha256": plan.source_sha,
        "dependency_fingerprint": plan.dependency_fingerprint,
        "post_dependency_fingerprint": after_fingerprint,
        "status": status,
        "exit_code": metrics.exit_code,
        "time_exit_status": metrics.time_exit_status,
        "timed_out": metrics.timed_out,
        "watchdog_killed": metrics.watchdog_killed,
        "cancelled_by_fail_fast": metrics.cancelled_by_fail_fast,
        "timeout_seconds": timeout_seconds,
        "wall_seconds": round(metrics.wall_seconds, 6),
        "gnu_time_wall_seconds": metrics.gnu_time_wall_seconds,
        "max_rss_kb": metrics.max_rss_kb,
        "started_at": running.started_at,
        "finished_at": _iso_now(),
        "check_mode": check_mode,
        "command": _leaf_command(plan.target, with_dependencies),
        "working_directory": _stable_path_label(PACKAGE_ROOT),
        "output_log": _relative_artifact(running.output_path),
        "time_log": _relative_artifact(running.metrics_path),
    }
    _append_record(log_stream, record)
    rss = (
        f", max RSS {metrics.max_rss_kb / 1024:.1f} MiB"
        if metrics.max_rss_kb is not None
        else ""
    )
    print(
        f"[{plan.ordinal}/{plan.total}] {status.upper()} "
        f"exit {metrics.exit_code}, {metrics.wall_seconds:.2f}s{rss}"
    )
    return status


def _run_one_leaf_job_at_a_time(
    targets: Sequence[Target],
    fingerprinter: Fingerprinter,
    successes: set[tuple[str, str, str]],
    output_dir: Path,
    log_stream: TextIO,
    run_id: str,
    *,
    timeout_seconds: float,
    no_resume: bool,
    fail_fast: bool,
    with_dependencies: bool,
    check_mode: str,
    controller: ActiveRunController,
) -> tuple[int, int, int, int]:
    succeeded = 0
    skipped = 0
    failures = 0
    total = len(targets)
    for ordinal, target in enumerate(targets, start=1):
        plan = _prepare_leaf_plan(
            target,
            ordinal,
            total,
            fingerprinter,
            successes,
            no_resume=no_resume,
            with_dependencies=with_dependencies,
            check_mode=check_mode,
            timeout_seconds=timeout_seconds,
            verify_dependencies=not with_dependencies,
        )
        if plan is None:
            skipped += 1
            continue

        output_path, metrics_path = _unique_artifacts(
            output_dir, target, ordinal
        )
        running = RunningLeaf(
            plan=plan,
            output_path=output_path,
            metrics_path=metrics_path,
            started_at=_iso_now(),
        )
        leaf_action = "BUILD" if with_dependencies else "RUN  "
        print(
            f"[{ordinal}/{total}] {leaf_action} {target.relative} "
            f"(timeout {timeout_seconds:g}s)",
            flush=True,
        )
        controller.reserve(plan.ordinal)
        metrics = _run_one(
            target,
            timeout_seconds,
            output_path,
            metrics_path,
            with_dependencies,
            controller,
            plan.ordinal,
        )
        status = _record_leaf_result(
            running,
            metrics,
            fingerprinter,
            log_stream,
            run_id,
            timeout_seconds,
            with_dependencies,
            check_mode,
        )
        if status == "success":
            succeeded += 1
        else:
            failures += 1
            if fail_fast:
                break
    return succeeded, skipped, failures, 0


def _run_two_leaf_jobs(
    targets: Sequence[Target],
    fingerprinter: Fingerprinter,
    successes: set[tuple[str, str, str]],
    output_dir: Path,
    log_stream: TextIO,
    run_id: str,
    *,
    timeout_seconds: float,
    no_resume: bool,
    fail_fast: bool,
    check_mode: str,
    controller: ActiveRunController,
) -> tuple[int, int, int, int]:
    """Run independent artifact-building leaves with a hard two-worker bound."""

    total = len(targets)
    plans: list[LeafPlan] = []
    skipped = 0
    # All preflights remain serial.  Only the final timed leaf commands below
    # enter the two-worker executor.
    for ordinal, target in enumerate(targets, start=1):
        plan = _prepare_leaf_plan(
            target,
            ordinal,
            total,
            fingerprinter,
            successes,
            no_resume=no_resume,
            with_dependencies=True,
            check_mode=check_mode,
            timeout_seconds=timeout_seconds,
            verify_dependencies=False,
        )
        if plan is None:
            skipped += 1
        else:
            plans.append(plan)

    succeeded = 0
    failures = 0
    cancelled = 0
    pending = list(plans)
    active: dict[Future[Metrics], RunningLeaf] = {}
    fail_fast_triggered = False

    def launch(plan: LeafPlan, executor: ThreadPoolExecutor) -> None:
        output_path, metrics_path = _unique_artifacts(
            output_dir, plan.target, plan.ordinal
        )
        running = RunningLeaf(
            plan=plan,
            output_path=output_path,
            metrics_path=metrics_path,
            started_at=_iso_now(),
        )
        print(
            f"[{plan.ordinal}/{plan.total}] BUILD {plan.target.relative} "
            f"(timeout {timeout_seconds:g}s)",
            flush=True,
        )
        controller.reserve(plan.ordinal)
        future = executor.submit(
            _run_one,
            plan.target,
            timeout_seconds,
            output_path,
            metrics_path,
            True,
            controller,
            plan.ordinal,
        )
        active[future] = running

    def next_independent_index() -> int | None:
        for index, plan in enumerate(pending):
            if all(
                _leaves_independent(plan, running.plan)
                for running in active.values()
            ):
                return index
        return None

    executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="p2-leaf")
    try:
        while pending or active:
            if fail_fast_triggered and not active:
                break
            while not fail_fast_triggered and len(active) < 2 and pending:
                index = next_independent_index()
                if index is None:
                    break
                launch(pending.pop(index), executor)
            if not active:
                # With no active leaf, the first pending leaf is vacuously
                # independent.  This branch is defensive against a future
                # change to the selection predicate.
                if pending and not fail_fast_triggered:
                    launch(pending.pop(0), executor)
                else:
                    break

            completed, _not_done = wait(active, return_when=FIRST_COMPLETED)
            for future in sorted(
                completed, key=lambda item: active[item].plan.ordinal
            ):
                running = active.pop(future)
                metrics = future.result()
                status = _record_leaf_result(
                    running,
                    metrics,
                    fingerprinter,
                    log_stream,
                    run_id,
                    timeout_seconds,
                    True,
                    check_mode,
                )
                if status == "success":
                    succeeded += 1
                elif status == "cancelled_by_fail_fast":
                    cancelled += 1
                else:
                    failures += 1
                    if fail_fast:
                        fail_fast_triggered = True

            if fail_fast_triggered:
                for running in active.values():
                    controller.cancel(running.plan.ordinal)
    except BaseException:
        for running in active.values():
            controller.cancel(running.plan.ordinal)
        for future in active:
            try:
                future.result()
            except BaseException:
                pass
        raise
    finally:
        executor.shutdown(wait=True, cancel_futures=False)

    return succeeded, skipped, failures, cancelled


def _acquire_lock() -> object:
    DEFAULT_STATE_DIR.mkdir(parents=True, exist_ok=True)
    lock_stream = GLOBAL_LOCK.open("a+", encoding="utf-8")
    try:
        fcntl.flock(lock_stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as error:
        lock_stream.close()
        raise UsageError(
            f"another p=2 kernel-check runner holds {GLOBAL_LOCK}"
        ) from error
    return lock_stream


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Kernel-check canonical-p=2 Lean sources with resumable metrics.",
    )
    parser.add_argument(
        "targets",
        nargs="+",
        metavar="SOURCE_OR_GLOB",
        help="*P2*.lean source or quoted glob, relative to lean/rhbridge",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=1800.0,
        metavar="SECONDS",
        help="wall timeout applied independently to each source (default: 1800)",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=DEFAULT_LOG,
        help=f"append-only JSONL log (default: {DEFAULT_LOG})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"per-source stdout/time artifacts (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="rerun matching prior successes instead of skipping them",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="stop after the first failed/timed-out source and terminate an active peer",
    )
    parser.add_argument(
        "--with-dependencies",
        action="store_true",
        help=(
            "build locally resolvable transitive p=2 imports in dependency "
            "order before checking selected leaves"
        ),
    )
    parser.add_argument(
        "--jobs",
        type=int,
        choices=(1, 2),
        default=1,
        metavar="{1,2}",
        help=(
            "timed leaf builds to run at once; 2 requires "
            "--with-dependencies (default: 1)"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "resolve, validate, fingerprint, and print dependency actions "
            "without invoking Lake/Lean or writing state"
        ),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    active_runs = ActiveRunController()
    try:
        if not math.isfinite(args.timeout) or not (args.timeout > 0.0):
            raise UsageError("--timeout must be a positive finite number")
        if args.jobs == 2 and not args.with_dependencies:
            raise UsageError("--jobs 2 requires --with-dependencies")
        if not PACKAGE_ROOT.is_dir():
            raise UsageError(f"Lean package not found: {PACKAGE_ROOT}")
        targets = _expand_targets(args.targets)
        log_path = _validate_artifact_path(args.log, "JSONL log")
        output_dir = _validate_artifact_path(args.output_dir, "output directory")
        if log_path.suffix != ".jsonl":
            raise UsageError("--log must end in .jsonl")
        if output_dir.exists() and not output_dir.is_dir():
            raise UsageError(f"output directory is not a directory: {output_dir}")

        successes = set() if args.no_resume else _load_successes(log_path)
        fingerprinter = Fingerprinter()
        check_mode = _check_mode(args.with_dependencies)
        dependency_plan = _dependency_plan(fingerprinter, targets)
        p2_dependency_plan = [
            module for module in dependency_plan if _is_p2_module(module)
        ]
        prepared: list[tuple[Target, str, str, bool]] = []
        for target in targets:
            source_sha, dependency_fingerprint = fingerprinter.fingerprint(target.path)
            skip = (target.relative, dependency_fingerprint, check_mode) in successes
            prepared.append((target, source_sha, dependency_fingerprint, skip))

        if args.dry_run:
            for module in dependency_plan:
                dependency_action = (
                    "BUILD+VERIFY"
                    if args.with_dependencies and _is_p2_module(module)
                    else "VERIFY"
                )
                print(
                    f"{dependency_action}\t{module.name}\t"
                    f"{_stable_path_label(module.source)}"
                )
            for target, _source_sha, dependency_fingerprint, skip in prepared:
                action = (
                    "SKIP"
                    if skip
                    else ("BUILD" if args.with_dependencies else "RUN")
                )
                print(f"{action}\t{target.relative}\t{dependency_fingerprint[:16]}")
            return 0

        for executable in ("lake",):
            if shutil.which(executable) is None:
                raise UsageError(f"required executable is not on PATH: {executable}")
        if not Path("/usr/bin/time").is_file() or not Path("/usr/bin/timeout").is_file():
            raise UsageError("GNU /usr/bin/time and /usr/bin/timeout are required")

        lock_stream = _acquire_lock()
        try:
            if args.with_dependencies:
                # A resumed batch normally has an entirely current import DAG.
                # Let Lake certify that in one read-only pass; only fall back
                # to the deliberately serial rebuild when something is stale.
                try:
                    _verify_local_dependency_artifacts(
                        dependency_plan, args.timeout
                    )
                except UsageError:
                    _build_local_dependencies(
                        p2_dependency_plan, args.timeout
                    )
            log_path.parent.mkdir(parents=True, exist_ok=True)
            output_dir.mkdir(parents=True, exist_ok=True)
            run_id = uuid.uuid4().hex
            with log_path.open("a", encoding="utf-8") as log_stream:
                if args.jobs == 2:
                    succeeded, skipped, failures, cancelled = _run_two_leaf_jobs(
                        targets,
                        fingerprinter,
                        successes,
                        output_dir,
                        log_stream,
                        run_id,
                        timeout_seconds=args.timeout,
                        no_resume=args.no_resume,
                        fail_fast=args.fail_fast,
                        check_mode=check_mode,
                        controller=active_runs,
                    )
                else:
                    succeeded, skipped, failures, cancelled = (
                        _run_one_leaf_job_at_a_time(
                            targets,
                            fingerprinter,
                            successes,
                            output_dir,
                            log_stream,
                            run_id,
                            timeout_seconds=args.timeout,
                            no_resume=args.no_resume,
                            fail_fast=args.fail_fast,
                            with_dependencies=args.with_dependencies,
                            check_mode=check_mode,
                            controller=active_runs,
                        )
                    )
            print(
                f"p=2 checks complete: {succeeded} succeeded, "
                f"{skipped} skipped, {failures} failed, {cancelled} cancelled"
            )
            return 1 if failures or cancelled else 0
        finally:
            lock_stream.close()
    except KeyboardInterrupt:
        active_runs.cancel_all()
        print("interrupted; active process group terminated", file=sys.stderr)
        return 130
    except UsageError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
