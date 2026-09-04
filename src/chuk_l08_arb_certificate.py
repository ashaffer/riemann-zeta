#!/usr/bin/env python3
"""Rigorous common-node Arb certificate for Chuk's ``L = 0.8`` window.

This driver independently encloses the one-stroke minorant

    R_alpha(f) = alpha ||f||_2^2
       + (1/pi) int_0^200 (Omega(t)-alpha) |F(t)|^2 dt
       + (zeta pole term),

with ``alpha = 1/2``.  Chuk's crude digamma envelope gives
``Omega(t) >= beta_*(200) > 1/2`` for ``t >= 200``; therefore the
completed-zeta Weil form is at least ``R_alpha``.

The finite matrix is assembled in the L2-normalized Legendre basis on
[-4/5,4/5].  All transcendental values, Gauss--Legendre nodes, weights,
matrix products, and Cholesky pivots are Arb balls (python-flint).  Unlike a
sampled quadrature calculation, the common-node quadrature has an explicit
analytic remainder:

* split [0,200] into unit panels;
* use q-point Gauss--Legendre on every panel;
* continue each entry to the Bernstein ellipse with imaginary semiaxis 1/4;
* bound ``|Omega(z)-alpha| < 21`` there;
* use ``|F_k(z)| <= sqrt(2a) exp(a |Im z|)`` and the Chebyshev tail bound

      |int f - GL_q(f)|
        <= h * 8 B rho^(-2q) / (1-rho^(-1)).

Here h=1/2 and rho=(1+sqrt(5))/2.  Summing this bound over all 200 panels
encloses each matrix entry.  The proof is elementary: Gauss--Legendre is
exact through degree 2q-1, a function bounded by B on E_rho has Chebyshev
coefficients at most 2 B rho^(-k), and both the integral and quadrature
functionals have norm 2 on C[-1,1].

The infinite Legendre complement is not omitted.  A spherical-Bessel tail
bound gives its band leakage ``rho_tail``; a two-by-two Schur calculation
includes the finite/tail coupling, tail diagonal, and pole leakage.  Thus a
successful final line certifies the bounded minorant on the whole real L2
window, not merely a Galerkin section.  Comparison with the actual Weil form
holds on its logarithmic form domain

    D_log = {f: supp f subset [-a,a],
             int log(2+|t|) |F(t)|^2 dt < infinity}.

Equivalently, one may extend Q by +infinity outside D_log.  Since all kernels
are real, the same inequality holds on the complex form domain by splitting
into real and imaginary parts.

The only analytic input not proved inside this file is Chuk's displayed crude
digamma envelope outside the cutoff (a weaker cousin of Theorem F7 in the
project's FULLINF audit).  The script checks its exact endpoint
specialization, support mask {2,3,4}, every quadrature/error constant, and the
complete head-to-tail transfer.

Default target:

    head R_alpha > 9.0e-18,
    full R_alpha - 8.9e-18 I is positive definite,
    total Legendre degrees k=0,...,249 (125 per parity).

At q=80 the uniform quadrature-radius contribution has operator norm below
2e-27 in either 125-dimensional parity block.  The degree-250 infinite-tail
Schur tax is negligible relative to the 1e-19 head/full shift clearance.
"""

from __future__ import annotations

import argparse
from math import factorial, prod
from time import time

from flint import acb, acb_mat, arb, arb_mat, ctx, fmpq

# Transcendental module constants below must never be frozen at python-flint's
# default 53-bit context.  Keep this assignment explicit instead of relying
# on the imported helper's current (incidental) precision side effect.
CONSTANT_PRECISION = 512
ctx.prec = CONSTANT_PRECISION

from arb_fullinf_certificate import (
    interval_cholesky,
    require_gt,
    require_lt,
    spherical_i,
)

# Defend against future changes to the imported module's context settings.
ctx.prec = CONSTANT_PRECISION


def Q(n: int, d: int = 1) -> fmpq:
    return fmpq(n, d)


def A(x) -> arb:
    return arb(x)


