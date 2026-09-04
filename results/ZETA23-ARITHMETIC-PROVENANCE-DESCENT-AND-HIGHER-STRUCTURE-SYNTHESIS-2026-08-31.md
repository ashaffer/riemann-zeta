# Arithmetic provenance, descent, and the higher structure of the project

**Date:** 2026-08-31
**Status:** structural consolidation; elementary exact lemmas proved; all
load-bearing analytic targets remain open

Preflight:
[`zeta23_arithmetic_provenance_higher_structure_preflight_v1.json`](context/zeta23_arithmetic_provenance_higher_structure_preflight_v1.json)

Machine-readable ledger:
[`zeta23_arithmetic_provenance_higher_structure_ledger_v1.json`](context/zeta23_arithmetic_provenance_higher_structure_ledger_v1.json)

Exact algebra and replay:
[`arithmetic_provenance_structure.py`](../src/arithmetic_provenance_structure.py),
[`test_arithmetic_provenance_structure.py`](../src/test_arithmetic_provenance_structure.py)

Authoritative inputs:

- [`ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`](ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md);
- [`ZETA23-LITERATURE-SURVEY-IMPORT-AND-RESEARCH-REFRAME-2026-08-31.md`](ZETA23-LITERATURE-SURVEY-IMPORT-AND-RESEARCH-REFRAME-2026-08-31.md);
- [`ZETA23-CA4-MASS-PRESERVING-NATURAL-MASK-TRANSFERENCE-FALSIFIER-2026-08-31.md`](ZETA23-CA4-MASS-PRESERVING-NATURAL-MASK-TRANSFERENCE-FALSIFIER-2026-08-31.md);
- [`ZETA23-CA4-NATURAL-MASK-MASS-TRANSFERENCE-HOSTILE-AUDIT-2026-08-31.md`](ZETA23-CA4-NATURAL-MASK-MASS-TRANSFERENCE-HOSTILE-AUDIT-2026-08-31.md);
- [`CORE-INSIGHTS-SYNTHESIS.md`](CORE-INSIGHTS-SYNTHESIS.md);
- [`NO-GO-THEOREM-GUIDE.md`](../publication/NO-GO-THEOREM-GUIDE.md).

---

## 0. Consolidated verdict

The project has uncovered a common *shape* behind several failures, but not a
common analytic theorem that solves them.  In each main branch, a familiar
proof engine becomes applicable only after forgetting one or more pieces of
arithmetic provenance.  The desired conclusion is not determined by the
resulting coarse object.  The silently assumed inverse to that forgetting
map is the missing mathematics.

The recurring invalid composite is

```text
source-labelled arithmetic object
      -> forget source / mask / sign / boundary / resolution
      -> apply a familiar positive, average, or extension theorem
      -> silently reconstruct the forgotten labelled object.
```

This diagnosis is now precise enough to be falsifiable.  For a forgetful map
`U` and target functional `T`, inspect `T` on every fiber of `U`.  Large
fiber oscillation blocks two-sided reconstruction.  For an upper or lower
theorem, the fiber supremum or infimum must instead cross the claimed
threshold.  These tests organize the abstract Weil-extension no-go, the
natural-mask `CA4` no-go, soft `LTRAD` countermodels, and several resolution
and truncation failures.

Three exact structural observations survive the consolidation:

1. **Fiber descent criterion.**  Two-sided approximate reconstruction from a
   coarse object is equivalent to a uniform fiber-diameter bound; one-sided
   claims use exact fiber suprema or infima.  This is an elementary theorem,
   not a metaphor.
2. **Pointed relative energy.**  The live Weil, `CA4`, and `LTRAD` quantities
   are all energies or quotient norms of a distinguished arithmetic section,
   vector, multiplier, or cross block.  Unpointed carrier information does
   not determine them.
3. **Two-channel product-boundary identity.**  The already-known ordered-path
   flux representation of a zero-mass mask discrepancy lifts under the
   symmetric square to an additive rank-at-most-two divergence on the
   prime-pair product graph.  The semiprime discrepancy is exactly one mixed
   product `M_delta M_(lambda+eta)`.  This is a useful compression and
   integration-by-parts interface, but exactness alone supplies no
   cancellation.

The current theorem status is unchanged:

```text
RH:                                      OPEN
global Weil positivity:                 OPEN / RH-equivalent interface
fixed zero-free strip near Re(s)=1:     OPEN
DPA_P(.019):                            OPEN
LTRAD_P(.0189,.001):                    OPEN
CA4:                                    OPEN, sufficient for one DPA route
sharp four-cycle bound:                 OPEN, not a direct strip gate
fixed strip -> RH amplifier:            ABSENT
```

The most important higher-level correction is therefore not “find one grand
categorical theorem.”  It is:

> Search for source-conditioned descent: prove that the actual arithmetic
> label either determines the missing cross interaction, or keeps the
> distinguished object uniformly observable in the relevant signed norm.

This principle links the form of the bottlenecks while keeping the Weil and
QP/Turan architectures logically separate.

---

## 1. The actual dependency graph

The project is a typed directed hypergraph, not a linear proof tree.

```text
RH
`-- global Weil positivity                         [RH-equivalent]
    `-- actual-zeta adjacent-support/source
        identification or Schur estimate           [OPEN]

fixed strip of width 10^-6 near Re(s)=1            [separate milestone]
`-- DPA_P(c), c>.0189  AND  LTRAD_P(.0189,.001)
    |-- DPA_P sufficient high-tail route
    |   |-- frozen-hat low band through Y^.8392    [PROJECT-PROVED;
    |   |                                             imported gap input]
    |   `-- CA4 high band                           [OPEN]
    |       `-- scalar natural HL*(4) transfer      [REFUTED proof class]
    `-- source-conditioned finite-time return       [OPEN]

fixed strip -> RH                                  [NO ADAPTER]
```

Consequences that must remain visible:

- `CA4` is a sufficient child of one route to `DPA_P`, not a necessary child
  of the fixed strip and not a direct child of RH.
- Proving `CA4` would still leave `LTRAD_P` open.
- Proving both present QP/Turan locks would yield the contemplated fixed
  strip, not RH.
- Global Weil positivity remains the only RH-equivalent node currently
  connected by an imported equivalence.

The earlier tendency to narrate this graph as

```text
four-cycle -> strip -> RH
```

was the highest decision-tree error.  There is no such proved path.

---

## 2. Statements, engines, and adapters are different objects

The following distinction prevents a large fraction of the project's false
progress reports.

