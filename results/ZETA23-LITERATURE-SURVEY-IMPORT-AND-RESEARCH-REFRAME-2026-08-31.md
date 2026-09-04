# Literature survey, theorem import, and research reframe

**Date:** 2026-08-31
**Literature cutoff:** 2026-08-31
**Preflight:**
[`zeta23_literature_reframe_preflight_v1.json`](context/zeta23_literature_reframe_preflight_v1.json)
**Machine-readable ledger:**
[`zeta23_literature_import_ledger_2026_08_31_v1.json`](context/zeta23_literature_import_ledger_2026_08_31_v1.json)

Companion audits:

- [`ZETA23-WEIL-GLOBAL-SUPPORT-LITERATURE-PASSPORT-AND-RECENT-CLAIM-AUDIT-2026-08-31.md`](ZETA23-WEIL-GLOBAL-SUPPORT-LITERATURE-PASSPORT-AND-RECENT-CLAIM-AUDIT-2026-08-31.md)
- [`ZETA23-QP-TURAN-ACTUAL-PRIME-LITERATURE-DELTA-AND-PASSPORT-AUDIT-2026-08-31.md`](ZETA23-QP-TURAN-ACTUAL-PRIME-LITERATURE-DELTA-AND-PASSPORT-AUDIT-2026-08-31.md)
- [`ZETA23-COEFFICIENT-SENSITIVE-RADIALIZATION-LITERATURE-PASSPORT-2026-08-31.md`](ZETA23-COEFFICIENT-SENSITIVE-RADIALIZATION-LITERATURE-PASSPORT-2026-08-31.md)
- [`ZETA23-YANG-YANG-7962-ZENODO-HOSTILE-AUDIT-2026-08-31.md`](ZETA23-YANG-YANG-7962-ZENODO-HOSTILE-AUDIT-2026-08-31.md)

## Verdict

No surveyed result proves the contemplated uniform zero-free strip, either
of its two open QP/Turan inputs, global Weil positivity, or RH.  The search
nevertheless changes the research map in five consequential ways.

1. A new preprint of Marcus Chuk claims strict Weil positivity at physical
   half-window `a=.8`, which is project `L_program=3.2`.  This is much larger
   than the formal project seed `L_program=1.75` and is numerically plausible,
   but the public source contains no numerical certificate.  It is not yet a
   trusted theorem import and, even if correct, it is only a larger local
   seed.

2. Alpoge--Furman's final public paper proves the new unconditional
   two-thirds theorem and states exactly where its method next meets hard
   arithmetic.  Its fourth trace requires Hardy--Littlewood-type correlations
   of `Lambda*Lambda` at shifts `|h|<=X^2/T`.  At our specialization this is
   precisely `H=Y^2/T=Y^(16/33)`, the physical scale of `CA4`.  This strongly
   validates our diagnosis of the bottleneck, but its natural weights do not
   match our adjacent-gap hats.

3. A Zenodo manuscript claiming `79.62%` says it bypasses that fourth-trace
   wall by truncating to polylogarithmic moduli.  Two independent audits found
   the same fatal first gap: the truncation invents a per-cell `ell^(-k)`
   decay by reusing a single global normalization.  The actual modulus weights
   put asymptotically vanishing mass, not `1-o(1)` mass, below a polylogarithmic
   cutoff.  Its exact moment-to-density certificate is valid conditionally;
   the asserted moments and headline are not established.

4. Maynard--Pandey--Radziwill and Wright supply genuinely new prime and
   Kloosterman estimates, but exact exponent and passport audits rule out
   black-box applications.  MPR has the wrong phase, mask, localization, and
   major-arc behavior; Wright's unchanged first term caps even an idealized
   reconstruction at gain `1/8`, far below the `CA4` requirement `127/330`.

5. Recent weighted algebraic-energy results are stronger than our earlier
   shorthand suggested: Hu really does allow arbitrary complex weights.  But
   these theorems count exact equalities on a full dual group.  They do not
   serialize the project's prescribed near-relations, translated kernel,
   masks, source, or adaptive quantifiers.  They are downstream terminators,
   not the missing transport.

The durable state is therefore

