"""Independent python-flint/Arb check of the FULLINF class certificate.

This checker intentionally imports no project modules.  Exact polynomial and
kernel-series arithmetic uses FLINT ``fmpq``; all transcendental and enclosure
arithmetic uses Arb.  It independently verifies the spectral core and is also
used below for the closed-form T2/error bound and explicit class witness.

Requires python-flint >= 0.9.0.  It is independent of mpmath.iv, but the
analytic inequalities instantiated here remain part of the mathematical trust
base; see results/experts/FULLINF.md.
"""

from flint import arb, fmpq, ctx
from math import comb, factorial
from time import time

ctx.prec = 512
ctx.threads = 4


def Q(n, d=1):
    return fmpq(n, d)


def A(x):
    return arb(x)


def decimal_rational(text):
    """Parse a displayed finite decimal as an exact fmpq."""
    negative = text.startswith("-")
    if negative:
        text = text[1:]
    if "." in text:
        whole, fractional = text.split(".")
        numerator = int(whole + fractional)
        denominator = 10 ** len(fractional)
    else:
        numerator, denominator = int(text), 1
    return Q(-numerator if negative else numerator, denominator)


def require_lt(value, rational_bound, name):
    if not value < A(rational_bound):
        raise ArithmeticError(f"Arb did not prove {name} < {rational_bound}: {value}")


def require_gt(value, rational_bound, name):
    if not value > A(rational_bound):
        raise ArithmeticError(f"Arb did not prove {name} > {rational_bound}: {value}")


def legendre_polynomials(m):
    out = [[Q(1)], [Q(0), Q(1)]]
    while len(out) < m:
        n = len(out) - 1
        nxt = [Q(0)] * (n + 2)
        for j, c in enumerate(out[n]):
            nxt[j + 1] += Q(2 * n + 1, n + 1) * c
        for j, c in enumerate(out[n - 1]):
            nxt[j] -= Q(n, n + 1) * c
        out.append(nxt)
    return out


def overlap_polynomial(k, j, polys):
    """Coefficients in v of integral_-1^(1-v) P_k(t)P_j(t+v) dt."""
    if k > j:
        k, j = j, k
    pk, pj = polys[k], polys[j]
    degree_t = k + j
    bivar = [[Q(0)] * (degree_t + 1) for _ in range(j + 1)]
    for i, cj in enumerate(pj):
        for q in range(i + 1):
            cvq = cj * comb(i, q)
            p = i - q
            for r, ck in enumerate(pk):
                bivar[p][q + r] += cvq * ck
    result = [Q(0)] * (k + j + 2)
    for p, row in enumerate(bivar):
        for q, c in enumerate(row):
            if not c:
                continue
            cint = c / (q + 1)
            for s in range(q + 2):
                result[p + s] += cint * comb(q + 1, s) * (-1) ** s
            result[p] -= cint * (-1) ** (q + 1)
    while len(result) > 1 and not result[-1]:
        result.pop()
    return result


def kernel_series(nmax, s=Q(1, 2)):
    """Exact coefficients of exp(-s u)/(1-exp(-2u))-1/(2u)."""
    bern = [fmpq.bernoulli(n) * 2**n / factorial(n)
            for n in range(nmax + 2)]
    exponential = [(2 - s)**n / factorial(n) for n in range(nmax + 2)]
    c = [Q(0)] * (nmax + 2)
    for i, ei in enumerate(exponential):
        for j, bj in enumerate(bern[:nmax + 2 - i]):
            c[i + j] += ei * bj
    return [c[r + 1] / 2 for r in range(nmax + 1)]


def kernel_tail(u, terms=200):
    """Arb enclosure of integral_u^inf exp(-x/2)/(1-exp(-2x)) dx."""
    u = A(u)
    ratio = (-2 * u).exp()
    total = A(0)
    term = None
    for n in range(terms):
        c = Q(4 * n + 1, 2)
        term = (-A(c) * u).exp() / A(c)
        total += term
    remainder = term * ratio / (1 - ratio)
    return total + arb(0, remainder.upper())


