"""Finite evaluator-model signature for Sonine/Fourier reflection.

The Hermitian zero involution is tau(rho)=1-conj(rho).  In biorthogonal
coordinates its reflection matrix fixes critical-line nodes and exchanges the
two nodes in every off-line tau-orbit.
"""

from __future__ import annotations

import numpy as np


def reflection_matrix(nodes: list[complex], tolerance: float = 1e-10) -> np.ndarray:
    matrix = np.zeros((len(nodes), len(nodes)), dtype=complex)
    for column, node in enumerate(nodes):
        reflected = 1.0 - np.conjugate(node)
        for row, candidate in enumerate(nodes):
            if abs(candidate - reflected) < tolerance:
                matrix[row, column] = 1.0
                break
        else:
            raise ValueError(f"node set is not reflection invariant at {node}")
    return matrix


def signature(matrix: np.ndarray, tolerance: float = 1e-10) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(matrix)
    return (
        sum(value > tolerance for value in eigenvalues),
        sum(value < -tolerance for value in eigenvalues),
        sum(abs(value) <= tolerance for value in eigenvalues),
    )


def main() -> None:
    critical_nodes = [0.5 + 14.0j, 0.5 - 14.0j]
    beta = 0.7
    off_line_quartet = [
        beta + 10.0j,
        1.0 - beta + 10.0j,
        beta - 10.0j,
        1.0 - beta - 10.0j,
    ]
    for label, nodes in (
        ("critical pair", critical_nodes),
        ("critical pair plus off-line quartet", critical_nodes + off_line_quartet),
    ):
        matrix = reflection_matrix(nodes)
        eigenvalues = np.linalg.eigvalsh(matrix)
        print(label)
        print("  eigenvalues:", " ".join(f"{value:.1f}" for value in eigenvalues))
        print("  signature (+,-,0):", signature(matrix))


if __name__ == "__main__":
    main()
