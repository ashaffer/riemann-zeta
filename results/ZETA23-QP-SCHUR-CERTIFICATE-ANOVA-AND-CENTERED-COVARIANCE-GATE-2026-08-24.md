# QP carrier Schur certificate: exact ANOVA and the centered covariance gate

**Date:** 2026-08-24  
**Verdict:** the finite inequality

```text
Delta+dbar <= sqrt(D)                                   (0.1)
```

does not have a plausible uniform geometric proof.  It succeeds in the
computed actual-prime range because those graphs still have mean degree
below one and very small maximum degree.  The cubic window alone gives only
`Delta<<D`; the corresponding all-integer matrices already violate (0.1)
strongly.

There is a sharper exact result.  After empirical constant centering, the
mean degree disappears completely.  The operator splits into

```text
a rank-two degree-fluctuation channel
       +
a doubly centered broad carrier operator.               (0.2)
```

The first channel has norm equal to the RMS degree fluctuation, not
`Delta+dbar`.  The square of the second is an explicit centered
common-neighbor covariance.  Thus the sharp carrier theorem is equivalent,
up to an absolute factor, to one selected-modulus BDH estimate and one
balanced mask-sensitive covariance estimate.  This reduction is exact.

No faithful actual-prime counterexample was found, and the two estimates in
(0.2) remain open asymptotically.

## 1. Exact meanings of `Delta` and `dbar`

Let `S=S(q)` be the narrow prime-power shell, `n=|S|`, and

```text
T_(b,c)=sum_(a in S) 1_(|8abc-q^3|<=qD),
d_b=sum_c T_(b,c),
E=sum_b d_b,
Delta=max_b d_b,
dbar=E/n,
mu=E/n^2=dbar/n.                                       (1.1)
```

Thus `dbar` is the mean row degree and `mu` is the mean matrix entry.  The
finite certificate used

```text
||T-mu J|| <= ||T||+||mu J|| <= Delta+dbar.             (1.2)
```

The first Schur bound in (1.2) is exact for a nonnegative symmetric matrix,
but the triangle inequality throws away the cancellation for which the
centering was introduced.

For a fixed carrier `b`, define

```text
I_b=[(q^3-qD)/(8b),(q^3+qD)/(8b)],
r_S,2(m)=#{(a,c) in S^2:ac=m}.                           (1.3)
```

Then the degree has the exact short-product formula

```text
d_b=sum_(m in I_b intersect Z) r_S,2(m).                 (1.4)
```

The shell endpoint ratio is `e^.4<2`, so it contains at most one power of
each base prime.  Unique factorization therefore gives

```text
r_S,2(m)<=2.                                             (1.5)
```

The interval length is

```text
|I_b|=qD/(4b)<=e^.2 D/2.                                 (1.6)
```

Consequently

```text
Delta<=2(floor(qD/(4 min(S)))+1)<<D.                     (1.7)
```

This is the full unconditional degree consequence of the product window
and prime-power Sidonicity.  It is `D`, not `sqrt(D)`.

That scale is compatible with the desired operator theorem.  Since the
entries of `T` are zero or one, the squared norm of the `b`-th centered
column is exactly

```text
||(T-mu J)e_b||_2^2=d_b-2mu d_b+n mu^2.                 (1.7a)
```

Thus one row of degree `D` naturally produces norm `sqrt(D)`, not `D`.
The original Schur argument lost this square root by replacing an `ell^2`
column norm with an `ell^1` row sum.  A maximum-degree `sqrt(D)` theorem is
therefore stronger than necessary even before considering its expected
failure.

The total edge count is exactly

```text
E=#{(a,b,c) in S^3:|8abc-q^3|<=qD}.                     (1.8)
```

Thus a uniform proof of `dbar<=sqrt(D)` would require a strong upper bound
for balanced three-prime products in the very short interval centered at
`q^3/8`.  The density heuristic is instead

```text
E~qD/(log q)^3,
dbar~D/(log q)^2.                                       (1.9)
```