| Desired statement | Available proof engines | Missing adapter or arithmetic input |
|---|---|---|
| global Weil positivity | Galerkin certification, Friedrichs extensions, Schur complements, positive-definite extension | adjacent-support positivity for the **actual** completed-zeta cross block |
| `CA4` | semiprime expansion, large sieve, delta/circle methods, conditional natural `HL*(4)` template | the exact adjacent-gap mask, all signed mixed terms, common translated kernel, and `H=Y^2/T` resolution |
| `LTRAD` | large sieve, Kronecker density, convex compression, exact-energy theorems | adaptive source-normalized one-sided return by time `Y^(50/33)` |
| fixed strip | Turan and phase-localization machinery | both `DPA_P` and `LTRAD_P`, or a new coupled substitute |
| RH | Weil equivalence, formal reductions, zero-density or moment certificates | global Weil positivity or a different complete RH implication |

Lean, Arb, SDP, Galerkin, delta methods, and theorem provers are engines or
verification artifacts.  They upgrade confidence in exact premises and
deductions.  They do not manufacture a missing analytic premise.

---

## 3. Arithmetic provenance and the exact descent test

### 3.1 Structured objects

Represent a theorem input by

\[
 x=(\text{formula},\text{source},\text{mask},\text{cone},
 \text{normalization},\text{quantifiers},\text{window},
 \text{floor},\text{resolution},\text{rate},\text{socket}).       \tag{3.1}
\]

A forgetful map `U:X->B` deletes some fields or replaces them by coarse
summaries.  Examples include:

- retaining only local Weil restriction and forgetting the global zeta
  continuation;
- replacing adjacent-gap hats by a natural prime weight;
- retaining a carrier operator and forgetting the legal source event;
- retaining an exact energy count and forgetting the required near-equality
  resolution;
- retaining coefficient mass or density and forgetting its signed geometry.

The target is a real functional `T:X->R`, a truth-valued property, or a norm
bound.  The question “does the desired theorem descend through `U`?” has an
exact answer.

### 3.2 Fiber-diameter lemma

For a nonempty fiber `X_b=U^(-1)(b)`, put

\[
 \operatorname{osc}_b(T)
 =\sup_{x,x'\in X_b}|T(x)-T(x')|.                  \tag{3.2}
\]

**Lemma 3.1 (real approximate descent).**  Let `epsilon>=0`.  There is a function
`Tbar:B->R` such that

\[
 |T(x)-\overline T(Ux)|\leq\varepsilon
 \quad\hbox{for every }x\in X                         \tag{3.3}
\]

if and only if every fiber range is bounded and

\[
 \operatorname{osc}_b(T)\leq2\varepsilon             \tag{3.4}
\]

for every `b` in the image of `U`.

**Proof.**  Equation (3.3) puts the whole fiber range inside an interval of
length `2 epsilon`, proving necessity.  Conversely choose `Tbar(b)` to be
the midpoint between the fiber infimum and supremum.  Equation (3.4) gives
(3.3).  Empty fibers are irrelevant.  QED

Exact descent is the case `epsilon=0`: `T` must be constant on every fiber.
For a truth-valued target, one positive and one negative object in a single
licensed fiber immediately rule out factorization through `U`.

Lemma 3.1 is the exact test for reconstructing a two-sided scalar value.  A
one-sided theorem needs the corresponding one-sided envelope, not small
diameter.  For an upper bound the optimal descended target is

\[
 T^\uparrow(b)=\sup_{Ux=b}T(x),                       \tag{3.5}
\]

and for a lower bound it is `T^downarrow(b)=inf_(Ux=b) T(x)`.  Large fiber
diameter alone does not refute `T(x)<=B(Ux)` if the entire fiber still lies
below `B`.  A valid upper-bound countermodel must push `T^uparrow` across the
claimed threshold; a lower-bound countermodel must push `T^downarrow` below
it.  Relative to a chosen section `s`, the relevant upper reconstruction
defect is `sup_(Ux=b)(T(x)-T(s(b)))`, and analogously for a lower theorem.

For approximate summaries, define the **provenance modulus**

\[
 \omega_{T|U}(r)
 =\sup\{|T(x)-T(y)|:d_B(Ux,Uy)\leq r\}.             \tag{3.5a}
\]

Its value at zero is the identifiability obstruction; its growth as
`r downarrow 0` measures stability and conditioning.  One-sided versions
replace the absolute difference by the directed defect appropriate to an
upper or lower theorem.  This separates two failures that were previously
conflated: natural-mask transfer has a nontrivial vertical obstruction
already at `r=0`, whereas a unique reconstruction can have zero vertical
oscillation but an unusably steep modulus.

This lemma does not refute a theorem using extra arithmetic input.  It says
exactly what the extra input must do: shrink the licensed fiber, choose a
canonical section, or control the relevant two-sided oscillation/one-sided
envelope inside it.

### 3.3 The Mass--Identifiability--Stability audit

Every proposed adapter must pass three separate tests.

1. **Mass (M).**  The retained or transported object carries `1-o(1)` of the
   target norm or mass at the target normalization.
2. **Identifiability (I).**  Licensed fibers of the forgotten representation
   have two-sided target oscillation, or the relevant one-sided envelope,
   inside the error budget.
3. **Stability (S).**  A section or reconstruction exists with condition
   number, component count, resolution distortion, and exponent loss inside
   every downstream budget.

Passing identifiability without stability is not enough: a unique inverse
may be too ill-conditioned to preserve a fixed-power estimate.  Passing
stability on an `o(1)`-mass truncation is also irrelevant.

The recent failures classify cleanly:

| Route | M | I | S | Verdict |
|---|---:|---:|---:|---|
| Yang--Yang polylog-modulus truncation | fail | not reached | not reached | normalized conductor mass is lost |
| scalar natural-mask transfer to `CA4` | pass only after retaining gaps | fail | fail | bounded-density fibers change the band fourth moment; actual variation costs `>>(log Y)^-4` versus a fixed-power budget |
| abstract positive extension of local Weil kernel | pass | fail | not reached | many positive completions need not equal the zeta continuation |
| source-free compression for `LTRAD` | pass | fail | fail | source orientation changes the quotient norm; `B^-1` return is unstable |
| exact-energy import to translated contact | pass | fail unless mask retained | fail | exact equality does not preserve `H=Y^2/T` near-equality resolution |
| fixed strip to RH | n/a | n/a | n/a | no adapter has been supplied |

For two-sided reconstruction, the decisive hostile check is

