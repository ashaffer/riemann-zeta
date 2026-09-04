"""Exact residual algebra for the balanced QP four-cycle gate.

The routines in this module are finite identity checks.  They isolate the
zero color-determinant sector and the short shift parametrization which
remains when the determinant is nonzero.  They do *not* prove the requested
four-cycle estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class ResidualCycleLedger:
    """Exact invariants of one ordered four-cycle.

    Rows, columns, and colors use the order

    ``(11, 12, 21, 22)``.
    """

    q: int
    residuals: tuple[int, int, int, int]
    color_determinant: int
    alternating_sum: int
    alternating_product: int
    carrier_product: int
    row_shifts: tuple[int, int]
    column_shifts: tuple[int, int]

    @property
    def modulus(self) -> int:
        return self.q**3

    @property
    def bilinear_level(self) -> int:
        if self.alternating_sum % 8:
            raise ArithmeticError("the alternating residual sum must be divisible by 8")
        return self.alternating_sum // 8


@dataclass(frozen=True)
class CrossConicLedger:
    """The fixed diagonal-color/cross-product conic invariants."""

    diagonal_products: tuple[int, int]
    cross_color_product: int
    cross_triple_products: tuple[int, int]
    cross_difference: int


def residual(q: int, a: int, b: int, c: int) -> int:
    """Return the exact carry residual ``8abc-q^3``."""

    return 8 * a * b * c - q**3


def cycle_ledger(
    q: int,
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> ResidualCycleLedger:
    """Build all exact residual, determinant, and shift invariants."""

    a1, a2 = rows
    b1, b2 = columns
    (c11, c12), (c21, c22) = colors
    r11 = residual(q, a1, b1, c11)
    r12 = residual(q, a1, b2, c12)
    r21 = residual(q, a2, b1, c21)
    r22 = residual(q, a2, b2, c22)
    residuals = (r11, r12, r21, r22)
    alternating_sum = r11 + r22 - r12 - r21
    alternating_product = r11 * r22 - r12 * r21
    return ResidualCycleLedger(
        q=q,
        residuals=residuals,
        color_determinant=c11 * c22 - c12 * c21,
        alternating_sum=alternating_sum,
        alternating_product=alternating_product,
        carrier_product=a1 * a2 * b1 * b2,
        row_shifts=(b1 * c11 - b2 * c12, b1 * c21 - b2 * c22),
        column_shifts=(a1 * c11 - a2 * c21, a1 * c12 - a2 * c22),
    )


def determinant_identity_sides(ledger: ResidualCycleLedger) -> tuple[int, int]:
    """Return the two sides of ``Q S+T=64 k a1 a2 b1 b2``."""

    left = ledger.modulus * ledger.alternating_sum + ledger.alternating_product
    right = 64 * ledger.color_determinant * ledger.carrier_product
    return left, right


def cross_product_identity_sides(
    ledger: ResidualCycleLedger,
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[int, int]:
    """Return the two sides of the exact color/residual cross identity."""

    (_, c12), (c21, _) = colors
    _, r12, r21, _ = ledger.residuals
    off_color_product = c12 * c21
    left = off_color_product * (
        ledger.modulus * ledger.alternating_sum + ledger.alternating_product
    )
    right = ledger.color_determinant * (ledger.modulus + r12) * (
        ledger.modulus + r21
    )
    return left, right


def shift_identity_sides(
    ledger: ResidualCycleLedger,
    rows: tuple[int, int],
    columns: tuple[int, int],
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Return all four residual-difference/short-shift identity pairs."""

    a1, a2 = rows
    b1, b2 = columns
    r11, r12, r21, r22 = ledger.residuals
    u1, u2 = ledger.row_shifts
    v1, v2 = ledger.column_shifts
    return (
        (r11 - r12, 8 * a1 * u1),
        (r21 - r22, 8 * a2 * u2),
        (r11 - r21, 8 * b1 * v1),
        (r12 - r22, 8 * b2 * v2),
    )


