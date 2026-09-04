# Symmetrized consecutive-gap dispersion: exact transfer gate

**Date:** 2026-08-13

**Verdict.**  No theorem-grade power saving beyond the truncated-trapezoid
transition was obtained from Vaughan transfer, prime-pair dispersion, or
finite inclusion--exclusion.  The attack does, however, isolate three exact
facts which narrow the remaining actual-prime problem.

1. The centered consecutive-gap weight is an exact mesh derivative.  Its
   prefix discrepancy from the natural von-Mangoldt weight is
   `x-vartheta(x)` at Voronoi boundaries.  Consequently a power-saving
   transfer in prefix/Abel norm is already a power-saving PNT, hence a
   zero-free strip.  Vaughan's natural-weight estimate cannot be transferred
   this way without circularly assuming the desired kind of input.
2. At a frozen rational frequency, forward/reverse symmetrization kills the
   **antisymmetric** part of the consecutive-residue transition matrix
   exactly.  It leaves its symmetric part untouched.  This is the precise
   content of the cancellation suggested by Kim's opposite-bias model.
3. Exact removal of “consecutive” introduces correlations of unbounded
   order.  A truncation after `K` interior primes has the exact Bonferroni
   remainder `binom(N-1,K)`.  In the mean-one Poisson benchmark, absolute
   control at relative size `Y^(-kappa)` requires

   ```text
   K >=(kappa+o(1)) log(Y)/loglog(Y),
   kappa=.0180303234.                                  (0.1)
   ```

   Thus fixed-order prime-pair or prime-tuple dispersion, used through this
   inclusion--exclusion transfer with an absolute remainder, does not close
   the gap, even after the useful symmetrization.

Items 1 and 2 are unconditional identities for the actual primes.  Item 3 is
a rigorous identity plus a **Poisson benchmark for absolute truncation**; it
is not a no-go theorem for actual primes or for a resummed, sign-sensitive
argument.  The live endpoint is a direct estimate at the `z=0` boundary of
the gap-renewal transform, or an equivalent frequency-specific symmetric
transition theorem.  No zero-free strip is claimed here.

---

## 1. The coefficient and its exact primitive

Work first in physical coordinates, away from the two fixed shell
endpoints.  Put

```text
g_j=p_(j+1)-p_j,
b_(j+1/2)=(p_j+p_(j+1))/2,
w_j=b_(j+1/2)-b_(j-1/2)=(g_(j-1)+g_j)/2.             (1.1)
```

The leading physical form of the logarithmic Voronoi coefficient is
`phi(log(p_j/Y)) w_j/Y`; the smooth factor and the `O(g^2/Y^2)` correction
do not affect the algebra below.  Telescoping gives the exact identity

```text
sum_(j=m)^n w_j=b_(n+1/2)-b_(m-1/2).                 (1.2)
```

Thus the cumulative Voronoi mesh measure equals physical length exactly at
cell boundaries.  Let

```text
vartheta(x)=sum_(p<=x) log p.
```

At `x=b_(n+1/2)`, with a fixed lower endpoint absorbed in a constant,

```text
sum_(j<=n)(w_j-log p_j)=x-vartheta(x)+constant.       (1.3)
```

For an arbitrary `x`, the same statement has an error bounded by the one
cell intersecting `x`.

### Proposition 1.1 (prefix transfer is strip-strength)

Suppose, uniformly on all sufficiently large dyadic shells, one proves

```text
sup_n |sum_(j<=n)(w_j-log p_j)| <<Y^(1-delta).        (1.4)
```

If the one-cell error is `O(Y^(1-delta))` (as it is for the present tiny-gap
truncation, and also for `delta=.018...` from standard maximal-gap bounds),
then

```text
vartheta(x)-x=O(x^(1-delta))                          (1.5)
```

after dyadic summation.  Mellin continuation of `-zeta'/zeta` then excludes
zeta zeros in `Re(s)>1-delta`.

This proposition does not say that every comparison with `Lambda` is
circular.  It rules out the particular black-box plan

```text
gap weights --power bound in prefix norm--> log p weights
            --Vaughan--> minor-arc cancellation.      (1.6)
```

A viable comparison must be frequency-specific and exploit cancellation
before taking the prefix supremum.  The known second gap moment only gives an
`l^2` coefficient comparison; the ordinary large sieve then gives an
average over frequencies and still permits the selected exceptional one.