\[
 \sup_{Ux=Uy}|T(x)-T(y)|
 \leq \hbox{available reconstruction error}.          \tag{3.6}
\]

For an upper or lower theorem, replace (3.6) by the corresponding fiber
envelope above and require the fiber to straddle the claimed bound.  If that
test fails in a countermodel satisfying every hypothesis actually used by
the proposed engine, the proof class is closed.  A lower-fidelity model only
identifies which omitted arithmetic property might matter; it does not
refute the arithmetic theorem.

---

## 4. The costed category of theorem passports

Category theory is useful here as type discipline, not as an analytic proof.

Let objects be theorem statements together with complete passports of the
form (3.1).  A morphism `A->B` is a *proved* implication or adapter, not a
verbal resemblance.  Identities are tautological implications and
composition is logical composition.  Attach to each morphism the resource
record

\[
 c(f)=(e_{\rm exp},e_{\rm mass},e_{\rm comp},e_{\rm res};\,D),   \tag{4.1}
\]

where the nonnegative numerical coordinates record exponent, mass, component, and
resolution losses, and `D` is the set of unresolved provenance obligations.
For composable adapters without a reconstruction certificate, define the
**syntactic accumulated ledger** by

\[
 c_{\rm led}(g\circ f)
 =(e(f)+e(g);\,D(f)\cup D(g)).                       \tag{4.2}
\]

This is equality because the ledger records what that displayed route spent.
If `c_min` denotes the best semantic cost of the composite, only the lax
inequality

\[
 c_{\min}(g\circ f)\preceq c_{\rm led}(g\circ f)      \tag{4.3}
\]

is justified: a direct proof or cancellation may improve the composite.

A separately proved canonical section, fiber-diameter theorem, or stable
reconstruction may discharge a field from `D`; it must appear as its own
morphism with a proof and a budget.  A better numerical exponent cannot by
itself recover a mask or source label.

With certified recoveries, the provenance component is more accurately a
three-state ordered transition system—present, unresolved, or recovered—than
a bare union monoid.  Composition is order-sensitive: a later recovery can
close an obligation, and a still later forgetting reopens it.  The replay
code checks associativity of this transition law exhaustively for one field.

Thus the repository has an ordinary path category of proved adapters with an
additive ordered monoid for numerical costs and the three-state transition
monoid for provenance obligations.  The debt-only fragment reduces to
addition/union.  Alternative proofs can be compared on a Pareto frontier.
Nothing in that language proves that a low-cost morphism exists; it prevents
composition from hiding its price.

Two practical consequences follow.

1. “Same asymptotic scale” means two objects have one matching coordinate.
   It does not construct a morphism between them.
2. A route is complete only when its terminal passport exactly matches the
   target and its composite resource record fits every budget.

The script linked above checks the elementary associativity-compatible loss
composition with exact rational exponents.  It deliberately permits a field
to be discharged only by an explicitly recorded certified recovery.

### 4.1 Provenance fibers

For every coarse object `b`, let `X_b` be the category or set of structured
arithmetic refinements above it.  The disjoint union of these fibers projects
to the coarse base.  This is safely called a **fibered model**.  It becomes a
Grothendieck fibration only after coherent reindexing functors along base
morphisms have actually been specified; the project has not proved such
data, so “arithmetic provenance fibration” should remain a design proposal,
not a theorem.

Useful descent can occur in four ways:

- the arithmetic hypotheses prove that the target object lies in the image
  of a canonical section, and the estimate holds on that section;
- the target has small diameter throughout the fiber;
- explicit coherence data controls the cross terms between local sections;
- a stable reconstruction theorem recovers the forgotten field within the
  resource budget.

Every credible new adapter should name which of these mechanisms it uses.

### 4.2 Restriction of labelled diagrams

A more precise categorical model represents a live object by a small labelled
diagram `F:J->C`.  A subdiagram inclusion `i:J_0->J` induces restriction

\[
 i^*:\mathcal C^J\longrightarrow\mathcal C^{J_0}.    \tag{4.4}
\]

The failed simplifications restrict away exactly one load-bearing arrow or
point:

| Branch | Deleted part of the diagram |
|---|---|
| Weil | the source-labelled old/new cross arrow `C` |
| `CA4` | the marked multiplier/vector over the natural marginal |
| `LTRAD` | the distinguished point `v:1->V` and its source event |

The familiar theorem acts on the restricted diagram.  When the relevant
left/right Kan extension or positive completion exists, it can supply
possible lifts, but generally not the arithmetic lift.  Lemma 3.1 says the
target functional/functor on
`C^J` does not factor, even approximately at the required scale, through
`i^*` unless the appropriate fiber condition holds.

This refines, rather than replaces, the project's earlier categorical work:

- [`CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`](CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md)
  developed ordered norm-enriched Hermitian fibers and probe-cone descent;
- [`ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`](ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md)
  recorded signatures, costs, cross-effects, sparse-defect quotients, and the
  first-nonformal-node rule;
- [`ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`](ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md)
  already emphasized same-local-data/different-global-order examples and
  cross rectangles;
- [`CATEGORICAL-ADMISSION-TESTS-EXECUTION-SYNTHESIS-2026-08-12.md`](CATEGORICAL-ADMISSION-TESTS-EXECUTION-SYNTHESIS-2026-08-12.md)
  executed an earlier admission policy, although its carrier-slice priority
  was later pruned.
- [`ZETA23-BELLMAN-REWARD-SAMPLING-2026-08-30.md`](ZETA23-BELLMAN-REWARD-SAMPLING-2026-08-30.md)
  already formulated typed-DAG, information-gain, and long-horizon reward
  discipline; the present M/I/S test supplies a sharper local reward and
  falsifier for each adapter edge.

The present contribution is to attach those abstractions to the corrected
2026-08-31 graph, the natural-mask falsifier, exact one-sided fiber envelopes,
and the M/I/S audit.  It should not be presented as the first categorical
formulation in the project.

---

## 5. One common form: pointed relative energies

The strongest unification is not that Weil, `CA4`, and `LTRAD` are the same
problem.  It is that each target depends on a distinguished arithmetic
direction that the failed simplification forgets.

### 5.1 Weil: a source-labelled Schur complement

For an old/new support decomposition, write the actual zeta form as

\[
 Q_b=\begin{pmatrix}A&C\\ C^*&D\end{pmatrix}.         \tag{5.1}
\]

In finite dimensions,

\[
 Q_b\succeq0
 \quad\Longleftrightarrow\quad
 A\succeq0,\quad (I-AA^\dagger)C=0,\quad
 D-C^*A^\dagger C\succeq0.                           \tag{5.2}
\]

