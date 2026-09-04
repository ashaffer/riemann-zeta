"""Exact phase-jet and affine-height identities for the symmetric QP cusp.

The module records algebraic identities only.  In particular, it does not
assert that phase jets with different labels are orthogonal in the physical
completion norm.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def _fraction(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def critical_action_jet(
    C: int,
    S: int,
    p: int,
    d: int,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
) -> dict[str, Fraction]:
    """Return the exact completion-sum action jet at ``t0=(p+d)/(2p)``.

    The physical phase is

    ``F(S,a)=C*h/a+C*k/(S-a)-m*a``.

    The supplied mode is required to be stationary at
    ``a0=S*(p+d)/(2p)``.  Let ``J(S)`` be the critical value obtained by
    continuing this regular critical point as the completion sum varies,
    with ``C,h,k,m`` fixed.  The return value contains ``J,J',J'',J'''`` at
    the supplied ``S``.  The fourth derivative is also returned because it
    resolves the order-two/three mirror up to physical reflection.  A linear
    outer completion character changes only ``J`` and ``J'``.
    """

    if min(C, S, p) <= 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("require C,S,p>0, |d|<p, and gcd(p,d)=1")
    h, k, m = map(_fraction, (h, k, m))
    r, s = p + d, p - d
    a = Fraction(S * r, 2 * p)
    b = Fraction(S * s, 2 * p)
    left_slope = Fraction(C) * h / a**2
    right_slope = Fraction(C) * k / b**2
    stationary_integer = right_slope - left_slope
    if stationary_integer != m:
        raise ValueError("the supplied mode is not stationary at t0")

    left_cubic = h / a**3
    right_cubic = k / b**3
    curvature_density = left_cubic + right_cubic
    if curvature_density == 0:
        raise ValueError("the critical point is a cubic fold, not a regular action")

    action = Fraction(C) * h / a + Fraction(C) * k / b - m * a
    first = -Fraction(C) * k / b**2
    second = (
        2 * Fraction(C) * left_cubic * right_cubic / curvature_density
    )
    third = (
        -6
        * Fraction(C)
        * left_cubic
        * right_cubic
        * (right_cubic**2 / a + left_cubic**2 / b)
        / curvature_density**3
    )
    fourth = (
        6
        * Fraction(C)
        * left_cubic
        * right_cubic
        * (
            4 * left_cubic**4 * a**2
            - 5 * left_cubic**3 * right_cubic * a**2
            + 18 * left_cubic**2 * right_cubic**2 * a * b
            - 5 * left_cubic * right_cubic**3 * b**2
            + 4 * right_cubic**4 * b**2
        )
        / (a**2 * b**2 * curvature_density**5)
    )

    alpha0 = Fraction(4 * C * p, S * r)
    beta0 = -Fraction(4 * C * p * d, S * s * s)
    assert action == h * alpha0 + k * beta0
    return {
        "a": a,
        "b": b,
        "t0": Fraction(r, 2 * p),
        "alpha0": alpha0,
        "beta0": beta0,
        "action": action,
        "first": first,
        "second": second,
        "third": third,
        "fourth": fourth,
        "left_cubic": left_cubic,
        "right_cubic": right_cubic,
        "curvature_density": curvature_density,
        "stationary_integer": stationary_integer,
    }


def nonlinear_action_quotient_rigidity(
    C: int,
    S: int,
    p: int,
    d: int,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
) -> dict[str, Fraction]:
    """Return the exact ``J'',J''',J''''`` reflection-rigidity invariants.

    Put ``t=a/S`` and ``u=da/dS=K/(H+K)``.  For ``J''!=0`` define

    ``A=-S*J'''/(3J'')`` and ``B=S^2*J''''/(3J'')``.

    Then

    ``A=1+(u-t)^2/(t(1-t))``

    and, off ``m=0``,

    ``R=(4A^2-B)/(5(A-1))=u(1-u)/(t(1-t))``.

    The map ``(t,u)->(A-1,R)`` has Jacobian

    ``(t-u)^2/(t^3(1-t)^3)``.

    Hence the nonlinear derivatives of orders two through four recover
    ``(t,u)`` up to ``(t,u)->(1-t,1-u)``; conditioning degenerates only at
    the zero-Poisson locus ``u=t`` inside a compact collar.
    """

    data = critical_action_jet(C, S, p, d, h, k, m)
    if data["second"] == 0:
        raise ValueError("endpoint jets have no nonlinear quotient")
    t = data["t0"]
    u = data["right_cubic"] / data["curvature_density"]
    A = -Fraction(S) * data["third"] / (3 * data["second"])
    B = Fraction(S * S) * data["fourth"] / (3 * data["second"])
    gap = A - 1
    expected_gap = (u - t) ** 2 / (t * (1 - t))
    assert gap == expected_gap
    if gap == 0:
        raise ValueError("the zero-Poisson quotient is noninjective")
    R = (4 * A * A - B) / (5 * gap)
    expected_R = u * (1 - u) / (t * (1 - t))
    jacobian = (t - u) ** 2 / (t**3 * (1 - t) ** 3)
    assert R == expected_R
    assert jacobian == gap / (t * t * (1 - t) ** 2)
    return {
        "t": t,
        "u": u,
        "A": A,
        "B": B,
        "gap": gap,
        "R": R,
        "jacobian": jacobian,
        "reflected_t": 1 - t,
        "reflected_u": 1 - u,
    }


def recover_regular_packet_from_action_jet(
    C: int,
    S: int,
    first: int | Fraction,
    second: int | Fraction,
    third: int | Fraction,
) -> dict[str, Fraction]:
    """Invert a nondegenerate ``(J',J'',J''')`` completion-action jet.

    Write

    ``q=-J'/C``, ``R2=J''/(2C)``, ``c=R2/q``, and
    ``R=-J'''/(3J'')``.  Then the right saddle coordinate is exactly

    ``b=(R*S-1)/(R+c^2*S-2c)``.

    The denominator vanishes precisely on the zero-Poisson branch ``m=0``.
    Outside the endpoint, fold, and zero-Poisson degeneracies, the first
    three action derivatives therefore recover ``a,b,h,k,m`` uniquely.
    """

    if min(C, S) <= 0:
        raise ValueError("require C,S>0")
    first, second, third = map(_fraction, (first, second, third))
    if first == 0 or second == 0:
        raise ValueError("endpoint/one-inverse jets are degenerate")
    q = -first / C
    R2 = second / (2 * C)
    c = R2 / q
    R = -third / (3 * second)
    denominator = R + c * c * S - 2 * c
    if denominator == 0:
        raise ValueError("the zero-Poisson action jet is not injective")
    b = (R * S - 1) / denominator
    a = Fraction(S) - b
    if a <= 0 or b <= 0:
        raise ValueError("the recovered critical point is not interior")
    right_cubic = q / b
    if right_cubic == R2:
        raise ValueError("the recovered jet is singular")
    left_cubic = R2 * right_cubic / (right_cubic - R2)
    k = q * b * b
    h = left_cubic * a**3
    m = Fraction(C) * (q - h / a**2)
    return {
        "a": a,
        "b": b,
        "h": h,
        "k": k,
        "m": m,
        "q": q,
        "R2": R2,
        "c": c,
        "R": R,
        "inverse_denominator": denominator,
    }


def action_jet_inverse_determinant(
    C: int,
    S: int,
    p: int,
    d: int,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
) -> dict[str, Fraction]:
    """Return the exact factor controlling action-jet invertibility.

    For a regular nonendpoint saddle, the rational inverse denominator is

    ``R+c^2*S-2c=(1-c*S)^2/a``

    and also

    ``m^2/(C^2*a*b^2*(H+K)^2)``,

    where ``H=h/a^3`` and ``K=k/b^3``.  It vanishes if and only if ``m=0``.
    """

    data = critical_action_jet(C, S, p, d, h, k, m)
    if data["first"] == 0 or data["second"] == 0:
        raise ValueError("the determinant formula requires a nonendpoint jet")
    q = -data["first"] / C
    R2 = data["second"] / (2 * C)
    c = R2 / q
    R = -data["third"] / (3 * data["second"])
    direct = R + c * c * S - 2 * c
    square = (1 - c * S) ** 2 / data["a"]
    poisson = (
        _fraction(m) ** 2
        / (
            Fraction(C) ** 2
            * data["a"]
            * data["b"] ** 2
            * data["curvature_density"] ** 2
        )
    )
    assert direct == square == poisson
    return {
        "c": c,
        "R": R,
        "direct": direct,
        "square": square,
        "poisson": poisson,
    }


def second_third_jet_mirror(
    C: int,
    S: int,
    p: int,
    d: int,
    h: int | Fraction,
    k: int | Fraction,
) -> dict[str, Fraction]:
    """Construct the exact nontrivial collision after discarding ``J'``.

    At a fixed saddle position put ``H=h/a^3``, ``K=k/b^3`` and
    ``rho=K/(H+K)``.  The ratio ``-J'''/(3J'')`` determines only
    ``(rho-t0)^2``.  Reflecting ``rho`` to ``2*t0-rho`` and rescaling the
    total curvature to preserve ``J''`` gives a generally different rational
    mode with exactly the same second and third action derivatives.

    This is a no-go for a theorem that keeps only nonlinear orders two and
    three while allowing an arbitrary independent affine slope per packet.
    """

    if min(C, S, p) <= 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("invalid physical parameters")
    h, k = map(_fraction, (h, k))
    r, s = p + d, p - d
    a = Fraction(S * r, 2 * p)
    b = Fraction(S * s, 2 * p)
    H = h / a**3
    K = k / b**3
    T = H + K
    if H == 0 or K == 0 or T == 0:
        raise ValueError("endpoint and fold modes have no regular mirror")
    rho = K / T
    t0 = a / S
    mirror_rho = 2 * t0 - rho
    if mirror_rho in (0, 1):
        raise ValueError("the mirror lands on an endpoint")
    mirror_T = T * rho * (1 - rho) / (
        mirror_rho * (1 - mirror_rho)
    )
    mirror_H = mirror_T * (1 - mirror_rho)
    mirror_K = mirror_T * mirror_rho
    mirror_h = mirror_H * a**3
    mirror_k = mirror_K * b**3
    mirror_m = Fraction(C) * (mirror_k / b**2 - mirror_h / a**2)
    original_m = Fraction(C) * (k / b**2 - h / a**2)
    original = critical_action_jet(C, S, p, d, h, k, original_m)
    mirror = critical_action_jet(
        C, S, p, d, mirror_h, mirror_k, mirror_m
    )
    assert original["second"] == mirror["second"]
    assert original["third"] == mirror["third"]
    return {
        "h": h,
        "k": k,
        "m": original_m,
        "mirror_h": mirror_h,
        "mirror_k": mirror_k,
        "mirror_m": mirror_m,
        "first": original["first"],
        "mirror_first": mirror["first"],
        "second": original["second"],
        "third": original["third"],
        "rho": rho,
        "mirror_rho": mirror_rho,
    }


def scaled_cusp_affine_defects(
    Q: int, y: int, g: int, p: int, d: int
) -> dict[str, Fraction | int]:
    """Identify universal scaled-cusp factors with affine intercept defects.

    Work at ``C=Q^2,S=2Q``.  The physical reciprocal coordinates attached
    to content ``g`` are

    ``a=Q+y``, ``V=Q-y+g(p-d)/2``, ``W=Q+y+g(p+d)/2``.

    If ``alpha,beta`` are their intercepts in the line parallel to the
    tangent at ``t0=(p+d)/(2p)``, then exactly

    ``alpha-alpha0=j_-/(2(p+d)^2)``,
    ``beta-beta0=j_+/(2(p-d)^2)``.

    In the notation of the scaled-cusp report, ``z=-H`` and ``v=U``.
    Thus ``H=0`` is ``z=0``, while ``j_-=0`` and ``j_+=0`` are respectively
    ``z=-d*v`` and ``z=d*v``.
    """

    if Q <= 0 or p <= abs(d) or d == 0 or gcd(p, abs(d)) != 1:
        raise ValueError("require Q>0, p>|d|>0, and gcd(p,d)=1")
    ell = p * p - d * d
    U = 2 * d * y - g * ell
    content_offset = 2 * d * d * Q - g * p * ell
    H = content_offset - 2 * p * U
    j_minus = H - d * U
    j_plus = H + d * U
    r, s = p + d, p - d
    a = Q + y
    left_coordinate = Fraction(2 * (Q - y) + g * (p - d), 2)
    right_coordinate = Fraction(2 * (Q + y) + g * (p + d), 2)
    alpha = left_coordinate + Fraction(p * p * a, r * r)
    beta = right_coordinate - Fraction(p * p * a, s * s)
    alpha0 = Fraction(2 * Q * p, r)
    beta0 = -Fraction(2 * Q * p * d, s * s)
    delta_alpha = alpha - alpha0
    delta_beta = beta - beta0
    assert delta_alpha == Fraction(j_minus, 2 * r * r)
    assert delta_beta == Fraction(j_plus, 2 * s * s)
    return {
        "ell": ell,
        "U": U,
        "content_offset": content_offset,
        "H": H,
        "j_minus": j_minus,
        "j_plus": j_plus,
        "z": -H,
        "scaled_v": U,
        "alpha": alpha,
        "beta": beta,
        "alpha0": alpha0,
        "beta0": beta0,
        "delta_alpha": delta_alpha,
        "delta_beta": delta_beta,
    }


def stationary_affine_height_defect(
    p: int,
    d: int,
    h: int | Fraction,
    k: int | Fraction,
    m: int | Fraction,
    H: int,
    U: int,
) -> Fraction:
    """Return the exact physical-minus-tangent stationary action height.

    At the symmetric centre stationarity is

    ``m=p^2*(k/(p-d)^2-h/(p+d)^2)``.

    The affine-height defect is both

    ``h*j_-/(2(p+d)^2)+k*j_+/(2(p-d)^2)``

    and

    ``H/2*(h/(p+d)^2+k/(p-d)^2)+d*U*m/(2p^2)``.
    """

    if p <= abs(d) or gcd(p, abs(d)) != 1:
        raise ValueError("require p>|d| and gcd(p,d)=1")
    h, k, m = map(_fraction, (h, k, m))
    r, s = p + d, p - d
    expected_m = p * p * (k / (s * s) - h / (r * r))
    if m != expected_m:
        raise ValueError("the frequency is not stationary at t0")
    j_minus, j_plus = H - d * U, H + d * U
    direct = h * j_minus / (2 * r * r) + k * j_plus / (2 * s * s)
    resolved = (
        Fraction(H, 2) * (h / (r * r) + k / (s * s))
        + Fraction(d * U, 2 * p * p) * m
    )
    assert direct == resolved
    return direct


def distinguished_affine_height_probes(
    Q: int, y: int, g: int, p: int, d: int
) -> dict[str, Fraction | int | bool]:
    """Evaluate the four distinguished stationary normals on one packet.

    The left one-inverse, right one-inverse, zero-Poisson, and cubic-fold
    normals have height defects

    ``j_-/2, j_+/2, H, d*(H-p*U)``.

    The last quantity exposes a new fold-height invariant.  It is not one of
    the three already peeled normal-crossing axes.
    """

    data = scaled_cusp_affine_defects(Q, y, g, p, d)
    H, U = int(data["H"]), int(data["U"])
    r, s = p + d, p - d
    left = stationary_affine_height_defect(
        p, d, r * r, 0, -p * p, H, U
    )
    right = stationary_affine_height_defect(
        p, d, 0, s * s, p * p, H, U
    )
    zero = stationary_affine_height_defect(
        p, d, r * r, s * s, 0, H, U
    )
    fold = stationary_affine_height_defect(
        p, d, r**3, -s**3, -2 * p**3, H, U
    )
    fold_invariant = H - p * U
    assert left == Fraction(int(data["j_minus"]), 2)
    assert right == Fraction(int(data["j_plus"]), 2)
    assert zero == H
    assert fold == d * fold_invariant
    return {
        **data,
        "left_probe": left,
        "right_probe": right,
        "zero_probe": zero,
        "fold_probe": fold,
        "fold_invariant": fold_invariant,
        "square_content_forced": H == 0 and U == 0,
    }


def fold_height_zero_parametrization(
    Q: int, y: int, g: int, p: int, d: int
) -> dict[str, Fraction | int]:
    """Resolve the new exact fold-height branch ``H-p*U=0``.

    On this branch, integrality and ``gcd(p,d)=1`` force

    ``p|Q``, ``d|g``, ``U=d*w``, ``n=-p*w``.

    Writing ``M=Q/p`` and ``a=g/d`` gives

    ``a*(p^2-d^2)+3*w=2*d*M``

    and the two exact error factorizations

    ``4e=w*(a*(p-d)^2-w)``,
    ``4f=w*(a*(p+d)^2-w)``.

    This is divisor-major in ``p`` but does not force ``d^2|g``.
    """

    data = distinguished_affine_height_probes(Q, y, g, p, d)
    if data["fold_invariant"] != 0:
        raise ValueError("the point is not on the fold-height branch")
    U = int(data["U"])
    if U % d:
        raise AssertionError("fold height should force d|U")
    if Q % p or g % d:
        raise AssertionError("fold height divisibility failed")
    w, M, a_scale = U // d, Q // p, g // d
    ell = p * p - d * d
    n = p * y - Q * d
    assert n == -p * w
    assert a_scale * ell + 3 * w == 2 * d * M
    left_shift = Fraction(g * (p - d), 2)
    right_shift = Fraction(g * (p + d), 2)
    e = left_shift * (Q + y) - y * y
    f = right_shift * (Q - y) - y * y
    left_formula = Fraction(w * (a_scale * (p - d) ** 2 - w), 4)
    right_formula = Fraction(w * (a_scale * (p + d) ** 2 - w), 4)
    eta = a_scale * (p - d) ** 2 - w
    x = p - d
    divisor_target = 2 * Q + 3 * eta
    divisor_factorization = 2 * x * (a_scale * (p + x) + M)
    assert e == left_formula
    assert f == right_formula
    assert 4 * e == w * eta
    assert divisor_factorization == divisor_target
    return {
        **data,
        "w": w,
        "M": M,
        "a_scale": a_scale,
        "n": n,
        "e": e,
        "f": f,
        "left_formula": left_formula,
        "right_formula": right_formula,
        "eta": eta,
        "x": x,
        "divisor_target": divisor_target,
        "divisor_factorization": divisor_factorization,
        "square_content": g % (d * d) == 0,
    }


def fold_height_branch_exponent_ledger() -> dict[str, Fraction]:
    """Return the energy-core powers closing the fold-height branch.

    On ``|w|<=sqrt(A)``, the relation

    ``a*(p^2-d^2)=2*d*(Q/p)-3*w``

    and ``|a*d*p*w|<=2B`` imply

    ``d << B^(3/4)*Q^(-1/4)``.

    At the worst energy endpoint this is ``D^(23/64)``, below the smallest
    square-root budget ``D^(1/2)``.  The residual primitive floor also makes
    the spacing in ``w`` under ``a->a+1`` much larger than ``sqrt(A)``, so
    there is at most one scale ``a`` for fixed ``(p,d)``.

    On ``|w|>sqrt(A)``, ``eta=4e/w`` has ``O(sqrt(A))`` possible values and
    ``p-d`` divides ``2Q+3eta``.  This gives ``O(sqrt(A)Q^o(1))`` points.
    """

    Q = Fraction(33, 16)
    A_max = Fraction(11, 10)
    B_max = Fraction(7, 6)
    p_floor = Fraction(77, 160)
    low_w_d = 3 * B_max / 4 - Q / 4
    sqrt_A_floor = Fraction(1, 2)
    sqrt_A_ceiling = A_max / 2
    w_spacing = 2 * p_floor
    assert low_w_d == Fraction(23, 64)
    assert sqrt_A_floor - low_w_d == Fraction(9, 64)
    assert w_spacing > sqrt_A_ceiling
    return {
        "Q": Q,
        "A_max": A_max,
        "B_max": B_max,
        "primitive_p_floor": p_floor,
        "low_w_d_count": low_w_d,
        "sqrt_A_floor": sqrt_A_floor,
        "low_w_saving": sqrt_A_floor - low_w_d,
        "w_spacing_floor": w_spacing,
        "sqrt_A_ceiling": sqrt_A_ceiling,
    }


def square_content_from_double_intercept_collision(
    Q: int, y: int, g: int, p: int, d: int
) -> bool:
    """Verify that simultaneous zero intercept defects force ``d^2|g``."""

    data = scaled_cusp_affine_defects(Q, y, g, p, d)
    if data["j_minus"] != 0 or data["j_plus"] != 0:
        return False
    if data["H"] != 0 or data["U"] != 0:
        raise AssertionError("the two intercept equations should give H=U=0")
    if g % (d * d):
        raise AssertionError("the exact cusp should have square content")
    return True