A_HALF_WIDTH = Q(4, 5)
CUTOFF = 200
ALPHA = Q(1, 2)
PI = arb.pi()
I = acb(0, 1)


def prime_data() -> tuple[list[tuple[int, arb, arb]], arb]:
    """Return active prime powers and their exact-form Arb amplitudes."""
    log2 = A(2).log()
    log3 = A(3).log()
    data = [
        (2, log2, A(2).sqrt() * log2),
        (3, log3, 2 * log3 / A(3).sqrt()),
        (4, 2 * log2, log2),
    ]
    return data, sum((amplitude for _, _, amplitude in data), A(0))


PRIME_DATA, PRIME_MASS = prime_data()


def omega_on_real_ball(t: arb) -> arb:
    """Enclose the real Weil symbol on a real interval ``t``."""
    value = acb(Q(1, 4), t / 2).digamma().real - PI.log()
    for _, logarithm, amplitude in PRIME_DATA:
        value -= amplitude * (t * logarithm).cos()
    return value


def omega_holomorphic(t: acb) -> acb:
    """Holomorphic symmetrization used by the independent adaptive replay."""
    plus = (acb(Q(1, 4)) + I * t / 2).digamma()
    minus = (acb(Q(1, 4)) - I * t / 2).digamma()
    value = (plus + minus) / 2 - PI.log()
    for _, logarithm, amplitude in PRIME_DATA:
        value -= amplitude * (t * logarithm).cos()
    return value


def support_and_envelope_checks() -> None:
    """Certify the mask, exterior floor, and elementary multiplier bounds."""
    support = 2 * A(A_HALF_WIDTH)
    require_lt(A(2).log(), support, "log(2) < 2a")
    require_lt(A(3).log(), support, "log(3) < 2a")
    require_lt(A(4).log(), support, "log(4) < 2a")
    require_gt(A(5).log(), support, "log(5) > 2a")

    beta_star = (
        (A(CUTOFF) / (2 * PI)).log()
        - Q(1, CUTOFF)
        - PRIME_MASS
    )
    require_gt(beta_star, ALPHA, "crude exterior floor beta_*(200) > 1/2")
    print("crude exterior beta_*", beta_star.str(18, radius=True), flush=True)

    # On the real band, recurrence plus Binet at w+1 (Re=5/4) gives
    # |psi(1/4+it/2)| <= log R + pi/2 + 2/5 + 4/75 + 4.
    # This avoids relying on monotonicity of Re psi for the Schur transfer.
    radius = (A(Q(5, 4)) ** 2 + A(Q(CUTOFF, 2)) ** 2).sqrt()
    psi_real_band_bound = (
        radius.log() + PI / 2 + Q(2, 5) + Q(4, 75) + 4
    )
    real_multiplier_bound = (
        psi_real_band_bound + PI.log() + PRIME_MASS + A(ALPHA)
    )
    require_lt(real_multiplier_bound, Q(16), "|Omega-alpha| on [0,200]")

    # On the common Bernstein ellipses, |Im t|<=1/4.  The two arguments
    # 1/4 +/- it/2 have Re >= 1/8.  Apply recurrence and Binet at w+1,
    # where Re >= 9/8, and use |cos(z log n)| <= cosh(log(4)/4).
    real_extent = A(CUTOFF) + (A(5).sqrt() - 2) / 4
    complex_radius = (
        A(Q(11, 8)) ** 2 + (real_extent / 2) ** 2
    ).sqrt()
    psi_ellipse_bound = (
        complex_radius.log()
        + PI / 2
        + Q(4, 9)
        + Q(16, 243)
        + 8
    )
    comb_ellipse_bound = PRIME_MASS * (A(4).log() / 4).cosh()
    ellipse_multiplier_bound = (
        psi_ellipse_bound + PI.log() + comb_ellipse_bound + A(ALPHA)
    )
    require_lt(
        ellipse_multiplier_bound,
        Q(21),
        "|Omega-alpha| on all Bernstein ellipses",
    )