If `A>0`, the range condition disappears and the last term is the ordinary
Schur complement.  Equivalently, the cross block factors as

\[
 C=A^{1/2}KD^{1/2},\qquad \|K\|\leq1.                \tag{5.3}
\]

The restrictions `A,D` do not determine positivity: with `A=D=1`, the lift
is positive exactly when `|C|<=1`.  Abstract positive-definite extension
selects *some* admissible `C`; it does not identify the completed-zeta `C`.
For a possibly singular old block, the live source-labelled invariant is the
pair

\[
 \left((I-AA^\dagger)C,\quad
 S_\zeta=D-C^*A^\dagger C\right).                    \tag{5.4}
\]

### 5.2 `CA4`: a multiplier-labelled Gram energy

Let `V_T` synthesize the semiprime phases on `[T,2T]`, and put
`G_T=V_T^*V_T`.  If `c_eta` is a natural semiprime coefficient vector and
the adjacent-gap multiplier produces

\[
 c_\lambda=D_\rho c_\eta,                            \tag{5.5}
\]

then the target is

\[
 E_\rho=\langle D_\rho c_\eta,G_TD_\rho c_\eta\rangle. \tag{5.6}
\]

A scalar natural theorem controls only
`<c_eta,G_T c_eta>`.  If `c_lambda=alpha c_eta+z` with
`z perpendicular to c_eta`, then

\[
 E_\rho=|\alpha|^2\langle c_\eta,G_Tc_\eta\rangle
 +2\Re\!\left(\bar\alpha\langle c_\eta,G_Tz\rangle\right)
 +\langle z,G_Tz\rangle.                             \tag{5.7}
\]

Mass, bounded density ratio, and positivity of `G_T` do not determine the
last two terms.  The bounded-density periodic motif and the actual-prime
variation certificate make that failure quantitative.

### 5.3 `LTRAD`: a source-labelled quotient norm

For the prime carrier operator

\[
 A_Yy(t)=y\cdot a_P(t),\qquad
 h_Y(y)=\|A_Yy\|_\infty,                             \tag{5.8}
\]

and the legal event source `v`, the transverse quantity is

\[
 s_v=\inf_{y\cdot v=-1}h_Y(y)
     ={1\over\|v\|_{h_Y,*}},                         \tag{5.9}
\]

with the usual extended-value conventions.  This is an exact scaling/duality
identity.  `LTRAD` is a bound on the observability of the distinguished
source vector, not merely a frame estimate for `A_Y`.

For example,

\[
 h(y)=\max(\varepsilon|y_1|,|y_2|)                   \tag{5.10}
\]

has identical carrier data for both unit sources, while

\[
 s_{e_1}=\varepsilon,\qquad s_{e_2}=1.               \tag{5.11}
\]

Forgetting source orientation therefore has order-one fiber oscillation.

### 5.4 The common invariant and its limit

All three are **pointed relative energies**:

| Branch | Unpointed carrier | Arithmetic point/section | Target invariant |
|---|---|---|---|
| Weil | old/new diagonal forms | actual zeta cross block | range defect plus Schur complement `S_zeta` |
| `CA4` | natural semiprime Gram operator | adjacent-gap multiplier | `<D_rho c,G_TD_rho c>` |
| `LTRAD` | prime carrier operator | legal event source `v` | `1/||v||_*` |

This abstraction predicts where the real information lives: a pointed mixed
interaction, often a signed off-diagonal coherence.  In `LTRAD` it is more
accurately the orientation of the source relative to a one-sided finite-time
orbit.  Diagonal mass, trace, density, and unpointed frame data are
deliberately insensitive to these distinctions.

It does **not** give a common proof.  The Weil branch needs an upper
contractivity/positivity statement, `CA4` needs a sharp upper fourth-energy
bound, and `LTRAD` needs a lower finite-time observability statement.  The
directions, quantifiers, and arithmetic sources differ.

---

## 6. The ordered-prime chain complex and its product lift

### 6.1 What was already known

Let

\[
 v_1<\cdots<v_N,qquad C_1\xrightarrow{\partial}C_0
 \xrightarrow{\epsilon}\mathbb R\to0               \tag{6.1}
\]

be the oriented path on the prime-log nodes, where `epsilon` sums vertex
coefficients.  The project's earlier
[`ZETA23-PRIME-GRAPH-DIFFUSION-AND-ADJACENT-PAIR-TAIL-GATE-2026-08-13.md`](ZETA23-PRIME-GRAPH-DIFFUSION-AND-ADJACENT-PAIR-TAIL-GATE-2026-08-13.md)
proved

\[
 \operatorname{im}\partial=\ker\epsilon.             \tag{6.2}
\]

Thus adjacent-edge flux coordinates parameterize **every** same-mass
coefficient change.  Without a new norm or arithmetic restriction, changing
to flux coordinates is not a reduction.

Apply this to the normalized retained hat vector `lambda` and normalized
natural shell vector `eta`.  Both have mass one, so

\[
 \delta:=\lambda-\eta=\partial c,qquad
 c_j=\sum_{k\leq j}\delta_k                            \tag{6.3}
\]

for a unique oriented edge flux `c`.  With
`z_j(t)=exp(itv_j)`, summation by parts gives

\[
 M_\delta(t)
 =\sum_{j<N}c_j\bigl(z_j(t)-z_{j+1}(t)\bigr)
 =\sum_{j<N}c_jz_j(t)\bigl(1-e^{it\Delta_j}\bigr).    \tag{6.4}
\]

Hence every edge earns the exact derivative factor

\[
 |1-e^{it\Delta_j}|\leq\min(2,|t|\Delta_j).           \tag{6.5}
\]

For retained gaps `g_j<=G=Y^(163/1000)`, the worst-case transition
`t Delta_j asymp 1` occurs near

\[
 t\asymp Y/G=Y^{837/1000}.                            \tag{6.6}
\]

This is close to the existing low/high split, with the frozen-hat low band
proved through `Y^.8392`.  It explains why discrete integration by parts is
useful at low height and why its trivial gain saturates in the residual band
up to `Y^(50/33)`.  It does not reproduce the low-band proof or control the
high band by itself.

### 6.2 The symmetric-square/product-boundary identity

Put `s=lambda+eta`.  Polarization collapses the apparently many mask
components to two channels:

