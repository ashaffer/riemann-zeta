"""Fail-fast probes for the R99 prime-log moment and alias gates.

The positive difference measure

    dnu_r(x) = x**r exp(-delta*x) (1-exp(-gap*x)) dx

has support down to zero, whereas every prime-power logarithm is at least
``log(2)``.  Its truncated multiplication-by-x Rayleigh quotient therefore
detects a support mismatch.  This module computes that quotient at high
precision, builds the corresponding polynomial separator, and evaluates the
bounded infinite-order arithmetic alias

    cos(2*pi*exp(x)) - 1.

The routines are diagnostics.  The mathematical certificate is the exact
moment identity and the generalized eigenvalue inequality, not floating-point
output by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse

import mpmath as mp


with mp.workdps(100):
    LOG_TWO = +mp.log(2)


def _positive(value: object, name: str) -> mp.mpf:
    result = mp.mpf(value)
    if not mp.isfinite(result) or result <= 0:
        raise ValueError(f"{name} must be finite and positive")
    return result


def _nonnegative_integer(value: object, name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a nonnegative integer")
    result = int(value)
    if result != value or result < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return result


def difference_moment(
    delta: object,
    gap: object,
    power: object,
    *,
    vanishing_order: object = 0,
) -> mp.mpf:
    """Return an exact closed form for a difference-measure moment.

    The returned value is

        integral x**(power+vanishing_order)
                 exp(-delta*x) (1-exp(-gap*x)) dx.
    """

    delta_mp = _positive(delta, "delta")
    gap_mp = _positive(gap, "gap")
    power_i = _nonnegative_integer(power, "power")
    order_i = _nonnegative_integer(vanishing_order, "vanishing_order")
    total = power_i + order_i
    return mp.factorial(total) * (
        delta_mp ** (-(total + 1))
        - (delta_mp + gap_mp) ** (-(total + 1))
    )


def normalized_first_moment(
    delta: object,
    gap: object,
    *,
    vanishing_order: object = 0,
) -> mp.mpf:
    """Mean of x for the requested difference measure."""

    mass = difference_moment(
        delta, gap, 0, vanishing_order=vanishing_order
    )
    return (
        difference_moment(delta, gap, 1, vanishing_order=vanishing_order)
        / mass
    )


@dataclass(frozen=True)
class LocalizerCertificate:
    """Smallest truncated multiplication eigenpair."""

    rayleigh: mp.mpf
    coefficients: tuple[mp.mpf, ...]
    vanishing_order: int
    polynomial_degree: int


def smallest_localizing_rayleigh(
    delta: object,
    gap: object,
    polynomial_degree: object,
    *,
    vanishing_order: object = 1,
    dps: int = 80,
) -> LocalizerCertificate:
    """Minimize ``int x*q^2 dnu / int q^2 dnu`` over ``deg(q)<=n``.

    The moment matrices are formed in the monomial basis and solved after a
    high-precision Cholesky whitening.  The returned coefficients are ordered
    from the constant coefficient upward.
    """

    degree_i = _nonnegative_integer(polynomial_degree, "polynomial_degree")
    order_i = _nonnegative_integer(vanishing_order, "vanishing_order")
    if dps < 30:
        raise ValueError("dps must be at least 30")

    with mp.workdps(dps):
        delta_mp = _positive(delta, "delta")
        gap_mp = _positive(gap, "gap")
        moments = [
            difference_moment(
                delta_mp,
                gap_mp,
                k,
                vanishing_order=order_i,
            )
            for k in range(2 * degree_i + 2)
        ]
        size = degree_i + 1
        gram = mp.matrix(size)
        shifted = mp.matrix(size)
        for row in range(size):
            for column in range(size):
                gram[row, column] = moments[row + column]
                shifted[row, column] = moments[row + column + 1]

        lower = mp.cholesky(gram)
        lower_inverse = lower**-1
        whitened = lower_inverse * shifted * lower_inverse.T
        eigenvalues, eigenvectors = mp.eigsy(whitened)
        whitened_vector = eigenvectors[:, 0]
        coefficient_vector = lower_inverse.T * whitened_vector

        # Copy values out of the work-precision context.
        rayleigh = +eigenvalues[0]
        coefficients = tuple(+coefficient_vector[index] for index in range(size))

    return LocalizerCertificate(
        rayleigh=rayleigh,
        coefficients=coefficients,
        vanishing_order=order_i,
        polynomial_degree=degree_i,
    )


def laguerre_comparison_bound(
    delta: object,
    polynomial_degree: object,
    *,
    vanishing_order: object = 1,
) -> mp.mpf:
    """Upper bound for the comparison-gamma Rayleigh quotient.

    For ``alpha=vanishing_order+1``, the exact gamma quotient is the smallest
    zero of ``L_(n+1)^alpha(delta*x)``.  The classical explicit estimate

        x_min < (alpha+1)(alpha+2)/(n+alpha+2)

    gives the returned bound after scaling by ``delta``.
    """

    delta_mp = _positive(delta, "delta")
    degree_i = _nonnegative_integer(polynomial_degree, "polynomial_degree")
    order_i = _nonnegative_integer(vanishing_order, "vanishing_order")
    return mp.mpf((order_i + 2) * (order_i + 3)) / (
        delta_mp * (degree_i + order_i + 3)
    )


def difference_localizer_bound(
    delta: object,
    gap: object,
    polynomial_degree: object,
    *,
    vanishing_order: object = 1,
) -> mp.mpf:
    """Comparison upper bound for the actual difference-measure quotient.

    We compare against ``gap*x**(r+1)*exp(-delta*x) dx`` on
    ``[0, 1/gap]``.  ``+inf`` is returned when the chosen comparison quotient
    is too large for that truncation argument.
    """

    gap_mp = _positive(gap, "gap")
    gamma_bound = laguerre_comparison_bound(
        delta,
        polynomial_degree,
        vanishing_order=vanishing_order,
    )
    cutoff = 1 / gap_mp
    if gamma_bound >= cutoff:
        return mp.inf
    comparison_floor = 1 - mp.e**-1
    return gamma_bound / (
        comparison_floor * (1 - gamma_bound / cutoff)
    )


def separator_coefficients(
    certificate: LocalizerCertificate,
    *,
    support_floor: object = LOG_TWO,
) -> tuple[mp.mpf, ...]:
    """Return coefficients of ``x^r (x-a) q(x)^2`` in ascending order."""

    floor_mp = _positive(support_floor, "support_floor")
    q = certificate.coefficients
    square = [mp.mpf("0") for _ in range(2 * len(q) - 1)]
    for left, left_value in enumerate(q):
        for right, right_value in enumerate(q):
            square[left + right] += left_value * right_value

    order = certificate.vanishing_order
    result = [mp.mpf("0") for _ in range(order + len(square) + 1)]
    for index, value in enumerate(square):
        result[order + index] -= floor_mp * value
        result[order + index + 1] += value
    return tuple(result)


def evaluate_polynomial(coefficients: tuple[mp.mpf, ...], x: object) -> mp.mpf:
    """Evaluate ascending-order coefficients by Horner's rule."""

    x_mp = mp.mpf(x)
    value = mp.mpf("0")
    for coefficient in reversed(coefficients):
        value = value * x_mp + coefficient
    return value


