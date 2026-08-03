"""Finite-model census for negative squares of a logarithmic derivative.

For a real-symmetric finite zero multiset Z, set

    m(z) = - P'(z)/P(z) = -sum_{a in Z} 1/(z-a).

The script forms the Nevanlinna kernel

    (m(z)-conj(m(w))) / (z-conj(w))

at sample points in the upper half-plane.  Real zeros give a positive kernel;
each conjugate pair of nonreal zeros contributes one negative square.
"""

from __future__ import annotations

import numpy as np


def logarithmic_derivative(z: complex, zeros: list[complex]) -> complex:
    return -sum(1.0 / (z - zero) for zero in zeros)


def pick_matrix(points: list[complex], zeros: list[complex]) -> np.ndarray:
    matrix = np.empty((len(points), len(points)), dtype=complex)
    for row, z in enumerate(points):
        for column, w in enumerate(points):
            matrix[row, column] = (
                logarithmic_derivative(z, zeros)
                - np.conjugate(logarithmic_derivative(w, zeros))
            ) / (z - np.conjugate(w))
    return matrix


def report(label: str, zeros: list[complex], points: list[complex]) -> None:
    eigenvalues = np.linalg.eigvalsh(pick_matrix(points, zeros))
    tolerance = 1e-10
    print(label)
    print("  eigenvalues:", " ".join(f"{value:.9g}" for value in eigenvalues))
    print(f"  negative squares: {sum(value < -tolerance for value in eigenvalues)}")


def main() -> None:
    real_zeros = [-21.0, -14.0, 14.0, 21.0]
    off_axis_quartet = [-10.0 + 0.4j, 10.0 + 0.4j, -10.0 - 0.4j, 10.0 - 0.4j]
    sample_points = [
        -18.0 + 0.7j,
        -12.0 + 0.9j,
        -7.0 + 0.6j,
        0.0 + 0.8j,
        7.0 + 0.7j,
        12.0 + 1.1j,
        18.0 + 0.9j,
        3.0 + 2.0j,
    ]
    report("real zeros only", real_zeros, sample_points)
    report("one off-axis quartet", real_zeros + off_axis_quartet, sample_points)


if __name__ == "__main__":
    main()
