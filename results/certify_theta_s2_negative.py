"""Rigorous Arb certificate that the actual-theta S_2 tail can be negative.

The certified target is S_{2,T}(0) at T=97.2, using

  S_2 = (2/pi) int_0^inf
          [Z(T)^2-Z(T+x)Z(T-x)]/x^2 dx,
  Z(t) = xi((1-i*t)/2)/4.

The middle integral is enclosed by python-flint/Arb.  The removable origin
is bounded by Cauchy's estimate.  Beyond W, the constant Z(T)^2/x^2 is
integrated exactly and the remaining product is bounded using only gamma
recurrence and the first Euler--Maclaurin formula for zeta.
"""

from flint import acb, arb, ctx


ctx.dps = 80

T = arb("97.2")
EPS = arb("1e-8")
CAUCHY_RADIUS = arb("0.1")
W = arb(200)
N = 40

PI = arb.pi()
I = acb(0, 1)


def xi(s: acb) -> acb:
    return (
        arb("0.5")
        * s
        * (s - 1)
        * ((-s / 2) * PI.log()).exp()
        * (s / 2).gamma()
        * s.zeta()
    )


def z_transform(t) -> acb:
    return xi((1 - I * t) / 2) / 4


ZT = z_transform(T)


def divided_turan(x, _analytic) -> acb:
    return (ZT * ZT - z_transform(T + x) * z_transform(T - x)) / (x * x)


# Rigorous analytic quadrature on the nonsingular middle interval.
middle = acb.integral(
    divided_turan,
    EPS,
    W,
    abs_tol=arb("1e-43"),
    eval_limit=2_000_000,
    depth_limit=40,
)
core = (middle + ZT * ZT / W) * 2 / PI


# Origin bound.  For g(z)=Z(T+z)Z(T-z), g is even and
# (g(0)-g(x))/x^2=-int_0^1(1-t)g''(tx)dt.  An Arb evaluation
# on a square containing |z|<=R supplies M>=max_|z|<=R |g(z)|;
# Cauchy then bounds the omitted integral by eps*M/(R-eps)^2.
box = acb(
    arb(0, CAUCHY_RADIUS),
    arb(0, CAUCHY_RADIUS),
)
g_box = z_transform(T + box) * z_transform(T - box)
M = abs(g_box).upper()
origin_bound = EPS * M / (CAUCHY_RADIUS - EPS) ** 2


def z_upper(y: arb) -> arb:
    """Elementary upper bound for |Z(y)|, valid for positive real y.

    Put t=y/2 and v=y/4.  Euler--Maclaurin gives
    |zeta(1/2+i*t)| <= t+3.  Recurrence and the Euler integral give
    |Gamma(1/4+i*v)| <= Gamma(N+1/4)/v^N.
    """
    t = y / 2
    v = y / 4
    return (
        (arb(N) + arb("0.25")).gamma()
        * (t * t + arb("0.25"))
        * (t + 3)
        / (8 * PI ** arb("0.25") * v**N)
    )


# For x>=W, z_upper(x+T) is decreasing.  The other factor is at most
# z_upper(W-T)*((x-T)/(W-T))^(3-N), and x^-2<=W^-2.
tail_bound = (
    z_upper(W + T)
    * z_upper(W - T)
    / W**2
    * (W - T)
    / (N - 4)
)

total_error = 2 / PI * (origin_bound + tail_bound)
upper = core.real.upper() + total_error.upper()
lower = core.real.lower() - total_error.upper()

print("middle:", middle)
print("core (constant tail included):", core)
print("origin absolute bound:", origin_bound)
print("product-tail absolute bound:", tail_bound)
print("certified S_2 enclosure: [", lower, ",", upper, "]")
print("CERTIFIED_NEGATIVE:", bool(upper < 0))

