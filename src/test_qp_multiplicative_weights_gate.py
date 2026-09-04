import math

from qp_multiplicative_weights_gate import (
    KAPPA_MAX,
    KAPPA_MIN,
    bessel_coefficient_mass,
    exponent_gap,
    i0_normalized_halfspace_limit,
    i0_series,
    orthant_witness_upper_bound,
    scalar_bessel_floor,
    sufficient_dichotomy_iterations,
)


def test_i0_series_and_coefficient_mass() -> None:
    assert math.isclose(i0_series(0.0), 1.0)
    assert math.isclose(i0_series(1.0), 1.2660658777520082, rel_tol=1.0e-14)
    mass = bessel_coefficient_mass(0.01, 100)
    assert mass > 1.0
    assert math.isclose(math.log(mass), 100 * (0.01 - math.log(i0_series(0.01))))


def test_continued_run_produces_depth_half_orthant_witness() -> None:
    epsilon = 0.01
    minimum_mass = 1.0e-6
    iterations = sufficient_dichotomy_iterations(epsilon, minimum_mass)
    bound = orthant_witness_upper_bound(
        epsilon, epsilon / 2.0, iterations, minimum_mass
    )
    assert bound <= -epsilon / 2.0


def test_scalar_bessel_floor_formula() -> None:
    floor = scalar_bessel_floor(delta=1.0e-12, step=0.001, iterations=10_000)
    assert math.isclose(floor.effective_order, 10.0)
    assert floor.coefficient_mass > 1.0
    assert floor.scalar_error >= 0.0
    assert floor.poisson_tail_error > 0.0
    assert floor.normalized_lower_bound > 0.0


def test_i0_normalized_halfspace_partition_drops() -> None:
    values = [i0_normalized_halfspace_limit(a) for a in (0.0, 0.5, 1.0, 2.0)]
    assert math.isclose(values[0], 1.0)
    assert all(0.0 < value <= 1.0 for value in values)
    assert all(left > right for left, right in zip(values, values[1:]))


def test_exponent_ledgers_have_no_common_choice() -> None:
    assert KAPPA_MIN < KAPPA_MAX
    assert exponent_gap() > 0.0007
    # A same-scale dichotomy would need c below the first and above the second.
    assert not (KAPPA_MAX < KAPPA_MIN)