\[
\begin{aligned}
 A:=\lambda\otimes\lambda-\eta\otimes\eta
  &={1\over2}(\delta\otimes s+s\otimes\delta)\\
  &=\partial_1\!\left({c\otimes s\over2}\right)
    +\partial_2\!\left({s\otimes c\over2}\right).   \tag{6.7}
\end{aligned}
\]

Equivalently, set `r_i=delta_i/s_i` wherever `s_i>0`.  Positivity gives
`|r_i|<=1`, while equality of total masses gives the exact balance law

\[
 \sum_i s_i r_i=\sum_i\delta_i=0.
\]

Moreover,

\[
 A_{ik}={1\over2}s_is_k(r_i+r_k).                    \tag{6.8}
\]

Thus the semiprime selector discrepancy has matrix rank at most two and is
an additive lift of one bounded, `s`-balanced vertex color.  The earlier three-term
expansion into `delta tensor eta`, `eta tensor delta`, and
`delta tensor delta` is correct but nonminimal.  Equation (6.7) is the exact
compression of the vague phrase “a large vector-valued masked theorem” to
one signed edge channel and one positive vertex channel.

Let `Pi` push an ordered prime pair `(p_i,p_j)` to its product `p_i p_j`, and
let

\[
 \mathcal S_T(A)(t)=\sum_{i,j}A_{ij}e^{it(v_i+v_j)}.
\]

Unique factorization and linearity give the exact semiprime discrepancy

\[
 M_\lambda(t)^2-M_\eta(t)^2
 =M_\delta(t)M_s(t)
 =\mathcal S_T\!\left(
   \partial_1{(c\otimes s)\over2}
   +\partial_2{(s\otimes c)\over2}\right).           \tag{6.9}
\]

More generally, the degree-`k` tensor finite difference telescopes as

\[
 \lambda^{\otimes k}-\eta^{\otimes k}
 =\sum_{a=0}^{k-1}
   \lambda^{\otimes a}\otimes\delta
   \otimes\eta^{\otimes(k-1-a)}.                    \tag{6.9a}
\]

After Fourier evaluation this is just the divided-difference factorization
of `M_lambda^k-M_eta^k`.  It generalizes the two-channel viewpoint to higher
moments without importing any higher-order estimate.

The replay script verifies the path identity, the three-term product
boundary, and the two-channel polarization over exact rational arithmetic.
These are elementary tensor identities; no claim of literature-level novelty
is made for the algebra itself.

The semiprime coefficient diagonal of the difference is also exact.  If
`d(n)=a_lambda(n)-a_eta(n)`, then

\[
 \mathcal D(\delta,s):=\sum_n|d(n)|^2
 =\|\delta\|_2^2\|s\|_2^2
  +|\langle\delta,s\rangle|^2
  -\sum_i\delta_i^2s_i^2
 \leq2\|\delta\|_2^2\|s\|_2^2.                     \tag{6.10}
\]

Current diagonal information gives

\[
 \mathcal D(\delta,s)\ll Y^{-2q+o(1)},
 \qquad q={2787\over3250}.                           \tag{6.11}
\]

The diagonal is therefore affordable.  The unresolved object is the
translated off-diagonal contact.

### 6.3 What homology does and does not buy

The two probability vectors represent the same class in

\[
 H_0(C_\bullet)\cong\mathbb R.                       \tag{6.12}
\]

Their symmetric squares also agree after passing to product homology.  But
the translated fourth-moment kernel is a chain-level energy, not a homology
invariant.  It can assign radically different energies to representatives
of the same class; the bounded-density periodic motif demonstrates exactly
that.

This is the key limitation of the homological abstraction:

> Every pair of probability vectors on an ordered support differs by a
> boundary.  Therefore exactness has no arithmetic content until one controls
> the flux in a norm seen favorably by the oscillatory semiprime operator.

In categorical language, symmetric squaring itself is not failing to commute
with a linear map.  The defect comes from replacing one structured lift
`lambda` by a chosen coarse section `eta`; equation (6.7) measures that
section/reconstruction error.

### 6.4 The honest theorem-shaped consequence

The weakest direct transfer estimate would be

\[
 \|M_\lambda^2-M_\eta^2\|_{L^2(T,2T)}
 \ll T^{1/2}Y^{-q+1/20+o(1)},
 \qquad q={2787\over3250}.                            \tag{6.13}
\]

Combined with a natural estimate at the same scale, (6.13) implies `CA4` by
the triangle inequality.  Rewriting (6.13) using (6.9) is an exact normal
form, not yet a smaller theorem.  It becomes a research reduction only if a
new lemma bounds the product boundary from strictly weaker flux data already
known for actual consecutive primes.

The most precise conditional interface is the diagonal-relative mixed large
sieve

\[
 \int\psi(t/T)|M_\delta(t)M_s(t)|^2dt
 \ll T Y^{1/10+o(1)}\mathcal D(\delta,s).             \tag{6.14}
\]

Call this `PG-EF(1/10)`.  It is narrower than arbitrary-coefficient
four-cycle because the ordered semiprime color is the fixed additive
rank-two form (6.8).  It is an open diagonal-relative strengthening of the
direct discrepancy target (6.13), and can be strictly stronger when
`D(delta,s)=o(Y^(-2q))`.  The algebra alone does not make it easier; its
right side still needs an independently proved flux/correlation theorem.

An alternative sufficient input, given the natural `eta` bound, is the
existing difference-measure target

\[
 \int_T^{2T}|M_{\lambda-\eta}(t)|^4dt
 \ll T Y^{-2q+1/10+o(1)}.                            \tag{6.15}
\]

For the mixed energy (6.14), squaring the one-divergence form and summing by
parts moves one edge difference onto each leg of the contact kernel.  The
gain is only `min(1,T Delta_e) min(1,T Delta_e')`; it saturates in the open
band.  The alternative fourth moment (6.15) has a double boundary on each
coefficient side and therefore four finite-difference factors, which also
saturate.  At the top endpoint even a physical gap of two has
`T Delta >> Y^(17/33)`.

The bounded-gap four-point pseudonode motif supplies a sharp warning.  It has
`||c||_infinity=O(N^-1)`, `||c||_2^2=O(N^-1)`, transport distance `O(N^-1)`,
and product `H^-1` energy `O(N^-2)`, yet at a legal resonant height

\[
 M_\delta(t)M_s(t)=1/16.                             \tag{6.16}
\]

With `N asymp Y/log Y`, the right side proposed in (6.14) tends to zero.
Thus boundary status, transport, a phase-weighted edge square function, and
minimal product `H^-1` norm do not imply the theorem in the licensed soft
pseudonode class.  An actual-prime proof must use non-aliasing or marked
selector correlation beyond graph topology.

