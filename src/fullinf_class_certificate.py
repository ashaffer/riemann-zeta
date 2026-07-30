"""Reproducible software certificate for one FULLINF frequency-tail class.

This instantiates Theorem F4 of ``results/experts/FULLINF.md`` at

    L = 7/4, m = 48, R = 50, tau_bar = 1e-15.

The conclusion concerns unit vectors in the full form domain whose normalized
Fourier mass above R is at most tau_bar.  It is not the unrestricted Weil-form
infimum and does not imply RH.  An exact-moment calculation for an explicit
degree-28 rational polynomial certifies that the class is nonempty.  It does
not certify that any proposed zero-centered packet belongs to the class.

The arithmetic is outward-rounded by mpmath.iv.  Its elementary functions and
interval operations are therefore part of the trust base.  Analytic inputs are
Theorem F4, the digamma bounds in THEOREMS.md, the conservative Landau bound
|J_nu(z)| <= z^(-1/3) used in the T2 majorant, and the complex asymptotic
remainder bound for digamma in DLMF 5.11(ii).  The latter is used for a second
certificate: Q_(7/4) is uniformly coercive on the orthogonal complement of the
first 48 Legendre modes.

The T2 integral is bounded without quadrature.  For r >= 1,

    Omega_bar(r) <= 15 + log(r) + log(5)/2 = C + log(r),

and the content bound is at most min(1, A (a r)^(-5/3)), with
A = pi*m^2/2 (we replace Landau's constant < 1 by 1).  Splitting where the
two branches cross reduces both integrals to closed-form antiderivatives.
"""

from fractions import Fraction
from math import comb, factorial
import time

import mpmath as mp
from mpmath import iv

import certified_spectral as spectral
from certified_margins import F2iv, iv_cholesky_pd


PREC = 512
iv.prec = PREC
spectral.iv.prec = PREC
mp.mp.dps = 100


def endpoint_lo(x):
    return mp.mpf(x.a)


def endpoint_hi(x):
    return mp.mpf(x.b)


def require_upper(x, bound, name):
    if not x < F2iv(bound):
        raise ValueError(f"failed to prove {name} < {bound}")


def require_lower(x, bound, name):
    if not x > F2iv(bound):
        raise ValueError(f"failed to prove {name} > {bound}")


def certify_core(L, m, lambda_cert):
    """Interval-Cholesky proof that the m-dimensional minimum exceeds beta."""
    Q, G = spectral.certified_spectral_form(L, m, N=400)
    shifted = [
        [
            Q[i][j] - (F2iv(lambda_cert * G[i]) if i == j else 0)
            for j in range(m)
        ]
        for i in range(m)
    ]
    return iv_cholesky_pd(shifted)


def t2_majorant(a, m, R):
    """Closed-form interval upper bound for FULLINF's T2(m,R)."""
    # This exact constant dominates c0 = |psi(1/4)-log(pi)| + 8 + C_pr.
    c0_bar = F2iv(15)
    C = c0_bar + iv.log(F2iv(5)) / 2

    # With Landau's constant replaced by 1, the third content branch is
    # A_z * (a*r)^(-5/3), A_z = pi*m^2/2.
    A_z = iv.pi * F2iv(m * m) / 2
    r0 = iv.exp(F2iv(Fraction(3, 5)) * iv.log(A_z)) / F2iv(a)
    if not F2iv(R) < r0:
        raise ValueError("T2 split requires R below the branch crossing")

    def primitive(r):
        y = C + iv.log(r)
        return r * (y * y - 2 * y + 2)

    low_piece = primitive(r0) - primitive(F2iv(R))
    q = F2iv(Fraction(2, 3))
    y0 = C + iv.log(r0)
    # A_r * integral_{r0}^inf r^(-5/3)(C+log r)^2 dr.  The crossing
    # identity A_r*r0^(-2/3)=r0 yields this numerically stable expression.
    tail_piece = r0 * (y0 * y0 / q + 2 * y0 / (q * q) + 2 / (q * q * q))
    return 2 * F2iv(a) / iv.pi * (low_piece + tail_piece), C


