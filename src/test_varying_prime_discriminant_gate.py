import pytest

from varying_prime_discriminant_gate import (
    adjacent_continuant_factorization,
    adjacent_continuant_cross_identity,
    affine_trace_parameters,
    aperiodic_autocorrelation,
    adversarial_row_dependent_character_sum,
    axis_discriminant,
    axis_matrix_mod_prime,
    axis_parameter,
    character_after_squarefree_reduction,
    complete_trace_character_sum,
    heath_brown_critical_ledger,
    is_nonzero_square,
    legendre_symbol,
    opposite_scaling_trace,
    puncture_zero,
    punctured_autocorrelation_sharpness_ledger,
    sharp_trace_energy_example,
    square_kernel_pair_energy,
    squarefree_decomposition,
    trace_fiber_factorization,
    trace_dot_product_offset,
    trace_large_sieve_critical_ledger,
    trace_pair_invariants,
    trace_discriminant,
    trace_offset,
    trace_value,
    weighted_nonparabolic_trace_energy,
)


def test_trace_discriminant_factorization() -> None:
    for values in [(1, 1, 2, 3, 4), (2, -1, 3, 2, -4), (3, 0, 5, 7, 9)]:
        a, h1, h2, h3, h4 = values
        trace = trace_value(a, h1, h2, h3, h4)
        offset = trace_offset(a, h1, h2, h3, h4)
        delta = trace_discriminant(a, h1, h2, h3, h4)
        assert trace == offset + 2
        assert delta == trace * trace - 4
        assert delta == offset * (offset + 4)


def test_fixed_pair_trace_fiber_factorization() -> None:
    for values in [(1, 1, 2, 3, 4), (2, -1, 3, 2, -4), (3, 5, -2, 7, 9)]:
        assert trace_fiber_factorization(*values)[0] == trace_fiber_factorization(*values)[1]


def test_adjacent_continuant_factorization() -> None:
    for values in [
        (1, 1, 2, 3, 4),
        (2, -1, 3, 2, -4),
        (3, 5, -2, 7, 9),
        (1, 1, 1, -5, 8),  # the degenerate p=0 adjacent pair
    ]:
        _, left, right = adjacent_continuant_factorization(*values)
        assert left == right


def test_adjacent_continuant_cross_identity() -> None:
    first = (1, 2, 3, 4)
    second = (3, 4, 1, 2)
    assert trace_value(1, *first) == trace_value(1, *second)
    left, right = adjacent_continuant_cross_identity(1, first, second)
    assert left == right
    with pytest.raises(ValueError):
        adjacent_continuant_cross_identity(1, first, (3, 4, 1, 3))


def test_trace_is_exact_sum_product_dot_product() -> None:
    for values in [(1, 1, 2, 3, 4), (2, -1, 3, 2, -4), (3, 5, -2, 7, 9)]:
        assert trace_dot_product_offset(*values) == trace_offset(*values)
    assert trace_pair_invariants(3, 5, -2) == (-30, -3)


def test_trace_is_affine_in_the_fourth_shift() -> None:
    for a, h1, h2, h3 in [(1, 1, 2, 3), (2, -1, 3, 2), (3, 5, -2, 7)]:
        slope, intercept = affine_trace_parameters(a, h1, h2, h3)
        for h4 in range(-5, 6):
            assert trace_value(a, h1, h2, h3, h4) == slope * h4 + intercept


def test_opposite_scaling_is_an_exact_trace_symmetry() -> None:
    original, scaled = opposite_scaling_trace(1, 2, 1, 3, 8, -5, 6)
    assert original == scaled
    with pytest.raises(ValueError):
        opposite_scaling_trace(1, 2, 1, 3, 7, -5, 6)


def test_trace_discriminant_is_never_a_nonzero_square() -> None:
    for trace in range(-500, 501):
        assert not is_nonzero_square(trace * trace - 4)


def test_negative_trace_discriminants_are_only_minus_three_or_minus_four() -> None:
    negative = {trace * trace - 4 for trace in range(-100, 101) if trace * trace < 4}
    assert negative == {-4, -3}


def test_axis_slice_exact_x_classification() -> None:
    expected = {
        0: (0, 0),
        1: (-3, -3),
        2: (-4, -1),
        3: (-3, -3),
        4: (0, 0),
        5: (5, 5),
    }
    for x, (delta, kernel) in expected.items():
        # Set a=h3=1, h2=x, h4=0, so the axis parameter is x.
        assert axis_parameter(1, x, 1, 0) == x
        assert axis_discriminant(1, x, 1, 0) == delta
        assert squarefree_decomposition(delta)[0] == kernel


