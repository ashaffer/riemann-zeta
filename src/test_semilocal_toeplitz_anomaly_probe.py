import numpy as np

from semilocal_toeplitz_anomaly_probe import (
    cayley_midpoint_grid,
    midpoint_fourier_coefficients,
    noncyclic_section_trace_split,
    padded_hardy_trace_split,
    triangular_hat_transform,
)


def test_hat_transform_and_cayley_jacobian() -> None:
    values = triangular_hat_transform(
        np.array([0.0]), np.array([0.3]), np.array([0.2]), np.array([2.5])
    )
    assert abs(values[0] - 0.5) < 1.0e-15

    theta, t, jacobian = cayley_midpoint_grid(1 << 12)
    index = 937
    numerical = (t[index + 1] - t[index - 1]) / (
        theta[index + 1] - theta[index - 1]
    )
    assert abs(numerical / jacobian[index] - 1) < 2.0e-6


def test_noncyclic_section_retains_the_unit_shift_anomaly() -> None:
    # U(z)=z has phase derivative one.  With P on n<=0,
    # P-U^*PU is the rank-one projection onto e_0.
    max_mode = 32
    u = np.zeros(2 * max_mode + 1, dtype=complex)
    g = np.zeros_like(u)
    u[max_mode + 1] = 1
    g[max_mode] = 1
    for length in (2, 5, 12):
        split = noncyclic_section_trace_split(u, g, max_mode, length)
        assert abs(split.total - 1) < 1.0e-14
        assert abs(split.minus_minus) < 1.0e-14


def test_midpoint_coefficients_reconstruct_a_smooth_anomaly() -> None:
    count = 1 << 14
    theta = 2 * np.pi * (np.arange(count) + 0.5) / count
    amplitude = 0.7
    u_values = np.exp(1j * amplitude * np.sin(theta))
    g_values = np.cos(theta)
    max_mode = 256
    u = midpoint_fourier_coefficients(u_values, max_mode)
    g = midpoint_fourier_coefficients(g_values, max_mode)
    split = padded_hardy_trace_split(u, g, max_mode, 16, 128)
    # mean(cos(theta) * amplitude*cos(theta)) = amplitude/2.
    assert abs(split.total.real - amplitude / 2) < 2.0e-12
    assert abs(split.total.imag) < 2.0e-12
