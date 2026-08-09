# Coboundary dispersion as a cancellation candidate

Status: exact reduction and fail-fast specification, 2026-08-06.  This note
does **not** prove a new zero-free region or the Riemann Hypothesis.

## 1. Verdict

There is one completion-preserving way to turn the fixed-window/Type-II
problem into a positive dispersion problem:

1. group the entire Vaughan tail by its total product;
2. include the full Type-I centering;
3. take the logarithmic scale coboundary;
4. square only after those three operations, and then average in scale.

The resulting quadratic form retains every cofactor and parity cross term.
It also keeps an off-critical zero exponentially visible.  Thus averaging
does not commit the usual topology error of discarding a sparse exceptional
phase.

This construction is a new attack surface, not a bound.  Its first exact
calibration shows that the semiprime diagonal alone is of order `log X`.
Any successful estimate must cancel that term against unequal-product and
centering cross terms before taking absolute values.

## 2. Complete first, then difference

Retain the notation of
`FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md`.  For fixed cutoffs `U,V`, put

```text
a_(U,V)(n)
 =sum_(dbm=n, d>U, b>V) mu(d)Lambda(b)
 =(mu_(>U)*Lambda_(>V)*1)(n).                             (2.1)
```

Then the full balanced term is

```text
B_(U,V)^(k)(exp R)
 =sum_n a_(U,V)(n)n^(-1/2)Phi_(h,k)(R-log n).             (2.2)
```

Grouping by `n` is essential.  For distinct primes
`p<q`, both above the cutoffs,

```text
a_(U,V)(pq)=-(log p+log q)=-log(pq).                      (2.3)
```

The two prime assignments are one coefficient, not two independent
diagonal blocks.

Let

```text
F_(U,V)(R)=B_(U,V)^(k)(exp R)-Z_(U,V)^(k)(exp R).         (2.4)
```

For `h=ell/k`, define the compact window

```text
W_(ell,k)(t)=Phi_(h,k)(t+ell)-Phi_(h,k)(t).               (2.5)
```

It is nonnegative, symmetric, and supported on `[-ell,ell]`.  At `k=1` it
is exactly the triangular window `w_ell`.  With one frozen pair of cutoffs,

```text
Delta_ell F_(U,V)(R)
 :=F_(U,V)(R+ell)-F_(U,V)(R)                              (2.6)
```

has discrete part

```text
sum_n a_(U,V)(n)n^(-1/2)W_(ell,k)(R-log n).               (2.7)
```

The difference also simplifies the center.  Write

```text
P=J_0 M_U(1),
Q=J_1 M_U(1)+J_0[M_U'(1)-M_U(1)L_V(1)].                  (2.8)
```

The center is

```text
Z_(U,V)^(k)(exp R)=exp(R/2)[J_0-PR-Q]-I_0.               (2.9)
```

Consequently,

```text
Delta_ell Z(R)
 =exp(R/2){exp(ell/2)[J_0-P(R+ell)-Q]-[J_0-PR-Q]}.        (2.10)
```

The entire critical-value constant `I_0` cancels.  Only finite cutoff data
at `s=1` remain in the local center.

The fixed-order Vaughan theorem gives

```text
Delta_ell F_(U,V)(R)
 =D_(ell,k)(R)+Delta_ell E_(U,V)(R),                      (2.11)
```

where `D_(ell,1)=D_ell` and `E_(U,V)` is the stated Euler-evaluation defect.
Below the fixed-order endpoint, the last term tends to zero.  On a short
scale block, `U,V` can be frozen at the lower endpoint and remain within
constant factors of the balanced range.

The transform multiplier of (2.5) is

```text
(exp(ell s)-1)H_(h,k)(s).                                 (2.12)
```

All of its nonzero zeros lie on the imaginary axis.  The coboundary therefore
does not cancel a pole arising from an off-critical zeta zero.

## 3. The exact energy exponent

For the triangular detector, fix `R_0>ell` and set

```text
mathcal E_ell(T)=integral_(R_0)^T abs(D_ell(R))^2 dR.      (3.1)
```

### Proposition 3.1 (scale-energy width)

Subject to the same explicit-formula input as the fixed-window theorem,

```text
limsup_(T->infinity)
 log(1+mathcal E_ell(T))/(2T)=Delta.                       (3.2)
```

Equivalently, the abscissa

```text
inf{sigma>0:
    integral_(R_0)^infinity exp(-2sigma R)abs(D_ell(R))^2 dR
    <infinity}                                             (3.3)
```

is exactly `Delta`.