def digamma_real_at_quarter(y, shift=50, terms=10):
    """Enclose Re psi(1/4+i*y) without calling a special-function oracle.

    Recurrence moves the argument to Z=1/4+shift+i*y.  We then use

      psi(Z) = log Z - 1/(2Z)
               - sum_{k=1}^{terms-1} B_(2k)/(2k Z^(2k)) + remainder.

    DLMF 5.11(ii) bounds the complex remainder by the first omitted term
    times sec(arg(Z)/2)^(2*terms+1).  The identity
    sec(arg(Z)/2)^2 = 2|Z|/(|Z|+Re Z) avoids an interval atan.
    """
    x = Fraction(1, 4)
    z0 = iv.mpc(F2iv(x), F2iv(y))
    Z = z0 + shift
    approximation = iv.log(Z) - 1 / (2 * Z)
    for k in range(1, terms):
        numerator, denominator = mp.bernfrac(2 * k)
        bernoulli = Fraction(int(numerator), int(denominator))
        approximation -= F2iv(bernoulli) / (2 * k * Z ** (2 * k))

    numerator, denominator = mp.bernfrac(2 * terms)
    next_bernoulli = abs(Fraction(int(numerator), int(denominator)))
    abs_Z = abs(Z)
    sec_squared = 2 * abs_Z / (abs_Z + Z.real)
    remainder = (
        F2iv(next_bernoulli) / (2 * terms * abs_Z ** (2 * terms))
        * sec_squared ** F2iv(Fraction(2 * terms + 1, 2))
    )

    recurrence = sum((1 / (z0 + j) for j in range(shift)), iv.mpc(0))
    center = (approximation - recurrence).real
    return center + F2iv([-1, 1]) * remainder


def certify_legendre_complement():
    """Certify Q_(7/4)(w) > 0.1773 ||w||^2 for w perpendicular to V_48.

    Re psi(1/4+i*y) is increasing for y>=0, directly from its convergent
    partial-fraction series.  Hence for |r|>=R the single-prime symbol at this
    window is bounded below by its digamma value at R with cos(r log 2)
    replaced by 1.  Below R, F2 bounds the Fourier mass of w perpendicular to
    V_m.  The rank-two pole term is controlled by its Legendre projection
    error.
    """
    L = Fraction(7, 4)
    a = L / 4
    m = 48
    R = Fraction(20)

    c_pr = 2 * iv.log(F2iv(2)) / iv.sqrt(F2iv(2))
    psi_at_cut = digamma_real_at_quarter(R / 2)
    omega_high = psi_at_cut - iv.log(iv.pi) - c_pr
    require_lower(
        omega_high,
        Fraction(1774, 10_000),
        "symbol outside |r|=20",
    )

    z = a * R
    q_m = z * z / Fraction((2 * m + 1) * (2 * m + 3))
    if q_m >= 1:
        raise ValueError("Bessel-tail geometric majorant requires q_m < 1")
    odd_double_factorial = 1
    for k in range(1, 2 * m + 2, 2):
        odd_double_factorial *= k
    t_m = Fraction(2 * m + 1) * z ** (2 * m) / odd_double_factorial**2
    B_star = t_m / (1 - q_m)
    # By Plancherel and F2(a), this is the fraction of ||w||^2 that can lie in
    # |r|<=R when w is perpendicular to V_m.
    low_mass = 2 * F2iv(a) * F2iv(R) / iv.pi * F2iv(B_star)

    # Projection error for both pole vectors, exactly as in class_lower_bound.
    delta_p = (
        2
        * iv.sqrt(2 * F2iv(a))
        * iv.exp(F2iv(a) / 2)
        * F2iv((a / 2) ** m)
        / F2iv(factorial(m))
    )
    coefficient = (
        omega_high * (1 - low_mass)
        - F2iv(7) * low_mass
        - delta_p * delta_p / 2
    )
    require_upper(low_mass, Fraction(2, 10**60), "low-frequency complement mass")
    require_lower(
        coefficient,
        Fraction(1773, 10_000),
        "Legendre-complement coercivity",
    )
    return {
        "omega_high_lower": endpoint_lo(omega_high),
        "low_mass_upper": endpoint_hi(low_mass),
        "coercivity_lower": endpoint_lo(coefficient),
    }


