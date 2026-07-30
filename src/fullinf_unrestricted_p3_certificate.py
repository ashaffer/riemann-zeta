"""Arb certificate for the unrestricted p=3 window at L=497/200.

This is the two-prime analogue of ``fullinf_unrestricted_certificate.py``.
It is intentionally a separate driver so that the stable L=7/4 certificate
and its parameters remain untouched.

For a=497/800 and S=70, define

    alpha = Re psi(1/4 + 35 i) - log(pi)
            - sqrt(2)log(2) - 2log(3)/sqrt(3).

Strict monotonicity of Re psi(1/4+ir/2) in |r| makes alpha an exterior
lower bound for the multiplier.  The script uses python-flint/Arb to enclose
the clipped 80-dimensional normalized-Legendre matrix, prove it exceeds
beta=1e-10 by interval Cholesky, and verify the finite-to-full 2x2 transfer
at gamma=9.99e-11.

The calculation is written for the real Hilbert space.  It extends to the
complexification because all operators have real kernels and the Hermitian
form splits over real and imaginary parts.

The prime sum contains exactly n=2,3 because log(3)<L/2<log(4); all three
strict support decisions are checked with Arb.  Generic conversion, modified
spherical-Bessel, comparison, and Cholesky helpers come from
``arb_fullinf_certificate``.  No prior matrix or numerical result is reused.

EXPECTED (2026-07-27, python-flint 0.9.0 / FLINT 3.6.0, 128 bits):

    alpha                         0.1617833272712522268...
    smallest shifted pivot       0.0020771237783520...
    rho                           8.58130593924763e-23
    coupling c                    7.20961672485123e-11
    shifted 2x2 determinant       1.61783275192779e-14
    inf Q_(497/200)               > 9.99e-11

Two complete runs took 319 and 399 seconds on the audit machine.
"""

from math import factorial, prod
from time import time

from flint import acb, arb, ctx, fmpq

from arb_fullinf_certificate import (
    interval_cholesky,
    require_gt,
    require_lt,
    spherical_i,
)


PRECISION = 128
ABS_TOL_BITS = 75
M = 80
S = 70

ctx.prec = PRECISION
ctx.threads = 1


def Q(n, d=1):
    return fmpq(n, d)


def A(x):
    return arb(x)


A_HALF_WIDTH = Q(497, 800)
HALF_SUPPORT = 2 * A_HALF_WIDTH
PI = arb.pi()
LOG2 = A(2).log()
LOG3 = A(3).log()
PRIME_2 = A(2).sqrt() * LOG2
PRIME_3 = 2 * LOG3 / A(3).sqrt()
PRIME_AMPLITUDE = PRIME_2 + PRIME_3
I = acb(0, 1)
ALPHA = (
    acb(Q(1, 4), A(S) / 2).digamma().real
    - PI.log()
    - PRIME_AMPLITUDE
)
TOLERANCE = A(2) ** (-ABS_TOL_BITS)


def omega(z):
    """Holomorphic symmetrization of the two-prime Weil symbol."""
    plus = (acb(Q(1, 4)) + I * z / 2).digamma()
    minus = (acb(Q(1, 4)) - I * z / 2).digamma()
    return (
        (plus + minus) / 2
        - PI.log()
        - PRIME_2 * (z * LOG2).cos()
        - PRIME_3 * (z * LOG3).cos()
    )


_ODD_DOUBLE_FACTORIAL = [prod(range(1, 2 * k + 2, 2)) for k in range(M)]


def spherical_j_series(k, r):
    """Entire spherical-j formula for the first panel containing zero."""
    z = A(A_HALF_WIDTH) * r
    return (
        z**k / _ODD_DOUBLE_FACTORIAL[k]
        * (-z * z / 4).hypgeom_0f1(Q(2 * k + 3, 2))
    )


def spherical_j_bessel(k, r, analytic):
    """Spherical j_k through Arb's Bessel J on positive panels."""
    z = A(A_HALF_WIDTH) * r
    return (
        z.bessel_j(Q(2 * k + 1, 2))
        * (PI / (2 * z)).sqrt(analytic=analytic)
    )


def band_integral(k, j):
    """Enclose integral_0^S (Omega-alpha) j_k(ar)j_j(ar) dr."""

    def first_panel(r, _analytic):
        return (
            (omega(r) - ALPHA)
            * spherical_j_series(k, r)
            * spherical_j_series(j, r)
        )

    def regular_panel(r, analytic):
        return (
            (omega(r) - ALPHA)
            * spherical_j_bessel(k, r, analytic)
            * spherical_j_bessel(j, r, analytic)
        )

    result = acb.integral(
        first_panel,
        0,
        1,
        abs_tol=TOLERANCE,
        rel_tol=TOLERANCE,
        deg_limit=80,
        eval_limit=100_000,
        depth_limit=25,
    )
    if not result.is_finite():
        raise ArithmeticError(f"non-finite first-panel integral ({k}, {j})")
    for left in range(1, S):
        panel = acb.integral(
            regular_panel,
            left,
            left + 1,
            abs_tol=TOLERANCE,
            rel_tol=TOLERANCE,
            deg_limit=80,
            eval_limit=100_000,
            depth_limit=25,
        )
        if not panel.is_finite():
            raise ArithmeticError(
                f"non-finite integral for ({k}, {j}) on [{left},{left + 1}]"
            )
        result += panel
    if not result.imag.contains(0):
        raise ArithmeticError(f"real-path integral ({k}, {j}) excludes reality")
    return result.real