For the upper bound, absolute summability on the zero side gives
`D_ell(R)=O_(ell,epsilon)(exp((Delta+epsilon)R))`.  For the
lower bound, suppose `exp(-sigma R)D_ell(R)` belonged to `L2` for some
`sigma<Delta`.  Cauchy--Schwarz would make its one-sided Laplace transform
holomorphic on `Re(s)>sigma`.  Choose an off-line zero with displacement
larger than `sigma`.  The fixed-window transform is nonzero at that node, so
the same Laplace transform has a genuine pole in this half-plane, a
contradiction.  The usual abscissa relation for the nondecreasing integral
in (3.1) gives (3.2).

This proves that scale averaging retains a single exceptional zero.  A
subexponential bound for (3.1) is still RH-strength; the proposition changes
the geometry of the estimate, not its logical strength.

## 4. Positive Gram form on the prime side

For `k=1`, define the critically centered logarithmic measure

```text
d eta(u)
 =sum_n Lambda(n)n^(-1/2)delta_(log n)(du)-exp(u/2)du.     (4.1)
```

For `R>ell`,

```text
D_ell(R)=integral w_ell(u-R)d eta(u).                     (4.2)
```

For a finite scale interval `I`, put

```text
K_I(u,v)=integral_I w_ell(u-R)w_ell(v-R)dR.               (4.3)
```

Then

```text
integral_I abs(D_ell(R))^2 dR
 =double_integral K_I(u,v)d eta(u)d eta(v).                (4.4)
```

The kernel is positive semidefinite because

```text
sum_(i,j)c_i c_j K_I(u_i,u_j)
 =integral_I [sum_i c_i w_ell(u_i-R)]^2 dR>=0.            (4.5)
```

It vanishes when `abs(u-v)>2ell`.  Thus (4.4) is a local multiplicative
dispersion form.  Unlike the indefinite Selberg/Hankel term, which couples
`u+v`, this is a Toeplitz-type autocorrelation coupling `u-v`.

Applying the same expansion to (2.6) gives

```text
sum_(m,n) a_(U,V)(m)a_(U,V)(n)/(sqrt(mn))
  * integral_I W_(ell,k)(R-log m)W_(ell,k)(R-log n)dR,    (4.6)
```

together with the two exact center cross terms and the center square.  No
cofactor, parity, dyadic, or Type-I sector has been squared separately.

## 5. Hardy-space audit and its boundary

For fixed `U,V` and `sigma>1/2`, ordinary Laplace Plancherel gives

```text
integral_0^infinity exp(-2sigma R)abs(B(exp R)-Z(exp R))^2 dR
 =1/(2pi) integral_R
   abs(H(s)A_(U,V)(s+1/2)-Zhat(s))^2 dt,                 (5.1)

s=sigma+it,
A_(U,V)(w)
 =(1-zeta(w)M_U(w))[-zeta'(w)/zeta(w)-L_V(w)].            (5.2)
```

The fourth-order factor in (5.1) is the complete modulus

```text
abs(H)^2 abs(1-zeta M_U)^2
 *abs(-zeta'/zeta-L_V)^2.                                 (5.3)
```

Splitting either modulus deletes required cross terms.  Extending (5.1) as
an `L2` bound from `sigma>1/2` to every `sigma>0` would exclude exactly the
off-line poles and is therefore not a free Hardy-space estimate.

Cutoff variance is also a false positive.  Exact cutoff transport gives

```text
F_alpha=C_full+E_alpha.                                   (5.4)
```

Hence variance over a family of cutoffs is just `Var(E_alpha)`, which is
small unconditionally because it projects out the common mode `C_full`.
Any cutoff-dispersion theorem must control the cutoff mean, not merely its
orthogonal variance.

## 6. The semiprime diagonal calibration

The positive diagonal in (4.6) is not small.  The first exact benchmark is
the following conventional consequence of the two-variable prime number
theorem.

### Lemma 6.1 (semiprime diagonal)

Let `0<theta<1/2`, and let `W` be a fixed nonnegative compactly supported
smooth function.  Then

```text
sum_(X^theta<p<q)
 (log(pq))^2/(pq) W(log(pq/X))
 ~log X * log((1-theta)/theta) * integral_R W(t)dt.        (6.1)
```

Indeed, write `p=X^u` and
`q=X^(1-u+t/log X)`.  The restriction `p<q` gives
`theta<u<1/2`, and the prime densities reduce the main term to

