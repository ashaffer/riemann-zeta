import math

import numpy as np

from sparse_cosine_antipode_classification import (
    all_root_cells,
    build_antipode_certificate,
    consecutive_chebyshev_classification,
    dominant_top_weights,
    palindromic_coefficients,
)


def test_arbitrary_sparse_frequency_support_and_root_cells() -> None:
    harmonics = (7, 11, 16, 19)
    depth = 0.5
    weights = dominant_top_weights(harmonics, depth)
    roots = all_root_cells(harmonics, weights, depth)
    assert len(roots) == harmonics[-1]
    assert np.all(roots > np.arange(harmonics[-1]) * math.pi / harmonics[-1])
    assert np.all(roots < np.arange(1, harmonics[-1] + 1) * math.pi / harmonics[-1])
    assert 2.0 * weights[-1] - 1.0 > depth


def test_selected_antipode_is_exact_and_remote() -> None:
    certificate = build_antipode_certificate((101, 107, 113, 127), depth=0.73)
    assert certificate.maximum_vector_residual < 2e-12
    assert abs(certificate.evaluation_determinant) > 1e-10
    assert certificate.top_weight_margin > 0.0
    assert min(certificate.harmonics) > 100


def test_palindromic_normalization_and_unimodular_simple_roots() -> None:
    harmonics = (2, 5, 7)
    depth = 0.43
    weights = dominant_top_weights(harmonics, depth)
    coefficients = palindromic_coefficients(harmonics, weights, depth)
    assert np.allclose(coefficients, coefficients[::-1])
    assert np.all(coefficients >= 0.0)
    roots = np.polynomial.polynomial.polyroots(coefficients)
    assert np.max(np.abs(np.abs(roots) - 1.0)) < 2e-10
    assert min(abs(left - right) for index, left in enumerate(roots) for right in roots[index + 1 :]) > 1e-4

    theta = 0.371
    z = np.exp(1j * theta)
    polynomial_value = np.polynomial.polynomial.polyval(z, coefficients)
    scalar_value = depth + np.dot(weights, np.cos(np.asarray(harmonics) * theta))
    expected = (2.0 / weights[-1]) * z ** harmonics[-1] * scalar_value
    assert abs(polynomial_value - expected) < 2e-12


def test_consecutive_chebyshev_sign_classification() -> None:
    base = build_antipode_certificate((1, 2, 3, 4, 5), depth=0.4)
    row = consecutive_chebyshev_classification(base.phases)
    assert row.feasible_positive_antipode
    assert row.strict_positive_antipode
    assert row.formula_residual is not None and row.formula_residual < 2e-11
    assert row.depth is not None and math.isclose(row.depth, 0.4, abs_tol=2e-11)


def test_singular_constant_chebyshev_stratum_is_infeasible() -> None:
    # (x-1/sqrt(2))(x+1/sqrt(2)) = T_2(x)/2 has zero T_0 coefficient.
    row = consecutive_chebyshev_classification((math.pi / 4.0, 3.0 * math.pi / 4.0))
    assert abs(row.chebyshev_coefficients[0]) < 1e-12
    assert not row.feasible_positive_antipode


def test_boundary_zero_coefficient_drops_one_harmonic() -> None:
    # R=(x-b)(x+b)=T_2(x)/2+(1/2-b^2)T_0 has r_1=0.
    # For b<1/sqrt(2), this is the feasible boundary stratum supported only
    # on harmonic 2.
    b = 0.5
    phases = (math.acos(b), math.acos(-b))
    row = consecutive_chebyshev_classification(phases)
    assert row.feasible_positive_antipode
    assert not row.strict_positive_antipode
    assert abs(row.chebyshev_coefficients[1]) < 1e-12
    assert row.weights is not None and np.allclose(row.weights, (0.0, 1.0))
    assert row.depth is not None and math.isclose(row.depth, 0.5, abs_tol=1e-12)
    assert row.formula_residual is not None and row.formula_residual < 1e-12