def laplace_polynomial(
    coefficients: tuple[mp.mpf, ...], rate: object
) -> mp.mpc:
    """Laplace transform of a polynomial on ``[0, infinity)``."""

    rate_mp = mp.mpc(rate)
    if mp.re(rate_mp) <= 0:
        raise ValueError("rate must have positive real part")
    return sum(
        coefficient * mp.factorial(power) / rate_mp ** (power + 1)
        for power, coefficient in enumerate(coefficients)
    )


def cubic_gap_coefficients(
    lower_root: object,
    upper_root: object,
) -> tuple[mp.mpf, ...]:
    """Coefficients of ``x(x-b)(x-c)`` for ``0<b<c<log(2)``."""

    lower = _positive(lower_root, "lower_root")
    upper = _positive(upper_root, "upper_root")
    if not lower < upper < LOG_TWO:
        raise ValueError("roots must satisfy 0 < lower < upper < log(2)")
    return (mp.mpf("0"), lower * upper, -(lower + upper), mp.mpf("1"))


def alias_weight(x: object) -> mp.mpf:
    """The bounded arithmetic-null alias ``cos(2*pi*exp(x))-1``."""

    return mp.cos(2 * mp.pi * mp.exp(mp.mpf(x))) - 1


def alias_laplace(rate: object) -> mp.mpc:
    """Laplace transform of the arithmetic-null alias for ``Re(rate)>0``.

    Substitution ``u=exp(x)`` writes the oscillatory part in terms of the
    generalized exponential integral ``E_p`` and avoids numerical tail
    quadrature.
    """

    rate_mp = mp.mpc(rate)
    if mp.re(rate_mp) <= 0:
        raise ValueError("rate must have positive real part")
    frequency = 2 * mp.pi
    oscillatory = (
        mp.expint(rate_mp + 1, -1j * frequency)
        + mp.expint(rate_mp + 1, 1j * frequency)
    ) / 2
    return oscillatory - 1 / rate_mp


def stationary_phase_envelope(real_part: object, height: object) -> mp.mpf:
    """Leading magnitude from the positive-frequency stationary point."""

    sigma = _positive(real_part, "real_part")
    height_mp = _positive(height, "height")
    return mp.mpf("0.5") * (height_mp / (2 * mp.pi)) ** (
        -sigma - mp.mpf("0.5")
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--delta", type=float, default=1.0)
    parser.add_argument("--gap", type=float, default=1.0)
    parser.add_argument("--max-degree", type=int, default=8)
    parser.add_argument("--order", type=int, default=1)
    args = parser.parse_args()

    print(
        "degree rayleigh comparison_bound below_log2",
    )
    for degree in range(args.max_degree + 1):
        certificate = smallest_localizing_rayleigh(
            args.delta,
            args.gap,
            degree,
            vanishing_order=args.order,
        )
        bound = difference_localizer_bound(
            args.delta,
            args.gap,
            degree,
            vanishing_order=args.order,
        )
        print(
            degree,
            mp.nstr(certificate.rayleigh, 12),
            mp.nstr(bound, 12),
            certificate.rayleigh < LOG_TWO,
        )

    for sigma in (mp.mpf("0.25"), mp.mpf("2")):
        height = mp.mpf("100")
        observed = abs(alias_laplace(sigma + 1j * height))
        predicted = stationary_phase_envelope(sigma, height)
        print(
            "alias",
            mp.nstr(sigma, 4),
            mp.nstr(observed, 12),
            mp.nstr(predicted, 12),
            mp.nstr(observed / predicted, 8),
        )


if __name__ == "__main__":
    main()
