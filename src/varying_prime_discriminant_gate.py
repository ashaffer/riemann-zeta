"""Exact algebra and scale ledgers for the R100 varying-prime gate.

These routines support
``results/R100-VARYING-PRIME-DISCRIMINANT-PARITY-GATE.md``.  They test
integer identities, character grouping, and exponent budgets; they do not
claim a new estimate for zeta zeros.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from math import ceil, floor
from numbers import Number


def trace_value(a: int, h1: int, h2: int, h3: int, h4: int) -> int:
    """The four-step SL2 trace from the Blomer--Pascadi conversion."""

    return (
        a * a * h1 * h2 * h3 * h4
        - a * (h1 + h3) * (h2 + h4)
        + 2
    )


def trace_discriminant(a: int, h1: int, h2: int, h3: int, h4: int) -> int:
    """Return ``Tr(g)^2-4`` exactly."""

    trace = trace_value(a, h1, h2, h3, h4)
    return trace * trace - 4


def trace_offset(a: int, h1: int, h2: int, h3: int, h4: int) -> int:
    """Return F=Tr(g)-2, for which Delta=F(F+4)."""

    return trace_value(a, h1, h2, h3, h4) - 2


def axis_parameter(a: int, h2: int, h3: int, h4: int) -> int:
    """On h1=0, return X=a*h3*(h2+h4)."""

    return a * h3 * (h2 + h4)


def axis_discriminant(a: int, h2: int, h3: int, h4: int) -> int:
    """On h1=0, Delta=X(X-4)."""

    x = axis_parameter(a, h2, h3, h4)
    return x * (x - 4)


def axis_matrix_mod_prime(
    a: int, h2: int, h3: int, h4: int, prime: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    """The four-step matrix on the h1=0 slice, reduced modulo ``prime``."""

    entries = (
        (1 - a * h3 * h4, a * h3),
        (-h2 + h4 * (a * h2 * h3 - 1), 1 - a * h2 * h3),
    )
    return tuple(tuple(value % prime for value in row) for row in entries)  # type: ignore[return-value]


def trace_fiber_factorization(
    a: int, h1: int, h2: int, h3: int, h4: int
) -> tuple[int, int]:
    """Return the two sides of the fixed-(h1,h3) trace-fiber identity.

    With ``u=h1*h3``, ``x=h1+h3``, and ``F=Tr-2``, one has

        (a*u*h2-x)(a*u*h4-x) = u*F+x^2.
    """

    u = h1 * h3
    x = h1 + h3
    offset = trace_offset(a, h1, h2, h3, h4)
    left = (a * u * h2 - x) * (a * u * h4 - x)
    right = u * offset + x * x
    return left, right


def adjacent_continuant_factorization(
    a: int, h1: int, h2: int, h3: int, h4: int
) -> tuple[int, int, int]:
    """Return the adjacent-pair continuant factorization.

    Put ``p=a*h1*h2-1`` and ``T=trace_a(h1,h2,h3,h4)``.  Then

        (p*a*h3-a*h1)(p*h4-h2) = p**2 + T*p + 1.

    For ``a=1`` this is the reciprocal-quadratic continuant equation
    highlighted by Badziahin's factorization framework.  It shows that,
    after fixing the adjacent pair ``(h1,h2)``, every nonparabolic trace
    fiber is a divisor problem.  It does *not* remove the outer set of
    ``H^(2-o(1))`` possible adjacent products.
    """

    p = a * h1 * h2 - 1
    trace = trace_value(a, h1, h2, h3, h4)
    left = (p * a * h3 - a * h1) * (p * h4 - h2)
    right = p * p + trace * p + 1
    return p, left, right


def adjacent_continuant_cross_identity(
    a: int,
    first: tuple[int, int, int, int],
    second: tuple[int, int, int, int],
) -> tuple[int, int]:
    """Return the two sides of the off-diagonal continuant identity.

    The quadruples must have the same trace.  If their adjacent parameters
    are ``p`` and ``q``, and their continuant factors are ``U,V`` and
    ``U',V'``, respectively, then

        q*U*V - p*U'*V' = (p-q)*(p*q-1).

    This is the exact shifted-divisor equation left after the easy
    ``p=q`` energy diagonal has been removed.
    """

    if trace_value(a, *first) != trace_value(a, *second):
        raise ValueError("the two quadruples must have the same trace")

    h1, h2, h3, h4 = first
    p = a * h1 * h2 - 1
    u = p * a * h3 - a * h1
    v = p * h4 - h2

    k1, k2, k3, k4 = second
    q = a * k1 * k2 - 1
    u_prime = q * a * k3 - a * k1
    v_prime = q * k4 - k2

    left = q * u * v - p * u_prime * v_prime
    right = (p - q) * (p * q - 1)
    return left, right


def trace_pair_invariants(
    a: int, h1: int, h3: int
) -> tuple[int, int]:
    """Return the two coordinates used in the trace dot-product model.

    If ``P=(a*h1*h3, -(h1+h3))`` and
    ``Q=(h2*h4, h2+h4)``, then ``Tr(g)-2=a*P dot Q``.
    The unordered pair ``{h1,h3}`` is recovered from its product and sum,
    so this parametrization is at most two-to-one.
    """

    return a * h1 * h3, -(h1 + h3)


def trace_dot_product_offset(
    a: int, h1: int, h2: int, h3: int, h4: int
) -> int:
    """Compute ``Tr(g)-2`` through the two-dimensional dot product."""

    p1, p2 = trace_pair_invariants(a, h1, h3)
    q1 = h2 * h4
    q2 = h2 + h4
    return a * (p1 * q1 + p2 * q2)


def affine_trace_parameters(
    a: int, h1: int, h2: int, h3: int
) -> tuple[int, int]:
    """Return ``(slope, intercept)`` for the affine map in ``h4``.

    Exactly,

        trace_a(h1,h2,h3,h4) = slope*h4 + intercept.

    Away from the coordinate axes, the map from ``(h1,h2,h3)`` to this
    affine pair has only divisor-type multiplicity.  This is the affine-line
    formulation of the remaining weighted incidence problem.
    """

    slope = a * a * h1 * h2 * h3 - a * (h1 + h3)
    intercept = 2 - a * (h1 + h3) * h2
    return slope, intercept


def opposite_scaling_trace(
    a: int,
    numerator: int,
    denominator: int,
    h1: int,
    h2: int,
    h3: int,
    h4: int,
) -> tuple[int, int]:
    """Check the exact split-torus scaling symmetry when it stays integral.

    Odd positions are multiplied by ``numerator/denominator`` and even
    positions by its reciprocal.  The two returned traces are equal.
    """

    if numerator == 0 or denominator == 0:
        raise ValueError("scaling numerator and denominator must be nonzero")
    if (numerator * h1) % denominator or (numerator * h3) % denominator:
        raise ValueError("scaled odd coordinates are not integral")
    if (denominator * h2) % numerator or (denominator * h4) % numerator:
        raise ValueError("scaled even coordinates are not integral")
    scaled = (
        numerator * h1 // denominator,
        denominator * h2 // numerator,
        numerator * h3 // denominator,
        denominator * h4 // numerator,
    )
    return trace_value(a, h1, h2, h3, h4), trace_value(a, *scaled)


def aperiodic_autocorrelation(values: Sequence[Number]) -> dict[int, Number]:
    """Return the exact finite aperiodic autocorrelation of ``values``."""

    result: dict[int, Number] = {}
    length = len(values)
    for shift in range(-(length - 1), length):
        total: Number = 0
        for index in range(length):
            other = index - shift
            if 0 <= other < length:
                total += values[index] * complex(values[other]).conjugate()
        result[shift] = total
    return result


def puncture_zero(sequence: Mapping[int, Number]) -> dict[int, Number]:
    """Remove the zero shift, as in the explicit off-axis trace block."""

    return {shift: value for shift, value in sequence.items() if shift != 0}


def weighted_nonparabolic_trace_energy(
    a: int, sequences: Sequence[Mapping[int, Number]]
) -> float:
    """Compute the finite weighted energy after deleting traces ``+/-2``.

    This is an exact small-box falsifier, not an asymptotic estimator.
    """

    if len(sequences) != 4:
        raise ValueError("exactly four shift sequences are required")
    coefficients: dict[int, complex] = defaultdict(complex)
    for h1, z1 in sequences[0].items():
        for h2, z2 in sequences[1].items():
            for h3, z3 in sequences[2].items():
                for h4, z4 in sequences[3].items():
                    trace = trace_value(a, h1, h2, h3, h4)
                    if trace not in (-2, 2):
                        coefficients[trace] += z1 * z2 * z3 * z4
    return float(sum(abs(value) ** 2 for value in coefficients.values()))


def sharp_trace_energy_example(h: int) -> tuple[int, int]:
    """Return the exact elementary lower example and its squared norm.

    Take ``a=1``, ``z1=z2=delta_1`` and ``z3=z4=1_[1,h]``.  Then
    ``Tr=1-h3-h4``.  Removing ``Tr=-2`` deletes the two representations of
    ``h3+h4=3`` and hence four units of energy.  The second return value is
    ``prod_i ||z_i||_2^2=h^2``.
    """

    if h < 2:
        raise ValueError("h must be at least two")
    energy = (2 * h**3 + h) // 3 - 4
    return energy, h * h


def punctured_autocorrelation_sharpness_ledger(h: int) -> dict[str, int]:
    """A rigorous ``Omega(H)`` trace-energy example with zero axes.

    The first two packets are punctured autocorrelations of ``(1,1)``.
    The last two are punctured autocorrelations of a flat packet of length
    ``h+1``.  Restricting to ``h1=h2=1`` and
    ``ceil(h/4)<=h3,h4<=floor(h/2)`` gives a nonparabolic positive subenergy.
    The returned integer bounds prove

        energy / prod_i ||z_i||_2^2 >= h / 24576.

    Thus even within genuine punctured autocorrelations no uniform theorem
    can improve the candidate ``H^(1+o(1))`` scale.
    """

    if h < 8:
        raise ValueError("h must be at least eight")
    interval_length = floor(h / 2) - ceil(h / 4) + 1
    # The flat interval convolution has energy (2*m^3+m)/3.  Each selected
    # long autocorrelation coefficient is at least h/2.
    convolution_energy = (2 * interval_length**3 + interval_length) // 3
    subenergy_lower = h**4 * convolution_energy // 16
    long_norm_squared = h * (h + 1) * (2 * h + 1) // 3
    exact_norm_product = 4 * long_norm_squared**2
    coarse_norm_upper = 16 * h**6
    coarse_energy_lower = h**7 // 1536
    return {
        "interval_length": interval_length,
        "convolution_energy": convolution_energy,
        "subenergy_lower": subenergy_lower,
        "exact_norm_product": exact_norm_product,
        "coarse_energy_lower": coarse_energy_lower,
        "coarse_norm_upper": coarse_norm_upper,
    }


def squarefree_decomposition(n: int) -> tuple[int, int]:
    """Return signed squarefree d and nonnegative m with n=d*m^2.

    Zero is represented by ``(0, 0)``.
    """

    if n == 0:
        return 0, 0
    sign = -1 if n < 0 else 1
    remaining = abs(n)
    square_part = 1
    kernel = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        square_part *= prime ** (exponent // 2)
        if exponent % 2:
            kernel *= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        kernel *= remaining
    return sign * kernel, square_part


def is_nonzero_square(n: int) -> bool:
    """Whether n is a positive nonzero integer square."""

    if n <= 0:
        return False
    root = int(n**0.5)
    while (root + 1) * (root + 1) <= n:
        root += 1
    while root * root > n:
        root -= 1
    return root * root == n


def legendre_symbol(n: int, prime: int) -> int:
    """The Legendre symbol (n/prime) for an odd prime."""

    if prime < 3 or prime % 2 == 0:
        raise ValueError("prime must be an odd prime")
    residue = n % prime
    if residue == 0:
        return 0
    value = pow(residue, (prime - 1) // 2, prime)
    if value == 1:
        return 1
    if value == prime - 1:
        return -1
    raise ValueError("the supplied modulus does not behave as a prime")


def character_after_squarefree_reduction(n: int, prime: int) -> tuple[int, int]:
    """Compare (n/p) with (sf(n)/p), retaining ramification information."""

    kernel, square_part = squarefree_decomposition(n)
    original = legendre_symbol(n, prime)
    reduced = legendre_symbol(kernel, prime) if kernel else 0
    if square_part % prime == 0:
        reduced = 0
    return original, reduced


def heath_brown_critical_ledger(h: int) -> dict[str, int]:
    """Scale ledger in the favorable a=1, H=sqrt(R) model.

    There are K=H^4 four-tuples, discriminant height D=H^8, and R=H^2
    outer moduli.  With unit, collision-free coefficients, the quadratic
    large-sieve/Cauchy bound has scale H^7 while direct summation has H^6.
    """

    if h < 1:
        raise ValueError("h must be positive")
    outer_scale = h * h
    tuple_count = h**4
    conductor_height = h**8
    trivial_scale = outer_scale * tuple_count
    hb_scale = h * (h**4) * (h**2)
    return {
        "R": outer_scale,
        "K": tuple_count,
        "D": conductor_height,
        "trivial": trivial_scale,
        "quadratic_large_sieve": hb_scale,
    }


def trace_large_sieve_critical_ledger(h: int) -> dict[str, int]:
    """Critical scale after grouping by the trace rather than Delta.

    The trace interval has length N=H^4.  The exact divisor argument gives
    at most H^(2+o(1)) tuples in a nonparabolic trace fiber.  For unit
    coefficients this bounds trace energy by H^6.  The additive trace large
    sieve then has the same H^6 scale as direct summation.
    """

    if h < 1:
        raise ValueError("h must be positive")
    return {
        "R": h**2,
        "trace_interval": h**4,
        "tuple_count": h**4,
        "max_fiber_bound": h**2,
        "trace_energy_bound": h**6,
        "trivial": h**6,
        "trace_large_sieve": h**6,
    }


def complete_trace_character_sum(prime: int) -> int:
    """Return sum_{t mod p} (t^2-4 / p), exactly ``-1``."""

    return sum(legendre_symbol(t * t - 4, prime) for t in range(prime))


def square_kernel_pair_energy(coefficients: dict[int, Number]) -> float:
    """Return sum_d (sum_{n=d*m^2}|a_n|)^2.

    Signs of d are kept separate.  This is the square-pair quantity in the
    general-coefficient form of Heath--Brown's quadratic large sieve.
    """

    grouped: dict[int, float] = defaultdict(float)
    for n, coefficient in coefficients.items():
        kernel, _ = squarefree_decomposition(n)
        grouped[kernel] += abs(coefficient)
    return sum(value * value for value in grouped.values())


def adversarial_row_dependent_character_sum(
    primes: list[int], discriminants: list[int]
) -> tuple[int, int]:
    """Show why arbitrary r-dependent coefficients defeat a large sieve.

    Set c_{r,d}=(d/r) on nonramified pairs.  Then every product
    c_{r,d}(d/r) equals one.  Return the signed sum and the number of
    nonramified pairs; they are equal.
    """

    total = 0
    pairs = 0
    for prime in primes:
        for discriminant in discriminants:
            symbol = legendre_symbol(discriminant, prime)
            if symbol:
                total += symbol * symbol
                pairs += 1
    return total, pairs