```text
RH                                             OPEN
global arithmetic Weil positivity             OPEN / RH-equivalent
zeta-specific adjacent-support propagation     OPEN
DPA_P(.019)                                    OPEN
LTRAD_P(.0189,.001)                            OPEN
CA4(163/1000,1/10)                             OPEN
sharp four-cycle bound                         OPEN, not a direct strip gate
```

## 1. Search protocol and theorem passport

The survey used primary papers, official preprints, journal pages, author
manuscripts, and released proof artifacts.  Search hits were compared to the
existing August 29 import so that old results were not presented as new.

Every proposed import was tested for

```text
arithmetic mask and source;
coefficient cone and sign;
normalization;
height band and one-sided polarity;
quantifier order;
metric resolution;
exponent budget;
downstream adapter;
retained share of the target norm.
```

The last field is a new mandatory preflight gate.  An estimate on an easy
range is irrelevant if that range carries `o(1)` of the normalized object.

## 2. Weil/global-support literature

### 2.1 Chuk's compact-window claim

Marcus Chuk's
[*Weil positivity in compact windows: certified two-sided bounds and a
Landau--Widom decay law*](https://arxiv.org/abs/2608.24827) claims

\[
 Q(f)\ge 8.9\times10^{-18}\|f\|_2^2,
 \qquad \operatorname{supp}f\subset[-.8,.8].       \tag{2.1}
\]

The normalization is easy to misread.  Chuk's `L` is our physical
half-window `a`, while the project's historical support coordinate is

\[
 L_{\rm program}=4a.
\]

Thus (2.1) is the project point `L_program=3.2`.  It has active prime powers
`2,3,4` and lies only

\[
 2\log5-3.2=.018875824868\ldots                  \tag{2.2}
\]

below the next prime activation.  It would enlarge the formal seed
`a=7/16`, `L_program=1.75`, by a factor `64/35`.

The public arXiv source does not contain the matrix, interval quadrature,
verified Cholesky factor, or tail balls used for its stated `8.9e-18` floor.
An independent 65-digit project assembly gave the even-sector values

```text
m=32   5.7499e-16
m=48   1.7460e-17
m=64   1.7026e-17
m=80   1.6787e-17
```

and at `m=80` a second-even value near `8.44e-12` and odd minimum near
`1.59e-14`.  These numbers agree in scale with the preprint and exclude a
gross normalization/parity mistake.  They are floating Galerkin diagnostics,
not a lower-bound certificate.

There is also a repairable domain defect: because the Weil symbol grows like
`log|t|`, the finite quadratic-form domain is naturally

\[
 \left\{f\in L^2[-a,a]:
 \int \log(2+t^2)|\widehat f(t)|^2dt<\infty\right\}, \tag{2.3}
\]

not literally every `L2` function unless the form is declared extended
valued.  Ground-state statements need the corresponding closed/Friedrichs
operator.

**Import decision.**  Record (2.1) as a plausible recent claim and reproduce
it with interval arithmetic before promoting the local endpoint.  It proves
no support propagation.

### 2.2 What Chuk's barrier really rules out

For the finite prime comb of mass

\[
 A_L=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n},
\]

simultaneous recurrence of the prime phases gives `sup P_L=A_L`.  Chuk's
one-stroke certificate therefore needs

\[
 T^\sharp>2\pi e^{A_L},\qquad A_L\sim4e^L,          \tag{2.4}
\]

and its matrix dimension grows doubly exponentially.

This is a real barrier for replacing the whole comb by the constant absolute
bound `A_L`.  It is not a no-go for every pointwise-symbol method: a
`t`-dependent estimate can couple phase recurrence to the growing
archimedean term, and a compact transition band can be certified directly.

The strategic conclusion is still strong.  Repeatedly enlarging a constant
comb envelope is not a scalable RH program.  A global proof needs averaged
or operator control, or arithmetic uniqueness of the actual zeta
continuation.

### 2.3 Operator and extension imports

Suzuki's revised
[arXiv:2606.09096v2](https://arxiv.org/abs/2606.09096v2) supplies the
localized Friedrichs framework, continuity of the lowest eigenvalue, and a
conditional characteristic-function limit.  The current target is

\[
 e^{\phi(a,z)}W(a,\theta;z)\longrightarrow
 \frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)},     \tag{2.5}
