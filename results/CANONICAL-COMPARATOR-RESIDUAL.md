# Canonical comparator residual

## Exact mechanism

The CCM comparison vector is

`k_lambda = E(h_lambda)`,

where `h_lambda` is the zero-integral combination of prolate modes 0 and 4.
CCM prove that its transform converges to the completed critical-line function
`Xi` uniformly on closed substrips.

The Guinand--Weil representation shows why this vector is a near-kernel.  For
fixed zero radius `R`, the polarized residual against a test vector is a finite
sum of values of `Fourier(k_lambda)` at zeta-zero spectral coordinates.  Since
`Xi` vanishes at every such coordinate, whether real or nonreal, compact-local
convergence gives

`finiteDiskResidual_R(k_lambda, g) -> 0`

for every fixed `R`.  This explanation is unconditional and does not use RH.

## The real analytic gap

The full Weil residual requires the limits in the opposite order:

`lim_lambda lim_R finiteDiskResidual_R(k_lambda,g)`.

Fixed-disk convergence only controls

`lim_R lim_lambda finiteDiskResidual_R(k_lambda,g)`.

Interchanging these limits requires a zero-tail majorant uniform in `lambda`
after the chosen normalization.  Compact-local convergence alone supplies no
such bound.  This is the exact place where growth, exponential type, and the
shrinking Weil margin interact.

There is a second, related boundary issue.  A bound on either transform factor
alone degenerates near a strip edge.  The paired-tail calculation in
`STAGE4-PAIRED-TAIL-MECHANISM.md` improves this substantially: complementary
Weil factors have powers `lambda^(-1/2-alpha)` and
`lambda^(-1/2+alpha)`, whose product is exactly `lambda^-1`.  Only the
reciprocal edge constants and ordinate decay remain to be summed.

The uniform-tail formulation is stronger than necessary.  The completed
argument uses dominated convergence on the polarized zero series.  The
zero-free region permits logarithmic growth in the comparator factor, while
the fixed smooth test contributes quadratic ordinate decay; Riemann--von
Mangoldt then gives a summable majorant.  See
`STAGE4-PAIRED-TAIL-MECHANISM.md`.

## Formal result

`Stage4CanonicalResidual.lean` defines spectral invisibility as convergence of
every polarized symmetric-disk residual to zero and proves that it forces both
the full weak radical identity and zero diagonal Weil energy.  The proof uses
only uniqueness of the already formalized Guinand--Weil disk limit.

The formal interface separates:

1. fixed-disk convergence from `Fourier(k_lambda) -> Xi`;
2. uniform zero-tail control;
3. the resulting asymptotic weak-radical conclusion.

That interface is now complete.  `FixedDiskInvisible` records convergence on
each fixed symmetric disk, `UniformZeroTail` records eventual tail control
uniformly along the comparator sequence, and
`asymptoticallyWeakRadical_of_fixedDisk_of_uniformZeroTail` proves their exact
Moore--Osgood consequence.  The limit-interchange proof itself has no new
literature axiom in its Lean axiom audit.

## Sonin/trace audit

Passing to the Sonin trace does not presently remove the missing estimate.
Connes--Consani's proved theorem is explicitly the single archimedean-place
case, with support in `(1/2,2)` so that no rational prime occurs.  Their paper
states the semilocal construction for a finite set of places as the intended
next mechanism; it does not prove the growing-support, all-prime positivity or
the comparator-uniform remainder bound needed here.

Consequently the prime-inclusive Stage 4 theorem is not a consequence of the
archimedean result.  It is instead obtained from the weighted
prolate--Poisson--Mellin majorant in `STAGE4-PROLATE-MOMENT-PROOF.md`, followed
by zero-free-region and zero-counting estimates.  The Lean theorem records
that majorant as a certificate on the actual moving comparator family; the
remaining formal trust boundary is itemized by its axiom audit.
