"""Exact actual-prime ledgers for the neighbourhood-degree-sum gate.

This module does *not* assert the open sharp NDS estimate.  It records the
lossless four-completion formulation, the determinant-label injection, the
precise scope of the ``D**2 < q`` approximate-gcd observation, and one
literal all-prime residual double star.

For a fixed ordered colour pair ``gamma=(c,C)``, a two-step chain is

    gamma --(row a)-- p=(b,B) --(row x)-- gamma'=(d,E).

All four displayed triples lie in the hard product window.  Pair uniqueness
therefore makes a chain equivalent to a pair of row labels ``(a,x)`` which
passes four deterministic completion tests.  The two determinants

    delta = b*c-B*C,       ell = C*d-c*E

label the chain injectively on the project shell.  This gives an elementary
``O(D**2)`` ceiling.  The desired NDS theorem is the genuinely stronger
statement that only ``O(D*q**o(1))`` determinant cells are occupied.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, gcd, isqrt
from typing import Iterable, Mapping, Sequence


Pair = tuple[int, int]
Triple = tuple[int, int, int]


def exact_balanced_degree(q: int) -> int:
    """Return ``floor(q**(16/33))`` using integer comparisons only."""

    if q <= 1:
        raise ValueError("q must exceed one")
    target = q**16
    lower, upper = 0, 1
    while upper**33 <= target:
        upper *= 2
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle**33 <= target:
            lower = middle
        else:
            upper = middle
    return lower


def in_hard_window(q: int, D: int, triple: Triple) -> bool:
    """Test the literal inequality ``|8abc-q^3| <= qD``."""

    a, b, c = triple
    return abs(8 * a * b * c - q**3) <= q * D


def _is_prime(value: int) -> bool:
    """Small deterministic primality check used only by the fixed fixture."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def hard_completion(
    q: int, D: int, values: Iterable[int], first: int, second: int
) -> int | None:
    """Return the unique actual node completing one hard-window pair.

    The function checks uniqueness instead of assuming it.  In the project
    range the interval in the missing variable has length ``O(D/q)<1``.
    """

    allowed = set(int(value) for value in values)
    denominator = 8 * first * second
    quotient = q**3 // denominator
    selected = tuple(
        candidate
        for candidate in {quotient, quotient + 1}
        if candidate in allowed
        and abs(denominator * candidate - q**3) <= q * D
    )
    if len(selected) > 1:
        raise ValueError("the hard window has two completions")
    return selected[0] if selected else None


@dataclass(frozen=True)
class FourCompletionChain:
    """One exact two-step chain based at a fixed colour pair."""

    base_colors: Pair
    base_row: int
    centers: Pair
    next_row: int
    next_colors: Pair
    base_determinant: int
    endpoint_determinant: int


def four_completion_chains(
    q: int,
    D: int,
    values: Sequence[int],
    gamma: Pair,
    *,
    residual_only: bool = True,
) -> tuple[FourCompletionChain, ...]:
    """Enumerate NDS chains via the exact four-completion formulation.

    For each ``(a,x)`` the four calls are

    ``b=comp(a,c), B=comp(a,C), d=comp(x,b), E=comp(x,B)``.

    There is no convolutional relaxation or copy of a coefficient mask.
    """

    nodes = tuple(int(value) for value in values)
    c, other_c = gamma
    answer: list[FourCompletionChain] = []
    for a in nodes:
        b = hard_completion(q, D, nodes, a, c)
        other_b = hard_completion(q, D, nodes, a, other_c)
        if b is None or other_b is None:
            continue
        delta = b * c - other_b * other_c
        if residual_only and delta == 0:
            continue
        for x in nodes:
            d = hard_completion(q, D, nodes, x, b)
            other_d = hard_completion(q, D, nodes, x, other_b)
            if d is None or other_d is None:
                continue
            next_delta = b * d - other_b * other_d
            if residual_only and next_delta == 0:
                continue
            ell = other_c * d - c * other_d
            answer.append(
                FourCompletionChain(
                    base_colors=gamma,
                    base_row=a,
                    centers=(b, other_b),
                    next_row=x,
                    next_colors=(d, other_d),
                    base_determinant=delta,
                    endpoint_determinant=ell,
                )
            )
    return tuple(answer)


