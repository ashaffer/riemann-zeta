# Independent audit of the fixed-window reduction

Status: hostile proof and quantifier audit, 2026-08-30. This report verifies a
conditional reduction to a uniform zero-free strip. It proves no new strip and
does not prove RH.

## 1. Binary verdict

The fixed-parameter, pointwise reduction survives the audit. After importing
the standard normalization-matched Guinand--Weil formula for the triangular
test, the following implication is sound and noncircular:

```text
for some fixed ell,k,eta>0, with
0<theta<=theta_k=1/2-1/[4(k+1)], and every sufficiently large real x,

  |B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)| << x^(1/2-eta),
  U=V=floor(x^theta)

                         implies

  zeta(s) has no zero with Re(s)>1-eta.
```

The audit did **not** establish the premise. In fact, at any one admissible
choice of fixed parameters, existence of an all-sufficiently-large-real-`x`
fixed power saving for the complete centered aggregate is equivalent, up to
an arbitrarily small loss in the exponent, to existence of a uniform
zero-free strip. The reduction is therefore an exact arithmetic coordinate
system for the goal, not evidence that the goal has become easier.

The component verdicts are:

| Item | Verdict after audit | Qualification |
|---|---|---|
| fixed-window width | passes relative to a standard imported theorem | the low-regularity triangular Guinand--Weil formula is still an axiom in the local Lean trust boundary |
| prime-power deletion | passes | its quantitative PNT asymptotic is not needed for the strip implication |
| ramp coboundary exponent | passes by an elementary telescoping lemma | no second transform-pole uniqueness argument is needed |
| fixed-order Euler/B-spline lemma | passes | one intermediate joint `h,j` bound needs the correction in Section 4 below |
| growing-order constant at `h=ell/k` | passes the corrected trace | this gives localization only, not a moving-test converse |
| Vaughan reduction | passes coefficientwise and in the exponent ledger | it contains no Type-II saving |
| fixed-exponent implication | passes for fixed parameters and all large real `x` | dyadic-only, averaged, or subsequential estimates do not suffice without a new interpolation theorem |
| fixed-power estimate | open | it is already strip-strength |

## 2. Exact theorem that survives

Fix, before taking any limit,

```text
ell>0,
k an integer with k>=1,
h=ell/k,
0<theta<=theta_k=1/2-1/[4(k+1)].
```

For every sufficiently large real `x`, put

```text
U(x)=V(x)=floor(x^theta).
```

Then `UV<=x exp(-ell)` eventually. With the definitions in Section 5 of
[`FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md`](../publication/FIXED-WINDOW-WIDTH-AND-TYPE-II-REDUCTION.md),
the exact finite Vaughan calculation gives

```text
C_(h,k)(log x)
 =B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
  +O_(h,k)([U^(k+1)log(2x)+(UV)^(k+1)]/x^(k+1/2)).       (2.1)
```

At `theta=theta_k`, the second error is `O_(ell,k)(1)` because

```text
2 theta_k(k+1)-k-1/2=0,
```

and the first error power-decays because

```text
theta_k(k+1)-k-1/2=-k/2-1/4<0.                            (2.2)
```

Below the endpoint both errors decay. For these fixed parameters,

```text
limsup_(x->infinity)
 log(1+|B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)|)/log x
 =Delta,                                                   (2.3)

Delta=sup_rho |Re(rho)-1/2|.
```

Consequently, an all-large-`x` bound

```text
|B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)|<=C x^(1/2-eta)            (2.4)
```

implies `Delta<=1/2-eta`, and zeta symmetry gives

```text
eta<=Re(rho)<=1-eta
```

for every nontrivial zero. Conversely, if `Delta<=1/2-delta`, (2.3) gives,
for every `epsilon>0`,

```text
|B-Z|<=x^(1/2-delta+epsilon)
```

eventually. Taking `epsilon<delta` produces some fixed saving. The converse
does not assert the endpoint big-O bound with `epsilon=0` merely from a
limsup identity.

