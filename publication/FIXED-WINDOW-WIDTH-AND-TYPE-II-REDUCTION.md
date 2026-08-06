# A fixed logarithmic-window detector and its balanced Type-II reduction

Status: analytic manuscript draft, 2026-08-06.  Specialist review and a
dedicated priority search are still required.  This note does **not** prove
the Riemann Hypothesis.

## 1. What is proved

The fixed-window work has three main results.

1. One translated triangular von Mangoldt discrepancy measures the full
   horizontal width of the nontrivial zeta zeros.
2. Removing all prime powers except primes changes that discrepancy only by
   an explicit bounded term, and a one-sided logarithmic primitive gives the
   same detector in coboundary form.
3. For every fixed smoothing order, Vaughan's identity moves the detector
   into one explicitly centered near-square Type-II aggregate.  The two
   bilinear variables can be confined to
   `[x^(1/2-epsilon),x^(1/2+epsilon)]` for any fixed positive `epsilon`.

Tracking the smoothing-order constant also gives an unconditional
`x^(1/2+o(1))` arithmetic localization.  It is not presently an RH-equivalent
moving-test criterion.

The fixed-order statement is a reduction, not an estimate.  Boundedness of
the full fixed-order centered Type-II aggregate is still equivalent to RH.

The accompanying obstruction results explain why estimates that freeze a
cofactor, a singular mode, or the Type-I centering are not faithful to this
aggregate.  They do not rule out a direct joint arithmetic estimate.

## 2. The fixed-window theorem

Fix `ell>0` and set

```text
w_ell(u)=(1-abs(u)/ell)_+,
M_ell^2=16 sinh^2(ell/4)/ell,
Delta=sup_rho abs(Re(rho)-1/2).
```

Zeros are counted with multiplicity.  Define

```text
D_ell(R)
 =sum_n Lambda(n)n^(-1/2)w_ell(log n-R)
  -M_ell^2 exp(R/2).                                      (2.1)
```

### Theorem 2.1 (fixed-window width)

For every fixed `ell>0`,

```text
limsup_(R->infinity) log(1+abs(D_ell(R)))/R=Delta.         (2.2)
```

Consequently,

```text
RH
 <=> D_ell is bounded on a forward half-line
 <=> D_ell(R)=O_(ell,epsilon)(exp(epsilon R))
     for every epsilon>0.                                 (2.3)
```

### Proof spine

Let

```text
g_ell=ell^(-1/2)1_[-ell/2,ell/2],
T_ell(z)=4 sin^2(ell z/2)/(ell z^2).
```

The normalization-matched Guinand--Weil formula identifies the separated
box correlation with

```text
B_ell(R)=sum_rho m_rho T_ell(z_rho)exp(-i z_rho R),
z_rho=(rho-1/2)/i.                                        (2.4)
```

The coefficients are absolutely summable because `T_ell(z)=O_ell(|z|^-2)`
in the critical strip.  This gives the upper exponent `Delta`.  Every zero
of `T_ell` is real, so an off-line zeta zero produces a genuine pole in the
one-sided Laplace transform of (2.4).  Holomorphic uniqueness gives the
matching lower exponent, even if the supremum `Delta` is not attained.
The arithmetic formula differs from `-B_ell` only by an exponentially
decaying pole and archimedean correction.  This proves (2.2).

The full normalization and low-regularity discussion are in
[`FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`](../results/FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md).

## 3. Prime stripping and the coboundary

Let `P_ell` be (2.1) with the von Mangoldt sum replaced by

```text
sum_p (log p)p^(-1/2)w_ell(log p-R).
```

The square-prime term and all higher powers satisfy

```text
D_ell(R)
 =P_ell(R)+ell/2
  +O_ell(exp(-c sqrt(R))+(1+R)exp(-R/6)).                  (3.1)
```

Thus `P_ell` has the same exponent `Delta`.  For the one-sided ramp

```text
Phi_ell(t)=min(1,max(0,t/ell)),
J_ell=4(1-exp(-ell/2))/ell,
```

put

```text
C_ell(R)
 =sum_n Lambda(n)n^(-1/2)Phi_ell(R-log n)
  -J_ell exp(R/2).                                        (3.2)
```

Then

```text
D_ell(R)=C_ell(R+ell)-C_ell(R).                           (3.3)
```

The Perron multiplier of `C_ell` is

```text
(1-exp(-ell s))/(ell s^2),                                (3.4)
```