def residual_transition_support(
    q: int, D: int, values: Sequence[int]
) -> frozenset[tuple[Pair, Pair]]:
    """Build the residual transition support on one finite node set."""

    nodes = tuple(int(value) for value in values)
    by_row: dict[int, list[Pair]] = {}
    for row in nodes:
        entries: list[Pair] = []
        for center in nodes:
            color = hard_completion(q, D, nodes, row, center)
            if color is not None:
                entries.append((center, color))
        by_row[row] = entries
    support: set[tuple[Pair, Pair]] = set()
    for entries in by_row.values():
        for b, c in entries:
            for other_b, other_c in entries:
                if b * c != other_b * other_c:
                    support.add(((b, other_b), (c, other_c)))
    return frozenset(support)


def determinant_label_map(
    chains: Iterable[FourCompletionChain],
) -> dict[tuple[int, int], FourCompletionChain]:
    """Certify that ``(delta,ell)`` labels the supplied chains injectively."""

    labels: dict[tuple[int, int], FourCompletionChain] = {}
    for chain in chains:
        key = (chain.base_determinant, chain.endpoint_determinant)
        previous = labels.get(key)
        if previous is not None and previous != chain:
            raise ValueError("two distinct chains occupy one determinant cell")
        labels[key] = chain
    return labels


def same_determinant_step(
    gamma: Pair, first_centers: Pair, second_centers: Pair
) -> int:
    """Return the exact Farey step between equal-determinant centre pairs.

    If ``b*c-B*C=b'*c-B'*C`` and ``gcd(c,C)=1``, then

    ``(b-b',B-B')=t*(C,c)``.

    On a shell of diameter smaller than ``min(c,C)``, this forces ``t=0``.
    """

    c, other_c = gamma
    b, other_b = first_centers
    next_b, next_other_b = second_centers
    if gcd(c, other_c) != 1:
        raise ValueError("the endpoint pair must be primitive")
    if b * c - other_b * other_c != next_b * c - next_other_b * other_c:
        raise ValueError("the determinants are different")
    difference_b = b - next_b
    difference_other = other_b - next_other_b
    if difference_b % other_c or difference_other % c:
        raise AssertionError("primitive determinant step failed")
    step = difference_b // other_c
    if difference_other != step * c:
        raise AssertionError("the two Farey steps disagree")
    return step


@dataclass(frozen=True)
class ErrorDivisorLedger:
    """The exact approximate-gcd identity for one arm of an NDS chain."""

    first_error: int
    second_error: int
    endpoint_determinant: int
    linear_error: int
    factored_linear_error: int


def error_divisor_ledger(
    base_row: int,
    next_row: int,
    base_colors: Pair,
    next_colors: Pair,
) -> ErrorDivisorLedger:
    """Verify ``C*(xd-ac)-c*(xE-aC)=x*(Cd-cE)`` exactly."""

    a, x = base_row, next_row
    c, other_c = base_colors
    d, other_d = next_colors
    first_error = x * d - a * c
    second_error = x * other_d - a * other_c
    ell = other_c * d - c * other_d
    linear = other_c * first_error - c * second_error
    factored = x * ell
    if linear != factored:
        raise AssertionError("the approximate-gcd identity failed")
    return ErrorDivisorLedger(
        first_error=first_error,
        second_error=second_error,
        endpoint_determinant=ell,
        linear_error=linear,
        factored_linear_error=factored,
    )


def error_pair_step(
    base_colors: Pair, first_errors: Pair, second_errors: Pair
) -> int:
    """Certify injectivity of ``(r,s) -> C*r-c*s`` in a short box."""

    c, other_c = base_colors
    if gcd(c, other_c) != 1:
        raise ValueError("the endpoint pair must be primitive")
    r, s = first_errors
    next_r, next_s = second_errors
    if other_c * r - c * s != other_c * next_r - c * next_s:
        raise ValueError("the linear error labels differ")
    difference_r = r - next_r
    difference_s = s - next_s
    if difference_r % c or difference_s % other_c:
        raise AssertionError("primitive error step failed")
    step = difference_r // c
    if difference_s != step * other_c:
        raise AssertionError("the two error steps disagree")
    return step


@dataclass(frozen=True)
class PrimeResidualEdge:
    """One edge in the literal all-prime double-star fixture."""

    row: int
    centers: Pair
    colors: Pair
    residuals: Pair
    determinant: int


@dataclass(frozen=True)
class PrimeResidualDoubleStar:
    """An all-prime central edge with both residual endpoint degrees >=2."""

    q: int
    D: int
    primes: tuple[int, ...]
    central: PrimeResidualEdge
    same_center_arm: PrimeResidualEdge
    same_color_arm: PrimeResidualEdge
    central_center_degree_lower_bound: int
    central_color_degree_lower_bound: int
    central_nds_lower_bound: int


