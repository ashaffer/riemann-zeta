"""Fast unit tests for the high-precision theta ``S_3`` target scout."""

from __future__ import annotations

import mpmath as mp
from flint import arb

from theta_s3_arb_simpson_target import (
    constant_sine_cubic_tail,
    scaled_transform_jet,
)


def test_exact_normalized_laguerre_jet_at_hard_target() -> None:
    _, _, _, laguerre = scaled_transform_jet(arb("1302.5"), dps=60)
    expected = arb(
        "7185481787.00912595780762576622053142400859547199343337723108"
    )
    assert laguerre.lower() < expected < laguerre.upper()


def test_constant_tail_formula() -> None:
    mp.mp.dps = 50
    p = mp.mpf("1.3")
    cutoff = mp.mpf("2.75")
    expected = mp.quadosc(
        lambda x: mp.sin(p * x) / x**3,
        [cutoff, mp.inf],
        omega=p,
    )
    observed = constant_sine_cubic_tail(
        arb(str(p)), arb(str(cutoff)), arb.pi()
    )
    # mpmath's infinite oscillatory quadrature is only a numerical comparator.
    assert abs(float(observed.mid()) - float(expected)) < 2e-8
