# R136 weak-tail and good-lambda audit

Status: the reciprocal weak-tail proposal is sharpened and materially
reclassified.  The exact weakest tail condition is an exponentially weighted
summability condition for the normalized endpoint tail.  More importantly,
the unit-increment property of the Mertens function converts **any** fixed
weak-`L^q` gain into a pointwise power saving.  Thus the weak-tail target
allows some exceptional values at a given quantitative exponent, but the
existence of any exponent `q>1` is not qualitatively weaker than proving some
pointwise power bound `M(x)=O(x^theta)`, `theta<1`.

An exact reciprocal-scale form of the divisor recurrence is also derived.
After global mean-zero centering, its linear floor-sum operator still has no
`L1 -> weak-Lq` bound for any `q>1`; a two-point centered input saturates the
weak-`L1` scaling.  This closes a coefficient-free martingale,
Calderon--Zygmund, or good-lambda bootstrap from the recurrence.  A successful
argument must use cancellations special to the actual Mobius coefficients,
not just reciprocal scaling, global centering, or the divisor-floor kernel.

These results do not prove a fixed zero-free strip.

```text
exact fixed-strip tail condition                 THEOREM (Section 2)
stationary normalized-tail good-lambda criterion THEOREM (Section 3)
weak-Lq plus unit increments => pointwise saving  THEOREM (Section 4)
existence of weak gain <=> some pointwise saving  THEOREM (Section 4)
reciprocal law for floor(N/k)                     EXACT (Section 5)
coefficient-free centered floor-operator bootstrap CLOSED (Section 6)
Mobius-specific normalized-tail contraction       OPEN
fixed zero-free strip                              NOT PROVED.       (1.1)
```

The statements called new below are new within this project audit.  The
spike-spreading argument is elementary and may be folklore; it is not claimed
as a literature-priority result.

## 2. The exact weakest tail target

Put

```text
nu({n})=1/[n(n+1)],
X(n)=|M(n)|,
T(U)=nu(X>U),
G(U)=U T(U).                                                (2.1)
```

The weights telescope, so `nu` is a probability measure and

```text
nu(n>=N)=1/N.                                               (2.2)
```

The trivial bound `|M(n)|<=n` gives the endpoint estimate

```text
T(U)<=1/(floor(U)+1)<=1/U,     G(U)<=1.                    (2.3)
```

For every `p>0`, layer cake gives

```text
sum_n |M(n)|^p/[n(n+1)]
 =p integral_0^infinity U^(p-1)T(U)dU.                     (2.4)
```

Fix any `A>1`.  Monotonicity of `T` on each interval
`[A^j,A^(j+1)]` proves the equivalence

```text
sum_n |M(n)|^p/[n(n+1)] < infinity
 <=> sum_(j>=0) A^(pj)T(A^j)<infinity
 <=> sum_(j>=0) A^((p-1)j)G(A^j)<infinity.                 (2.5)
```

The omitted initial interval contributes a finite amount.  For example, on
one geometric interval,

```text
(A^p-1)A^(pj)T(A^(j+1))
 <=p integral_(A^j)^(A^(j+1)) U^(p-1)T(U)dU
 <=(A^p-1)A^(pj)T(A^j),                                   (2.6)
```

and shifting the lower series by one index proves (2.5).

By the arithmetic Nyman--Beurling theorem imported and cited in
`R136-NYMAN-L1-LP-SELF-IMPROVEMENT-GATE.md`, a fixed zero-free strip is
therefore equivalent to

```text
there are A>1 and delta>0 such that
sum_(j>=0) A^(delta j)G(A^j)<infinity.                      (2.7)
```

This is strictly weaker as a tail formulation than demanding a uniform
weak-`L^q` estimate.  It is the exact minimal geometric tail-summability
target.  It also shows precisely why `G(A^j)->0` at only a subexponential
rate in `j`, as furnished by known PNT bounds, is insufficient: multiplying
by `A^(delta j)` makes the series diverge for every fixed `delta>0`.

## 3. The useful good-lambda form

The natural endpoint-normalized good-lambda target is

```text
G(AU)<=eta G(U),       eta<1,                               (3.1)
```

eventually, or merely at `U=A^j U_0`.  Iteration gives