def _residual_edge(q: int, D: int, row: int, centers: Pair, colors: Pair) -> PrimeResidualEdge:
    triples = ((row, centers[0], colors[0]), (row, centers[1], colors[1]))
    residuals = tuple(8 * a * b * c - q**3 for a, b, c in triples)
    if any(abs(residual) > q * D for residual in residuals):
        raise AssertionError("the proposed edge left the hard window")
    determinant = centers[0] * colors[0] - centers[1] * colors[1]
    if determinant == 0:
        raise AssertionError("the proposed edge is tangent")
    return PrimeResidualEdge(
        row=row,
        centers=centers,
        colors=colors,
        residuals=(residuals[0], residuals[1]),
        determinant=determinant,
    )


def actual_prime_residual_double_star() -> PrimeResidualDoubleStar:
    """Return a literal all-prime residual double star at the critical scale.

    Put ``m=2,934,091`` and ``q=2m``.  The seven numbers

    ``m+u, u in {-24,-18,-12,0,6,12,18}``

    are prime.  Three residual edges share one central edge in the two
    possible directions.  Across either arm, neither semiprime leg is an
    exact equality or a swapped factorisation.  Thus actual prime support
    does not make every residual degree one, although this fixture is far
    below (and fully consistent with) the conjectural NDS bound.
    """

    m = 2_934_091
    q = 2 * m
    D = exact_balanced_degree(q)
    offsets = (-24, -18, -12, 0, 6, 12, 18)
    primes = tuple(m + offset for offset in offsets)
    if not all(_is_prime(value) for value in primes):
        raise AssertionError("the fixed affine nodes are not all prime")
    lower = (q / 2.0) * exp(-0.2)
    upper = (q / 2.0) * exp(0.2)
    if not all(lower <= value <= upper for value in primes):
        raise AssertionError("a fixed prime left the project shell")

    center_pair = (m, m + 6)
    color_pair = (m + 18, m + 12)
    next_color_pair = (m + 12, m + 6)
    next_center_pair = (m + 6, m + 12)
    central = _residual_edge(q, D, m - 18, center_pair, color_pair)
    same_center = _residual_edge(q, D, m - 12, center_pair, next_color_pair)
    same_color = _residual_edge(q, D, m - 24, next_center_pair, color_pair)

    # Rule out the easy exact-product/swapped explanation on both arms.
    for coordinate in (0, 1):
        base_factors = {central.row, central.colors[coordinate]}
        next_factors = {same_center.row, same_center.colors[coordinate]}
        if base_factors & next_factors:
            raise AssertionError("the same-centre arm has a repeated semiprime factor")
        base_factors = {central.row, central.centers[coordinate]}
        next_factors = {same_color.row, same_color.centers[coordinate]}
        if base_factors & next_factors:
            raise AssertionError("the same-colour arm has a repeated semiprime factor")

    support = residual_transition_support(q, D, primes)
    if (center_pair, color_pair) not in support:
        raise AssertionError("the central transition disappeared")
    left_degrees: dict[Pair, int] = {}
    right_degrees: dict[Pair, int] = {}
    for centers, colors in support:
        left_degrees[centers] = left_degrees.get(centers, 0) + 1
        right_degrees[colors] = right_degrees.get(colors, 0) + 1
    nds = neighbourhood_degree_sums(support)
    if left_degrees[center_pair] != 4 or right_degrees[color_pair] != 4:
        raise AssertionError("unexpected central degree in the prime fixture")
    if nds[color_pair] != 14:
        raise AssertionError("unexpected NDS value in the prime fixture")

    return PrimeResidualDoubleStar(
        q=q,
        D=D,
        primes=primes,
        central=central,
        same_center_arm=same_center,
        same_color_arm=same_color,
        central_center_degree_lower_bound=left_degrees[center_pair],
        central_color_degree_lower_bound=right_degrees[color_pair],
        central_nds_lower_bound=nds[color_pair],
    )


def neighbourhood_degree_sums(
    edges: Iterable[tuple[Pair, Pair]],
) -> dict[Pair, int]:
    """Return ``W(gamma)=sum_(p~gamma) deg(p)`` for a bipartite support."""

    support = set(edges)
    left_degrees: dict[Pair, int] = {}
    for center, _ in support:
        left_degrees[center] = left_degrees.get(center, 0) + 1
    answer: dict[Pair, int] = {}
    for center, color in support:
        answer[color] = answer.get(color, 0) + left_degrees[center]
    return answer