## 3. Fixed-window pole audit

For fixed `ell>0`, set

```text
H_ell(z)=4 sin^2(ell z/2)/(ell z^2),
z_rho=(rho-1/2)/i.
```

The triangular Guinand--Weil identity is

```text
B_ell(R)=sum_rho m_rho H_ell(z_rho)exp(-i z_rho R).        (3.1)
```

The audit checks every point needed by the lower-exponent argument.

1. Uniformly for `|Im z|<=1/2`,
   `H_ell(z)=O_ell((1+|Re z|^2)^(-1))`. Riemann--von Mangoldt counting
   therefore makes (3.1) absolutely convergent.
2. For `Im z>1/2`, termwise integration gives

   ```text
   integral_0^infinity B_ell(R)exp(i zR)dR
    =i sum_rho m_rho H_ell(z_rho)/(z-z_rho).               (3.2)
   ```

   On every compact set avoiding the nodes, the tail is normally convergent:
   the extra denominator improves the already summable coefficient by one
   power of the ordinate.
3. Every zero of `H_ell` is real. Thus an off-critical node has a nonzero
   residue in (3.2). Repeated zeros add through `m_rho`; distinct symmetric
   zeros occur at distinct nodes and cannot cancel the pole.
4. If the growth exponent were below the positive imaginary part of one
   node, an intermediate exponential majorant would make the left side of
   (3.2) holomorphic across that node. Meromorphic uniqueness contradicts its
   nonzero residue.
5. Taking the supremum over nodes proves the result even when `Delta` is not
   attained. No rightmost zero is assumed.

The prime-side discrepancy differs from `-B_ell` by pole and archimedean
terms of size `O_ell(exp(-R/2))`. Hence

```text
limsup_(R->infinity) log(1+|D_ell(R)|)/R=Delta.             (3.3)
```

This uses the explicit formula, functional-equation symmetry, the classical
critical strip, and zero counting. It does not use a fixed zero-free strip.

The local formalization still declares the smooth and logarithmic-domain
Guinand--Weil formulas as literature axioms in
[`GuinandWeilLiterature.lean`](../lean/rhbridge/RHBridge/GuinandWeilLiterature.lean).
The smallest trust-boundary repair is to derive the translated triangle from
the smooth compact-support formula by even mollification and dominated
convergence. Quadratic transform decay supplies the domination.

### 3.1 Prime powers are not a circular input

The sharper formula

```text
D_ell(R)=P_ell(R)+ell/2
 +O_ell(exp(-c sqrt(R))+(1+R)exp(-R/6))                    (3.4)
```

is consistent. The square-prime main term is `ell/2`; powers at least three
give the exponentially decreasing remainder. The PNT estimate used for the
displayed rate comes from a classical shrinking zero-free region, not from a
fixed strip.

More importantly, (3.4) is unnecessary in the shortest strip proof.
Chebyshev bounds already give `D_ell-P_ell=O_ell(1)`, enough to preserve the
growth exponent. The Vaughan reduction below works directly with the full
von Mangoldt field and does not use prime stripping at all.

## 4. Coboundary and Euler audit

### 4.1 Elementary coboundary-exponent lemma

Let `f` be locally bounded on a forward half-line, fix `ell>0`, and put

```text
d(R)=f(R+ell)-f(R),
lambda(g)=limsup_(R->infinity) log(1+|g(R)|)/R.
```

Then

```text
lambda(f)=lambda(d).                                       (4.1)
```

Indeed, `lambda(d)<=lambda(f)` follows from the triangle inequality and
invariance under a fixed translation. Conversely, write uniquely
`R=r+n ell` with `r` in a fixed compact base interval and telescope:

```text
f(r+n ell)=f(r)+sum_(j=0)^(n-1)d(r+j ell).                 (4.2)
```

For any `epsilon>0`, the definition of `lambda(d)` bounds the summands by
`exp((lambda(d)+epsilon)(r+j ell))` after a fixed initial segment. The
geometric sum, with local boundedness on the initial compact set, proves
`lambda(f)<=lambda(d)+epsilon`; let `epsilon` decrease to zero.

