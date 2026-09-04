#!/usr/bin/env python3
"""Cross-cache regression tests for the authoritative September route.

These tests check finite algebra and claim-state consistency.  They do not
prove an analytic estimate, a zero-free strip, or RH.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from types import ModuleType

import pytest

import zeta23_proof_tree as zpt


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CONTEXT = RESULTS / "context"


def load_json(name: str) -> dict:
    return json.loads((CONTEXT / name).read_text(encoding="utf-8"))


def load_script(name: str) -> ModuleType:
    path = RESULTS / name
    spec = importlib.util.spec_from_file_location(f"zeta23_test_{path.stem}", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prime_factorization(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def mobius(n: int) -> int:
    factors = prime_factorization(n)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def add_log_vector(total: dict[int, int], vector: dict[int, int], scale: int) -> None:
    for prime, coefficient in vector.items():
        total[prime] = total.get(prime, 0) + scale * coefficient
        if total[prime] == 0:
            del total[prime]


def test_authoritative_verifiers_are_in_default_pytest() -> None:
    for script in (
        "verify_zeta23_r105_r116_r73_adapter_audit.py",
        "verify_zeta23_post_synthesis_decision_path.py",
        "verify_zeta23_correction_closure.py",
        "verify_zeta23_recursive_fixed_point_postflight.py",
        "verify_zeta23_correction_bundle.py",
        "verify_zeta23_current_authority_manifest.py",
    ):
        module = load_script(script)
        module.main()


def test_current_caches_agree_and_old_tree_is_not_default() -> None:
    post = load_json("zeta23_post_synthesis_decision_path_v1.json")
    s0 = load_json("zeta23_r105_r116_r73_adapter_audit_v1.json")
    closure = load_json("zeta23_correction_closure_v1.json")

    for key in ("uniform_zero_free_strip", "riemann_hypothesis", "strip_to_rh_amplifier"):
        assert post["global_status"][key] == s0["global_status"][key]
        assert post["global_status"][key] == closure["global_status"][key]

    stages = {stage["id"]: stage for stage in post["selected_strip_route"]["stages"]}
    assert stages["S0"]["status"] == "COMPLETE_GO_FAILED_BRANCH_SWITCH_FIRED"
    assert s0["s0_verdict"]["first_open_edge"] == "COMPLETE_FIXED_WINDOW_QH_R71_ENERGY"
    assert post["selected_strip_route"]["attack_surface"]["status"] == "OPEN_STRIP_EQUIVALENT_ENDPOINT"
    assert closure["exhaustiveness_status"].startswith("NOT_PROVED")

    current = zpt.current_routing_packet()
    historical = zpt.load_seed()
    assert current["date"] == "2026-09-02"
    assert historical["meta"]["date"] < current["date"]
    assert historical["resume"] == "FQPP"
    assert current["s1"] == "RAW_CANDIDATE_A0_FAILED_BOTH_MECHANISM_CLASSES_UNFORMULATED"
    assert current["next"] == post["next_action"]
    assert set(current["companion_authorities"]) == {
        "results/context/zeta23_r105_r116_r73_adapter_audit_v1.json",
        "results/context/zeta23_correction_closure_v1.json",
    }
    assert current["integrity_manifest"] == (
        "results/context/zeta23_current_authority_manifest_v1.json"
    )
    assert current["reload_context"] == (
        "results/context/zeta23_correction_bundle_v1.z23v"
    )
    assert current["reload_command"] == (
        "python3 src/zeta23_correction_context.py resume"
    )


def test_current_bundle_validator_rejects_authority_drift() -> None:
    original = {
        "route": load_json("zeta23_post_synthesis_decision_path_v1.json"),
        "adapter": load_json("zeta23_r105_r116_r73_adapter_audit_v1.json"),
        "closure": load_json("zeta23_correction_closure_v1.json"),
    }

    def fresh() -> dict[str, dict]:
        return copy.deepcopy(original)

    mutations = []

    bundle = fresh()
    del bundle["adapter"]
    mutations.append(bundle)

    bundle = fresh()
    bundle["route"]["schema"] = "stale-schema"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["date"] = "2026-09-01"
    mutations.append(bundle)

    bundle = fresh()
    bundle["adapter"]["global_status"]["riemann_hypothesis"] = "PROVED"
    mutations.append(bundle)

    bundle = fresh()
    bundle["adapter"]["s0_verdict"]["primitive_only_go_condition"] = "GO"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["corrections"]["primitive_sign"] = "BOTH_SIGNS_PROVED"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["corrections"]["energy_map"] = "eta=kappa/2"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["exhaustiveness_status"] = "EXHAUSTIVE"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["s1"]["candidate_a_structural_inequality_class"] = "CLOSED"
    mutations.append(bundle)

    bundle = fresh()
    bundle["closure"]["growing_families"]["fixed_step_sublinear"] = (
        "R80_CONVERSE_PROVED"
    )
    mutations.append(bundle)

    bundle = fresh()
    bundle["route"]["human_authority"] = "../missing.md"
    mutations.append(bundle)

    for bundle in mutations:
        with pytest.raises(ValueError):
            zpt.validate_current_authority_bundle(bundle)


def test_legacy_cache_clis_warn_that_their_routes_are_historical() -> None:
    commands = (
        [sys.executable, "src/zeta23_context_cache.py", "--json", "live"],
        [sys.executable, "src/zeta23_kg_cache.py", "query", "--live", "--json"],
    )
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        assert "historical August" in completed.stderr
        assert "zeta23_correction_context.py resume" in completed.stderr


def test_mobius_log_convolution_is_lambda_symbolically() -> None:
    """Check C*1=Lambda in the free abelian basis {log p}."""
    for n in range(1, 501):
        actual: dict[int, int] = {}
        for d in divisors(n):
            add_log_vector(actual, prime_factorization(d), -mobius(d))

        factors = prime_factorization(n)
        expected = {next(iter(factors)): 1} if len(factors) == 1 else {}
        assert actual == expected, n


def test_adjacent_filter_identity_has_exact_normalization() -> None:
    """The only new coefficient in C_(P-1)-C_P is +P^(-1/2)."""
    for prime in (2, 3, 5, 7, 11, 19, 31, 43):
        assert len(prime_factorization(prime)) == 1
        before = {q: mobius(q) for q in range(1, prime)}
        after = {q: mobius(q) for q in range(1, prime + 1)}
        difference = {
            q: before.get(q, 0) - after.get(q, 0)
            for q in set(before) | set(after)
            if before.get(q, 0) != after.get(q, 0)
        }
        # Values are the numerators of the common q^(-1/2) basis.
        assert difference == {prime: 1}

    # On exp((s-1/2)R), the unnormalized difference has exponent -beta.
    # Multiplication by P gives raw exponent 1-beta, but its critical-line
    # response has exponent 1/2.  The relative exponent is therefore the
    # shifted-scale exponent 1/2-beta; these are not the same normalization.
    for beta in (Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
        raw_exponent = 1 - beta
        critical_exponent = Fraction(1, 2)
        assert raw_exponent - critical_exponent == Fraction(1, 2) - beta


def test_all_class_bilinear_recompletion_is_finite_convolution_algebra() -> None:
    """Replay the R128 double-sum identity with exact integer coefficients."""
    limit = 24
    coefficient = {q: ((q * q + 3 * q + 1) % 11) - 5 for q in range(1, limit + 1)}
    convolved = {
        n: sum(coefficient[q] for q in divisors(n))
        for n in range(1, limit + 1)
    }

    def kernel(n1: int, n2: int) -> int:
        return ((7 * n1 + 11 * n2 + 3 * n1 * n2) % 17) - 8

    left = 0
    for q1 in range(1, limit + 1):
        for q2 in range(1, limit + 1):
            for m1 in range(1, limit // q1 + 1):
                for m2 in range(1, limit // q2 + 1):
                    left += coefficient[q1] * coefficient[q2] * kernel(q1 * m1, q2 * m2)
    right = sum(
        convolved[n1] * convolved[n2] * kernel(n1, n2)
        for n1 in range(1, limit + 1)
        for n2 in range(1, limit + 1)
    )
    assert left == right


def test_known_status_errors_do_not_reappear() -> None:
    closure = (RESULTS / "ZETA23-CORRECTION-CLOSURE-AND-FAITHFULNESS-TRILEMMA-2026-09-02.md").read_text()
    decision = (RESULTS / "ZETA23-POST-SYNTHESIS-DECISION-PATH-2026-09-02.md").read_text()
    handoff = (ROOT / "CODEX_HANDOFF.md").read_text()
    proxy = (RESULTS / "RH-PROXY-LEDGER.md").read_text()
    registry = (RESULTS / "REDUCTION-REGISTRY.md").read_text()
    r116 = (RESULTS / "R116-SIGNED-JOINT-TYPEII-ATTACK.md").read_text()
    r120 = (RESULTS / "R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md").read_text()
    r121 = (RESULTS / "R121-COMPOSITE-CRT-SPARSE-BRIDGE-GATE.md").read_text()
    r122 = (RESULTS / "R122-ZERO-REPLICATION-DENSITY-GATE.md").read_text()
    r124 = (RESULTS / "R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md").read_text()
    r125 = (RESULTS / "R125-ADJACENT-FILTER-PRIME-PACKET-BRIDGE-GATE.md").read_text()
    r128 = (RESULTS / "R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md").read_text()
    r130 = (RESULTS / "R130-NULL-TAIL-HADAMARD-DILATION-FRAME-GATE.md").read_text()
    r180 = (RESULTS / "ZETA23-STRIP-TO-R68-REVERSE-CALIBRATION-2026-09-02.md").read_text()

    assert "Theorem 2.1 (architecture-specific trilemma)" not in closure
    assert "arbitrary-composition classification                NOT PROVED" in closure
    assert "D-rated numerical diagnostic" in r124
    assert "not a certified negative spectral witness" in r124
    assert "The sign route therefore closes as a shortcut" not in r124
    assert "It is repaired by some combination" not in r124
    assert "does not\nupgrade the present floating calculation into a sign theorem" in r124
    assert "actual primitive sign                 OPEN" in r120
    assert "Only that all-class family" not in r120
    assert "Positivity returns\nonly after" not in r120
    assert "does not by itself furnish that\nabsolute family bound" in r116
    assert "R80 bank supplies the\nneeded scale/frequency coverage" not in r116
    assert "signed R116 primitive\npacket" not in r121
    assert "so no order-reflecting comparison makes" not in r121
    assert "multiplier `lambda_P` is real but signed" not in r122
    assert "actual full-shell\nsign is unclassified" in r122
    assert "after critical normalization" not in r125
    assert "X^(beta-1/2)P^(1-beta)" in r125
    assert "P^(1-beta)/P^(1/2)" in r125
    assert "Its negative\nbands are repaired" not in r128
    assert "SIGN NOT CERTIFIED" in r128
    assert "only D-rated numerical evidence of full-shell sign change" in r128
    assert "saves a square root in amplitude, hence a" not in r130
    assert "frame energy <<Y^(1-kappa),       0<kappa<=1" in r130
    assert "0<\\eta\\le\\tfrac12" in r180
    assert "The current exact state is:" not in handoff
    assert "R80 supplies the missing detector converse" not in proxy
    assert "isolated positive-energy adapter **ABSENT**" not in proxy
    assert "primitive-only positive-energy adapter ABSENT" not in registry
    assert "some fixed `0<eta<=1/2`" in decision
    assert "`0<eta<=1/2`, force" in closure
