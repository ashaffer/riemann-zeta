# Atlas of exact obstructions

Status: canonical scope and proof-debt index, 2026-08-05.

This atlas records what the project's negative results actually prove.  It is
not a list of failed conversations and it is not a no-go theorem for the
Riemann Hypothesis.  Each card identifies a precise candidate class, the
obstruction, the evidence level, and the surviving escape hatch.  Full proofs
remain in the linked reports and Lean modules.

The governing release rules are in
[`publication/PROOF-STANDARD.md`](publication/PROOF-STANDARD.md).  In this
file, “eliminated” always means “eliminated under the hypotheses printed in
the same card.”

The independent internal objections and their dispositions are recorded in
[`publication/NO-GO-REFEREE-RESPONSE.md`](publication/NO-GO-REFEREE-RESPONSE.md).

## 1. Evidence key

- **F:** Lean checks the named statement; the linked audit prints its axioms.
- **A:** a conventional analytic or algebraic proof is written in the linked
  report, but the full statement is not checked by Lean.
- **L:** the proof uses a named theorem from the literature.
- **C:** an exact or interval computer certificate proves a finite statement.
- **D:** a diagnostic computation or scout, not a theorem at the advertised
  infinite level.

The evidence code is attached to each component, not to a surrounding story.
In particular, an F-rated toy countermodel does not turn its zeta-specific
interpretation into an F-rated theorem.

## 2. Obstruction matrix

| ID | Exact candidate class eliminated or constrained | Decisive mechanism | Evidence | Smallest visible survivor |
|---|---|---|---|---|
| NG-01 | Integer detectors continuous for compact-open normalized divisor perturbations, or using only the real critical-line phase | A remote normalized off-line quartet tends to one on every fixed compact and is positive on the real line | A; finite quartet algebra F | A genuinely global weighted topology tied to arithmetic growth |
| NG-02 | Continuous-symbol winding obtained as a uniform limit of the two canonical finite-prime shifted Euler-loop models | Finite loops are null-homotopic; the literal product is not `B^2` bounded, while the normalized phase is `B^2` but not uniformly Cauchy in the relevant strip | finite contraction F; limit claims A | A completion-native relative index with independently specified operator topology and all-place summability |
| NG-03 | A fixed finite set of finite places plus the archimedean place, required to remain positive on arbitrarily large supports | Its pole-annihilated Fourier multiplier is negative at zero and positive at high frequency | A | Support-coupled activation of unboundedly many places |
| NG-04 | Improving an independently assigned prime-edge Gram factorization by splitting one cross coefficient among more positive channels | Positivity forces endpoint diagonal cost at least twice the cross mass; the difference square is sharp | F | Essential cross-coupling between distinct places and infinity |
| NG-05 | Treating a nonzero pure mixed Hilbert pairing itself as a universally nonnegative quadratic form | Flipping one channel reverses its sign | F | Additional diagonal terms or a separately constructed positive polarization |
| NG-06 | Repairing degree-zero Hodge coercivity solely by changing a later differential while the first differential is fixed | Degree-zero energy is exactly the norm square of the first differential | F | Change the first map, degree, domain, or pairing |
| NG-07 | Deriving the last Schur-complement sign only from convolution, evenness, analyticity, separate block positivity, and the weak old equation | An explicit analytic rank-one kernel satisfies those properties while its exterior response exceeds the old gap | F for the countermodel and pivot algebra | A zeta-specific prime--archimedean cancellation estimate |
| NG-08 | Inferring a positive spectral metric from functional-equation duality, or fitting that metric after the spectrum is known | An off-line pair preserves alternating duality but admits no strictly positive adjoint metric; the general metric equation already encodes critical-line spectrum | minimal rational block F; general finite characterization A | A canonical positive metric constructed independently of zero locations |
| NG-09 | Fixed countable, scale-compatible, summable dictionaries of finite sign-reversing prime-set substitutions on dyadic squarefree collars | A finite-prefix conditioning and summable tail bound leave positive density untouched | A | An `N`-adaptive, unbounded-incidence mechanism with global matching state |
| NG-10 | Fixed-prime-conditioned Bagchi tails used to approximate a continued zeta remainder containing an off-line zero | The limiting random Euler tail is zero-free, so a Rouché approximation event is empty | A+L | A growing-cutoff, zeta-specific continuation theorem outside the fixed-block limit |

