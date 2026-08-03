# Incidence shell-completion fail-fast checkpoint

Status: the exact old--old shell isometry holds.  Return and shell-only
channels fail strongly; adding the old-edge innovation produces a tempting
proper sublayer at coarse resolution, but the exact amplified criterion
crosses below one under validated refinement.  A cross-support parity scan
also rejects a uniform index-one repair mechanism, 2026-08-01.

## 1. Nested relative decomposition

For successive supports `L0 < L1`, put

`I_j=[-L_j/4,L_j/4]`, `D_j=D(L_j)`, and `Delta=D_1-D_0`.

The diagnostic uses old hats on `I_0` and independent hats on the two collars
`I_1 \ I_0`.  It imposes both exact moment conditions and orthogonally splits
the new relative Galerkin space as

`U = embedded old relative space`,

`W = orthogonal moment-corrected collar`.

Prime autocorrelations are evaluated exactly by piecewise-polynomial spatial
quadrature.  Consequently every run below has

`||H_shell|_U - Delta I_U|| = 0`

to floating-point precision.  The only truncated part of the assembly is the
archimedean Fourier integral.

For the Weil block matrix

`Q_1 = [[A,X],[X*,K]]`,

the old ground vector `u` has cross residual `g=X*u`.  When `K>0`, its best
collar correction is `w=-K^-1 g`, with

`primal defect = <u,A u> - <g,K^-1 g>`.

The corresponding normalized Rayleigh quotient is the defect divided by
`1+||K^-1 g||^2`.  The complete old-space Schur complement

`A-X K^-1 X*`

has the same positivity sign as `Q_1`; using it without an independent lower
bound is therefore only a restatement of the target.

## 2. Exact shell-return gate

Write the incidence-gradient blocks as

`B_old = (A_0, sqrt(Delta) V)` on `U`,

`B_collar = (F,G)` on `W`,

where `V*V=I_U`.  Let `C` be the canonical old dual column,

`A_0* C = sqrt(D_0) I_U`.

Define

`P=F* C`, `Q=G* V`,

`r=sqrt(Delta/D_0)`, `alpha=sqrt(D_0/D_1)`.

The propagated old column leaves the collar dual residual

`Y=alpha(P+rQ)`.

The complementary shell-return map is

`T=Q-rP`.

Within this shell-return ansatz, a bounded collar right inverse requires

`T T* >= D_1 I_W`.

The least finite-dimensional old-column correction is obtained from `T Z=Y`.
If `S=I-C*C`, its exact nonlinear norm budget on old inputs is

`(1+r^2) Z*Z <= (alpha I-rZ)* S (alpha I-rZ)`.

The table's final column compares its squared norm with the uncorrected
propagated slack.  That ratio is a severity diagnostic, not by itself the exact
operator inequality.  In contrast, `T T* >= D_1 I_W` is a necessary condition
coming from collar-only inputs, so its failure already rejects the ansatz.

At `21` old hats and `6` hats in each collar:

| transition | `||P+rQ||/(||P||+r||Q||)` | rank / stable rank of `P+rQ` | `lambda_min(TT*)/D_1` | `||T^dagger Y||` | correction squared / old slack |
|---:|---:|---:|---:|---:|---:|
| `1.750 -> 2.485` | `1.000` | `12 / 3.35` | `4.91e-8` | `2.0430` | `2.84e2` |
| `2.485 -> 2.996` | `1.000` | `12 / 3.53` | `3.09e-12` | `3.1746` | `3.46e5` |
| `2.996 -> 3.555` | `0.909` | `12 / 2.99` | `9.43e-8` | `8.2899` | `2.91e6` |
| `3.555 -> 4.040` | `1.000` | `12 / 2.25` | `3.04e-8` | `2.4004` | `3.27e5` |

There is no favorable cancellation in `P+rQ`, and the return floor misses its
required value by at least seven orders of magnitude already at this coarse
resolution.  The correction is order one while the available old slack is
small.

For the representative transition `2.485 -> 2.996`, refinement gives