def class_lower_bound():
    L = Fraction(7, 4)
    a = L / 4
    m = 48
    R = Fraction(50)
    tau_bar = Fraction(1, 10**15)
    lambda_cert = Fraction(313, 10_000_000)  # 3.13e-5

    if R < 1:
        raise ValueError("closed-form T2 majorant requires R >= 1")
    # Fail closed on F4's displayed sufficient cut condition
    # aR <= 0.9*(2m+1)/e.
    if not F2iv(a * R) < F2iv(Fraction(9 * (2 * m + 1), 10)) / iv.e:
        raise ValueError("F4 cut condition is not interval-certified")

    # Verify the two simple symbol constants rather than trusting decimal text.
    psi14 = -iv.euler - iv.pi / 2 - 3 * iv.log(F2iv(2))
    kappa0 = abs(psi14 - iv.log(iv.pi))
    c_pr = 2 * iv.log(F2iv(2)) / iv.sqrt(F2iv(2))
    require_upper(kappa0 + 8 + c_pr, 15, "c0")
    require_upper(kappa0 + c_pr, 7, "c_minus")

    started = time.time()
    core_ok = certify_core(L, m, lambda_cert)
    core_seconds = time.time() - started
    if not core_ok:
        raise RuntimeError("finite Galerkin core did not certify")

    T2, C = t2_majorant(a, m, R)

    z = a * R
    q_m = z * z / Fraction((2 * m + 1) * (2 * m + 3))
    if q_m >= 1:
        raise ValueError("Bessel-tail geometric majorant requires q_m < 1")
    odd_double_factorial = 1
    for k in range(1, 2 * m + 2, 2):
        odd_double_factorial *= k
    t_m = Fraction(2 * m + 1) * z ** (2 * m) / odd_double_factorial**2
    B_star = t_m / (1 - q_m)
    beta_capture = iv.sqrt(2 * F2iv(a) * F2iv(B_star))

    eps = iv.sqrt(F2iv(tau_bar)) + iv.sqrt(F2iv(R) / iv.pi) * beta_capture

    # Projection error for e^{+/-x/2}, bounded by the degree-(m-1) Taylor
    # polynomial.  Projection is at least as accurate as this competitor.
    delta_p = (
        2
        * iv.sqrt(2 * F2iv(a))
        * iv.exp(F2iv(a) / 2)
        * F2iv((a / 2) ** m)
        / F2iv(factorial(m))
    )
    omega_R = C + iv.log(F2iv(R))
    sinh_a = (iv.exp(F2iv(a)) - iv.exp(-F2iv(a))) / 2
    E = 2 * (
        iv.sqrt(T2) * eps
        + omega_R * iv.sqrt(F2iv(R) / iv.pi) * beta_capture * eps
        + iv.sqrt(2 * sinh_a) * delta_p * eps
    ) + (F2iv(7) + delta_p * delta_p / 2) * eps * eps
    lower = F2iv(lambda_cert) * (1 - eps * eps) - E

    # Exact rational comparisons back every printed CERTIFIED inequality.
    require_upper(iv.sqrt(T2), Fraction(159237, 500), "sqrt(T2)")  # 318.474
    require_upper(beta_capture, Fraction(357, 50_000_000_000_000),
                  "capture beta")  # 7.14e-12
    require_upper(eps, Fraction(317, 10_000_000_000), "epsilon")  # 3.17e-8
    require_upper(delta_p, Fraction(39, 10**94), "pole delta")  # 3.9e-93
    require_lower(lower, Fraction(11139, 1_000_000_000),
                  "restricted-class lower bound")  # 1.1139e-5

    return {
        "core_ok": core_ok,
        "core_seconds": core_seconds,
        "sqrt_T2_upper": endpoint_hi(iv.sqrt(T2)),
        "capture_beta_upper": endpoint_hi(beta_capture),
        "epsilon_upper": endpoint_hi(eps),
        "delta_p_upper": endpoint_hi(delta_p),
        "class_lower": endpoint_lo(lower),
    }


# Rational coefficients of one even polynomial
#   f(x) = sum_k d_k P_k(x/a),  a=7/16,
# obtained by rounding a numerical top time-band-concentration vector.  Their
# origin is irrelevant to the certificate: all calculations below use these
# displayed decimals as exact rational numbers.
_WITNESS_LEGENDRE = {
    0: Fraction("0.65232833448355803706776267482523357"),
    2: Fraction("-1.4186875217102238423816095868074176"),
    4: Fraction("1.3851582340132392648510269378955254"),
    6: Fraction("-1.0051788971195944548648788680647068"),
    8: Fraction("0.58028817023475974477121015779510872"),
    10: Fraction("-0.27377264589814093446693662376743423"),
    12: Fraction("0.10725958959755578877304599656518492"),
    14: Fraction("-0.035315712438526000357543171158159492"),
    16: Fraction("0.0098706373620027180676349103289012549"),
    18: Fraction("-0.0023629324862985554215833023491156143"),
    20: Fraction("0.00048846852098389556727191085420220129"),
    22: Fraction("-0.00008785800251582385646579672661454081"),
    24: Fraction("0.000013846113635082742455114255197255555"),
    26: Fraction("-0.0000019244227389602900083895911760910136"),
    28: Fraction("0.00000023731246900664426015967255425923963"),
}


def _legendre_polynomials(max_degree):
    """Exact monomial coefficients of P_0,...,P_max_degree."""
    polys = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for n in range(1, max_degree):
        nxt = [Fraction(0)] * (len(polys[n]) + 1)
        for j, coefficient in enumerate(polys[n]):
            nxt[j + 1] += Fraction(2 * n + 1, n + 1) * coefficient
        for j, coefficient in enumerate(polys[n - 1]):
            nxt[j] -= Fraction(n, n + 1) * coefficient
        polys.append(nxt)
    return polys[:max_degree + 1]


