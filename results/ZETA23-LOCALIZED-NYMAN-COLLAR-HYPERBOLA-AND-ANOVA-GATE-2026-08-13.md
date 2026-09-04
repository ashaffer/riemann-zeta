# Localized Nyman collar: harmonic hyperbola and ANOVA gate

Status: focused arithmetic attack, 2026-08-13.

Binary verdict: **no bound `Q_(p,b)(n)=n^o(1)` is proved for any fixed
`b<1`, even along a subsequence**.  The exact floor sum does, however,
collapse to a short-cofactor harmonic transform of one centered Mertens
function.  For `p=2`, its first collar further splits exactly into one
scalar carrier and one positive bridge energy.  These are narrower targets
than the original Nyman norm and show precisely why current short-interval
and Type-II results do not close the millionth-wide test.

Put

```text
delta=1-b,                 R=floor(n^(1/b)),
K=floor(R/n)=n^((1-b)/b+o(1)).                       (0.1)
```

The exponent ledger is

```text
target                                      Q_(p,b)(n)=n^o(1)
trivial bound                               Q_(p,b)(n)<<n^(1-b)
best bound obtained from VK                 n^(1-b) exp(-c_b L(n))
L(n)                                        (log n)^(3/5)(loglog n)^(-1/5)
b=.999999 missing fixed exponent            0.000001
p=2 first-collar target                     n^(2.999998+o(1))
current fixed-power conclusion              NOT PROVED.                 (0.2)
```

Since `L(n)=o(log n)`, the displayed unconditional bound is
`n^(1-b-o(1))`, not `n^o(1)`.  Passing to an unspecified unbounded sequence
does not turn this proved upper bound into the target.

## 1. Normalization and the exact harmonic-hyperbola identity

Use the notation of the quantitative Nyman report:

```text
M(x)=sum_(k<=x)mu(k),
g(n)=sum_(k<=n)mu(k)/k,
gamma(n)=sum_(k<n) M(k)/[k(k+1)],
C_n=n gamma(n),

F_n(m)=1-sum_(k<=n)mu(k)floor(m/k)
          +n g(n)floor(m/n).                         (1.1)
```

Abel summation gives

```text
g(n)=M(n)/n+gamma(n),       n g(n)-M(n)=C_n.         (1.2)
```

The prime number theorem implies both `g(n)->0` and `M(n)/n->0`, so (1.2)
also gives the useful future-tail identity

```text
gamma(n)=-sum_(t>=n) M(t)/[t(t+1)].                  (1.3)
```

### Proposition 1.1 (exact harmonic transform)

For every pair of integers `m>=n>=2`, with `r=floor(m/n)`, one has

```text
F_n(m)=sum_(j<=r) {M(floor(m/j))+C_n}.                (1.4)
```

#### Proof

The elementary Mobius identity

```text
sum_(k<=m)mu(k)floor(m/k)=1
```

turns (1.1) into

```text
F_n(m)=sum_(n<k<=m)mu(k)floor(m/k)+r n g(n).
```

Layering the floor and using `j<=r` gives

```text
sum_(n<k<=m)mu(k)floor(m/k)
 =sum_(j<=r)sum_(n<k<=m/j)mu(k)
 =sum_(j<=r){M(floor(m/j))-M(n)}.
```

Now use (1.2).  QED

Thus, with

```text
G_n(t)=M(t)+C_n,                                      (1.5)
```

the full critical Nyman window is the finite harmonic transform

```text
F_n(m)=sum_(j<=m/n)G_n(floor(m/j)),
1<=j<=K=n^((1-b)/b+o(1)).                            (1.6)
```

There is an equivalent increment form.  Since `F_n(n-1)=0`, define

```text
a_n(q)=F_n(q)-F_n(q-1)
      =sum_(k|q, k>n)mu(k)+n g(n)1_(n|q).            (1.7)
```

Then

```text
F_n(m)=sum_(n<=q<=m)a_n(q).                           (1.8)
```

On `q<=R`, every exterior divisor is `k=q/j` with the cofactor
`j<=K`.  This is the exact short-cofactor Type-I/II formulation; no
Vaughan remainder or smoothing error has been introduced.

