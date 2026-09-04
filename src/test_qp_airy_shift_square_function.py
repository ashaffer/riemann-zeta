from fractions import Fraction

import numpy as np

from qp_airy_shift_square_function import (
    actual_residual_shift_fixture,
    airy_vector_exponent_ledger,
    completion_character_gram,
    completion_repetition_audit,
    constant_amplitude_no_localization_fixture,
    localized_fejer_vector_bound,
    normalized_fejer_square_mass,
    positive_cosine_amplitude,
    shift_square_audit,
)


def test_exact_shift_identity_and_both_parsevals():
    size = 9
    amplitude = np.array(
        [[complex((3 * x + y) % 7, (x - 2 * y) % 5) for y in range(size)] for x in range(size)]
    )
    coefficients = np.array(
        [[complex((x * y + 1) % 11, (2 * x + y) % 3) for y in range(size)] for x in range(size)]
    )
    audit = shift_square_audit(amplitude, coefficients)
    assert abs(audit.direct_sum - audit.shifted_sum) < 2.0e-10
    assert abs(audit.amplitude_fourier_energy - audit.amplitude_physical_energy_scaled) < 2.0e-10
    assert abs(audit.shifted_field_energy - audit.coefficient_physical_energy_scaled) < 2.0e-8
    assert abs(audit.direct_sum) <= audit.cauchy_bound + 2.0e-10


def test_exact_normalized_fejer_square_mass():
    for order in (1, 2, 7, 31):
        coefficients = [
            Fraction(order - abs(index), order * order)
            for index in range(-order + 1, order)
        ]
        assert sum(value * value for value in coefficients) == normalized_fejer_square_mass(order)


def test_localized_layer_recovers_square_root_gain_for_arbitrary_complex_values():
    order, curvature_width = 100, 4
    cardinality = curvature_width * order
    amplitude = 37.0
    bound = localized_fejer_vector_bound(order, cardinality, amplitude)
    assert bound["square_function"] < 1.01 * amplitude * (curvature_width / order) ** 0.5
    assert bound["pointwise_fejer"] == amplitude * curvature_width / order
    assert bound["best"] == bound["pointwise_fejer"]


def test_constant_positive_amplitude_refutes_gain_without_localization():
    size = 64
    amplitude, coefficients = constant_amplitude_no_localization_fixture(size)
    audit = shift_square_audit(amplitude, coefficients)
    assert abs(audit.direct_sum - 1.0) < 1.0e-12
    assert abs(audit.shifted_sum - 1.0) < 1.0e-12
    assert abs(audit.direct_sum) > size ** -0.5


def test_positive_cosine_has_only_the_expected_three_fourier_shifts():
    size, first, second = 17, 3, 5
    amplitude = positive_cosine_amplitude(size, first, second)
    assert min(min(row) for row in amplitude) >= 0
    fourier = np.fft.fft2(np.asarray(amplitude)) / size**2
    support = {
        (x, y)
        for x in range(size)
        for y in range(size)
        if abs(fourier[x, y]) > 1.0e-10
    }
    assert support == {(0, 0), (first, second), ((-first) % size, (-second) % size)}
    assert abs(fourier[0, 0] - 1) < 1.0e-12
    assert abs(fourier[first, second] - 0.5) < 1.0e-12


def test_airy_exponents_close_exactly_at_square_root_target():
    ledger = airy_vector_exponent_ledger()
    assert ledger.airy_width == Fraction(1, 48)
    assert ledger.airy_amplitude == Fraction(49, 48)
    assert ledger.fourier_spread == Fraction(25, 24)
    assert ledger.l2_layer_gain == Fraction(-25, 48)
    assert ledger.l2_total == ledger.target == Fraction(1, 2)
    assert ledger.l1_layer_gain == Fraction(-25, 24)
    assert ledger.l1_total == Fraction(-1, 48)


def test_fixed_lattice_theorem_does_not_create_completion_orthogonality():
    audit = completion_repetition_audit([1, 2j, -3], completion_count=25)
    assert audit.repetition_loss == 5
    assert audit.repeated_operator_norm == 5 * audit.one_fiber_norm


def test_genuine_completion_characters_are_orthogonal_up_to_label_multiplicity():
    labels = [1, 2, 5, 1, 8]
    gram = completion_character_gram(labels, completion_modulus=7)
    eigenvalue = np.linalg.eigvalsh(gram)[-1]
    # 1 and 8 coincide modulo 7, and label 1 occurs twice already.
    assert abs(eigenvalue - 3) < 1.0e-10


def test_actual_residual_intercept_has_an_exact_major_shift():
    fixture = actual_residual_shift_fixture(multiplier=3, family_index=2)
    assert (fixture.p, fixture.d, fixture.n) == (33, 7, -1)
    assert fixture.content == 1275
    assert fixture.content % 49 == 1
    assert (fixture.left_error, fixture.right_error) == (29429, 30704)
    assert fixture.tangent_modulus == 270400
    assert (fixture.alpha - Fraction(921447, 1600)).denominator == 1
    assert (fixture.beta - Fraction(-161179, 676)).denominator == 1
    assert (fixture.alpha + Fraction(fixture.alpha_shift, fixture.torus_size)).denominator == 1
    assert (fixture.beta + Fraction(fixture.beta_shift, fixture.torus_size)).denominator == 1