No row excludes all possible uses of its subject.  The last column is part of
the theorem's scope, not an invitation to call the surviving idea plausible.

## 3. Canonical theorem cards

### NG-01 — Compact-local invisibility of a remote quartet

**Statement.**  For `gamma, delta > 0`, let

```text
Q_(gamma,delta)(z)
  = ((z-gamma)^2+delta^2)((z+gamma)^2+delta^2),
A = gamma^2+delta^2.
```

For real `x`, `Q_(gamma,delta)(x)>0`.  For every fixed `R`,

```text
sup_(|z|<=R) |Q_(gamma,delta)(z)/A^2-1|
  <= 2 R^2/A + R^4/A^2,
```

which tends to zero as `gamma` tends to infinity with `delta` fixed.
Consequently, no integer-valued detector continuous for this compact-open
normalization can distinguish every such remote quartet from the baseline;
real critical-line phase alone cannot distinguish it at any height.

**Evidence and trust base.**  The inequality is an elementary analytic
calculation.  Lean checks the expansion, evenness, strict real positivity,
and sign preservation in
[`QuantizedPhaseIndexNoGo.lean`](lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGo.lean),
with the advertised declarations listed in
[`QuantizedPhaseIndexNoGoAudit.lean`](lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGoAudit.lean).
Lean does not presently check the compact-open estimate.

**Sharpness and nonclaim.**  Multiplication by `Q/A^2` changes global growth
and need not preserve an Euler product.  The theorem constrains compact-local
divisor or boundary-phase carriers, not arithmetic topologies that retain
global growth.  It does not construct a modified zeta function.

**Full argument.**
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

### NG-02 — Finite Euler loops lose their index at the all-prime limit

**Statement.**  Two assertions must be kept separate.

1. For `|r|<1`, the local unit phase
   `(1-r conjugate(z))/(1-r z)` on `|z|=1` contracts through nonvanishing unit
   phases by replacing `r` with `t r`, `0<=t<=1`.  Every finite product has
   trivial ordinary winding class.
2. For `0<a<1/2`, the literal two-sided shifted quotient has unbounded
   Besicovitch `B^2` norm as primes are added.  The functional-equation-
   normalized right phase is `B^2`-Cauchy for every `a>0`, but is not uniformly
   Cauchy for `0<a<=1/2`.

Therefore ordinary continuous-symbol winding does not pass from these finite
loops to an all-prime symbol in the RH-relevant strip: the topology in which
a limit is proved does not by itself supply an invertible continuous symbol,
and uniform symbol convergence fails.

**Evidence and trust base.**  Assertion 1 is F-rated in the phase module and
audit above.  Assertion 2 is A-rated: it uses prime-coordinate orthogonality,
the divergence/convergence of the displayed prime sums, unique factorization,
and Kronecker approximation.  Those analytic statements are not yet in Lean.

**Exact eliminated class.**  Uniform continuous-symbol limits of the two
finite-prime Euler-loop models specified in the report, equipped with ordinary
winding inherited from those approximants.

**Nonclaim.**  Uniform symbol nonconvergence does not prove nonconvergence in
a Calkin, strong, strict, or Fredholm-pair topology; no such operator model is
defined here.  No universal arithmetic index theorem is asserted.  A new
completion-native semifinite or relative index with a separately proved
operator topology is not addressed.

