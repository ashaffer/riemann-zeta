# Coefficient-sensitive radialization literature passport

**Date:** 2026-08-31

**Literature checked through:** 2026-08-31

**Status:** primary-source theorem import, scale audit, and route reframe.

**Headline nonclaim:** this report proves neither a uniform zero-free strip,
`LTRAD_P(.0189,.001)`, `PWCT(.0179,.001)`, `CA4(163/1000,1/10)`, nor the
sharp four-cycle bound.

## 0. Executive verdict

The survey changes the description of the missing mathematics more than it
changes the list of proved estimates.

1. Classical large-sieve and frame theory already gives the natural
   blockwise `L^2` control once genuinely unresolved reflected frequencies
   are clustered.  Therefore the missing radialization theorem should not be
   described merely as a stronger vector-valued large sieve.  It must include
   the features that those theorems omit: a one-sided dip, an adaptive
   coefficient vector chosen after the source event, preservation of the
   source equality, and a return before the finite horizon.

2. Over an unbounded height range, finite prime-log phase control is
   qualitatively easy: unique factorization makes the logarithms of distinct
   primes rationally independent, and Kronecker--Weyl gives a dense torus
   orbit.  The hard problem is a **quantitative hitting theorem for a growing-
   dimensional prime-log flow before**

   ```text
   B=Y^(50/33).
   ```

   This is a finite-time arithmetic-mixing problem, not a static convex-hull
   problem.

3. Approximate Caratheodory, discrepancy, empirical-process, and generic
   sampling theorems incur square-root accuracy.  At the project's absolute
   radial scale `Y^(-.0189)`, soft sampling needs about `Y^.0378` atoms, while
   the current participation mechanism can afford only the `Y^.0179`--
   `Y^.0189` scale.  This factor-of-two exponent mismatch is intrinsic to that
   proof class, not a missing constant.

4. The August 2026 additive-energy papers are important possible
   **terminators after serialization**, but they are not serialization
   theorems.  Jing--Wu controls exact unweighted four-fold energy on algebraic
   surfaces; Cushman--Demeter--Wu controls exact unweighted six-fold energy on
   strictly convex curves; Hu converts hereditary exact energy into genuinely
   weighted `L^4`/Young estimates.  None controls prescribed `B^(-1)` near
   relations, a translated finite-height kernel, the four project masks, or
   the source-conditioned one-sided sign.

5. The actual-prime input that could cross the remaining gap must therefore
   look like one of the following:

   - source-conditioned quantitative Bohr/Kronecker return for the actual
     growing prime shell;
   - signed, gap-weighted semiprime product covariance at physical resolution
     `H=Y^2/T`, uniformly over the whole CA4 aperture;
   - a resolution-stable Freiman/jet transport of the actual prime object to a
     bounded-complexity algebraic variety, followed by one of the new exact
     energy theorems.

The first two contain actual-prime arithmetic.  The last route contains it
entirely in the transport theorem; the downstream algebraic-energy theorem is
soft geometry.

## 1. Preflight and theorem passports

### 1.1 Routing state

This audit uses
[`ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`](ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md)
and
[`zeta23_research_preflight_v1.json`](context/zeta23_research_preflight_v1.json)
as the current state.

The Weil and QP/Turan architectures remain separate.  The durable statuses
remain:

```text
RH                                                   OPEN
uniform zero-free strip                              OPEN
DPA_P(.019)                                          OPEN
LTRAD_P(.0189,.001)                                  OPEN
PWCT(.0179,.001)                                     OPEN
CA4(163/1000,1/10)                                  OPEN
sharp four-cycle bound                               OPEN
```

### 1.2 Radialization passport

For each legal source event at `t0`, with source depth

```text
D >= Y^(-.001),
```

the prime-only LTRAD gate asks, schematically, that for **every** legal signed
adaptive dual vector `y` satisfying the source normalization `y . v=-1`, one
can find a height

```text
t in H_Y=[Y^.01,Y^(50/33)]
```

for which

```text
y . a_P(t) >= Y^(-.0179+o(1)).
```

Together with the source depth this yields the radial exponent `.0189`.  A
valid import must preserve:

| Field | Required value |
|---|---|
| mask/node | actual prime carrier/corrector object |
| source | the same legal source event at `t0` |
| coefficients | signed, adaptive, source-normalized dual cone |
| normalization | literal `y.v=-1`, including the depth floor |
| window | the full prescribed `H_Y`, not an unbounded or selected sequence |
| quantifiers | event first, arbitrary legal `y` next, witness `t` last |
| resolution | reflected clusters at the finite-band scale `B^(-1)` |
| rate | absolute `Y^(-.0179)` and radial `Y^(-.0189)` exponents |
| adapter | the proved strip adapter, with corrector loss retained |

For the positive-carrier subclass `PWCT`, a probability vector `alpha>=0`
has source surplus and worst future dip

```text
A(alpha)=D+Phi_alpha(t0)>0,
a(alpha)=-inf_(t in H_Y) Phi_alpha(t),
```

and the target is

