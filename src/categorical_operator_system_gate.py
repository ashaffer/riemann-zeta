"""Finite operator-system admission gate for the two-packet zeta fixture.

This module keeps two logically different objects separate.

* The exact normalized reflected-pair (``mirror``) algebra is
  ``span{I, J}``, where ``J`` exchanges the packets.
* The smallest support-asymmetric enlargement adds the left/right contrast
  ``Z`` and has self-adjoint part ``Sym_2(R)``.

The first system is detected by the two parity states and has an explicit
completely positive recovery.  The second cannot be order-reflected by any
finite family of scalar states.  A full matrix-valued pair probe has a UCP
inverse, but it simply retains the complete two-packet matrix.

The exact statements use only rational arithmetic and ``sqrt(2)`` (SymPy is
used to check them).  The optional arithmetic-place assembly is a numerical
sanity check for the repository's L=7/4, two-hat Weil fixture.  Its gamma
integral is not interval-certified and is never used to prove an exact claim.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np
import sympy as sp


I2 = sp.eye(2)
J2 = sp.Matrix([[0, 1], [1, 0]])
Z2 = sp.Matrix([[1, 0], [0, -1]])


@dataclass(frozen=True)
class NumericPlaceFixture:
    """Whitened numerical place matrices for the L=7/4 two-hat fixture."""

    gram: np.ndarray
    gamma: np.ndarray
    pole: np.ndarray
    prime2: np.ndarray
    normalized_gamma: np.ndarray
    normalized_pole: np.ndarray
    normalized_prime2: np.ndarray


def exact_two_hat_gram() -> sp.Matrix:
    """Exact L2 Gram matrix at L=7/4, m=2.

    The hat half-width is d=7/24 and the centers are +/-7/48.  Hence the
    diagonal overlap is 2d/3 and the adjacent overlap is d/6.
    """
    return sp.Rational(7, 144) * (4 * I2 + J2)


def exact_prime2_form() -> sp.Matrix:
    """Exact unsigned p=2 translation form in the two-hat coefficient basis.

    Only one directed overlap survives.  Symmetrization gives ``p J`` with

        p = 96 log(2) (7/8-log(2))^3 / (49 sqrt(2)) > 0.

    The completed Weil form contains the negative of this matrix; its sign
    does not change the generated operator system.
    """
    return exact_prime2_coefficient() * J2


def exact_prime2_coefficient() -> sp.Expr:
    """Positive off-diagonal coefficient of the exact p=2 form."""
    return (sp.Rational(96, 49) * sp.log(2)
            * (sp.Rational(7, 8) - sp.log(2)) ** 3 / sp.sqrt(2))


def exact_normalized_prime2_form() -> sp.Matrix:
    """Whitened p=2 form, written without a matrix square root.

    The Gram and prime matrices commute, so G^{-1/2} P G^{-1/2}=G^{-1}P.
    In particular its J coefficient is nonzero, proving exactly that support
    plus p=2 generate the mirror system ``span{I,J}``.
    """
    return sp.simplify(exact_two_hat_gram().inv() * exact_prime2_form())


def exact_support_contrast_scale() -> sp.Expr:
    """Scale in P_left-P_right=(sqrt(15)/4) Z after Gram whitening.

    ``P_left`` and ``P_right`` are the rank-one projections onto the two
    normalized original hat rays in the whitened Hilbert space.  Thus the
    normalized contrast Z is defined from packet/support data before zeros or
    a negative eigenvector are selected.
    """
    return sp.sqrt(15) / 4


def parity_vectors() -> tuple[sp.Matrix, sp.Matrix]:
    root2 = sp.sqrt(2)
    return (sp.Matrix([1, 1]) / root2,
            sp.Matrix([1, -1]) / root2)


def vector_expectation(matrix: sp.Matrix, vector: sp.Matrix) -> sp.Expr:
    return sp.simplify((vector.T * matrix * vector)[0])


def mirror_observation_matrix(probes: Sequence[sp.Matrix]) -> sp.Matrix:
    """Observation matrix on the ordered Hermitian basis (I,J)."""
    return sp.Matrix([
        [vector_expectation(I2, vector),
         vector_expectation(J2, vector)]
        for vector in probes
    ])


def asymmetric_observation_matrix(probes: Sequence[sp.Matrix]) -> sp.Matrix:
    """Observation matrix on the ordered Hermitian basis (I,J,Z)."""
    return sp.Matrix([
        [vector_expectation(I2, vector),
         vector_expectation(J2, vector),
         vector_expectation(Z2, vector)]
        for vector in probes
    ])


def symmetry_recovery_effects() -> tuple[sp.Matrix, sp.Matrix]:
    """Positive effects giving the exact recovery C^2 -> M_2.

    If Phi(A)=(<e_+,Ae_+>,<e_-,Ae_->) on span{I,J}, then
    Psi(x,y)=x P_+ + y P_- and Psi Phi is the identity on that system.
    The direct-sum Choi datum is ``P_+ direct_sum P_-``.
    """
    plus, minus = parity_vectors()
    return plus * plus.T, minus * minus.T


def symmetry_recovery_block_choi() -> sp.Matrix:
    plus, minus = symmetry_recovery_effects()
    return sp.diag(plus, minus)


def four_scalar_counterexample() -> sp.Matrix:
    """Exact indefinite matrix positive on coordinate and parity probes.

    It is ``I-(9/8)ww^T`` for w at angle pi/8.  Its eigenvalues are
    ``1`` and ``-1/8``.  Each of e1,e2,e+,e- has expectation at least
    ``(14-9 sqrt(2))/32 > 0``.
    """
    return (sp.Rational(7, 16) * I2
            - sp.Rational(9, 32) * sp.sqrt(2) * (J2 + Z2))


def finite_scalar_counterexample(angles: Iterable[float]) -> np.ndarray:
    """Construct an indefinite matrix missed by any finite real scalar probes.

    Probe rays are given by angles modulo pi.  Put the negative eigenvector at
    the midpoint of the largest projective angular gap.  If ``delta`` is that
    gap, the nearest probe has squared overlap ``cos(delta/2)^2 < 1``.  Taking
    ``c`` strictly between 1 and its reciprocal makes
    ``A=I-c ww^T`` indefinite while every supplied expectation is positive.

    This floating-point constructor illustrates the exact nonpolyhedral
    theorem; it is not an interval certificate.
    """
    values = sorted({float(angle) % math.pi for angle in angles})
    if not values:
        return np.diag([-1.0, 1.0])
    extended = values + [values[0] + math.pi]
    gaps = [extended[i + 1] - extended[i] for i in range(len(values))]
    index = int(np.argmax(gaps))
    delta = gaps[index]
    midpoint = (extended[index] + delta / 2.0) % math.pi
    overlap = math.cos(delta / 2.0) ** 2
    coefficient = (1.0 + 1.0 / overlap) / 2.0
    w = np.array([math.cos(midpoint), math.sin(midpoint)])
    return np.eye(2) - coefficient * np.outer(w, w)


def cross_aware_unitary() -> sp.Matrix:
    plus, minus = parity_vectors()
    return sp.Matrix.hstack(plus, minus)


def unitary_recovery_choi() -> sp.Matrix:
    """Choi matrix for B |-> U B U*, the inverse full-pair recovery."""
    unitary = cross_aware_unitary()
    # Column-major vectorization matches the standard Choi convention.
    vectorized = sp.Matrix([
        unitary[0, 0], unitary[1, 0],
        unitary[0, 1], unitary[1, 1],
    ])
    return sp.simplify(vectorized * vectorized.T)


def block_dephasing(matrix: np.ndarray, split: int) -> np.ndarray:
    """Conditional expectation onto two diagonal matrix blocks."""
    matrix = np.asarray(matrix)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    if not 0 < split < matrix.shape[0]:
        raise ValueError("split must be strictly inside the matrix")
    answer = np.zeros_like(matrix)
    answer[:split, :split] = matrix[:split, :split]
    answer[split:, split:] = matrix[split:, split:]
    return answer


def block_dephasing_covariance(matrix: np.ndarray, split: int) -> np.ndarray:
    """Kadison covariance E(H*H)-E(H*)E(H) for block dephasing."""
    matrix = np.asarray(matrix)
    adjoint = matrix.conj().T
    return (block_dephasing(adjoint @ matrix, split)
            - block_dephasing(adjoint, split)
            @ block_dephasing(matrix, split))


def _inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2.0)
    if values[0] <= 0.0:
        raise ValueError("matrix must be positive definite")
    return (vectors @ np.diag(values ** -0.5) @ vectors.conj().T)


def normalized_block_covariance(
    positive_left: np.ndarray,
    cross: np.ndarray,
    positive_right: np.ndarray,
) -> dict[str, float | np.ndarray]:
    """Compare block-dephasing covariance with the Schur coupling.

    For C=A^{-1/2} B D^{-1/2}, dephasing the normalized block matrix
    ``[[I,C],[C*,I]]`` has covariance ``diag(CC*,C*C)``.  Its norm is
    exactly ``||C||^2``.  Therefore the covariance inequality ``Cov<I`` is
    precisely the usual strict Schur-complement criterion, not a new sign.
    """
    left = np.asarray(positive_left)
    right = np.asarray(positive_right)
    cross = np.asarray(cross)
    left_root = _inverse_square_root(left)
    right_root = _inverse_square_root(right)
    normalized_cross = left_root @ cross @ right_root
    left_size, right_size = left.shape[0], right.shape[0]
    normalized = np.block([
        [np.eye(left_size), normalized_cross],
        [normalized_cross.conj().T, np.eye(right_size)],
    ])
    covariance = block_dephasing_covariance(normalized, left_size)
    coupling = float(np.linalg.svd(normalized_cross,
                                   compute_uv=False)[0])
    covariance_norm = float(np.linalg.norm(covariance, ord=2))
    return {
        "normalized_cross": normalized_cross,
        "covariance": covariance,
        "coupling": coupling,
        "covariance_norm": covariance_norm,
        "norm_identity_error": abs(covariance_norm - coupling * coupling),
    }


def _hat_overlap(differences: np.ndarray, width: float) -> np.ndarray:
    scaled = np.abs(differences) / width
    return width * np.where(
        scaled <= 1.0,
        2.0 / 3.0 - scaled * scaled + scaled ** 3 / 2.0,
        np.where(scaled <= 2.0, (2.0 - scaled) ** 3 / 6.0, 0.0),
    )


def _hat_fourier(frequencies: np.ndarray, centers: np.ndarray,
                 width: float) -> np.ndarray:
    argument = frequencies[:, None] * width / 2.0
    sinc_squared = np.sinc(argument / math.pi) ** 2
    return (width * sinc_squared
            * np.exp(-1j * frequencies[:, None] * centers[None, :]))


def numerical_place_fixture(*, support_parameter: float = 7.0 / 4.0,
                            size: int = 2, cutoff: float = 240.0,
                            intervals: int = 24000) -> NumericPlaceFixture:
    """Assemble the independent support/gamma/pole/p=2 finite fixture.

    This follows ``weil_core.build_form`` but returns the individual place
    matrices.  Simpson quadrature is chunked and uses only O(intervals+size^2)
    memory.  ``intervals`` must be even.  The calculation is diagnostic: no
    interval enclosure of the digamma integral is claimed.
    """
    if size < 2:
        raise ValueError("size must be at least two")
    if intervals <= 0 or intervals % 2:
        raise ValueError("intervals must be a positive even integer")

    module_dir = pathlib.Path(__file__).resolve().parent
    if str(module_dir) not in sys.path:
        sys.path.insert(0, str(module_dir))
    from weil_core import cdig  # local import keeps exact tests lightweight

    ell = support_parameter / 2.0
    width = ell / (size + 1)
    centers = np.linspace(-ell / 2.0 + width,
                          ell / 2.0 - width, size)
    differences = centers[None, :] - centers[:, None]
    gram = _hat_overlap(differences, width)

    frequencies = np.linspace(1e-9, cutoff, intervals + 1)
    step = frequencies[1] - frequencies[0]
    weights = np.ones(intervals + 1)
    weights[1:-1:2] = 4.0
    weights[2:-1:2] = 2.0
    weights *= step / 3.0
    symbol_weights = np.real(cdig(0.25 + 0.5j * frequencies)) * weights

    gamma_integral = np.zeros((size, size), dtype=float)
    chunk = 4000
    for start in range(0, len(frequencies), chunk):
        stop = min(start + chunk, len(frequencies))
        transform = _hat_fourier(frequencies[start:stop], centers, width)
        gamma_integral += np.real(
            (transform * symbol_weights[start:stop, None]).conj().T
            @ transform
        )
    gamma = gamma_integral / math.pi - math.log(math.pi) * gram

    exponent = 0.5
    common = ((2.0 * np.cosh(exponent * width) - 2.0)
              / (exponent * exponent * width))
    pole_plus = np.exp(exponent * centers) * common
    pole_minus = np.exp(-exponent * centers) * common
    pole = (np.outer(pole_plus, pole_minus)
            + np.outer(pole_minus, pole_plus))

    shifted = _hat_overlap(differences + math.log(2.0), width)
    prime2 = ((2.0 * math.log(2.0) / math.sqrt(2.0))
              * (shifted + shifted.T) / 2.0)

    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    inverse_root = (eigenvectors
                    @ np.diag(eigenvalues ** -0.5)
                    @ eigenvectors.T)

    def normalize(matrix: np.ndarray) -> np.ndarray:
        answer = inverse_root @ matrix @ inverse_root
        return (answer + answer.T) / 2.0

    return NumericPlaceFixture(
        gram=gram,
        gamma=gamma,
        pole=pole,
        prime2=prime2,
        normalized_gamma=normalize(gamma),
        normalized_pole=normalize(pole),
        normalized_prime2=normalize(prime2),
    )


def mirror_coordinates(matrix: np.ndarray) -> tuple[float, float, float]:
    """Return I coefficient, J coefficient, and Frobenius residual."""
    matrix = np.asarray(matrix, dtype=float)
    identity_coefficient = float(np.trace(matrix) / 2.0)
    exchange_coefficient = float((matrix[0, 1] + matrix[1, 0]) / 2.0)
    projection = (identity_coefficient * np.eye(2)
                  + exchange_coefficient * np.array([[0.0, 1.0],
                                                      [1.0, 0.0]]))
    return (identity_coefficient, exchange_coefficient,
            float(np.linalg.norm(matrix - projection)))


def _sympy_float(value: sp.Expr) -> float:
    return float(sp.N(value, 30))


def exact_gate_summary() -> dict[str, object]:
    e1 = sp.Matrix([1, 0])
    e2 = sp.Matrix([0, 1])
    plus, minus = parity_vectors()
    coordinate_observation = mirror_observation_matrix((e1, e2))
    parity_observation = mirror_observation_matrix((plus, minus))
    four_observation = asymmetric_observation_matrix((e1, e2, plus, minus))
    counterexample = four_scalar_counterexample()
    expectations = [vector_expectation(counterexample, vector)
                    for vector in (e1, e2, plus, minus)]
    eigenvalues = list(counterexample.eigenvals().keys())
    p2_coefficient = exact_prime2_coefficient()
    prime_i = -sp.Rational(48, 35) * p2_coefficient
    prime_j = sp.Rational(192, 35) * p2_coefficient
    mirror_choi_eigenvalues = []
    for value, multiplicity in symmetry_recovery_block_choi().eigenvals().items():
        mirror_choi_eigenvalues.extend([_sympy_float(value)] * multiplicity)
    pair_choi_eigenvalues = []
    for value, multiplicity in unitary_recovery_choi().eigenvals().items():
        pair_choi_eigenvalues.extend([_sympy_float(value)] * multiplicity)
    return {
        "exact_fixture": {
            "L": "7/4",
            "m": 2,
            "gram": str(exact_two_hat_gram()),
            "normalized_prime2_I_coefficient": str(prime_i),
            "normalized_prime2_J_coefficient": str(prime_j),
            "normalized_prime2_J_coefficient_numeric": _sympy_float(prime_j),
            "support_contrast_scale": str(exact_support_contrast_scale()),
        },
        "mirror_coordinate_probes": {
            "observation_rank": int(coordinate_observation.rank()),
            "kernel_witness": "J",
            "order_reflecting": False,
            "cp_recovery": False,
            "reason": "nonzero Hermitian kernel element",
        },
        "mirror_parity_probes": {
            "observation_rank": int(parity_observation.rank()),
            "order_reflecting": True,
            "cp_recovery": True,
            "block_choi_eigenvalues": sorted(mirror_choi_eigenvalues),
            "warning": "outputs are exactly the original parity eigenvalues",
        },
        "asymmetric_four_scalar_probes": {
            "observation_rank": int(four_observation.rank()),
            "counterexample": str(counterexample),
            "counterexample_eigenvalues": sorted(_sympy_float(v)
                                                  for v in eigenvalues),
            "probe_expectations": [_sympy_float(v) for v in expectations],
            "minimum_exact_expectation": "(14-9*sqrt(2))/32",
            "order_reflecting": False,
            "cp_recovery": False,
            "reason": "positive observation of an indefinite system element",
        },
        "all_finite_scalar_probes_on_Sym2": {
            "order_reflecting": False,
            "reason": "finite halfspace intersection is polyhedral; Pos_2 is not",
        },
        "cross_aware_matrix_probe": {
            "order_reflecting": True,
            "cp_recovery": True,
            "choi_eigenvalues": sorted(pair_choi_eigenvalues),
            "warning": "unitary full-pair observation retains the whole matrix",
        },
        "block_dephasing_covariance": {
            "exact_formula": "diag(B B*, B* B)",
            "normalized_formula": "diag(C C*, C* C)",
            "C": "A^(-1/2) B D^(-1/2)",
            "covariance_norm": "||C||^2",
            "decision": "equivalent to the existing Schur coupling threshold",
        },
    }


def numeric_gate_summary(fixture: NumericPlaceFixture) -> dict[str, object]:
    place_matrices = {
        "gamma": fixture.normalized_gamma,
        "pole": fixture.normalized_pole,
        "prime2": fixture.normalized_prime2,
    }
    coordinates = {
        name: {
            "I": mirror_coordinates(matrix)[0],
            "J": mirror_coordinates(matrix)[1],
            "mirror_residual_frobenius": mirror_coordinates(matrix)[2],
        }
        for name, matrix in place_matrices.items()
    }
    columns = [np.eye(2).reshape(-1)]
    columns.extend(matrix.reshape(-1) for matrix in place_matrices.values())
    singular_values = np.linalg.svd(np.column_stack(columns),
                                    compute_uv=False)
    rank_tolerance = singular_values[0] * 1e-11
    return {
        "place_coordinates": coordinates,
        "symmetric_generator_singular_values": singular_values.tolist(),
        "symmetric_generator_numeric_rank": int(np.sum(singular_values
                                                        > rank_tolerance)),
        "asymmetric_rank_after_Z": 3,
        "certification": "floating-point Simpson/digamma diagnostic only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=float, default=240.0)
    parser.add_argument("--intervals", type=int, default=24000)
    parser.add_argument("--skip-numeric", action="store_true")
    args = parser.parse_args()

    summary = exact_gate_summary()
    if not args.skip_numeric:
        fixture = numerical_place_fixture(cutoff=args.cutoff,
                                          intervals=args.intervals)
        summary["numeric_arithmetic_sanity"] = numeric_gate_summary(fixture)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
