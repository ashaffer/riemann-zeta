# R114 numerator-completion and transition gate

Status: two coefficient-uniform numerator-completion theorems are proved
for the exact R81/R105 reciprocal phases.  They improve the previously
recorded high-mode ledger without requiring short additive supports.  On the
recombined R105 top box the gain stops exactly at shift-product length
`K=X^(3/2)`; the remaining range up to `X^2` is not power-saved against the
physical direct bound.  No fixed zero-free strip, and no theorem excluding
one, is proved.

Date: 2026-08-07.

Companion fixed-product audit:
[`R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md`](R113-R105-MULTIPLIER-AVERAGE-FAIL-FAST-AUDIT.md).
R113 sharpens Section 4 below on the actual square-root Vaughan boxes by
using divisor-fiber multiplicity; R114 records the distinct
varying-denominator completion (2.3) and its transition exponent.

## 1. Why complete the numerator

The mask-free R81 form in R84 Proposition 4.1 is

```text
B=sum_(m,n,k) alpha_m beta_n nu_k e_m(k inverse(n)),  (1.1)
```

with `(m,n)=1`.  Earlier ledgers sent (1.1) directly to a trilinear
Kloosterman-fraction theorem.  When the integer numerator range is at least
as long as the modulus, there is a more elementary operation: fold `k`
modulo `m`, use additive Parseval, and only then sum the varying moduli.

This operation is exact.  It retains arbitrary complex coefficients and is
therefore available before using any Mobius- or von-Mangoldt-specific input.

## 2. A varying-denominator numerator-completion theorem

Let `mathcal M` be any set of positive integers in `[M,2M]`.  Let `beta`
and `nu` be supported on integer intervals containing respectively at most
`N` and `K` integers.  Put

```text
B(alpha,beta,nu)
 =sum_(m in mathcal M) alpha_m
   sum_(n:(n,m)=1) beta_n
   sum_k nu_k e_m(k inverse(n)).                     (2.1)
```

For a residue `a modulo m`, define the exact folds

```text
beta_(m,a)=sum_(n congruent a mod m) beta_n,
nu_(m,a)=sum_(k congruent a mod m) nu_k.              (2.2)
```

**Theorem 2.1 (numerator completion).**  One has

```text
abs(B)
 <=[sum_(m in mathcal M) m L_N(m)L_K(m)]^(1/2)
      norm(alpha)_2 norm(beta)_2 norm(nu)_2,          (2.3)

L_N(m)=ceil(N/m)+1,
L_K(m)=ceil(K/m)+1.                                  (2.4)
```

In particular,

```text
abs(B)
 <<M sqrt[(1+N/M)(1+K/M)]
      norm(alpha)_2 norm(beta)_2 norm(nu)_2.          (2.5)
```

### Proof

For fixed `m`, inversion permutes the unit residues.  Cauchy and additive
Parseval give

```text
abs[sum_(a in (Z/mZ)^*) beta_(m,a)
       sum_(b mod m)nu_(m,b)e_m(b inverse(a))]^2

 <=norm(beta_m)_2^2
    sum_(x mod m)abs(sum_b nu_(m,b)e_m(bx))^2

 =m norm(beta_m)_2^2 norm(nu_m)_2^2.                 (2.6)
```

Every residue class meets an interval of length `N` at most `L_N(m)`
times.  Cauchy within the residue classes therefore gives

```text
norm(beta_m)_2^2<=L_N(m)norm(beta)_2^2,
norm(nu_m)_2^2<=L_K(m)norm(nu)_2^2.                  (2.7)
```

Multiply (2.6) by `abs(alpha_m)`, sum `m`, and use Cauchy once more.  This
proves (2.3).  Since `#mathcal M<=M` and `m asymp M`, (2.5) follows.  QED.

No primality, squarefreeness, interval location, or boundedness assumption
on the coefficients occurs in the proof.

## 3. The R105 top-box ledger

Use the notation of R105 Section 4.  On its forced top box,

```text
M=N=X,
norm(alpha)_2 norm(beta)_2=X^(-1+o(1)),              (3.1)

integral norm(nu_t)_2 dt
 <<X^o K^(1/2),                                      (3.2)
```

where `K` is the dyadic size of the grouped product `k=j theta`.
Theorem 2.1 gives

```text
B_K
 <<X^o K^(1/2)(1+K/X)^(1/2).                        (3.3)
```

If `K=X^kappa`, this has exponent

```text
kappa/2,          0<=kappa<=1,
kappa-1/2,        1<=kappa<=2.                       (3.4)
```

This strictly improves R105 (4.5) on much of the large-`K` range.  The
physical estimate R105 (4.7), however, is

```text
E_T<<X^(1+o(1)).                                     (3.5)
```

Consequently (3.3) is power-better than (3.5) only for

```text
K<X^(3/2-o(1)).                                      (3.6)
```

At `K=X^(3/2)` it merely recovers the physical scale, and at the genuine
endpoint `K=X^2` it gives `X^(3/2+o(1))`.  Thus numerator completion lowers
the former `X^(15/8)` Wright ledger at the endpoint to `X^(3/2)`, but it
does not close the top box.

