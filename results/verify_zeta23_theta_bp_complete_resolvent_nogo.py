"""Independent symbolic/Arb verifier for the complete resolvent no-go."""

from __future__ import annotations

import sys
from pathlib import Path

from flint import arb, ctx
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from theta_bp_complete_resolvent_nogo import build_report  # noqa: E402


def symbolic_checks() -> None:
    t, lam, d = sp.symbols("t lam d", real=True)
    factored = (1 + (lam + t) ** 2) * (1 + (lam - t) ** 2)
    expanded = lam**4 + 2 * (1 - t**2) * lam**2 + (1 + t**2) ** 2
    assert sp.expand(factored - expanded) == 0

    # Check the Green ODE away from d=0 on the positive half-line.
    green = sp.exp(-d) * (
        sp.cos(t * d) + sp.sin(t * d) / t
    ) / (4 * (1 + t**2))
    ode = (
        sp.diff(green, d, 4)
        + 2 * (t**2 - 1) * sp.diff(green, d, 2)
        + (t**2 + 1) ** 2 * green
    )
    assert sp.simplify(sp.trigsimp(ode)) == 0

    # The even extension is C^2 and has the unit third-derivative jump
    # required by the leading D^4 term.
    assert sp.simplify(sp.limit(sp.diff(green, d), d, 0, dir="+")) == 0
    third_plus = sp.simplify(
        sp.limit(sp.diff(green, d, 3), d, 0, dir="+")
    )
    assert third_plus == sp.Rational(1, 2)


def arb_negative_witnesses() -> None:
    ctx.dps = 80
    pi = arb.pi()
    for raw in ("0.5", "1", "2", "10"):
        t = arb(raw)
        displacement = pi / t
        value = (-displacement).exp() / (-4 * (1 + t * t))
        assert value.upper() < 0
        print(
            "T=", raw,
            " witness_d=", displacement,
            " green_interval=", value,
            " CERTIFIED_NEGATIVE=True",
        )


if __name__ == "__main__":
    symbolic_checks()
    arb_negative_witnesses()
    report = build_report((0.0, 0.5, 1.0, 2.0, 10.0))
    assert report["schema"].endswith("v1")
    print("SYMBOLIC_OPERATOR_AND_JUMP_CHECKS=PASS")
    print("SCOPE=scalar translation-invariant inverse resolvent only")