The complete derivation and exponent audit are in
[`ZETA23-CA4-EDGE-FLUX-PRODUCT-GRAPH-AND-TWO-CHANNEL-AUDIT-2026-08-31.md`](ZETA23-CA4-EDGE-FLUX-PRODUCT-GRAPH-AND-TWO-CHANNEL-AUDIT-2026-08-31.md).

---

## 7. A general dual obstruction principle

Many no-go proofs in the repository are instances of one elementary lemma.
Let a dictionary `D` have atom costs `w(d)`, and let

\[
 \|x\|_{\mathcal A}
 =\inf\left\{\sum_i|a_i|w(d_i)+\|r\|_R:
 x=\sum_i a_id_i+r\right\}.                          \tag{7.1}
\]

**Lemma 7.1 (dual adapter obstruction).**  If a linear functional `L`
satisfies

\[
 |L(d)|\leq w(d)\quad(d\in\mathcal D),
 \qquad |L(r)|\leq\|r\|_R,                           \tag{7.2}
\]

then

\[
 \|x\|_{\mathcal A}\geq|L(x)|.                      \tag{7.3}
\]

**Proof.**  Apply `L` to an arbitrary representation in (7.1), use (7.2)
and the triangle inequality, then take the infimum.  QED

For the scalar natural-mask `CA4` adapter, take the discrete sign witness

\[
 b=D^T\operatorname{sgn}(D\lambda),qquad B=bb^T.     \tag{7.4}
\]

Then `<B,lambda lambda^T>=V(lambda)^2`, while every permitted consecutive
natural interval atom pairs at its charged cost.  The project-proved
actual-prime variation theorem in the cited falsifier (analytic manuscript,
not a literature novelty claim) is

\[
 V(\lambda)\gg(\log Y)^{-2}                          \tag{7.5}
\]

This forces scalar decomposition cost `>>(log Y)^-4`, far larger than the
required `Y^(-5249/6500+o(1))` budget.  This is a dictionary-wide lower bound,
not a failure of one partition algorithm.

The methodological generalization is useful:

1. specify the exact atom dictionary and cost before constructing a
   decomposition;
2. search first for a dual functional that is cheap on every atom and large
   on the target;
3. stop the entire primal proof class if the dual lower bound exceeds the
   downstream budget.

This turns many months of serializer optimization into a finite obstruction
search.  It also clarifies the escape: retain the components jointly so that
the signed sum is formed before the norm; the scalar atomic gauge is then no
longer the relevant cost.

---

## 8. The adjacent-gap mark filtration

The natural and hat measures are not small perturbations in the statistic
that matters.  Write on the common retained support

\[
 \lambda_j=\eta_j(1+\kappa_j),
 \qquad \sum_j\eta_j\kappa_j=0.                      \tag{8.1}
\]

Here `kappa_j` records the local two-sided cell or adjacent-gap mark.  In a
finite-shell point-process analogy, `eta` samples a typical prime point,
whereas the Voronoi/hat mass weights a prime by the amount of nearby physical
volume assigned to it.  This is a Palm-versus-size-biased intuition, not an
asserted limiting point-process theorem.

For the translated fourth-energy kernel, define

\[
 \mathcal E_K(w)
 =\sum_{i,j,k,l}w_iw_jw_kw_l
 K(v_i+v_j-v_k-v_l).                                 \tag{8.2}
\]

Substituting (8.1) gives an exact expansion by mark degree:

\[
 \mathcal E_K(\lambda)
 =\sum_{r=0}^4 \mathcal E_K^{[r]}(\eta,\kappa),       \tag{8.3}
\]

where grade `r` is the sum of the terms with `r` inserted `kappa` factors.
Grade zero is the natural-weight object appearing in the matching or
conditional `HL*(4)` input from the literature.  Grades one through four
retain the adjacent-gap selector and are not controlled by a scalar natural
theorem.

Equation (8.3) is only a mark-count expansion, not yet a cumulant expansion.
The centering in (8.1) kills the one-mark term only for a constant kernel; it
does not kill the translated contact term.  A genuine connected/cumulant
decomposition would require a specified probabilistic ensemble and proved
mixing input.

There is, however, a better exact coordinate for the square difference.  The
unbounded relative mark `kappa` is transformed to the bounded contrast

\[
 r_i={\lambda_i-\eta_i\over\lambda_i+\eta_i}
     ={\kappa_i\over2+\kappa_i},
 \qquad |r_i|\leq1,\qquad \sum_i s_ir_i=0,           \tag{8.4}
\]

where `s=lambda+eta`.  Polarization repackages the **square coefficient
difference** into the single additive color `r_i+r_j` in (6.8), allowing the
Minkowski transfer route to bypass a grade-by-grade proof.  It does not
literally resum the full fourth-energy difference.  If `G` is the semiprime
Gram operator, then

\[
 \mathcal E_K(\lambda)-\mathcal E_K(\eta)
 =\Re\langle A,G(\lambda\lambda^T+\eta\eta^T)\rangle,
 \quad
 (\lambda\lambda^T+\eta\eta^T)_{ij}
 ={s_is_j\over2}(1+r_ir_j).                         \tag{8.4a}
\]

Thus an even color remains in a direct energy comparison.  The
bounded-contrast coefficient representation is nevertheless better
conditioned than truncating `lambda/eta`: it preserves all mass, and the
representation itself pays no `Y^theta` density-ratio supremum.  The periodic
motif shows that boundedness and centering alone still do not control the
high-band contact.

This filtration suggests a disciplined experiment: locate the first mark
grade that violates the natural bound in actual-prime and licensed hostile
models.  If grades one and two admit kernel-averaged estimates while grade
four fails, the target theorem can be localized.  If grade one already
carries the obstruction, higher combinatorial decompositions are a dead end.

The gap mark has genuinely higher-order arithmetic content.  For `p` already
assumed prime, the exact successor identity is

\[
 {\bf1}_{p^+-p=g}
 ={\bf1}_{\mathbb P}(p+g)
 \prod_{1\leq h<g}(1-{\bf1}_{\mathbb P}(p+h))        \tag{8.5}
\]

This identity contains both a prime endpoint and the emptiness of the entire intervening
interval.  Natural `Lambda*Lambda` correlations see endpoints and products,
not that unbounded-order emptiness selector.

The credible `CA4` theorem families are therefore:

