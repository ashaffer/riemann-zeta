import numpy as np
import pytest

from qp_diagonal_calibration_quartic_gate import (
    active_leverage_skew_product,
    calibrated_quartic,
    cubic_value,
    polarization_replay,
    positive_core_legal_value,
    singleton_residual,
    symmetrized_rank_one_quartic,
    trilinear_value,
)


def symmetric_test_tensor() -> np.ndarray:
    rng = np.random.default_rng(20260815)
    raw = rng.normal(size=(4, 4, 4))
    tensor = np.zeros_like(raw)
    for permutation in [
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    ]:
        tensor += np.transpose(raw, permutation)
    return tensor / 6.0


def test_active_product_is_positive_quartic_after_orientation() -> None:
    tensor = symmetric_test_tensor()
    a = np.array([1.0, -0.2, 0.5, 0.7])
    rng = np.random.default_rng(7)
    for _ in range(40):
        x = rng.normal(size=4)
        x /= np.linalg.norm(x)
        q = calibrated_quartic(a, tensor, x)
        oriented = x if a @ x < 0 else -x
        if q > 0:
            assert a @ oriented < 0
            assert cubic_value(tensor, oriented) < 0
            assert active_leverage_skew_product(a, tensor, oriented) == pytest.approx(q)


def test_symmetrized_four_tensor_has_the_quartic_diagonal() -> None:
    tensor = symmetric_test_tensor()
    a = np.array([0.3, -0.8, 0.4, 1.2])
    x = np.array([0.2, -0.5, 0.7, 0.1])
    quartic_tensor = symmetrized_rank_one_quartic(a, tensor)
    value = float(np.einsum("ijkl,i,j,k,l->", quartic_tensor, x, x, x, x))
    assert value == pytest.approx(calibrated_quartic(a, tensor, x), abs=2e-12)


def test_real_polarization_identity() -> None:
    tensor = symmetric_test_tensor()
    rng = np.random.default_rng(11)
    x, y, z = (rng.normal(size=4) for _ in range(3))
    assert polarization_replay(tensor, x, y, z) == pytest.approx(
        trilinear_value(tensor, x, y, z), abs=2e-11
    )


def test_polarization_constant_ledger() -> None:
    assert 8 * 3**3 / 48 == pytest.approx(9 / 2)


def test_singleton_residual_is_calibrated_and_nonnegative() -> None:
    logs = np.array([-0.18, -0.07, 0.05, 0.11, 0.19])
    selected = 2
    v = singleton_residual(logs, selected, odd=101)
    assert v[selected] == pytest.approx(0.0, abs=2e-13)
    assert np.min(v) >= -2e-13


def test_positive_core_orientation_is_legal_and_keeps_diagonal_value() -> None:
    # A nonnegative symmetric tensor supported on the same three coordinates.
    tensor = np.zeros((3, 3, 3))
    tensor[0, 1, 2] = 1.0
    for permutation in [(0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        tensor[permutation] = 1.0
    v = np.array([0.0, 0.4, 1.7])
    x = np.array([1.0, 2.0, 3.0])
    legal_dot, negative_cubic = positive_core_legal_value(tensor, v, x)
    x /= np.linalg.norm(x)
    assert legal_dot < 0
    assert negative_cubic == pytest.approx(cubic_value(tensor, x))
    assert negative_cubic > 0