def spherical_i(k, z, terms=80):
    odd_df = 1
    for t in range(1, 2 * k + 2, 2):
        odd_df *= t
    z = A(z)
    term = z**k / odd_df
    total = term
    for s in range(1, terms + 1):
        term *= z * z / (2 * s * (2 * k + 2 * s + 1))
        total += term
    next_ratio = z * z / (2 * (terms + 1) * (2 * k + 2 * terms + 3))
    remainder = term * next_ratio / (1 - next_ratio)
    return total + arb(0, remainder.upper())


def assemble():
    a = Q(7, 16)
    two_a = 2 * a
    m = 48
    nmax = 400
    polys = legendre_polynomials(m)
    overlaps = [[None] * m for _ in range(m)]
    for k in range(m):
        for j in range(k, m):
            if (k + j) % 2 == 0:
                overlaps[k][j] = overlap_polynomial(k, j, polys)

    g = kernel_series(nmax)
    smax = 2 * m + 2
    powers = [Q(1)]
    for _ in range(smax + nmax + 3):
        powers.append(powers[-1] * two_a)
    moments = [Q(0)] * (smax + 1)
    for s in range(1, smax + 1):
        moments[s] = sum((g[r] * powers[s + r + 1] / (s + r + 1)
                          for r in range(nmax + 1)), Q(0))

    pi = arb.pi()
    ratio = A(two_a) / pi
    remainder_scale = A(250) / pi * ratio**(nmax + 1) / (1 - ratio)
    psi14 = -arb.const_euler() - 3 * A(2).log() - pi / 2
    tail = kernel_tail(two_a)
    gram = [two_a / (2 * k + 1) for k in range(m)]
    log2 = A(2).log()
    assert log2 < A(two_a)
    assert A(3).log() > A(two_a)
    prime_v = log2 / A(a)
    prime_weight = 2 * log2 / A(2).sqrt()

    qmat = [[A(0) for _ in range(m)] for _ in range(m)]
    for k in range(m):
        for j in range(k, m):
            if (k + j) % 2:
                continue
            f = overlaps[k][j]
            gkj = gram[k] if k == j else Q(0)
            h = [Q(0)] * len(f)
            a_power = Q(1)
            for p in range(1, len(f)):
                h[p] = -f[p] * a_power
                a_power /= a
            i1 = sum((h[p] * powers[p] / p for p in range(1, len(h))), Q(0)) / 2
            i2 = sum((h[p] * moments[p] for p in range(1, len(h))), Q(0))
            hb = sum((abs(h[p]) * powers[p + 1] / (p + 1)
                      for p in range(1, len(h))), Q(0))
            err_rad = (2 * remainder_scale * A(hb)).upper()
            entry = (psi14 * A(gkj) + 2 * (A(i1) + A(i2))
                     + arb(0, err_rad) + 2 * A(gkj) * tail
                     - pi.log() * A(gkj))
            fv = A(0)
            for c in reversed(f):
                fv = fv * prime_v + A(c)
            entry -= prime_weight * A(a) * fv
            qmat[k][j] = qmat[j][k] = entry

    pole = [2 * A(a) * spherical_i(k, a / 2) for k in range(m)]
    for k in range(m):
        for j in range(m):
            if (k + j) % 2 == 0:
                qmat[k][j] += pole[k] * pole[j] * ((-1)**j + (-1)**k)
    return qmat, gram


def interval_cholesky(qmat, gram, beta=Q(313, 10_000_000)):
    m = len(qmat)
    chol = [[A(0) for _ in range(m)] for _ in range(m)]
    pivot_lowers = []
    for j in range(m):
        pivot = qmat[j][j] - A(beta * gram[j])
        for k in range(j):
            pivot -= chol[j][k] * chol[j][k]
        if not pivot > A(0):
            raise ArithmeticError(f"pivot {j} not proved positive: {pivot}")
        pivot_lowers.append(pivot.lower())
        chol[j][j] = pivot.sqrt()
        for i in range(j + 1, m):
            t = qmat[i][j]
            for k in range(j):
                t -= chol[i][k] * chol[j][k]
            chol[i][j] = t / chol[j][j]
    return pivot_lowers


