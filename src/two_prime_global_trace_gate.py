"""Exact finite unit tests for the global-trace/separate-polarization branch.

The arithmetic fixture is the semilocal place set ``{infinity, 3, 5}`` with
``25 < exp(L) < 27``.  It sees 3, 3^2, 5, and 5^2, while the mixed integer 15
lies in the same window and must have zero connected von Mangoldt weight.

This module deliberately does not fit a Gram matrix.  It records the smallest
linear-algebra gate separating functional-equation duality from a positive
adjoint metric.  The corresponding general statements are documented in
``results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`` and the 2x2
countermodel is kernel-checked in ``RHBridge.FinitePolarizationNoGo``.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Dict, Iterable, List, Tuple


Exponent = Tuple[int, int]
Matrix2 = Tuple[Tuple[Fraction, Fraction], Tuple[Fraction, Fraction]]


def connected_euler_jet(max_power: int = 2) -> Dict[Exponent, Fraction]:
    """Coefficients of ``-log(1-x)-log(1-y)`` through each pure power."""
    if max_power < 1:
        raise ValueError("max_power must be positive")
    answer: Dict[Exponent, Fraction] = {}
    for power in range(1, max_power + 1):
        answer[(power, 0)] = Fraction(1, power)
        answer[(0, power)] = Fraction(1, power)
    return answer


def connected_coefficient(a: int, b: int) -> Fraction:
    """All-order two-place connected coefficient.

    Applying ``-d/ds`` after ``x=p^-s`` turns the pure coefficient ``1/k``
    into the von Mangoldt coefficient ``log(p)`` at ``p^k``.  Every exponent
    with both coordinates positive is zero.
    """
    if a < 0 or b < 0 or a + b == 0:
        raise ValueError("expected a nonconstant monomial")
    if a and b:
        return Fraction(0)
    power = a or b
    return Fraction(1, power)


def semilocal_3_5_fixture() -> Dict[int, Tuple[int, int] | None]:
    """Pure prime powers and the mixed-composite control below 27.

    A value ``(p,k)`` denotes connected weight ``log(p)`` at ``p^k``; ``None``
    denotes exact cancellation.  Other primes are outside this semilocal place
    set rather than being assigned a coefficient here.
    """
    return {3: (3, 1), 5: (5, 1), 9: (3, 2), 15: None, 25: (5, 2)}


def _transpose(matrix: Matrix2) -> Matrix2:
    return ((matrix[0][0], matrix[1][0]),
            (matrix[0][1], matrix[1][1]))


def _multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2))
              for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def _add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def off_line_generator(a: Fraction) -> Matrix2:
    half = Fraction(1, 2)
    return ((half + a, Fraction(0)), (Fraction(0), half - a))


def alternating_pairing() -> Matrix2:
    return ((Fraction(0), Fraction(1)),
            (Fraction(-1), Fraction(0)))


def on_line_generator(gamma: Fraction) -> Matrix2:
    half = Fraction(1, 2)
    return ((half, -gamma), (gamma, half))


def identity_metric() -> Matrix2:
    return ((Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(1)))


def bridge_projection_p() -> Matrix2:
    """First noncommuting projection in the contractible-bridge control."""
    return ((Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0)))


def bridge_projection_q() -> Matrix2:
    """Second noncommuting projection in the contractible-bridge control."""
    half = Fraction(1, 2)
    return ((half, half), (half, half))


def bridge_projections_commute() -> bool:
    return (_multiply(bridge_projection_p(), bridge_projection_q())
            == _multiply(bridge_projection_q(), bridge_projection_p()))


def adjoint_law(left: Matrix2, metric: Matrix2) -> Matrix2:
    """Return ``left^T metric + metric left``."""
    return _add(_multiply(_transpose(left), metric),
                _multiply(metric, left))


def _trace(matrix: Matrix2) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def fake_global_supertrace(word: str) -> Fraction:
    """Supertrace of the exact contractible noncommutative bridge.

    ``P`` and ``Q`` act on one pure even state each.  They also act by two
    noncommuting projections on identical even and odd bridge copies joined by
    the identity differential.  Hence bridge words cancel in supertrace.
    """
    if not word or any(letter not in "PQ" for letter in word):
        raise ValueError("word must be a nonempty P/Q word")
    bridge = identity_metric()
    for letter in word:
        bridge = _multiply(bridge, bridge_projection_p()
                           if letter == "P" else bridge_projection_q())
    bridge_even_minus_odd = _trace(bridge) - _trace(bridge)
    pure_p = Fraction(1) if set(word) == {"P"} else Fraction(0)
    pure_q = Fraction(1) if set(word) == {"Q"} else Fraction(0)
    return pure_p + pure_q + bridge_even_minus_odd


def invariant_gram_pattern(labels: Iterable[Tuple[int, ...]]) -> List[List[bool]]:
    """Allowed Gram entries under independent self-adjoint place labels.

    Distinct joint weights are orthogonal.  ``True`` therefore means that an
    invariant Gram entry is not forced to vanish by equivariance alone.
    """
    weights = list(labels)
    if len(set(weights)) != len(weights):
        raise ValueError("the minimal gate expects distinct joint weights")
    return [[left == right for right in weights] for left in weights]


def minimal_all_place_labels() -> List[Tuple[int, int, int]]:
    """Weights for p,p^2,q,q^2 and the first two gamma modes."""
    return [(1, 0, 0), (2, 0, 0), (0, 1, 0),
            (0, 2, 0), (0, 0, 1), (0, 0, 2)]


def first_two_gamma_mode_sum(tau: Fraction) -> Fraction:
    """The n=0,1 rational part of the fixed digamma expansion.

    The full archimedean multiplier also contains the non-fitted constant
    ``-log(pi)-EulerGamma`` and the modes n>=2.
    """
    tau_half_sq = (tau / 2) ** 2
    total = Fraction(0)
    for n in range(2):
        shift = Fraction(n, 1) + Fraction(1, 4)
        total += Fraction(1, n + 1) - shift / (shift * shift + tau_half_sq)
    return total


def main() -> None:
    off_line = off_line_generator(Fraction(1, 3))
    omega = alternating_pairing()
    on_line = on_line_generator(Fraction(7, 5))
    identity = identity_metric()
    print("connected_jet", connected_euler_jet())
    print("semilocal_fixture", semilocal_3_5_fixture())
    print("off_line_duality", adjoint_law(off_line, omega) == omega)
    print("on_line_positive_control", adjoint_law(on_line, identity) == identity)
    print("fake_global_PQP_supertrace", fake_global_supertrace("PQP"))
    print("equivariant_gram_pattern", invariant_gram_pattern(minimal_all_place_labels()))
    print("first_two_gamma_modes_at_tau=1", first_two_gamma_mode_sum(Fraction(1)))


if __name__ == "__main__":
    main()