Since `sqrt(D)/(log q)^2` tends to infinity, (1.9) predicts that the mean
degree itself eventually exceeds `sqrt(D)`.  This is a heuristic, not a
faithful counterexample: presently available short-almost-prime results do
not force balanced factors at the sparse centers `q^3/8` with `q` prime.
It does show why (0.1) is the wrong asymptotic target.

## 2. Exact constant/degree/broad ANOVA

Put

```text
u=n^(-1/2) 1,                 P=I-u u^T,
delta=d-dbar 1,               w=n^(-1/2) delta,
A=T-mu J,                     B=P T P.                   (2.1)
```

### Theorem 1 (exact carrier ANOVA)

One has

```text
A=B+u w^T+w u^T.                                        (2.2)
```

Moreover, `w` is perpendicular to `u`, and hence

```text
||u w^T+w u^T||=||w||
 =[(1/n)sum_b(d_b-dbar)^2]^(1/2)=:sigma_d.               (2.3)
```

Relative to `C u direct-sum u^perp`, the matrix is exactly

```text
A = [ 0    w^T ]
    [ w     B  ].                                        (2.4)
```

Therefore

```text
max(sigma_d,||B||)<=||A||<=sigma_d+||B||.                (2.5)
```

**Proof.**  Expanding `PTP` gives

```text
PTP=T-(d 1^T+1 d^T)/n+(E/n^2)J.                         (2.6)
```

Subtract (2.6) from `T-(E/n^2)J` and use
`d=dbar 1+delta` to obtain (2.2).  Since `sum delta=0`, the two summands in
the degree channel exchange the orthogonal unit vectors `u` and
`w/||w||`, with eigenvalues `+-||w||`.  Compression of `A` to `u^perp` is
`B`, while `Au=w`, proving both lower bounds in (2.5).  The upper bound is
the triangle inequality applied to (2.2).  `square`

The empirical mean `dbar` is absent from (2.5).  Its magnitude is not an
operator obstruction once it is subtracted exactly.

If the analytic centering uses a prescribed `kappa` rather than the
empirical `mu`, there is one additional scalar requirement:

```text
T-kappa J=A+(mu-kappa)J,
||(mu-kappa)J||=|dbar-kappa n|.                          (2.7)
```

Controlling (2.7) is itself a balanced three-prime short-interval main-term
problem.  A data-dependent regularization may instead remove `mu J`
exactly.

## 3. The degree channel is precisely selected-modulus BDH

The first necessary and sufficient input from (2.5) is

```text
(1/n)sum_b(d_b-dbar)^2 << D q^o(1).                      (3.1)
```

This is the selected-modulus BDH estimate from the two-star formulation,
with the full shell as coefficient support.  It says exactly

```text
sigma_d<<sqrt(D)q^o(1).                                 (3.2)
```

The elementary degree cap does not prove it.  It gives only

```text
sigma_d^2<=Delta*dbar<<D*dbar.                           (3.3)
```

The finite matrices have `dbar<1`, so (3.3) already makes the degree
channel tiny there.  That mechanism disappears once the expected degree
grows.

Coherent tangent packets can contribute at the diagonal-strength scale
`sum(d_b-dbar)^2~nD`, which is permitted by (3.1).  Peeling them is useful
for classifying equality but does not improve the required exponent.
After any literal edge deletion, Theorem 1 applies again to the residual
matrix with its new degree vector.

The proved local tangent classification also does not imply (3.1) for the
scattered residual.  It controls cells of carrier length `sqrt(D)`, while
there are `q/sqrt(D)>>D` such cells; the remaining `D` incidences can occupy
distinct cells.  This is the cross-interval barrier already identified in
the two-star audit.

## 4. The broad block is a centered common-neighbor covariance

Let

```text
C=T^2,
C_(b,b')=#{c:T_(b,c)=T_(b',c)=1}.                        (4.1)
```

Thus `C` is the exact common-neighbor matrix.  Squaring the broad block in
(2.1) gives another exact identity.

### Theorem 2 (centered covariance identity)

```text
B^2=P C P-delta delta^T/n.                               (4.2)
```

**Proof.**  Since `B=PTP`,

```text
B^2=PT(I-u u^T)TP=PT^2P-(PTu)(PTu)^T.                   (4.3)
```