def clipped_matrix(verbose=True):
    """Assemble the clipped form in the normalized Legendre basis."""
    matrix = [[A(0) for _ in range(M)] for _ in range(M)]
    normalization = [
        (2 * A(A_HALF_WIDTH) * (2 * k + 1)).sqrt()
        for k in range(M)
    ]
    for k in range(M):
        row_started = time()
        for j in range(k, M):
            if (k + j) % 2:
                continue
            phase = (-1) ** ((j - k) // 2)
            entry = (
                phase
                * normalization[k]
                * normalization[j]
                / PI
                * band_integral(k, j)
            )
            if k == j:
                entry += ALPHA
            matrix[k][j] = matrix[j][k] = entry
        if verbose:
            print(
                f"integrated row {k + 1}/{M} in {time() - row_started:.2f}s",
                flush=True,
            )

    pole_vector = [
        normalization[k] * spherical_i(k, A_HALF_WIDTH / 2)
        for k in range(M)
    ]
    for k in range(M):
        for j in range(M):
            if (k + j) % 2 == 0:
                matrix[k][j] += (
                    pole_vector[k]
                    * pole_vector[j]
                    * ((-1) ** j + (-1) ** k)
                )
    return matrix


def support_checks():
    if not LOG2 < A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove that n=2 is present")
    if not LOG3 < A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove that n=3 is present")
    if not A(4).log() > A(HALF_SUPPORT):
        raise ArithmeticError("failed to prove that every n>=4 is absent")
    require_gt(ALPHA, Q(161, 1000), "exterior floor alpha")


def certify_finite_core(verbose=True):
    support_checks()
    started = time()
    matrix = clipped_matrix(verbose=verbose)
    assembly_seconds = time() - started
    beta = Q(1, 10**10)
    pivots = interval_cholesky(matrix, [Q(1)] * M, beta=beta)
    return matrix, pivots, beta, assembly_seconds


def full_space_transfer(beta):
    """Certify the Legendre-tail and two-by-two full-space transfer."""
    a = A_HALF_WIDTH
    z = a * S
    geometric_ratio = z * z / ((2 * M + 1) * (2 * M + 3))
    if not geometric_ratio < 1:
        raise ArithmeticError("exact Bessel-tail ratio is not below one")
    odd_double_factorial = prod(range(1, 2 * M + 2, 2))
    first_tail_term = (
        (2 * M + 1) * z ** (2 * M) / odd_double_factorial**2
    )
    b_star = first_tail_term / (1 - geometric_ratio)
    rho = 2 * A(a) * S / PI * A(b_star)

    delta = (
        (2 * A(a)).sqrt()
        * (A(a) / 2).exp()
        * A((a / 2) ** M)
        / factorial(M)
    )
    sinh_a = (A(a).exp() - (-A(a)).exp()) / 2
    pole_norm = (2 * sinh_a).sqrt()
    kappa = arb.const_euler() + PI / 2 + 3 * LOG2 + PI.log()
    c_minus = kappa + PRIME_AMPLITUDE
    multiplier_bound = c_minus + ALPHA
    require_gt(
        multiplier_bound - 2 * PRIME_AMPLITUDE,
        Q(3),
        "gap between M_bound and the upper symbol direction",
    )
    d = ALPHA - multiplier_bound * rho - 2 * delta * delta
    c = multiplier_bound * rho.sqrt() + 2 * pole_norm * delta

    require_lt(rho, Q(86, 10**24), "Legendre band defect rho")
    require_lt(delta, Q(51, 10**161), "one-sign pole residual delta")
    require_lt(multiplier_bound, Q(7783, 1000), "band multiplier bound")
    require_gt(d, Q(161, 1000), "complement diagonal d")
    require_lt(c, Q(721, 10**13), "low/high coupling c")

    gamma = Q(999, 10**13)  # 9.99e-11
    if not beta > gamma:
        raise ArithmeticError("finite beta does not exceed full target gamma")
    determinant = A(beta - gamma) * (d - A(gamma)) - c * c
    require_gt(d - A(gamma), Q(16, 100), "shifted complement diagonal")
    require_gt(determinant, Q(16, 10**15), "2x2 shifted determinant")
    return {
        "q": geometric_ratio,
        "B_star": b_star,
        "rho": rho,
        "delta": delta,
        "multiplier_bound": multiplier_bound,
        "d": d,
        "c": c,
        "gamma": gamma,
        "determinant": determinant,
    }


if __name__ == "__main__":
    print("alpha", ALPHA.str(30, radius=True), flush=True)
    clipped, pivot_lowers, beta, seconds = certify_finite_core()
    print(f"assembly seconds {seconds:.2f}")
    print("smallest shifted Cholesky pivot", min(pivot_lowers).str(25))
    print("last shifted Cholesky pivot", pivot_lowers[-1].str(25))
    print("A00", clipped[0][0].str(25, radius=True))
    print("A79,79", clipped[79][79].str(25, radius=True))
    print("ARBITRARY-PRECISION BALL CERTIFIED: lambda_min(A_80) > 1e-10")
    transfer = full_space_transfer(beta)
    print("Bessel geometric ratio", transfer["q"])
    print("B_star", A(transfer["B_star"]).str(18, radius=True))
    print("rho", transfer["rho"].str(18, radius=True))
    print("pole residual delta", transfer["delta"].str(18, radius=True))
    print("multiplier bound M", transfer["multiplier_bound"].str(18, radius=True))
    print("complement diagonal d", transfer["d"].str(18, radius=True))
    print("coupling c", transfer["c"].str(18, radius=True))
    print("shifted 2x2 determinant", transfer["determinant"].str(18, radius=True))
    print("ANALYTIC INPUT: monotonicity of Re psi(1/4+ir/2) in |r|")
    print("ARBITRARY-PRECISION BALL CERTIFIED: inf Q_(497/200) > 9.99e-11")
