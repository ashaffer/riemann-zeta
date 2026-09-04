from fractions import Fraction

import pytest

from qp_pre_stationary_fejer_completion_bundle import (
    completion_fourier_energy,
    absolute_wedge_majorant,
    apply_wedge_incidence,
    color_pair_coefficients,
    exact_hard_window_amplitude,
    factorable_pair_norm,
    fejer_coefficients,
    contract_stinespring_matrix,
    hard_window,
    hard_window_scalar_matrix,
    hard_window_stinespring_matrix,
    harmonic_lift,
    jackson_coefficients,
    kernel_value,
    lifted_kernel_operator,
    direct_row_gram,
    incidence_expansion_norms,
    norm_squared,
    pair_bundle_energy,
    pair_gram_energy,
    path_mask_eigenvalues,
    proposed_split_threshold_ledger,
    reciprocal_phase,
    scalar_anchored_energy,
    scalar_kernel_operator,
    schatten_fourth_power,
    masked_wedge_quadratic,
    ordered_wedge_incidence,
    same_center_pair_rank,
    zero_dual_action,
)


def test_fejer_and_jackson_coefficients_are_supported_probabilities() -> None:
    coefficients = fejer_coefficients(7)
    assert sum(coefficients.values()) == 1
    assert min(coefficients.values()) > 0
    assert set(coefficients) == set(range(-6, 7))

    squared = jackson_coefficients(7, 2)
    assert sum(squared.values()) == 1
    assert min(squared.values()) > 0
    assert set(squared) == set(range(-12, 13))


def test_canonical_harmonic_coefficient_lift_is_an_isometry() -> None:
    z = {2: 1 + 2j, 5: -3j, 9: 2 - 1j}
    lifted = harmonic_lift(z, fejer_coefficients(6))
    assert norm_squared(lifted) == pytest.approx(norm_squared(z), abs=1.0e-12)


def test_generic_scalar_kernel_operator_equals_lifted_synthesis() -> None:
    z = {0: 1 + 1j, 1: -0.25 + 2j, 2: 0.5 - 0.75j}
    amplitudes = {
        (10, 0): 1.2,
        (10, 1): -0.4j,
        (11, 0): 0.75,
        (11, 2): 1.1 + 0.2j,
    }
    phases = {
        (10, 0): 0.031,
        (10, 1): -0.073,
        (11, 0): 0.119,
        (11, 2): -0.017,
    }
    harmonics = fejer_coefficients(8)
    scalar = scalar_kernel_operator(z, amplitudes, phases, harmonics)
    lifted = lifted_kernel_operator(
        harmonic_lift(z, harmonics), amplitudes, phases, harmonics
    )
    assert lifted == pytest.approx(scalar, abs=1.0e-12)


def test_literal_hard_window_has_exact_supported_fejer_representation() -> None:
    q, D = 101, 17
    triples = [(40, 43, 75), (40, 46, 70), (40, 48, 67), (37, 35, 1)]
    # This small replay uses a low order so the selected reciprocal defects
    # avoid kernel zeros.  The theorem chooses order as a small fixed
    # multiple of q/D for the same reason.
    harmonics = fejer_coefficients(3)
    assert sum(hard_window(q, D, *triple) for triple in triples) == 3
    for a, b, colour in triples:
        theta = float(reciprocal_phase(q, a, b, colour))
        selected = hard_window(q, D, a, b, colour)
        amplitude = exact_hard_window_amplitude(
            q, D, a, b, colour, harmonics
        )
        reconstructed = amplitude * kernel_value(harmonics, theta)
        assert reconstructed == pytest.approx(selected, abs=1.0e-12)


def test_literal_matrix_has_exact_stinespring_contraction_and_s4_domination() -> None:
    q, D = 101, 17
    rows = [40, 41, 42]
    columns = [43, 46, 48, 52, 62, 67, 70, 75]
    colours = [75, 70, 67, 62, 52, 48, 46, 43]
    z = {
        colour: complex((index % 3) - 0.75, (-1) ** index * 0.35)
        for index, colour in enumerate(colours)
    }
    harmonics = fejer_coefficients(3)
    scalar = hard_window_scalar_matrix(q, D, rows, columns, colours, z)
    lifted = hard_window_stinespring_matrix(
        q, D, rows, columns, colours, z, harmonics
    )
    contracted = contract_stinespring_matrix(
        lifted, rows, columns, harmonics
    )
    assert contracted == pytest.approx(scalar, abs=1.0e-11)
    assert schatten_fourth_power(scalar) <= schatten_fourth_power(lifted) + 1.0e-9


def test_pair_bundle_gram_and_completion_dft_are_the_same_energy() -> None:
    pairs = [(5, 9), (6, 8), (7, 7), (4, 11), (8, 6)]
    weights = {
        (5, 9): 1 + 2j,
        (6, 8): -0.5j,
        (7, 7): 0.75 - 0.25j,
        (4, 11): -1.25,
        (8, 6): 0.3 + 0.8j,
    }
    harmonics = fejer_coefficients(4)
    direct = pair_bundle_energy(pairs, weights, 23.75, harmonics)
    gram = pair_gram_energy(pairs, weights, 23.75, harmonics)
    fourier = completion_fourier_energy(pairs, weights, 23.75, harmonics, 31)
    assert gram == pytest.approx(direct, abs=1.0e-10)
    assert fourier == pytest.approx(direct, abs=1.0e-10)