```text
log X * integral_theta^(1/2)du/[u(1-u)] * integral W
 =log X * log((1-theta)/theta) * integral W.              (6.2)
```

Because of (2.3), this is literally the distinct-semiprime part of the
equal-total-product diagonal.  A proposed dispersion engine must identify
where its negative counterpart occurs among unequal products and the exact
center cross terms.  An estimate of the diagonal alone cannot work.

## 7. Fixed-step spectral cooling

The manuscript's growing-order regime keeps the total width `ell` fixed and
sets `h=ell/k`.  That localizes the Type-II variables but does not damp a
fixed zero mode: its centered multiplier tends to one.  A different regime
does produce a genuine contraction.

Fix `h>0`, let the order `k` grow, and allow the total width

```text
ell_k=kh.                                                  (7.1)
```

For the compact coboundary, the zero-mode multiplier is

```text
G_(h,k)(s)
 =(exp(khs)-1)H_(h,k)(s)
 =[2sinh(khs/2)/s]
   [sinh(hs/2)/(hs/2)]^k.                                 (7.2)
```

On the critical line,

```text
abs(G_(h,k)(i gamma))
 <=2/abs(gamma) * abs(sinc(h gamma/2))^k.                  (7.3)
```

The zeta divisor has no node with `gamma=0`.  Consequently, for fixed `h`
there is a `q_h<1` controlling the low zero ordinates, while the elementary
`1/abs(gamma)` bound controls the high tail.  Riemann--von Mangoldt counting
then gives exponential decay in `k` for the absolutely summed critical-line
contribution.

The conclusion is different off the line.  For
`s_0=delta+i gamma`, `delta!=0`, neither factor in (7.2) vanishes and

```text
log abs(G_(h,k)(s_0))=O_(h,s_0)(k).                       (7.4)
```

The corresponding mode therefore has size

```text
exp(delta R+O_(h,s_0)(k)).                                (7.5)
```

It survives whenever `k=o(R)`.  The coboundary also cancels the `s=0`
Perron residue which makes the primitive `C_(h,k)` tend to a constant under
RH.  Thus fixed-step repeated scale averaging exponentially cools every
critical-line oscillation while retaining every off-line exponential drift.
This is the actual cancellation operator proposed here.

There is a real uniformity cost.  Re-running the Euler proof with fixed `h`
and support extending down to `exp(-hk)` gives a constant of size at most

```text
exp(O_h(k^2+k log(k+2))),                                 (7.6)
```

not the fixed-total-width `exp(O_ell(k log k))` bound.  If

```text
U=V=floor(x^(1/2-c/k)),       c>1/4,                      (7.7)
```

the logarithm of the Type-I error is bounded by

```text
O_h(k^2+k log(k+2))-(2c-1/2+o(1))log x,                  (7.8)
```

and the support condition requires

```text
h k^2 <=(2c+o(1))log x.                                   (7.9)
```

Hence a schedule such as

```text
k(R)=floor(R^alpha),        0<alpha<1/2,                  (7.10)
```

leaves the Euler error power-small while putting both Type-II variables in
`x^(1/2+o(1))` and the cofactor in `x^o(1)`.

The correct converse should first be proved for a locally constant schedule:
take `R_j=2^j`, set `k=k_j=floor(R_j^alpha)` on
`[R_j,2R_j)`, and use the complete coboundary energy on each block.  Under
RH, (7.3) makes that energy subexponential (in fact the zero part is
exponentially cooled in `k_j`).  If an off-line zero exists, a cardinal
function isolating its quartet together with (7.5) should force energy
`exp(2delta R_j-o(R_j))`.  This blockwise oscillation argument is still a
proof obligation; an arbitrary adaptive schedule is not covered.

Fixed-step cooling supplies a contraction and a faithful false-world signal.
The full/exact-head field now has the unconditional Vinogradov--Korobov
upper bound

```text
E_I^full <=exp[R-c_h R^(4/5)(log R)^(-3/5)].             (7.11)
```

See [`FULL-FIELD-VK-SUBPOWER-BOUND.md`](FULL-FIELD-VK-SUBPOWER-BOUND.md).
The periodic-Euler estimate (7.6)--(7.9) now transfers the same bound to the
frozen-cutoff field with its evaluated rank-two center.  This does not give a
fixed exponential saving or prove the varying-test converse.  The remaining
arithmetic question is whether a genuinely new joint estimate improves the
imported subpower saving to a fixed power.

## 8. Finite falsification

The exploratory unit-ramp probe used `U=V=floor(x^(3/8))` on 25 geometric
points from `10^4` to `10^7`.

