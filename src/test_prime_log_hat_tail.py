from fractions import Fraction
import math

import numpy as np
from scipy.integrate import quad
from flint import arb, ctx

from prime_log_hat_tail import (
    HatVector,
    PrimeHatVector,
    WIDTH,
    arb_mid_float,
    build_prime_hat_vector,
    continuum_certificate,
    exact_prime_shell,
    float_arb_exact,
    fraction_arb,
    full_tent_mass,
    hat_vector_from_arb_nodes,
    interpolation_cell_lower,
    jitter_control,
    odd_half_grid_control,
    prime_vector_fingerprints,
    validate_dyadic_leaf_partition,
)


def _profile(value: float) -> float:
    width = float(WIDTH)
    return (1.0 - abs(value) / width) * math.exp(0.49 * value)


def test_hat_weights_are_positive_and_partition_the_truncated_mass() -> None:
    node_values = np.array([-0.19, -0.071, 0.027, 0.111, 0.193])
    vector = hat_vector_from_arb_nodes(
        tuple(float_arb_exact(float(value)) for value in node_values)
    )
    numerical_mass = quad(
        _profile,
        float(node_values[0]),
        float(node_values[-1]),
        points=[0.0],
        epsabs=1e-13,
        epsrel=1e-13,
    )[0]
    assert math.isclose(
        arb_mid_float(vector.truncated_mass),
        numerical_mass,
        rel_tol=2e-12,
        abs_tol=2e-14,
    )
    assert all(weight.lower() > 0 for weight in vector.raw_weights)
    assert sum(vector.weights).contains(1)

    for index, raw_weight in enumerate(vector.raw_weights):
        def integrand(value: float) -> float:
            if index and node_values[index - 1] <= value <= node_values[index]:
                hat = (
                    (value - node_values[index - 1])
                    / (node_values[index] - node_values[index - 1])
                )
            elif (
                index + 1 < len(node_values)
                and node_values[index] <= value <= node_values[index + 1]
            ):
                hat = (
                    (node_values[index + 1] - value)
                    / (node_values[index + 1] - node_values[index])
                )
            else:
                hat = 0.0
            return _profile(value) * hat

        numerical_weight = quad(
            integrand,
            float(node_values[max(0, index - 1)]),
            float(node_values[min(len(node_values) - 1, index + 1)]),
            points=[value for value in (0.0, node_values[index]) if
                    node_values[max(0, index - 1)] < value
                    < node_values[min(len(node_values) - 1, index + 1)]],
            epsabs=1e-13,
            epsrel=1e-13,
        )[0]
        assert math.isclose(
            arb_mid_float(raw_weight),
            numerical_weight,
            rel_tol=3e-11,
            abs_tol=3e-14,
        )


def test_cusp_crossing_hat_fixture_matches_independent_values() -> None:
    ctx.prec = 192
    nodes = tuple(
        fraction_arb(value)
        for value in (Fraction(-17, 100), Fraction(-13, 1000), Fraction(181, 1000))
    )
    vector = hat_vector_from_arb_nodes(nodes)
    expected = (
        0.0307602587421608724515018551541170747,
        0.123922792793836713930545047605379068,
        0.0424277369377381757454874433636533592,
    )
    for observed, target in zip(vector.raw_weights, expected):
        assert math.isclose(
            arb_mid_float(observed), target, rel_tol=2e-15, abs_tol=2e-16
        )
    assert math.isclose(
        arb_mid_float(vector.truncated_mass),
        0.197110788473735762127534346123149502,
        rel_tol=2e-15,
        abs_tol=2e-16,
    )


def test_exact_prime_shell_has_complete_known_mask() -> None:
    primes, nodes, lower, upper = exact_prime_shell(
        Fraction(129, 2), precision_bits=128
    )
    assert primes == (53, 59, 61, 67, 71, 73)
    assert len(nodes) == len(primes)
    assert lower < 53 and upper > 73
    assert upper < 79