Applied to

```text
D_ell(R)=C_ell(R+ell)-C_ell(R),
```

this closes the exponent part of `FW-COBOUNDARY` directly from `FW-WIDTH`.
The additional Perron pole argument in the draft is valid but unnecessary.
Boundedness under RH still follows from the absolutely convergent fixed-test
zero series; bounded increments alone would only imply linear growth.

For the higher-order primitive used in (2.1), the fixed zero multiplier is

```text
H_(h,k)(s)=(1/s)[(1-exp(-hs))/(hs)]^k.                    (4.2a)
```

Its nonzero zeros lie on the imaginary axis and its zero coefficients decay
as `O_(h,k)(|gamma|^(-k-1))`. Thus the same normally convergent Laplace-pole
argument gives

```text
lambda(C_(h,k))=Delta                                     (4.2b)
```

for every fixed `h>0,k>=1`. Equivalently, each additional logarithmic
average multiplies the Laplace transform by
`(1-exp(-hs))/(hs)`, which is nonzero at every off-axis zero. This is the
missing explicit bridge from the triangular `k=1` detector to (2.3).

### 4.2 Euler/B-spline lemma

Let

```text
(A_h F)(X)=h^(-1) integral_0^h F(X exp(-u))du.
```

Finite sum/integral interchange gives exactly

```text
A_h^k[sum_(n<=X)n^(-a)]
 =sum_n n^(-a)Phi_(h,k)(log(X/n)).                         (4.3)
```

For the periodic Bernoulli expansion, use the right-continuous convention

```text
Bbar_1(n)=-1/2.
```