| old hats | hats per collar | `dim U / dim W` | `lambda_min(TT*)/D_1` | `||T^dagger Y||` | correction squared / old slack |
|---:|---:|---:|---:|---:|---:|
| `21` | `6` | `19 / 12` | `3.09e-12` | `3.17461218` | `3.46e5` |
| `31` | `10` | `29 / 20` | about `4e-16` | `3.17461218` | `1.20e6` |
| `61` | `20` | `59 / 40` | `1.48e-21` | `3.17461254` | `3.39e6` |

The smallest singular value is numerically delicate, but the trend is not:
the return map loses its lower bound while the correction norm is stable.  If
`dim W > dim U`, then `T:U -> W` is rank deficient and the return floor is
exactly zero.  For example, `21` old hats and `10` hats per collar give ranks
`19 -> 20` and a zero floor.

This is the finite-section signature of a smoothing old-to-collar return map,
not a support-uniform right inverse.

## 3. Fresh-shell and combined collar channels

The orthogonal innovation in the fresh shell is

`R_fresh = G*G - Q Q* >= 0`.

A fresh-shell-only sufficient construction would require

`R_fresh >= D_1 I_W`.

The larger natural cycle family has response capacity

`T (I+r^2 C*C)^-1 T* + R_fresh`.

At the same coarse resolution, the floor ratios for the four transitions are

| transition | `lambda_min(R_fresh)/D_1` | combined capacity floor / `D_1` |
|---:|---:|---:|
| `1.750 -> 2.485` | `0.08446` | `0.08496` |
| `2.485 -> 2.996` | `0.04176` | `0.04202` |
| `2.996 -> 3.555` | `0.07461` | `0.07516` |
| `3.555 -> 4.040` | `0.06700` | `0.06716` |

All matrices have full collar rank in these tests, so the failure is a size
failure rather than merely a kernel.  At `31+10+10` hats the corresponding
ratios are respectively

`0.08355/0.08407`, `0.04175/0.04223`, `0.07388/0.07421`, and
`0.06574/0.06609`.

Thus the fresh-shell channel is stable under refinement but supplies only
about four to eight percent of the required degree.  Adding the natural return
channel changes the floor very little.

This rejects the fresh-shell-only sufficient construction and the displayed
return-plus-fresh cycle family.  It does **not** reject every possible cycle in
the full kernel of the old edge map.

## 4. Old-edge innovation and the exact amplified criterion

The missing orthogonal piece in the old-place edge space is

`R_old = F*F - F*A_0 (A_0*A_0)^-1 A_0*F >= 0`.

Numerically, the three mutually orthogonal cycle capacities satisfy

`R_old + R_fresh + T(I+r^2 C*C)^-1 T*`

` = G_WW-G_WU G_UU^-1 G_UW`,

the complete incidence Schur complement.  The operator-norm error in this
identity is below `4.2e-15` in every reported run.

At `21+6+6` hats, the raw degree floors are

| transition | `R_old/D_1` | `(R_old+R_fresh)/D_1` | full-kernel capacity / `D_1` |
|---:|---:|---:|---:|
| `1.750 -> 2.485` | `0.90417` | `1.02500` | `1.02530` |
| `2.485 -> 2.996` | `0.98510` | `1.07367` | `1.07424` |
| `2.996 -> 3.555` | `0.90703` | `1.03177` | `1.03221` |
| `3.555 -> 4.040` | `0.91585` | `1.04513` | `1.04551` |

Thus the two fresh innovations, excluding the coupled return channel, appear
to pass with an order-percent reserve.  This raw comparison is not the correct
completion threshold, however, because it omits amplification by leakage from
the nearly singular old Weil block.

Put

`S_0=B_U*B_U`, `Q_a=S_0-D_1 I`,

`L=S_0^-1 B_U*B_W`.

For the canonical old column the exact amplified threshold is

`H=D_1 [I+L* S_0 Q_a^-1 L]`.

For a cycle capacity `G_J`, the structured sufficient test is

