# Suzuki Euler--Lagrange boundary residual

Status: the exact weak equation and arithmetic boundary residual are proved;
the boundary continuation estimate remains open.

The unconditional Suzuki identity has now been polarized.  On the smooth
core, Lean proves

`B_screw(phi,psi) = B_pole(phi,psi) + B_arch(phi,psi) - B_prime(phi,psi)`

and identifies this with the arithmetic `weilCross` exactly.

For a candidate localized eigenfunction `phi`, the weak old-sector equation
is

`B_screw(phi,psi) = lambda <phi,psi>`

for every variation `psi` supported in the old interval.  Defining

`R_lambda(phi,psi) = B_screw(phi,psi) - lambda <phi,psi>`,

Lean proves that `R_lambda` vanishes on every old-supported variation.  For an
`L2`-orthogonal collar variation, it is exactly the combined old--collar Weil
cross term measured in the numerical experiment.

This gives the precise continuation problem: control a functional known to
vanish on the old test subspace when it is evaluated just outside that
subspace.

## Important correction

The residual is not merely an endpoint value.  Suzuki's prime ramps have kink
lines `x-y = +/- log n` throughout the integration square.  Integration by
parts produces shifted interior traces as well as outer-boundary terms.  The
observed cancellation is therefore a nonlocal pole + digamma/Lerch - prime
ramp identity.

The next theorem must exploit regularity or a functional equation of the
explicit screw kernel to continue the annihilating residual across the
support boundary with a quantitative norm below one.  The present file does
not assume that estimate or positivity.

## Low-sector stress test

The corrected diagnostic evaluates combinations of low old eigenmodes.  At
the tight first event, with old hat dimension 121:

| low modes | collar modes | continuation norm |
|---:|---:|---:|
| 1 | 20 | `0.813` |
| 12 | 20 | `0.931` |
| 24 | 24 | `0.952` |

The norm remains below one but approaches it as resolution grows.  This
supports a strict event-by-event contraction, not a support-independent gap.
The values are non-certified diagnostics and are not Lean premises.

`cross_sq_le_of_lowEnergy_rigidity` proves the exact composition: after the
continuation inequality is established on the chosen low sector, ordinary
`L2` estimates handle its high-energy complement.

## Refined convergence and extremizer

Simultaneous refinement to old dimension 161 and 32 low/32 collar modes gives
`0.956`.  Increasing to 40 collar modes leaves this unchanged, and changing
the angular-frequency cutoff from 2400 to 4800 also leaves it unchanged to
the displayed precision.  This is a major numerical validation of the
finite-dimensional continuation phenomenon, though still not an interval
certificate for the infinite-dimensional operator.

The maximizing pair is even to relative symmetry error below `2e-12`.  In
unit old-energy and collar-energy normalization its signed cross components
are

`pole = 74.0049`, `archimedean = -50.7779`, `prime = 22.2705`,

so

`pole + archimedean - prime = 0.95646`.

Thus the small residual is cancellation among terms roughly fifty to seventy
times larger than the result.  The witness is saved in
`results/low-energy-cross-witness.npz`.

This also clarifies the analytic obstacle.  The cancellation is not explained
by parity alone: parity isolates the dangerous block but does not relate the
three large functionals.  The weak Euler--Lagrange equation explains their
relation on old-supported variations; extending that relation to the collar
with norm below one remains exactly the mixed-positivity problem.  No
strictly weaker identity has yet emerged from the extremizer.
