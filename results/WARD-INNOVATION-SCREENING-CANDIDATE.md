# Ward--innovation screening for the near-square Type-II energy

Status: exact identities and asymptotic calibration retained; local,
higher-cumulant, and nonlocal Ward--innovation lifts closed; 2026-08-06.
This note does **not** prove a new zero-free region or the Riemann Hypothesis.

## 1. Verdict

The fixed-step coboundary from R71 exposes a second cancellation candidate
which is not a large-sieve estimate.

1. Repeated logarithmic averaging has an exact law-of-total-variance
   decomposition.  The retained low-pass energy is the raw energy minus a
   nonnegative accumulated innovation.
2. Selberg's coefficient identity

   ```text
   Lambda log+Lambda*Lambda=mu*log^2                         (1.1)
   ```

   is a Ward identity for the multiplicative convolution.  On a distinct
   semiprime it splits the large equal-product diagonal into a connected
   collision term and a factor-ratio anisotropy.
3. If the two prime factors are restricted to
   `x^(1/2+/-delta)`, the connected term has linear size in `delta`, whereas
   the anisotropy is cubic in `delta`.

For the R71 choice `delta=c/k`, the connected term therefore accounts for
all but an `O(k^-2)` fraction of the semiprime diagonal.  After normalizing
the compact window in `L2`, the remaining diagonal is of size `O(R/k^3)`,
where `R=log x`.  This creates a nonempty experimental schedule

```text
R^(1/3)<<k<<R^(1/2).                                      (1.2)
```

The upper inequality is the fixed-step Euler/support constraint; the lower
inequality makes the normalized anisotropy tend to zero.  Only polynomial,
rather than vanishing, residual energy is needed for the RH criterion, so
the lower inequality is a calibration rather than a logical necessity.

The attempted lift is now closed in its local, higher-cumulant, and nonlocal
forms.  The local calculation supplies only one of the two required
`Lambda*Lambda` copies, and factor swapping isolates the anisotropy rather
than the connected channel.  More decisively, exact Vaughan completion makes
the proposed global remainder identically equal to the original completed
covariance energy minus the tail diagonal.  Selberg's one-product identity
can relabel that diagonal but gives no sign to the center or unequal-product
Gram entries.  A complete finite B-spline/Vaughan diagnostic violates all
four natural orientations in the same configuration.  See
[`NONLOCAL-WARD-COVARIANCE-NOGO.md`](NONLOCAL-WARD-COVARIANCE-NOGO.md).

Thus the Ward/Wick subtraction remains an exact, faithful, but indefinite
renormalization.  The cubic anisotropy remains a useful calibration.  Neither
is a positive cancellation mechanism, and subtracting the semiprime diagonal
in isolation would still be invalid.

## 2. Exact Markov innovations

For `h>0`, let

```text
(P_h f)(R)=h^(-1) integral_0^h f(R-u)du.                  (2.1)
```

For a complex-valued `f`, define its one-step carre du champ by

```text
Gamma_h(f)
 =P_h abs(f)^2-abs(P_h f)^2
 =(2h^2)^(-1) integral_0^h integral_0^h
     abs(f(R-u)-f(R-v))^2 du dv>=0.                       (2.2)
```

Iteration gives the exact telescope

```text
P_h^k abs(f)^2-abs(P_h^k f)^2
 =sum_(j=0)^(k-1) P_h^(k-1-j) Gamma_h(P_h^j f).           (2.3)
```

There is also a one-shot form, which is the more promising one here.  If
`S_k,S_k'` are independent sums of `k` uniform variables on `[0,h]`, then

```text
P_h^k abs(f)^2-abs(P_h^k f)^2
 =1/2 E abs(f(R-S_k)-f(R-S_k'))^2.                        (2.4)
```

Take `f` to be the sharply cut off, critically centered von Mangoldt
primitive.  Then `P_h^k f` is exactly its order-`k` B-spline residual.  The
same remains true after the scale coboundary because translations commute
with `P_h`.

For the Type-II lift it is better not to return all the way to the sharp
state.  Set `C_j=P_h^j C_0`, including its complete center, and take
`j` and `m` both comparable to `k`.  Then

```text
P_h^m abs(C_j)^2-abs(C_(j+m))^2
 =1/2 E abs(C_j(R-S_m)-C_j(R-S_m'))^2.                   (2.4a)
```