---

## 2. What forward/reverse symmetrization cancels exactly

Freeze an additive rational phase `e_q(a n)=exp(2 pi i a n/q)`.  For a
physical interval containing complete consecutive-prime edges, define the
gap-mass transition matrix

```text
W_(r,s)=sum_(p_j=r mod q, p_(j+1)=s mod q) g_j.       (2.1)
```

The leading symmetric endpoint sum is

```text
F_q(a)
 =1/2 sum_j g_j[e_q(a p_j)+e_q(a p_(j+1))]
 =1/2 sum_(r,s) W_(r,s)[e_q(ar)+e_q(as)].             (2.2)
```

If

```text
R_r=sum_s W_(r,s),             C_r=sum_s W_(s,r),    (2.3)
```

then

```text
F_q(a)=1/2 sum_r (R_r+C_r)e_q(ar).                   (2.4)
```

Equivalently, (2.2) depends only on

```text
W_sym=(W+W^T)/2.                                     (2.5)
```

Every antisymmetric perturbation of the transition law vanishes.  This is
the exact finite statement behind the modeled cancellation between Kim's
forward and reversed prime-running biases.  It does **not** say that (2.4)
is small: the symmetric transition mass remains completely visible.

Grouping instead by the physical gap `h` gives another exact form,

```text
F_q(a)
 =sum_(h>=1) h/2 sum_(p,p+h consecutive)
       e_q(ap)[1+e_q(ah)].                            (2.6)
```

The factor in brackets suppresses transitions whose endpoint phases are
opposite and maximizes transitions whose endpoint phases recur.  Hence the
symmetrization is a directional filter, not generic cancellation.

For the logarithmic target, (2.2)--(2.6) apply to the frozen linear phase on
a curvature block, with the already audited Taylor and smooth-weight
bookkeeping.  They are not being asserted as an exact replacement of the
global phase `t log p`.

---

## 3. Why ordinary prime-pair dispersion stops before consecutiveness

For fixed endpoints `p,p+h`, put

```text
N_(p,h)=#{r: 1<=r<h and p+r is prime}.               (3.1)
```

Then

```text
1_(p,p+h consecutive)
 =1_P(p)1_P(p+h)1_(N_(p,h)=0).                       (3.2)
```

For every integer `K>=0` and `N>=0`, the binomial identity

```text
1_(N=0)
 =sum_(k=0)^K (-1)^k binom(N,k)
  +(-1)^(K+1) 1_(N>=1) binom(N-1,K)                 (3.3)
```

is exact.  The `k`th term in (3.3), inserted into (3.2), is a correlation of
the two endpoint primes with `k` distinct intermediate primes.  Thus a
prime-pair theorem is only the `k=0` layer; a fixed `k`-tuple theorem reaches
only finitely many Taylor coefficients of the no-intermediate-prime event.

This explains precisely why replacing “consecutive pair” by “prime pair” in
(2.6) is invalid for a signed Fourier sum.  A nonnegative upper-bound sieve
does not preserve its complex sign, and dropping the intermediate-prime
condition can add many pairs.

### 3.1 Quantitative order gate for absolute Bonferroni truncation

The relevant physical lengths include `h asyp log Y`, for which the standard
Poisson benchmark has `N` of mean one.  If `N` is Poisson with mean one, the
absolute remainder in (3.3) satisfies

```text
E[1_(N>=1) binom(N-1,K)]
 >=P(N=K+1)=exp(-1)/(K+1)!.                           (3.4)
```

Therefore an argument which disposes of the remainder in absolute value at
relative scale `Y^(-kappa)` must at least have

```text
log((K+1)!) >=(kappa+o(1))log Y.                     (3.5)
```

Stirling's formula turns (3.5) into (0.1).  This is deliberately scoped:

* it is a lower gate in the Poisson benchmark, not a theorem that actual
  prime interiors are Poisson;
* it applies to absolute truncation, not to a resummation that controls the
  alternating remainder with its phase;
* it shows why all imported results with fixed tuple order, even arbitrarily
  large fixed order, cannot by themselves certify a fixed power of `Y`.

The benchmark is nevertheless the favorable case for naive truncation.
When `h/log Y` is large, the binomial remainder becomes harder, not easier,
unless the long-gap tail is used before expansion.

---

## 4. The gap-renewal transform is the exact remaining boundary