def class_error_bound():
    """Independent Arb evaluation of F4's closed-form error majorant."""
    a = Q(7, 16)
    m = 48
    cutoff = Q(50)
    tail_mass = Q(1, 10**15)
    lambda_cert = Q(313, 10_000_000)
    pi = arb.pi()

    # F4's displayed Bessel-cut sufficient condition.
    if not A(a * cutoff) < A(Q(9 * (2 * m + 1), 10)) / arb.const_e():
        raise ArithmeticError("Arb did not prove the F4 cut condition")

    psi14 = -arb.const_euler() - pi / 2 - 3 * A(2).log()
    kappa0 = abs(psi14 - pi.log())
    c_pr = 2 * A(2).log() / A(2).sqrt()
    require_lt(kappa0 + 8 + c_pr, Q(15), "c0")
    require_lt(kappa0 + c_pr, Q(7), "c_minus")

    # Closed-form majorant for T2: split min(1, A_z (ar)^(-5/3))
    # at equality.  Landau's constant is conservatively replaced by 1.
    c = A(15) + A(5).log() / 2
    a_z = pi * m * m / 2
    r0 = (A(Q(3, 5)) * a_z.log()).exp() / A(a)
    if not A(cutoff) < r0:
        raise ArithmeticError("T2 branch crossing is below the cutoff")

    def primitive(r):
        y = c + r.log()
        return r * (y * y - 2 * y + 2)

    low_piece = primitive(r0) - primitive(A(cutoff))
    exponent = A(Q(2, 3))
    y0 = c + r0.log()
    tail_piece = r0 * (
        y0 * y0 / exponent
        + 2 * y0 / (exponent * exponent)
        + 2 / (exponent * exponent * exponent)
    )
    t2 = 2 * A(a) / pi * (low_piece + tail_piece)

    z = a * cutoff
    geometric_ratio = z * z / ((2 * m + 1) * (2 * m + 3))
    if not geometric_ratio < 1:
        raise ArithmeticError("Bessel-tail series ratio is not below one")
    odd_double_factorial = 1
    for k in range(1, 2 * m + 2, 2):
        odd_double_factorial *= k
    first_tail_term = ((2 * m + 1) * z ** (2 * m)
                       / odd_double_factorial**2)
    b_star = first_tail_term / (1 - geometric_ratio)
    capture_beta = (2 * A(a) * A(b_star)).sqrt()
    epsilon = A(tail_mass).sqrt() + (A(cutoff) / pi).sqrt() * capture_beta

    pole_delta = (
        2 * (2 * A(a)).sqrt() * (A(a) / 2).exp()
        * A((a / 2) ** m) / factorial(m)
    )
    omega_cutoff = c + A(cutoff).log()
    sinh_a = (A(a).exp() - (-A(a)).exp()) / 2
    error = 2 * (
        t2.sqrt() * epsilon
        + omega_cutoff * (A(cutoff) / pi).sqrt()
        * capture_beta * epsilon
        + (2 * sinh_a).sqrt() * pole_delta * epsilon
    ) + (7 + pole_delta * pole_delta / 2) * epsilon * epsilon
    lower = A(lambda_cert) * (1 - epsilon * epsilon) - error

    require_lt(t2.sqrt(), Q(159237, 500), "sqrt(T2)")
    require_lt(capture_beta, Q(357, 50_000_000_000_000), "capture beta")
    require_lt(epsilon, Q(317, 10_000_000_000), "epsilon")
    require_lt(pole_delta, Q(39, 10**94), "pole projection delta")
    require_gt(lower, Q(11139, 10**9), "restricted-class lower bound")
    return t2.sqrt(), capture_beta, epsilon, pole_delta, lower


_WITNESS = {
    0: "0.65232833448355803706776267482523357",
    2: "-1.4186875217102238423816095868074176",
    4: "1.3851582340132392648510269378955254",
    6: "-1.0051788971195944548648788680647068",
    8: "0.58028817023475974477121015779510872",
    10: "-0.27377264589814093446693662376743423",
    12: "0.10725958959755578877304599656518492",
    14: "-0.035315712438526000357543171158159492",
    16: "0.0098706373620027180676349103289012549",
    18: "-0.0023629324862985554215833023491156143",
    20: "0.00048846852098389556727191085420220129",
    22: "-0.00008785800251582385646579672661454081",
    24: "0.000013846113635082742455114255197255555",
    26: "-0.0000019244227389602900083895911760910136",
    28: "0.00000023731246900664426015967255425923963",
}