Every signal in (2.4a) now has smoothing order comparable to `k`, so all of
its Vaughan representations retain `x^(1/2+O(1/k))` geometry.  This is the
terminal macro innovation meant below.

This identity has the right false-world fidelity.  Put

```text
a_h(s)=(1-exp(-hs))/(hs).
```

For one exponential mode,

```text
P_h^k exp(sR)=a_h(s)^k exp(sR).                            (2.5)
```

If `s=i gamma`, `gamma!=0`, then `abs(a_h(s))<1`.  If
`s=delta+i gamma`, `delta>0`, its logarithmic output size is

```text
delta R+k log abs(a_h(s))=delta R+O_(h,s)(k).              (2.6)
```

Thus every critical-line oscillation is cooled exponentially in `k`, while
an off-line mode survives whenever `k=o(R)`.  Dividing the final compact
window by a polynomial factor such as its `L2` norm does not alter this
conclusion.

Equation (2.3) is not by itself a bound: Jensen gives only
`abs(P_h^k f)^2<=P_h^k abs(f)^2`.  A proof needs an arithmetic reason why the
innovation removes almost all of the dangerous raw energy.

## 3. The Selberg Ward identity

Let

```text
b(n)=Lambda(n)log n+(Lambda*Lambda)(n).                   (3.1)
```

The Dirichlet-series calculation

```text
-K'(s)+K(s)^2=zeta''(s)/zeta(s),
K(s)=-zeta'(s)/zeta(s),                                   (3.2)
```

gives coefficientwise

```text
b=mu*log^2.                                                (3.3)
```

Equivalently, `b*1=log^2`.  More generally, `mu*log^j`
vanishes on integers with more than `j` distinct prime factors.  This is a
finite-difference or connected-cluster truncation, not a probabilistic
heuristic.

The standard Selberg symmetry estimate implies a local screening sum rule.
For a fixed compactly supported `C^1` function `w`, with `R=log X`, partial
summation gives

```text
sum_n b(n)/n * w(log(n/X))
 =2R integral w(u)du+2 integral (u+1)w(u)du+O_w(1).       (3.4)
```

This is the honest arithmetic analogue of a second-moment Ward or
Stillinger--Lovett relation.  Its ordinary inversion is not useful:
recovering `b` from `b*1=log^2` inserts `mu`, and the corresponding analytic
condition operator contains `1/zeta` or `1/zeta^2`, as recorded in R67.

## 4. Cubic factor-ratio defect

Let `0<theta<1/2`, put `delta=1/2-theta`, and let `W` be a fixed nonnegative
compactly supported smooth function.  For distinct primes in the central
Type-II range define

```text
S_theta(X)
 =sum_(X^theta<p<q)
   (log(pq))^2/(pq) W(log(pq/X)),                          (4.1)

C_theta(X)
 =sum_(X^theta<p<q)
   4log(p)log(q)/(pq) W(log(pq/X)),                        (4.2)

A_theta(X)
 =sum_(X^theta<p<q)
   (log(q)-log(p))^2/(pq) W(log(pq/X)).                    (4.3)
```

At every summand,

```text
(log p+log q)^2
 =4log p log q+(log q-log p)^2
 =2(Lambda*Lambda)(pq)+(log q-log p)^2.                   (4.4)
```

Hence `S_theta=C_theta+A_theta` exactly.  The two-variable prime number
theorem gives

```text
S_theta(X)
 ~R log((1-theta)/theta) integral W,                       (4.5)

C_theta(X)
 ~4delta R integral W,                                    (4.6)

A_theta(X)
 ~R[log((1-theta)/theta)-4delta] integral W.              (4.7)
```

The remaining coefficient has the convergent expansion

```text
log((1+2delta)/(1-2delta))-4delta
 =16delta^3/3+64delta^5/5+... .                            (4.8)
```

Thus the Ward-labeled counterterm accounts algebraically for the entire
linear factor-ratio mass, leaving a positive cubic anisotropy.  This does not
mean that Markov innovation removes it: (4.4) is only a relocation of the
semiprime diagonal until the connected term is found with the opposite sign
among the innovation, unequal-product terms, and exact Type-I center.  The
local test in Section 6 shows that this opposite-sign match cannot be made
fiber by fiber.

### A canonical Ward/Wick subtraction