def test_special_character_central_value_on_axis_requires_a_second_zero() -> None:
    prime = 11
    identity = ((1, 0), (0, 1))
    minus_identity = ((10, 0), (0, 10))
    for h2 in range(prime):
        for h3 in range(prime):
            for h4 in range(prime):
                matrix = axis_matrix_mod_prime(3, h2, h3, h4, prime)
                if matrix == identity:
                    assert h3 == 0
                    assert (h2 + h4) % prime == 0
                assert matrix != minus_identity


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, (0, 0)), (1, (1, 1)), (12, (3, 2)), (-12, (-3, 2)), (-4, (-1, 2)), (72, (2, 6))],
)
def test_signed_squarefree_decomposition(n: int, expected: tuple[int, int]) -> None:
    assert squarefree_decomposition(n) == expected
    d, m = expected
    assert n == d * m * m


def test_squarefree_reduction_preserves_character_with_ramification_mask() -> None:
    for n in [-300, -12, -4, 5, 12, 45, 300]:
        for prime in [3, 5, 7, 11, 13]:
            assert character_after_squarefree_reduction(n, prime)[0] == character_after_squarefree_reduction(n, prime)[1]


def test_critical_quadratic_large_sieve_scale_is_worse_than_trivial() -> None:
    ledger = heath_brown_critical_ledger(10)
    assert ledger == {
        "R": 100,
        "K": 10_000,
        "D": 100_000_000,
        "trivial": 1_000_000,
        "quadratic_large_sieve": 10_000_000,
    }
    assert ledger["quadratic_large_sieve"] // ledger["trivial"] == 10


def test_trace_grouping_reaches_but_does_not_beat_the_critical_scale() -> None:
    ledger = trace_large_sieve_critical_ledger(10)
    assert ledger["trace_interval"] == 10_000
    assert ledger["max_fiber_bound"] == 100
    assert ledger["trace_energy_bound"] == 1_000_000
    assert ledger["trace_large_sieve"] == ledger["trivial"]


def test_exact_sharp_trace_energy_example() -> None:
    for h in range(2, 12):
        sequences = [{1: 1}, {1: 1}, {j: 1 for j in range(1, h + 1)}, {j: 1 for j in range(1, h + 1)}]
        energy, norm_product = sharp_trace_energy_example(h)
        assert weighted_nonparabolic_trace_energy(1, sequences) == energy
        assert norm_product == h * h


def test_punctured_autocorrelation_example_has_linear_sharpness() -> None:
    short = puncture_zero(aperiodic_autocorrelation([1, 1]))
    assert short == {-1: (1 + 0j), 1: (1 + 0j)}
    for h in [8, 12, 20]:
        ledger = punctured_autocorrelation_sharpness_ledger(h)
        long = puncture_zero(aperiodic_autocorrelation([1] * (h + 1)))
        long_norm = sum(abs(value) ** 2 for value in long.values())
        assert ledger["exact_norm_product"] == 4 * long_norm**2
        assert ledger["subenergy_lower"] >= ledger["coarse_energy_lower"]
        assert ledger["exact_norm_product"] <= ledger["coarse_norm_upper"]
        assert (
            ledger["subenergy_lower"] / ledger["exact_norm_product"]
            >= h / 24576
        )


@pytest.mark.parametrize("prime", [3, 5, 7, 11, 13, 17, 19])
def test_complete_trace_character_has_only_the_minus_one_zero_mode(prime: int) -> None:
    assert complete_trace_character_sum(prime) == -1


def test_square_kernel_pair_energy_pairs_equal_kernels() -> None:
    coefficients = {3: 2, 12: -1, 5: 4, 20: 3, -3: 5}
    # Kernels: 3,3,5,5,-3, so (2+1)^2+(4+3)^2+5^2=83.
    assert square_kernel_pair_energy(coefficients) == 83


def test_arbitrary_row_dependent_weights_can_cancel_every_character_sign() -> None:
    total, pairs = adversarial_row_dependent_character_sum(
        [5, 7, 11, 13], [-3, -1, 2, 3, 5, 6, 10]
    )
    assert pairs > 0
    assert total == pairs


def test_legendre_symbol_rejects_even_modulus() -> None:
    with pytest.raises(ValueError):
        legendre_symbol(3, 2)
    with pytest.raises(ValueError):
        heath_brown_critical_ledger(0)
