"""Arb certificate for a two-crossing S_2 profile at T=152.7.

It encloses S_2(P,T) at P=0, 0.0794535, and 0.12 using the exact
divided-Turan cosine transform.  Positive, negative, positive signs at these
ordered P values rigorously falsify an at-most-one-crossing proposal.
"""

from flint import acb, arb, ctx


ctx.dps = 100

T = arb("152.7")
P_VALUES = (arb(0), arb("0.0794535"), arb("0.12"))
EPS = arb("1e-8")
CAUCHY_RADIUS = arb("0.1")
W = arb(300)
# Near-optimal gamma-recurrence depth for (W-T)/4 = 36.825.  Taking N much
# larger makes Gamma(N+1/4)/v^N grow again and weakens the tail enclosure.
N = 65

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


def divided_turan(x) -> acb:
    return (ZT * ZT - z_transform(T + x) * z_transform(T - x)) / (x * x)


def z_upper(y: arb) -> arb:
    t = y / 2
    v = y / 4
    return (
        (arb(N) + arb("0.25")).gamma()
        * (t * t + arb("0.25"))
        * (t + 3)
        / (8 * PI ** arb("0.25") * v**N)
    )


box = acb(arb(0, CAUCHY_RADIUS), arb(0, CAUCHY_RADIUS))
g_box = z_transform(T + box) * z_transform(T - box)
origin_bound = EPS * abs(g_box).upper() / (CAUCHY_RADIUS - EPS) ** 2
tail_bound = (
    z_upper(W + T)
    * z_upper(W - T)
    / W**2
    * (W - T)
    / (N - 4)
)
common_error = 2 / PI * (origin_bound + tail_bound)


def constant_tail(p: arb) -> arb:
    if p == 0:
        return 1 / W
    return (p * W).cos() / W - p * (PI / 2 - (p * W).si())


for p in P_VALUES:
    def integrand(x, _analytic):
        return (p * x).cos() * divided_turan(x)

    middle = acb.integral(
        integrand,
        EPS,
        W,
        abs_tol=arb("1e-63"),
        eval_limit=3_000_000,
        depth_limit=45,
    )
    core = (middle + ZT * ZT * constant_tail(p)) * 2 / PI
    lower = core.real.lower() - common_error.upper()
    upper = core.real.upper() + common_error.upper()
    print("P:", p)
    print("core:", core)
    print("enclosure: [", lower, ",", upper, "]")
    print("CERTIFIED_POSITIVE:", bool(lower > 0))
    print("CERTIFIED_NEGATIVE:", bool(upper < 0))

print("origin absolute bound:", origin_bound)
print("product-tail absolute bound:", tail_bound)