def shift_factorization_sides(
    ledger: ResidualCycleLedger,
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the two exact small-shift carrier factorizations.

    With ``L=S/8`` and ``k=det(c_ij)``, these are

    ``v1*u1=c11*L-k*a2*b2`` and
    ``v2*u2=c22*L-k*a1*b1``.
    """

    a1, a2 = rows
    b1, b2 = columns
    (c11, _), (_, c22) = colors
    u1, u2 = ledger.row_shifts
    v1, v2 = ledger.column_shifts
    level = ledger.bilinear_level
    determinant = ledger.color_determinant
    return (
        (v1 * u1, c11 * level - determinant * a2 * b2),
        (v2 * u2, c22 * level - determinant * a1 * b1),
    )


def cross_conic_ledger(
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> CrossConicLedger:
    """Build ``s,t,n,X,Y,w`` for the cross-product conic."""

    a1, a2 = rows
    b1, b2 = columns
    (_, c12), (c21, _) = colors
    first = c12 * a1 * b2
    second = c21 * a2 * b1
    return CrossConicLedger(
        diagonal_products=(a1 * b1, a2 * b2),
        cross_color_product=c12 * c21,
        cross_triple_products=(first, second),
        cross_difference=first - second,
    )


def cross_conic_identity_sides(
    conic: CrossConicLedger,
    colors: tuple[tuple[int, int], tuple[int, int]],
    bilinear_level: int,
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Return sum, product, and discriminant identities of the cross conic."""

    (c11, _), (_, c22) = colors
    s, t = conic.diagonal_products
    first, second = conic.cross_triple_products
    center_sum = c11 * s + c22 * t - bilinear_level
    return (
        (first + second, center_sum),
        (first * second, conic.cross_color_product * s * t),
        (
            conic.cross_difference**2,
            center_sum**2 - 4 * conic.cross_color_product * s * t,
        ),
    )


def cross_conic_factorization_sides(
    c11: int,
    c22: int,
    cross_color_product: int,
    diagonal_product_s: int,
    diagonal_product_t: int,
    bilinear_level: int,
    cross_difference: int,
) -> tuple[int, int]:
    """Factor the conic, viewed as a quadratic in ``t``.

    If ``w^2=(c*s+d*t-L)^2-4*n*s*t`` and

    ``B=2*d*(c*s-L)-4*n*s``, then

    ``(2d^2t+B-2dw)(2d^2t+B+2dw)``

    equals ``16*n*s*(n*s-d*(c*s-L))``.
    """

    c = c11
    d = c22
    n = cross_color_product
    s = diagonal_product_s
    t = diagonal_product_t
    level = bilinear_level
    w = cross_difference
    linear = 2 * d * (c * s - level) - 4 * n * s
    left = (2 * d * d * t + linear - 2 * d * w) * (
        2 * d * d * t + linear + 2 * d * w
    )
    right = 16 * n * s * (n * s - d * (c * s - level))
    return left, right


def tangent_modes(ledger: ResidualCycleLedger) -> tuple[str, ...]:
    """Classify the exact conic tangent ``v2*u2=0``.

    ``column_swap`` means ``v2=0`` (the second-column residuals agree), and
    ``row_swap`` means ``u2=0`` (the second-row residuals agree).  An empty
    tuple is the generic conic sector.
    """

    _, u2 = ledger.row_shifts
    _, v2 = ledger.column_shifts
    answers: list[str] = []
    if v2 == 0:
        answers.append("column_swap")
    if u2 == 0:
        answers.append("row_swap")
    return tuple(answers)


def tangent_identity_sides(
    ledger: ResidualCycleLedger,
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[int, int]:
    """Return ``v2*u2`` and ``c22*L-k*a1*b1``."""

    a1, _ = rows
    b1, _ = columns
    (_, _), (_, c22) = colors
    _, u2 = ledger.row_shifts
    _, v2 = ledger.column_shifts
    return (
        v2 * u2,
        c22 * ledger.bilinear_level - ledger.color_determinant * a1 * b1,
    )


def residual_sum_pinning_error(
    ledger: ResidualCycleLedger,
    colors: tuple[tuple[int, int], tuple[int, int]],
) -> float:
    """Return ``S-kQ/(c12*c21)`` from the exact cross identity."""

    (_, c12), (c21, _) = colors
    return ledger.alternating_sum - (
        ledger.color_determinant * ledger.modulus / (c12 * c21)
    )


def residual_sum_pinning_bound(
    residual_cap: int,
    determinant_abs: int,
    modulus: int,
    off_color_product: int,
) -> float:
    """Elementary upper bound for ``|S-kQ/(c12*c21)|``.

    It follows by expanding the exact cross-product identity and using
    ``|r_ij|<=residual_cap``.
    """

    if residual_cap < 0 or determinant_abs < 0:
        raise ValueError("caps must be nonnegative")
    if modulus <= 0 or off_color_product <= 0:
        raise ValueError("modulus and color product must be positive")
    return (
        2 * determinant_abs * residual_cap / off_color_product
        + determinant_abs * residual_cap**2 / (off_color_product * modulus)
        + 2 * residual_cap**2 / modulus
    )


def short_product_pairing(
    modulus: int,
    residuals: tuple[int, int, int, int],
) -> tuple[str, ...]:
    """Classify a zero-cross-ratio residual quadruple in a short interval.

    The input order is ``(r11,r12,r21,r22)``.  If

    ``(Q+r11)(Q+r22)=(Q+r12)(Q+r21)``

    and ``2*max(|r|)^2<Q``, equality of the sums and products forces one of
    the row or column pairings.  The returned tuple lists the valid pairings.
    """

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    r11, r12, r21, r22 = residuals
    cap = max(abs(value) for value in residuals)
    if 2 * cap * cap >= modulus:
        raise ValueError("the residual interval is not shorter than sqrt(Q/2)")
    if (modulus + r11) * (modulus + r22) != (modulus + r12) * (
        modulus + r21
    ):
        raise ValueError("the cross products are not equal")
    answers: list[str] = []
    if r11 == r12 and r22 == r21:
        answers.append("rows")
    if r11 == r21 and r22 == r12:
        answers.append("columns")
    if not answers:
        raise ArithmeticError("short product equality failed to pair")
    return tuple(answers)


def prime_power_base(value: int) -> int | None:
    """Return the prime base when ``value`` is a prime power, else ``None``."""

    if value < 2:
        return None
    candidate = value
    base = None
    divisor = 2
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            base = divisor
            while candidate % divisor == 0:
                candidate //= divisor
            break
        divisor = 3 if divisor == 2 else divisor + 2
    if base is None:
        return value
    if candidate != 1:
        return None
    # The first divisor found is prime.  Removing it completely left one,
    # hence the original value is a power of that prime.
    return base


def is_pairwise_coprime_prime_power_shell(values: Sequence[int]) -> bool:
    """Check the multiplicative-Sidon input used by the zero-mode proof."""

    bases: set[int] = set()
    for value in values:
        base = prime_power_base(value)
        if base is None or base in bases:
            return False
        bases.add(base)
    return True


def zero_determinant_nondegenerate_impossible(
    q: int,
    rows: tuple[int, int],
    columns: tuple[int, int],
    colors: tuple[tuple[int, int], tuple[int, int]],
    residual_cap: int,
) -> bool:
    """Certify the actual-shell zero-determinant exclusion for one cycle.

    This finite checker enforces the hypotheses used in the proof:

    * every displayed node is a prime power and distinct values have distinct
      prime bases;
    * ``2H^2<q^3`` and ``2H<8m^2``;
    * all four residuals have magnitude at most ``H``;
    * the two row and two column indices are distinct.

    It returns ``True`` exactly when these hypotheses make determinant zero
    impossible.  A nonzero determinant is not an error and returns ``False``.
    """

    a1, a2 = rows
    b1, b2 = columns
    flat_colors = (colors[0][0], colors[0][1], colors[1][0], colors[1][1])
    nodes = tuple(dict.fromkeys((*rows, *columns, *flat_colors)))
    if not is_pairwise_coprime_prime_power_shell(nodes):
        raise ValueError("nodes are not a pairwise-coprime prime-power shell")
    if a1 == a2 or b1 == b2:
        raise ValueError("the rectangle is degenerate")
    minimum = min(nodes)
    if 2 * residual_cap**2 >= q**3 or 2 * residual_cap >= 8 * minimum**2:
        raise ValueError("the residual cap is too large for the rigidity lemma")
    ledger = cycle_ledger(q, rows, columns, colors)
    if max(abs(value) for value in ledger.residuals) > residual_cap:
        raise ValueError("a residual lies outside the stated cap")
    if ledger.color_determinant != 0:
        return False
    # If determinant zero really occurred, the short-product lemma gives a
    # row or column pairing.  Multiplicative Sidonicity swaps the two factors,
    # and the second cap inequality then forces the corresponding row or
    # column indices to coincide, contrary to nondegeneracy.
    short_product_pairing(q**3, ledger.residuals)
    return True


def divisor_count(value: int) -> int:
    """Return the number of positive divisors of ``value``."""

    if value <= 0:
        raise ValueError("value must be positive")
    answer = 1
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            answer *= exponent + 1
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        answer *= 2
    return answer


def weighted_determinant_layer(
    values: Sequence[int],
    weights: Mapping[int, complex],
    determinant: int,
) -> float:
    """Compute the absolute weighted color layer with fixed determinant."""

    return float(
        sum(
            abs(
                weights.get(c11, 0)
                * weights.get(c12, 0)
                * weights.get(c21, 0)
                * weights.get(c22, 0)
            )
            for c11 in values
            for c12 in values
            for c21 in values
            for c22 in values
            if c11 * c22 - c12 * c21 == determinant
        )
    )


def weighted_determinant_layer_bound(
    values: Sequence[int],
    weights: Mapping[int, complex],
    determinant: int,
) -> float:
    """Divisor-majorant bound for one weighted determinant layer.

    The proof applies ``AB<=(A^2+B^2)/2`` and then fixes either diagonal
    product.  The complementary pair factors one fixed positive integer.
    """

    if not values:
        return 0.0
    maximum_product = max(values) ** 2 + abs(determinant)
    divisor_majorant = max(divisor_count(value) for value in range(1, maximum_product + 1))
    norm_sq = sum(abs(weights.get(value, 0)) ** 2 for value in values)
    return float(divisor_majorant * norm_sq**2)


def active_exponent_ledger() -> dict[str, tuple[int, int]]:
    """Return exact q-exponents at ``D=q^(16/33)``."""

    return {
        "D": (16, 33),
        "D_over_sqrt_q": (-1, 66),
        "D_squared_over_q": (-1, 33),
        "sqrt_D": (8, 33),
    }


def local_shift_degree_bound(residual_cap: int, minimum_node: int) -> int:
    """Number of available integral row/column shifts before carrier saving.

    For two residuals with magnitude at most ``H``, the exact difference
    identity gives a shift of magnitude at most ``H/(4m)``.  In a shell of
    diameter smaller than ``m``, each shift has at most one Diophantine lift.
    This is the proved ``O(D)`` bound; it deliberately contains no unproved
    square-root carrier cancellation.
    """

    if residual_cap < 0 or minimum_node <= 0:
        raise ValueError("invalid residual cap or node minimum")
    radius = residual_cap // (4 * minimum_node)
    return 2 * radius + 1
