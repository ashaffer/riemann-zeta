"""Exponent and arithmetic replay for the QP prime-power multiscale gate."""

from __future__ import annotations

from fractions import Fraction


def layer_count_exponent(k: int) -> float:
    if k < 1:
        raise ValueError("k must be positive")
    return 1.0 / k


def layer_mesh_exponent(k: int) -> float:
    """BHP logarithmic mesh exponent for p^k near Y."""

    if k < 1:
        raise ValueError("k must be positive")
    return 19.0 / (40.0 * k)


def second_order_quadrature_top(k: int, target_c: float) -> float:
    """Largest sigma certified by t^2 h_k^2 <= Y^(-target_c)."""

    if target_c <= 0.0:
        raise ValueError("target_c must be positive")
    return layer_mesh_exponent(k) - target_c / 2.0


def layer_amplification_exponent(k: int, target_c: float) -> float:
    """Per-node amplification needed to give layer k mass Y^(-c).

    Relative to the dominant prime layer, the natural total mass of layer k
    is Y^(1/k-1+o(1)).
    """

    if k < 2:
        raise ValueError("the amplification tax concerns proper powers")
    return 1.0 - 1.0 / k - target_c


def scaled_zero_is_separated(beta: float, k0: int, k: int, multiplier: int = 1) -> bool:
    """Whether a rho/k0 pole lies right of every m*k-scaled zeta zero.

    A singularity of P(k s) inherited from -zeta'/zeta(m k s) at s=rho/k0
    would require a zeta zero with real part ``multiplier*k*beta/k0``.
    Values strictly above one are impossible.
    """

    if not (0.0 < beta < 1.0):
        raise ValueError("beta must lie in (0,1)")
    if k0 < 1 or k <= k0 or multiplier < 1:
        raise ValueError("require 1 <= k0 < k and multiplier >= 1")
    return multiplier * k * beta / k0 > 1.0


def distinct_prime_factors(n: int) -> set[int]:
    if n < 1:
        raise ValueError("n must be positive")
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.add(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.add(n)
    return factors


def prime_power_base(n: int) -> int | None:
    """Return p when n is a positive prime power p^a, otherwise None."""

    if n < 2:
        return None
    factors = distinct_prime_factors(n)
    if len(factors) != 1:
        return None
    return next(iter(factors))


def rational_shift_overlap(nodes: list[int], ratio: Fraction) -> list[tuple[int, int]]:
    """Pairs (n,m) of supplied prime powers with m/n=ratio."""

    if ratio <= 0 or ratio == 1:
        raise ValueError("ratio must be positive and nontrivial")
    node_set = set(nodes)
    pairs: list[tuple[int, int]] = []
    for n in nodes:
        numerator = n * ratio.numerator
        if numerator % ratio.denominator:
            continue
        m = numerator // ratio.denominator
        if m in node_set:
            pairs.append((n, m))
    return pairs


def shift_overlap_factor_bound(ratio: Fraction) -> int:
    """The omega(ab) bound for a reduced rational shift a/b."""

    if ratio <= 0 or ratio == 1:
        raise ValueError("ratio must be positive and nontrivial")
    return len(distinct_prime_factors(ratio.numerator * ratio.denominator))


def target_ledger(target_c: float = 0.019) -> dict[str, float]:
    return {
        "target_c": target_c,
        "prime_quadrature_top": second_order_quadrature_top(1, target_c),
        "square_quadrature_top": second_order_quadrature_top(2, target_c),
        "proper_power_mass": -0.5,
        "square_amplification_tax": layer_amplification_exponent(2, target_c),
        "aperture_top": 50.0 / 33.0,
    }


if __name__ == "__main__":
    print(target_ledger())