* The raw triple-sum `L1` mass grew from `77.6` to `11359.2`, while the
  centered residual stayed near `-2.68`.
* The exact cofactor blocks reinforced: the median of
  `abs(B)/sum_m abs(S_m)` was `0.999998`.
* Dyadic cross energies changed sign and supplied no stable orientation.
* At `x=10^7`, the parity sectors were approximately

```text
omega(d)=1  -2588.08
omega(d)=2  +5109.55
omega(d)=3  -3098.25
omega(d)=4   +551.26
omega(d)=5    -12.02.                                    (7.1)
```

This is substantial sieve-parity cancellation, but `B` remained within one
independent-squarefree-sign standard deviation throughout the scan.  It is
not anomalous finite evidence for an RH-scale law.  The experiment rules out
independent cofactor randomness and a fixed dyadic sign.  It does not test
the completed coboundary energy in (4.6).

The reproducible probe is `src/type2_block_mechanism_probe.py`.

The separate fixed-step probe verifies (7.2) and a direct finite von
Mangoldt coboundary.  At the default

```text
h=0.1, k=32, gamma=14.134725..., delta=0.1, R=1000,
```

it reports

```text
critical-line contraction       0.0665577354,
off-line core log-amplitude    97.2904623,
total log support width         3.2.                       (8.1)
```

Thus the same filter strongly damps both critical and off-critical
oscillation factors, but the latter still has the positive drift
`delta R+o(R)` on a sublinear schedule.  This is a universal low-pass
effect, not numerical evidence for RH.  The reproducible implementation is
`src/fixed_step_spectral_cooling_probe.py`.

## 9. Fair next tests

1. Prove Proposition 3.1 and Lemma 6.1 in publication-ready detail.  The full
   `k>1` explicit formula is now proved for the cutoff-independent exact-head
   field, and the frozen-center transfer is proved by classical synthesis, in
   [`FULL-FIELD-VK-SUBPOWER-BOUND.md`](FULL-FIELD-VK-SUBPOWER-BOUND.md).
2. Prove or falsify the locally constant fixed-step converse in Section 7,
   including the zero-isolation estimate.  The
   `exp(O_h(k^2+k log k))` Euler trace is now imported; do not use an adaptive
   schedule.
3. Implement (4.6) on logarithmic scale blocks.  Report the equal-product
   diagonal, unequal-product term, the two center cross terms, and the final
   energy; never report only sectorwise absolute values.
4. Treat the full and frozen-center Vinogradov--Korobov bounds as imported
   calibration lemmas.  Do not count another derivation of their subpower
   exponent as progress toward a fixed strip.
5. Search for a low-frequency product-correlation estimate after
   total-product grouping.  It must cancel (6.1) jointly with the center and
   must not replace the complete coefficient `a_(U,V)(n)` by separate
   cofactor norms.  A standard large-sieve bound that returns only the
   diagonal is insufficient.  The first Ward/Markov attempt is audited in
   [`WARD-INNOVATION-SCREENING-CANDIDATE.md`](WARD-INNOVATION-SCREENING-CANDIDATE.md):
   its local, higher-cumulant, and nonlocal lifts all fail.  Exact completion
   identifies the proposed global remainder with the original completed
   energy minus the tail diagonal; see
   [`NONLOCAL-WARD-COVARIANCE-NOGO.md`](NONLOCAL-WARD-COVARIANCE-NOGO.md).
   A revival must therefore be a genuinely new cutoff-complete two-shift
   correlation estimate for the full energy, not another Ward relabeling.
   The exact two-frequency formula, failed shortcut gates, and surviving
   fixed-power target are recorded in
   [`DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md`](DIRECT-CUTOFF-COMPLETE-TWO-SHIFT-GATE.md).
   The last Mobius-specific cutoff/Riccati attempt, including the optimized
   candidate Vinogradov--Korobov calibration and its remaining uniformity
   obligations, is audited in
   [`MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md`](MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md).
6. Treat a bound

```text
mathcal E_ell(T)<<exp((1-2eta+o(1))T)                     (8.1)
```

   as a new fixed zero-free strip, and
   `mathcal E_ell(T)=exp(o(T))` as RH itself.  These are success thresholds,
   not intermediate estimates to assume.

The candidate survives the repository's finite-rank Hankel, cutoff-variance,
fixed-cofactor, and coefficient-norm no-go results because it uses an
infinite-rank positive autocorrelation **after** exact completion.  Whether
the actual arithmetic off-diagonal can be controlled remains completely
open.