def certify_class_witness():
    """Prove that C(50,1e-15) contains an explicit rational polynomial.

    The band-energy kernel is sin(R(x-y))/(pi(x-y)).  We integrate its sinc
    Taylor polynomial exactly against f(x)f(y).  Once the omitted alternating
    terms decrease uniformly on |R(x-y)| <= 43.75, the first omitted term
    bounds the kernel error.  Cauchy--Schwarz gives

        (integral |f|)^2 <= 2a ||f||_2^2,

    converting that uniform error into a normalized Fourier-tail bound.
    """
    a = Fraction(7, 16)
    R = Fraction(50)
    series_degree = 80
    max_degree = max(_WITNESS_LEGENDRE)
    legendre = _legendre_polynomials(max_degree)

    # Exact monomial coefficients of f(x) on [-a,a].
    polynomial = [Fraction(0)] * (max_degree + 1)
    for degree, coefficient in _WITNESS_LEGENDRE.items():
        for power, legendre_coefficient in enumerate(legendre[degree]):
            polynomial[power] += (
                coefficient * legendre_coefficient / a**power
            )

    def moment(power):
        total = Fraction(0)
        for degree, coefficient in enumerate(polynomial):
            exponent = degree + power
            if exponent % 2 == 0:
                total += coefficient * 2 * a**(exponent + 1) / (exponent + 1)
        return total

    norm_sq = Fraction(0)
    for i, ci in enumerate(polynomial):
        for j, cj in enumerate(polynomial):
            exponent = i + j
            if exponent % 2 == 0:
                norm_sq += ci * cj * 2 * a**(exponent + 1) / (exponent + 1)
    if norm_sq <= 0:
        raise RuntimeError("explicit witness has nonpositive exact norm")

    moments = [moment(power) for power in range(2 * series_degree + 1)]
    sinc_integral = Fraction(0)
    for n in range(series_degree + 1):
        difference_moment = sum(
            Fraction((-1) ** j * comb(2 * n, j))
            * moments[2 * n - j] * moments[j]
            for j in range(2 * n + 1)
        )
        term = difference_moment * R ** (2 * n) / factorial(2 * n + 1)
        sinc_integral += term if n % 2 == 0 else -term

    # Sum the highly cancelling Taylor polynomial exactly before the one
    # conversion to interval arithmetic.
    band_series = F2iv(R * sinc_integral) / iv.pi
    zmax = 2 * a * R
    if zmax * zmax >= (2 * series_degree + 4) * (2 * series_degree + 5):
        raise RuntimeError("sinc remainder terms are not uniformly decreasing")
    relative_remainder = (
        2 * F2iv(a) * F2iv(R) / iv.pi
        * F2iv(zmax ** (2 * series_degree + 2))
        / F2iv(factorial(2 * series_degree + 3))
    )
    tail_upper = 1 - band_series / F2iv(norm_sq) + relative_remainder
    require_upper(
        tail_upper,
        Fraction(3, 10**17),
        "normalized Fourier tail of explicit witness",
    )
    return {
        "tail_upper": endpoint_hi(tail_upper),
        "norm_sq": endpoint_lo(F2iv(norm_sq)),
        "series_degree": series_degree,
    }


if __name__ == "__main__":
    complement = certify_legendre_complement()
    result = class_lower_bound()
    witness = certify_class_witness()
    print("rounded complement diagnostics:")
    print("  symbol lower endpoint outside |r|=20:",
          mp.nstr(complement["omega_high_lower"], 12))
    print("  low-frequency mass factor:",
          mp.nstr(complement["low_mass_upper"], 8))
    print("  complement coercivity endpoint:",
          mp.nstr(complement["coercivity_lower"], 12))
    print("SOFTWARE-CERTIFIED: Q_(7/4)|_(V_48^perp) > 0.1773 I")
    print(f"m=48 core lambda_m > 3.13e-5: {result['core_ok']} "
          f"({result['core_seconds']:.1f} s)")
    print("rounded endpoint diagnostics:")
    print("  sqrt(T2):", mp.nstr(result["sqrt_T2_upper"], 12))
    print("  capture beta:", mp.nstr(result["capture_beta_upper"], 12))
    print("  epsilon:", mp.nstr(result["epsilon_upper"], 12))
    print("  pole projection delta:", mp.nstr(result["delta_p_upper"], 8))
    print("  class lower endpoint:", mp.nstr(result["class_lower"], 12))
    print("CERTIFIED: sqrt(T2)<318.474, beta<7.14e-12, eps<3.17e-8")
    print("SOFTWARE-CERTIFIED CLASS BOUND: inf_C Q_L > 1.1139e-5")
    print("rounded witness-tail endpoint:", mp.nstr(witness["tail_upper"], 12))
    print("CERTIFIED NONVACUITY: explicit degree-28 polynomial tail < 3e-17")
