# Full-field and frozen-center Vinogradov--Korobov subpower bound

Status: analytic/literature-conditional theorem for the cutoff-independent
full von Mangoldt coboundary and analytic classical-synthesis transfer to the
frozen-cutoff rank-two center, internally audited; 2026-08-07.  The
varying-test converse remains open.  This note does **not** prove a fixed
zero-free strip or the Riemann Hypothesis.

## 1. Verdict

The formal R74 calibration

```text
E_I^full <=exp(R-R^(4/5-o(1)))                           (1.1)
```

can be made rigorous for the **full/exact-head** field.  A direct
distributional explicit formula avoids the unfinished growing-order
Guinand--Weil and Euler-transfer route.  On the regular schedule

```text
k=floor(sqrt(R)/log R),
H=R/k,
L=hk,                                                    (1.2)
```

one obtains the concrete estimate

```text
E_I^full
 <=exp[R-c_h R^(4/5)(log R)^(-3/5)].                    (1.3)
```

This closes the subpower **full-field** calculation.  Arbitrary-order
periodic Euler summation, with its constants tracked for fixed `h`, also
transfers (1.3) to the frozen-cutoff field with the evaluated rank-two center;
see Section 9.  That transfer is classical bookkeeping, not a new
cancellation theorem.

Neither result proves a fixed saving `exp((1-2eta)R)`: the effective
`eta(R)` still tends to zero.  The report also does not prove that the moving
detector retains the exact width exponent `Delta`; that is the separate
varying-test converse.

## 2. The normalized fixed-step window

Fix `h>0` and an integer `k>=1`, and put `L=hk`.  Define

```text
Phi_(h,k)(t)
 =(1/h^k)vol{u in [0,h]^k:u_1+...+u_k<t},               (2.1)

W_(h,k)(t)=Phi_(h,k)(t+L)-Phi_(h,k)(t),                 (2.2)
N_(h,k)=norm(W_(h,k))_2,
V_(h,k)=W_(h,k)/N_(h,k).                                (2.3)
```

The window is continuous, even, nonnegative, supported on `[-L,L]`, and
bounded above by one.  Symmetry of the sum of the uniform variables gives

```text
integral W_(h,k)=L,
W_(h,k)(t)>=1/2 for abs(t)<=L/2,
TV(W_(h,k))=2.                                          (2.4)
```

Consequently,

```text
sqrt(L)/2<=N_(h,k)<=sqrt(L),
norm(V_(h,k))_1<=2sqrt(L),
TV(V_(h,k))<=4/sqrt(L).                                 (2.5)
```

Use the bilateral Laplace convention

```text
Vhat(s)=integral_R V(t)exp(-st)dt.                       (2.6)
```

The exact compact-coboundary multiplier is

```text
Vhat_(h,k)(s)
 =1/N_(h,k) * [2sinh(Ls/2)/s]
   *[sinh(hs/2)/(hs/2)]^k.                              (2.7)
```

At `s=0` the right side is interpreted by continuity and equals
`L/N_(h,k)`.

## 3. Canonical theorem card

### Theorem 3.1 (full-field VK energy bound)

Define the cutoff-independent completed field

```text
D_(h,k)^full(r)
 =sum_(n>=1) Lambda(n)n^(-1/2)V_(h,k)(r-log n)
  -exp(r/2)Vhat_(h,k)(1/2).                             (3.1)
```

Equivalently, in the notation of the fixed-step primitive,

```text
D_(h,k)^full(r)
 =N_(h,k)^(-1)[C_(h,k)(r+L)-C_(h,k)(r)].                (3.2)
```

Let

```text
k_R=floor(sqrt(R)/log R),
L_R=h k_R,
H_R=R/k_R.                                               (3.3)
```

There are constants `c_h>0` and `R_h` such that, for every `R>=R_h` and
every measurable weight `0<=psi<=1` supported in `[R-H_R,R]`,

```text
E_(I,psi)^full
 :=integral psi(r)abs(D_(h,k_R)^full(r))^2dr
 <=exp[R-c_h R^(4/5)(log R)^(-3/5)].                    (3.4)
```

#### Evidence class and trust base

This is an analytic theorem conditional on the classical
Vinogradov--Korobov zero-free region and Riemann--von Mangoldt counting.  The
window algebra, contour shift, residue inventory, shell optimization, and
block bookkeeping are proved below.  The result has received one independent
internal analytic audit; it is not formalized in Lean and no novelty claim is
made.

