"""Exponent ledger for the coefficient-sensitive QP cross-Gram gate.

The companion report applies Heath-Brown's difference-set large-value
estimate to the shifted matrix ``Phi(tau+t_i-t_j)``.  This module records the
three resulting powers and the exact repeated-lag coefficient of an
arithmetic progression.  It proves no estimate for the actual primes.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class HeathBrownLedger:
    packet_exponent: float
    pair_count_term: float
    repeated_difference_term: float
    aperture_term: float
    pair_count_frobenius: float
    repeated_difference_frobenius: float
    aperture_frobenius: float
    required_residual: float
    repeated_difference_gap: float


def heath_brown_ledger(c: float = 0.019, aperture: float = 50.0 / 33.0) -> HeathBrownLedger:
    """Return normalized square-sum and Frobenius exponents.

    With ``R=Y^(2c)`` and ``B=Y^aperture``, Heath-Brown gives

    ``sum |Phi(tau+t_i-t_j)|^2``
    ``<= Y^o(R^2/Y + R + R^(5/4)B^(1/2)/Y)``.
    """

    if c <= 0.0 or aperture <= 0.0:
        raise ValueError("c and aperture must be positive")
    pair_count = 4.0 * c - 1.0
    repeated = 2.0 * c
    aperture_term = 2.5 * c + 0.5 * aperture - 1.0
    required = -c
    repeated_frobenius = 0.5 * repeated
    return HeathBrownLedger(
        packet_exponent=2.0 * c,
        pair_count_term=pair_count,
        repeated_difference_term=repeated,
        aperture_term=aperture_term,
        pair_count_frobenius=0.5 * pair_count,
        repeated_difference_frobenius=repeated_frobenius,
        aperture_frobenius=0.5 * aperture_term,
        required_residual=required,
        repeated_difference_gap=repeated_frobenius - required,
    )


def repeated_lag_pair_count(length: int, lag: int) -> int:
    """Ordered AP pairs ``(i,j)`` with ``i-j=lag``."""

    if length < 1:
        raise ValueError("length must be positive")
    if abs(lag) >= length:
        return 0
    return length - abs(lag)


def repeated_lag_weight(length: int, coefficient: float, lag: int) -> float:
    """Autocorrelation weight at one AP lag for constant coefficients."""

    return repeated_lag_pair_count(length, lag) * coefficient * coefficient


def admissible_unit_resonance_multiplicity(depth: float) -> float:
    """Largest multiplicity allowed by ``mu*depth^2 <= depth``.

    This is the repeated-lag threshold for constant critical coefficients
    when the translated characteristic value can have unit size.
    """

    if not 0.0 < depth <= 1.0:
        raise ValueError("depth must lie in (0,1]")
    return 1.0 / depth


def admissible_resonance_multiplicity(depth: float, translated_size: float) -> float:
    """Threshold from ``mu*depth^2*translated_size <= depth``."""

    if not 0.0 < depth <= 1.0 or not 0.0 < translated_size <= 1.0:
        raise ValueError("depth and translated_size must lie in (0,1]")
    return 1.0 / (depth * translated_size)


def distinct_cell_correction_exponent(
    c: float = 0.019, aperture: float = 50.0 / 33.0
) -> float:
    """Exponent of ``C_Y R^2`` in the GM distinct-cell square sum.

    The top-aperture part dominates ``C_Y`` here, so the exponent is
    ``aperture - 8/5 + 4c``.  Negativity makes the correction
    ``sqrt(C_Y R^2)`` subpower.
    """

    if c <= 0.0 or aperture <= 0.0:
        raise ValueError("c and aperture must be positive")
    return aperture - 8.0 / 5.0 + 4.0 * c


def fejer_required_lag_magnitude(length: int, normalization_cap: float) -> float:
    """Lag floor forced by the stable critical-AP Fejer argument.

    For ``M=floor(sqrt(length)/8)``, Proposition 4.1 gives
    ``max_{1<=k<M}|Phi(kd)| + 1/M >= 1/(pi^2(K+3))``.
    The returned value is the resulting lower bound for the maximum.
    """

    if length < 256:
        raise ValueError("length must be at least 256")
    if normalization_cap <= 0.0:
        raise ValueError("normalization_cap must be positive")
    order = math.floor(math.sqrt(length) / 8.0)
    return max(
        0.0,
        1.0 / (math.pi * math.pi * (normalization_cap + 3.0)) - 1.0 / order,
    )


def critical_ap_energy_exponents(depth_exponent: float) -> dict[str, float]:
    """Show saturation of the classical large-value energy term.

    At depth ``delta=Y^-d`` the critical length is ``L=Y^(2d)``.
    Both ``L^3`` and the second Heath-Brown/GM energy term
    ``L^2 Y^(2d)`` have exponent ``6d``.
    """

    if depth_exponent <= 0.0:
        raise ValueError("depth_exponent must be positive")
    return {
        "critical_length": 2.0 * depth_exponent,
        "ap_energy": 6.0 * depth_exponent,
        "large_value_second_term": 6.0 * depth_exponent,
        "first_term": 8.0 * depth_exponent - 1.0,
    }