## 2. A two-sided reduction to centered Mertens energy

Recall

```text
Q_(p,b)(n)^p
 =sum_(n<=m<=R)|F_n(m)|^p m^(-1-pb),       1<=p<=2. (2.1)
```

### Proposition 2.1 (weighted harmonic Hardy bound)

For fixed `0<b<1` and `1<=p<=2`,

```text
Q_(p,b)(n)^p
 <=C_(p,b) n^(1-p)R^(p(1-b))
      sum_(n<=t<=R)|M(t)+C_n|^p/t^2.                 (2.2)
```

For all sufficiently large `n` (so that `R>=2n-1`), one also has the
necessary first-collar bound

```text
Q_(p,b)(n)^p
 >=(2n)^(-1-pb)
      sum_(n<=t<2n)|M(t)+C_n|^p.                     (2.3)
```

#### Proof

By (1.4) and the convexity inequality
`|sum_(j<=r)z_j|^p<=r^(p-1)sum_(j<=r)|z_j|^p`, the left side of (2.2) is at
most

```text
sum_(m<=R)m^(-1-pb)(m/n)^(p-1)
 sum_(j<=m/n)|G_n(floor(m/j))|^p.                    (2.4)
```

For fixed `(j,t)`, the condition `floor(m/j)=t` restricts `m` to the at
most `j` integers in `[jt,j(t+1))`.  Put `a=p(1-b)>0`.  Their contribution
to (2.4) is at most

```text
n^(1-p) j^(a-1)t^(a-2)|G_n(t)|^p.                   (2.5)
```

Since

```text
sum_(j<=R/t)j^(a-1)<<_a(R/t)^a,
```

summing (2.5) proves (2.2).  On `n<=m<2n`, (1.4) has only `j=1`, so
`F_n(m)=G_n(m)`; comparison of the weights with `(2n)^(-1-pb)` proves
(2.3).  QED

For `b=.999999`, the first collar enters the stated critical window only
after

```text
n^((1-b)/b)>=2,
```

roughly `n>=2^999999`.  This astronomical threshold is irrelevant to the
asymptotic implication but is an important finite-range hostile check.

Equations (2.2)--(2.3) isolate the actual arithmetic scale.  For `p=2`,
the first-collar consequence of `Q_(2,b)(n)=n^o(1)` is

```text
sum_(n<=m<2n)|M(m)+C_n|^2
 <=n^(1+2b+o(1)).                                    (2.6)
```

At `b=.999999`, the exponent on the right is `2.999998+o(1)`.  This is a
fixed, if tiny, saving over the coefficient-blind cubic scale.

## 3. Exact first-collar ANOVA: scalar plus bridge

The first collar admits a sharper decomposition than an appeal to a
generic Mertens moment.  Put

```text
A_n=n g(n),
P_h=sum_(j=1)^h mu(n+j),       0<=h<=n-1,
P_bar=n^(-1)sum_(h=0)^(n-1)P_h.                     (3.1)
```

Then `M(n+h)+C_n=A_n+P_h`.  Define the scalar carrier

```text
L_n=n(A_n+P_bar)
   =n^2g(n)+sum_(j=1)^(n-1)(n-j)mu(n+j)
   =sum_(m=n)^(2n-1)(M(m)+C_n).                      (3.2)
```

### Theorem 3.1 (exact ANOVA/bridge identity)

One has

```text
sum_(m=n)^(2n-1)|M(m)+C_n|^2
 =|L_n|^2/n
  +(1/n)sum_(0<=u<v<=n-1)
       |sum_(u<j<=v)mu(n+j)|^2.                     (3.3)
```

#### Proof

Ordinary ANOVA gives

```text
sum_h|A_n+P_h|^2
 =n|A_n+P_bar|^2+sum_h|P_h-P_bar|^2.                (3.4)
```

For any `n` real numbers `x_h`,

```text
sum_h|x_h-x_bar|^2
 =(1/n)sum_(u<v)|x_v-x_u|^2.                        (3.5)
```

Apply (3.5) to `x_h=P_h` and use
`P_v-P_u=sum_(u<j<=v)mu(n+j)`.  QED