The closest literature input is the standard zero-free boundary

```text
1-beta >=a (log abs(gamma))^(-2/3)
             (log log abs(gamma))^(-1/3)                (3.5)
```

at large height.  A current published explicit source is
[Bellotti, *Explicit bounds for the Riemann zeta function and a new
zero-free region*](https://doi.org/10.1016/j.jmaa.2024.128249); the complete
version ledger is in the imported analytic baseline.

#### Exact scope

The field in (3.1) retains the exact Type-I head, or equivalently works
directly with the full von Mangoldt sum.  Corollary 3.2 below compares it with
the frozen-cutoff balanced tail and its evaluated rank-two center.  The upper
bounds are unconditional, but their use as a converse detector for a growing
`k` is not established.

### Corollary 3.2 (frozen-center VK energy bound)

Let `R_0=R-H_R`, fix `c>1/4`, and freeze

```text
U_R=V_R=floor(exp[(1/2-c/k_R)R_0]).                     (3.6)
```

Let `D_(h,k_R)^(U_R,V_R)` be the normalized balanced Vaughan tail with the
complete evaluated rank-two Type-I center.  After possibly reducing `c_h`,
for all sufficiently large `R`,

```text
integral psi(r)abs(D_(h,k_R)^(U_R,V_R)(r))^2dr
 <=exp[R-c_h R^(4/5)(log R)^(-3/5)].                    (3.7)
```

The proof and the exact support/error ledger are in Section 9.  Its analytic
ingredients are also catalogued as `PROJ-EUL1` and `PROJ-EUL2` in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).

## 4. Uniform multiplier bound

For `s=delta+i gamma`, `abs(delta)<=1/2`, and `abs(gamma)>=1`, (2.5)--(2.7)
give

```text
abs(Vhat_(h,k)(s))
 <=4/sqrt(L) * exp(B_h k) * abs(gamma)^(-(k+1)),         (4.1)
```

where one may take

```text
B_h=h/4+max(0,log[2cosh(h/4)/h]).                        (4.2)
```

Indeed,

```text
abs(sinh(Ls/2))<=exp(L/4),
abs(sinh(hs/2)/(hs/2))
 <=2cosh(h/4)/(h abs(gamma)).                            (4.3)
```

The `sqrt(L)` normalization in (4.1) is the only polynomial window loss.
The growing order costs `exp(O_h(k))`, not `exp(O_h(k^2))`, on the exact
zero side.

## 5. Exact explicit formula and residue ledger

For `r>L`, Mellin inversion starts on `Re(s)>1/2` with

```text
D_(h,k)^full(r)
 =1/(2pi i) integral
  [-zeta'(s+1/2)/zeta(s+1/2)-1/(s-1/2)]
  Vhat_(h,k)(s)exp(sr)ds.                               (5.1)
```

The residue inventory is as follows.

1. The pole of zeta at `s+1/2=1` has residue `+1` in
   `-zeta'/zeta` and is cancelled exactly by `-1/(s-1/2)`.
2. The apparent primitive singularity at `s=0` is removed by the
   coboundary factor in (2.7).  The bracket in (5.1) is regular there, so no
   constant residue remains.
3. A nontrivial zero `rho`, counted with multiplicity `m_rho`, contributes

```text
-m_rho exp((rho-1/2)r)Vhat_(h,k)(rho-1/2).              (5.2)
```

4. The trivial zero at `-2m`, `m>=1`, contributes

```text
-exp((-2m-1/2)r)Vhat_(h,k)(-2m-1/2).                   (5.3)
```

These trivial-zero residues are the entire remaining archimedean
contribution in this direct `-zeta'/zeta` formulation.  There is no separate
gamma integral.

To justify the shift, choose horizontal heights away from zero ordinates and
move the left boundary through lines on which `Re(s+1/2)` is a negative odd
integer.  From compact support and (2.7),

```text
Vhat_(h,k)(s)exp(sr)
 =O_h(exp[-(r-L)abs(Re(s))+O_h(k)]abs(s)^(-(k+1)))       (5.4)
```

on the far left.  Standard logarithmic-derivative bounds away from zeros
then make the left and horizontal integrals vanish.  The window is
continuous, so no endpoint half-weight is introduced.  Thus

```text
D_(h,k)^full(r)
 =-sum_rho m_rho exp((rho-1/2)r)Vhat_(h,k)(rho-1/2)
  -sum_(m>=1)exp((-2m-1/2)r)Vhat_(h,k)(-2m-1/2).        (5.5)
```