`G_J >= H`.

When `G_J` is the full kernel capacity, this is algebraically the Schur
condition for the complete Weil matrix.  For a proper cycle subspace it is a
genuine sufficient criterion.

At `21+6+6` hats, the generalized minimum eigenvalue of `G_J` relative to `H`
is

| transition | return | shell | old | return+shell | old+return | old+shell | full kernel |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `1.750 -> 2.485` | `4.2e-8` | `0.0832` | `0.8351` | `0.0837` | `0.8364` | `1.00861` | `1.00996` |
| `2.485 -> 2.996` | `2.9e-12` | `0.0407` | `0.9128` | `0.0410` | `0.9134` | `1.01048` | `1.01107` |
| `2.996 -> 3.555` | `8.2e-8` | `0.0727` | `0.8387` | `0.0733` | `0.8398` | `1.00322` | `1.00366` |
| `3.555 -> 4.040` | `2.6e-8` | `0.0662` | `0.8601` | `0.0664` | `0.8612` | `1.00690` | `1.00797` |

Old-plus-shell is the only proper tested sublayer which passes at this
resolution.  The representative `2.485 -> 2.996` refinement is decisive:

| old hats | hats per collar | arch cutoff | old+shell ratio | full-kernel ratio |
|---:|---:|---:|---:|---:|
| `21` | `6` | `600` | `1.010479` | `1.011072` |
| `31` | `10` | `1200` | `1.004062` | `1.004684` |
| `61` | `20` | `1200` | `1.001722` | `1.002397` |
| `121` | `40` | `1600` | `1.000170` | `1.000764` |
| `121` | `60` | `1800` | `1.000161` | `1.000756` |
| `181` | `60` | `1600` | `0.999819` | `1.000420` |
| `181` | `60` | `2000` | `0.999828` | `1.000430` |

The crossing is much larger than its cutoff variation.  At both final runs
the old and full Weil gaps remain positive and of the expected sizes (`1.85e-5`
and about `2.9e-7`), unlike under-resolved low-cutoff experiments which can
corrupt the archimedean matrix.  The proper canonical old-plus-shell sublayer
is therefore numerically falsified before the continuum limit.

The failure is spectrally localized rather than a collapse of the whole
collar sector.  Since `H>0`, the inertia of

`R_old+R_fresh-H`

is exactly the inertia obtained by comparing the generalized eigenvalues of
`R_old+R_fresh` with `H`.  The two smallest eigenvalues and the number below
one are

| old / collar hats | smallest | second | count below `1-1e-10` | count below `1.01` | return on worst mode | full-kernel smallest |
|---:|---:|---:|---:|---:|---:|---:|
| `61 / 20` | `1.001721789` | `1.004968722` | `0` | `2` | `6.7544e-4` | `1.002396762` |
| `121 / 40` | `1.000169731` | `1.001365745` | `0` | `2` | `5.9473e-4` | `1.000764395` |
| `181 / 60` | `0.999828457` | `1.001283707` | `1` | `2` | `6.0175e-4` | `1.000430107` |

Here each generalized eigenvector is normalized by `v*H v=1`, so “return on
worst mode” means `v*R_return v` in the same dimensionless scale.  At the
crossing the sole negative generalized eigenvalue of the difference is
`-1.7154e-4`.  The return contribution on that vector is `6.0175e-4`, or
`3.51` times the deficit; its operator-norm coupling from the negative vector
to the positive generalized eigenspace is `1.1642e-4`.  Adding the return term
therefore repairs the one violating mode while leaving the second eigenvalue
positive.  In fact, writing the deficit as `mu=1.7154e-4`, the positive-sector
gap as `gamma=1.2837e-3`, the return diagonal as `r=6.0175e-4`, and this cross
norm as `c`, the elementary Schur estimate already has reserve

`(r-mu)-c^2/gamma = 4.1964e-4 > 0`.