Both terms in (3.3) are nonnegative.  Thus a proof of (2.6) cannot hide a
large mean carrier by cancellation against centered dispersion.  It needs
simultaneously

```text
|L_n|<=n^(1+b+o(1)),                                 (3.6)

sum_(0<=u<v<n)|sum_(u<j<=v)mu(n+j)|^2
 <=n^(2+2b+o(1)).                                    (3.7)
```

This is the sharpest smaller target found in this attack: one explicit
triangular Mobius scalar and one all-internal-interval bridge energy, at the
same selected `n`.

For comparison, direct expansion of the left side of (3.3) gives the
single signed-correlation ledger

```text
n A_n^2
+2A_n sum_(j=1)^(n-1)(n-j)mu(n+j)
+sum_(j=1)^(n-1)(n-j)mu(n+j)^2
+2sum_(d=1)^(n-2)sum_(j=1)^(n-1-d)
      (n-j-d)mu(n+j)mu(n+j+d).                      (3.8)
```

The diagonal in (3.8) is

```text
(3/pi^2)n^2+O(n^(3/2)),                              (3.9)
```

by the standard squarefree counting asymptotic.  It is safely below
(2.6).  The obstruction is the complete signed off-diagonal/mean
recombination, equivalently the two positive quantities in (3.3), not the
diagonal.

## 4. Strongest unconditional bound obtained here

Let

```text
V(x)=exp{-c (log x)^(3/5)(loglog x)^(-1/5)}.         (4.1)
```

After decreasing `c>0` when necessary, the Vinogradov--Korobov estimate
and (1.3) give, uniformly for `t>=n`,

```text
|M(t)|<=t V(n),              |C_n|<=n V(n).          (4.2)
```

Indeed, the tail in (1.3) is bounded after the change of variables
`u=log t` by an integral of `exp(-c u^(3/5)(log u)^(-1/5))`; its polynomial
prefactor is absorbed by decreasing `c`.

For `rn<=m<(r+1)n`, (1.4), (4.2), and the harmonic-sum bound give

```text
|F_n(m)|
 <<n r(1+log(r+1))V(n).                              (4.3)
```

The original definition also gives `|F_n(m)|<=3n` for large `n`.  Hence,
with `W=V(n)(1+log(K+1))`,

```text
|F_n(m)|<<n min(1,rW).                               (4.4)
```

Grouping (2.1) into the blocks `rn<=m<(r+1)n` yields

```text
Q_(p,b)(n)^p
 <<n^(p(1-b)) sum_(r<=K)r^(-1-pb)min(1,(rW)^p).
```

Splitting at `r=1/W` (with the same bound if that point lies beyond `K`)
shows that the last sum is `O_(p,b)(W^(pb))`.  Therefore

```text
Q_(p,b)(n)
 <<_(p,b)n^(1-b)
 exp{-c_b (log n)^(3/5)(loglog n)^(-1/5)}.           (4.5)
```

Logarithmic factors have again been absorbed into `c_b`.  For
`b=.999999`, (4.5) is

```text
n^.000001 exp{-c (log n)^(3/5)(loglog n)^(-1/5)}
 =n^(.000001-o(1)),                                  (4.6)
```

so it does not prove the desired `n^o(1)` on any theorem-selected
unbounded sequence.

## 5. Why current averaged-Mobius and Type-II inputs stop here

### 5.1 Almost-all short intervals

Matomaki--Radziwill prove cancellation in almost all intervals whose
length tends to infinity.  Their sequel explicitly notes that the
`o(1)` amplitude cannot in general be replaced by `h^(-c)`; the power
saving proved there is in the size of the exceptional set, not in the
retained long mean.

The sharper 2026 theorem of
Matomaki--Radziwill--Shao--Tao--Teravainen gives, for every **fixed** `A`,
an `H/(log X)^A` Mobius bound outside `O_A(X/(log X)^A)` starting points in
Corollary 1.2(i)'s range
`X^(1/3+epsilon)<=H<=X^(1-epsilon)` (with fixed `epsilon>0`).  At any one
eligible length, squaring and absorbing the exceptional set gives arbitrary
logarithmic savings in the starting-point-averaged mean-square ledger.  It
does not by itself give the all-length bridge estimate at one prescribed
starting point.  In any event,

