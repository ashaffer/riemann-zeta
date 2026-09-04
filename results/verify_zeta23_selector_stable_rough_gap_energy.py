#!/usr/bin/env python3
"""Exact exponent replay for the selector-stable rough-gap energy lemma."""

from fractions import Fraction as F


d = F(5, 9)
e = F(1, 1000)
L = d + e
m = 2 * L / 3
n = L / 3
q = L
eta_star = 1 - 5 * L / 3

theta = F(797, 5000)
beta = F(799, 5000)
h_block = F(8, 33)


def type_ii_nodes(h: F) -> dict[str, F]:
    """Exponent nodes in Matomaki Lemma 5.4's fourth-power bracket."""
    hmnq_over_x = h + m + n + q - 1
    outer = max(hmnq_over_x, n)
    q_plus_n2 = max(q, 2 * n)
    mq_square = 2 * (m + q)
    inner_one = m + q + outer + q_plus_n2
    inner_two = h + 3 * (m + n) + q - 1
    bracket = max(mq_square, outer + max(inner_one, inner_two))
    total = F(1, 2) + h / 2 + bracket / 4
    return {
        "hmnq_over_x": hmnq_over_x,
        "outer": outer,
        "q_plus_n2": q_plus_n2,
        "mq_square": mq_square,
        "inner_one": inner_one,
        "inner_two": inner_two,
        "bracket": bracket,
        "total": total,
    }


def phi(g: F, cap: F) -> F:
    return g * min(g, cap)


assert L == F(5009, 9000)
assert eta_star == F(391, 5400)
assert d / F(8, 33) == F(55, 24) > 2
assert m > 0 and n > 0 and d - m > 0
assert d - m + e == n

nodes = type_ii_nodes(eta_star)
assert nodes["hmnq_over_x"] == n
assert nodes["q_plus_n2"] == L
assert nodes["mq_square"] == F(10, 3) * L
assert nodes["inner_one"] == 3 * L
assert nodes["inner_two"] == F(7, 3) * L
assert nodes["bracket"] == F(10, 3) * L
assert nodes["total"] == 1

# Any h below the endpoint has a genuine saving (eta_star-h)/2.
probe_delta = F(1, 10000)
probe = type_ii_nodes(eta_star - probe_delta)
assert probe["total"] == 1 - probe_delta / 2

# The moving split n=h+2L-1 leaves the (MQ)^2 node exactly at exponent 1.
h = eta_star - probe_delta
n_bad = h + 2 * L - 1
m_bad = L - n_bad
moving_split_total = F(1, 2) + h / 2 + 2 * (m_bad + L) / 4
assert moving_split_total == 1

rho_variance = theta - eta_star
rho_boundary = 2 * theta - h_block
rho_selector = max(eta_star, rho_variance, rho_boundary)
stage_saving = (beta - rho_selector) / 2

assert theta > 2 * eta_star
assert rho_variance == F(1468, 16875)
assert rho_boundary == F(6301, 82500)
assert rho_selector == rho_variance
assert stage_saving == F(9829, 270000)

# Exhaustively replay superadditivity on a rational grid.  The report also
# gives the two-case algebraic proof; this is only a regression tripwire.
cap = F(1)
for ia in range(101):
    for ib in range(101):
        a, b = F(ia, 25), F(ib, 25)
        assert phi(a, cap) + phi(b, cap) <= phi(a + b, cap)

# Naive truncated squares and full boundary-gap ledgers are not selector
# stable.  A 3/2-long gap is absent from the cap-1 truncated ledger, but its
# two 3/4 refinements contribute; five blocks can also count one full gap
# five times if each imports both boundary gaps.
truncated_square = lambda g: g * g if g <= cap else F(0)
assert truncated_square(F(3, 2)) < 2 * truncated_square(F(3, 4))
assert 5 * F(3, 2) ** 2 > F(3, 2) ** 2

print(f"d={d} e={e} L={L}")
print(f"balanced split m={m} n={n} q<={q}")
print(f"eta_star={eta_star} ({float(eta_star):.12f})")
print(f"rough cutoff endpoint ratio d/bmax={d / F(8, 33)}")
print(f"Type-II endpoint bracket={nodes['bracket']}, total={nodes['total']}")
print("moving split n=h+2L-1 total=1 (no power saving): CONFIRMED")
print(f"theta-eta_star={rho_variance} ({float(rho_variance):.12f})")
print(f"boundary rho=2theta-h={rho_boundary} ({float(rho_boundary):.12f})")
print(f"selector rho={rho_selector} ({float(rho_selector):.12f})")
print(f"normalized stage saving={stage_saving} ({float(stage_saving):.12f})")
print("phi_G(g)=g min(g,G) superadditivity grid: PASS")
print("naive truncated monotonicity / full-boundary aggregation: FAIL (as claimed)")
