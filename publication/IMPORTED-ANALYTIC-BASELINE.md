# Imported analytic-number-theory baseline for R65--R98

Status: literature survey and normalization audit, 2026-08-07.  Sources were
checked through that date.  This document is the claim-of-record for what the
active fixed-window/Vaughan program may use as an imported lemma rather than
advertise as a research goal.

This is a focused survey of the analytic inputs that can plausibly touch the
R71--R98 completed energy and its fixed-strip descendants.  It is not a bibliography of every theorem related
to the Riemann Hypothesis.  Published theorems, current preprints, rigorous
computations, and project deductions are kept in separate evidence classes.

## 1. Executive verdict

The following items are baseline, not goals:

1. compact-test Guinand--Weil and smoothed Perron formulas;
2. Riemann--von Mangoldt zero counting and logarithmic shell bounds;
3. exact Vaughan and generalized Heath--Brown decompositions;
4. arbitrary-order periodic Euler--Maclaurin and cardinal B-spline bounds;
5. the Vinogradov--Korobov zero-free region and its PNT/Mertens consequences;
6. Montgomery--Vaughan mean values and the classical large-values bounds;
7. Guth--Maynard's improved large-values and zero-density theorems;
8. current almost-all short-interval and shifted-correlation theorems;
9. rigorous finite-height verification of RH; and
10. the native 2026 MRSTT Type-II contagion and Wright fixed-denominator
    Kloosterman estimates, with their R71 application gates kept explicit.

There is also one correction to the active project ledger.  The fixed-`h`,
growing-`k` Euler comparison between the exact-head field and the frozen
rank-two center is a classical-synthesis lemma, not a new cancellation
estimate.  Written with the exact R71 parameters, it transfers the proved
Vinogradov--Korobov subpower bound to the frozen-center field.

What is **not** supplied by the literature is one fixed power in the complete
R71 norm:

```text
E_I^(frozen) <=exp((1-2eta+o(1))R),       eta>0 fixed.   (1.1)
```

No surveyed theorem retains every Mobius cofactor, the full Type-I head or
its evaluated rank-two center, every regular block, and a fixed power saving
simultaneously.  This is the genuine frontier.  R80's proportional-order bank
has discharged the program-level moving-edge converse; the remaining gap is
the arithmetic upper bound, not recurrence of an unattained horizontal edge.

## 2. The normalization every imported theorem must meet

Put `x=exp(R)`.  The finite R71 field has the form

```text
G_I(r)=B_I(r)-z_I(r),                                   (2.1)

B_I(r)=sum_n a_(U,V)(n)n^(-1/2)V_(h,k)(r-log n),

a_(U,V)=mu_(>U)*Lambda_(>V)*1,

z_I(r)=exp(r/2)(alpha_I+beta_I r)/norm(W_(h,k))_2.       (2.2)
```

The cutoffs are frozen on a regular logarithmic block.  In the balanced
growing-order regime,

```text
U,V=x^(1/2-O(1/k)),       n=x^(1+o(1)),
d,r=x^(1/2+o(1)),         cofactor=x^o(1).               (2.3)
```

The raw total-product Dirichlet polynomial therefore has length
`N=x^(1+o(1))`; its two balanced factor polynomials have lengths
`x^(1/2+o(1))`.  The compact transform is

```text
F_I(t)=Fourier[chi_I G_I](t).                            (2.4)
```

Near the block boundary its atomic kernels depend on `n`, so it is not
globally legitimate to replace (2.4) by one multiplier times an uncompleted
Dirichlet polynomial.  The rank-two center is of the same critical
exponential size as the tail and must be kept until after subtraction.

For fixed Sobolev order, a hypothetical zero of displacement `d` is
localized only up to a height `T=x^(tau+o(1))` with `tau<1/2`.  On the
growing-order schedule the relevant height is `x^o(1)`.  An input passes the
R71 gate only if it controls the complete object on every carrier block; an
average over heights, shifts, or physical interval starts is not silently
interchangeable with that quantifier.

The two calibrated energy scales are

```text
known subpower: E_I <=x exp[-c(log x)^(4/5)(log log x)^(-3/5)],

fixed strip:    E_I <=x^(1-2eta+o(1)),       eta>0 fixed. (2.5)
```

The first line is `x^(1-o(1))`; it does not approach the second line.

## 3. Explicit formulas, counting, and decomposition

### LIT-EF1 -- Guinand--Weil explicit formula

Under the standard analytic-strip and decay hypotheses on a test `h`, the
sum of `h` over the nontrivial zeros equals the pole, gamma, and prime-power
terms with the corresponding Fourier normalization.  Compactly supported
smooth prime-side tests, or their distributional limits after the stated
approximation, are therefore legitimate zero detectors.