One useful operation is already legitimate.  In the completely expanded
R71 energy, let `mathcal C` be the central-semiprime diagonal obtained by
replacing `(log(pq))^2` with `4log(p)log(q)`, using exactly the same kernel,
cutoffs, and block.  Let `mathcal A` use `(log(q)-log(p))^2`.  Then

```text
central semiprime diagonal=mathcal C+mathcal A             (4.9)
```

exactly, and (4.6) plus the Selberg identity makes `mathcal C` a canonical
connected counterterm rather than a fitted constant.  Define the
Ward/Wick-renormalized energy by

```text
mathcal E^W=mathcal E-mathcal C.                          (4.10)
```

On every fixed or regular sublinear schedule considered here,
`mathcal C=exp(o(R))`.  Subtracting it therefore leaves the exponential
width carrier unchanged: an off-line contribution to `mathcal E` is
exponential in `R`, while under RH both the original energy and the
counterterm are subexponential.  The central equal-product diagonal of
`mathcal E^W` is `mathcal A`, with the cubic coefficient (4.8).

This is an exact and faithful renormalization, but it sacrifices positivity.
A bound for `abs(mathcal E^W)` would bound the original energy after adding
back the explicit subexponential counterterm; no such bound is presently
known.  The point of the innovation bridge is to realize the same
subtraction through a positive fluctuation--dissipation identity instead of
declaring an indefinite renormalized form.

## 5. The fixed-step normalization and schedule

Let

```text
W_(h,k)(t)=Phi_(h,k)(t+kh)-Phi_(h,k)(t)                   (5.1)
```

be the R71 compact coboundary window.  Its integral is `kh`, and for fixed
`h` its squared norm satisfies

```text
norm(W_(h,k))_2^2 asymp_h kh.                             (5.2)
```

The latter is the central-limit plateau: away from two transition regions
of width `O_h(sqrt(k))`, the window is close to one on an interval of length
`kh`.

The diagonal energy uses `W_(h,k)^2` as its semiprime test weight.  With
`delta=c/k`, the raw anisotropy scale predicted by (4.7)--(4.8) is therefore

```text
R delta^3 norm(W_(h,k))_2^2
 asymp_h R/k^2.                                           (5.3)
```

This is polynomial in `R`, hence already subexponential.  For the sharper
calibration define

```text
V_(h,k)=W_(h,k)/norm(W_(h,k))_2.                          (5.4)
```

The normalized anisotropy is then

```text
(16c^3/3+o(1))R/k^3.                                     (5.5)
```

Choosing `k=R^alpha` with

```text
1/3<alpha<1/2                                             (5.6)
```

makes (5.5) tend to zero, preserves the false-world mode, and respects both
the `hk^2<=2cR+o(R)` support condition and the
`exp(O_h(k^2+k log k))` Euler trace from R71.

Equations (4.5)--(4.7) were stated for fixed `theta,W`.  Their uniform
version for `theta=1/2-c/k` and the growing B-spline family is a proof
obligation, not something silently supplied by the fixed-test theorem.

## 6. Why the two identities do not yet compose

There are five distinct obstructions.

1. **Toeplitz versus Hankel geometry.**  The innovation in (2.2) compares
   scale shifts and depends on differences.  The Ward convolution in (3.3)
   groups factor logs by their sum.  A div--curl-style or fluctuation--
   dissipation bridge is needed to put them in one formula.
2. **Completion.**  The `Lambda log` term, every cofactor, all unequal total
   products, and the exact Type-I center must occur before the connected
   term is canceled.  Applying (4.4) only to the positive semiprime diagonal
   repeats the sector-splitting error excluded by R68--R71.
3. **One-step accumulation.**  If an `O(R/j^3)` terminal estimate is inserted
   independently at `O(k)` levels of (2.3), the naive sum is `O(R/k^2)`.
   Requiring that to vanish conflicts with `k=o(sqrt(R))`.  The viable object
   is the one-shot macro innovation (2.4), or a telescope with an additional
   summable gain.
4. **Universality of innovations.**  Equations (2.2)--(2.4) hold for a
   synthetic signal `exp((delta+i gamma)R)` as well.  They keep the false
   mode visible but cannot exclude it without additional arithmetic input;
   Section 7 shows that the proposed Ward lift does not supply that input.
