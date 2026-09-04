import numpy as np
import pytest

from qp_pure_state_channel import (
    channel_adjoint_apply,
    channel_apply,
    channel_ledger,
    cross_state_channel,
    kraus_cross_cauchy_ledger,
    pair_incidence_operator,
    pure_pair_vector,
    pure_state_channel,
    residual_layers,
    weighted_carry_matrix,
)


def sample_tensor() -> np.ndarray:
    tensor = np.zeros((3, 4, 3), dtype=complex)
    tensor[0, 0, 0] = 1
    tensor[1, 0, 2] = 1j
    tensor[0, 1, 1] = -1
    tensor[2, 1, 0] = 2
    tensor[1, 2, 1] = 1 - 1j
    tensor[2, 2, 2] = 1
    tensor[0, 3, 2] = -0.5j
    tensor[2, 3, 1] = 1
    return tensor


def test_channel_is_row_gram() -> None:
    tensor = sample_tensor()
    z = np.array([1 + 2j, -0.5j, 2 - 1j])
    matrix = weighted_carry_matrix(tensor, z)
    assert np.allclose(pure_state_channel(tensor, z), matrix @ matrix.conj().T)


def test_pair_operator_is_vectorized_channel() -> None:
    tensor = sample_tensor()
    z = np.array([1 + 2j, -0.5j, 2 - 1j])
    left = pair_incidence_operator(tensor) @ pure_pair_vector(z)
    right = pure_state_channel(tensor, z).reshape(-1)
    assert np.allclose(left, right)


def test_all_four_mass_representations_agree() -> None:
    ledger = channel_ledger(
        sample_tensor(),
        np.array([1 + 2j, -0.5j, 2 - 1j]),
        row_values=(11, 13, 17),
        color_values=(19, 23, 29),
    )
    assert ledger.fourth_mass == pytest.approx(ledger.channel_mass)
    assert ledger.fourth_mass == pytest.approx(ledger.pair_operator_mass)
    assert ledger.fourth_mass == pytest.approx(ledger.residual_zero_mass)


def test_residual_layers_sum_to_h() -> None:
    tensor = sample_tensor()
    layers = residual_layers(tensor, (11, 13, 17), (19, 23, 29))
    assert np.allclose(sum(layers.values()), pair_incidence_operator(tensor))


def test_channel_adjoint_identity() -> None:
    tensor = sample_tensor()
    x = np.array(
        [[1, 2j, 0], [-2j, 3, 1 - 1j], [0, 1 + 1j, -1]], dtype=complex
    )
    y = np.array(
        [[2, 1, -1j], [1, -2, 0.5], [1j, 0.5, 4]], dtype=complex
    )
    assert np.vdot(channel_apply(tensor, x), y) == pytest.approx(
        np.vdot(x, channel_adjoint_apply(tensor, y))
    )


def test_kraus_cross_cauchy() -> None:
    tensor = sample_tensor()
    x = np.array([1 + 2j, -0.5j, 2 - 1j])
    y = np.array([-1j, 3 + 0.25j, 0.5])
    left, right = kraus_cross_cauchy_ledger(tensor, x, y)
    assert left <= right + 1e-10
    assert np.allclose(
        cross_state_channel(tensor, x, y),
        channel_apply(tensor, np.outer(x, y.conj())),
    )


def test_validation() -> None:
    tensor = sample_tensor()
    with pytest.raises(ValueError):
        weighted_carry_matrix(tensor, np.ones(2))
    with pytest.raises(ValueError):
        channel_apply(tensor, np.ones((2, 2)))
    with pytest.raises(ValueError):
        residual_layers(tensor, (1, 2), (1, 2, 3))