- a kernel-averaged marked `HL*(4)` theorem for the specific local cell mark;
- a two-channel edge-contact theorem acting on the single mixed product in
  (6.9);
- actual-gap twisted four-distinct semiprime dispersion, with the common
  translated kernel kept until after signed recombination;
- determinant dispersion or a sieve empty-interval identity that converts
  (8.5) into cancellation without scalarizing the mark.

Arbitrary-multiplier stability would also imply the target, but is much
stronger than necessary and risks spending the full density-ratio exponent.
The actual mark and the common kernel should be built into the statement.

---

## 9. `LTRAD` as pointed finite-time observability

The quantifier structure is

```text
for every legal negative source event E,
for every source-normalized adaptive separator y,
there exists t in the prescribed finite band
with the required one-sided return.
```

Generic large-sieve or covariance theorems average over `t` after the source
direction has been forgotten.  Kronecker density treats each fixed vector
but gives no uniform return time for an adaptively varying family.  Neither
determines (5.9).

The next high-information experiment is a **source-fiber bifurcation**:

1. derive every exact joint restriction imposed by a legal event on
   `(v,y,A_Y)`, preserving signs, normalization, adaptation, and quantifier
   order;
2. ask whether the existing prime-density pseudo-node models can realize all
   those restrictions while making `s_v` too small;
3. if yes, close the entire soft-geometry proof class;
4. if no, isolate the first violated condition and promote only that condition
   as a candidate prime-specific invariant.

This is preferable to proposing another source-free frame theorem.  Either
outcome changes the decision graph.

There is one further abstraction worth retaining.  The present strip proof
splits into an upper universal radius bound and a lower event-conditioned
return bound.  A single event-conditioned separator certificate could, in
principle, close the contradiction without proving the strongest independent
versions of both `DPA_P` and `LTRAD_P`.  No such coupled certificate is known;
the point is to keep that logical option visible rather than optimize one
side of an unnecessarily strong AND gate forever.

---

## 10. Weil positivity as arithmetic descent

The local-to-global problem is not a sheaf-local positivity problem.  On an
overlap, local diagonal restrictions do not determine the polarization
between old and new directions.  The cross block in (5.1) is descent data.

The exact adjacent-support target is either the Schur estimate

\[
 C_{a,b}^*Q_a^\dagger C_{a,b}\preceq N_{a,b},         \tag{10.1}
\]

together with its range condition, or the equivalent contraction
factorization.  An absolute estimate on `||C_{a,b}||` is inadequate when the
floor of `Q_a` collapses; (10.1) must be relative to the near-null old
direction and exploit the exact prime-power, pole, and archimedean source.

A noncircular source-identifying alternative must separate identification
from positivity.  Let `A_b` be an affine family cut out by proved
completed-zeta source recurrences, and put

\[
 \mathcal F_{a,b}
 =\{Q\in\mathcal A_b:R_{ba}Q=Q_a\}.                  \tag{10.2}
\]

It would be enough to prove, independently,

\[
 \mathcal F_{a,b}=\{Q_b^\zeta\}
 \quad\hbox{and}\quad
 \exists\widetilde Q\in\mathcal F_{a,b}
       \text{ with }\widetilde Q\succeq0.            \tag{10.3}
\]

Then `Qtilde=Q_b^zeta`.  The first clause is source uniqueness without a
positivity predicate; the second is positive completion inside the same
source-constrained fiber.  Positive completion without uniqueness selects
an arbitrary positive-definite completion.  Uniqueness that merely encodes
the unknown actual cross block, or positive existence that presupposes zeta
positivity, is circular and earns no reduction credit.