5. **Local orientation and multiplicity.**  Put `x=log p`, `y=log q` on one
   central distinct-semiprime fiber.  The two tail assignments are `-y` and
   `-x` and have one common scale profile.  Their natural covariance cross
   is

   ```text
   2xy K=(Lambda*Lambda)(pq)K,                            (6.1)
   ```

   whereas the cubic decomposition uses `4xy K`.  The missing copy appears
   only after reclassifying the assignment self-squares by
   `x^2+y^2=2xy+(x-y)^2`; it is not generated by Markov covariance.  The
   factor-assignment swap has innovation `(x-y)^2/4`, exactly the
   anisotropic channel, so it removes the wrong part.  At `p^2`, subtracting
   `2(Lambda*Lambda)` even leaves a negative diagonal remainder.  Thus no
   coefficientwise positive Ward extraction works on all local fibers.

The continuous positive countermodel from R67 passes a power-saving PNT and
the ordinary `O(x)` Selberg remainder while retaining an off-line
exponential.  This already showed that a lift would have to use the exact
Mobius connected-cluster structure rather than the generic Selberg estimate.
Section 7 now shows that exact completion still supplies no independent sign.

## 7. The nonlocal remainder is closed

Let `a_n` be the grouped tail coefficient, `phi_n` its scale profile, `Z` the
complete center, and `K` the terminal covariance kernel.  The last candidate
was

```text
G=K(Z,Z)-2 sum_n a_n K(phi_n,Z)
  +sum_(n!=r) a_n a_r K(phi_n,phi_r).                     (7.1)
```

Put

```text
T=sum_n a_n phi_n,
D_tail=sum_n a_n^2 K(phi_n,phi_n).                        (7.2)
```

Polarization gives exactly

```text
D_tail+G=K(T-Z,T-Z).                                     (7.3)
```

The exact joint Vaughan identity from R70 now decides the issue.  If
`C_full` is the full von Mangoldt field minus its pole field and `E_Y` is the
signed error made when the exact Type-I head is replaced by its explicit
Euler evaluation, then

```text
T-Z=C_full+E_Y.                                          (7.4)
```

Consequently

```text
G=K(C_full+E_Y,C_full+E_Y)-D_tail.                        (7.5)
```

This is not a new Ward identity; it is the original completed energy in
Vaughan coordinates.  With the exact head `E_Y=0`.  With the approximate
head, the mixed term `2K(C_full,E_Y)` has no sign and cannot be bounded from
the size of `E_Y` alone before `K(C_full,C_full)` is controlled.

Selberg's relation can replace the chosen semiprime part of `D_tail` by its
connected term plus anisotropy.  It has no second product index and therefore
does not control the unequal-product or center terms in (7.1).  In Fourier
coordinates those terms contain the mandatory twist

```text
2log(p)log(q) cos(t log(p/q)),                            (7.6)
```

which changes sign; the ordinary Ward coefficient is only its value at
`t=0`, where the innovation multiplier vanishes.

The complete finite audit in
[`NONLOCAL-WARD-COVARIANCE-NOGO.md`](NONLOCAL-WARD-COVARIANCE-NOGO.md)
retains the actual grouped coefficient, every unequal product, the B-spline
profile, the continuous terminal law, and the smooth center.  One
three-product configuration and a larger 44-product replication violate
both possible signs for “supplying” the missing copy, innovation domination,
and retained-energy cancellation.

Therefore (7.1) is closed as an algebraic Markov/Ward lift.  An independently
proved cutoff-complete two-shift correlation estimate could still bound the
right side of (7.5), but that is a direct attack on the P4/R71 completed
energy rather than a new intermediate mechanism.

## 8. Higher connected Ward hierarchy is closed in its natural form

Identity (3.3) is the second member of an exact hierarchy:

```text
mu*log^r  <->  (-1)^r zeta^(r)/zeta.                     (8.1)
```

The right side is a Bell polynomial in `K=-zeta'/zeta` and its derivatives;
for example,

```text
zeta''/zeta=K^2-K',
-zeta'''/zeta=K^3-3KK'+K''.                              (8.2)
```

At a squarefree integer `n=p_1...p_r`,

```text
(mu*log^r)(n)=r! product_i log(p_i),                      (8.3)
```

and the coefficient vanishes when `n` has more than `r` distinct primes.
An equal-factor comparison can be forced by AM--GM:

```text
(sum_i a_i)^2
 -r^r product_i(a_i)/(sum_i a_i)^(r-2)>=0,
a_i=log(p_i),                                             (8.4)
```

with equality exactly when all factor logs agree.  But using (8.3) in (8.4)
requires division by `(log n)^(r-2)`: the Ward coefficient has log-degree
`r`, whereas the Type-II energy has degree two.