def test_controls_preserve_the_registered_geometry() -> None:
    nodes = np.array([-0.19, -0.13, -0.071, 0.061, 0.121, 0.19])
    band_right = 10_000.0
    half_grid = odd_half_grid_control(nodes, band_right)
    assert half_grid[0] == nodes[0]
    assert half_grid[-1] == nodes[-1]
    assert np.all(np.diff(half_grid) > 0)
    assert np.max(np.abs(np.cos(half_grid[1:-1] * band_right) + 1)) < 1e-12

    first = jitter_control(nodes, 0.6, 31415)
    second = jitter_control(nodes, 0.6, 31415)
    assert np.array_equal(first, second)
    assert first[0] == nodes[0] and first[-1] == nodes[-1]
    assert np.all(np.diff(first) > 0)
    assert np.array_equal(np.sign(first), np.sign(nodes))


def test_exact_input_fingerprint_is_precision_stable() -> None:
    first = build_prime_hat_vector(Fraction(129, 2), precision_bits=128)
    second = build_prime_hat_vector(Fraction(129, 2), precision_bits=192)
    first_hash = prime_vector_fingerprints(first)["exact_input_sha256"]
    second_hash = prime_vector_fingerprints(second)["exact_input_sha256"]
    assert first_hash == second_hash


def test_small_actual_vector_gets_a_complete_rigorous_cover() -> None:
    vector = build_prime_hat_vector(Fraction(129, 2), precision_bits=128)
    certificate = continuum_certificate(
        vector,
        dyadic_bits=24,
        max_depth=24,
        max_leaves=100_000,
        record_leaves=True,
    )
    assert certificate.status == "PASS"
    assert certificate.trust == "ARB-CONTINUUM-CERTIFIED"
    assert certificate.leaf_count > 0
    assert certificate.point_evaluation_count > 0
    assert certificate.partition_verified
    paths = tuple(
        (int(leaf["depth"]), int(leaf["index"]))
        for leaf in certificate.leaves
    )
    valid, kraft_sum = validate_dyadic_leaf_partition(paths)
    assert valid and kraft_sum == 1


def test_interpolation_remainder_uses_the_sharp_one_eighth_factor() -> None:
    ctx.prec = 160
    width = Fraction(1, 10)
    half_width = fraction_arb(width) / 2
    value_left = (arb.pi() - half_width).cos()
    value_right = (arb.pi() + half_width).cos()
    lower = interpolation_cell_lower(
        value_left, value_right, arb(1), width
    )
    assert lower <= -1
    false_one_sixteenth = (
        value_left.lower()
        - fraction_arb(width) * fraction_arb(width) / 16
    )
    assert false_one_sixteenth > -1


def _synthetic_prime_vector(node: arb) -> PrimeHatVector:
    one = arb(1)
    center = Fraction(129, 2)
    return PrimeHatVector(
        center=center,
        primes=(2,),
        shell_lower=arb(-1),
        shell_upper=arb(1),
        vector=HatVector(
            nodes=(node,),
            raw_weights=(one,),
            weights=(one,),
            truncated_mass=one,
        ),
        full_tent_mass=full_tent_mass(),
        precision_bits=160,
    )


def test_certificate_fail_requires_a_rigorous_in_band_point() -> None:
    ctx.prec = 160
    vector = _synthetic_prime_vector(arb.pi() / 100)
    certificate = continuum_certificate(
        vector,
        scout_argmin=100.0,
        max_depth=0,
        record_leaves=False,
    )
    assert certificate.status == "FAIL"
    assert certificate.trust == "ARB-POINT-WITNESS"
    assert certificate.witness_time == "100/1"
    assert certificate.witness_value is not None


def test_certificate_reports_inconclusive_for_an_unresolved_cell() -> None:
    ctx.prec = 160
    vector = _synthetic_prime_vector(fraction_arb(Fraction(1, 200)))
    certificate = continuum_certificate(
        vector,
        max_depth=0,
        record_leaves=False,
    )
    assert certificate.status == "INCONCLUSIVE"
    assert certificate.trust == "ARB-INCOMPLETE-COVER"
    assert certificate.unresolved_cell == {"depth": 0, "index": 0}