**Prior-art boundary.**  Almost-periodic Wiener--Hopf and mean-winding index
theories already exist, including work of
[Coburn--Douglas--Schaeffer--Singer](https://www.numdam.org/item/PMIHES_1971__40__69_0/),
[Murphy](https://doi.org/10.1016/j.jfa.2005.08.012), and
[Yakubovich](https://arxiv.org/abs/math/0606153).  The claim here is only the
failure of the two displayed Euler direct limits to furnish the required
continuous symbol, not a general theorem that mean topologies admit no index.

**Full argument.**
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

### NG-03 — Fixed finite-place Weil forms are eventually indefinite

**Statement.**  Fix a finite set `P` of primes and include the standard
archimedean place.  On the subspace annihilating the two pole moments, the
corresponding form has Fourier multiplier

```text
M_P(t) = -log(pi) + Re psi(1/4+i t/2)
         - 2 sum_(p in P) log(p) sum_(m>=1) p^(-m/2) cos(m t log p).
```

Then `M_P(0)<0`, whereas `M_P(t)` tends to positive infinity as `|t|` tends
to infinity.  Compactly supported broad bumps can satisfy the pole moments
exactly and concentrate their Fourier mass at zero.  Hence the fixed-place
form has a negative direction on sufficiently large support and is genuinely
indefinite.

**Evidence and trust base.**  A-rated conventional proof using Plancherel,
standard digamma asymptotics, and dominated convergence.  The floating-point
two-prime scan in the report is only D-rated corroboration and is not used in
the theorem.

**Sharpness and nonclaim.**  The prime set is fixed while support grows.  The
result neither contradicts positivity on a fixed small window nor treats the
full form, where newly active prime powers change with support.

**Prior-art boundary.**  The localization method is standard and belongs
near the variational Weil-form and semilocal literature, including
[Bombieri](https://eudml.org/doc/252338) and
[Connes--Consani](https://arxiv.org/abs/2006.13771).  The audit did not locate
the exact fixed-`P` indefiniteness statement.  This supports only “plausibly
new as stated,” pending specialist review.

**Full argument.**
[`TWO-PRIME-INFINITY-FAIL-FAST.md`](results/TWO-PRIME-INFINITY-FAIL-FAST.md).

### NG-04 — Optimal local Gram cost for one prime edge

**Statement.**  If vectors `u,v` in a real inner-product space satisfy
`<u,v>=w`, then

```text
2w <= ||u||^2+||v||^2.
```

The bound is attained by equal endpoint vectors.  Thus replacing the standard
difference-square representation of one negative cross coefficient by a
higher-rank direct sum of independent positive Gram channels cannot lower its
total endpoint diagonal cost.

**Evidence and trust base.**  F-rated in
[`PrimeEdgePolarization.lean`](lean/rhbridge/RHBridge/PrimeEdgePolarization.lean)
and its focused
[`PrimeEdgePolarizationAudit.lean`](lean/rhbridge/RHBridge/PrimeEdgePolarizationAudit.lean).

**Exact eliminated class.**  Independent place-by-place Gram channels that
reproduce each prime edge separately and sum their endpoint diagonal costs.

**Proof debt and nonclaim.**  The existing negative zeta-residual table is an
ordinary floating-point diagnostic.  Until a negative residual witness is
proved analytically or by a frozen interval certificate, the zeta-specific
application is not a complete no-go theorem.  Essential cross-place channels
are outside the local-cost theorem.

**Full argument.**
[`PRIME-EDGE-POLARIZATION-NOGO.md`](results/PRIME-EDGE-POLARIZATION-NOGO.md).

### NG-05 — Pure mixed pairings are not positive

**Statement.**  In a real inner-product space, a nonzero mixed coefficient
`2<u,v>` has a negative direction after replacing `v` by `-v`.  If the mixed
pairing is nonnegative for both signs, then `<u,v>=0`.

**Evidence and trust base.**  F-rated in
[`GlobalMobiusCancellation.lean`](lean/rhbridge/RHBridge/GlobalMobiusCancellation.lean)
and
[`GlobalMobiusCancellationAudit.lean`](lean/rhbridge/RHBridge/GlobalMobiusCancellationAudit.lean).
The same module imports mathlib's identity `moebius * log = vonMangoldt`; that
identity does not supply positivity.

**Exact eliminated class.**  A construction whose entire proposed positive
quadratic form is a nonzero pure off-diagonal Hilbert pairing.

**Nonclaim.**  Indefinite mixed terms can occur inside a positive block after
independently controlled diagonal terms are added.  Nonlocal Möbius incidence
is not itself ruled out.

### NG-06 — Later differentials cannot repair degree-zero energy

**Statement.**  In a two-step Hilbert complex
`C0 --d0--> C1 --d1--> C2`, the degree-zero Hodge energy is `||d0 x||^2`.
With `d0` and a scalar degree term fixed, its nonnegativity is exactly the
original relative Poincaré inequality and is independent of `d1`, even when
the square-zero law is imposed.

**Evidence and trust base.**  F-rated in
[`CompletedIncidenceComplexNoGo.lean`](lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGo.lean)
and
[`CompletedIncidenceComplexNoGoAudit.lean`](lean/rhbridge/RHBridge/CompletedIncidenceComplexNoGoAudit.lean).

**Scope and novelty boundary.**  This is an elementary structural lemma, not
a standalone research theorem.  It eliminates only the proposal to repair a
fixed degree-zero form by appending or changing a later differential.

The Lean theorem concerns bounded continuous maps on ambient Hilbert spaces.
Applying it to a concrete continuum incidence operator additionally requires
a densely defined closed or closable realization, fixed domains and metrics,
and an exact normalized identification with the Weil form.  Those
zeta-specific obligations are not proved by this card.

**Survivor.**  A construction may change `d0`, the grading, the domain, or the
pairing, but then it must derive the target arithmetic form anew.

### NG-07 — Generic low-sector structure does not force contraction

**Statement.**  For the rank-one convolution form

```text
Q(f)=||f||_2^2-alpha |integral f|^2
```

on two disjoint sets of measures `m,n`, choose `alpha m<1`, `alpha n<1`, and
`alpha(m+n)>1`.  Both separate compressions are positive and the nonlocal
kernel is entire and even, yet the exterior response exceeds the old gap and
the union has a negative direction.  For `m=n=1`, `alpha=3/4` is a rational
example.  The exact one- and two-mode Schur pivots are also recorded.

**Evidence and trust base.**  F-rated countermodel and algebra in
[`HodgeLowSectorNoGo.lean`](lean/rhbridge/RHBridge/HodgeLowSectorNoGo.lean)
and
[`HodgeLowSectorNoGoAudit.lean`](lean/rhbridge/RHBridge/HodgeLowSectorNoGoAudit.lean).

**Exact eliminated inference.**  Contraction cannot be deduced solely from
self-adjoint convolution form, evenness, analyticity off the diagonal,
separate block positivity, and the weak old eigen-equation.

**Nonclaim.**  The countermodel is not the zeta kernel.  It leaves open an
event-specific estimate exploiting exact cancellation between prime and
archimedean response entries.

**Full argument.**
[`HODGE-LOW-SECTOR-DTN-NOGO.md`](results/HODGE-LOW-SECTOR-DTN-NOGO.md).

### NG-08 — Duality is weaker than a positive polarization

**Statement.**  For nonzero rational `a`, the real off-line block

```text
A_a = diag(1/2+a,1/2-a)
```

preserves the standard alternating functional-equation pairing, but there is
no strictly positive rational quadratic metric `G` satisfying
`A_a^T G+G A_a=G`.  The real critical-line block has the identity as a
positive control.  More generally, over the complex numbers a positive
Hermitian solution exists exactly when `A-1/2` is similar to a skew-Hermitian
matrix, equivalently when `A` is diagonalizable with spectrum on the critical
line.

**Evidence and trust base.**  The rational two-by-two statements are F-rated
in
[`FinitePolarizationNoGo.lean`](lean/rhbridge/RHBridge/FinitePolarizationNoGo.lean)
and
[`FinitePolarizationNoGoAudit.lean`](lean/rhbridge/RHBridge/FinitePolarizationNoGoAudit.lean).
The general finite-dimensional characterization is A-rated standard linear
algebra in the linked report.

The latter is an instance of classical Lyapunov/inertia theory; see, for
example, [Ostrowski--Schneider](https://doi.org/10.1016/0022-247X(62)90030-6).
No novelty is claimed for that equivalence.

**Exact eliminated inference.**  Functional-equation duality alone cannot be
promoted to positivity, and solving for a metric from already known spectral
data does not independently explain the critical line.

**Survivor.**  A geometric or arithmetic polarization fixed before and
independently of the spectrum.

**Full argument.**
[`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md).

### NG-09 — Static summable prime substitutions miss positive density

**Statement.**  Let `T` be a fixed countable dictionary of scale-compatible
sign-reversing templates `(p;q,r)` on odd squarefree dyadic collars, and
suppose

```text
sum_((p;q,r) in T) 1/(qr) < infinity.
```

Then a positive-density set of squarefree integers avoids both support
patterns `100` and `011` for every template.  Its intersection with
`(N/2,N]` has `(d/2)N+o(N)` elements, and none of those vertices can be an
endpoint of an allowed substitution.  The same holds for pairs of disjoint
nonempty finite prime sets of opposite parity with summable endpoint-cylinder
weights.  Bounded prime incidence implies the required summability.

**Evidence and trust base.**  A-rated proof.  Finite-prime squarefree density
is converted to a countable statement by an explicit prefix conditioning and
the deterministic tail bound

```text
#{n<=x : some tail template applies}
  <= x sum_tail (1/p+1/(qr)).
```

No independence between overlapping templates is assumed.  Independent
referee review and a full prior-art comparison remain amber debt.

The support-pattern event contains the event that a substitution is actually
available in a particular collar; it need not equal it, because the proposed
target can leave the collar.  Avoiding the larger cylinder is what yields the
claimed isolated vertices.

**Exact eliminated class.**  Fixed summable dictionaries, including every
fixed bounded-incidence family of finite, scale-compatible, parity-flipping
prime-set substitutions.  The theorem concerns applicability, so it applies
regardless of how an algorithm prioritizes applicable templates.

**Nonclaim.**  An `N`-dependent sequential matching with unbounded incidence
and global collision resolution is outside the theorem.  No Mertens estimate
is proved.

**Full argument.**
[`MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`](results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md).

**Prior-art boundary.**  The density passage is close to classical
convergent-multiples arguments of
[Davenport--Erdos](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/2/1/93274/on-sequences-of-positive-integers),
while squarefree divisibility complexes already appear in
[Bjorner](https://arxiv.org/abs/1101.5704) and
[Pakianathan--Winfree](https://arxiv.org/abs/1104.4324).  The potentially new
piece is the exact scale-compatible substitution formulation and its
bounded-incidence corollary.  Priority remains unestablished.

### NG-10 — Fixed-cutoff conditioned Euler tails are zero-free

**Statement.**  Fix a prime cutoff `y` and a compact disk `K` in
`1/2<Re(s)<1`.  The conditional Bagchi tail after removing primes at most `y`
is almost surely the exponential of a locally uniformly convergent
holomorphic random series, hence is zero-free on `K`.  If the analytically
continued deterministic remainder has a zero in `K`, every boundary
approximation close enough for Rouché's theorem is impossible.  Its limiting
conditional probability is zero.

**Evidence and trust base.**  A+L-rated.  The local zero-free/Rouché
obstruction is elementary once the random Euler tail is constructed.  The
translation-frequency formulation uses Bagchi's functional limit framework
and a classical zero-density estimate, with sources and normalization in the
full report.

**Exact eliminated class.**  Fixed-cutoff phase conditioning followed by
ordinary zero-free random Euler-tail approximation to a zero-bearing
continued remainder.

**Nonclaim.**  A cutoff growing with height is a different shrinking-target
problem and is not covered.  It currently lacks the required zero-bearing
conditional small-ball theorem.

**Full argument.**
[`BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`](results/BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md).

## 4. Supporting countermodels, not headline no-go theorems

These artifacts are useful because they prevent invalid logical shortcuts.
They should not be advertised as independent progress on RH.

| Artifact | Exact lesson | Evidence boundary |
|---|---|---|
| [`Stage3BoundaryNoGo.lean`](lean/rhbridge/RHBridge/Stage3BoundaryNoGo.lean) | A quantitative collar-size lower bound alone does not exclude a new radical direction | F-rated two-dimensional countermodel only |
| [`Stage3ParityNoGo.lean`](lean/rhbridge/RHBridge/Stage3ParityNoGo.lean) | Simplicity of a ground state and reflection symmetry do not force the state into the even sector | F-rated two-dimensional countermodel only |
| [`LEE-YANG-INVERSE-CONE-FINAL-2026-08.md`](results/LEE-YANG-INVERSE-CONE-FINAL-2026-08.md) | A finite model-free moment cone can hold while the stronger independent-spin cone fails | C/D finite statement; no infinite Lee--Yang theorem |
| [`MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md`](results/MOBIUS-RESIDUE-TO-DENSITY-FINAL-2026-08.md) | Large every-scale partial sums do not imply pretentiousness for general bounded multiplicative functions; the exact Möbius parameter is singular | A+L counterexample to a generic inverse gate, not to every Möbius-specific inverse theorem |
| [`CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md`](results/CYCLOTOMIC-TWO-PRIME-TRACE-FINAL-2026-08.md) | Pure Euler coefficients with no mixed coefficient do not make a finite positive global trace | Exact finite algebra; infinite geometric realizations remain open |
| [`TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md`](results/TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md) | Ten proposed mechanisms were reduced to explicit gates or counterexamples | Research ledger; each row inherits only the evidence of its linked proof |

The complete branch registry is
[`results/REDUCTION-REGISTRY.md`](results/REDUCTION-REGISTRY.md).  A registry
entry is not promoted merely by appearing there.

## 5. The common theorem behind the failures

The results point to a recurring structural obstruction, not a universal
meta-theorem:

```text
one off-line zero
      |
      v
global coherent phase --------- visible to continuation/divisor topology
      |
      +---- locally square-summable or zero-density
      |             |
      |             +---- erased by mean, mass, or fixed-resolution topology
      |
      +---- requires all places and infinity
                    |
                    +---- broken by fixed-place or termwise positive assembly
```

The precise reusable lesson is a design test.  A proposed RH mechanism must
name:

1. the object changed by one off-line zero;
2. the topology in which that change has nonvanishing size;
3. the all-place completion native to that topology;
4. an independent order, contraction, or exclusion theorem;
5. a closed global limit in the same topology.

NG-01 and NG-02 attack items 1--2; NG-03 through NG-08 attack attempts to
manufacture item 4 locally; NG-09 and NG-10 show how locality and averaging
can lose items 2--3.  This synthesis guides candidate selection.  It is not,
by itself, a proof that every future route must fail.

## 6. Current proof-debt ledger

| ID | State | Required action before publication as a headline result |
|---|---|---|
| NG-01 | Amber | Typeset the compact-open lemma independently of the phase narrative; obtain a referee check of the exact detector corollary |
| NG-02 | Amber | Formalize or independently referee the `B^2` norm identities and Kronecker nonuniformity; freeze the two model definitions |
| NG-03 | Amber | Write a standalone theorem with the test-function scaling and domination details; independent normalization audit |
| NG-04 | Green for the abstract cost; Red for the zeta application | The focused audit passes; prove or interval-certify a negative residual witness before claiming the full local-edge class is eliminated |
| NG-05 | Green as a supporting lemma | Keep it subordinate; it is elementary and does not establish positivity of any completed form |
| NG-06 | Green as a bounded supporting lemma; Red for the continuum instantiation | Construct the densely defined closed/closable operator, fix its domain and metric, and prove the exactly normalized form identity before invoking the lemma |
| NG-07 | Green for logical insufficiency | Do not transfer the countermodel's bad sign to the zeta kernel; the zeta-specific estimate remains open |
| NG-08 | Green for the rational block; Amber for the general characterization/application | Add a primary-source comparison and, if used centrally, formalize the general Hermitian statement |
| NG-09 | Amber | Independent proof review, prior-art comparison, and a clean standalone manuscript proof |
| NG-10 | Amber | Independent audit of the conditional-law convention and every zero-density normalization; state literature inputs verbatim |

“Green” here certifies only the exact card component named in the state
column.  It is not a novelty or importance grade.

## 7. Focused reproduction and memory warning

The formal obstruction audits can be checked individually without replaying
the generated certificate corpus.  They should still be run serially.  Before
import minimization, several cold individual Lean processes peaked above 6 GB
RSS.  After replacing the five broad `Mathlib` imports in this layer, the
remeasured audits peaked at roughly 1.5--2.4 GB; the other focused no-go audits
were previously in the 2.3--2.7 GB range.  These commands are lower-risk than
an umbrella build, not tiny-memory:

```text
cd lean/rhbridge
lake env lean RHBridge/PrimeEdgePolarizationAudit.lean
lake env lean RHBridge/GlobalMobiusCancellationAudit.lean
lake env lean RHBridge/CompletedIncidenceComplexNoGoAudit.lean
lake env lean RHBridge/HodgeLowSectorNoGoAudit.lean
lake env lean RHBridge/FinitePolarizationNoGoAudit.lean
lake env lean RHBridge/QuantizedPhaseIndexNoGoAudit.lean
lake env lean RHBridge/Stage3BoundaryNoGoAudit.lean
lake env lean RHBridge/Stage3ParityNoGoAudit.lean
```

These commands check only the named Lean statements.  They do not validate
the A- or L-rated arguments in the reports.  Those require conventional
referee review under the proof standard.  A fresh clean-checkout measurement
remains a release task.  The present working-tree artifacts must also be
committed before any clean-checkout reproduction claim is made.
