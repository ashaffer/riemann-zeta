# Theta modularity as all-order boundary-jet cancellation

Status: exact structural theorem; finite theta truncations are ruled out,
2026-08-01.

Let `f` be smooth and rapidly decreasing on `[0,infinity)` and put

`H(x) = integral_0^infinity f(u) cos(xu) du`.

Repeated integration by parts shows that if the first nonzero odd boundary
derivative is `f^(2k+1)(0)`, then

`H(x) = C x^(-p) + O(x^(-p-2))`, with `p=2k+2` and `C != 0`.

Consequently

`H'(x)^2 - H(x)H''(x)`

` = -p C^2 x^(-2p-2) + O(x^(-2p-4)) < 0`

for all sufficiently large `x`.  Thus a cosine transform can satisfy the
first Laguerre inequality at every height only if every odd boundary jet of
its half-line kernel vanishes (or if no first nonzero odd jet exists within
the regularity class).

For the completed xi theta kernel, the modular relation makes its even
extension smooth and hence enforces

`Phi^(2j+1)(0)=0` for every `j>=0`.

This cancellation occurs only after summing the full theta series.  An
individual `n`-summand has nonzero odd boundary data, so its Laguerre density
must eventually be negative.  More generally, every finite truncation whose
first surviving odd boundary jet is nonzero must fail at high frequency.

At `t=0`, `x=46`, the numerical interaction matrix confirms the mechanism:

- diagonal `n=1` contribution: `-3.47376659628e-13`;
- diagonal `n=2` contribution: `+1.19033418706e-14`;
- twice the `n=1,n=2` cross contribution: `+4.07494e-13`;
- combined first-two-summand value: `+7.20205e-14`.

The cross term, not the positive diagonal tail, repairs the dominant negative
piece.  Higher summands are already negligible at this particular height,
but they are indispensable globally because the exact all-order boundary-jet
cancellation uses the infinite modular sum.

## Consequence

The modular invariant has now been isolated: all-order cancellation of odd
jets at the symmetry boundary.  This explains why finite approximants can
look excellent on bounded ranges yet cannot establish global Laguerre
positivity.  It does not itself control the sign after the algebraic tail has
been cancelled.  The next valid theta target must turn the full modular
functional equation—not a finite summand truncation—into a sign statement for
the remaining beyond-all-orders Fourier contribution.