It certifies the individual index-one repair without using the
positive-sector block of the return operator.  Across these refinements the
near-threshold sector has dimension two and the actually negative sector has
dimension at most one.  This is a useful low-dimensional residual for this
transition, but not evidence that the count remains bounded in the continuum
limit.

That qualification is decisive.  Repeating the same `121/40` test across all
four support transitions gives the following parity-resolved spectrum.  The
parity signs are measured in physical hat coordinates under `x -> -x`, not in
the arbitrary null-space basis.  `R/deficit` is the return quadratic form on
the worst `H`-normalized mode divided by `1-lambda_1`; it is omitted when
there is no deficit.  The cross column is the operator norm of the return
block between the negative and positive generalized eigenspaces.

| transition | `lambda_1` (parity) | `lambda_2` (parity) | negative / below `1.01` | `R(worst)`; `R/deficit` | return cross | full-kernel `lambda_1` |
|---:|---:|---:|---:|---:|---:|---:|
| `1.750 -> 2.485` | `1.001787` (odd) | `1.009288` (even) | `0 / 2` | `1.63e-3`; -- | -- | `1.003421` |
| `2.485 -> 2.996` | `1.000170` (even) | `1.001366` (odd) | `0 / 2` | `5.95e-4`; -- | -- | `1.000764` |
| `2.996 -> 3.555` | `0.997973` (odd) | `0.999828` (even) | `2 / 3` | `2.63e-3`; `1.299` | `6.36e-3` | `1.000123` |
| `3.555 -> 4.040` | `0.999029` (odd) | `0.999478` (even) | `2 / 3` | `1.31e-3`; `1.347` | `2.83e-4` | `1.000167` |

Thus two transitions already have both an odd and an even violating mode at
the first common refined resolution.  The full return channel repairs both,
but there is no uniform index-one defect theorem across support steps.

This is insensitive to a cheap collar-aspect-ratio check.  Increasing the
collar count from `40` to `60` at fixed `121` old hats changes the two later
transitions respectively from

`(0.997973, 0.999828; 2 negative)` to
`(0.997956, 0.999809; 2 negative)`,

and from

`(0.999029, 0.999478; 2 negative)` to
`(0.999023, 0.999478; 2 negative)`.

The complete `181/60` scan (cutoff `2000`) makes the nonuniformity sharper:

| transition | `lambda_1` (parity) | `lambda_2` (parity) | negative (even / odd) | below `1.01` | `R(worst)`; `R/deficit` | return cross | full-kernel `lambda_1` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `1.750 -> 2.485` | `1.000976` (odd) | `1.008169` (even) | `0 (0 / 0)` | `2` | `1.68e-3`; -- | -- | `1.002650` |
| `2.485 -> 2.996` | `0.999828` (even) | `1.001284` (odd) | `1 (1 / 0)` | `2` | `6.02e-4`; `3.508` | `1.16e-4` | `1.000430` |
| `2.996 -> 3.555` | `0.997762` (odd) | `0.999528` (even) | `3 (2 / 1)` | `3` | `2.92e-3`; `1.305` | `1.18e-2` | `1.000081` |
| `3.555 -> 4.040` | `0.998834` (odd) | `0.999357` (even) | `2 (1 / 1)` | `3` | `1.34e-3`; `1.147` | `3.01e-4` | `1.000061` |

The defect indices are therefore `0,1,3,2`, and the three-mode case contains
both parities.  Consequently even a uniform index-two or single-parity
replacement is not supported: the return repair is low-dimensional in these
finite sections, but its required index is already support- and
resolution-dependent.

There is a related propagated, noncanonical construction.  It carries a
coupled-return kernel component inside the inherited old column, then uses
only `R_old+R_fresh` for the new correction and right inverse.  Its computed
contraction slack stays positive, but from `61` through `181` old hats it
agrees with the exact canonical Weil margin to roughly `1e-14`--`1e-16`
absolute.  It has no independently resolved reserve and should presently be
treated as a knife-edge reformulation, not as validation of the falsified
proper sublayer.

## 5. Comparison with the actual Weil margin