```text
T(U) << U^(-q),
q=1+log(1/eta)/log A >1.                                   (3.2)
```

Consequently every `p<q` satisfies (2.4), and the zero-free half-plane is
`Re(s)>1/p`.  Notice that the contraction is imposed on `G(U)=UT(U)`, not
just on `T`: a fixed contraction of the unnormalized tail can still leave
the endpoint exponent equal to one.

The defect-tolerant version is the following.

**Proposition 3.1 (good-lambda with summable arithmetic defects).**  Let

```text
g_j=G(A^j U_0).
```

Suppose that

```text
g_(j+1)<=eta g_j+r_j,
eta A^delta<1,
sum_j A^(delta j)r_j<infinity                               (3.3)
```

for some `delta>0`.  Then

```text
sum_j A^(delta j)g_j<infinity,                              (3.4)
```

so `M_1` lies in `L^(1+delta)` and a fixed strip follows.

Indeed, iterate the first inequality, multiply by `A^(delta j)`, and sum
the resulting geometric convolution.  Condition `eta A^delta<1` makes its
operator norm finite.  This is the weakest standard good-lambda-shaped
target found in the audit: the defect need not vanish, but it must itself
have a fixed exponential gain on logarithmic scales.  A PNT-sized
subexponential defect cannot close (3.3).

## 4. Weak reciprocal tails already force pointwise power cancellation

The earlier R136 report emphasizes that a reciprocal weak tail allows sparse
large values.  That is quantitatively true, but the unit-increment geometry
of `M` sharply limits how sparse a large value can be.

**Theorem 4.1 (spike spreading).**  Let `a(0)=0` be real-valued with

```text
|a(n)-a(n-1)|<=1,       |a(n)|<=n.                          (4.1)
```

Use the measure `nu` in (2.1).

1. If, for some `q>0`,

   ```text
   nu(|a|>U)<=C U^(-q)                                    (4.2)
   ```

   for all `U>0`, then

   ```text
   |a(N)| <= C_q (1+C)^(1/(q+1)) N^(2/(q+1)).              (4.3)
   ```

2. If

   ```text
   K_p=sum_n |a(n)|^p/[n(n+1)]<infinity,                   (4.4)
   ```

   then

   ```text
   |a(N)| <= C_p (1+K_p)^(1/(p+1)) N^(2/(p+1)).            (4.5)
   ```

### Proof

Write `H=|a(N)|`.  The cases `H<4` are absorbed into the constants.  For

```text
N-floor(H/4)<=n<=N,                                        (4.6)
```

the Lipschitz property gives `|a(n)|>H/2`.  There are at least `H/4` such
integers, and their reciprocal weights are at least `1/[N(N+1)]`.  Hence

```text
nu(|a|>H/2) >= H/[4N(N+1)],                                (4.7)

sum_n |a(n)|^p/[n(n+1)]
 >=H^(p+1)/[2^(p+2)N(N+1)].                                (4.8)
```

Combining (4.7) with (4.2), and (4.8) with (4.4), proves
(4.3) and (4.5).  QED.

Apply the theorem to `a=M`, whose increments are `mu(n)` and hence have
absolute value at most one.  A weak-`L^q` estimate with any `q>1` gives

```text
M(N)=O(N^(2/(q+1))),       2/(q+1)<1.                       (4.9)
```

Conversely, if for some `theta>0`

```text
|M(N)|<=C N^theta,                                         (4.10)
```

then telescoping (2.2) gives

```text
T(U)<=C^(1/theta) U^(-1/theta),                            (4.11)
```

up to an inessential adjustment for bounded `U`.  In addition,

```text
sum_n |M(n)|^p/[n(n+1)]<infinity       whenever p theta<1. (4.12)
```

It follows that the following two existence statements are equivalent:

```text
there is q>1 for which M is reciprocal weak-Lq;
there is theta<1 for which M(N)=O(N^theta).                 (4.13)
```

Combining this with the imported arithmetic Nyman--Beurling equivalence and
(4.5), one obtains the qualitative four-way equivalence

```text
a fixed zero-free strip exists
<=> M belongs to reciprocal Lp for some p>1
<=> M belongs to reciprocal weak-Lq for some q>1
<=> M(N)=O(N^theta) for some theta<1.                       (4.14)
```