whose nonzero zeros lie on the imaginary axis.  Hence `C_ell` also has
growth exponent `Delta`.  Its correctly centered actual-prime counterpart is

```text
C_ell^p(R)
 =sum_p (log p)p^(-1/2)Phi_ell(R-log p)
  -J_ell exp(R/2)+R/2.                                    (3.5)
```

The difference `C_ell-C_ell^p` is an explicit constant plus an error
summable on every progression of step `ell`, and

```text
C_ell^p(R+ell)-C_ell^p(R)=P_ell(R)+ell/2.                 (3.6)
```

The triangle, prime-only, primitive, and Birkhoff-sum statements are
therefore coordinates on one detector, not independent RH proxies.

## 4. The fixed-order Euler lemma

The near-square reduction uses a genuine smoothing estimate, not a formal
appeal to Euler--Maclaurin.  Fix an integer `k>=1`, set `h=ell/k`, and define

```text
Phi_(h,k)(t)
 =(1/h^k)vol{u in [0,h]^k:u_1+...+u_k<t},

H_(h,k)(s)
 =(1/s)[(1-exp(-hs))/(hs)]^k.                              (4.1)
```

### Lemma 4.1 (logarithmic B-spline Euler summation)

If `K_a` is compactly contained in `0<Re(a)<1`, then, uniformly for
`a in K_a`,

```text
sum_n n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)H_(h,k)(1-a)+zeta(a)
  +O_(K_a,h,k)(X^(-Re(a)-k)).                             (4.2)
```

The derivative of the remainder in `a` is

```text
O_(K_a,h,k)(X^(-Re(a)-k)log X).                           (4.3)
```

To prove the lemma, write the left side as the `k`-fold multiplicative
average of `sum_(n<=X)n^(-a)`.  Periodic Euler summation expresses the sharp
remainder through mean-zero periodic Bernoulli functions.  An order-`k`
B-spline has a finite-measure `k`th distributional derivative.  Integrating
each Bernoulli term by parts `k` times therefore gains `X^-k`.  Uniformity in
a follows on compact subsets of the strip, and Cauchy's estimate justifies
differentiating the remainder.  A complete proof, including endpoint
conventions, is in Lemma 6.1 of
[`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`](../results/ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md).

The fixed-order proof also permits a useful uniform refinement.  If
`h=ell/k`, then for `a` in a fixed compact subset of the strip,

```text
abs(remainder)
 <=exp(C_ell k log(k+2))X^(-Re(a)-k),                     (4.4)
```

and the differentiated remainder gains only `1+log X`.  The proof combines
`norm(Bbar_n)_infinity<=4n!/(2pi)^n` with

```text
norm(D^q kappa_(ell/k,k))_TV<=(2k/ell)^q.
```

Proposition 6.2 of the detailed report gives the complete constant trace.

## 5. The balanced Vaughan theorem

Let

```text
F_x(n)=n^(-1/2)Phi_(h,k)(log(x/n)),
M_U(s)=sum_(d<=U)mu(d)d^(-s),
L_V(s)=sum_(b<=V)Lambda(b)b^(-s),
beta_V(r)=sum_(b|r,b>V)Lambda(b),

B_(U,V)^(k)(x)
 =sum_(d>U,r>V)mu(d)beta_V(r)F_x(dr).                     (5.1)
```

Put `J_0=H_(h,k)(1/2)`, `J_1=H_(h,k)'(1/2)` and define

```text
I_pol
 =sqrt(x){M_U(1)[J_0 log x+J_1]
          +J_0[M_U'(1)-M_U(1)L_V(1)]},

I_0
 =-zeta'(1/2)M_U(1/2)+L_V(1/2)
  -zeta(1/2)M_U(1/2)L_V(1/2),

Z_(U,V)^(k)(x)=J_0 sqrt(x)-I_pol-I_0.                      (5.2)
```

### Theorem 5.1 (fixed-order near-square reduction)

If `U,V` are positive integer cutoffs and `UV<=x exp(-ell)`, then

```text
C_(h,k)(log x)
 =B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
  +O_(h,k)([U^(k+1)log(2x)+(UV)^(k+1)]/x^(k+1/2)),        (5.3)
```

where `C_(h,k)` is (3.2) with `Phi_ell,J_ell` replaced by
`Phi_(h,k),J_0`.

This is Vaughan's identity