```text
a(alpha)/A(alpha) >= Y^(-.0179+o(1)).
```

The abstract, Fejer, prime-density pseudo-node, and finite-evidence
falsifiers remain licensed only against proof classes that do not use more
actual-prime arithmetic than those models preserve.

### 1.3 CA4 and four-cycle passport

The current centered semiprime gate is

```text
CA4(163/1000,1/10):
integral_T^(2T) |R_Y(t)|^4 dt
    <= T Y^(-2q+1/10+o(1)),
q=2787/3250,
Y^(1049/1250) <= T <= Y^(50/33),
```

over the remaining high aperture.  After expansion its exact kernel form is

```text
T sum_(m,n) a_m a_n K(T log(m/n)).
```

The diagonal `m=n` is governed by unique factorization and is affordable.
The open term is a **signed, translated, gap-weighted four-distinct
covariance** at product resolution

```text
H=Y^2/T,
```

down to `Y^(16/33)`.  An exact additive-energy theorem sees only the atom
`m=n`; it does not see the prescribed near-diagonal kernel.

The sharp four-cycle and jet/affine-compression routes have still stricter
passports: four masks, arbitrary coefficients or the exact scoped coefficient
cone, literal normalization, `B^(-1)` label resolution, and collective rather
than rootwise reconstruction.  `CA4` has fixed positive adjacent-gap weights
and is neither the arbitrary-coefficient four-cycle theorem nor a direct
radialization theorem.

## 2. Fast passport matrix

`Yes` in the final column means that an input uses arithmetic not reproduced
by generic pseudo-nodes.  It does not mean that the input is sufficient.

| Imported result | Exact output | Main failed passport fields | Actual-prime input? |
|---|---|---|---|
| Montgomery--Vaughan Hilbert/large sieve | separated-frequency `L^2` Gram bound | one-sided sign, source, adaptivity, finite return | No |
| BSS/MSS/restricted invertibility | spectral sparsification or a well-conditioned subset | source equality, full floor, sign, labels | No |
| Banaszczyk/Spencer/Bansal--Jiang | a signing with small discrepancy | direction is opposite; no forced dip or source | No |
| approximate Caratheodory | sparse convex approximation with `O(eps^-2)` support | loses a factor two in the required exponent | No |
| chaining/small-ball methods | stochastic supremum or lower-tail bounds | require randomness/small-ball input; wrong absolute scale | No |
| inverse Littlewood--Offord | random concentration implies GAP structure | no Rademacher concentration supplied; source and metric labels lost | No |
| BSG/PFR/Bogolyubov--Ruzsa | exact high energy implies additive structure | exact rather than `B^-1` relations; no masks/source | No |
| Tchakaloff/weighted least squares | exact finite moments or stable random sampling | finite function space; two-sided; no one-sided orbit hit | No |
| fixed-dimensional Kronecker--Weyl | eventual phase approximation | no quantitative growing-dimensional hitting time | prime independence only |
| zeta universality/random Euler models | fixed target or restricted-cutoff distributional comparison | wrong dimension/cutoff; RH-circular in strongest short form | Sometimes, at wrong scale |
| Jing--Wu 2026 | exact unweighted `E(X)` on an algebraic surface | no serialization, weights, metric resolution, source, masks | No |
| Cushman--Demeter--Wu 2026 | exact unweighted `J_3` on a convex curve | six-fold rather than CA4; no prescribed thickening scale | No |
| Hu 2026 | hereditary exact energy and weighted `L^4`/Young | full-dual exact equality, not finite-window signed covariance | No |

## 3. Large sieve, frames, and restricted invertibility

### LIT-R1 -- Montgomery--Vaughan generalized Hilbert inequality (`IMPORTED`)