Package all correlation orders at once by

```text
Z_(h,J)(z;alpha)
 =sum_(p in J) 1_P(p)1_P(p+h)
    z^[N_(p,h)] exp(2 pi i alpha p).                  (4.1)
```

Then

```text
Z(1;alpha) = ordinary prime-pair Fourier sum,
Z(0;alpha) = consecutive-prime-pair Fourier sum.      (4.2)
```

Derivatives at `z=1` are precisely the finite interior-prime correlations in
(3.3).  The desired edge sum (2.6) is a weighted sum of the `z=0` boundary
values, followed by forward/reverse symmetrization.  Existing pair
correlations, fixed-complexity higher-uniformity theorems, and restriction
estimates live at `z=1` or at finitely many derivatives.  None supplies
uniform analytic transport across the full unit interval to `z=0` with a
fixed power saving.

This formulation leaves three genuinely different live mechanisms:

1. a direct Type-II/dispersion identity for the symmetric `z=0` boundary;
2. a sign-sensitive cluster or renewal expansion controlling (4.1) uniformly
   from `z=1` to `z=0` at order at least (0.1);
3. a frequency-specific comparison of the centered mesh derivative with
   natural `Lambda` which never takes the strip-strength prefix norm (1.4).

Merely proving another natural-`Lambda` minor-arc estimate does not address
any of these three interfaces.

---

## 5. Literature scope

* Jaeyoon Kim,
  [*Prime Running Functions*](https://arxiv.org/abs/2006.13355), makes even
  the fixed-modulus forward main term conjectural for actual primes.  His
  proved expectation and variance statements concern a fixed-sieve random
  model.  The reversed opposite bias is a model prediction; identity (2.4)
  shows exactly which antisymmetric part it would cancel.
* Lemke Oliver--Soundararajan,
  [*Unexpected biases in the distribution of consecutive
  primes*](https://arxiv.org/abs/1603.03720), use uniform Hardy--Littlewood
  tuple conjectures and inclusion--exclusion for their precise asymptotic
  predictions.  This supports the architecture (3.3), but is not an
  unconditional growing-order estimate.
* Gallagher,
  [*On the distribution of primes in short
  intervals*](https://doi.org/10.1112/S0025579300016442), obtains Poisson gap
  laws conditionally from sufficiently uniform Hardy--Littlewood
  asymptotics.  It does not provide the unconditional, phased `z=0` estimate
  in (4.2).
* Matomaki--Radziwill--Tao,
  [*Correlations of the von Mangoldt and higher divisor functions
  I*](https://arxiv.org/abs/1707.01315), prove an almost-all-shifts
  `Lambda(n)Lambda(n+h)` theorem down to shift-window exponent `8/33`.
  It averages the shift, has no consecutiveness condition or additive phase,
  and controls only the pair boundary `z=1`.
* Matomaki--Radziwill--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals II: almost
  all intervals*](https://arxiv.org/abs/2411.05770), reach ordinary `Lambda`
  in almost all intervals of length `X^(1/3+epsilon)`, with logarithmic
  saving and fixed complexity.  Their theorem is not uniform growing-order
  control of (4.1).
* Ford--Maynard,
  [*On the theory of prime-producing
  sieves*](https://arxiv.org/abs/2407.14368), prove optimality results for
  their precise Type-I/Type-II axioms.  Those results do not eliminate a new
  coefficient-specific identity at `z=0`; they do prevent a vague appeal to
  Type-I information from being treated as such an identity.

No source above proves a power bound for (4.1) at `z=0`, for its symmetric
transition marginal (2.4), or for the global logarithmic target.  Conversely,
none proves that the actual-prime route is impossible.

---

## 6. Updated disposition

```text
natural Lambda minor-arc saving:                ample but nontransferable;
prefix/Abel coefficient transfer:               strip-strength (exact);
forward/reverse first-bias cancellation:         exact antisymmetric only;
prime-pair dispersion:                           z=1, not consecutive z=0;
fixed-order absolute inclusion--exclusion:       no fixed-power remainder;
growing-order absolute benchmark:                K~kappa logY/loglogY;
actual-prime symmetric z=0 dispersion:            OPEN.                 (6.1)
```

The algebra and the finite identities are checked by

```bash
python3 results/verify_zeta23_sym_gap_dispersion_gate.py
```