def gauss_legendre_rule(order: int) -> list[tuple[arb, arb]]:
    """Certified q-point Gauss--Legendre nodes and weights on [-1,1]."""
    return [
        arb.legendre_p_root(order, k, weight=True)
        for k in range(order)
    ]


def spherical_j_direct(k: int, z: arb) -> arb:
    return (
        z.bessel_j(Q(2 * k + 1, 2))
        * (PI / (2 * z)).sqrt()
    )


def spherical_j_vector(z: arb, degree: int) -> list[arb]:
    """Rigorous j_0(z),...,j_(degree-1)(z) by anchored downward recurrence.

    Since 0 < z < 121 < degree in the certified run, j_degree(z) has no
    zero.  Arb encloses j_(degree+1)/j_degree, the exact three-term
    recurrence transports the ratio downward, and a direct Bessel value at
    an order close to z fixes the scale.  This uses three Bessel evaluations
    per common node rather than one per matrix entry.
    """
    top = degree
    j_top = spherical_j_direct(top, z)
    if j_top.contains(0):
        raise ArithmeticError("top spherical Bessel enclosure contains zero")
    ratio = spherical_j_direct(top + 1, z) / j_top
    values = [A(0) for _ in range(top + 2)]
    values[top] = A(1)
    values[top + 1] = ratio
    for k in range(top, 0, -1):
        values[k - 1] = (2 * k + 1) * values[k] / z - values[k + 1]

    pivot = min(degree - 1, max(0, int(float(z.mid()))))
    if values[pivot].contains(0):
        raise ArithmeticError("Miller recurrence pivot contains zero")
    scale = spherical_j_direct(pivot, z) / values[pivot]
    result = [value * scale for value in values[:degree]]
    if any(not value.is_finite() for value in result):
        raise ArithmeticError("non-finite spherical Bessel vector")
    return result


def quadrature_entry_error(order: int) -> arb:
    """Uniform absolute error for each completed matrix entry."""
    rho = (A(1) + A(5).sqrt()) / 2
    imag_semiaxis = Q(1, 4)
    fourier_product_bound = (
        2 * A(A_HALF_WIDTH)
        * (2 * A(A_HALF_WIDTH) * A(imag_semiaxis)).exp()
    )
    integrand_bound = 21 * fourier_product_bound
    half_panel = Q(1, 2)
    per_panel = (
        half_panel
        * 8
        * integrand_bound
        * rho ** (-2 * order)
        / (1 - 1 / rho)
        / PI
    )
    return CUTOFF * per_panel


def zero_matrix(rows: int, columns: int) -> arb_mat:
    return arb_mat(rows, columns)