The cutoff-complete finite test kills this hierarchy more decisively.  For a
squarefree `n=product_i p_i`,

```text
a_Y(n)
 =sum_(p_i>Y) log(p_i)
   sum_(D subset {j:j!=i}, product_(j in D)p_j>Y)(-1)^|D|. (8.5)
```

If every prime exceeds `Y`, then `a_Y(n)=-log n`; however this sector is
empty near `n~X` for `r>=3` once `Y=X^theta` with `theta->1/2`.  In the
actual central geometry, take `n=2pq` or `n=6pq` with `p,q>Y`.  Cofactor
inclusion--exclusion gives

```text
a_Y(2pq)=a_Y(6pq)=0,                                     (8.6)
```

while `mu*log^3(2pq)` and `mu*log^4(6pq)` are strictly positive.  The
AM--GM connected counterterm is therefore positive where the exact completed
tail coefficient, and hence its square, is zero.  Other triple examples make
the proposed remainder change sign.

Consequently the untruncated higher Ward cumulants cannot be applied before
grouping without violating the R71 ordering, and after grouping they do not
give a sign-controlled decomposition.  A revival would require a genuinely
cutoff-adapted cumulant sharing the exact zeros of `a_Y`, not the hierarchy
`mu*log^r`.  Inverting any member also inserts `1/zeta` and remains
inadmissible.

## 9. Finite diagnostics

The finite tests separate several visually similar phenomena.

* The coefficient Ward identity was checked through `n=5000`; the largest
  floating closure error was `4.75e-14`.
* At `X=10^7`, `delta=0.1`, and a triangular product window of half-width
  `0.4`, the measured total, connected, and anisotropic coefficients were

  ```text
  total         0.397024112    predicted 0.405465108,
  connected     0.391606859    leading   0.400000000,
  anisotropy    0.005417253    predicted 0.005465108.
  ```

  The exact finite decomposition closed to roundoff.
* For the completed `ell=0.5` prime discrepancy on the output block
  `[8,10]`, `h=0.1`, the retained/raw Markov energy fractions at orders
  `1,4,16,32` were approximately

  ```text
  0.5381, 0.1329, 0.003625, 0.0001428.                    (9.1)
  ```

  At order `32`, innovations account for `99.9857%` of the sampled energy,
  and the telescope closes to `1.21e-17`.  This is expected low-pass
  behavior, not evidence for RH: an off-line exponential has essentially
  the same retained/raw fraction but still carries its `exp(delta R)` drift.

A separate finite-block Toeplitz audit found that the direct prime-atom
off-diagonal is nonnegative and that the smooth center supplies nearly all
the observed cancellation.  The residual agrees with the first critical
zeros' low-pass prediction.  Calling that observation "hyperuniformity"
would merely rename the R71 detector.

The exact semiprime-fiber gate additionally verifies that the terminal scale
covariance is rank one on the two assignments, its cross has only one Ward
copy, the factor swap returns the anisotropy, and the exact Type-I head
cancels the whole fiber.  The prime-square companion demonstrates that a
global positive anisotropy extraction cannot be obtained by simply
subtracting `2(Lambda*Lambda)` everywhere.

The complete nonlocal gate restores every grouped product and the smooth
center.  At `X=76,Y=5,h=0.05,j=m=1`, its three active products are
`70,77,78`, with central semiprime `77`.  Both signs for the missing-copy
claim, full-innovation domination, and retained-energy cancellation fail in
that one model; a 44-product run gives the same verdict.  The covariance and
Vaughan-polarization closures are stable to about `1e-15` under quadrature
refinement.  These are floating diagnostics, while (7.5) is the exact
analytic no-go.

The reproducible diagnostics are
[`src/prime_log_screening_probe.py`](../src/prime_log_screening_probe.py) and
[`src/ward_innovation_probe.py`](../src/ward_innovation_probe.py), together
with the exact rational finite gate
[`src/ward_vaughan_bridge_falsifier.py`](../src/ward_vaughan_bridge_falsifier.py)
and the complete covariance gate
[`src/ward_nonlocal_covariance_probe.py`](../src/ward_nonlocal_covariance_probe.py),
with focused unit tests.  The first two and the complete covariance gate are
ordinary floating calculations, not proof certificates; the rational gate
is exact finite algebra in Python, not a Lean theorem.
