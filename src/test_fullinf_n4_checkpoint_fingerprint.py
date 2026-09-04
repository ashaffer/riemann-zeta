#!/usr/bin/env python3
"""Fail-closed guards for the unrestricted n=4 Arb checkpoint."""

from __future__ import annotations

from pathlib import Path

import pytest

import fullinf_unrestricted_n4_certificate as cert


def test_v3_fingerprint_covers_globals_and_dependency_versions(monkeypatch) -> None:
    baseline = cert.cache_integrand_fingerprint_sha256()

    with monkeypatch.context() as patch:
        patch.setattr(cert, "A_HALF_WIDTH", cert.Q(3, 4))
        assert cert.cache_integrand_fingerprint_sha256() != baseline

    with monkeypatch.context() as patch:
        patch.setattr(cert, "PRIME_2", cert.A(0))
        assert cert.cache_integrand_fingerprint_sha256() != baseline

    with monkeypatch.context() as patch:
        changed = list(cert._ODD_DOUBLE_FACTORIAL)
        changed[0] += 1
        patch.setattr(cert, "_ODD_DOUBLE_FACTORIAL", changed)
        assert cert.cache_integrand_fingerprint_sha256() != baseline

    with monkeypatch.context() as patch:
        patch.setattr(cert.flint, "__version__", "changed-for-regression-test")
        assert cert.cache_integrand_fingerprint_sha256() != baseline


def test_pinned_legacy_checkpoint_is_accepted_only_for_exact_state(tmp_path: Path) -> None:
    assert cert.checkpoint_metadata()["version"] == 3
    assert cert.legacy_v2_checkpoint_metadata()["version"] == 2
    cert.validate_legacy_v2_checkpoint(cert.DEFAULT_CHECKPOINT)

    copied = tmp_path / "legacy.jsonl"
    copied.write_bytes(cert.DEFAULT_CHECKPOINT.read_bytes())
    with pytest.raises(ArithmeticError, match="pinned path"):
        cert.validate_legacy_v2_checkpoint(copied)


def test_new_empty_checkpoint_uses_v3_metadata(tmp_path: Path) -> None:
    path = tmp_path / "v3.jsonl"
    handle = cert.open_checkpoint(path)
    handle.close()
    assert cert.load_checkpoint(path, []) == {}
