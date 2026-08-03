# Stage 4: paired-tail mechanism

**Status:** the canonical comparator residual theorem is proved on the smooth
compact test core.  Extension to every vector in the closed logarithmic form
domain is reduced in `STAGE4-FORM-DOMAIN-EXTENSION.md` to uniform dual-form
boundedness; density by itself does not supply that extension.

## Correction to the first formulation

The CCM comparator is a moving-support family:

`k_lambda(u) = E(h_lambda)(u)` on `[lambda^-1, lambda]`.

It is therefore incorrect to regard all comparators as vectors in one fixed
compact-support space.  The correct weak-residual statement pairs `k_lambda`
with each fixed compact test after zero-extending that test into the growing
window.  This geometry is now formalized by `movingWeilCross` and
`movingZeroCrossInDisk`.

## Arithmetic factorization and the truncation defect

Before restriction to `[lambda^-1,lambda]`, the Mellin transform of the
arithmetic map

`E(h)(u) = u^(1/2) sum_(n>=1) h(nu)`

formally factors as a zeta factor times the Mellin transform of `h`.  At a
nontrivial zeta zero, the untruncated transform therefore vanishes.  The value
of the *truncated* comparator transform at that zero is consequently governed
entirely by the omitted Mellin tails.  Thus the residual is not a generic
Paley--Wiener zero-tail problem; it is a prolate leakage problem.

For the upper tail there is no direct contribution once the interval prolate
function is extended by zero.  The lower tail is converted by Poisson
summation into the Fourier leakage of `h_lambda` outside `[-lambda,lambda]`.
This is exactly the quantity controlled by the prolate concentration
eigenvalues.  The zero-integral condition removes the zero Fourier mode.

## New paired-edge cancellation

The published compact-strip estimate has the schematic form

`|A_lambda(alpha,t)| <= C(alpha,t) lambda^(-1/2-alpha)`

for `-1/2 < alpha < 1/2`.  Estimating a single zero sample is badly
nonuniform as `alpha -> -1/2`.  But a Guinand--Weil zero summand never contains
one sample alone.  It contains the complementary product

`A_lambda(alpha,t) A_lambda(-alpha,-t)`.

The powers cancel exactly:

`lambda^(-1/2-alpha) lambda^(-1/2+alpha) = lambda^-1`.

This cancellation is independent of the real part of the zero.  Hence zeros
approaching either boundary of the critical strip do **not** destroy the
power of `lambda` in the quadratic residual.  The earlier attempt to demand a
uniform bound for each transform factor separately discarded this essential
Weil symmetry.

This observation applies directly to the diagonal energy.  The polarized weak
residual against a fixed test contains one comparator factor and one fixed-test
factor, so diagonal pairing alone is not enough.  The weak residual is instead
closed by the dominated-convergence mechanism below.

## Dominated weak-residual mechanism

At each fixed zero, CCM compact-strip convergence makes the comparator
transform tend to zero.  Uniformly in the comparator scale, their absolute
Mellin estimate bounds that transform by a constant times the reciprocal
distance `delta_rho` to the nearest strip edge.  The unconditional zero-free
region gives

`delta_rho^-1 = O(log(2 + |Im rho|))`.

For a fixed globally `C^2` compact test, two Fourier integrations by parts give

`|G(+-alpha_rho + i Im rho)| = O((1 + |Im rho|)^-2)`.

Thus every polarized zero summand is eventually dominated by a test-dependent
constant times

`multiplicity(rho) log(2+|Im rho|) / (1+|Im rho|)^2`.

The Riemann--von Mangoldt count makes this weight summable: dyadic shells have
`O(T log T)` zeros and contribute `O(log(T)^2/T)`.  Tannery's theorem now
passes the pointwise comparator limit through the complete zero sum.  This
proves convergence of the full weak residual on smooth compact tests without
any uniform interchange of the support and zero-radius limits.

The Lean module `Stage4DominatedResidual.lean` proves precisely this
dominated-zero-sum implication and specializes it to the standard height
weight.  `ZetaZeroCountingLiterature.lean` imports only the unconditional
summability consequence of Riemann--von Mangoldt.

## Residual theorem

Let `k_lambda` be the CCM comparator, represented in its growing logarithmic
support interval, with the normalization for which its Mellin transform tends
to `Xi`.  For every fixed globally `C^2` compactly supported logarithmic test
`g`, embedded into the same growing interval,

`WeilCross(k_lambda,g) -> 0`.

Proof.  Polarize the symmetric-disk Guinand--Weil formula term by term.  At a
zero `rho`, each term is a sum of one comparator transform and one fixed-test
transform.  CCM convergence makes the comparator factor tend to
`Xi(rho)=0`.  Their absolute Mellin remainder estimate, made symmetric by the
functional equation, is bounded uniformly in `lambda` by
`C / delta_rho`, where `delta_rho` is the distance of `Re rho` from the strip
boundary.  The classical zero-free region gives
`delta_rho^-1 <= C log(2+|Im rho|)` (enlarging `C` absorbs the finite low-zero
set).  Uniformly for real parts in the critical strip, two integrations by
parts give the fixed-test bound `(1+|Im rho|)^-2`.  Therefore the polarized
summand is dominated by a constant times `residualHeightWeight`.  That weight
is summable by Riemann--von Mangoldt.  Tannery gives convergence of the full
polarized zero series to zero.  Absolute convergence of this polarized series
identifies its sum with the symmetric-disk limit, and Guinand--Weil identifies
that limit with the full Weil cross form.  Hence the asserted residual tends
to zero.

No RH assumption occurs in this argument.  The arithmetic inputs are the
functional equation, the classical zero-free region, and Riemann--von
Mangoldt counting.

### Formal ledger

- `movingZeroCrossSummand`: the correctly polarized moving-support summand;
- `tendsto_nontrivialZerosInDisk_atTop`: disk exhaustion is cofinal;
- `zeroCrossInDisk_tendsto_tsum_of_summable`: absolute polarized convergence
  agrees with symmetric-disk convergence;
- `movingWeilCross_tendsto_zero_of_dominated_zero_summands`: Tannery theorem;
- `movingWeilCross_tendsto_zero_of_standard_CCM_majorant`: specialization to
  the zero-free-region/Riemann--von Mangoldt height weight.

The residual target is consequently reduced to a bound of the form

`|zeroSummand_lambda(rho)|
   <= lambda^-1 B_lambda(Im rho) / (1 - 4 alpha(rho)^2)`.

For the diagonal estimate, the remaining work has two concrete parts:

1. derive `B_lambda(t)` from repeated Mellin integration by parts and the
   prolate endpoint/leakage estimates;
2. sum the resulting majorant using zero counting and an unconditional
   zero-free-region bound for the reciprocal edge factor.

If `B_lambda(t)` has two integrable powers of ordinate uniformly after the
prolate normalization, zero counting costs only a logarithm and the complete
paired zero tail is `O(lambda^-1 polylog(lambda))`, which tends to zero.
This is now the active Stage-4 theorem.  No positivity or RH assumption enters
the paired-power cancellation.