```text
(log X)^(-A)=X^(-o(1))                               (5.1)
```

for every fixed `A`.  The constants are not uniform for taking
`A` of order `log X/loglog X`, which is what the fixed
`n^(-2(1-b))` saving in (2.6)--(3.7) would require.

Moreover, those theorems concern centered local behavior.  The scalar
`L_n` in (3.2) is an orthogonal ANOVA summand and is not removed by an
exceptional-set estimate for the bridge.  The freedom to choose `n` can
avoid finitely many exceptional sets at dyadic scales, but the resulting
amplitude remains logarithmic and no audited result controls `L_n` with
(3.6) at the same selected `n`.

### 5.2 Averaged Chowla

The averaged Chowla theorem controls averages of shifted Mobius/Liouville
correlations with qualitative or logarithmic decay.  Inserting those
estimates into (3.8) gives at best a subpower improvement over the cubic
absolute ledger.  The required saving in (2.6) is the fixed power
`n^(-2(1-b))`, however small `1-b` is.

### 5.3 Short-cofactor Type I/II

Formula (1.7) shows exactly what a decomposition must estimate.  The
`j=1` exterior-divisor branch is `mu(q)` itself.  Centered dispersion can
control nonprincipal variation, but restoring its mean gives (3.2), while
summing all cofactor branches with their signs reconstructs (1.4) exactly.
At additive frequency zero a rectangular bilinear piece factorizes, so a
large-sieve or nonzero-phase saving has no mechanism for the surviving
principal carrier.  Estimating the `j=1` branch separately by a fixed power
is already a fixed-power Mertens theorem; taking absolute values across
`j<=K` spends the full `n^(1-b)` budget.

## 6. Truth boundary and research target

What is proved here:

1. the exact harmonic-hyperbola identity (1.4) and increment identity
   (1.7);
2. the weighted sufficient/necessary reductions (2.2)--(2.3);
3. the exact first-collar ANOVA and signed-correlation formulas
   (3.3), (3.8);
4. the unconditional subexponentially improved bound (4.5);
5. the precise reason the audited modern inputs do not turn (4.5) into a
   fixed exponent saving.

What is not proved:

1. `Q_(p,b)(n)=n^o(1)` for a single fixed `b<1`;
2. (3.6)--(3.7) along an unbounded sequence;
3. a fixed-power averaged Mobius or Mertens estimate;
4. any new zero-free strip.

The narrowest surviving arithmetic experiment is now explicit.  For
`b=.999999`, seek an unbounded sequence of `n` on which **both**

```text
|n^2g(n)+sum_(j<n)(n-j)mu(n+j)|
     <=n^(1.999999+o(1)),                            (6.1)

sum_(0<=u<v<n)|sum_(u<j<=v)mu(n+j)|^2
     <=n^(3.999998+o(1))                             (6.2)
```

hold, and then control the remaining harmonic cofactors `2<=j<=K` through
(1.4) or the sufficient weighted energy (2.2).  This is smaller than
another global Nyman norm reformulation: (6.1) is one signed triangular
carrier, (6.2) is one positive bridge energy, and the number of remaining
cofactors is only `n^(0.000001000001...+o(1))`.  None is currently supplied
with a fixed power by the known inputs audited above.

## Primary sources used for the input audit

* K. Matomaki and M. Radziwill,
  [*Multiplicative functions in short intervals*](https://annals.math.princeton.edu/2016/183-3/p06),
  Ann. of Math. 183 (2016), 1015--1056.
* K. Matomaki and M. Radziwill,
  [*Multiplicative functions in short intervals II*](https://arxiv.org/abs/2007.04290).
* K. Matomaki, M. Radziwill, X. Shao, T. Tao, and J. Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals II: almost
  all intervals*](https://doi.org/10.1007/s00222-026-01408-6),
  Invent. Math. 244 (2026), 967--1091; see especially Corollary 1.2(i).
* K. Matomaki, M. Radziwill, and T. Tao,
  [*An averaged form of Chowla's conjecture*](https://arxiv.org/abs/1503.05121),
  Algebra Number Theory 9 (2015), 2167--2196.
