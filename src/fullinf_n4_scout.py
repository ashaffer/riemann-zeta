"""Fast parameter scout for the n=4 unrestricted certificate (NOT a certificate).

The intended endpoint is L=749/250, so a=L/4=749/1000 and the prime-power
sum contains n=2,3,4.  This program does *not* assemble or certify the clipped
Legendre matrix.  It only does three inexpensive pieces of reconnaissance:

* a floating-point scan of the oscillatory symbol (explicitly nonrigorous);
* an Arb interval bridge proving the proposed exterior floor on [110,160],
  conditional only on the analytic monotonicity of Re psi used by the existing
  full-space certificates for the tail [160,infinity);
* Arb evaluation of the exact Legendre-tail and pole-residual formulas.

The scan suggests why S=110 is useful.  The interval bridge and tail constants
are rigorous, but this scout is not a positivity proof by itself.  The
separate completed Arb/Cholesky proof is
``fullinf_unrestricted_n4_certificate.py``.
"""

from math import factorial, prod

import numpy as np
from flint import acb, arb, ctx, fmpq
from scipy.optimize import minimize_scalar
from scipy.special import digamma


PRECISION = 128
L = fmpq(749, 250)
A_HALF_WIDTH = fmpq(749, 1000)
S = 110
ENVELOPE_START = 160
PANEL_DENOMINATOR = 1000  # exact panels of width 1/1000

ctx.prec = PRECISION
ctx.threads = 1

PI = arb.pi()
LOG2 = arb(2).log()
LOG3 = arb(3).log()
PRIME_2 = arb(2).sqrt() * LOG2
PRIME_3 = 2 * LOG3 / arb(3).sqrt()
PRIME_4 = LOG2
PRIME_AMPLITUDE = PRIME_2 + PRIME_3 + PRIME_4
I = acb(0, 1)


def omega_ball(r):
    """Arb enclosure of the exact n=2,3,4 symbol on a real ball r."""
    plus = (acb(fmpq(1, 4)) + I * r / 2).digamma()
    minus = (acb(fmpq(1, 4)) - I * r / 2).digamma()
    return (
        (plus + minus) / 2
        - PI.log()
        - PRIME_2 * (r * LOG2).cos()
        - PRIME_3 * (r * LOG3).cos()
        - PRIME_4 * (2 * r * LOG2).cos()
    ).real


CRUDE_FLOOR_AT_ENVELOPE_START = (
    acb(fmpq(1, 4), arb(ENVELOPE_START) / 2).digamma().real
    - PI.log()
    - PRIME_AMPLITUDE
)
ALPHA = arb(fmpq(29, 100))  # 0.29, below the crude floor at r=160


def support_checks():
    half_support = L / 2
    if not arb(4).log() < arb(half_support):
        raise ArithmeticError("failed to prove n=4 is present")
    if not arb(5).log() > arb(half_support):
        raise ArithmeticError("failed to prove every n>=5 is absent")


def rigorous_exterior_bridge():
    """Prove Omega(r)>=0.29 on [110,160] by exact Arb panels.

    Evenness gives the negative half-line.  For |r|>=160, the analytic
    monotonicity of Re psi and |cos|<=1 give the same lower bound ALPHA.
    """
    if not CRUDE_FLOOR_AT_ENVELOPE_START > ALPHA:
        raise ArithmeticError("crude envelope at r=160 does not exceed alpha")
    count = (ENVELOPE_START - S) * PANEL_DENOMINATOR
    denominator = 2 * PANEL_DENOMINATOR
    worst = None
    worst_panel = None
    for k in range(count):
        numerator = 2 * S * PANEL_DENOMINATOR + 2 * k + 1
        r = arb(fmpq(numerator, denominator), fmpq(1, denominator))
        gap = omega_ball(r) - ALPHA
        if not gap > 0:
            raise ArithmeticError(f"panel {k} did not prove Omega-alpha > 0")
        if worst is None or gap.lower() < worst.lower():
            worst = gap
            worst_panel = k
    return worst_panel, worst


def scanned_last_negative_minimum():
    """NONRIGOROUS dense double-precision scan used only for scouting."""
    log2 = np.log(2.0)
    log3 = np.log(3.0)
    p2 = np.sqrt(2.0) * log2
    p3 = 2.0 * log3 / np.sqrt(3.0)
    p4 = log2

    def omega_float(r):
        return (
            np.real(digamma(0.25 + 0.5j * r))
            - np.log(np.pi)
            - p2 * np.cos(r * log2)
            - p3 * np.cos(r * log3)
            - p4 * np.cos(2 * r * log2)
        )

    grid = np.linspace(0.0, ENVELOPE_START, 240_001)
    values = omega_float(grid)
    indices = np.where(
        (values[1:-1] < values[:-2]) & (values[1:-1] < values[2:])
    )[0] + 1
    negative = []
    for k in indices:
        result = minimize_scalar(
            omega_float,
            bounds=(grid[k - 1], grid[k + 1]),
            method="bounded",
        )
        if result.fun < 0:
            negative.append((result.x, result.fun))
    return negative[-1]


def transfer_constants(m):
    """Rigorous Arb values entering the finite-to-full transfer."""
    a = A_HALF_WIDTH
    z = a * S
    q = z * z / ((2 * m + 1) * (2 * m + 3))
    odd_double_factorial = prod(range(1, 2 * m + 2, 2))
    first = (2 * m + 1) * z ** (2 * m) / odd_double_factorial**2
    b_star = first / (1 - q)
    rho = 2 * arb(a) * S / PI * arb(b_star)
    delta = (
        (2 * arb(a)).sqrt()
        * (arb(a) / 2).exp()
        * arb((a / 2) ** m)
        / factorial(m)
    )
    kappa = arb.const_euler() + PI / 2 + 3 * LOG2 + PI.log()
    multiplier_bound = kappa + PRIME_AMPLITUDE + ALPHA
    pole_norm = (arb(2) * arb(a).sinh()).sqrt()
    d = ALPHA - multiplier_bound * rho - 2 * delta * delta
    c = multiplier_bound * rho.sqrt() + 2 * pole_norm * delta
    return q, b_star, rho, delta, multiplier_bound, d, c


if __name__ == "__main__":
    support_checks()
    print("NONRIGOROUS scan: last negative local minimum", scanned_last_negative_minimum())
    panel, gap = rigorous_exterior_bridge()
    print("RIGOROUS Arb alpha", ALPHA.str(25, radius=True))
    print("RIGOROUS Arb crude floor at r=160", CRUDE_FLOOR_AT_ENVELOPE_START.str(25, radius=True))
    print("RIGOROUS Arb bridge: all 50000 panels pass")
    print("worst panel", panel, "gap", gap.str(20, radius=True))
    for m in (130, 131, 132, 133, 134):
        q, b_star, rho, delta, bound, d, c = transfer_constants(m)
        print(
            f"m={m}: q={arb(q).str(8)}, rho={rho.str(8)}, "
            f"delta={delta.str(5)}, M={bound.str(8)}, "
            f"d={d.str(8)}, c={c.str(8)}"
        )
    print("SCOUT ONLY: run fullinf_unrestricted_n4_certificate.py for the proof")