This comparison is important.  The natural benchmark is the exact physical
bound (3.5), not the much larger coefficient-blind absolute scale of the
completed reciprocal coordinates.  A saving relative to the latter can
still be a loss relative to (3.5).

## 4. Exact completion after unfolding the Vaughan product

R105 (5.1) has the more special fixed-modulus slice

```text
F_c(k)
 =sum_(d in D,b in E) alpha_d beta_b
    e_c(k inverse(db)),                              (4.1)
```

where `D,E` contain units modulo `c`.  This admits a second exact theorem
which does not pass through the full-Fourier/inverse-image Kloosterman
formula.

**Theorem 4.1 (inverse-product multiplier mean square).**  For an arbitrary
coefficient `nu` on `Z/cZ`,

```text
abs[sum_(k mod c)nu_k F_c(k)]
 <=sqrt[c min(#D,#E)]
    norm(nu)_2 norm(alpha)_2 norm(beta)_2.            (4.2)
```

### Proof

On the unit group put

```text
gamma(x)=sum_(db=x mod c)alpha_d beta_b.              (4.3)
```

Multiplicative Young and Cauchy give

```text
norm(gamma)_2
 <=min{norm(alpha)_1 norm(beta)_2,
       norm(alpha)_2 norm(beta)_1}
 <=sqrt[min(#D,#E)]norm(alpha)_2norm(beta)_2.         (4.4)
```

Inversion is a permutation of the unit group.  Cauchy followed by additive
Parseval therefore yields

```text
abs[sum_x gamma(x)sum_k nu_k e_c(k inverse(x))]
 <=norm(gamma)_2
    [sum_(y mod c)abs(sum_k nu_k e_c(ky))^2]^(1/2)
 =sqrt(c)norm(gamma)_2norm(nu)_2.                    (4.5)
```

Equations (4.4)--(4.5) prove (4.2).  QED.

At the Vaughan scale `#D,#E asymp sqrt(c)`, (4.2) has coefficient factor

```text
c^(3/4).                                             (4.6)
```

For the actual fixed-ratio product intervals, R113 Lemma 3.1 improves
(4.6) to `c^(1/2+epsilon)` by observing that each residue product has only
divisor-many bounded integer lifts.  The generic theorem here is retained
because it needs no interval geometry.

This remains valid although the Fourier transform of `alpha` has full
support and the inverse image of `E` is not an additive interval.  It is
therefore a genuine bypass of the R105 short-support mismatch for a
multiplier average.

If an integer `k`-interval of length `K` is folded modulo `c`, residue-class
Cauchy gives

```text
norm(nu_fold)_2
 <=(1+K/c)^(1/2)norm(nu)_2.                          (4.7)
```

This factor is sharp for arbitrary coherent aliases.  The transformed
R71 amplitude is not an arbitrary `nu`, but no theorem presently proves a
fixed-power improvement over (4.7) uniformly through all its high
shift-product boxes.

## 5. Why undoing the solution-line Poisson step does not add a saving

For reference, the exact R81 amplitude is

```text
A_(g,m,n,theta)(j)
 =g integral L_Q(u+gj,u)e(theta u/(gmn))du.           (5.1)
```

At `g=1`, `m,n,j,theta asymp X`, summing `j` first forces the residue
`theta inverse(n) mod m` into a bounded neighborhood of zero.  This looks
like an `X`-fold cancellation.  Poisson inversion shows exactly what it
does: the surviving congruences are

```text
theta=a n-b m                                        (5.2)
```

with the original bounded Fourier aliases `a,b`.  The resulting sum is the
finite cofactor expression from which (5.1) was derived.  Its scale is
precisely (3.5).  Thus completing `j` recovers the physical normalization;
it does not by itself save a power beyond it.

The two zero marginals of `L_Q` remove `a=0` and `b=0`, but the first
nonzero aliases have scaled frequency of order one.  They are not small by
smoothness or by the moment conditions.

## 6. Transition verdict

The exact information now fits into three ranges on the R105 top box:

```text
small and medium K:  Wright/R84 or Theorem 2.1 can be nontrivial;
K<X^(3/2):           numerator completion beats the physical scale;
K>=X^(3/2):          coefficient-uniform completion does not;
K=X^2:               new bound X^(3/2), physical bound X.          (6.1)
```

The factor-unfolded mean square (4.2) is a real structural improvement, but
after residue folding and restoration of the full R71 normalization it has
not yet produced `X^(1-delta)`.  Closing the range in (6.1) requires one of:

1. a power improvement in the actual alias-folding norm in (4.7);
2. Mobius--von-Mangoldt cancellation in the multiplicative convolution
   (4.3), beyond coefficient-uniform Young;
3. a signed estimate that combines different numerator blocks before their
   physical Poisson recombination; or
4. a direct full-support trace theorem which is measured against (3.5), not
   against the larger completed-coordinate baseline.

Failure of the coefficient-uniform theorems at `K>=X^(3/2)` is a method
boundary, not evidence that a fixed zero-free strip is false.
