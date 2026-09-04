#!/usr/bin/env python3
"""Exact exponent checks for the truncated-trapezoid/log-curvature report."""

from fractions import Fraction as F


theta = F(797, 5000)
mu = F(63827, 65000)
kappa = F(90151617, 5_000_000_000)  # .0180303234
aperture = F(50, 33)
beta = F(1537, 10_000)

d = 1 - mu
third_moment = 2 * theta + mu
third_saving = 3 - third_moment
transition = 1 - theta
peano_at_transition = third_saving - 2 * transition
formal_frontier = (third_saving - kappa) / 2
continuous_theta = F(2, 15) + F(13, 9) * kappa
continuous_transition = 1 - continuous_theta

assert theta == F(797, 5000)
assert d == F(1173, 65_000)
assert third_moment == F(84_549, 65_000)
assert third_saving == F(110_451, 65_000)
assert transition == F(4203, 5000)
assert peano_at_transition == d
assert d > kappa
assert formal_frontier > transition
assert continuous_theta == F(796_885_669, 5_000_000_000)
assert continuous_transition == F(4_203_114_331, 5_000_000_000)
assert continuous_transition > formal_frontier

# The low-q cell deletion remains o(1) for O(log Y)-sized cells in the
# exact-log integer countermodel at the top aperture.
minor_measure_saving = 1 - beta - aperture / 2
minor_collar_saving = 2 - aperture - 2 * beta
assert minor_measure_saving == F(29_279, 330_000)
assert minor_collar_saving == F(29_279, 165_000)
assert minor_measure_saving > 0
assert minor_collar_saving > 0

# Linearization on logarithmic blocks: t(log Y)^2/Y^2=o(1).
assert 2 - aperture == F(16, 33) > 0

print("PASS")
print(f"theta={float(theta):.12f}")
print(f"tail_saving={float(d):.12f}")
print(f"truncated_third_moment_exponent={float(third_moment):.12f}")
print(f"third_moment_fourier_saving={float(third_saving):.12f}")
print(f"proved_transition_endpoint={float(transition):.12f}")
print(f"formal_peano_frontier={float(formal_frontier):.12f}")
print(f"continuous_tail_frontier={float(continuous_transition):.12f}")
print(f"margin_over_kappa={float(d-kappa):.12g}")
print(f"integer_model_minor_measure_saving={float(minor_measure_saving):.12f}")
print(f"integer_model_minor_collar_saving={float(minor_collar_saving):.12f}")