```text
Lambda
 =mu_(<=U)*log+Lambda_(<=V)-mu_(<=U)*Lambda_(<=V)*1
  +mu_(>U)*Lambda_(>V)*1                                  (5.4)
```

followed by Lemma 4.1 on each Type-I term.  No estimate for the balanced
term is inserted.  More explicitly, if `mathcal L_x` denotes evaluation
against `F_x`, the three head terms are

```text
mathcal L_x(mu_(<=U)*log)
 =sqrt(x){M_U(1)[J_0 log x+J_1]+J_0 M_U'(1)}
  -zeta'(1/2)M_U(1/2)
  +O_(h,k)(U^(k+1)x^(-k-1/2)log(2x)),

mathcal L_x(Lambda_(<=V))=L_V(1/2),

-mathcal L_x(mu_(<=U)*Lambda_(<=V)*1)
 =-J_0 sqrt(x)M_U(1)L_V(1)
  -zeta(1/2)M_U(1/2)L_V(1/2)
  +O_(h,k)((UV)^(k+1)x^(-k-1/2)).                         (5.4a)
```

These main terms sum to `I_pol+I_0`, and the two remainders are exactly the
error in (5.3).

Choose

```text
U=V=floor(x^theta),
0<theta<=theta_k=1/2-1/[4(k+1)].                          (5.5)
```

The error in (5.3) is bounded at `theta_k` and tends to zero below it.  The
nonzero zeros of `H_(h,k)` lie on the imaginary axis, so

```text
limsup_(x->infinity)
 log(1+abs(B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)))/log x
 =Delta.                                                   (5.6)
```

Consequently, boundedness or any fixed polylogarithmic bound for the full
centered aggregate is RH-equivalent.  Both bilinear variables lie between
`x^theta` and `x^(1-theta)`.  Given fixed `epsilon>0`, a fixed sufficiently
large `k` puts both in
`[x^(1/2-epsilon),x^(1/2+epsilon)]`.

The fixed-order equivalence (5.6) does not by itself permit `k=k(x)`,
`theta=1/2`, or an `x^(1/2+o(1))` **equivalence**.  The uniform estimate
(4.4) does, however, give the following unconditional arithmetic
localization.  If

```text
k=k(x)->infinity,       k log(k+2)=o(log x),
c>1/4,                  U=V=floor(x^(1/2-c/k)),            (5.7)
```

then

```text
C_(ell/k,k)(log x)
 =B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
  +O_ell(x^(-(2c-1/2)+o(1))).                             (5.8)
```

All bilinear variables are `x^(1/2+o(1))`, and the retained cofactors are
`x^o(1)`.  This is not known to imply RH in the reverse direction because
the test transform changes with `x`; the fixed-transform Laplace-pole
argument no longer applies.

## 6. Why the pieces cannot be bounded separately

The obstruction has one concise form:

> The bounded observable is a moving, globally centered cancellation across
> the full cofactor sum, Möbius parity, the Type-I head, and every hyperbola
> mode.  Freezing a piece or taking absolute values destroys the factor that
> lowers higher-order critical-zero poles to simple poles.

Four exact results expose different faces of this obstruction.

### 6.1 Fixed cofactor blocks lose the zeta factor

For fixed cutoffs, the balanced coefficient series is

```text
(1-zeta(s)M_U(s))[-zeta'(s)/zeta(s)-L_V(s)].              (6.1)
```

At a multiplicity-`m` zeta zero it has the same simple principal part as
`-zeta'/zeta`.  Restricting the cofactor to a fixed nonempty finite set
`mathcal K` instead gives

```text
Q_mathcalK(s)[1/zeta(s)-M_U(s)]
             [-zeta'(s)/zeta(s)-L_V(s)],
Q_mathcalK(s)=sum_(q in mathcal K)q^(-s).                 (6.2)
```

This has a pole of order `m+1` whenever `Q_mathcalK(rho)!=0`.  A nonzero
Dirichlet polynomial and the smoothing resonance lattice each have only
`O(T)` zeros through height `T`, whereas the known distinct odd-order
critical-line zeros number `>>T log T`.  One can therefore choose a critical
zero avoiding both exceptional sets.  Any centering whose transform is
regular or at most simple there cannot make the block bounded.  The
separately frozen Euler bulk and boundary pieces obey the same conclusion;
their multipliers are explicitly nonzero at a suitable critical zero.