Montgomery and Vaughan's
[Hilbert inequality](https://doi.org/10.1112/jlms/s2-8.1.73) implies the
standard almost-periodic mean-value estimate: if the real frequencies
`lambda_j` have separation at least `delta`, then

```text
integral_I |sum_j c_j exp(i lambda_j t)|^2 dt
  = |I| sum_j |c_j|^2 + O(delta^(-1) sum_j |c_j|^2).
```

Coordinatewise integration gives the identical bound for Hilbert-space-valued
`c_j`.  Thus the usual scalar large sieve already tensorizes, but acquires no
one-sided conclusion by doing so.

At the project horizon `B=Y^(50/33)`, same-side prime-log frequency spacing is
of order `Y^(-1)`, so the normalized off-diagonal error after true separation
is of order

```text
(B/Y)^(-1)=Y^(-17/33).
```

Near-reflected pairs can be closer than `B^(-1)` and have to be treated as
small blocks.  This supports a useful decomposition:

```text
unresolved reflection blocks  +  separated block Gram matrix.
```

It does **not** prove the project's carrier theorem, because enlarging the
existing fusion threshold would itself change the mask and source passport.
More importantly, an `L^2` norm lower bound says that a function is large in
absolute value somewhere; it does not give the required sign at a height
chosen after the source-conditioned coefficient vector.

### LIT-R2 -- spectral sparsification (`IMPORTED`, wrong interface)

The [Batson--Spielman--Srivastava theorem](https://arxiv.org/abs/0808.0163)
says, in one standard form, that if

```text
sum_i v_i v_i^* = I_n,
```

then for every `d>1` there are nonnegative weights supported on at most
`ceil(dn)` indices such that

```text
(1-d^(-1/2))^2 I_n
 <= sum_i s_i v_i v_i^*
 <= (1+d^(-1/2))^2 I_n.
```

[Spielman--Srivastava restricted invertibility](https://arxiv.org/abs/0911.1114)
extracts a subset of size proportional to stable rank on which an operator
has a quantitative lower singular value.  The
[Marcus--Spielman--Srivastava solution of Kadison--Singer](https://arxiv.org/abs/1306.3969)
partitions an isotropic frame with small vector norms into pieces with spectral
control.

These are covariance-preservation theorems.  They may sparsify a discretized
height Gram matrix, but they do not preserve the affine source equality
`y.v=-1`, the exact coefficient cone, the full-band floor, or prime labels.
They also give symmetric spectral information rather than a signed return.

### LIT-R3 -- near-critical exponential frames (`IMPORTED`, selection reversed)

[Bownik--van Velthoven](https://arxiv.org/abs/2411.19562), Adv. Math. 467
(2025), prove that for a compact spectrum `Omega` and `eps>0` one can choose a
frequency set `Lambda` of uniform density at most `(1+eps)|Omega|` whose
exponentials form a frame for `L^2(Omega)`, with frame bounds depending only on
`eps`.

The theorem selects a sampling frequency set after seeing `Omega`.  In LTRAD
the prime frequencies and height window are fixed, while the adversarial dual
coefficient is selected after the source event.  The quantifier direction is
therefore reversed, and the conclusion is again two-sided `L^2`.

**Import decision.**  Use `R1` as the routine off-block estimate in any future
cluster proof.  Do not open a research branch for a stronger ordinary frame
theorem unless its statement explicitly contains the source, sign, and
adaptive quantifiers.

## 4. Discrepancy and convex approximation

### LIT-R4 -- discrepancy theorems (`IMPORTED`, polarity mismatch)

[Banaszczyk](https://doi.org/10.1002/(SICI)1098-2418(199807)12:4%3C351::AID-RSA3%3E3.0.CO;2-S)
shows that vectors of sufficiently small Euclidean norm can be signed so that
their sum lies in a constant dilation of any symmetric convex body of Gaussian
measure at least `1/2`.  Spencer's
[six-standard-deviations theorem](https://doi.org/10.2307/2000258) gives
`O(sqrt(n))` discrepancy for `n` sets on `n` points.  The
[Gram--Schmidt walk](https://arxiv.org/abs/1708.01079) makes Banaszczyk-type
coloring algorithmic.

The newer [Bansal--Jiang affine spectral-independence method](https://arxiv.org/abs/2508.03961)
resolves Beck--Fiala for `k >= log^2 n` up to the stated regimes and improves
the general Komlos bound to polylogarithmic order
`~O(log^(1/4)n)`.  Here “affine” names constraints inside their rounding SDP;
it does not mean that an arbitrary project source equality is preserved.

All these theorems construct a signing with **small** row discrepancies.  The
LTRAD problem asks to prove that every legal source-normalized signing incurs
a sufficiently large excursion of a prescribed sign.  Better discrepancy can
therefore strengthen a hostile construction rather than prove radialization.

### LIT-R5 -- approximate Caratheodory and the factor-two wall (`IMPORTED` + `DERIVED`)

[Barman's approximate Caratheodory theorem](https://arxiv.org/abs/1406.2296)
gives an `ell_p` approximation, `p>=2`, to a point in a convex hull using
`O(p/eps^2)` atoms.  Taking `p` of logarithmic size gives the familiar
`O(log m/eps^2)` support for `ell_infinity` approximation on `m` coordinates.
[Mirrokni et al.](https://proceedings.mlr.press/v70/mirrokni17a/mirrokni17a.pdf)
give matching lower bounds, up to constants in the relevant regimes.

For PWCT the worst allowed source scale is

```text
A >= D >= Y^(-.001),
```

and a relative return `Y^(-.0179)` therefore requires absolute accuracy at
least

```text
eps_abs = Y^(-.0189).
```

Generic convex sampling consequently needs

```text
eps_abs^(-2)=Y^.0378
```

atoms, up to logarithms.  The current participation mechanism operates only
at the `Y^.0179`--`Y^.0189` scale.  Thus carrierize-then-sample loses almost a
factor two in the exponent before any arithmetic loss is paid.

This does not refute an actual-prime compression theorem.  It refutes the
claim that dimension-free soft convex approximation by itself supplies the
required compression.

## 5. Empirical processes, chaining, and small-ball methods

### LIT-R6 -- generic chaining and chaos (`IMPORTED`, conditional input missing)

[Dirksen's generic-chaining tail bounds](https://arxiv.org/abs/1309.3522)
control suprema of processes with subgaussian/subexponential increments.
[Krahmer--Mendelson--Rauhut](https://arxiv.org/abs/1207.0235) control suprema
of chaos processes and derive RIP bounds for structured random matrices.
[Mendelson's small-ball method](https://arxiv.org/abs/1401.0304) replaces
concentration by a uniform lower bound on the chance that a linear form is not
too small.

To apply these tools here one must first produce a probability distribution on
the deterministic height orbit for which every legal adaptive coefficient
vector has a uniform small-ball probability, with the required sign or enough
symmetry to recover it.  That hypothesis is already a quantitative orbit
anti-concentration theorem and is essentially the missing input.

There is also a scale obstruction.  For a diffuse probability carrier with
roughly `Y` coefficients, independent-phase `L^2` size is approximately

```text
||alpha||_2 ~ Y^(-1/2),
```

far below the absolute PWCT target near `Y^(-.0189)`.  A random-phase or
generic small-ball theorem predicts the pseudo-node scale, not the enormous
source-conditioned return demanded by PWCT.  Any successful theorem must
explain a special arithmetic resonance with the source.

**Falsifier map.**  These are soft geometry/probability results.  The smooth
pseudo-prime model and center-density hostile model are licensed against any
proposed proof using only their hypotheses.

## 6. Inverse Littlewood--Offord and additive structure

### LIT-R7 -- inverse Littlewood--Offord (`IMPORTED`, wrong antecedent)

The [Tao--Vu inverse Littlewood--Offord theorem](https://annals.math.princeton.edu/2009/169-2/p06)
and the [Nguyen--Vu optimal inverse theory](https://arxiv.org/abs/1004.3967)
say, roughly, that polynomially large concentration of a random signed sum
forces most coefficients into a low-rank generalized arithmetic progression,
with quantitative size control.

LTRAD gives no Rademacher concentration law.  Replacing the one-parameter
height orbit by independent signs is exactly the unproved growing-dimensional
equidistribution step.  Even after such a replacement, the inverse conclusion
would concern most coefficients, while the project needs the literal source
coordinate, reflected labels at `B^(-1)` resolution, and the whole signed
normalization.

### LIT-R8 -- energy-to-structure theorems (`IMPORTED`, exact/metric mismatch)

The strengthened Balog--Szemeredi--Gowers theorem of
[Reiher--Schoen](https://arxiv.org/abs/2308.10245) gives a large subset with
small difference set from high exact additive energy.  Sanders'
[Bogolyubov--Ruzsa lemma](https://arxiv.org/abs/1011.0107) places a large
structured progression/coset progression inside iterated sumsets under small
doubling hypotheses.  The polynomial Freiman--Ruzsa/Marton advances of
[Gowers--Green--Manners--Tao](https://arxiv.org/abs/2311.05762) and their
[bounded-torsion extension](https://arxiv.org/abs/2404.02244) are powerful
exact-group inverse theorems.

These inputs are useful **after** one has shown high exact energy in a
faithful group model.  The project objects instead carry metric near-relations
at a prescribed scale, four masks or gap weights, and a source label.
Thresholding or dyadic decomposition can destroy all three.  Prime logs are
rationally independent, so exact additive relations among single prime logs
are deliberately sparse; the difficult relations arise only after products,
jets, or finite-resolution projection.

An inverse theorem can therefore be a middle step, not the missing first
step.  The first step must preserve the `B^(-1)` metric relation and label
dependencies.

## 7. Quadrature, sampling, and leverage weights

### LIT-R9 -- Tchakaloff (`IMPORTED`, finite test space only)

The Bayer--Teichmann proof of
[Tchakaloff's theorem](https://arxiv.org/abs/math/0502473) shows that finitely
many moments of a positive measure can be represented exactly by a positive
cubature formula with at most the dimension of the moment space many nodes.

This can preserve a finite list of source and grid moments exactly, but its
support grows with that list.  Uniform control over a height continuum at
`B^(-1)` resolution has a growing metric entropy.  Tchakaloff supplies no
dimension-free support bound, no one-sided floor, and no preference for
actual-prime labels.

### LIT-R10 -- Christoffel/leverage sampling (`IMPORTED`, explains a falsifier)

[Cohen--Migliorati](https://arxiv.org/abs/1608.00512) obtain stable weighted
least-squares approximation by sampling from an optimal measure governed by a
Christoffel/leverage function and applying reciprocal weights; the sample
complexity is essentially `m log m` for an `m`-dimensional space.  Related
adaptive variants include [Cohen--Dolbeault](https://arxiv.org/abs/2010.11040).

This literature explains, rather than defeats, the center-density hostile
falsifier.  Reciprocal density/leverage weights are designed precisely to
compensate for nonuniform sampling density.  Hence local center abundance can
be erased by legal inverse-density weighting unless the arithmetic source
restricts that weighting.

[Temlyakov's Marcinkiewicz discretization results](https://arxiv.org/abs/1703.03743)
likewise discretize two-sided norms on finite-dimensional spaces using entropy
and chaining.  They do not produce a prescribed one-sided orbit excursion.

## 8. Universality and random Euler products

### LIT-R11 -- qualitative prime-phase controllability (`DERIVED`)

For a fixed finite set of distinct primes, unique factorization implies

```text
sum_p n_p log p=0, n_p in Z  =>  n_p=0 for every p.
```

Kronecker--Weyl therefore makes

```text
t -> (t log p / 2pi)_p
```

dense in the finite torus.  Given a fixed carrier and any prescribed prime
phase pattern, some unbounded height approximates it.  In particular, the
infinite-horizon convex-hull problem has much stronger qualitative solutions
than PWCT asks for.

The missing number is the hitting time.  General Diophantine bounds deteriorate
exponentially with the torus dimension, while the prime shell has dimension
about `Y/log Y` and the allowed horizon is only polynomial in `Y`.  This is the
precise place where qualitative universality stops.

### LIT-R12 -- short-interval universality (`IMPORTED`, fixed dimension/circularity)

[Lee--Pankowski](https://arxiv.org/abs/2502.15364) prove a short-interval
universality result: under RH they reach intervals of logarithmic length;
unconditionally they obtain a positive-upper-density form on such intervals.
The phase approximation in the proof first fixes a finite prime set and then
uses Kronecker--Weyl.  It is not uniform when the number of controlled primes
grows like `Y/log Y`.  Moreover, importing the strongest short-interval result
into an attempted proof of a zero-free strip would import RH itself.

Effective and hybrid universality results have the same passport issue: a
fixed analytic target on a fixed compact region is not an adaptive legal dual
vector over a growing prime shell.

The [Pecherskii rearrangement theorem](https://www.mathnet.ru/eng/im1797),
which underlies several universality constructions, similarly turns
divergence in every Hilbert-space direction plus square summability into a
qualitative density statement for an infinite unimodular series.  It supplies
neither a finite partial-sum length nor a polynomial hitting-time bound, and
it has no distinguished source coordinate.  It therefore reinforces the
same dividing line: qualitative phase flexibility is available, quantitative
growing-dimensional return is not.

### LIT-R13 -- random Euler comparison (`IMPORTED`, scale fails literally)

[Lamzouri--Lester--Radziwill](https://arxiv.org/abs/1402.6682) compare the
distribution of zeta with a random Euler-product model.  A reusable input in
their proof, Lemma 3.2, bounds the `2k`-th moment of a prime polynomial over
`[T,2T]` when

```text
k <= log T / (3 log z).
```

At the project scale `z~Y` and even at the top height
`T=Y^(50/33)`, the right side is

```text
50/99 < 1.
```

Thus this moment range does not license even the first positive integer
moment parameter needed for a shell-level fourth-moment comparison.  Random
Euler products remain a useful null model, but not an imported theorem at the
project's prime/height scale.

This calculation also clarifies the pseudo-node evidence: independent prime
phases naturally live at square-root amplitude.  PWCT, if true, is not generic
random-Euler anti-concentration; it is a strong source-conditioned actual-
prime resonance.

## 9. August 2026 algebraic-energy papers

All three items below are arXiv preprints as of the audit date.  The statements
are imported as claims proved in the cited manuscripts, not as independently
peer-reviewed project theorems.

### LIT-R14 -- Jing--Wu surface energy (`IMPORTED`)

[Jing--Wu, arXiv:2608.14467v2](https://arxiv.org/abs/2608.14467) prove that if
`F:R^3->R` is irreducible of degree at least two and

```text
Lambda_F(X)=max(1, sup_(affine lines ell in Z(F)) |X intersect ell|),
```

then every finite `X subset Z(F)` satisfies

```text
E(X) <= C_(deg F,eps) Lambda_F(X) |X|^(2+eps).
```

This is a sharp near-diagonal theorem for **exact, unweighted** four-fold
relations `a+b=c+d`.  It has no scale parameter and no finite-height kernel.

#### Passport against project gates

| Gate | Result |
|---|---|
| approximate four-cycle | Fails: project near-relations are at `B^-1`, masked, and coefficient-sensitive. |
| jet/A2 serialization | Conditional terminator only: one must first map jets to a bounded-degree surface with relation fidelity and control `Lambda_F`. |
| CA4 | Fails: exact equality counts the UFD diagonal but not `K(T log(m/n))` near covariance. |
| adaptive convex hull/PWCT | Fails: no source, one-sided sign, orbit window, or adaptive coefficients. |

Even if a hereditary application plus dyadic decomposition supplies weights,
it would still live on exact relations.  The essential missing hypothesis is a
resolution-stable serialization, not merely a weighted extension.

### LIT-R15 -- Cushman--Demeter--Wu convex-curve energy (`IMPORTED`)

[Cushman--Demeter--Wu, arXiv:2608.12316v3](https://arxiv.org/abs/2608.12316)
prove, for every finite `X subset R` and every strictly convex graph
`gamma(t)=(t,f(t))`,

```text
J_3(gamma(X))
 = #{x_1,...,x_6: sum_(i<=3) gamma(x_i)=sum_(i>3) gamma(x_i)}
 <= C_eps |X|^(3+eps),
```

with a constant independent of the curve and its point spacing.

The spacing independence is not a metric near-relation theorem.  Their
“admissible thickening” chooses a positive thickness depending on the finite
set so small that neighborhoods of unequal triple sums remain disjoint.  The
paper explicitly allows this thickness to depend on `gamma(X)`.  It supplies
no lower bound comparable to the prescribed project resolution `B^(-1)`.

#### Passport against project gates

| Gate | Result |
|---|---|
| approximate four-cycle | Fails: six-fold exact equality and no four masks or arbitrary weights. |
| jet serialization | Potential terminator only after a `B^-1`-faithful convex jet embedding. |
| CA4 | Fails: wrong moment (`L^6`, not the signed weighted `L^4` kernel) and no translated aperture. |
| adaptive convex hull/PWCT | Fails completely: no source or one-sided phase return. |

The paper's real relevance is conceptual: order/interlacing can replace
quantitative curvature for exact equalities.  A future packet proof should
test whether a bounded number of monotone jet leaves exists, but must budget
the cost of globalization and preserve metric labels.

### LIT-R16 -- Hu weighted algebraic energy (`IMPORTED`, closest downstream match)

[Hu, arXiv:2608.18956v1](https://arxiv.org/abs/2608.18956) defines, for an
admissible irreducible `m`-dimensional bounded-degree variety `V`,

```text
sigma(V)=2m-dim Zar(V-V),
alpha(V)=max(2,1+2 sigma(V)/m),
```

and a hereditary translation-partition flag parameter `Lambda_(a,R)`.  For
`alpha(V)<=a<3`, the paper proves

```text
E(X) <= C Lambda_(a,R)(X;V)^(3-a) |X|^(a+eps).
```

For the quadratic codimension-two threefold

```text
Sigma={(u,Q_1(u),Q_2(u)):u in R^3} subset R^5,
```

with `Q_1` positive definite and simple generalized spectrum, it proves

```text
E(X) <= C_eps |X|^(2+eps).
```

Most importantly for the coefficient audit, the paper does **not** stop at
unweighted energy.  A hereditary estimate

```text
E(A) <= K^(3-a) |A|^(a+o(1))  for every A subset X
```

implies the weighted restriction estimate

```text
||f_hat||_4
 <= K^((3-a)/4) |X|^o(1) ||f||_(ell^(4/a)),
supp(f) subset X.
```

At `a=2` this is an arbitrary complex-weight `ell^2 -> L^4` bound on the
compact dual of the exact torsion-free group generated by `X`.  Hu also gives
off-diagonal Young inequalities in the sharp region `p,q<=2`,
`1/p+1/q>=1`.

This is the strongest apparent match in the new literature, but the passport
still fails at the decisive place:

- the `L^4` integral is Haar measure on the **full dual** and counts exact
  additive equality;
- the project's integral is on a translated finite interval and weights a
  continuum of `B^(-1)` near equalities by a signed kernel;
- the admissible-thickening device in Hu's Section 6 is chosen after the
  finite set to avoid every nonzero triple-sum relation; no uniform lower
  bound at the requested resolution is supplied;
- the theorem has no four masks, source event, adaptive quantifier, or
  one-sided floor.

#### Exact-unweighted versus signed-weighted verdict

```text
Jing--Wu: exact + unweighted + L4 energy
CDW:      exact + unweighted + L6 energy
Hu:       exact + arbitrary complex weights + L4/Young
CA4:      approximate at prescribed resolution + fixed arithmetic weights
          + signed translated kernel + finite aperture
FC:       approximate at prescribed resolution + four masks
          + coefficient-sensitive collective reconstruction
LTRAD:    adaptive coefficients + source-conditioned one-sided orbit hit
```

Thus it would be incorrect to dismiss Hu as “only unweighted.”  It would be
equally incorrect to treat its weighted theorem as CA4: weighting exact Haar
energy is not resolution-sensitive signed finite-window control.

Hu also extends the CDW theorem to point sets of turning complexity `kappa`:

```text
J_3(P) <= C_eps kappa(P)^2 |P|^(3+eps),
```

and gives matching examples.  The sharp `kappa^2` tax is a warning that a
many-leaf jet partition can erase the desired exponent even after every leaf
is geometrically favorable.

## 10. Pseudo-node falsifier audit

### 10.1 What the synthetic models now rule out

The literature validates the following hostile conclusions.

1. **Covariance alone is insufficient.**  Frame bounds, BSS sparsification,
   restricted invertibility, and generic chaining are shared by soft models.
   They cannot distinguish the actual prime shell from a pseudo-node model
   with the same Gram data.

2. **Density alone is insufficient.**  Christoffel/leverage sampling explains
   how inverse-density weights cancel center-density advantages.  Any center-
   abundance proof must restrict the legal coefficient cone using arithmetic
   source information.

3. **Exact energy alone is insufficient.**  A model may have excellent exact
   additive energy while retaining many relations at a prescribed nonzero
   resolution.  The new algebraic-energy theorems do not invalidate this
   falsifier because their thickening scale is set-dependent.

4. **Random-phase anti-concentration is insufficient.**  Its natural scale is
   `Y^(-1/2)`, while the project needs a source-conditioned return close to
   `Y^(-.0189)`.

5. **Sparse convex approximation alone is insufficient.**  The optimal
   square-root law yields the literal `.0378` support exponent.

### 10.2 What the synthetic models do not rule out

They do not refute a theorem using any of the following genuinely arithmetic
features at their full fidelity:

- the exact adjacent-prime source relation and its induced coefficient
  restrictions;
- multiplication and unique factorization after the semiprime lift;
- the actual distribution of prime products in windows of width `Y^2/T`;
- a prime-specific Diophantine lower bound for low-complexity simultaneous
  phase relations;
- cancellation of the signed translated kernel coupled to actual gap weights.

These are legitimate escape hypotheses.  Merely naming “primes” while using
only their density, separation, or rational independence is not.

### 10.3 Arithmetic-fidelity hierarchy

| Hypothesis actually used | Classification | Escapes current pseudo-node falsifiers? |
|---|---|---|
| norm, covariance, isotropy, entropy, convexity, bounded algebraic degree | soft geometry | No |
| prime-shell density or average spacing | arithmetic statistic but explicitly mimicked | No |
| rational independence of finitely many prime logs | genuine prime fact, but a generic dissociated set can mimic it | No |
| unique factorization for the exact semiprime diagonal | genuine arithmetic and already useful | Not by itself; a Sidon model mimics the diagonal |
| actual adjacent-gap weights tied to the same source event | source-level actual-prime arithmetic | Potentially |
| signed correlations of actual prime products in every moving window of width `Y^2/T` | metric actual-prime arithmetic at target fidelity | Yes |
| a quantitative growing-shell phase-return theorem with explicit polynomial horizon | Diophantine actual-prime arithmetic at target fidelity | Yes |

This table separates “true because the nodes are primes” from “strong enough
to distinguish the nodes from the licensed synthetic models.”  Only the last
three rows can currently invalidate those falsifiers.

## 11. Reframed research program

### 11.1 Radialization: make the source arithmetic explicit

The next useful theorem should be stated as a source-conditioned quantitative
return theorem, not as a generic large sieve.  A falsifiable prototype is:

```text
SCQKR(beta):
for every actual legal source event and every legal source-normalized
adaptive carrier/corrector coefficient, the actual prime-log flow has,
before B=Y^(50/33), a return into a one-sided target set of radius
Y^(-beta), with beta <= .0179 after adapter losses.
```

Before attempting a proof, identify the arithmetic restriction on the legal
coefficient vector that is absent from the prime-density pseudo-node model.
Without such a restriction, the hostile models predict failure.

### 11.2 CA4: attack the metric covariance, not the exact diagonal

The new algebraic-energy literature can help only after a transport lemma of
the following kind:

```text
RST(beta):
map the actual weighted semiprime/jet atoms into O(Y^o(1)) bounded-degree
variety leaves so that every product relation with
|log(m/n)| <= 1/T is preserved, false relations are controlled,
the adjacent-gap weights and signs remain attached, and the total leaf
complexity costs less than the CA4 1/10 budget.
```

If `RST` lands on Hu's quadratic threefold with simple spectrum, Hu supplies
a powerful weighted exact terminator on each leaf.  If it lands on a strictly
convex curve, CDW supplies an exact six-fold terminator, but an additional
moment-conversion step is required.  Jing--Wu is useful when a genuine surface
serialization and line-occupancy bound emerge.

The fast falsifier is to construct two semiprime configurations with the same
exact serialized relations but different `B^(-1)` covariance.  If this is
possible under the proposed map, the map is not resolution-stable and the
literature theorem cannot close CA4.

### 11.3 Four-cycle: retain masks and collective weights from the start

Any application of BSG, surface energy, or frame sparsification must be written
on the four masked coefficient arrays before thresholding.  A valid theorem
must control a restricted-type or weighted form and reconstruct collectively;
an unweighted support count followed by a rootwise maximum repeats the known
failure.

### 11.4 Priority order after the survey

1. Extract the exact algebraic restrictions imposed on radial dual
   coefficients by an actual source event, and test whether the pseudo-node
   falsifiers can realize them.  This is the highest-information radial step.
2. For CA4, derive a local normal form for the signed near-product kernel and
   test a bounded-complexity Hu-threefold serialization at the literal
   `H=Y^2/T` scale.  Kill it immediately if the map is not bi-faithful at that
   resolution or if the leaf/turning tax exceeds `Y^.1`.
3. Use Montgomery--Vaughan only as the routine separated-block estimate; do
   not spend effort reproving soft `L^2` geometry.
4. Treat the August 2026 papers as downstream modules, not evidence that an
   approximate four-cycle or CA4 estimate has already been proved.

## 12. Source ledger

### Harmonic analysis and frames

- Montgomery--Vaughan,
  [“Hilbert's inequality”](https://doi.org/10.1112/jlms/s2-8.1.73), J. London
  Math. Soc. (1974).
- Montgomery--Vaughan,
  [“The large sieve”](https://doi.org/10.1112/S0025579300004708), Mathematika
  (1973).
- Batson--Spielman--Srivastava,
  [“Twice-Ramanujan sparsifiers”](https://arxiv.org/abs/0808.0163).
- Spielman--Srivastava,
  [“An elementary proof of the restricted invertibility theorem”](https://arxiv.org/abs/0911.1114).
- Marcus--Spielman--Srivastava,
  [“Interlacing families II”](https://arxiv.org/abs/1306.3969).
- Bownik--van Velthoven,
  [“On exponential frames near the critical density”](https://arxiv.org/abs/2411.19562).

### Discrepancy, sampling, and empirical processes

- Banaszczyk,
  [“Balancing vectors and Gaussian measures of n-dimensional convex bodies”](https://doi.org/10.1002/(SICI)1098-2418(199807)12:4%3C351::AID-RSA3%3E3.0.CO;2-S).
- Spencer,
  [“Six standard deviations suffice”](https://doi.org/10.2307/2000258).
- Bansal--Dadush--Garg--Lovett,
  [“The Gram--Schmidt walk”](https://arxiv.org/abs/1708.01079).
- Bansal--Jiang,
  [“Decoupling via affine spectral-independence”](https://arxiv.org/abs/2508.03961).
- Barman,
  [“Approximating Nash equilibria and dense subgraphs via an approximate version of Caratheodory's theorem”](https://arxiv.org/abs/1406.2296).
- Mirrokni et al.,
  [“Tight bounds for approximate Caratheodory and beyond”](https://proceedings.mlr.press/v70/mirrokni17a/mirrokni17a.pdf).
- Dirksen,
  [“Tail bounds via generic chaining”](https://arxiv.org/abs/1309.3522).
- Krahmer--Mendelson--Rauhut,
  [“Suprema of chaos processes and the RIP”](https://arxiv.org/abs/1207.0235).
- Mendelson,
  [“Learning without concentration”](https://arxiv.org/abs/1401.0304).
- Bayer--Teichmann,
  [“The proof of Tchakaloff's theorem”](https://arxiv.org/abs/math/0502473).
- Cohen--Migliorati,
  [“Optimal weighted least-squares methods”](https://arxiv.org/abs/1608.00512).
- Temlyakov,
  [“The Marcinkiewicz-type discretization theorems”](https://arxiv.org/abs/1703.03743).

### Inverse and additive combinatorics

- Tao--Vu,
  [“Inverse Littlewood--Offord theorems and the condition number of random discrete matrices”](https://annals.math.princeton.edu/2009/169-2/p06).
- Nguyen--Vu,
  [“Optimal inverse Littlewood--Offord theorems”](https://arxiv.org/abs/1004.3967).
- Reiher--Schoen,
  [“A note on the Balog--Szemeredi--Gowers theorem”](https://arxiv.org/abs/2308.10245).
- Sanders,
  [“On the Bogolyubov--Ruzsa lemma”](https://arxiv.org/abs/1011.0107).
- Gowers--Green--Manners--Tao,
  [“On a conjecture of Marton”](https://arxiv.org/abs/2311.05762) and the
  [bounded-torsion extension](https://arxiv.org/abs/2404.02244).

### Universality and new algebraic energy

- Lee--Pankowski,
  [“Universality of the zeta function in short intervals”](https://arxiv.org/abs/2502.15364).
- Pecherskii,
  [“Rearrangements of terms in functional series”](https://www.mathnet.ru/eng/im1797).
- Lamzouri--Lester--Radziwill,
  [“Discrepancy bounds for the distribution of the Riemann zeta-function and applications”](https://arxiv.org/abs/1402.6682).
- Jing--Wu,
  [“Near diagonal additive energy bound for points on algebraic surfaces”](https://arxiv.org/abs/2608.14467).
- Cushman--Demeter--Wu,
  [“Near optimal three-fold additive energy bound for points on convex curves”](https://arxiv.org/abs/2608.12316).
- Hu,
  [“Complexity-sensitive additive energy and off-diagonal Young inequalities on bounded-degree algebraic varieties”](https://arxiv.org/abs/2608.18956).

## 13. Final status update

No headline claim status changes.

The literature-level novelty, if the project succeeds, is now more sharply
located:

```text
not ordinary vector-valued L2,
not generic discrepancy or sparse convex approximation,
not exact unweighted additive energy,
not fixed-dimensional universality,

but either

(A) source-conditioned finite-time arithmetic phase return in growing
    dimension,

or

(B) resolution-stable signed weighted transport of actual semiprime/jet
    near-relations, followed by exact algebraic-energy machinery.
```

That distinction is the principal information gained by this survey.
