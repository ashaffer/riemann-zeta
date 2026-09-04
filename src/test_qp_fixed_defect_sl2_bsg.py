import pytest

from qp_fixed_defect_sl2_bsg import (
    actual_prime_sl2_audit,
    centered_star_family_moment,
    centered_star_rayleigh,
    centered_level_moment,
    determinant,
    free_quotient_sidon_set,
    is_quotient_sidon,
    minimum_distinct_quotient_energy,
    multiplicative_energy,
    quotient_multiplicities,
    quotient_sidon_star,
    star_relative_commutator_trace,
    star_numerical_radius,
)


@pytest.mark.parametrize("defect", [-11, 1, 17])
@pytest.mark.parametrize("cardinality", [1, 2, 7, 24])
def test_free_conjugates_are_exact_fixed_level_quotient_sidon_sets(
    defect: int, cardinality: int
) -> None:
    matrices = free_quotient_sidon_set(cardinality, defect=defect)
    assert all(determinant(matrix) == defect for matrix in matrices)
    assert is_quotient_sidon(matrices)
    assert multiplicative_energy(matrices) == minimum_distinct_quotient_energy(
        cardinality
    )
    multiplicities = quotient_multiplicities(matrices)
    assert sorted(multiplicities.values()) == [1] * (
        cardinality * (cardinality - 1)
    ) + [cardinality]


def test_high_centered_level_moments_do_not_change_sidon_energy() -> None:
    level_count = 10
    support_size = 13
    assert centered_level_moment(level_count, support_size, 1) == 10 * 13**2
    assert centered_level_moment(level_count, support_size, 4) == 10 * 13**8
    matrices = free_quotient_sidon_set(support_size, defect=7)
    assert multiplicative_energy(matrices) == 2 * support_size**2 - support_size
    assert multiplicative_energy(matrices) / support_size**3 < 2 / support_size


@pytest.mark.parametrize("cardinality", [1, 3, 19, 64])
def test_fixed_defect_directed_star_is_still_quotient_sidon(
    cardinality: int,
) -> None:
    matrices = quotient_sidon_star(cardinality, defect=7)
    assert is_quotient_sidon(matrices)
    assert multiplicative_energy(matrices) == 2 * cardinality**2 - cardinality
    assert star_numerical_radius(cardinality) == pytest.approx(
        cardinality**0.5 / 2
    )
    # A polynomially large isolated reservoir enforces exact mean-zero
    # centering while losing only a bounded factor in the Rayleigh quotient.
    assert centered_star_rayleigh(cardinality, max(4, cardinality**2)) >= (
        cardinality**0.5 / 4
    )


def test_one_centered_vector_amplifies_all_sidon_defect_levels() -> None:
    levels, cardinality, reservoir = 12, 25, 25**2
    rayleigh = centered_star_rayleigh(cardinality, reservoir)
    assert centered_star_family_moment(
        levels, cardinality, reservoir, 1
    ) == pytest.approx(levels * rayleigh**2)
    assert centered_star_family_moment(
        levels, cardinality, reservoir, 3
    ) == pytest.approx(levels * rayleigh**6)
    for defect in range(1, levels + 1):
        matrices = quotient_sidon_star(cardinality, defect=defect)
        assert is_quotient_sidon(matrices)
        assert star_relative_commutator_trace(defect) != 2


def test_literal_actual_prime_rays_are_quotient_sidon_at_q100003() -> None:
    audit = actual_prime_sl2_audit(100_003)
    assert audit.degree_parameter == 265
    assert audit.level_count == 52
    assert audit.maximum_block_count == 6
    assert audit.maximum_wedge_count == 24
    assert audit.every_level_quotient_sidon