This is a fixed-truncation theorem.  It does not rule out co-varying dyadic
or cofactor decompositions.

### 6.2 The ambient near-square operator does not contract

In logarithmic coordinates the sharp kernel is

```text
(T_L f)(u)=integral_0^(L-u)f(v)dv,
```

with singular values

```text
sigma_j(T_L)=2L/[(2j-1)pi].                               (6.3)
```

Fixed-width smoothing changes it by `o(L)` in Hilbert--Schmidt norm.  Thus
removing any fixed number of moment or singular directions leaves norm
comparable to `L`.  This excludes fixed-rank, coefficient-blind ambient-norm
contractions; it says nothing against cancellation of the actual arithmetic
vectors across all modes.

### 6.3 Local reflection reinforces a semiprime collar

At equal cutoff `y`, fix `c>1` and suppose
`c^2 y^2<=x exp(-ell)`.  Then primes `p,q in (y,cy]`, including the diagonal,
lie on the ramp plateau and contribute the coherent block

```text
-A_y B_y~-4(sqrt(c)-1)^2 y/log y,
A_y=sum_(y<p<=cy)(log p)/sqrt(p),
B_y=sum_(y<p<=cy)1/sqrt(p).                                (6.4)
```

Hence a product-fiber or local divisor-pair sign reversal cannot remove the
central collar.  Cancellation may still occur against other products,
parity sectors, cofactors, or the Type-I head.

### 6.4 The natural exterior square changes sign

The four cutoff sectors form a rank-one outer-product table before ramp
evaluation.  Entrywise ramp evaluation destroys rank one.  Its exact
`2 x 2` exterior-square formula has both signs, including after prime powers
are deleted.  This rules out a determinant-sign shortcut for that table, not
a different completed matrix or nondeterminantal invariant.

The detailed proofs are in
[`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`](../results/ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md),
[`MOVING-TYPE-II-NORM-CHECKPOINT.md`](../results/MOVING-TYPE-II-NORM-CHECKPOINT.md)
and
[`JOINT-TYPE-II-CUTOFF-IDENTITY.md`](../results/JOINT-TYPE-II-CUTOFF-IDENTITY.md).

## 7. Evidence, debt, and nonclaims

| Item | Evidence | Present debt |
|---|---|---|
| Fixed-window width | Analytic proof from Guinand--Weil, zero symmetry, and Riemann--von Mangoldt counting | Package the piecewise-linear explicit formula as one precise cited theorem; independent specialist review |
| Prime stripping | Analytic proof from PNT and Chebyshev bounds | Independent review of constants and endpoint conventions |
| Fixed- and growing-order Euler lemma | Self-contained analytic proof with `exp(O_ell(k log k))` constant | Independent review; no varying-test converse |
| Vaughan reduction | Exact convolution algebra plus the Euler lemma | Independent review; the aggregate estimate is open |
| Reflection and determinant signs | Analytic no-go statements plus small Arb witnesses | Freeze environment and source hashes before release |

No theorem in this note is presently formalized in Lean.  The Arb programs
certify only their stated finite enclosures and are not needed for the main
width or Vaughan theorems.

In particular, this note does not prove RH, give probabilistic evidence for
RH, bound a separate Type-II block, construct a positive metric, justify an
RH converse for a growing smoothing order, or establish novelty.  Nearby
literature includes classical explicit-formula detectors and Vaughan-type RH criteria; a search
that fails to find this exact normalization would still not establish
priority.

## 8. The fair next checkpoints

The direct branch should be tested in stages.

1. Derive a cofactor-complete dispersion or fourth-moment identity for
   `B-Z` without taking absolute values of its sectors.
2. Seek any fixed power saving
   `B-Z=O(x^(1/2-eta))`.  By (5.6) this would prove a genuine fixed
   zero-free strip, not RH; failure of one proposed dispersion engine would
   prune only that engine.
3. Only if the same mechanism preserves cross-cofactor cancellation should
   it be tested at the polylogarithmic, RH-equivalent scale.
4. For the growing-order fork, prove a varying-test oscillation converse
   before treating a subpower moving-test residual as an RH criterion.

A method should be retired when an exact counterexample violates its claimed
sign or contraction, or when its defining inequality provably deletes the
cofactor cross terms.  A poor finite experiment, a coefficient-blind model,
or failure to reach the final polylogarithmic scale is not by itself a fair
reason to discard a completion-preserving method.