Both sums are absolutely convergent for every `k>=1`.  For the nontrivial
zeros this follows from (4.1) and `N(T+1)-N(T)=O(log(T+2))`; for the trivial
zeros it follows from `r>L`.

## 6. The zero-shell estimate

Choose `j_0`, `a>0`, and `A>0` so that every nontrivial zero with

```text
exp(j)<=abs(gamma)<exp(j+1),       j>=j_0,               (6.1)
```

satisfies (3.5) in the form

```text
1-beta>=a(j+1)^(-2/3)[log(j+1)]^(-1/3),                 (6.2)
```

and the shell contains at most `A exp(j)(j+1)` zeros, counted with
multiplicity.  Combining (4.1), (5.2), and (6.2), the shell contribution is
at most

```text
C_h/sqrt(L) * exp(r/2+B_h k)
 *(j+1)exp{
   -k j-a r(j+1)^(-2/3)[log(j+1)]^(-1/3)
 }.                                                      (6.3)
```

Put

```text
Y=(r/k)^(3/5)[log(e+r/k)]^(-1/5),
S(r,k)=kY
      =r^(3/5)k^(2/5)[log(e+r/k)]^(-1/5).                (6.4)
```

For `j<Y`, the second term in the exponent of (6.3) is at least a fixed
positive multiple of `S(r,k)`.  For `j>=Y`, the term `k j` is at least
`S(r,k)`, and the remaining tail is geometrically summable.  Polynomial
factors in `j` are absorbed after reducing the constant.  Hence there are
`c_0,C_0>0` such that

```text
sum_(abs(gamma)>=exp(j_0)) abs(zero contribution)
 <=C_0/sqrt(L)
   exp[r/2+B_h k-c_0 S(r,k)].                            (6.5)
```

There are only finitely many lower zeros.  Since none lies on `Re(s)=1`,
there are fixed `M_0,d_0>0` such that their contribution is at most

```text
2M_0 sqrt(L)exp[r/2-d_0 r+L/2].                          (6.6)
```

Finally, (2.5) bounds the trivial-zero sum by

```text
2sqrt(L) exp[-(5/2)(r-L)]/[1-exp(-2(r-L))].              (6.7)
```

Equations (6.5)--(6.7) give a complete pointwise bound; no zero or
archimedean term is omitted.

## 7. The regular-block calculation

On the schedule (3.3),

```text
L_R/H_R=h k_R^2/R<=h/(log R)^2,                          (7.1)
```

so `R-H_R-L_R` tends to infinity and the full window stays inside a large
safe core.  Uniformly for `r in [R-H_R,R]`,

```text
S(r,k_R)
 >=c R^(4/5)(log R)^(-3/5).                             (7.2)
```

Moreover,

```text
B_h k_R=o(S),
log H_R=o(S),
log L_R=o(S).                                            (7.3)
```

The low-zero term (6.6) has a fixed linear saving and the trivial-zero term
is negligible.  Squaring (6.5), integrating over a set of length at most
`H_R`, and absorbing (7.3) proves (3.4).

This realizes the formal optimization

```text
S(R,k)
 asymp R^(3/5)k^(2/5)[log(R/k)]^(-1/5)                  (7.4)
```

at the largest regular fixed-step order allowed up to logarithms by
`hk^2=o(R)`.

## 8. Independent PNT fallback

There is a simpler proof of a weaker bound.  Suppose the classical
Vinogradov--Korobov prime-number-theorem remainder is written

```text
abs(Psi(x)-x)
 <=A x exp[-a P(log x)],
P(u)=u^(3/5)(log u)^(-1/5).                              (8.1)
```

Stieltjes integration by parts, (2.5), and support in `[-L,L]` give, for
`R-H-L` beyond the starting point of (8.1),

```text
integral_(R-H)^R abs(D_(h,k)^full(r))^2dr
 <=A^2 H(sqrt(L)+4/sqrt(L))^2
   *exp[R+L-2a P(R-H-L)].                               (8.2)
```

On (3.3), all terms other than `R-2aP(R)` are lower order, so for large `R`

```text
E_I^full
 <=exp[R-(a/2)R^(3/5)(log R)^(-1/5)].                   (8.3)
```