\]

not the older `z^2 xi/xi'` expression used in Suzuki v1 and historical
project notes.
The convergence remains an assumption.

Krein/Jorgensen--Niedzialomski extension theory supplies a useful route
killer: in one dimension a continuous positive-definite function on an
interval has a global positive-definite extension, generally nonunique.
Therefore proving the existence of *some* positive extension cannot identify
the globally defined zeta kernel.  The missing theorem must control the
actual old/new cross block or prove uniqueness from exact arithmetic source
coordinates.

No source checked in the Suzuki, Connes--Consani--Moscovici,
Connes--van Suijlekom, Groskin, Burnol, or positive-extension literature
proves

```text
actual zeta positivity on [-a,a]
    => actual zeta positivity on [-a-delta,a+delta].
```

## 3. Gabor higher traces and the fourth-correlation wall

### 3.1 The valid two-thirds theorem

Alpoge--Furman
[*More than two thirds of the zeta zeros are simple and on the critical
line*](https://arxiv.org/abs/2608.13637) prove unconditionally

\[
 \frac{N_0^s(T,2T)}{N(T,2T)}\ge\frac23-o(1),
 \qquad
 \frac{N_d(T,2T)}{N(T,2T)}\ge\frac56-o(1),          \tag{3.1}
\]

with optimized constants `.6725007...` and `.8362503...`.  The project had
already imported and checked the rank/inertia theorem; this survey replaces
the earlier CDN citation by the final arXiv paper and imports its exact
higher-trace boundary.

Their prime-side diagonal method for trace order `k` works in the
Rudnick--Sarnak range

\[
 X^k\le T^{2-\varepsilon}.                          \tag{3.2}
\]

At project scale `X=Y`, `T=Y^(50/33)`, order four misses (3.2) by

\[
 \frac{Y^4}{Y^{(50/33)(2-\varepsilon)}}
 =Y^{32/33+(50/33)\varepsilon}.                    \tag{3.3}
\]

Their conditional `HL*(4)` statement identifies the missing arithmetic as

\[
 \sum_m(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h),
 \qquad |h|\le X^2/T.                              \tag{3.4}
\]

Putting `X=Y` makes the shift scale in (3.4)

\[
 H=Y^2/T=Y^{16/33},                                \tag{3.5}
\]

exactly the top-scale product resolution of the project's `CA4` expansion.
This is the strongest literature confirmation that `CA4` found a natural
arithmetic obstruction rather than an artifact of our derivation.

The match stops at the passport.  Equation (3.4) has natural
`Lambda*Lambda` weights and a global Gabor trace.  `CA4` has positive
adjacent-gap hat weights, one shell, and a translated signed kernel.  Even a
proof of natural `HL*(4)` would require a mask-preserving adapter.

### 3.2 The `79.62%` certified-candidate does not cross the wall

Yang--Yang's
[Zenodo manuscript](https://zenodo.org/records/21975237) claims trace moments
through order six and `79.62%` simple on-line zeros.  Its
[public package](https://github.com/JoshuaHKU/zeta-0.7947-reproduction)
contains real exact-rational and Lean work.  In particular, the degree-six
moment certificate correctly proves

```text
the asserted moments
    => 0.7962709657... simple/on-line
       and 0.8981354828... distinct.
```

It does not prove the asserted moments.

The first fatal edge is the paper's modulus truncation.  It defines one
global

\[
 \ell_1=\log(T/2\pi)+2\log2-1                      \tag{3.6}
\]

and later silently treats `ell_1` as an integer cell parameter with a
cellwise `ell^(-k)` weight.  That factor is absent from the actual trace
ledger, whose modulus weight is

\[
 \frac{\Lambda(b_1)\Lambda(b_2)}{b_1b_2}.          \tag{3.7}
\]

By Mertens' formula, a cutoff `P=(log X)^B` retains the raw fraction

\[
 \frac{\left(\sum_{b\le P}\Lambda(b)/b\right)^2}
      {\left(\sum_{b\le X}\Lambda(b)/b\right)^2}
 =\left(\frac{B\log\log X}{\log X}\right)^2+o(1)
 \longrightarrow0.                                \tag{3.8}
\]

The proposed truncation therefore deletes almost all of the mass.  The
manuscript itself calls the power-modulus version open.  Removing the invalid
truncation restores exactly the unrestricted higher-trace correlation wall
in (3.4).

The Lean files verify polynomial/rational identities and finite local laws;
they contain no zeta, prime-sum, limit, trace-moment, or Lemma-D theorem.
The minor/mixed spectral `L2` aggregation is also asserted as classical
rather than proved, and several cited analytic archives are absent.

**Import decision.**  Import the conditional moment-consumption algebra.
Do not import Lemma D, `m_4=13/4`, the higher moments, or the `79.62%`
headline.  The proof is invalid as written; the numerical density statement
itself is not refuted.

## 4. Prime, Kloosterman, and exact-energy imports

### 4.1 Maynard--Pandey--Radziwill

Maynard--Pandey--Radziwill
[*Exponential sums over primes*](https://arxiv.org/abs/2608.14777) prove,
for `alpha=a/q+epsilon` and `B=max(q,qN|epsilon|)`, that

\[
 \left|\sum_{n<N}\Lambda(n)e(n\alpha)\right|
 \le N^{o(1)}\left(\frac{N}{B^{1/2}}+N^{19/24}\right). \tag{4.1}
\]

This is a genuine improvement over the classical `N^(4/5)` term.  It does
not directly estimate the project object:

- its phase is additive, not `t log(p/Y)`;
- its coefficients are the natural von Mangoldt sequence, not adjacent-gap
  hats or a source-normalized signed vector;
- linearizing the log phase at top height needs blocks of length at most
  `Y^(8/33)`, whereas differencing (4.1) leaves a `Y^(19/24)` error;
- the major-arc term can have no fixed saving.

Even granting the friendliest false identifications, the resulting normalized
square is only `Y^(-5/12+o(1))`; `CA4` requires
`Y^(-5249/3250+o(1))`.  The deficit is

\[
 \frac{5249}{3250}-\frac5{12}
 =\frac{23369}{19500}=1.198410\ldots .              \tag{4.2}
\]

The theorem is an important benchmark, but not a current adapter.

### 4.2 Wright's subdyadic Kloosterman theorem

Wright's
[*Trilinear Kloosterman fractions II*](https://arxiv.org/abs/2608.27732)
improves trilinear reciprocal-phase bounds when two variables are on
subdyadic intervals and extends a nearly balanced convolution range from
`1/112` to `1/68`.

This recognizes a real feature of our attempted completion: physical short
blocks.  At the exact `CA4` top scale, however, the theorem's unchanged first
term caps an ideal lossless reconstruction at gain

\[
 \frac18.
\]

The target needs `127/330`, leaving

\[
 \frac{127}{330}-\frac18
 =\frac{343}{1320}=.259848\ldots .                  \tag{4.3}
\]

The actual scalar reconstruction is worse because summing short blocks can
cost `Y^(1-theta)`.  The theorem also has three separated coefficient slots
and a nonzero reciprocal phase; it does not retain four adjacent-gap weights,
the translated sign, the zero/main sector, or the shell-center quantifiers.

**Decision.**  Close the black-box `CA4 -> Wright II` route.  A useful new
dispersion theorem would have to improve the first term and preserve the
collective signed reconstruction.

Ramaré's 2026 preprint *The weighted large sieve through Parseval*,
[arXiv:2605.29470](https://arxiv.org/abs/2605.29470), is withdrawn by the
author for an important miscalculation and is excluded from the import set.

### 4.3 Hu, Jing--Wu, and Cushman--Demeter--Wu

The August 2026 algebraic-energy results are:

- [Jing--Wu](https://arxiv.org/abs/2608.14467): sharp near-diagonal exact
  four-fold energy on algebraic surfaces, with a line-occupancy factor;
- [Cushman--Demeter--Wu](https://arxiv.org/abs/2608.12316): near-optimal
  exact six-fold energy on strictly convex curves;
- [Hu](https://arxiv.org/abs/2608.18956): hereditary exact energy implies
  arbitrary complex weighted `L4`/Young estimates, including a sharp
  quadratic-threefold case.

The exact distinction is

```text
these papers: full-dual integral -> exact additive equality;
project CA4: translated finite interval -> signed near equality at 1/T;
project FC:  four masks + coefficient-sensitive near equality;
project LTRAD: source-conditioned one-sided finite-time return.
```

Set-dependent admissible thickening does not provide a uniform lower bound at
the prescribed resolution.  These theorems become relevant only after a
resolution-stable serialization that preserves masks and controls its leaf or
turning-complexity tax.

## 5. LTRAD and the soft-geometry boundary

Montgomery--Vaughan already tensorizes to Hilbert-space-valued coefficients
and supplies separated-block `L2` control.  Cluster-frame results handle
resolved frequency clusters.  A generic “mask-sensitive vector-valued large
sieve” is therefore not an adequate description of the missing theorem.

The actual `LTRAD` quantifier is

```text
for every legal actual-prime source event,
  for every adaptive source-normalized signed dual vector,
    find a height before B=Y^(50/33)
      with the required one-sided return.
```

Qualitatively, rational independence of distinct prime logarithms gives
density of each fixed-dimensional phase orbit.  Quantitatively, the shell
dimension grows like `Y/log Y`, while the allowed hitting time is only
polynomial.  That is the missing arithmetic.

Soft convex compression cannot bridge it.  Absolute radial accuracy
`Y^(-.0189)` costs about

\[
 \varepsilon^{-2}=Y^{.0378}                         \tag{5.1}
\]

atoms under approximate Caratheodory, while the proved participation scale
is only `Y^.0179`--`Y^.0189`.  The factor-two exponent loss is intrinsic to
that proof class.  Generic random-phase amplitudes are around `Y^(-1/2)`,
also far below the unusually large source-conditioned excursion required by
the target.

Thus `LTRAD` must exploit a concrete algebraic restriction imposed by an
actual negative prime source event.  Density, separation, covariance, and
rational independence alone survive the project's pseudo-node falsifiers.

## 6. Reframed decision tree

```text
RH
|
+-- Weil equivalence
|   |
|   +-- local seed: formal L=1.75; Chuk claims L=3.2
|   `-- actual-zeta adjacent support / identifying continuation  OPEN
|
`-- contemplated fixed strip near Re(s)=1
    |
    +-- DPA_P(.019)                                 OPEN
    |   `-- frozen hats proved through t<=Y^.8392
    |       `-- high tail: weighted semiprime covariance / CA4  OPEN
    |           `-- same scale as natural HL*(4), wrong mask
    |
    `-- LTRAD_P(.0189,.001)                         OPEN
        `-- source-conditioned finite-time prime-log return
            `-- soft L2/convex/exact-energy tools need new transport
```

This reframe changes priorities, not theorem status.

### 6.1 Weil route

1. Reproduce Chuk's `a=.8` claim with interval/Arb arithmetic, a serialized
   matrix, explicit quadrature and tail balls, and the domain (2.3).
2. If it passes, promote only the seed.  The next controlled event is the
   adjacent `p=5` activation at `L_program=2log5`; attack its exact-source
   Schur complement rather than another global comb envelope.
3. In parallel, test whether exact finite source coordinates make the zeta
   continuation an exposed/unique positive extension.  Abstract extension
   existence is vacuous here.

### 6.2 DPA/CA4 route

The literature raises confidence that `CA4` is the correct *kind* of
high-tail arithmetic and lowers confidence that current general-purpose
moment technology can prove it.

The proposed **mass-preserving mask-transference falsifier** has now been
run; see the
[full audit](ZETA23-CA4-MASS-PRESERVING-NATURAL-MASK-TRANSFERENCE-FALSIFIER-2026-08-31.md).
It asked:

```text
Can the adjacent-gap-weighted, translated CA4 covariance be decomposed
into a controlled number of natural Lambda*Lambda correlation forms,
with the shell, kernel sign, H=Y^2/T resolution, and Y^.1 budget retained?
```

The answer is **no for scalar Alpoge--Furman-style transference through
consecutive intervals or bounded-variation smooth natural atoms**.  A dual
variation certificate for the actual retained hat weights forces scalar
recombination cost `gg (log Y)^(-4)`, whereas CA4 permits only
`Y^(-5249/6500+o(1))`.  Positive square mixtures fail exactly by rank, and a
bounded-density pseudonode model rules out rescue by abstract absolute
continuity.  This does not refute actual-prime CA4 or every conceivable
product-dependent atom.

The post-survey
[edge-flux/product-graph audit](ZETA23-CA4-EDGE-FLUX-PRODUCT-GRAPH-AND-TWO-CHANNEL-AUDIT-2026-08-31.md)
compresses this surviving target further.  With
`delta=lambda-eta`, `s=lambda+eta`, and
`r_i=delta_i/s_i`, the ordered semiprime discrepancy is exactly

```text
(delta tensor s+s tensor delta)/2,
A_ik=(s_i s_k/2)(r_i+r_k),
M_lambda^2-M_eta^2=M_delta M_s,
```

where `|r_i|<=1` and `sum s_i r_i=0`.  Thus the honest target is not an
arbitrarily large vector theorem but a two-channel, additive-rank-two,
selector-sensitive mixed estimate with the common translated kernel.  The
candidate `PG-EF(1/10)` diagonal-relative bound remains open, and the
bounded-gap motif proves that path-boundary, transport, edge-square, or
product-`H^-1` size alone cannot imply it.  This is the missing new
mathematics, not an adapter to scalar natural correlation.

### 6.3 LTRAD route

First extract the exact restrictions that a legal negative prime source
event imposes on the adaptive dual coefficients, and ask whether the
prime-density/inverse-compensation countermodels can realize those
restrictions.  If they can, the present LTRAD formulation is false or needs a
stronger arithmetic premise.  If they cannot, that obstruction is the first
genuinely prime-specific input for either:

- a source-conditioned quantitative Bohr/Kronecker return theorem; or
- a `B^(-1)`-faithful masked serialization into Hu/Jing--Wu/CDW-type exact
  energy terminators.

Do not spend further effort strengthening ordinary frame, discrepancy, or
sampling theorems without this source restriction.

## 7. Updated confidence and hard stops

The survey increases confidence in three diagnoses:

- `CA4` sits at a real Hardy--Littlewood higher-trace wall;
- the missing `LTRAD` theorem is arithmetic finite-time return, not generic
  vector-valued `L2`;
- global Weil progress requires source identification or cross-block control,
  not abstract positive extension.

It decreases confidence in three proposed shortcuts:

- small-modulus truncation without a mass ledger;
- black-box application of MPR or Wright II to the gap-hat statistic;
- exact algebraic energy without resolution-stable serialization.

Hard stops going forward:

1. Do not infer a strip from any density theorem, even density `1-o(1)`.
2. Do not infer global Weil positivity from any fixed local window.
3. Do not call a floating Galerkin value a certified lower bound.
4. Do not import Yang--Yang's Lemma D or headline.
5. Do not replace gap weights by `Lambda` weights without a quantified mask
   adapter.
6. Do not replace finite-window near equality by full-dual exact energy.
7. Do not accept a truncation until its retained normalized mass is `1-o(1)`.
8. Keep `DPA` and `LTRAD` as independent locks unless a common certificate is
   actually proved.

## 8. Net result

This survey imports several useful modules and one important negative result,
but no new strip theorem:

```text
trusted import:        Alpoge--Furman two-thirds/inertia theorem;
new boundary import:   its HL*(4) higher-trace correlation scale;
new benchmark:         MPR N^(19/24) prime exponential sum;
new benchmark:         Wright II subdyadic Kloosterman theorem;
downstream modules:    Hu/Jing--Wu/CDW exact energy;
version correction:    Suzuki 2606.09096v2 target;
pending reproduction:  Chuk local a=.8 positivity;
rejected proof:         Yang--Yang 79.62% analytic chain;
excluded source:        withdrawn Ramare weighted large sieve.
```

The most important conceptual import is the equality of scales

\[
 \boxed{\text{Gabor }HL^*(4)\text{ shifts}}
 \quad |h|\le X^2/T
 \quad\longleftrightarrow\quad
 \boxed{\text{project }CA4\text{ resolution}}
 \quad H=Y^2/T.
\]

That does not prove `CA4`.  It tells us that the four-distinct balanced
semiprime covariance is the real arithmetic problem, and that any proposed
escape must preserve both its conductor mass and its adjacent-gap mask.