But `PTu=delta/sqrt(n)`, which proves (4.2).  `square`

Consequently the remaining sharp theorem is exactly

```text
||P C P-delta delta^T/n||_(2->2)<<D q^o(1).              (4.4)
```

The left side is positive semidefinite; it equals `||B||^2`.  Formula
(4.4) is a carrier-preserving, mask-sensitive centered common-neighbor
large sieve.  In the reciprocal formulation it is the two-inverse theorem,
and in the automorphic formulation it is the regular two-index spectral
remainder.

The diagonal scale of (4.4) is already correct.  Directly,

```text
B_(b,c)=T_(b,c)-(d_b+d_c-dbar)/n.                        (4.5)
```

Using `Delta<<D` and `n=q^(1+o(1))>>D`, every row of (4.5) has squared norm

```text
sum_c |B_(b,c)|^2 << d_b+D^2/n <<D q^o(1).               (4.6)
```

What is missing is off-diagonal aggregation in (4.4), not another degree
or tangent estimate.

## 5. Why the original Schur certificate cannot be generalized directly

For the actual prime-power data through `q=1,000,003`, both `Delta` and
`dbar` happen to be tiny.  For example:

| `q` | `D` | `Delta` | `dbar` | `sigma_d` | `||PTP||` | `||T-mu J||` |
|---:|---:|---:|---:|---:|---:|---:|
| 1,013 | 28 | 4 | 0.343 | 0.893 | 2.209 | 2.519 |
| 25,013 | 135 | 4 | 0.146 | 0.534 | 2.543 | 2.560 |
| 200,003 | 371 | 6 | 0.433 | 0.943 | 3.352 | 3.352 |
| 1,000,003 | 811 | 8 | 0.706 | 1.185 | 3.638 | 3.641 |

This explains the exact finite Schur successes.  They do not yet sample
the anticipated positive-degree asymptotic regime.

The same cubic window with the full integer shell is a clean negative
control.  At `q=100003`, `D=265`, it has

```text
Delta=110,          dbar=39.670,          sqrt(D)=16.279,
(Delta+dbar)/sqrt(D)=9.19.                             (5.1)
```

Thus the cubic geometry, interval uniqueness, and narrow shell alone do
not imply (0.1).  Prime-power sparsity is essential.  This is not a
faithful actual-prime counterexample, and none is claimed.

## 6. The nonvacuous breakthrough statement

For empirical centering, the proposed sharp carrier theorem is equivalent,
within a factor two, to the conjunction

```text
selected-degree BDH:
  (1/n)sum_b(d_b-dbar)^2 <<D q^o(1),                    (6.1)

balanced common-neighbor covariance:
  ||P T^2 P-delta delta^T/n|| <<D q^o(1).               (6.2)
```

If a tangent/polar matrix is removed first, the identical two statements
must hold for the residual.  A successful regularized trace formula must
therefore do two concrete things:

1. synthesize and control the degree vector in (6.1);
2. prove (6.2) for the genuinely broad spectrum while charging any
   extracted polar pullback to the known tangent/chart sectors.

The mean density is not the missing gain, and a uniform maximum-degree
`sqrt(D)` theorem is neither necessary nor heuristically correct.  The
breakthrough is cancellation of centered common-neighbor correlations.

## 7. Status

```text
exact formulas for Delta and dbar:                    PROVED;
uniform product-window degree cap Delta<<D:           PROVED;
uniform Delta+dbar<=sqrt(D):                          NOT PROVED / IMPLAUSIBLE;
geometry-only version of that inequality:             FALSE;
faithful actual-prime counterexample:                  NOT FOUND;
exact constant/degree/broad ANOVA:                    PROVED;
degree-channel norm equals RMS degree fluctuation:     PROVED;
broad-square centered covariance identity:            PROVED;
selected-degree BDH (6.1):                            OPEN;
balanced covariance theorem (6.2):                   OPEN;
sharp four-cycle theorem:                             NOT PROVED.
```

The exact finite identities and regressions are in
`src/qp_finite_carrier_relative_trace.py` and
`src/test_qp_finite_carrier_relative_trace.py`.