For the last implication back to a strip, (4.10) makes
`s integral_1^infinity M(x)x^(-s-1)dx` converge for
`Re(s)>theta`; there it equals `1/zeta(s)` by continuation from
`Re(s)>1`.  Thus `zeta` has no zero in that half-plane.

The exponents furnished in the two directions are not sharp inverses.  The
point is qualitative: the proposed weak-tail theorem is an alternate
packaging of a fixed power-saving problem, not a route that can tolerate
arbitrarily isolated near-linear spikes.  The same conclusion follows from
any strong reciprocal `Lp`, `p>1`, via (4.5).

This is the main correction to the strategic emphasis of the earlier R136
report.  Distributional methods may still be the right way to prove a power
saving, but weak higher integrability is not a genuinely lower-strength
asymptotic target once the known increment structure is retained.

## 5. The exact reciprocal-scale divisor recurrence

Let `N` be a random positive integer with law `nu`, and put `M(0)=0`.  The
tail identity (2.2) gives, for every integer `k,m>=1`,

```text
P(floor(N/k)=m)
 =P(km<=N<k(m+1))
 =1/(km)-1/[k(m+1)]
 =(1/k)nu({m}).                                             (5.1)
```

Thus `floor(N/k)` is zero with probability `1-1/k` and, conditional on
being positive, has exactly the original reciprocal law.  For

```text
(D_k f)(n)=f(floor(n/k)),       f(0)=0,                     (5.2)
```

one has the exact distributional identities

```text
nu(|D_k f|>U)=(1/k)nu(|f|>U),
||D_k f||_p^p=(1/k)||f||_p^p.                              (5.3)
```

Mobius inversion supplies the pointwise floor recurrence

```text
sum_(k>=1) M(floor(n/k))=1.                                (5.4)
```

Indeed,

```text
sum_(k<=n)sum_(d<=n/k)mu(d)
 =sum_(d<=n)mu(d)floor(n/d)=1.                              (5.5)
```

If

```text
(Qf)(n)=sum_(k=2)^n f(floor(n/k)),                          (5.6)
```

then (5.4) reads

```text
(I+Q)M=1.                                                  (5.7)
```

The PNT mean-zero identity

```text
sum_n M(n)/[n(n+1)]=0                                      (5.8)
```

and (5.3) show that each individual `D_k M` is centered.  This makes a
martingale or square-function interpretation tempting.  The next section
shows why reciprocal scaling and global centering alone cannot provide it.

## 6. Exact centered-operator obstruction

**Theorem 6.1.**  For every `q>1`, the operator `Q` in (5.6) is not of weak
type `(1,q)` even on the mean-zero subspace of `L1(nu)`.  More explicitly,
there are finitely supported integer-valued functions `f_N` such that

```text
integral f_N dnu=0,
||f_N||_L1(nu)=1,                                          (6.1)
```

but

```text
sup_(U>0) U^q nu(|Qf_N|>U) ->infinity.                     (6.2)
```

### Proof

For `N>=2`, set

```text
f_N(1)=-1,
f_N(N)=N(N+1)/2,
f_N(m)=0 otherwise.                                        (6.3)
```

Since `nu({1})=1/2` and `nu({N})=1/[N(N+1)]`, (6.1) is
immediate.  At the single output point `n=2N`, exactly one index (`k=2`)
has `floor(2N/k)=N`, while exactly `N` indices
`k=N+1,...,2N` have `floor(2N/k)=1`.  Therefore

```text
(Qf_N)(2N)=N(N+1)/2-N=N(N-1)/2.                            (6.4)
```

Take `U=N(N-1)/4`.  The point `2N` belongs to the strict superlevel set,
so

```text
U^q nu(|Qf_N|>U)
 >=[N(N-1)/4]^q/[2N(2N+1)]
 asymp_q N^(2q-2),                                         (6.5)
```

which diverges for every `q>1`.  QED.

The same example defeats the rank-one centered operator

```text
Q_0 f=Qf-n integral f dnu,                                 (6.6)
```

because its correction vanishes on `f_N`.  At `q=1`, (6.5) stays at
constant order: the construction exactly saturates the endpoint scaling
rather than merely exploiting a poor estimate.