This safety-net theorem does not use the zero-shell optimization.  A recent
primary source for the sharp VK-shaped PNT error is
[Bellotti, *A new zero-density estimate for zeta and the error term in the
Prime Number Theorem*](https://arxiv.org/abs/2508.02041).

## 9. Uniform Euler transfer to the explicit center

Let `D_I^app` denote the frozen-cutoff balanced tail plus the evaluated
rank-two center, and let `epsilon_I` be its Euler-evaluation defect relative
to (3.1).  The exact Hilbert-space comparison is only

```text
abs(sqrt(E_I^app)-sqrt(E_I^full))
 <=norm(sqrt(psi)epsilon_I)_2.                           (9.1)
```

The required uniform Euler trace is

```text
norm(sqrt(psi)epsilon_I)_2
 <=exp(O_h(k^2+k log(k+2))-cR)                           (9.2)
```

(with a positive `c` after the cutoffs are chosen).  It follows from the
order-`k` periodic Euler formula rather than from a new arithmetic estimate.

For fixed `h>0` and `a` in a compact subset of `0<Re(a)<1`, averaging the
periodic Euler formula against the order-`k` cardinal B-spline gives

```text
sum_n n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)H_(h,k)(1-a)+zeta(a)
  +O(exp[C_h(k^2+klog(k+2))]X^(-Re(a)-k)).              (9.3)
```

The `a` derivative has the same bound with an extra `1+log X`.  To track the
constant, use

```text
norm(Bbar_m)_infinity<=4m!/(2pi)^m,
norm(D^q kappa_(h,k))_TV<=(2/h)^q.                      (9.4)
```

After `t=exp(-u)`, `0<=u<=hk`, the identity

```text
D_t^k=(-1)^k exp(ku)D_u(D_u+1)...(D_u+k-1)             (9.5)
```

costs `exp(O_h(k^2+klog k))`.  Integrating a periodic Bernoulli term by
parts `k` times introduces the bounded primitive
`[m!/(m+k)!]Bbar_(m+k)`, which cancels the factorial in (9.4).  The sharp
Euler remainder obeys the same bound.  This proves (9.3), including the
fixed-`h`, growing-support constant.

Exact Vaughan now yields, for `x=exp(r)`,

```text
abs(E_(U,V)(x))
 <<_h exp[C_h(k^2+klog(k+2))]
 [U^(k+1)log(2x)+(UV)^(k+1)]x^(-k-1/2).                (9.6)
```

Freeze `U,V` as in (3.6).  At the left endpoint, the dominant `UV` term has
logarithm at most

```text
-(2c-1/2+O(1/k))R_0+C_hk^2+O(klog k).                  (9.7)
```

It only decreases further through the block; the one-`U` term is much
smaller.  The support condition `UV<=x exp(-hk)` is implied by

```text
hk^2<=(2c-o(1))R_0.                                    (9.8)
```

On (3.3), `k^2=R/log^2 R=o(R)` and (9.8) holds.  Endpoint differencing,
division by `N_(h,k)>=sqrt(hk)/2`, and integration over a block of length
`H_R` consume only `exp(o(R))`.  Thus for some `kappa>0`,

```text
norm(sqrt(psi)epsilon_I)_2<=exp(-kappa R).              (9.9)
```

Combining (9.1), (9.9), and Theorem 3.1 proves Corollary 3.2.

This is a classical-synthesis analytic proof, not a verbatim theorem located
in the literature.  It should receive independent specialist review before
publication, but it is no longer a red mathematical cancellation obligation.

There is a second independent gap.  A fixed off-line carrier survives the
multiplier when `k=o(R)`, but the repository has not proved the complete
blockwise oscillation converse uniformly for the varying test.  Therefore
(3.4) and (3.7) are unconditional upper calibrations, not new zero-exclusion
theorems.

## 10. Reproduction and nonclaims

The exact multiplier factorization and a finite direct von Mangoldt
coboundary identity are exercised by
[`src/fixed_step_spectral_cooling_probe.py`](../src/fixed_step_spectral_cooling_probe.py)
and its focused tests:

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_fixed_step_spectral_cooling_probe.py
```

Those tests are diagnostics for the finite algebra.  They do not certify
the infinite contour shift or VK shell sum.  The theorem is the conventional
argument in Sections 4--7, with the literature inputs stated in Section 3.

This report proves (9.2) in the exact frozen-cutoff normalization through
(9.3)--(9.9).  It does not prove the varying-test converse, a fixed
exponential saving, a fixed zero-free strip, RH, or mathematical novelty.
