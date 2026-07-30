"""Arb certificate for the clipped-symbol Legendre matrix at L=7/4.

The clipped multiplier uses S=50 and

    alpha = Re psi(1/4 + i S/2) - log(pi) - sqrt(2) log(2).

Subject to the analytic monotonicity lemma recorded in
``results/experts/FULLINF.md``, this matrix is the finite core of an
unrestricted lower bound.  The script proves the finite-dimensional inequality
``A_48 > 2.27e-5 I`` and checks every constant in the elementary two-by-two
finite-to-full transfer, giving ``Q_(7/4) > 2.2699e-5`` on the full form-domain
unit sphere.
The calculation is written for the real Hilbert space.  The same bound holds
on its complexification: the multiplier, projection, and pole operator have
real kernels, so the Hermitian form of ``u+iv`` is the sum of the real forms
of ``u`` and ``v``.

All exact arithmetic uses FLINT fmpq and all transcendental, quadrature, and
linear-algebra enclosures use Arb through python-flint >= 0.9.0.  Generic Arb
conversion and Cholesky helpers are imported from ``arb_fullinf_certificate``;
no prior project matrix, quadrature, or numerical result is reused, and no
mpmath interval is imported.  The program does not machine-prove the
digamma-monotonicity lemma that compares the clipped operator with the full
Weil form; that analytic lemma remains part of the mathematical trust base.

The frequency integrals are split into unit panels.  On [0,1], spherical
Bessel functions use their entire 0F1 representation, avoiding the removable
singularity at zero.  On [1,50], Arb's Bessel J implementation is used.  This
split is important: using 0F1 on the whole oscillatory interval causes severe
ball overestimation, while J_(k+1/2)(z)*sqrt(pi/(2z)) is branch-safe away from
zero.

At L=7/4 the prime sum contains only n=2, since log(2)<L/2<log(3); the
script verifies both strict support decisions with Arb before certification.
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
M = 48
S = 50

ctx.prec = PRECISION
# Python callbacks into acb_calc are kept single-threaded.  Independent
# processes may still run separate certificates safely.
ctx.threads = 1


def Q(n, d=1):
    return fmpq(n, d)


def A(x):
    return arb(x)


A_HALF_WIDTH = Q(7, 16)
PI = arb.pi()
LOG2 = A(2).log()
PRIME_AMPLITUDE = A(2).sqrt() * LOG2
I = acb(0, 1)
ALPHA = (
    acb(Q(1, 4), A(S) / 2).digamma().real
    - PI.log()
    - PRIME_AMPLITUDE
)
TOLERANCE = A(2) ** (-ABS_TOL_BITS)


def omega(z):
    """Holomorphic symmetrization of the real zeta Weil symbol."""
    plus = (acb(Q(1, 4)) + I * z / 2).digamma()
    minus = (acb(Q(1, 4)) - I * z / 2).digamma()
    return (
        (plus + minus) / 2
        - PI.log()
        - PRIME_AMPLITUDE * (z * LOG2).cos()
    )


_ODD_DOUBLE_FACTORIAL = [prod(range(1, 2 * k + 2, 2)) for k in range(M)]


def spherical_j_series(k, r):
    """Entire 0F1 formula, used only on the first frequency panel."""
    z = A(A_HALF_WIDTH) * r
    return (
        z**k / _ODD_DOUBLE_FACTORIAL[k]
        * (-z * z / 4).hypgeom_0f1(Q(2 * k + 3, 2))
    )


def spherical_j_bessel(k, r, analytic):
    """Spherical j_k through Arb's Bessel J, away from the origin."""
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
    """Assemble A_S in the normalized Legendre basis."""
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

    # The zeta pole is an exact rank-two form.  For normalized P_k(x/a),
    # integral b_k(x)e^(x/2) dx = sqrt(2a(2k+1)) i_k(a/2), and replacing
    # x by -x contributes (-1)^k.
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


def certify_finite_core(verbose=True):
    if not ALPHA > A(1):
        raise ArithmeticError(f"failed even the coarse alpha > 1 check: {ALPHA}")
    if not LOG2 < A(2 * A_HALF_WIDTH):
        raise ArithmeticError("failed to prove that the n=2 prime term is present")
    if not A(3).log() > A(2 * A_HALF_WIDTH):
        raise ArithmeticError("failed to prove that all n>=3 prime terms are absent")
    started = time()
    matrix = clipped_matrix(verbose=verbose)
    assembly_seconds = time() - started
    target = Q(227, 10_000_000)  # 2.27e-5
    pivots = interval_cholesky(matrix, [Q(1)] * M, beta=target)
    return matrix, pivots, target, assembly_seconds


def full_space_transfer(beta):
    """Check the two-by-two transfer from V_M to all of real H_L.

    The analytic input is that the archimedean symbol is increasing in |r|.
    It gives Omega(r) >= alpha outside [-S,S], hence Q >= A_S.  On the band,
    |Omega-alpha| <= M_bound.  For w orthogonal to V_M, the exact Legendre
    Bessel-tail estimate gives ||C_S w||^2 <= rho ||w||^2.  The pole residuals
    are at most delta.  Consequently, for f=u+w,

      A_S(f) >= beta||u||^2 + d||w||^2 - 2c||u||||w||.

    Positivity of the displayed 2x2 matrix after subtracting gamma proves the
    unrestricted lower bound gamma.
    """
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

    # Each sign has the same Taylor-competitor projection bound.
    delta = (
        (2 * A(a)).sqrt()
        * (A(a) / 2).exp()
        * A((a / 2) ** M)
        / factorial(M)
    )
    sinh_a = (A(a).exp() - (-A(a)).exp()) / 2
    pole_norm = (2 * sinh_a).sqrt()

    kappa = (
        arb.const_euler()
        + PI / 2
        + 3 * LOG2
        + PI.log()
    )
    c_minus = kappa + PRIME_AMPLITUDE
    multiplier_bound = c_minus + ALPHA
    # The lower direction has magnitude at most c_-+alpha.  Monotonicity on
    # the band bounds the upper direction by 2*c_pr; certify that our chosen
    # scalar dominates both rather than silently assuming which is larger.
    require_gt(
        multiplier_bound - 2 * PRIME_AMPLITUDE,
        Q(5),
        "gap between M_bound and the upper symbol direction",
    )
    d = ALPHA - multiplier_bound * rho - 2 * delta * delta
    c = multiplier_bound * rho.sqrt() + 2 * pole_norm * delta

    # Rational, outward-rounded checks back every shortened decimal below.
    require_lt(rho, Q(81, 10**23), "Legendre band defect rho")
    require_lt(delta, Q(195, 10**95), "one-sign pole residual delta")
    require_lt(multiplier_bound, Q(7447, 1000), "band multiplier bound")
    require_gt(d, Q(1093, 1000), "complement diagonal d")
    require_lt(c, Q(212, 10**12), "low/high coupling c")

    gamma = Q(22699, 10**9)  # 2.2699e-5
    if not beta > gamma:
        raise ArithmeticError("finite beta does not exceed full target gamma")
    determinant = A(beta - gamma) * (d - A(gamma)) - c * c
    require_gt(d - A(gamma), Q(1), "shifted complement diagonal")
    require_gt(determinant, Q(1, 10**9), "2x2 shifted determinant")
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
    print("A47,47", clipped[47][47].str(25, radius=True))
    print("ARBITRARY-PRECISION BALL CERTIFIED: lambda_min(A_48) > 2.27e-5")
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
    print("ARBITRARY-PRECISION BALL CERTIFIED: inf Q_(7/4) > 2.2699e-5")