The primal block experiment also loses its apparent slack under refinement.
For `2.485 -> 2.996`:

| old / collar hats | old gap | full new gap | fixed-old cross ratio | fixed-old completed defect |
|---:|---:|---:|---:|---:|
| `21 / 6` | `2.42e-4` | `2.24e-4` | `0.0375` | `2.33e-4` |
| `31 / 10` | `6.99e-5` | `4.95e-5` | `0.1600` | `5.87e-5` |
| `61 / 20` | `2.48e-5` | `5.02e-6` | `0.4238` | `1.43e-5` |
| `121 / 40` | `1.93e-5` | `5.26e-7` | `0.5412` | `8.87e-6` |

The full new ground vector has more than `0.9999` of its `L2` mass in `U`, yet
a tiny moment-corrected collar component changes the gap by orders of
magnitude.  A single propagated old ground vector therefore does not capture
the full Schur obstruction; the dangerous direction rotates inside the old
sector as resolution increases.

For the full incidence Gram matrix `B*B=Q+D I`, the canonical dual frame has
the exact contraction margin

`1-||sqrt(D) B(B*B)^-1||^2 = lambda_min(Q)/(D+lambda_min(Q))`.

For example, at `61+20+20` hats the measured full gap is `5.019e-6` and this
canonical margin is `6.037e-7`.  Hence a generic completion using the full
inverse succeeds exactly when the finite Weil matrix is positive: it is
algebraically useful, but circular as an independent RH mechanism.

## 6. Numerical caveat and reproduction

The moment projection, hat Gram matrix, pole vectors, prime autocorrelations,
and shell isometry are exact up to ordinary floating-point rounding.  The
archimedean matrix uses a finite Simpson Fourier integral.  Values involving
the smallest singular value of `T` should therefore be read as diagnostics,
not certified enclosures.  The robust conclusions are the many-order
shortfall, its worsening with refinement, the stable order-one correction,
and the stable fresh-shell floor ratios.

Representative scan:

```bash
python3 src/incidence_shell_completion.py \
  --old-degree 21 --collar-degree 6 \
  --arch-cutoff 600 --arch-intervals 60000
```

Refined scan:

```bash
python3 src/incidence_shell_completion.py \
  --old-degree 31 --collar-degree 10 \
  --arch-cutoff 1200 --arch-intervals 120000
```

Return-floor refinement:

```bash
python3 src/incidence_shell_completion.py \
  --supports 2.485 2.996 \
  --old-degree 61 --collar-degree 20 \
  --arch-cutoff 1200 --arch-intervals 120000
```

Amplified-gate crossing check:

```bash
python3 src/incidence_shell_completion.py \
  --supports 2.485 2.996 \
  --old-degree 181 --collar-degree 60 \
  --arch-cutoff 2000 --arch-intervals 200000
```

Cutoff stability can be checked by repeating the `31+10+10` run with
`600/60000` and `1800/180000`.  The return correction changes only from
`3.174612182` to `3.174612185`; the return floor is already near floating-point
resolution.

## 7. Verdict

The new-shell isometry is real and exactly solves the old--old compressed
column.  The detailed cycle decomposition shows where the apparent reserve
goes:

1. the propagated cross residual has no low-rank cancellation;
2. the complementary return map is not bounded below;
3. its least old-column correction is order one while the uncorrected slack
   comparison worsens from hundreds to millions;
4. shell innovation supplies less than nine percent of the unamplified degree;
5. old-edge plus shell innovation clears the raw degree and initially clears
   the amplified threshold, but crosses below it under stable refinement;
6. the full three-piece capacity is exactly the incidence Schur complement,
   where the criterion becomes the original Weil positivity condition.

The tested proper structured sublayers are therefore pruned.  The propagated
noncanonical variant remains positive only at a margin numerically
indistinguishable from the exact Weil margin.  Falling back to the full kernel
or unrestricted Gram inverse makes the construction equivalent to finite Weil
positivity rather than supplying an independent theorem.
