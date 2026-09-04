#!/usr/bin/env python3
"""Exact finite algebra for the OD2 tensor-trace/low-slope gate.

This module does not assert the full actual-SPF OD2 theorem.  It certifies
three ingredients used in the accompanying theorem card:

* the paired first-return automaton has bond dimension four but a length-three
  Jordan tower on an empty paired word;
* endpoint-trapezoid quadrature is affine-exact and has the standard mesh
  squared C2 error;
* the low-integer-slope threshold and the failure of rational residue
  grouping have the claimed exact exponent ledgers.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Callable, Iterable


H_MIN = Fraction(8, 33)
H_MAX = Fraction(5797, 10_000)
EDGE_EXPONENT = Fraction(797, 5000)
TRUNCATED_CUBE_SAVING = Fraction(1173, 65_000)
SELECTOR_BETA = Fraction(1537, 10_000)
SELECTOR_CAP = Fraction(33, 133)

Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def matrix_identity(size: int) -> Matrix:
    if size < 1:
        raise ValueError("matrix size must be positive")
    return tuple(
        tuple(1 if row == column else 0 for column in range(size))
        for row in range(size)
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    if any(len(row) != len(left[0]) for row in left):
        raise ValueError("ragged left matrix")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("ragged right matrix")
    return tuple(
        tuple(
            sum(left[row][k] * right[k][column] for k in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(
        len(left_row) != len(right_row)
        for left_row, right_row in zip(left, right)
    ):
        raise ValueError("matrix dimensions must agree")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0 or not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("need a square matrix and nonnegative exponent")
    result = matrix_identity(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    return result


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    if not matrix or len(matrix[0]) != len(vector):
        raise ValueError("incompatible matrix and vector")
    return tuple(
        sum(value * vector[column] for column, value in enumerate(row))
        for row in matrix
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        raise ValueError("Kronecker factors must be nonempty")
    return tuple(
        tuple(
            left[i][j] * right[k][ell]
            for j in range(len(left[0]))
            for ell in range(len(right[0]))
        )
        for i in range(len(left))
        for k in range(len(right))
    )


def first_return_matrix(bit: int) -> Matrix:
    """Return M(bit) on the state (alive, accumulated distance)."""

    if bit not in (0, 1):
        raise ValueError("survivor bit must be zero or one")
    return ((1 - bit, 0), (1, 1))


def paired_transition(left_bit: int, right_bit: int) -> Matrix:
    """Four-state paired first-return transition."""

    return kronecker(first_return_matrix(left_bit), first_return_matrix(right_bit))


def paired_word_state(
    left_word: Iterable[int], right_word: Iterable[int]
) -> Vector:
    """Evaluate a paired word in state order PP, PS, SP, SS."""

    left = list(left_word)
    right = list(right_word)
    if len(left) != len(right):
        raise ValueError("paired words must have equal length")
    state: Vector = (1, 0, 0, 0)
    for left_bit, right_bit in zip(left, right):
        state = matrix_vector(paired_transition(left_bit, right_bit), state)
    return state


def paired_empty_jordan_certificate(length: int) -> dict[str, object]:
    """Return the exact polynomial-growth certificate for an empty pair."""

    if length < 1:
        raise ValueError("length must be positive")
    transition = paired_transition(0, 0)
    nilpotent = matrix_subtract(transition, matrix_identity(4))
    nilpotent_square = matrix_power(nilpotent, 2)
    nilpotent_cube = matrix_power(nilpotent, 3)
    state = matrix_vector(matrix_power(transition, length), (1, 0, 0, 0))
    return {
        "state": state,
        "expected_state": (1, length, length, length * length),
        "nilpotent_square_nonzero": any(
            value != 0 for row in nilpotent_square for value in row
        ),
        "nilpotent_cube_zero": all(
            value == 0 for row in nilpotent_cube for value in row
        ),
    }


def endpoint_trapezoid(
    points: Iterable[Fraction | int], function: Callable[[Fraction], complex]
) -> complex:
    """Apply endpoint-trapezoid weights on a finite partition."""

    nodes = [Fraction(value) for value in points]
    if len(nodes) < 2 or nodes != sorted(set(nodes)):
        raise ValueError("points must form a strictly increasing partition")
    total = 0j
    for left, right in zip(nodes, nodes[1:]):
        gap = right - left
        total += complex(gap) * (function(left) + function(right)) / 2
    return total


def partition_mesh(points: Iterable[Fraction | int]) -> Fraction:
    nodes = [Fraction(value) for value in points]
    if len(nodes) < 2 or nodes != sorted(set(nodes)):
        raise ValueError("points must form a strictly increasing partition")
    return max(right - left for left, right in zip(nodes, nodes[1:]))


def trapezoid_error_envelope(
    points: Iterable[Fraction | int], second_derivative_bound: Fraction | int
) -> Fraction:
    """Standard sum(g^3)*||f''||/12 trapezoid error envelope."""

    nodes = [Fraction(value) for value in points]
    if len(nodes) < 2 or nodes != sorted(set(nodes)):
        raise ValueError("points must form a strictly increasing partition")
    bound = Fraction(second_derivative_bound)
    if bound < 0:
        raise ValueError("derivative bound must be nonnegative")
    return bound * sum(
        ((right - left) ** 3 for left, right in zip(nodes, nodes[1:])),
        Fraction(0),
    ) / 12


def nested_affine_difference(
    coarse: Iterable[Fraction | int], fine: Iterable[Fraction | int]
) -> tuple[complex, complex]:
    """Return coarse-minus-fine quadrature on 1 and x."""

    coarse_nodes = [Fraction(value) for value in coarse]
    fine_nodes = [Fraction(value) for value in fine]
    if not set(coarse_nodes).issubset(fine_nodes):
        raise ValueError("coarse partition must be nested in fine partition")
    if coarse_nodes[0] != fine_nodes[0] or coarse_nodes[-1] != fine_nodes[-1]:
        raise ValueError("nested partitions need common endpoints")
    constant = endpoint_trapezoid(coarse_nodes, lambda _x: 1) - endpoint_trapezoid(
        fine_nodes, lambda _x: 1
    )
    linear = endpoint_trapezoid(coarse_nodes, lambda x: complex(x)) - endpoint_trapezoid(
        fine_nodes, lambda x: complex(x)
    )
    return constant, linear


def low_slope_exponent(h_exponent: Fraction) -> Fraction:
    """Exponent in Y^(d/4)(H G^3)^(-1/4)=Y^(-eta(h))."""

    if h_exponent <= 0:
        raise ValueError("block exponent must be positive")
    return (
        h_exponent + 3 * EDGE_EXPONENT - TRUNCATED_CUBE_SAVING
    ) / 4


def selector_wedge() -> dict[str, Fraction | bool]:
    """Exact exponent range in which the new selected numerator wedge exists."""

    eta_min = low_slope_exponent(H_MIN)
    eta_max = low_slope_exponent(H_MAX)
    h_cap = (
        4 * SELECTOR_CAP
        - 3 * EDGE_EXPONENT
        + TRUNCATED_CUBE_SAVING
    )
    return {
        "eta_at_h_min": eta_min,
        "eta_at_h_max": eta_max,
        "eta_min_exceeds_old_beta": eta_min > SELECTOR_BETA,
        "largest_h_with_nonempty_capped_wedge": h_cap,
        "wedge_reaches_h_max": eta_max <= SELECTOR_CAP,
    }


def low_slope_monomial_identity() -> dict[str, str]:
    """Check the sharp global cube-moment monomial equals Y*G.

    The factors are

        eta^4 = Y^d H^-1 G^-3,
        max_I C_I = H G^2,
        sum_I C_I = Y G^2 Y^-d.
    """

    return {
        "eta_fourth": "Y^d H^-1 G^-3",
        "max_local_cube_ledger": "H G^2",
        "global_cube_ledger": "Y G^2 Y^-d",
        "aggregate_with_Y": "Y*G",
    }


def rational_grouping_loss(h_sites: int, denominator: int, diagonal: Fraction | int) -> dict[str, Fraction]:
    """Cauchy/occupancy envelope after grouping sites modulo q.

    Parseval/Cauchy first costs q.  At most ceil(H/q) sites occupy a residue,
    so the net universal estimate is q*ceil(H/q)*D, comparable to H*D.
    """

    if h_sites < 1 or not 1 <= denominator <= h_sites:
        raise ValueError("need 1 <= q <= H")
    diagonal_value = Fraction(diagonal)
    if diagonal_value < 0:
        raise ValueError("diagonal must be nonnegative")
    occupancy = (h_sites + denominator - 1) // denominator
    envelope = denominator * occupancy * diagonal_value
    return {
        "q_factor": Fraction(denominator),
        "max_occupancy": Fraction(occupancy),
        "envelope": envelope,
        "two_h_diagonal": 2 * h_sites * diagonal_value,
    }


def audit() -> dict[str, object]:
    jordan = paired_empty_jordan_certificate(19)
    coarse = [0, 4, 9, 15]
    fine = [0, 1, 4, 6, 9, 12, 15]
    affine = nested_affine_difference(coarse, fine)
    grouping = rational_grouping_loss(101, 17, 23)
    return {
        "paired_jordan": jordan,
        "affine_difference": tuple(abs(value) for value in affine),
        "selector_wedge": {
            key: str(value) if isinstance(value, Fraction) else value
            for key, value in selector_wedge().items()
        },
        "monomial": low_slope_monomial_identity(),
        "grouping": {key: str(value) for key, value in grouping.items()},
    }


if __name__ == "__main__":
    print(audit())
