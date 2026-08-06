"""Fail-fast diagnostics for completed-Weil positive commutators.

The arithmetic Weil matrix ``Q`` is assembled in the orthonormal Legendre
basis used by :mod:`spectral_margins`.  If ``X`` is multiplication by the
logarithmic coordinate, the standard velocity-adapted finite conjugate is

    V = i [Q, X],       D = (X V + V X) / 2,
    C = i [Q, D].

Every eigenvector of ``Q`` has zero expectation against ``C``.  The script
checks that identity numerically and measures the least scalar ``kappa`` for
which ``C + kappa Q`` becomes positive in a positive Galerkin section.  This
last quantity is a diagnostic, not a proof.  Existence of a positive
``kappa`` making the repair positive definite is equivalent to strict
positivity of the finite matrix; semidefiniteness at ``kappa=0`` is not.

The default run is deliberately small.  Use larger dimensions explicitly;
assembling the high-precision Weil matrices is the expensive step.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np


def hermitian_part(matrix: np.ndarray) -> np.ndarray:
    """Remove floating-point skew-Hermitian noise."""

    return (matrix + matrix.conj().T) / 2


def legendre_position_matrix(support: float, dimension: int) -> np.ndarray:
    """Multiplication by ``x`` on the first normalized Legendre modes.

    The interval is ``[-support/4, support/4]``, matching
    ``spectral_margins.spectral_form``.
    """

    radius = support / 4.0
    position = np.zeros((dimension, dimension), dtype=float)
    for degree in range(dimension - 1):
        coefficient = (
            radius
            * (degree + 1)
            / np.sqrt((2 * degree + 1) * (2 * degree + 3))
        )
        position[degree, degree + 1] = coefficient
        position[degree + 1, degree] = coefficient
    return position


def adapted_virial_commutator(
    weil: np.ndarray, position: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return ``(velocity, conjugate, commutator)`` for one finite section."""

    weil = hermitian_part(np.asarray(weil, dtype=complex))
    position = hermitian_part(np.asarray(position, dtype=complex))
    velocity = hermitian_part(1j * (weil @ position - position @ weil))
    conjugate = hermitian_part(
        (position @ velocity + velocity @ position) / 2
    )
    commutator = hermitian_part(
        1j * (weil @ conjugate - conjugate @ weil)
    )
    return velocity, conjugate, commutator


@dataclass(frozen=True)
class VirialDiagnostic:
    support: float
    dimension: int
    lambda_min: float
    max_eigenstate_commutator_diagonal: float
    commutator_trace: float
    kappa_critical: float
    whitened_min: float
    whitened_max: float


def diagnose_matrix(
    support: float, weil: np.ndarray
) -> VirialDiagnostic:
    """Diagnose the adapted commutator of one positive Weil matrix.

    When ``Q`` is strictly positive, ``kappa_critical`` is the infimum of
    scalars for which ``C + kappa Q`` is positive semidefinite.  For a
    nonpositive ``Q`` the whitening diagnostic is undefined and the routine
    returns infinity.  Independently, the virial identity shows that no
    positive ``kappa`` can make the repaired form strictly positive on a
    nonpositive eigenvector.
    """

    weil = hermitian_part(np.asarray(weil, dtype=float))
    dimension = weil.shape[0]
    if weil.shape != (dimension, dimension):
        raise ValueError("weil matrix must be square")
    position = legendre_position_matrix(support, dimension)
    _, _, commutator = adapted_virial_commutator(weil, position)

    eigenvalues, eigenvectors = np.linalg.eigh(weil)
    eigenbasis_commutator = eigenvectors.conj().T @ commutator @ eigenvectors
    max_diagonal = float(
        np.max(np.abs(np.real(np.diag(eigenbasis_commutator))))
    )
    trace = float(np.real(np.trace(commutator)))

    if eigenvalues[0] <= 0:
        kappa_critical = float("inf")
        whitened_min = float("nan")
        whitened_max = float("nan")
    else:
        inverse_sqrt = (
            eigenvectors
            @ np.diag(1.0 / np.sqrt(eigenvalues))
            @ eigenvectors.conj().T
        )
        whitened = hermitian_part(
            inverse_sqrt @ commutator @ inverse_sqrt
        )
        whitened_eigenvalues = np.linalg.eigvalsh(whitened)
        whitened_min = float(whitened_eigenvalues[0])
        whitened_max = float(whitened_eigenvalues[-1])
        kappa_critical = max(0.0, -whitened_min)

    return VirialDiagnostic(
        support=support,
        dimension=dimension,
        lambda_min=float(eigenvalues[0]),
        max_eigenstate_commutator_diagonal=max_diagonal,
        commutator_trace=trace,
        kappa_critical=kappa_critical,
        whitened_min=whitened_min,
        whitened_max=whitened_max,
    )


def _format(result: VirialDiagnostic) -> str:
    return ",".join(
        [
            f"{result.support:.9g}",
            str(result.dimension),
            f"{result.lambda_min:.12e}",
            f"{result.max_eigenstate_commutator_diagonal:.12e}",
            f"{result.commutator_trace:.12e}",
            f"{result.kappa_critical:.12e}",
            f"{result.whitened_min:.12e}",
            f"{result.whitened_max:.12e}",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", nargs="+", type=float, default=[3.27],
        help="program support values L (prime 5 is active for L > 2 log 5)",
    )
    parser.add_argument(
        "--dimensions", nargs="+", type=int, default=[12, 16],
        help="Legendre Galerkin dimensions; larger values can be expensive",
    )
    parser.add_argument("--dps", type=int, default=35)
    args = parser.parse_args()

    # Imported lazily so the algebraic unit tests remain lightweight.
    from spectral_margins import spectral_form

    print(
        "support,dimension,lambda_min,max_eigenstate_commutator_diagonal,"
        "commutator_trace,kappa_critical,whitened_min,whitened_max"
    )
    for support in args.supports:
        for dimension in args.dimensions:
            weil = np.array(
                spectral_form(
                    support, dimension, dps=args.dps
                ).tolist(),
                dtype=float,
            )
            print(_format(diagnose_matrix(support, weil)), flush=True)


if __name__ == "__main__":
    main()