Prior project work also shows why fixed-core strong-resolvent convergence is
not an identifying replacement.  Under RH, every finite extension phase has
the same generalized strong-resolvent limit on the eventual compact core,
while the boundary defect vectors weakly escape.  The topology deliberately
forgets the phase-carrying data.  A live limit route must retain a stronger
boundary Weyl, Clark, characteristic, determinant, or norm-resolvent
invariant and avoid assuming the positive ambient space it seeks to prove.
See
[`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md).

The concrete next experiment remains:

1. independently certify or refute Chuk's claimed local `a=.8` positivity;
2. at the first adjacent `p=5` activation, compute the exact source-labelled
   old/new Schur complement and the face of positive completions;
3. test whether completed-zeta recurrences expose a unique point of that face
   or directly bound (10.1).

This is the highest direct-information route toward the only current
RH-equivalent edge.  It is separate from the fixed-strip program.

---

## 11. Higher abstractions that genuinely generalize

### 11.1 Relative information, not local information

The target usually lives in a *relation* between old and new, natural and
marked, or source and orbit.  Proving stronger facts about either endpoint
separately can leave that relation completely free.  This explains why so
many positive diagonal, density, energy, and extension theorems were real
mathematics yet irrelevant to the final socket.

### 11.2 Compression must follow excess

Compression, serialization, low rank, and category reduction are valuable
only after an inequality creates quantitative excess or a stable margin.
Before that, a coordinate change often parameterizes the original space:
path fluxes span every zero-mass vector, affine compression can restate the
same optimizer, and Schur complementation can merely name the missing floor.

### 11.3 Resolution is part of the topology

Exact equality, coarse congruence, averaged phase, and translated contact at
`H=Y^2/T` are different topologies on coefficient data.  A theorem continuous
in one need not be stable in another.  “Resolution loss” belongs in the
adapter object itself, not in an afterthought error term.

### 11.4 Absolute values are quotient maps with large fibers

Taking absolute values, positive mixtures, scalar norms, or traces deletes
signed interference.  The missing term in all three architectures is often
exactly what that quotient removes.  Before applying an inequality
componentwise, run the appropriate fiber-diameter or one-sided-envelope test
on the sign-forgetting map.

### 11.5 Countermodels identify missing provenance

A countermodel should be read as a classifier:

- if it satisfies the full target passport, it refutes the theorem;
- if it satisfies only the proof engine's hypotheses, it refutes that proof
  class and names the arithmetic datum the engine omitted;
- if it merely resembles the target, it is an intuition pump only.

This prevents both overclaiming a synthetic refutation and ignoring its
legitimate information.

### 11.6 The reconstruction problem is often the theorem

When a literature result lives on a coarse quotient and the project target
lives on a labelled lift, the “adapter” is not routine plumbing.  Stable,
source-faithful lifting can be exactly as hard as the desired theorem.  It
must be given a name, passport, falsifier, and cost of its own.

### 11.7 Vertical symmetries accelerate falsification

If `g:X->X` is a vertical automorphism with `U(gx)=U(x)`, every exactly
descended target must satisfy `T(gx)=T(x)`.  For an upper or lower theorem,
the orbit of `g` contributes to the corresponding fiber envelope.  Searching
for vertical symmetries is often faster than constructing arbitrary pairs:

- vary the Weil cross block while fixing both diagonal restrictions;
- rotate the `LTRAD` source in a fixed carrier geometry;
- vary adjacent-gap marks while fixing the natural marginal and soft density
  data.

This is the group-action version of the fiber falsifier.  The arithmetic
theorem must break or control precisely those vertical symmetries.

### 11.8 Statistical sufficiency is an equally useful language

Deterministically, `U(x)` is a statistic of the full arithmetic object.  The
question whether it retains enough information for `T` is a Blackwell-style
sufficiency question; a stable adapter is a well-posed decoder.  Fiber
countermodels prove non-sufficiency, and a dual witness supplies a separating
decision loss.  In this language M/I/S becomes:

```text
carrier retention + target sufficiency + Hadamard stability.
```

This is not a probabilistic theorem about primes.  It is a clean explanation
of the data-processing obstruction: once the proof has discarded a source,
mask, or phase, recovering it requires new information, not a more eloquent
use of the coarse statistic.

---

## 12. Hostile audit of the decision process

The main mistakes, ordered by height in the graph, were:

1. **Wrong root narrative.**  A small fixed strip was allowed to stand in for
   RH despite the absence of an amplifier.
2. **Premature four-cycle selection.**  The sharp endpoint was pursued before
   its exact strip adapter and exponent ledger were written.
3. **Silent inversion of forgetful maps.**  Natural masks, abstract positive
   extensions, and source-free carriers were treated as if their arithmetic
   lifts were automatic.
4. **Scale matching instead of passport matching.**  Literature theorems at
   the right `H` or conductor were treated as nearly applicable despite wrong
   masks, signs, quantifiers, or resolution.
5. **One-lock optimization.**  Work concentrated on `DPA/CA4` while the
   independent `LTRAD` lock remained open.
6. **Sufficient became necessary.**  `CA4`, diffuse positive antennas, and
   particular serializers were narrated as the route rather than one route.
7. **Compression before coercivity.**  New coordinates and decompositions
   were mistaken for a smaller feasible set before any excess estimate
   existed.
8. **Componentwise absolute values.**  Potentially useful common-kernel
   cancellation was destroyed before the arithmetic theorem was applied.
9. **Finite and synthetic evidence leakage.**  Diagnostics were occasionally
   allowed to influence asymptotic theorem status.

The replacement protocol is:

```text
write the typed dependency edge
-> fill the full passport and exponent budget
-> identify every forgotten field
-> run M/I/S and dual-fiber falsifiers
-> separate theorem statement from available engine
-> pursue only proof classes that survive
-> verify exact algebra
-> update theorem status only on a proved analytic premise.
```

---

## 13. Ranked research program

The ranking depends on which milestone is being optimized.

### 13.1 For the immediate fixed-strip target

1. **`LTRAD` source-fiber bifurcation.**  Highest information per unit effort.
   It either closes generic soft geometry or discovers the missing
   prime-specific invariant.
2. **Direct one-sided `DPA`/negative-excursion theorem.**  Formulate the
   weakest theorem that excludes the dangerous negative event, then test it
   on bounded-gap Bragg and prime-density models.  This may bypass `CA4`.
3. **Marked product-boundary `CA4`.**  Use (6.7)--(6.9) to design a joint
   signed, additive-rank-two theorem for the actual cell mark.  Do not return
   to scalar natural partitions.
4. **Event-conditioned common certificate.**  Explore only after the exact
   source restrictions are known; otherwise it simply renames both locks.

### 13.2 For the root goal RH

1. **Chuk certificate reproduction.**  This is the fast prerequisite and an
   independent truth check; a larger local seed alone still does not
   propagate globally.
2. **Weil `p=5` source-labelled Schur audit.**  Conditional on a certified
   adjacent seed, this probes the first open edge on the existing
   RH-equivalent route.
3. **Boundary-identifying global limit.**  Pursue only with a topology that
   retains the escaping source/phase data and without assuming RH positivity.

### 13.3 For `CA4` specifically

The best current mathematical bet is the combination

```text
centered actual gap mark / edge flux
      +
two-channel additive-color four-distinct determinant dispersion
      +
common translated kernel retained through recombination.
```

This is not yet a proof engine.  Its first falsifiable subtask is the
mark-degree audit in (8.3), followed by a search for a dual witness against
each proposed edge-flux square-function norm.  Only a norm surviving those
tests deserves a full analytic attack.

### 13.4 Hard stops

- Stop any truncation that loses a non-`o(1)` share of target mass.
- Stop any two-sided reconstruction with excessive licensed fiber
  oscillation, and any one-sided adapter whose licensed fiber envelope
  crosses the claimed threshold.
- Stop scalar natural-mask partitions for `CA4`; the dual variation theorem
  already closes them.
- Stop serializers that lose `H=Y^2/T` resolution or exceed the `Y^.1`
  component budget.
- Stop source-free `LTRAD` theorems based only on generic energy, density,
  covariance, or rational independence.
- Stop Weil propagation based only on existence of some positive extension.
- Stop fixed-strip-to-RH language until an explicit noncircular amplifier is
  present.

---

## 14. What was actually learned

The consolidation did not prove `CA4`, `DPA`, `LTRAD`, a zero-free strip, or
RH.  It did produce a sharper research object.

The project is not primarily missing a larger generic inequality.  It is
missing a **stable, source-faithful control of a distinguished mixed
interaction**:

- the actual zeta old/new cross block;
- the actual adjacent-gap mark inside semiprime fourth energy;
- the actual legal event source relative to its finite-time prime orbit.

Category theory explains the type error, homological algebra exposes an exact
integration-by-parts interface, and convex duality kills whole adapter
classes.  None supplies the analytic cancellation.  Their value is that the
next search can now be aimed at the information the quotient discarded,
rather than repeatedly strengthening the quotient theorem.

The deepest reusable rule is:

> Never ask whether a powerful theorem controls a nearby coarse object.
> Ask whether the target descends through the map to that object, with its
> mass, two-sided oscillation or relevant one-sided fiber envelope, and
> reconstruction condition number inside the exact downstream budget.

That is the equilibrium version of the project's repeated “are you sure?”
audit: it is a checkable condition, not another confidence statement.