def test_zero_phase_scalar_contraction_is_norm_one() -> None:
    pairs = [(4, 8), (5, 7), (6, 6), (3, 10), (8, 5)]
    weights = {
        pair: complex(index - 1.5, (-1) ** index * 0.4)
        for index, pair in enumerate(pairs)
    }
    harmonics = fejer_coefficients(5)
    scalar = scalar_anchored_energy(pairs, weights, 17.0, harmonics)
    vector = pair_bundle_energy(pairs, weights, 17.0, harmonics)
    assert scalar <= vector + 1.0e-10


def test_factorable_pair_coefficients_keep_the_original_l2_ceiling() -> None:
    left = {2: 1 + 1j, 3: -2j, 5: 0.5}
    right = {7: 2 - 1j, 8: -0.25j}
    all_pairs = [(a, b) for a in left for b in right]
    selected, full = factorable_pair_norm(left, right, all_pairs)
    assert selected == pytest.approx(full, abs=1.0e-12)
    subset, same_ceiling = factorable_pair_norm(left, right, all_pairs[:-2])
    assert subset <= same_ceiling


def test_completion_action_has_exact_zero_dual_alias_families() -> None:
    center = Fraction(121)
    for completion in (Fraction(19), Fraction(20), Fraction(21)):
        assert zero_dual_action(center, completion, 2, 7) == zero_dual_action(
            center, completion, 4, 5
        )


def test_proposed_split_exponents_and_airy_scale_are_exact() -> None:
    ledger = proposed_split_threshold_ledger()
    assert ledger.product_saving == Fraction(7, 48)
    assert ledger.fejer_block_drift == Fraction(-5, 16)
    assert ledger.harmonic_cell == Fraction(49, 48)
    assert ledger.harmonic_cell == ledger.allowed_cluster
    assert ledger.airy_step == Fraction(1, 48)
    assert ledger.airy_block_range == Fraction(17, 24)


def test_a_nonclique_pair_mask_cannot_be_a_hilbert_gram() -> None:
    eigenvalues = path_mask_eigenvalues()
    assert eigenvalues[0] < 0 < eigenvalues[-1]


def test_second_physical_incidence_keeps_the_rank_one_color_pair() -> None:
    triples = [
        (1, 11, 101),
        (2, 11, 103),
        (3, 11, 107),
        (1, 13, 109),
        (2, 13, 113),
        (4, 13, 127),
    ]
    z = {
        101: 1 + 0.2j,
        103: -0.3 + 0.7j,
        107: 0.4j,
        109: 0.8 - 0.1j,
        113: -0.2j,
        127: 0.5 + 0.6j,
    }
    incidence = ordered_wedge_incidence(triples)
    color_pairs = sorted({color_pair for _, color_pair in incidence})
    xi = color_pair_coefficients(z, color_pairs)
    assert apply_wedge_incidence(incidence, xi) == pytest.approx(
        direct_row_gram(triples, z), abs=1.0e-12
    )
    # On the full Cartesian color-pair space, xi=zbar tensor z has exactly
    # the fourth power of the original norm.
    all_pairs = [(first, second) for first in z for second in z]
    full_xi = color_pair_coefficients(z, all_pairs)
    assert norm_squared(full_xi) == pytest.approx(norm_squared(z) ** 2)


def test_every_bounded_pair_of_pair_deletion_is_absolutely_dominated() -> None:
    triples = [
        (1, 11, 101),
        (2, 11, 103),
        (3, 11, 107),
        (1, 13, 109),
        (2, 13, 113),
        (3, 13, 127),
    ]
    incidence = ordered_wedge_incidence(triples)
    pairs = sorted({color_pair for _, color_pair in incidence})
    xi = {
        pair: complex(0.2 * index - 0.7, (-1) ** index * 0.35)
        for index, pair in enumerate(pairs)
    }
    mask = {}
    for index, (row_pair, first) in enumerate(incidence):
        for candidate, second in incidence:
            if candidate == row_pair:
                # Complex masks are allowed here; only modulus <=1 matters.
                mask[row_pair, first, second] = 0.8j if index % 2 else -0.6
    masked = masked_wedge_quadratic(incidence, xi, mask)
    assert abs(masked) <= absolute_wedge_majorant(incidence, xi) + 1.0e-12


def test_restoring_completion_incidence_has_exact_participation_loss() -> None:
    # One color-pair column repeated on r physical row-pair outputs.
    repetition = 9
    gamma = (101, 103)
    incidence = {((index, index + 1), gamma): 1 for index in range(repetition)}
    xi = {gamma: 2 - 1j}
    original, expanded = incidence_expansion_norms(incidence, xi)
    assert expanded == pytest.approx(repetition * original)
    # Likewise the same-center selector is not one scalar rank-one tensor
    # once more than one center is present.
    assert same_center_pair_rank([11, 11, 13, 13, 17]) == 3