def class_witness():
    """Exact moments plus an Arb sinc remainder prove class nonvacuity."""
    a = Q(7, 16)
    cutoff = Q(50)
    series_degree = 80
    max_degree = max(_WITNESS)
    legendre = legendre_polynomials(max_degree + 1)
    polynomial = [Q(0)] * (max_degree + 1)
    for degree, text in _WITNESS.items():
        coefficient = decimal_rational(text)
        for power, legendre_coefficient in enumerate(legendre[degree]):
            polynomial[power] += coefficient * legendre_coefficient / a**power

    def moment(power):
        total = Q(0)
        for degree, coefficient in enumerate(polynomial):
            exponent = degree + power
            if exponent % 2 == 0:
                total += coefficient * 2 * a**(exponent + 1) / (exponent + 1)
        return total

    norm_squared = Q(0)
    for i, ci in enumerate(polynomial):
        for j, cj in enumerate(polynomial):
            exponent = i + j
            if exponent % 2 == 0:
                norm_squared += ci * cj * 2 * a**(exponent + 1) / (exponent + 1)
    if not norm_squared > 0:
        raise ArithmeticError("exact witness norm is not positive")

    moments = [moment(power) for power in range(2 * series_degree + 1)]
    sinc_integral = Q(0)
    for n in range(series_degree + 1):
        difference_moment = sum((
            (-1)**j * comb(2 * n, j)
            * moments[2 * n - j] * moments[j]
            for j in range(2 * n + 1)
        ), Q(0))
        term = difference_moment * cutoff**(2 * n) / factorial(2 * n + 1)
        sinc_integral += term if n % 2 == 0 else -term

    pi = arb.pi()
    band_series = A(cutoff * sinc_integral) / pi
    zmax = 2 * a * cutoff
    if not zmax * zmax < (2 * series_degree + 4) * (2 * series_degree + 5):
        raise ArithmeticError("sinc remainder terms are not decreasing")
    relative_remainder = (
        2 * A(a) * A(cutoff) / pi
        * A(zmax**(2 * series_degree + 2))
        / factorial(2 * series_degree + 3)
    )
    tail_upper = 1 - band_series / A(norm_squared) + relative_remainder
    require_lt(tail_upper, Q(3, 10**17), "explicit witness Fourier tail")
    return norm_squared, relative_remainder, tail_upper


if __name__ == "__main__":
    started = time()
    matrix, gram = assemble()
    print("assembly seconds", time() - started)
    started = time()
    pivots = interval_cholesky(matrix, gram)
    print("cholesky seconds", time() - started)
    print("ARBITRARY-PRECISION BALL CERTIFIED: lambda_48 > 3.13e-5")
    print("smallest raw pivot lower", min(pivots).str(25))
    print("last pivot lower", pivots[-1].str(25))
    print("Q00", matrix[0][0].str(25, radius=True))
    print("Q47,47", matrix[47][47].str(25, radius=True))
    sqrt_t2, capture, epsilon, pole_delta, class_lower = class_error_bound()
    print("sqrt(T2)", sqrt_t2.str(25, radius=True))
    print("capture beta", capture.str(25, radius=True))
    print("epsilon", epsilon.str(25, radius=True))
    print("pole projection delta", pole_delta.str(18, radius=True))
    print("ARBITRARY-PRECISION BALL CERTIFIED: inf_C Q_L > 1.1139e-5")
    print("class lower", class_lower.str(25, radius=True))
    norm_squared, sinc_remainder, witness_tail = class_witness()
    print("witness norm^2", A(norm_squared).str(25, radius=True))
    print("sinc remainder", sinc_remainder.str(18, radius=True))
    print("ARBITRARY-PRECISION BALL CERTIFIED: witness tail < 3e-17")
    print("witness tail", witness_tail.str(25, radius=True))