Consequences:

* summing the exact diluted copies in (5.3) cannot be handled by triangle
  inequalities to gain an exponent;
* subtracting only the global reciprocal mean does not turn the floor kernel
  into a Calderon--Zygmund smoother;
* centeredness of the individual `D_k M` terms does not make them martingale
  differences or orthogonal increments.

This is a coefficient-free obstruction.  It does **not** rule out an
estimate that uses the full equation (5.7) and special sign relations among
the actual values of `mu`; the recurrence uniquely singles out `M`, while
the test functions (6.3) do not satisfy it.  It says exactly what extra input
is required: a Mobius-specific cancellation theorem strong enough to prove
the normalized-tail contraction (3.1) or its summable-defect version (3.3).

## 7. Why current local Mobius cancellation does not supply the missing input

The theorem of Matomaki and Radziwill proves cancellation of `mu` in almost
all short intervals whose lengths tend to infinity.  This is powerful
coefficient-specific information, but it controls **increments**

```text
M(x+H)-M(x),                                                (7.1)
```

not the accumulated level `M(x)`.  A large level can persist while most
subsequent short increments have mean close to zero.  To turn (7.1) into
(3.1), one needs a scale-uniform anchoring or excursion theorem showing that
large accumulated levels cannot persist on enough reciprocal mass.  No such
consequence is present in the short-interval theorem.

This logical distinction also survives logarithmically averaged two-point
Chowla estimates: fixed-shift or averaged local correlations do not control
the growing collection of shifts needed for a large-value excursion, nor do
they anchor the height inherited from all earlier scales.  Invoking a
martingale concentration inequality without a proved conditional mean-zero
filtration would insert precisely the missing theorem.

Primary comparison sources:

* K. Matomaki and M. Radziwill,
  [*Multiplicative functions in short intervals*](https://doi.org/10.4007/annals.2016.183.3.6),
  Ann. of Math. 183 (2016), 1015--1056.
* T. Tao,
  [*The logarithmically averaged Chowla and Elliott conjectures for
  two-point correlations*](https://arxiv.org/abs/1509.05422),
  Forum Math. Pi 4 (2016), e8.

These papers are used only to delimit available local information; no lemma
from them is imported into Sections 2--6.

## 8. Reproducible finite diagnostic

The companion script

```text
python3 src/r136_mertens_weak_tail_probe.py
```

does three low-memory checks:

1. an exact rational sieve through `200` plus the worst-case unseen mass
   `1/201` certifies two finite-scale normalized-tail contractions;
2. a default NumPy sieve through `10^6` reports truncated tail ratios with
   the rigorous but coarse unseen-mass interval `0<=tail remainder<=1/(N+1)`;
3. it prints the growth in (6.5) for several centered test inputs.

The finite contractions are sanity checks only.  A fixed strip requires an
eventual contraction at every logarithmic scale, or the exponentially
weighted summability (2.7); no finite computation can certify that.

## 9. Verdict and next theorem

The weak-tail branch should no longer be advertised as escaping pointwise
power cancellation through sparse exceptions.  The exact revised status is:

1. The weakest tail formulation is (2.7), not uniform weak-`L^q`.
2. The clean good-lambda theorem is normalized contraction (3.1), with
   (3.3) as the useful defect-tolerant form.
3. Unit increments spread every height-`H` spike across reciprocal mass at
   least a constant times `H/N^2`; hence any fixed weak exponent already
   gives a pointwise fixed power saving.
4. Reciprocal dilation, the exact divisor recurrence, and global centering
   do not yield a generic higher-tail estimate: Theorem 6.1 is a sharp
   centered obstruction.
5. Current short-interval Mobius cancellation controls increments but lacks
   the level anchoring needed by (3.1).

The next genuinely arithmetic target is therefore not merely “prove a weak
moment.”  It is the more explicit excursion theorem

```text
G(AU)<=eta G(U)+r(U),
eta<1,
sum_j A^(delta j)r(A^j)<infinity                            (9.1)
```

for the actual Mertens function, with a fixed `delta>0`.  By Theorem 4.1,
proving it necessarily contains enough coefficient-specific information to
force a pointwise Mertens power saving.  No such estimate is proved here.