def assemble_parity_blocks(
    degree: int,
    order: int,
    *,
    verbose: bool = True,
) -> tuple[list[arb_mat], arb]:
    """Assemble the even and odd leading blocks with a rigorous GL error."""
    rules = gauss_legendre_rule(order)
    parity_degrees = [list(range(0, degree, 2)), list(range(1, degree, 2))]
    normalizations = [
        (2 * A(A_HALF_WIDTH) * (2 * k + 1)).sqrt()
        for k in range(degree)
    ]
    blocks = [
        zero_matrix(len(parity_degrees[parity]), len(parity_degrees[parity]))
        for parity in (0, 1)
    ]

    for panel in range(CUTOFF):
        started = time()
        common = [zero_matrix(len(parity_degrees[p]), order) for p in (0, 1)]
        weighted = [zero_matrix(order, len(parity_degrees[p])) for p in (0, 1)]
        for column, (node, weight) in enumerate(rules):
            t = A(panel) + (node + 1) / 2
            z = A(A_HALF_WIDTH) * t
            js = spherical_j_vector(z, degree)
            scalar_weight = (
                weight / 2 * (omega_on_real_ball(t) - A(ALPHA)) / PI
            )
            for parity in (0, 1):
                for row, k in enumerate(parity_degrees[parity]):
                    phase = -1 if ((k - parity) // 2) % 2 else 1
                    value = phase * normalizations[k] * js[k]
                    common[parity][row, column] = value
                    weighted[parity][column, row] = scalar_weight * value
        for parity in (0, 1):
            blocks[parity] += common[parity] * weighted[parity]
        if verbose:
            print(
                f"integrated common panel {panel + 1}/{CUTOFF} "
                f"in {time() - started:.2f}s",
                flush=True,
            )

    entry_error = quadrature_entry_error(order)
    error_ball = arb(0, entry_error.upper())
    for parity in (0, 1):
        size = len(parity_degrees[parity])
        # Intersect the two independently rounded symmetric evaluations,
        # then add the proved analytic quadrature radius.
        for i in range(size):
            for j in range(i, size):
                symmetric = blocks[parity][i, j].intersection(
                    blocks[parity][j, i]
                )
                if symmetric is None:
                    raise ArithmeticError("rounded symmetric entries do not overlap")
                value = symmetric + error_ball
                blocks[parity][i, j] = blocks[parity][j, i] = value
            blocks[parity][i, i] += A(ALPHA)

        pole = arb_mat(size, 1)
        for row, k in enumerate(parity_degrees[parity]):
            pole[row, 0] = normalizations[k] * spherical_i(k, A_HALF_WIDTH / 2)
        sign = 2 if parity == 0 else -2
        blocks[parity] += sign * pole * pole.transpose()

    return blocks, entry_error


def certify_head(
    blocks: list[arb_mat],
    head_shift: fmpq,
) -> list[list[arb]]:
    pivots = []
    for parity, block in enumerate(blocks):
        size = block.nrows()

        # Direct interval Cholesky in degree order suffers severe wrapping
        # because the spectrum spans roughly 18 decimal orders.  Ask FLINT
        # only for an approximate eigenbasis of the midpoint, then freeze
        # the real parts as exact dyadic Arb points.  The approximation is an
        # untrusted proposal: the interval congruence and Cholesky below
        # prove the result from scratch.  Positivity of V^T(A-shift I)V also
        # proves that the frozen V is invertible.
        approximate_eigenvalues, approximate_vectors = acb_mat(
            block.mid()
        ).eig(right=True, algorithm="approx", maxiter=50)
        proposal = arb_mat(size, size)
        for i in range(size):
            for j in range(size):
                proposal[i, j] = approximate_vectors[i, j].real.mid()
        shift_matrix = arb_mat(size, size)
        for i in range(size):
            shift_matrix[i, i] = A(head_shift)
        transformed = (
            proposal.transpose() * (block - shift_matrix) * proposal
        )
        nested = [
            [transformed[i, j] for j in range(size)]
            for i in range(size)
        ]
        sector_pivots = interval_cholesky(
            nested,
            [Q(1)] * size,
            beta=Q(0),
        )
        approximate_eigenvalues.sort(key=lambda z: float(z.real.mid()))
        print(
            ("even" if parity == 0 else "odd"),
            "approximate least eigenvalue",
            approximate_eigenvalues[0].real.str(25, radius=False),
            "congruence smallest shifted pivot",
            min(sector_pivots).str(25),
            flush=True,
        )
        pivots.append(sector_pivots)
    return pivots


def maximum_entry_radius(block: arb_mat) -> tuple[arb, int, int]:
    """Return the largest final ball radius and one attaining entry."""
    maximum = A(0)
    location = (0, 0)
    for i in range(block.nrows()):
        for j in range(block.ncols()):
            radius = block[i, j].rad()
            if radius > maximum:
                maximum = radius
                location = (i, j)
    return maximum, location[0], location[1]


def adaptive_entry(k: int, j: int, degree: int) -> arb:
    """Independently enclose one matrix entry with ``acb.integral``.

    This deliberately shares neither the common Gauss nodes nor the
    Bernstein error formula.  It is a cross-check, not an input to the main
    proof.
    """
    if (k - j) % 2:
        return A(0)
    tolerance = A(2) ** (-150)

    def spherical_series(order: int, r: acb) -> acb:
        z = A(A_HALF_WIDTH) * r
        odd_double_factorial = prod(range(1, 2 * order + 2, 2))
        return (
            z**order / odd_double_factorial
            * (-z * z / 4).hypgeom_0f1(Q(2 * order + 3, 2))
        )

    def spherical_bessel(order: int, r: acb, analytic: bool) -> acb:
        z = A(A_HALF_WIDTH) * r
        return (
            z.bessel_j(Q(2 * order + 1, 2))
            * (PI / (2 * z)).sqrt(analytic=analytic)
        )

    def first_panel(r: acb, _analytic: bool) -> acb:
        return (
            (omega_holomorphic(r) - A(ALPHA))
            * spherical_series(k, r)
            * spherical_series(j, r)
        )

    def regular_panel(r: acb, analytic: bool) -> acb:
        return (
            (omega_holomorphic(r) - A(ALPHA))
            * spherical_bessel(k, r, analytic)
            * spherical_bessel(j, r, analytic)
        )

    integral = acb.integral(
        first_panel,
        0,
        1,
        abs_tol=tolerance,
        rel_tol=tolerance,
        deg_limit=100,
        eval_limit=100_000,
        depth_limit=25,
    )
    for left in range(1, CUTOFF):
        integral += acb.integral(
            regular_panel,
            left,
            left + 1,
            abs_tol=tolerance,
            rel_tol=tolerance,
            deg_limit=100,
            eval_limit=100_000,
            depth_limit=25,
        )
    if not integral.is_finite() or not integral.imag.contains(0):
        raise ArithmeticError(f"adaptive integral ({k},{j}) is not finite real")

    norm_k = (2 * A(A_HALF_WIDTH) * (2 * k + 1)).sqrt()
    norm_j = (2 * A(A_HALF_WIDTH) * (2 * j + 1)).sqrt()
    phase = -1 if ((j - k) // 2) % 2 else 1
    entry = phase * norm_k * norm_j / PI * integral.real
    if k == j:
        entry += A(ALPHA)
    pole_k = norm_k * spherical_i(k, A_HALF_WIDTH / 2)
    pole_j = norm_j * spherical_i(j, A_HALF_WIDTH / 2)
    entry += (2 if k % 2 == 0 else -2) * pole_k * pole_j
    return entry


def adaptive_cross_check(blocks: list[arb_mat], degree: int) -> None:
    """Replay nine entries spanning both parities and the high tail."""
    pairs = (
        (0, 0),
        (0, 20),
        (20, 20),
        (40, 80),
        (80, 80),
        (1, 1),
        (1, 21),
        (81, 121),
        (249, 249),
    )
    # Python callbacks into acb_calc are not thread-safe.  Matrix assembly
    # may use several FLINT workers, but adaptive callback integration must
    # temporarily be single-threaded.
    old_threads = ctx.threads
    ctx.threads = 1
    try:
        for k, j in pairs:
            if max(k, j) >= degree:
                continue
            direct = adaptive_entry(k, j, degree)
            parity = k % 2
            row = (k - parity) // 2
            column = (j - parity) // 2
            common = blocks[parity][row, column]
            if not direct.overlaps(common):
                raise ArithmeticError(
                    f"adaptive/common-node mismatch at degrees ({k},{j})"
                )
            print(
                "adaptive cross-check",
                k,
                j,
                direct.str(18, radius=True),
                "OVERLAPS",
                common.str(18, radius=True),
                flush=True,
            )
    finally:
        ctx.threads = old_threads


def full_space_transfer(
    degree: int,
    head_shift: fmpq,
    full_shift: fmpq,
) -> dict[str, arb | fmpq]:
    """Certify the full-space two-by-two transfer in both parity sectors."""
    a = A_HALF_WIDTH
    z = a * CUTOFF
    ratio = z * z / ((2 * degree + 1) * (2 * degree + 3))
    if not ratio < 1:
        raise ArithmeticError("spherical-Bessel tail ratio is not below one")
    odd_double_factorial = prod(range(1, 2 * degree + 2, 2))
    first_tail_term = (
        (2 * degree + 1)
        * z ** (2 * degree)
        / odd_double_factorial**2
    )
    b_star = first_tail_term / (1 - ratio)
    rho_tail = 2 * A(a) * CUTOFF / PI * A(b_star)

    pole_delta = (
        (2 * A(a)).sqrt()
        * (A(a) / 2).exp()
        * A((a / 2) ** degree)
        / factorial(degree)
    )
    pole_norm = ((A(a).exp() - (-A(a)).exp())).sqrt()
    multiplier_bound = A(16)
    complement_diagonal = (
        A(ALPHA)
        - multiplier_bound * rho_tail
        - 2 * pole_delta * pole_delta
    )
    coupling = (
        multiplier_bound * rho_tail.sqrt()
        + 2 * pole_norm * pole_delta
    )

    if not A(head_shift) > A(full_shift):
        raise ArithmeticError("head shift must strictly exceed full shift")
    shifted_head = A(head_shift - full_shift)
    shifted_tail = complement_diagonal - A(full_shift)
    determinant = shifted_head * shifted_tail - coupling * coupling
    require_gt(shifted_tail, Q(1, 5), "shifted complement diagonal")
    require_gt(determinant, Q(0), "full-space shifted 2x2 determinant")
    return {
        "bessel_ratio": ratio,
        "B_star": b_star,
        "rho_tail": rho_tail,
        "pole_delta": pole_delta,
        "complement_diagonal": complement_diagonal,
        "coupling": coupling,
        "determinant": determinant,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, default=250)
    parser.add_argument("--order", type=int, default=80)
    parser.add_argument("--precision", type=int, default=384)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument(
        "--cross-check",
        action="store_true",
        help="independently replay nine entries with adaptive Arb integration",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.degree <= CUTOFF * A_HALF_WIDTH:
        raise ValueError(f"degree must exceed a*T={A_HALF_WIDTH * CUTOFF} for the tail bound")
    if args.order < 32:
        raise ValueError("quadrature order is implausibly small")
    if args.precision < 384:
        raise ValueError("the preconditioned head proof requires at least 384 bits")
    ctx.prec = args.precision
    ctx.threads = args.threads

    head_shift = Q(9, 10**18)      # 9.0e-18
    full_shift = Q(89, 10**19)    # 8.9e-18
    support_and_envelope_checks()
    print("prime mass", PRIME_MASS.str(30, radius=True), flush=True)
    print("quadrature entry error", quadrature_entry_error(args.order).str(18, radius=True), flush=True)
    started = time()
    blocks, entry_error = assemble_parity_blocks(
        args.degree,
        args.order,
        verbose=not args.quiet,
    )
    print(f"assembly seconds {time() - started:.2f}", flush=True)
    print(
        "parity block dimensions",
        blocks[0].nrows(),
        blocks[1].nrows(),
        flush=True,
    )
    print(
        "quadrature operator error bounds",
        (blocks[0].nrows() * entry_error).str(18, radius=True),
        (blocks[1].nrows() * entry_error).str(18, radius=True),
        flush=True,
    )
    for parity, block in enumerate(blocks):
        radius, row, column = maximum_entry_radius(block)
        print(
            ("even" if parity == 0 else "odd"),
            "maximum final entry radius",
            radius.str(18, radius=True),
            "at",
            row,
            column,
            flush=True,
        )
    if args.cross_check:
        adaptive_cross_check(blocks, args.degree)
    certify_head(blocks, head_shift)
    transfer = full_space_transfer(args.degree, head_shift, full_shift)
    for key, value in transfer.items():
        print(key, A(value).str(25, radius=True), flush=True)
    print(
        "ARBITRARY-PRECISION BALL CERTIFIED: "
        "Q(f) >= 8.9e-18 ||f||_2^2 on the full a=0.8 logarithmic form "
        "domain, with strict inequality for every nonzero f",
        flush=True,
    )


if __name__ == "__main__":
    main()