Primary sources are [Guinand, 1948](https://doi.org/10.1112/plms/s2-50.2.107)
and [Weil, 1952](https://cds.cern.ch/record/471308).  Booker's
[distributional formulation](https://arxiv.org/abs/1308.3067) is a modern
primary reference.  The repository exposes the imported interface in
`RHBridge/GuinandWeilLiterature.lean`.

**R71 import.**  For the B-spline coboundary the zero multiplier is explicit
and decays as `exp(O_h(k))(1+abs(gamma))^(-k-1)`.  The zero sum is absolutely
convergent for every fixed `k`; in the growing-order upper bound the exact
multiplier supplies the required uniformity directly.

**Nonclaim.**  An explicit formula is an equality.  It does not provide the
fixed-power upper bound (1.1).

### LIT-ZC1 -- Riemann--von Mangoldt counting

With multiplicity,

```text
N(T)=T/(2pi) log[T/(2pi e)]+O(log T).                    (3.1)
```

In particular, a unit additive shell at height `T` contains `O(log T)`
zeros and a multiplicative shell `[exp(j),exp(j+1))` contains
`O(exp(j)(j+1))` zeros.  A current explicit form, valid for `T>=e`, is

```text
abs(N(T)-T/(2pi)log[T/(2pi e)])
 <=0.10076 log T+0.24460 log log T+8.08344.              (3.2)
```

See [Bellotti--Wong](https://arxiv.org/abs/2412.15470).  The repository's
qualitative imported interface is `RHBridge/ZetaZeroCountingLiterature.lean`.

**R71 import.**  This is the shell-count input in the R79 zero sum.

**Nonclaim.**  Counting all zeros does not control how far the rightmost one
lies from `Re(s)=1`.

### LIT-DEC1 -- exact Vaughan identity

For arbitrary finite `U,V>=1`, coefficientwise,

```text
Lambda
 =mu_(<=U)*log-mu_(<=U)*Lambda_(<=V)*1
  +mu_(>U)*Lambda_(>V)*1+Lambda_(<=V).                  (3.3)
```

The identity has no support condition; restrictions such as `UV<=x` enter
only after a test weight is applied.  The original source is
[Vaughan, 1977](https://zbmath.org/0498434); an accessible derivation with
the sign ledger is in [Helfgott, Section 3.3.1](https://arxiv.org/abs/1501.05438).

**R71 import.**  The tail coefficient, all cofactors, and the Type-I head are
an exact decomposition.  Changing `U,V` cannot create cancellation by
itself: exact recompletion returns the same von Mangoldt field.

### LIT-DEC2 -- Heath--Brown generalized identity

If `X^K>=x`, then for `n<=x`,

```text
Lambda(n)=sum_(j=1)^K (-1)^(j-1) binom(K,j)
 [mu_(<=X)^(*j)*1^(*(j-1))*log](n).                     (3.4)
```

See Heath--Brown, Lemma 1, pp. 1366--1367
[DOI](https://doi.org/10.4153/CJM-1982-095-9).

**R71 import.**  This is available if a multilinear decomposition is useful.
It is not an improvement to the current transfer: it creates up to `2K`
variables and `O((log x)^(2K))` dyadic pieces and does not preserve the
rank-two center as cleanly as (3.3).

### LIT-DEC3 -- exact finite Ramanujan expansion

For a finite range `N`, put

```text
Lambda_N(n)=-sum_(d<=N,d|n)mu(d)log d.
```

The divisor identity `sum_(q|d)c_q(n)=d 1_(d|n)` gives the exact finite
expansion

```text
Lambda_N(n)=sum_(q<=N) LambdaHat_N(q)c_q(n),            (3.5)

LambdaHat_N(q)
 =-mu(q)/q sum_(d<=N/q,(d,q)=1)mu(d)log(dq)/d,

abs(LambdaHat_N(q))<<log^2(N)/q.                       (3.6)
```

For `n<=N`, `Lambda_N(n)=Lambda(n)`.  See equations (5)--(6) of
[Laporta, *On Ramanujan expansions and primes in arithmetic
progressions*](https://doi.org/10.1007/s12188-024-00282-4).

**R71 import.**  This is an exact reduced-rational decomposition on every
finite active product range, and the crude Hilbert coefficient ledger is only
polylogarithmic:

```text
sum_(q<=N)phi(q)abs(LambdaHat_N(q))^2<<log^5(N).        (3.7)
```

Poisson summation of the periodic comb for `c_q` leaves one explicit zero
frequency, of coefficient

```text
LambdaHat_N(1)-1
 =sum_(d<=N)-mu(d)log(d)/d-1.                          (3.8)
```

All other frequencies are reduced nonzero rationals modulo integers.

**R82 correction.**  Equation (3.8) is exactly the logarithmically weighted
Mertens tail, and a separate fixed power for it implies a fixed zero-free
strip.  It is not, however, an invariant obstruction: LIT-DEC4 below gives an
exact finite null gauge that moves it into nonzero modes at polylogarithmic
coefficient cost.  The resulting coherent large-modulus packet remains at
full energy, so this coordinate change is not a power estimate.

The formal limiting coefficients `mu(q)/phi(q)` are not a pointwise or
absolutely convergent expansion of `Lambda`.  Their standard truncation is a
Heath--Brown major-arc approximant, useful in Type-I, moment, and little-Gowers
norms; modern examples are Lemma 4.6 and Proposition 4.7 of
[Krause--Mousavi--Tao--Teravainen](https://doi.org/10.1017/etds.2025.10202).
It is not an `L2` approximation: for `Q=X^theta< X` its error on primes alone
has square mass `gg_(theta)X log X`, the full natural scale.

### LIT-DEC4 -- Ramanujan 0-clouds and Farey conditioning

Remark 2 of the
[Coppola--Ghidelli preprint](https://arxiv.org/abs/2005.14666), specializing
the exotic class of its Proposition 2, gives the finite-for-each-argument
identity

```text
sum_(K>=0)c_(p^K)(n)=0.                                (3.9)
```

When `p` does not divide `n`, (3.9) reduces to `c_1(n)+c_p(n)=0`.
Coppola--Laporta study the related `q>2H` short-interval sporadic regime in
[arXiv:1312.5701](https://arxiv.org/abs/1312.5701).

**R82 import.**  On active integers `n<=Y`, average
`c_1+c_p=0` over primes `Y<p<=2Y` with inverse-totient weights.  This moves
the coefficient (3.8) into nonzero reduced-rational modes, while

```text
sum_q phi(q)|htilde_q|^2<<log^5 Y.                     (3.10)
```

The exact theorem and vanishing Schur complement are in
[`FINITE-RAMANUJAN-NULL-GAUGE-GATE.md`](../results/FINITE-RAMANUJAN-NULL-GAUGE-GATE.md).

This redundancy forbids a generic frame argument.  Farey fractions of order
`Q` have spacing `asymp Q^(-2)`, and the sharp generic large-sieve scale is
`T+Q^2`; see
[Montgomery--Vaughan](https://doi.org/10.1112/jlms/s2-8.1.73) and
[Moitra's conditioning threshold](https://doi.org/10.1145/2746539.2746561).  At
`T asymp Q asymp Y`, the null cloud itself has logarithmic coefficient norm
but, for a fixed nondegenerate shell window, synthesizes natural energy
`asymp Y`.  Nonzero frequency plus a
polylogarithmic ledger therefore cannot imply a power saving.

**Nonclaim.**  The scale-adapted gauge is an exact coordinate improvement,
not a new zero-free region.  Completing its reciprocal phase in `theta`
returns the original shifted Ramanujan correlation; after its equal-prime
diagonal is restored, a separate native upper-half packet is the centered
top-prime covariance.

## 4. Zero-free, PNT, and Mertens baselines

### LIT-ZF1 -- Vinogradov--Korobov region

Bellotti proves an explicit near-line bound for zeta and, in the published
version, a zero-free region of the shape

```text
beta <=1-1/[53.989(log abs(gamma))^(2/3)
                    (log log abs(gamma))^(1/3)]          (4.1)
```

for the stated finite-height range, with asymptotic constant `48.0718`.
See the [published article](https://doi.org/10.1016/j.jmaa.2024.128249);
the older arXiv abstract records the slightly weaker finite constant
`54.004` and the same asymptotic constant
[arXiv:2306.10680](https://arxiv.org/abs/2306.10680).

A March 2026 preprint gives the improved classical explicit region

```text
beta <=1-1/[4.896 log abs(gamma)],       abs(gamma)>=3.  (4.2)
```

See [Bellotti--Trudgian--Yang](https://arxiv.org/abs/2603.21490).  Equation
(4.2) improves finite-height classical constants; asymptotically it does not
replace the Vinogradov--Korobov shape (4.1).

**R71 import.**  With logarithmic height `j=log abs(gamma)`, the horizontal
and multiplier losses combine as

```text
k j+cR j^(-2/3)(log j)^(-1/3).                          (4.3)
```

Optimizing gives

```text
S(R,k)asymp R^(3/5)k^(2/5)[log(R/k)]^(-1/5).            (4.4)
```

At `k=floor(sqrt(R)/log R)`, this is
`R^(4/5)(log R)^(-3/5)`.

**Nonclaim.**  Since `S(R,k)=o(R)`, current zero-free technology cannot turn
this calculation into a fixed `eta` in (1.1).

### LIT-ZD1 -- density near the Vinogradov--Korobov edge

Bellotti's 2025 preprint proves that sufficiently close to the left edge of
the VK zero-free region, `N(sigma,T)=O(1)`, and obtains the optimal PNT
transfer for a zero-free boundary `nu(t)`:

```text
psi(x)-x << x exp[-omega(x)],
omega(x)=min_(t>=1){nu(t)log x+log t}.                   (4.5)
```

For the VK boundary this has the familiar
`(log x)^(3/5)(log log x)^(-1/5)` scale.  See
[Bellotti](https://arxiv.org/abs/2508.02041).  This is a current preprint,
not a published input.

**R71 import.**  It supplies a sharp PNT safety net and explains the fixed-`k`
`3/5` saving.

**Nonclaim.**  `O(1)` possible zeros is not zero possible zeros.  One
off-line zero is enough to create the forbidden exponential carrier.

### LIT-MER1 -- unconditional Mertens bound

Lee--Leong prove explicit estimates of the form

```text
M(x) << x exp[-c(log x)^(3/5)(log log x)^(-1/5)]         (4.6)
```

and compatible bounds for `1/zeta(s)` near the one-line.  See
[Lee--Leong, v4](https://arxiv.org/abs/2208.06141).

**R71 import.**  Separate Mobius partial sums may be bounded at the VK
subpower scale.

**Nonclaim.**  Equation (4.6) is `x^(1-o(1))`, not a fixed power.  Uniformly
controlling every independent plateau rectangle by a fixed power would
already continue `1/zeta` into a fixed half-plane and is stronger than the
joint estimate being sought.

## 5. Mean values, large values, and moments

### LIT-MV1 -- Montgomery--Vaughan mean value

For distinct real frequencies `lambda_j`, with
`delta_j=min_(m!=j)abs(lambda_j-lambda_m)`, Hilbert's inequality gives

```text
integral_0^T abs(sum_j a_j exp(i lambda_j t))^2 dt
 =sum_j abs(a_j)^2[T+O(delta_j^(-1))].                  (5.1)
```

For `lambda_n=log n`,

```text
integral_0^T abs(sum_(n<=N)a_n n^(-it))^2dt
 =T sum abs(a_n)^2+O(sum n abs(a_n)^2)
 <<(T+N)sum abs(a_n)^2.                                 (5.2)
```

The primary source is
[Montgomery--Vaughan](https://doi.org/10.1112/jlms/s2-8.1.73).

**R71 import.**  For a balanced factor `N=x^(1/2+o(1))` and
`T=x^o(1)`, (5.2) costs `x^(1/2+o(1))`; Cauchy on two factors costs
`x^(1+o(1))`.  For the total-product polynomial `N=x^(1+o(1))`, the same
length term appears directly.  Thus this theorem proves the baseline
`eta=0`, not (1.1).

Applying (5.2) to the square of a polynomial gives

```text
integral abs(P)^4
 <<(T+N^2)sum_m abs(sum_(n_1n_2=m)a_(n_1)a_(n_2))^2.    (5.3)
```

Even when exact product grouping makes the last coefficient norm
subpower, the `N^2` term is the generic `x^(2+o(1))` fourth-moment barrier.

### LIT-LV1 -- Guth--Maynard large values

Let `abs(b_n)<=1`, let the `t_r` be one-separated in `[0,T]`, and suppose

```text
abs(sum_(N<=n<=2N)b_n n^(it_r))>=V.
```

Guth--Maynard prove

```text
#r <=T^o(1)[N^2 V^(-2)+N^(18/5)V^(-4)
                         +T N^(12/5)V^(-4)].            (5.4)
```

See [Theorem 1.1](https://arxiv.org/abs/2405.20552) and the
[Annals article](https://doi.org/10.4007/annals.2026.203.2.6).  Their
zero-density consequences include

```text
N(sigma,T)<=T^[15(1-sigma)/(3+5sigma)+o(1)],            (5.5)
```

and, after combination with the classical range,
`T^[30(1-sigma)/13+o(1)]`.  They also prove primes in every interval of
length at least `x^(17/30+epsilon)` and an almost-all result down to
`X^(2/15+epsilon)`.

**R71 import.**  At the normalized total-product threshold
`V=N^(1/2+alpha+o(1))`, the first term in (5.4) is
`N^(1-2alpha+o(1))`, positive for every `alpha<1/2`.  Moreover, the main
improvement regime asks for a much larger `T` relative to `N` than the R71
carrier window supplies.  Equation (5.4) can count many separated peaks; it
does not exclude one completed peak of width below one.

### LIT-LV2 -- reverse zero-density-to-large-values implication

Matomaki--Teravainen show that suitable zeta zero-density estimates imply
large-value bounds for Dirichlet polynomials; their Proposition 1.1 gives the
familiar zero-to-large-value direction and Theorem 1.2 a quantitative
reverse direction.  See
[arXiv:2403.13157](https://arxiv.org/abs/2403.13157).

**R71 import.**  Zero density and large values are not independent black
boxes in this regime.  Feeding a density theorem back into the completed
energy can control a number of exceptions but cannot exclude the one
exception that would be fatal.

### LIT-MOM1 -- classical zeta moments

Heath--Brown's fourth-moment theorem gives

```text
integral_0^T abs(zeta(1/2+it))^4dt
 =T P_4(log T)+O(T^(7/8+epsilon)),                       (5.6)
```

where `P_4` has degree four and leading coefficient `1/(2pi^2)`; see the
[primary article](https://doi.org/10.1112/plms/s3-38.3.385).  Heap,
Radziwill, and Soundararajan prove, for fixed `0<=q<=2`, the expected-order
upper bound

```text
integral_T^(2T) abs(zeta(1/2+it))^(2q)dt
 <<_q T(log T)^(q^2);                                   (5.7)
```

see [arXiv:1901.08423](https://arxiv.org/abs/1901.08423).

**R71 import.**  These are valid zeta baselines.

**Nonclaim.**  `F_I` is neither zeta nor zeta times a harmless short twist.
The factorization of its untruncated tail holds initially only to the right
of one and introduces `zeta'/zeta` poles when separated.  Localization,
Mobius cofactors, the Type-I head, and the rank-two center are all missing
from (5.6)--(5.7).  Conditional moment results assuming RH cannot be inputs
to an RH proof.

### LIT-DISP1 -- fixed-denominator trilinear Kloosterman fractions

Wright's Theorem 2.1 bounds a trilinear reciprocal-phase sum with a partially
fixed denominator.  In the balanced schematic regime

```text
M=N=x^(1/2+o(1)),       R_0=x^o(1),                     (5.8)
```

and with the phase numerator inside the theorem's polynomial range, the
worst displayed term gives a nominal local gain

```text
M^(-1/20+o(1))=x^(-1/40+o(1)).                         (5.9)
```

See [arXiv:2604.25177](https://arxiv.org/abs/2604.25177), submitted
2026-04-28.  This is a current preprint, not a published theorem.
The audit uses the weaker displayed statement of Theorem 2.1; one
intermediate proof display in v1 has a different power of its numerator-length
parameter.

**R71 candidate.**  R81 now gives the exact cofactorwise nonzero additive-mode
expansion.  Grouping its double modes by `theta=an-bm` and applying Poisson
summation on the solution lattice literally produces Wright's reciprocal
phase on the off-axis sector.  Completing that lattice inserts the one-sided
zero-mode axes, and absolute dyadic summation loses the conditionally
convergent all-cofactor center.  Thus no completed Wright bound is currently
proved.  At fixed proportional slope, an R71 cofactor has size
`x^(A_c lambda+o(1))` on the central shell and
`x^((A_c+h)lambda+o(1))` at the upper edge of the full window, not `x^o(1)`.
In the favorable schematic regime the crude full-window native-form gain is
`1/40-(11A_c+10h)lambda/40+o(1)` before phase and mode losses.

**Nonclaim.**  Wright's phase parameter is a nonzero integer.  The exact
cofactorwise completion cancels its zero lattice mode, but every fixed
rational `a/q` still has a singular-series prime main term.  For the actual
proportional B-splines, an individual zero residue persists on a universal
shell-normalized band and has a nonzero Gamma limit at fixed nonzero scaled
frequency; total-zero-sum noncancellation remains open.  Moreover, a fixed
power for the bare conditional cofactor tail would itself imply a fixed
zero-free strip.  Thus “nonzero phase” does not by itself separate the theorem
from the pole-bearing Mellin carrier.  See
[`COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md`](../results/COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md).
Wright's Corollary 2.2 is logarithmic, averaged over moduli, and unbalanced;
it does not cover the completed balanced R71 form.

**Version warning.**  arXiv:2601.00292, which claimed a stronger bilinear
Kloosterman and twisted-moment result in January 2026, was withdrawn.  Its
authors report a missing `L^2` factor and explicitly state that the argument
no longer gives the claimed improvement.  It is not an admissible input.

## 6. Almost-all intervals and correlations

### LIT-COR1 -- shifted von Mangoldt correlations

Matomaki--Radziwill--Tao prove the expected asymptotic for
`sum_(X<n<=2X)Lambda(n)Lambda(n+h)` and related divisor correlations for all
but a logarithmically small proportion of shifts in a range of length

```text
X^(8/33+epsilon)<=H<=X^(1-epsilon),                     (6.1)
```

with an arbitrary log-power average saving.  See the
[primary paper](https://arxiv.org/abs/1707.01315) and
[journal DOI](https://doi.org/10.1112/plms.12181).

**R71 import.**  This controls almost every additive shift in the stated
range.

**Nonclaim.**  The R71 fourth moment has Mobius-weighted multiplicative
near-products plus a continuous center.  An average over additive `h` does
not show that its weight avoids every exceptional shift, and a log saving is
not a fixed power.

### LIT-COR2 -- higher uniformity in almost all intervals

For fixed-complexity nilsequences and
`X^(1/3+epsilon)<=H<=X`, Matomaki--Radziwill--Shao--Tao--Teravainen prove,
for almost all `x in [X,2X]`,

```text
sup_g abs(sum_(x<n<=x+H)
 (Lambda(n)-Lambda^sharp(n)) conjugate(F(g(n)Gamma)))
 <<H log^(-A)X                                           (6.2)
```

for every fixed `A`; they obtain corresponding Gowers-uniformity and
correlation consequences.  See
[arXiv:2411.05770v2](https://arxiv.org/abs/2411.05770) and
[DOI](https://doi.org/10.1007/s00222-026-01408-6).

Their theorem permits Archimedean phases `n^(-iT)` over a very large `T`
range, so phase range is not the mismatch.

**R71 import.**  The shell-truncated tail coefficient has the elementary
Type-II coefficient hypotheses:
`a_(U,V)=alpha*beta_V`, where `alpha` is the truncated Mobius factor and
`0<=beta_V(q)<=log q`, so its `L2` and `L4` bounds hold.  The formal contagion
scale inequalities permit a small fixed power density if the required
large-correlation set of starts is supplied; the coefficient calculation does
not supply that set.  Specializing Theorem 1.1(ii)/Corollary 1.2(ii) to linear
phases and using summation by parts does give a project corollary: on genuine
polylogarithmic minor arcs, the exact completed scalar has an arbitrary
logarithmic square saving for some favorable translate of an `H`-partition.

**Nonclaim.**  Type-`I_2` is not the correct interface: its bounded-variation
hypothesis fails for `Lambda_(>V)` already on `(V,2V]`.  The Type-II inverse
theorem places locally Mellin-like phases in a permitted progression-wise
major-arc class; it does not exclude the R71 carrier.  The theorem is scalar
and almost-all-start, not a bound for the deterministic joint
tail--head--continuum square or its frequency supremum.  Applying (6.2)
cofactor by cofactor and taking absolute values also destroys the completion.
The favorable translated partition is not the predetermined R71 bank, and the
saving is not a fixed power.  More decisively, fixed rational phases are not
minor: for a smooth critical weight,

```text
P_(chi_X)(a/q)
 ~mu(q)/phi(q) X^(1/2) integral chi_0(u)u^(-1/2)du     (6.2a)
```

for fixed squarefree `q` and `(a,q)=1`.  Hence any power version must retain a
full rational--Archimedean major-arc union, not only a band around zero.

### LIT-MOB1 -- Mobius in all short intervals

For every fixed `theta>0.55`, Matomaki--Teravainen prove

```text
sum_(x<n<=x+x^theta)mu(n)=o(x^theta)                    (6.3)
```

for every sufficiently large `x`; see
[arXiv:1911.09076](https://arxiv.org/abs/1911.09076) and
[JEMS DOI](https://doi.org/10.4171/JEMS/1205).

**R71 import.**  This is a genuine all-start Mobius cancellation theorem.

**Nonclaim.**  Its interval is much longer than the balanced multiplicative
resolution, its saving is not a fixed power, and it does not retain the
prime factor or center.

## 7. Oscillation, recurrence, and finite verification

### LIT-OSC1 -- fixed-function oscillation converses

Classical Ingham--Pintz methods turn a specified singularity or boundary
zero into `Omega` values of the corresponding PNT or Mertens remainder along
sequences, sometimes locating opposite signs within intervals whose
logarithmic length still grows.  Kaczorowski-type recurrence theorems give
level crossings on sufficiently long intervals for one fixed boundary
function; their equilibration length depends on that function.

Primary examples are Pintz's
[PNT remainder theorem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/37/0/102630/on-the-remainder-term-of-the-prime-number-formula-ii-on-a-theorem-of-ingham)
and Kaczorowski's [Acta Arithmetica work](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/57).

**R71 import.**  For any fixed detector they support the usual principle
that an off-line pole cannot remain invisible forever.

**Nonclaim.**  They do not give a recurrence length uniform for the
triangular array `k=k(R)->infinity`, and they do not prove positive-density
recurrence when `sup Re(rho)` is not attained.  Turan, Ingham, Pintz, and
Kaczorowski therefore do not close the R78 nonattained-edge gate.

R80 closes the program-level gate by changing to a proportional-order bank;
it does not obtain a recurrence theorem for the original single triangular
array.

### LIT-COMP1 -- rigorous verification through finite height

Platt--Trudgian rigorously verify, using interval arithmetic, that every
nontrivial zero with

```text
0<gamma<=3*10^12
```

lies on the critical line.  See
[arXiv:2004.09765](https://arxiv.org/abs/2004.09765) and
[the published DOI](https://doi.org/10.1112/blms.12460).

**R71 import.**  All low-zero terms below that height may be treated as
critical-line terms, if a quantitative constant calculation benefits from
doing so.

**Nonclaim.**  Finite verification has no direct effect on a possible
unbounded sequence of off-line zeros.  Likewise, positive-proportion
critical-line theorems count zeros but do not exclude even one off-line
zero.

### LIT-LINE1 -- positive proportion on the critical line

Bui--Conrey--Young prove that more than `41%` of the nontrivial zeros, in the
standard asymptotic counting sense, lie on `Re(s)=1/2`; see
[arXiv:1002.4127](https://arxiv.org/abs/1002.4127) and the
[published DOI](https://doi.org/10.4064/aa150-1-3).

**R71 import.**  This is useful global context and can reduce estimates that
sum nonnegative contributions over all zeros.

**Nonclaim.**  A positive-proportion theorem is compatible with a sparse
off-line sequence approaching `Re(s)=1`; it cannot prove a fixed strip or
remove a single R71 carrier.

## 8. Project corollary: the Euler/frozen-center transfer

This section is not quoted verbatim from one paper.  It is a conventional
corollary of exact Vaughan, arbitrary-order periodic Euler--Maclaurin, and
cardinal B-spline variation.  Its proof is recorded so it can be imported
thereafter rather than repeatedly posed as a research problem.

### Lemma PROJ-EUL1 -- uniform fixed-step B-spline Euler summation

For fixed `h>0`, let

```text
Phi_(h,k)(t)=h^(-k)vol{u in [0,h]^k:sum u_i<t},

H_(h,k)(s)=s^(-1)[(1-exp(-hs))/(hs)]^k.                 (8.1)
```

If `K` is compact in `0<Re(a)<1`, there is `C_(h,K)>0` such that, uniformly
for `a in K`,

```text
sum_n n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)H_(h,k)(1-a)+zeta(a)
  +O(exp[C_(h,K)(k^2+k log(k+2))]X^(-Re(a)-k)).         (8.2)
```

On an inner compact set the `a` derivative obeys the same bound with an
extra factor `1+log X`.

#### Proof spine

Apply the order-`k` periodic Euler formula to
`P_a(X)=sum_(n<=X)n^(-a)` and average it against

```text
kappa_(h,k)=(h^(-1)1_[0,h])^(*k).                       (8.3)
```

The classical Fourier series gives

```text
norm(Bbar_m)_infinity<=4m!/(2pi)^m,                     (8.4)
```

while convolution differentiation gives

```text
norm(D^q kappa_(h,k))_TV<=(2/h)^q.                      (8.5)
```

After `t=exp(-u)`, `0<=u<=hk`,

```text
D_t^k=(-1)^k exp(ku)D_u(D_u+1)...(D_u+k-1).             (8.6)
```

The exponential weight costs `exp(O_h(k^2))`; the differential product
costs `exp(O(k log k))`.  Integrating the periodic term by parts `k` times
uses the bounded primitive
`[r!/(r+k)!]Bbar_(r+k)`; its factorial ratio cancels the factorial in
(8.4).  The sharp Euler remainder obeys the same bound.  Cauchy's estimate
gives the derivative statement.

Classical references for the Euler and Bernoulli ingredients are
[DLMF 25.11](https://dlmf.nist.gov/25.11#iii) and
[DLMF 24.8](https://dlmf.nist.gov/24.8#i); Schoenberg's cardinal-spline
source is *Quart. Appl. Math.* 4 (1946), 45--99 and 112--141.  The exact
R71 proof is also continuous with Proposition 6.2 of
`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`; the only change is tracking
the growing support `hk` rather than fixing total width.

### Corollary PROJ-EUL2 -- frozen-center VK energy

Exact Vaughan and (8.2) give

```text
C_(h,k)(log x)=B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)+E(x),

abs(E(x))
 <<_h exp[C_h(k^2+klog(k+2))]
 [U^(k+1)log(2x)+(UV)^(k+1)]x^(-k-1/2).                (8.7)
```

Let a block start at `R_0`, freeze

```text
U=V=floor(exp[(1/2-c/k)R_0]),       c>1/4,              (8.8)
```

and assume

```text
hk^2<=(2c-o(1))R_0,       k^2=o(R_0).                   (8.9)
```

Uniformly through the block, the dominant `UV` error in (8.7) is

```text
exp[-(2c-1/2+O(1/k))R_0+C_hk^2+O(klog k)].              (8.10)
```

The `U` error is smaller.  Differencing the two primitive endpoints and
using `norm(W_(h,k))_2>=sqrt(hk)/2` costs only subexponential factors.  Hence
on

```text
k=floor(sqrt(R)/log R),       H=R/k,                    (8.11)
```

the normalized Euler defect is `exp(-kappa R)` for some fixed
`kappa>0`.  Minkowski's inequality transfers Theorem 3.1 of
`FULL-FIELD-VK-SUBPOWER-BOUND.md` to the frozen-center field:

```text
E_I^(frozen)
 <=exp[R-c'_h R^(4/5)(log R)^(-3/5)]                   (8.12)
```

for all sufficiently large regular blocks and some `c'_h>0`.

**Evidence class.**  Analytic theorem by classical synthesis; not Lean
formalized and not claimed as literature novelty.  Independent specialist
review remains release debt, but no new number-theoretic cancellation input
is missing from (8.2)--(8.12).

**Nonclaim.**  Equation (8.12) has effective `eta(R)->0`.  It proves neither
a fixed strip nor RH.

## 9. Pass/fail matrix for the live target

| Imported result | What it legitimately discharges | Why it stops before (1.1) |
|---|---|---|
| Guinand--Weil + RvM | exact zero expansion and summable shells | equality/counting, not cancellation |
| Vaughan/Heath--Brown | exact finite decompositions | rearrangement does not create a saving |
| finite Ramanujan basis + R82--R86 quotient/beat recompletion | exact all-nonzero reduced-rational modes; the determinant-zero singular-series fluctuation is smoothly polylogarithmic; the global canonical beat tensor has ratio form `W(theta/(pr))`; arithmetic centering isolates the mean-zero reciprocal component; signed compression identifies its exact zero orbit | reciprocal transport has no zero shift character, so the joint zero orbit is the canonical contact; the native complete block is natural-size in the frame norm, leaving only the specially weighted all-sector kernel pairing |
| fixed `q^(-epsilon)` cofactor damping | absolute outer-cofactor completion for a shifted zero detector | componentwise gain is at most the paid shift; rational and zero-mode sectors remain |
| Euler--Maclaurin + splines | full-to-frozen subpower transfer | error is negligible, but the main field remains |
| VK/PNT/Mertens | `x exp[-(log x)^(c+o(1))]` baselines | every saving is `x^(1-o(1))` |
| Montgomery--Vaughan | complete generic `L2` baseline | adjacent-log length term gives `eta=0` |
| Guth--Maynard | fewer large values; improved zero density | first term permits many peaks; wrong `N/T` regime |
| zeta moments | sharp moments of zeta itself | wrong object; completion and zero poles are missing |
| MRT/MRSTT | Type-II architecture and a translated-partition completed logarithmic square on genuine minor arcs | no fixed power or predetermined-bank bound; rational--Archimedean major arcs survive |
| Wright 2026 | a nominal fixed power for its native nonzero reciprocal-phase form; after R85, the mask-free mean-zero component and reciprocal derivative transfer fit its scalar sequence architecture modulo an explicit kernel ledger | resonant axes, the conditional all-cofactor tail, and the finite primitive common-`g` mask remain outside the completed bound; R86 proves that ordinary zero-orbit completion leaves `-gamma` and that the native block is not Hilbert-small |
| signed dispersion and spectral reciprocity | Drappeau retains an exact low-character projector in an unbalanced range; Andersen--Kiral, Blomer--Khan, Wu, and Yang retain explicit diagonal/degenerate terms under reciprocity | the square-root box is balanced and self-dual, the canonical contact is not the low-character projector, and Eisenstein differentiation gives divisor-log coefficients plus differentiated zero-pole residues rather than `Lambda` cancellation |
| Mobius all intervals | all-start qualitative cancellation | long interval, no prime factor or center |
| Pintz/Kaczorowski | recurrence for fixed functions/sequences | superseded for this family by the R80 proportional-order bank, but supplies no arithmetic power |
| finite verification | removes low-height uncertainty | cannot control arbitrarily high zeros |

## 10. Research allocation after import

The following should no longer appear as standalone research goals:

- recover the Vinogradov--Korobov exponent;
- prove a subpower PNT or Mertens bound;
- derive the exact Vaughan/Heath--Brown identity;
- prove a generic Dirichlet-polynomial mean value;
- obtain a zero-density estimate without an exclusion mechanism;
- finish the growing-order Euler trace;
- transfer the R79 subpower bound to the frozen center;
- adapt Type-`I_2` to the rough prime factor;
- prove a separate nonattained-edge recurrence theorem for R71; or
- force absolute convergence by fixed cofactor damping and estimate its
  sectors separately.

The live goals are narrower.

1. **Axis-renormalized off-axis theorem.**  R83 recompletes the
   determinant/dual-zero and `q=1` sectors on the R82 quotient.  The
   determinant-zero singular-series fluctuation has polylogarithmically
   bounded partial sums, while the exact remainder is the completed
   one-point `Lambda-dt` carrier.  Prove a fixed power only for its joint
   centered combination with the off-axis Wright block, before absolute
   values.  A separate axis/Mertens power and a coefficient-uniform theorem
   through a zero Kloosterman index are already fixed-strip-strength.
2. **Coefficient/phase alignment.**  R84 removes the generic tensor-rank and
   shift-triangle objections: the canonical common dual is
   `W(theta/(pr))`, and in the original cofactor expansion `k=j theta` gives
   a scalar Wright sequence with only divisor loss.  R85 proves that the
   correct inverse-phase center is the Ramanujan mean
   `mu_r(k)=c_r(k)/(r-1)`.  Existing theorems power-save the nonresonant
   mean-zero component, but leave
   `mu_r(k)h_p conjugate(h_r)-gamma_(p,r,theta)` at full contact scale.
   Reciprocal derivative transfer and the one exact top-prime affine null
   gauge do not change that projection.  R86 computes the signed operator
   before projection.  Reciprocal transport has no zero shift character, its
   joint zero orbit is exactly `-gamma`, and the actual native complete block
   has a uniform full-scale prime-point residual in the canonical frame norm.
   The finite primitive common-`g` mask also remains open.  What remains is
   therefore not a square-root-block contraction: it is a specially weighted
   theorem for the complete all-`g`, all-axis, all-seam R71 kernel pairing
   before absolute values.
3. **Native-form exponent and summation.**  Finish the uniform B-spline
   kernel seminorm, mask, seam, and large-`Z` integration-by-parts ledger in
   R84.  Wright's favorable full-window budget begins at
   `1/40-(11A_c+10h)lambda/40+o(1)`; no part may be silently spent.
4. **Centered rational-major-arc sector.**  Prove the dimensionally normalized
   vector estimate (6.12) of
   `PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md`, or its exact mode-form analogue,
   retaining the balanced tail, Type-I head, pole integral, and every fixed
   rational singular-series term inside one square.  Its power must remain
   fixed as the slope tends to zero.
5. **Complete fixed-power energy.**  Combine the preceding inputs with
   the R80 RH-complete bank.  A fixed strip requires a zero-slope amplitude
   gap below `1/2`; RH requires limiting amplitude zero.

Any successful fixed-power theorem in items 1 or 5 is already a new fixed
zero-free strip at exponent scale.  It should be evaluated as the central
breakthrough, not described as a preliminary estimate on the way to one.

## 11. Logical reality check

This survey changes bookkeeping, not the status of RH.  It proves no new
zero-free strip and no statement about independence from ZFC.  All imported
theorems and the project corollary above live inside ordinary analytic number
theory.  A ZFC-independence route would need a separate metamathematical
mechanism; none of the density, moment, explicit-formula, or recurrence
results surveyed here supplies one.

## 12. Search and version ledger

The search was run on 2026-08-07 against arXiv, publisher pages, journal DOI
records, and the repository's existing citations.  Primary-source searches
included the following phrases and their theorem/contrapositive variants:

```text
Riemann zeta zero-free region 2025 2026
Riemann zeta zero density large values Dirichlet polynomials
Mertens Vinogradov Korobov bound
Mobius all short intervals
von Mangoldt correlations almost all shifts
higher uniformity arithmetic functions almost all intervals
trilinear Kloosterman fractions fixed denominator
bilinear Kloosterman fractions withdrawn 2026
Vaughan identity generalized Heath-Brown identity
Riemann hypothesis zeros verified 3*10^12
Ingham Pintz Kaczorowski oscillation recurrence
zeta twisted fourth moment long Dirichlet polynomial
finite Ramanujan expansion incomplete von Mangoldt function
Ramanujan null function cloud finite Farey dictionary
large sieve Farey spacing Vandermonde conditioning
discrete prolate high pass frame conditioning powered Fejer
Slepian discrete prolate Moitra Vandermonde phase transition
Heath-Brown approximant primes Gowers norm L2
```

The 2026 Bellotti--Trudgian--Yang zero-free region and the 2025 Bellotti
zero-density/PNT result are marked as preprints.  MRSTT v2, dated 2026-01-23,
incorporates referee comments and is linked both to arXiv and its Inventiones
DOI.  Guth--Maynard is linked to the 2026 Annals version.  Bellotti's VK
finite constant is quoted from the published 2024 article; the older arXiv
abstract's `54.004` is retained only as a version warning.

Wright arXiv:2604.25177 is marked as an April 2026 preprint.  The withdrawn
arXiv:2601.00292 is retained only as a negative version warning and is not
used as a theorem.

Laporta's 2024 finite Ramanujan identity is imported exactly.  The 2025
Krause--Mousavi--Tao--Teravainen paper is used only to calibrate the weaker
norms in which the Heath--Brown approximant is effective; the prime-diagonal
failure in `L2` is proved directly in R81.

Coppola--Ghidelli's null-function identity is imported as the algebraic seed
for R82's scale-adapted gauge.  The optimized completed coefficient ledger,
vanishing Schur complement, theta-sampling fail-fast identity, R83 quotient
Feshbach form, and sector recompletion are project derivations.  No search
establishes an external novelty claim for them.

The R83 zero-index extension checked Bruggeman's original Kuznetsov formula,
Zagier's regularized Rankin--Selberg theorem, Pascadi's optimized
Deshouillers--Iwaniec input, and current generalized/pseudo-Laplacian
formulations.  Their nondegenerate trace formulas require nonzero Fourier
indices; regularization subtracts cusp growth from the zeroth coefficient but
does not remove the `1/zeta(2s)` in nonzero Eisenstein coefficients.  This is
recorded as a boundary of the imported theorems, not as a no-go theorem for a
new arithmetic cancellation between the axis and off-axis contact terms.

R83's primitive Farey-beat frame and square-root modulus scale are finite
project derivations.  R84 corrects the first generic tensor diagnosis: the
global canonical common dual has ratio structure `W(theta/(pr))` and admits
norm-stable log-Mellin separation.  Its coefficient is nevertheless attached
to the slow additive phase, not Wright's reciprocal phase.  The high-band
repair is calibrated against Slepian's discrete prolate theory and Moitra's
Vandermonde threshold; the project report also supplies its own powered-box
witness and exact contact-duality identity.

R85 imports no new zero-free or prime-number theorem.  Its literature audit
uses the primary Kloosterman-fraction estimates already listed above and
checks their exact subtraction.  Their natural zero-frequency term is the
Ramanujan mean.  They control the mean-zero inverse-phase component, not the
canonical prime-derived `gamma` carrier.  The affine Ward, reciprocal
derivative-transfer, top-prime null-gauge, and square-root defect identities
are project derivations; the finite complex-phase checks are diagnostics.

R86 additionally checks Drappeau's signed low-character dispersion theorem,
the Fouvry--Radziwill unbalanced architecture, balanced Kloosterman
trace-function bounds, and the level/spectral reciprocity formulas of
Andersen--Kiral, Blomer--Khan, Wu, and Yang.  None contains the finite
canonical `Lambda-1` dual.  Differentiating the Eisenstein parameter produces
log-weighted divisor coefficients; `-zeta'/zeta` appears only in scalar
normalization and degenerate residue terms, where differentiation increases
zero-pole order.  The shifted-Ramanujan, compression, zero-orbit, averaging,
and prime-point conclusions are project derivations; their finite matrix
checks are diagnostics.

R94--R98 additionally import the classical Mertens/zero-free-half-plane
equivalence, Kronecker recurrence, Landau's one-sided Laplace theorem,
Dirichlet-series `H^2`/Bohr-lift theory, and Carlson's interior mean theorem
with its boundedness hypotheses.  None identifies natural integer ordering
with Euler ordering at the exceptional unit character below `Re(s)=1`.
Hedenmalm--Lindqvist--Seip and Saksman--Seip supply the relevant functional-
analytic boundary; the conditional-tail and Euler boundary-layer formulas
are project derivations.  Claimed fixed-strip or `quasi-RH => RH` preprints
are not imported merely from their titles: Azevedo and Burton are withdrawn,
and the exact Puglisi v9 audit finds a false alternating-exponential estimate
in its final parameter regime.  Details and source links are in
[`RECIPROCAL-AND-BILINEAR-LITERATURE-2026-08.md`](RECIPROCAL-AND-BILINEAR-LITERATURE-2026-08.md)
and the R95--R98 gate reports.  R97 also uses standard Schatten regularized
determinants and Landau/pretentious Euler-product arguments.  R98 imports the
classical Turan--Pintz--Allison converse theory, Ingham--Huxley and current
Guth--Maynard zero density, Deuring--Heilbronn hypotheses, and the standard
mollifier distinction between pointwise reciprocal approximation and
aggregate zero detection.  Those inputs supply no strict conditional map
`f(Theta)<Theta`; that identity-map conclusion is the audited composition,
not a claim that no different quasi-RH bootstrap can exist.

No exact predecessor was found for the repository's fixed-step
Euler-to-frozen-center normalization.  That supports only the classification
“classical-synthesis corollary not located verbatim,” not a novelty claim.
No surveyed source states the complete every-block fixed-power R71 estimate;
this is a search result and normalization audit, not proof that no
mathematically equivalent formulation exists anywhere in the literature.