Then `D Bbar_1=1-sum_n delta_n` distributionally. Its jump contributes the
positive endpoint atom required by the `n<=X` convention. The signs and
factorials in formulas (6.17c) and (6.17c') of
[`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`](ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md)
are correct.

If `q` is periodic of mean zero and has a bounded periodic `j`-fold
primitive, changing variables `t=exp(-u)` gives

```text
A_h^j[X^(-b)q(X)]
 =X^(-b) integral_(exp(-jh))^1 W_(b,h,j)(t)q(Xt)dt.        (4.4)
```

Extend `W` by zero. Its `j`th distributional derivative is a finite measure,
including all endpoint atoms. For `q=Bbar_r`,

```text
Q_j=[r!/(r+j)!]Bbar_(r+j),   Q_j^(j)=Bbar_r.               (4.5)
```

Distributional integration by parts therefore gains exactly `X^(-j)` with
no omitted boundary term. Applying this with `j=k` to every periodic term,
and using the explicit sharp remainder, proves

```text
sum_n n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)H_(h,k)(1-a)+zeta(a)
  +O_(K,h,k)(X^(-Re(a)-k)).                                (4.6)
```

On nested compact subsets of `0<Re(a)<1`, a Cauchy circle of radius
comparable to `1/log X` gives the differentiated error with the single extra
factor `log X`.

### 4.3 The one correction

Formula (6.17e') in the detailed report understates the dependence when it is
read jointly in `h` and `j`. The conversion

```text
D_t^j=(-1)^j exp(ju)D_u(D_u+1)...(D_u+j-1),  t=exp(-u),
```

on `0<=u<=jh` costs `exp(O_B(j^2 h))`, not merely
`exp(C_B jh)` with a constant independent of `j`. A safe replacement is

```text
||D_t^j W_(b,h,j)||_TV
 <=C_(B,j) exp(C_B j(j+1)h)(1+h^(-1))^j,                  (4.7)
```

uniformly for `b` in a fixed compact set `B`.

This does not affect the fixed-order lemma. It also does not affect the
fixed-total-width trace used in Proposition 6.2: with `j=k` and `h=ell/k`,
the corrected exponential is `exp(O_(ell,B)(k))`, while
`(1+h^(-1))^k=exp(O_ell(k log(k+2)))`. Thus the claimed bound

```text
exp(O_(ell,K)(k log(k+2)))X^(-Re(a)-k)                    (4.8)
```

survives.

## 5. Vaughan and uniformity audit

The coefficient identity

```text
Lambda
 =mu_(<=U)*log+Lambda_(<=V)-mu_(<=U)*Lambda_(<=V)*1
  +mu_(>U)*Lambda_(>V)*1                                  (5.1)
```

is exact. Cutoffs and the compact support of the test make every rearrangement
finite. The last term groups as

```text
a_(U,V)(n)
 =sum_(dbm=n; d>U,b>V)mu(d)Lambda(b)
 =(mu_(>U)*Lambda_(>V)*1)(n),                              (5.2)
```

or as the bilinear coefficient `mu(d) beta_V(r)` with `r=bm`. Thus the two
balanced variables are `d` and `r`, not `d` and `b`.

The three head evaluations follow from (4.6) at `a=1/2` and its derivative.
The terms `I_pol`, `I_0`, and hence `Z`, are mandatory exact centerings; no
PNT, Mertens power bound, or strip estimate enters their derivation.

The target is the scalar **complete** aggregate `|B-Z|`. It is not `B` alone,
not a generic bilinear operator norm, and not a sum of independently bounded
dyadic or cofactor blocks. After taking a compact coboundary and squaring, the
faithful energy must retain every unequal-product term, the tail--center cross
term, and the center square.

There is one separate bookkeeping warning for that later energy route. A
scale coboundary uses the same `U,V` at `R` and `R+ell`, whereas the pointwise
width law uses `U(R)=V(R)=floor(exp(theta R))`. A block proof must freeze the
cutoffs on each regular block and account for its cores and endpoints. One
may not difference the globally moving-cutoff field as if its cutoffs were
fixed. This warning does not alter the pointwise identity (2.1).

## 6. Replayed checks

The following existing deterministic tests were rerun:

```text
PYTHONPATH=src python3 -m unittest -v
  src/test_type2_block_mechanism_probe.py
  src/test_fixed_step_spectral_cooling_probe.py

8 tests passed.

cd src
python3 -m unittest -v test_fixed_box_width_spectrometer.py

6 tests passed.
```

The completed finite audit was rerun through product `512`. It checked `2,048`
coefficientwise Vaughan identities and `124` distinct semiprime groupings;
the exact rational quadratic closure error was zero. Its bounded arithmetic
scan again produced both signs for the off-diagonal-plus-center remainder and
ratios arbitrarily close to full diagonal cancellation in the tested grid.
These computations verify finite algebra and falsify simple sign shortcuts;
they do not prove an asymptotic saving.

A separate high-precision spot check of (4.6), for complex `a` and orders
`k=1,2,3,4`, showed the residual at the predicted `X^(-Re(a)-k)` scale. This
is diagnostic only; the proof is the distributional argument above.

## 7. Decision consequence

This audit removes the reduction itself as the main uncertainty. It also
removes it as a plausible source of a free gain.

The strongest currently available complete estimate is

```text
|B-Z| << x^(1/2)
 exp{-c(log x)^(3/5)(loglog x)^(-1/5)},                    (7.1)
```

whose effective power saving tends to zero. A new theorem proving (2.4)
would be real progress, but it would already be the desired uniform strip in
arithmetic form. Later all-conductor recompletion sharpens the warning: the
complete ordinary dual has coefficient

```text
(mu*Lambda)(n)=-mu(n)log n,
```

and reconstructs the original completed energy. Splitting its conductors,
cofactors, orientations, or center before cancellation changes the problem
and can erase the carrier.

Accordingly, the fixed-window chain should now be kept as an exact endpoint
and a falsifier for proposed arithmetic estimates, not described as a weaker
intermediate lemma. A subsequent search must either attack the completed
`-mu log` correlation at acknowledged strip strength or move to a genuinely
different sufficient condition; it should not add another coordinate change
inside this chain.
