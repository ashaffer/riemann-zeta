# Anthropic Zeta23: result audit and integration map

Status: source and formal-artifact audit, 2026-08-11.  The audited external
artifact is tag `v1.0`, commit
`3635e74826a4c1fcece7d1cd2b6fa75e43a00510`.

This note records what the Anthropic/Claude result proves, what part of its
method can be reused here, and which conclusions it cannot support.  The
primary sources are the [full paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf),
the [official Lean repository](https://github.com/anthropics/zeta-23-lean),
and Anthropic's [research announcement](https://www.anthropic.com/research/riemann-zeta).
The five-page announcement note is not a substitute for the full paper: the
latter contains the simple-zero theorem, multiplicity bookkeeping, and the
optimized-window argument.

## 1. Exact theorem

For ordinates `T < gamma <= 2T`, let

- `N(T,2T)` count all nontrivial zeta zeros with multiplicity;
- `N0*(T,2T)` count distinct zero locations on `Re(s)=1/2`;
- `N0s(T,2T)` count simple zeros on `Re(s)=1/2`; and
- `Nd(T,2T)` count distinct zero locations in the critical strip.

The flat-window theorem gives

```text
liminf N0*/N >= 2/3,
liminf N0s/N >= 2/3,
liminf Nd/N  >= 5/6.
```

With the Montgomery--Taylor window, put

```text
C = 3/2 - (1/sqrt(2)) cot(1/sqrt(2))
  = 0.672500703679... .
```

The paper proves separately

```text
liminf N0*/N >= C,
liminf N0s/N >= C,
liminf Nd/N  >= (1+C)/2 = 0.836250351840... .
```

It also proves primitive Dirichlet-`L` analogues.  These are unconditional
positive-density results, not RH and not a zero-free strip.

In Lean the limits are stated in epsilon form: for each positive `epsilon`,
the corresponding `(constant-epsilon) * N <= count` inequality holds for all
sufficiently large `T`.  The exact trigonometric constant is formalized.  The
decimal evaluation and the strict numerical comparison `C > 2/3` are stated
in comments/documentation rather than proved by a certified numerical
enclosure.  Until that small enclosure is added, the kernel-checked claim
should be quoted using the exact constant.

## 2. Proof mechanism

The argument uses a compression of Weil's Hermitian form rather than
term-by-term positivity.

1. Choose a physical support length

   ```text
   L = lambda log(T/(2*pi))
   ```

   and form about `L*T/(2*pi)` modulated copies of one compactly supported
   window.  This is a finite Gabor family of dimension comparable with
   `N(T,2T)`.

2. On the zero side, an on-line zero contributes a positive rank-one atom.
   An off-line functional-equation pair contributes a hyperbolic block with
   signature `(1,1)`.  Tapering controls remote zeros.

3. A rank--trace/Frobenius inequality converts this block structure into a
   lower bound for the number of positive directions.  In the
   multiplicity-sensitive case the decisive schematic inequality is

   ```text
   r >= 2 tr(P) + 4 tr(Q) - 4 n_+(Q) - ||P+Q||_F^2.
   ```

4. The explicit formula and the prime-side second moment evaluate the first
   two matrix moments.  Optimizing the window gives the Montgomery--Taylor
   constant.

The unconditional pair-correlation input and prime-side architecture build
on [Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh](https://arxiv.org/abs/2306.04799)
and its [follow-up](https://arxiv.org/abs/2501.14545).  The genuinely new
step is the inertia/rank treatment of the off-line hyperbolic blocks: it
removes the earlier narrow-box hypothesis without pretending those blocks
are positive.

## 3. Formal audit performed here

The official artifact pins Lean `v4.33.0-rc2` and a newer Mathlib commit.  A
full 9,010-job rebuild was not duplicated on this memory-constrained host.
The repository's source and audit ledger were checked instead:

- no `axiom`, `opaque`, `unsafe`, `extern`, `native_decide`, or `sorry`
  occurs in the trusted `Zeta23` solution tree;
- the deliberate challenge-file holes are not imported by the solution;
- the top-level analytic input structure is instantiated by proved
  declarations, including the explicit formula, Riemann--von Mangoldt,
  gamma estimates, Chebyshev--Mertens, and Montgomery--Vaughan;
- the separate pair-ceiling experiment has an external enclosure hypothesis,
  but the `C` density theorem does not depend on it; and
- upstream records comparator and independent kernel replay, with the
  headline theorems depending only on Lean's standard logical axioms.

As a direct compatibility test, the seven-file `Zeta23/LinAlg` core together
with `ZeroSide/RankTraceMult.lean` and `ZeroSide/TightMult.lean` was compiled
verbatim against this project's already cached Lean/Mathlib `v4.32.1` stack,
single-threaded under a 4 GiB memory cap.  The key rank, inertia, Weyl,
counting, and tightness lemmas compiled successfully and `#print axioms`
reported only `propext`, `Classical.choice`, and `Quot.sound`.  A 2 GiB cap
was insufficient for the combined audit.  No project file or publication
certificate was changed by that test.

This is strong formal evidence, not an independent end-to-end reproduction
of the entire external package.

## 4. What can strengthen this repository

### 4.1 Replace the smooth explicit-formula axiom

The strongest direct integration is semantic, not numerical.
`Zeta23.WeilEF.EF_lit_zetaZeroConfig` is a source-proved smooth Weil explicit
formula.  After a convention adapter, it is a credible replacement for
`smooth_guinandWeil_formula` in
`RHBridge/GuinandWeilLiterature.lean`.

During this audit the adjacent Paley--Wiener declaration
`smooth_bilateralLaplace_entire` was already removed from the literature trust
base.  It is now a Lean theorem obtained by composing this project's
`CompactSupportFourierLaplace.differentiable_transform` with `z=i*s` and
identifying the interval and full-line integrals using compact support.  Its
focused axiom audit reports only Lean's standard logical axioms.  Thus the
remaining adapter target is the number-theoretic smooth formula itself, not
entirety of the test transform.

The convention map is exact:

```text
Zeta23 paperFT f z       = integral f(u) exp(i z u) du,
Zeta23 gammaOf rho       = (rho - 1/2)/i,
Zeta23 weilTest f f      = f convolved with conjugate-reflection(f).
```

For real smooth `phi`, take `f=phi`.  Then

```text
paperFT phi (gammaOf rho)
  = bilateralLaplace phi (rho - 1/2),
```

the second transform factor becomes this project's
`bilateralLaplace phi (1/2-rho)`, the pole terms coincide, the
archimedean terms agree after `r=2*pi*xi`, and the two values at
`+/- log(n)` produce the autocorrelation coefficient used here.

The adapter requires seven bounded lemmas:

1. equivalence of the zero carriers and reindexing of their symmetric sums;
2. agreement of analytic multiplicities;
3. `paperFT`/bilateral-Laplace normalization;
4. convolution/autocorrelation normalization;
5. pole-term normalization;
6. Fourier scaling in the archimedean integral; and
7. reduction of the prime `tsum` to this project's finite active-prime-power
   sum.

That port would give the certified `a=7/16` positivity theorem a fully formal
smooth zero-side interpretation.  It would not prove the low-regularity
`logarithmicDomain_guinandWeil_formula`, whose symmetric zero-disk limit is a
separate approximation and closure problem.

Zeta23's formal local zero count is also a plausible route to eliminate the
two project summability axioms in `ZetaZeroCountingLiterature.lean`.

### 4.2 Add a density/inertia branch

The approximately 1,962-line generic algebra subset is immediately portable
to the current toolchain.  Its useful declarations include Sylvester inertia
under pullback, von Neumann's trace inequality, the rank--trace inequality,
Weyl bounds, the multiplicity-aware count, and a sharpness example.

The correct use is a new, explicitly separate density branch:

```text
mixed Gabor compression
    -> on-line positive atoms + off-line hyperbolic blocks
    -> trace/Frobenius/inertia certificate
    -> density information.
```

This also gives a constructive escape from this repository's diagonal-packet
no-go theorem: mixed Gabor Gram entries retain the separated-box phase that
diagonal Fejer packets lose.  The escape produces a bulk count, not positivity
of the full form.

Vendoring should wait until the first application theorem is stated.  If
files are copied, Anthropic's Apache-2.0 headers and `NOTICE` attribution must
be preserved.  Keeping the full Zeta23 analytic package in its own pinned
toolchain avoids invalidating the current 27 GiB RHBridge artifact cache.

### 4.3 Reframe the strip target as a spectral-edge problem

The rank--trace method shows exactly why first and second trace moments are
the wrong observables for a strip.  A sparse exceptional hyperbolic block
changes normalized moments by `o(1)` but still contains the one off-line zero
that defeats a uniform strip.  A strip-sensitive finite compression would
need a lower bound for its least eigenvalue, a bound on the norm of its
negative part strong enough to be less than one block, or another
maximum-sensitive observable.  No such arithmetic estimate follows from the
Zeta23 moment calculation.

This suggests a disciplined hybrid research target:

```text
Zeta23 bulk census       handles positive-density directions;
fixed-box spectrometer   remains sensitive to one exceptional zero;
new arithmetic input     must control the lower spectral edge uniformly.
```

The third line is the unsolved step.  The first two lines do not combine into
a strip without it.

A concrete theorem card for that step is the following.  For each proposed
strip displacement `delta0>0`, construct one common Hermitian compression
`G_T` and prove constants `kappa(delta0)>0` such that, uniformly at large
height:

```text
carrier:
  a zero with |Re(rho)-1/2| >= delta0 in the target band
    -> lambda_min(G_T) <= -kappa(delta0) + ||remoteTail_T||,

tail:
  ||remoteTail_T|| < kappa(delta0)/4,

prime edge:
  lambda_min(G_T) > -kappa(delta0)/2.
```

The three lines would contradict one another and exclude that displacement.
Zeta23 supplies the local hyperbolic-block geometry behind `carrier` and much
of the tapering language behind `tail`; it does not prove that one block's
negative direction survives the full positive bulk with a uniform margin.
This repository's fixed-box spectrometer explains why the desired conclusion
must be sensitive to one exceptional zero.  Neither that uniform carrier
statement nor `prime edge` is currently proved.  A trace/Frobenius estimate
cannot substitute for them, and any proposed proof should be tested first
against a matrix with one fixed negative eigenvalue and a growing positive
bulk.

That fail-fast carrier test has now been carried out, and it closes the route
on the current inputs.  For a positive background `A` and selected negative
atom `u u*`, the exact screening parameter is
`b=u* A^dagger u`: the downdate `A-u u*` is positive semidefinite exactly when
`u` lies in `range(A)` and `b<=1`.  Zeta23's abstract block hypotheses admit
strictly screened examples.  More decisively, for every real even window
supported in `[-L/2,L/2]`, a full modulation lattice of reflected off-line
pairs has a positive-semidefinite aggregate Gabor matrix.  Thus tapering,
Poisson norms, reflection symmetry, and the local count scale do not force
`b>1` for a selected pair.

The sharp interval window has a qualitative Cauchy-matrix escape when the
compression dimension `d` is at least the number `q` of distinct relevant
zeros.  The original fixed-parameter range does not instantiate this card:
at `lambda=1` its Riemann--von Mangoldt main term gives

```text
N(T,2T)-d = (2 log 2 - 1) T/(2 pi) + O(log T) > 0;
```

Subsequent raw-error analysis shows that a varying support
`L=ell1+eta(T)` can cross this count deficit while retaining the smooth
prime-side estimates; even `eta(T)=theta log log(T/(2*pi))`, `0<theta<1`, is
admissible.  This repairs the dimension count but not the route: the sharp
full space still loses the small remote-tail estimate, while the smooth
window has no uniform smallest-singular-value bound.  A further endpoint-jet
restriction of the sharp span now supplies exact Cauchy--Vandermonde
interpolation together with an exponentially small remote tail.  It still
has no effective asymptotic signed-carrier rate, although collision merging
and compactness give a strict separation-free edge at every fixed set of
parameters.  The sharp full matrix and its endpoint-jet compression also
have exact Loewner displacement rank at most two.  This leaves their
confluent diagonal data free, so the evaluated prime moments still do not
control the lower spectral edge.  The proofs and exact countermodels are in
[`SINGLE-HYPERBOLIC-BLOCK-ISOLATION-GATE.md`](../results/SINGLE-HYPERBOLIC-BLOCK-ISOLATION-GATE.md)
and
[`ZETA23-ADDITIVE-EDGE-PADDING-AUDIT-2026-08-11.md`](../results/ZETA23-ADDITIVE-EDGE-PADDING-AUDIT-2026-08-11.md),
with the repaired carrier and higher-invariant obstruction in
[`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md)
and the compact signed-margin theorem in
[`ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-COMPACT-CARRIER-MARGIN-2026-08-11.md).

There is now one concrete use of the new density and moment theorems in that
carrier analysis.  A core lattice with one reflected pair every three sharp
spacings obeys the Riemann--von Mangoldt count and reduces the carrier scale
to `X^(2*alpha/3)`, but its on-line fraction is only `1/3` and the theorem
above excludes it.  The least pure sublattice compatible with the exact
simple-line constant is `k=7`, because

```text
2/3<C<5/7.
```

It has count-and-density carrier scale `X^(6*alpha/7)`.  Probing that same
hypothetical configuration with the legal bandwidth-one Montgomery--Taylor
window produces Frobenius mass `asymp d*X^(12*alpha/7)`, whereas Zeta23
proves only `O(d)`.  No positive on-line filler with the correct trace can
absorb its negative trace.  A separate residue-class diagonalization proves
the matching signed edge `K asymp X^(6*alpha/7)` after endpoint jets, so this
is not an artefact of an upper norm bound.  Thus the simple-line theorem
removes the densest periodic screen and the evaluated second moment removes
the remaining density-legal `k=7` screen.  Sparse or aperiodic screening of
one exceptional pair remains outside both arguments.  See
[`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](../results/ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md),
[`ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md`](../results/ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md),
and
[`ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md`](../results/ZETA23-K7-GABOR-MOMENT-INCOMPATIBILITY-2026-08-11.md).

The sparse endpoint can also be stated sharply.  If there is only one core
off-line pair and every other local atom is simple and on line, a sampling
bound makes the on-line Gram operator polylogarithmic, while an explicit
binomial-tail packet in the endpoint-jet space gives
`K>=X^(alpha-o(1))/L`.  The first two moments are compatible with this large
single-pair edge.  Thus the remaining sparse problem is not one pair versus
the on-line population; it requires at least one additional off-line positive
mate.  See
[`ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md`](../results/ZETA23-SINGLE-CORE-PAIR-ONLINE-SCREENING-BOUND-2026-08-11.md).

The multi-pair sparse problem has now been decided at the level of those
inputs.  A Gevrey-tapered `k=3` island of sublinear ordinate length preserves
the full count, the global simple-line density, and the leading Zeta23
trace/Frobenius moment, while its endpoint-jet edge satisfies

```text
0<K<=X^(2*alpha/3+o(1)).
```

The independent hostile audit checks both the endpoint `q=3` corner and the
separate legal bandwidth-one moment probe.  The construction works throughout
the canonical logarithmic-padding regime for every `alpha<1/2`, and at the
weakest padding for `alpha<3/8`.  It is an artificial zero configuration, not
an `L`-function zero set, but it proves that the imported density and moment
theorems do not supply the missing full-power carrier estimate.  See
[`ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md`](../results/ZETA23-SPARSE-TAPERED-K3-ISLAND-2026-08-11.md).

This countermodel also corrects the most optimistic use of the density
constant.  A proportional two-lobe dimension ledger would formally give a
conditional right edge `0.597907...`, but its target-retention premise would
force a carrier larger than the sparse island's proved operator norm whenever
the lobe width is below `1/3`.  The first threshold not contradicted by that
model is the still-conditional edge `3/4+epsilon`.  Conversely, putting the
entire globally allowed off-line population in one equal-depth `k=2` block
does not evade the moment theorem: its legal `q=1` alias makes the Frobenius
norm too large.  Only sublinear local clusters survive the bulk ledger, and
their selected-row leverage remains uncontrolled.  See
[`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](../results/ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md)
and
[`ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md`](../results/ZETA23-LOCAL-K2-CLUSTER-MOMENT-BARRIER-2026-08-11.md).

For the explicit endpoint-flat packet, exact completion reduces the
power-sized arithmetic term to one smooth centered von Mangoldt polynomial.
The matched target is `o(Y^alpha)` and the current unconditional bound remains
`Y^(1/2-o(1))`, including for the shorter `Y=X^(2/3)` alias of the sparse
screen.  Exact recompletion leaves the ordinary coefficient
`-mu(n)log(n)`; it is not annihilated by the packet's zero integral.  A
prime-translate nullspace is a legitimate remaining candidate only with a
quantitative Laplace-leverage bound, not from dimension counting alone.  The
full packet and completion ledger is
[`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](../results/ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md).
The optimized nullspace is now characterized exactly: its factorization norm
is the Wiener `l^1` norm, and finite duality turns the carrier into an
`l^infinity` approximation problem on prime-power logarithms.  A natural
von-Mangoldt quadrature plus KMT gives only a logarithmic upper bound.  This
rules out a fixed limiting leverage but preserves the full power exponent;
no matching subpower lower bound is known.  Hermitian complexification
validates the independent-lobe polarization without adding a conjectural
real-descent step.  See
[`ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`](../results/ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md).

The unresolved estimates are scale-coupled.  For a depth-`alpha` pair, write
the actual normalized carrier margin as `K=(X^alpha/L)r_T`, `X=exp(L)`, and
put `B_X=osc(A_X)+(2/L)max|D_X|`.  Tail closure asks for
`E_remote=o(K)`, while the scalar prime route closes only with the matched
bound `B_X=o(X^alpha r_T)`.  A direct constrained Pick/Loewner theorem is an
alternative only if its normalized prime negative edge is `o(K)` at that
same actual `K`.  The exact statements, without conditioning shorthand, are
in
[`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](../results/ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md)
and
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](../results/ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
The exact scalar audit imports the best directly applicable sharp-cutoff
prime-twist estimate and obtains
`B_X<<X^(1/2)/(log X)^(3/10)` on the transition scale.  This is only
`X^(1/2-o(1))`, and the present critical-grid data do not satisfy the
stronger complex, continuous, power-wide hypotheses of Turan's converse
criterion.  See
[`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`](../results/ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md).
The endpoint-jet difference factor does not supply the missing power: after
the correct mass matrix is retained, generalized eigenvalues are exactly
those of the codimension-`m` compression, and most large confluent diagonal
coordinates have small discarded leverage.  See
[`ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md`](../results/ZETA23-ENDPOINT-JET-PRIME-COMPRESSION-OBSTRUCTION-2026-08-11.md).
Accordingly, this spectral-edge card is now a conditional survivor only.  Its
current zero-side bulk hypotheses have an explicit sparse countermodel; any
continuation must use a genuinely zeta-specific exclusion of that model or a
prime/zero interpolation estimate at the actual reduced edge.
The consolidated theorem/no-go frontier is
[`UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md`](../results/UNIFORM-STRIP-ITERATION-SYNTHESIS-2026-08-11.md).

## 5. Why this does not propagate the current certificate

The scale mismatch is decisive.  This repository's certified interval has
fixed physical support length `7/8`.  A Gabor family made from that window has
dimension `O(T)`, while `N(T,2T)` is of order `T log T`; its normalized rank
tends to zero.  Zeta23 obtains a positive proportion by letting support grow
like `log T`, precisely the all-support regime not reached by the current
local certificate.

More fundamentally, a density theorem permits a sparse sequence of off-line
zeros approaching `Re(s)=1`.  Such a sequence can determine

```text
sup_rho |Re(rho)-1/2|
```

while having density zero.  Even a hypothetical `100%-o(1)` critical-line
theorem would therefore imply neither a fixed zero-free strip nor RH.  Zeta23
does not inhabit any field of this project's `PropagationPackage`.

## 6. Separate disclosure concerning a wider numerical window

Anthropic's
[process appendix](https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf)
describes another agent-produced
interval-arithmetic positivity claim on multiplicative support `[1/3,3]`.
The appendix itself calls this unrefereed and not independently rerun.  No
source, raw data, theorem statement, or replayable certificate for it appears
in the public Zeta23 repository.  It is not an established input and has not
been incorporated as one.

It is nevertheless a priority warning.  In this project's convention it
would correspond to

```text
a = log(3),        L = 4 log(3) = 4.394449...,
```

with active prime powers below `9`, rather than the currently certified
`a=7/16` Lean endpoint.  It is also wider than the project's separate
computer-assisted `n=4` checkpoint at program length `L=749/250`, which has
half-width `a=749/1000` and active prime powers `{2,3,4}`.  Publication text
must therefore avoid unqualified claims such as “largest certified support”
or “first interval-arithmetic Weil certificate.”  The defensible distinction
of this repository is its fully specified, reproducible, Lean-kernel-checked
full-domain arithmetic theorem, not maximal window size.

## 7. Novelty and publication effect

If specialist review and independent reconstruction confirm it, the Zeta23
density theorem is a major analytic-number-theory result.  Its rank/inertia
idea and formalization belong to Anthropic's work; reusing them with
attribution does not become novelty of this project.

For this repository the immediate publication effect is mixed:

- completing the smooth explicit-formula adapter would materially strengthen
  the trust story by removing a named literature axiom;
- it would not strengthen the fixed-window arithmetic inequality or the
  all-support conclusion;
- the portable Hermitian library is useful infrastructure, but not an
  independent contribution unless a genuinely new application or API
  generalization is proved; and
- the unpublished wider-window disclosure weakens any numerical-priority
  claim even though it supplies no theorem that can be relied on.

The local endpoint remains plausibly publishable as a computer-assisted/formal
analysis result if it is presented as a reproducible full-domain arithmetic
certificate with exact normalization.  It should not be presented as the
leading current advance on the distribution of zeta zeros, nor as evidence
that the Zeta23 density theorem propagates to RH.

## 8. Integration decision

The result is incorporated here in three ways:

1. as a corrected modern density baseline;
2. as an explicit formal adapter target that can remove the smooth
   Guinand--Weil literature axiom; and
3. as a rank/inertia research branch whose output and limitations are kept
   separate from uniform-strip propagation.

The next code milestone should be the seven-lemma explicit-formula adapter,
proved in a small compatibility package before importing any large external
tree.  The proposed single-exception spectral-edge milestone has failed its
structural gate on the current hypotheses.  A mixed-Gabor strip branch should
resume only after zeta-specific stable-interpolation and prime lower-spectral-
edge results are available; varying additive padding has already removed the
coarse dimension deficit, and endpoint jets have removed the qualitative
sharp-tail conflict.  Until then,
the fixed-box exponent/Type-II program remains the better strip-facing
scoreboard.
