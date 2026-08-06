# Atlas of exact obstructions

Status: canonical scope and proof-debt index, 2026-08-06.

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
For a continuous mathematical narrative grouping the cards by their common
mechanisms, read
[`publication/NO-GO-THEOREM-GUIDE.md`](publication/NO-GO-THEOREM-GUIDE.md).

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
| NG-11 | A strict regular commutator on a localized pure-point spectral subspace treated as an independent test; pure finite-section commutators; geometric dilation | Eigenstate commutator expectations and finite commutator traces vanish; geometric dilation has an unbounded negative simultaneous-prime symbol; the analogous boundary-compatible transport result is conditional on a localized pseudodifferential packet lemma | finite algebra F; dilation analysis A; transport step Amber; prime-5 scout D | Another local generator, completion of the transport asymptotic, a genuinely nonlocal mixed inequality, or a singular support-moving generator with the exact completed boundary defect retained |
| NG-12 | Inferring canonical phase-labelled extension families from equivalence of coercively shifted energy norms | The energy-dual adjoint repair is valid, but an exact Dirichlet family has a nonconstant shift quotient of its boundary phasors | Riesz core F; Dirichlet counterexample A; completed-Weil scan D | A zeta-specific adjoint intertwiner, or an explicitly tuned shift/phase sequence with a proved graph limit |
| NG-13 | Inferring support-uniform compact spectral crowding from exponential type, inner-function symmetry, and a fixed-support high-energy Weyl law whose onset/remainder may depend on support | An explicit type-`a` Hermite--Biehler family moves every added Blaschke zero beyond `a^2`, retaining the full far-tail density while its fixed-compact phase tends to the single Cayley factor | phase-floor/coherence scalar lemmas F; Hermite--Biehler countermodel and kernel normalization A; completed-Weil winding D | A zeta-specific characteristic or boundary-scattering limit; NG-15 shows that fixed-core strong-resolvent convergence is automatic under RH and moving defect vectors escape |
| NG-14 | Using a canonical fixed-negative-shift exhaustion to converge directly to the unshifted pure zeta-zero operator, or treating moving finite Clark vectors as fixed strong-resolvent probes | Even under RH the shift adds `c dx/(2*pi)` to the global Fourier measure, hence an absolutely continuous spectral component; strong resolvent controls the Clark measures only after the embedded reference vectors are proved to converge | shift-mass scalar lemmas F; Plancherel/zero-frame target and Clark normalization A; current Galerkin probes D | Target the honest mixed-spectrum shifted operator or a stronger boundary topology; NG-15 proves natural moving-vector compatibility fails, while admissible shifts tending to zero already encode all-window positivity |
| NG-15 | Using normalized finite reference-defect Clark measures or a phase-tuned strong-resolvent limit to select the zeta divisor | Translation invariance makes the reference Riesz norms grow exponentially and their unit vectors converge weakly to zero; once RH supplies the positive global space, the compact smooth core is a generator core, so every phase choice has the same generalized strong-resolvent limit | Riesz projection scalars F; translation escape, group-core, and generalized-resolvent theorem A; norm-growth scout D | A stronger boundary topology: locally uniform characteristic/Weyl convergence, norm resolvent or multiplicity-controlled projections, or a renormalized scattering limit of the unnormalized escaping kernels |
| NG-16 | Treating one fixed support-independent negative shift, or a uniform completed prime--archimedean `L2` remainder, as a weaker preliminary target than RH | `W+c delta_0` positive definite makes `g-(c/2)|t|` a global screw function; its Herglotz transform is `i(xi'/xi)(1/2-iz)+ic/2`, whose upper-half-plane holomorphy excludes off-line zeros | abstract floor/common-shift dichotomy F; Suzuki transform, Krein--Langer correspondence, and zeta implication A+L | The lower false-world rate is now proved: displacement `delta` forces eventual growth `exp((2 delta-o(1))a)`. The survivor is the reverse stability bound in terms of the supremal displacement `Delta` |
| NG-17 | Deriving the reverse localized-floor rate solely from the strip consequence `Psi(x)-x=O_eta(x^(1/2+Delta+eta))`, Stieltjes partial summation, and separate archimedean coercivity | Exact pole/main cancellation leaves a residual multiplier bounded by `exp((2 Delta+epsilon)a)(1+|t|)`, hence an `H^(1/2)` loss; the archimedean form controls only `log(1+t^2)`, and fixed-support modulations make the gap unbounded | A | A uniform oscillatory Mellin/exponential-sum estimate saving the derivative, or a genuinely joint prime--archimedean estimate |
| NG-18 | Deriving the reverse localized-floor rate only from a horizontal zero strip, full Riemann--von Mangoldt counting, symmetry, unsigned sampling, and even finite lower floor on every fixed support | Microscopic sparse clusters preserve counting to `O(1)` and qualitative local semiboundedness, yet boundary-bump tests make selected floors decay like `-exp(A_k^2+Delta A_k)` | A | A signed even/odd sampling-discrepancy estimate using Euler-product arithmetic; translation-bounded local horizontal second moment is one sufficient condition |
| NG-19 | Forcing positivity of the coefficient-defined trace-class xi companion through its natural leading sections, diagonal symmetrization, accretivity, raw Hankel moments, or coefficient total positivity as a weaker target | The dimension-two section has a certified nonreal pair and indefinite Hermitian part; the degree-six section has two left-half-plane eigenvalues; full `PF_infinity` is equivalent to RH by Edrei--Schoenberg | determinant algebra A; strict finite signs C | A genuinely infinite, non-compression arithmetic structure such as a sign-regular resolvent or normal dilation; finite Taylor sections cannot supply it |
| NG-20 | Replacing the signed Paley--Wiener Gårding inequality by pointwise positivity or a pointwise lower bound with the full logarithmic principal coefficient | The exact completed symbol is already negative at the certified `a=7/16` window; Kronecker recurrence aligns every active prime phase while the pole decays, forcing any pointwise coefficient-`1/2` remainder to be at least `B_a+log(2*pi)~4e^a` | recurrence and normalization A; negative scalar evaluation D with a deterministic unit test; compressed positive floor independently C/F | Retain the `PW_a` compression. A strict subleading pointwise coefficient remains logically open but would be a new uniform large-values theorem; the minimal compressed endpoint is RH-equivalent |
| NG-21 | Lifting positivity on all modulated interval/Fejer packets, even at every width and position, to positivity of the whole compressed Hermitian Toeplitz form | Individual packets omit coherent cross terms between separated blocks. A minimal `3 x 3` Toeplitz matrix, a continuous shifted-atom operator, and a real-even entire rank-three kernel all pass every packet while retaining a negative direction | finite and rational scalar algebra F; continuous and entire countermodels A | Add mixed Gram data for coherent packet superpositions or a zeta-specific arithmetic relation. One fixed separated-box cross orbit already detects the exact zero width, but bounding it is RH-equivalent |

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

### NG-11 — Regular virial commutators cannot order the localized Weil spectrum

**Statement.**  Three claims have distinct trust bases.

1. If `H psi=lambda psi` and the commutator with a regular generator `G` is
   defined on `psi`, then

   ```text
   <psi,[H,G]psi>=0.
   ```

   Thus a strictly positive commutator on a nonempty pure-point spectral
   subspace is impossible.  Every finite matrix commutator also has trace
   zero, so it cannot be positive definite.
2. For the completed localized Weil form, geometric dilation has Fourier
   multiplier

   ```text
   r m_a'(r)
    = r tau_(1/4)(r)
      + sum_(log n<2a) (2 Lambda(n)/sqrt(n))(log n) r sin(r log n).
   ```

   In the prime-2-only window, this multiplier plus any fixed nonnegative
   multiple of `m_a` tends to minus infinity along an explicit frequency
   sequence.  Kronecker approximation makes all finitely many active
   prime-power slopes negative simultaneously at every fixed larger support.
3. If `G_v=v d/dx+v'/2` preserves the interval, then `v` vanishes at both
   endpoints and every nonzero such `v` has `v'<0` somewhere.  A
   high-frequency packet supported there in an interval shorter than `log 2`
   kills every prime translation and the pole term asymptotically.  The claim
   that its archimedean commutator tends to the negative `v'` average uses a
   localized pseudodifferential packet lemma whose symbol/remainder proof is
   not yet written out here.  Thus the transport conclusion remains
   conditional/Amber.

**Compression identity.**  For `P^2=P` and `R=I-P`,

```text
P[H,X]P=[PHP,PXP]+PHRXP-PXRHP.
```

The internal term has trace zero.  Any nonzero positive trace in a compressed
calculation is boundary leakage, not positivity of a pure commutator.

**Evidence and trust base.**  Lean checks the eigenvector identity, finite
trace obstruction, compression identity, and an exact `2x2` leakage model in
[`VirialCommutatorNoGo.lean`](lean/rhbridge/RHBridge/VirialCommutatorNoGo.lean),
with declarations listed by
[`VirialCommutatorNoGoAudit.lean`](lean/rhbridge/RHBridge/VirialCommutatorNoGoAudit.lean).
The bounded form-domain version, expressed only through Riesz representatives
and the pivot metric, is checked in
[`FormDomainVirial.lean`](lean/rhbridge/RHBridge/FormDomainVirial.lean) and
[`FormDomainVirialAudit.lean`](lean/rhbridge/RHBridge/FormDomainVirialAudit.lean).
The geometric-dilation symbol argument is A-rated.  The transport wave-packet
argument is Amber pending its localized archimedean remainder lemma.  The
Legendre prime-5 experiment is D-rated.

**Exact scope and nonclaim.**  This eliminates regular strict Mourre
estimates as an independent test, pure Galerkin commutator certificates, and
geometric dilation with a fixed scalar repair once a prime power is active.
The real transport-flow conclusion additionally depends on the named packet
lemma.  The result does not prove the Weil form indefinite and does not rule
out another local generator, a genuinely nonlocal mixed estimate, or a
singular support-moving generator.  The last must retain and sign the full
prime--archimedean--pole boundary defect; that is the existing collar problem
rather than a standard virial shortcut.

**Full argument.**
[`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](results/COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md).

### NG-12 — Equivalent energy norms do not identify phase-labelled boundary families

**Statement.**  Let a coercive closed form define an energy Hilbert space `V`
on a finite interval, let differentiation be symmetric on a dense smooth
core, and assume the inclusion from the usual test-function topology on that
core into `V` is continuous.  The last hypothesis ensures that every
continuous energy-dual functional restricts to a distribution.  The
adjoint-domain argument is then valid in the energy dual:

```text
Dom(D*)={v : D^x(Jv) belongs to J(V)},
J(D*v)=D^x(Jv).
```

Consequently the deficiency vectors are `J^-1 exp(-izx)`, or
`T^-1 exp(-izx)` when the form is represented by `T`, and the deficiency
indices are `(1,1)`.  This repairs the topology/domain gap in the fixed-window
argument without assuming positivity at shift zero.

The repair does not make the extension spectrum independent of the coercive
shift.  For the exact Dirichlet family

```text
T_kappa=-d^2/dx^2+kappa  on H_0^1(-a,a),
```

the derivative at `z=0` of the boundary phase is `2+2r_kappa`, where
`r_kappa=(integral x T_kappa^-1 e^x)/(integral T_kappa^-1 e^x)`.  At `a=1`,

```text
r_0=(e^2-7)/6,             lim_(kappa->infinity) r_kappa=2/(e^2-1),
```

and these values are strictly different.  Thus equivalent shifted energy
norms do not, by themselves, identify the full phase-labelled extension
families by one constant boundary-phase relabeling.  This derivative argument
does not compare the complete zero sets at one specially selected phase.

A later zeta-specific scalar calibration is also insufficient: matching the
derivative at `z=i` forces two weak imaginary-axis values to high accuracy,
but those values are close to the universal Cayley factor.  Real and off-axis
held-out errors remain large and nonmonotone.  This prunes inference from the
one-jet calibration, not possible compact-local convergence at much larger
support.

There is a stronger exact necessary condition when an actual unitary adjoint
intertwiner is claimed.  Since every labelled defect fiber is one-dimensional,
the normalized defect Gram kernels must differ by a diagonal phase gauge.
Their pairwise magnitudes and Bargmann triple products are invariant.  An
affine-coordinate completed-Weil Galerkin scan retains a held-out defect, but
this last statement is diagnostic rather than an infinite-dimensional
theorem.

Across nested supports the shift itself has an exact obstruction.  Canonical
zero extension changes shifted energy by
`(sigma_a-sigma_b)||f||_2^2`.  For an antitone spectral-floor family, existence
on a cofinal support sequence of strictly admissible shifts tending to zero is
equivalent to nonnegativity of every floor.  Thus a natural-core construction
cannot use a vanishing auxiliary shift as an independent route to global
positivity.

**Evidence and trust base.**  The exact Riesz/partial-adjoint equivalences are
Lean-checked in
[`GelfandTripleAdjoint.lean`](lean/rhbridge/RHBridge/GelfandTripleAdjoint.lean).
The projective Gram theorem, scalar shift identity, and cofinal equivalence are
Lean-checked in
[`ProjectiveGramInvariant.lean`](lean/rhbridge/RHBridge/ProjectiveGramInvariant.lean),
[`NestedShiftRigidity.lean`](lean/rhbridge/RHBridge/NestedShiftRigidity.lean),
and
[`CofinalShiftPositivity.lean`](lean/rhbridge/RHBridge/CofinalShiftPositivity.lean).
The distribution-compatibility hypothesis, exponential classification, and
Dirichlet computation are A-rated analytic inputs/arguments.  The
completed-Weil phase scan is D-rated and is reported separately.

**Exact scope and nonclaim.**  This closes the generic inference from Hilbert-
space isomorphism to pointwise covariance of the full boundary family.  It
does not disprove a zeta-specific intertwiner, compare exact zeta zero sets at
one selected phase, or exclude a specially tuned shift/phase sequence, and it
says nothing directly about RH.  Any surviving finite-to-infinite
construction must specify those choices and prove that the comparison map
conjugates both the adjoint derivatives and their boundary spaces.  Exact
cross-window unitary equivalence is stronger than selected-extension
strong-resolvent convergence; failure of the former does not exclude the
latter.  In the zeta specialization, however, an admissible shift sequence
tending to zero already carries the RH-strength all-window positivity target.

**Full arguments.**
[`SUZUKI-ENERGY-ADJOINT-REPAIR.md`](results/SUZUKI-ENERGY-ADJOINT-REPAIR.md)
and
[`SHIFT-PHASE-COVARIANCE-FAIL-FAST.md`](results/SHIFT-PHASE-COVARIANCE-FAIL-FAST.md),
with the projective/cofinal checkpoint in
[`SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md`](results/SUZUKI-PROJECTIVE-KERNEL-CHECKPOINT.md)
and the normalized scalar test in
[`SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md`](results/SUZUKI-LIVSIC-CALIBRATION-FAIL-FAST.md).

### NG-13 — Fixed-support Weyl density does not control growing-support compact counts

**Statement.**  Let `Phi_a` be a strictly increasing real lift of the unit
boundary characteristic for a simple symmetric extension family.  On a
half-open interval its phase-level count is exactly

```text
N_(a,theta)((u,v])
  = floor((Phi_a(v)-theta)/(2*pi))
      - floor((Phi_a(u)-theta)/(2*pi)),
```

and differs from `(Phi_a(v)-Phi_a(u))/(2*pi)` by less than one.  Thus the
varying-support problem is a local phase-mass problem.

An ordinary Weyl law takes the opposite order of limits.  This failure persists
inside the regular de Branges class, not merely for an abstract escaping
sequence.  Put `u_(a,n)=pi*n/a`, `N_a=ceil(a^3/pi)`, and

```text
E_a=-b_i product_(n>N_a)b_(u_(a,n)+i)b_(-u_(a,n)+i).
```

Then `E_a=-H_a#/H_a`, where

```text
H_a(z)=(z+i)sin(a(z+i))
       /product_(n=-N_a)^N_a(z-u_(a,n)+i)
```

is entire Hermite--Biehler of exact type `a`.  It has the required reflection
symmetry, `E_a(i)=0`, and a fixed-`a` level count
`N_(a,theta)([-T,T])=2aT/pi+O_a(1)`.  Nevertheless, on every fixed compact,

```text
Phi_a(R)-Phi_a(-R)=4 arctan(R)+O_R(1/a).
```

All added phase density begins beyond order `a^2`; the Weyl remainder contains
a term of order `-a^3`.  Therefore no statement whose high-energy onset or
remainder is allowed to depend on `a` can imply fixed-compact crowding.

For the repaired Suzuki characteristic, Cartwright theory gives at fixed
`a`

```text
N_a([-R,R])=(d_a/pi)R+o_a(R),       0<=d_a<=2a.
```

The full coefficient `d_a=2a` additionally requires endpoint support of the
characteristic distribution, which Suzuki v1 does not prove.  The explicit
family above shows that even granting it does not repair the quantifier
reversal.  For the exact Suzuki kernel, the normalized defect coherence obeys

```text
Phi_a'(x)=2/[(1+x^2)rho_a(x)^2],
sigma_(a,theta)({lambda})=pi(1+lambda^2)rho_a(lambda)^2,
nu_(a,theta)({lambda})=rho_a(lambda)^2.
```

Thus support growth is precisely a zeta-specific decorrelation theorem, and
growing raw counts can be offset by shrinking raw Clark atoms or fixed-vector
weights.  Bounded-memory
completed-Weil models wind close to `L*T/(4*pi)` on the presently certified
range; that is D-rated evidence, not a continuum theorem.

**Evidence and trust base.**  The exact floor membership/cardinality/error
theorems and the escaping-onset spacing statements are Lean-checked in
[`BoundaryPhaseCounting.lean`](lean/rhbridge/RHBridge/BoundaryPhaseCounting.lean).
The scalar coherence consequences are Lean-checked in
[`BoundaryPhaseCoherence.lean`](lean/rhbridge/RHBridge/BoundaryPhaseCoherence.lean).
The kernel normalization, Hermite--Biehler countermodel, Cartwright
indicator-width formula, and endpoint-support boundary are A-rated
conventional analysis.  The numerical tables and their scope are in the two
checkpoint reports linked below.

**Exact scope and nonclaim.**  This rejects a fixed-support Weyl asymptotic as
the missing support-uniform theorem.  It does not reject compact-local
selected-divisor convergence, much less RH.  Moreover, divergent raw compact
counts would refute a locally uniform characteristic limit but not
strong-resolvent convergence by themselves: surplus eigenvectors may escape
weakly, and their fixed-vector weights can vanish.  A zeta-specific bound such
as weighted-average `rho_a^2=O_R(1/a)` would still control the raw-count
question.  The follow-up NG-15 shows, however, that fixed-core strong-
resolvent convergence is conditionally automatic while the canonical moving
reference vectors escape.  The surviving operator target is therefore a
stronger characteristic or boundary-scattering statement.

**Full argument.**
[`SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md`](results/SUZUKI-SPECTRAL-COUNTING-CHECKPOINT.md)
and
[`SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md`](results/SUZUKI-COMPACT-PHASE-MASS-FAIL-FAST.md).

### NG-14 — A fixed coercive shift does not target the pure zeta-zero operator

**Statement.**  Grant RH and the global zero-frame representation.  With
`c=-sigma>0`, Plancherel gives

```text
Q_W(f)+c||f||_2^2
  = sum_gamma m_gamma |fhat(gamma)|^2
      + (c/(2*pi)) integral_R |fhat(t)|^2 dt.
```

The natural global Fourier completion therefore has multiplication measure

```text
sum_gamma m_gamma delta_gamma + c dt/(2*pi).
```

Its translation generator has a nonzero absolutely continuous component.
It is a different operator from the unshifted pure-point zeta-zero generator,
even after RH is assumed.  Hence a canonical fixed-negative-shift exhaustion
cannot be identified directly with Suzuki's stated unshifted target.

There is a second topology requirement.  If `sigma_alpha` is the raw Clark
measure, the canonical normalized reference-defect measure in the regular
model is

```text
nu_alpha(dx)=sigma_alpha(dx)/[pi(1+x^2)],
nu_alpha({lambda})=2/[(1+lambda^2)Phi'(lambda)]=rho(lambda)^2.
```

Its Stieltjes transform is root-free:

```text
m(z)=[i H_alpha(z)-z]/(1+z^2).
```

But these finite reference vectors move with the support.  Strong-resolvent
convergence controls their measures only if the comparison embeddings also
send them to one convergent ambient vector.  NG-15 proves that the natural
embeddings cannot do so: the normalized reference vectors weakly escape.  An exact full-type
Hermite--Biehler family additionally shows that at `alpha=-1` all normalized
Clark mass may escape to infinity; generic type and symmetry do not imply the
missing tightness.

**Evidence and trust base.**  Lean checks the raw/reference atom conversion,
the phase-density cancellation, and the strict positive mass added by a
negative shift in
[`ClarkSpectralWeight.lean`](lean/rhbridge/RHBridge/ClarkSpectralWeight.lean).
The absolutely continuous density uses Plancherel and Suzuki's global
zero-frame representation under RH.  The Herglotz conversion and explicit
countermodel are A-rated.  The completed-Weil phase and Cauchy rows are
D-rated and are not used to infer a continuum obstruction.

**Exact scope and nonclaim.**  This does not disprove Suzuki's proposed
varying-window limit, RH, or a noncanonical comparison construction.  It
forces the target to be stated correctly.  At fixed negative shift, the
honest canonical target has mixed spectrum.  To recover the pure target one
must either construct an operator-intertwining quotient or remove the shift.
For antitone cofinal window floors, however, existence of strictly admissible
shifts tending to zero is already equivalent to nonnegativity of every floor,
so the latter is not an independent proof of RH.

**Full argument.**
[`SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md`](results/SUZUKI-WEIGHTED-CLARK-MEASURE-CHECKPOINT.md).

### NG-15 — Defect-vector escape makes the strong-resolvent limit phase-blind

**Statement.**  Let the finite window spaces be nested isometrically by zero
extension at one fixed common shift.  The `-i` defect vector `v_(a,-)` is the
Riesz representative of

```text
ell_-(f)=fhat(i)=integral f(x)e^(-x) dx.
```

Translation preserves the energy norm but multiplies this functional by an
arbitrary exponential factor.  Translating one fixed compact test toward the
left endpoint gives

```text
||v_(a,-)||^2 >= C exp(2a).
```

The Riesz projection identity across nested windows then implies that the
normalized vectors converge weakly to zero.  They cannot converge strongly,
even after phases are changed, to a nonzero global de Branges defect vector.
The `+i` vectors obey the reflected statement.

There is a complementary positive theorem under RH.  The global Weil space
is the completion of `C_c^infinity(R)` in a translation-invariant norm, and
translations form a strongly continuous unitary group.  Group mollification
shows that `C_c^infinity(R)` is a graph core for its Stone generator.  Hence
the closure of the compact-core derivative is already the self-adjoint zeta
translation generator.  Every finite self-adjoint extension agrees with this
generator on each fixed test once the window is large enough.  For every
off-real `z`, therefore,

```text
J_a(D_(a,theta(a))-z)^(-1)J_a*
  -> (D_infinity-z)^(-1) strongly
```

for every phase function `theta(a)`.  This is generalized strong resolvent
convergence because the embedded finite operators are nondense.  Arbitrary
self-adjoint completions on the orthogonal complements give the corresponding
ordinary strong-resolvent theorem.

The fixed-core scalar measures consequently converge, with finite atoms

```text
|hhat(lambda)|^2/K_a(lambda,lambda),
```

to `sum m_gamma|hhat(gamma)|^2 delta_gamma` in the unshifted RH model.  This
does not apply to the moving normalized defect kernels.

**Evidence and trust base.**  The exact projection/coherence/tail formulas
and the amplified Riesz lower-bound algebra are Lean-checked in
[`RieszKernelEscape.lean`](lean/rhbridge/RHBridge/RieszKernelEscape.lean).
The translation argument, Bochner-mollifier core lemma, dense-set resolvent
proof, and functional-calculus corollary are A-rated conventional functional
analysis.  A bounded-memory Galerkin norm scout agrees with the analytic
escape but is D-rated and unnecessary for the theorem.

**Exact scope and nonclaim.**  This proves neither RH nor failure of Suzuki's
entire-function limit.  The positive global space used for the unshifted
resolvent theorem is itself RH-conditional.  The theorem instead shows that
strong resolvent convergence is too weak to select extension phases or raw
eigenvalues: it holds for all phases while the boundary vectors disappear
weakly.  Locally uniform characteristic convergence, norm resolvent control,
or a renormalized boundary-scattering limit remains open and strictly
stronger.

**Full argument.**
[`SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md`](results/SUZUKI-DEFECT-ESCAPE-AND-RESOLVENT-CHECKPOINT.md).

### NG-16 — A global `L2` semibound is already RH-equivalent

**Statement.**  Let

```text
Q_W(f)=W(f*f_tilde),
lambda(a)=inf Q_W(f)/||f||_2^2
```

over nonzero smooth tests supported in `(-a,a)`.  Then the following are
equivalent:

```text
RH;
there is c<infinity with Q_W(f)>=-c||f||_2^2 globally;
inf_(a>0) lambda(a)>-infinity;
one strict shift sigma<lambda(a) works for every a.
```

Hence failure of RH forces `lambda(a)` to tend to `-infinity`, not merely to
become negative once.

For the analytic implication, put `g=-Psi`, where Suzuki proves
`W=-g''`, and set `h=g-(c/2)|t|`.  Positivity of `W+c delta_0=-h''`
implies, by a compact-mollifier double-primitive argument, that `h` is a
global screw function.  Krein--Langer then gives a Herglotz function on the
upper half-plane.  Suzuki's exact one-sided transform fixes it as

```text
q_c(z)=i(xi'/xi)(1/2-i z)+i c/2.
```

An off-line zero to the right of the critical line would produce a genuine
pole in that half-plane, a contradiction.  Reflection by the functional
equation excludes the left side.  Conversely, RH gives `c=0` by Weil
positivity.

**Evidence and trust base.**  The abstract equivalence between a uniform
lower bound and one strict global shift, and the `-infinity` alternative for
an antitone floor, are Lean-checked in
[`SemiboundedFloorDichotomy.lean`](lean/rhbridge/RHBridge/SemiboundedFloorDichotomy.lean)
and its audit.  The zeta implication is A+L-rated: it uses Suzuki's
distribution identity and transform, the Krein--Langer correspondence, and
Suzuki's form-core identification of the localized floor.  Bochner--Schwartz
plus the older Benedetto--Joyner tempered-Weil criterion gives an independent
short check.

**Exact scope and nonclaim.**  This does not rule out proving a uniform
completed bound; doing so would prove RH.  It rules out presenting that bound
or a globally admissible fixed negative shift as an easier scaffolding lemma.
Termwise autocorrelation estimates have coefficient sum asymptotic to
`4 exp(a)`, and the prime term itself is unbounded with support, so separate
component estimates cannot reach the target.  The subsequent quantitative
audit does produce an explicit two-bump family: a zero of displacement
`delta` forces `lambda(a)<=-C_epsilon exp((2 delta-epsilon)a)` eventually.
The pole proof controls the complete divisor, and the all-support upgrade uses
Bondarenko--Radchenko--Seip cardinal interpolation followed by smooth
truncation.  This is a conditional false-world theorem, not evidence that an
off-line zero exists.

**Full argument.**
[`SEMIBOUNDED-WEIL-DICHOTOMY.md`](results/SEMIBOUNDED-WEIL-DICHOTOMY.md).
The rate theorem is
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).

### NG-17 — Prime-counting error does not control the reverse floor in `L2`

**Statement.**  Put `U=2a`, `X=exp(U)`, and

```text
R(x)=Psi(x)-x,
c_f(u)=integral f(x) conjugate(f(x+u)) dx.
```

After splitting `dPsi=dx+dR`, the pole term cancels the exponentially large
main prime term exactly.  The harmless remainder is bounded below by
`-4||f||_2^2`, while the error is

```text
E_U(f)=2 Re integral_0^U c_f(u) exp(-u/2) dR(exp u).
```

If all zero displacements are at most `Delta`, the standard explicit-formula
consequence `R(x)=O_eta(x^(1/2+Delta+eta))` and Stieltjes partial summation
give

```text
|E_U(f)| <= C exp((2 Delta+epsilon)a)
  [||f||_2^2 + integral |t| |fhat(t)|^2 dt/(2 pi)].
```

The exponent is the desired one, but the norm is not: the added integral is
the squared homogeneous `H^(1/2)` norm.  The archimedean part of the Weil
form controls only the logarithmic Fourier weight.  For a fixed compact bump
`g`, modulation by `exp(iNx)` preserves support and `L2` norm, while these
two energies grow respectively like `N` and `log N`.  Compact support
therefore supplies no missing interpolation inequality.

**Evidence and trust base.**  This is an A-rated Stieltjes partial-summation
calculation using the standard zero-strip prime-counting estimate.  It is
written with all normalizations in Section 7.1 of
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).

**Exact scope and nonclaim.**  This does not disprove the reverse floor
estimate.  It eliminates the route that retains only the cumulative
prime-counting error and tries to absorb its Abel-summation loss using the
archimedean term separately.  A smoothed or oscillatory exponential-sum
estimate could still save the derivative, as could a joint estimate that
never separates the prime and archimedean pieces.

### NG-18 — Strip and counting data do not control signed vertical sampling

**Statement.**  Strip width, functional-equation symmetry, the full
Riemann--von Mangoldt count, unsigned sampling, and qualitative lower
semiboundedness on every fixed support do not jointly imply the reverse
localized-floor rate.  There is a simple symmetric order-one divisor with
counting discrepancy `O(1)` and finite floor on every fixed support, but with

```text
lambda(A_k) <= -c exp(A_k^2+Delta A_k)
```

along a sequence `A_k->infinity`.

The local mechanism is already visible in the divisor

```text
Z={plus_or_minus exp(k) plus_or_minus i Delta : k>=1},
```

with multiplicity `k`.  For a real even nonnegative compact bump `phi`, put

```text
f_0(t)=phi(t-b)-phi(t+b),
F_0(z)=2i phihat(z) sin(bz).
```

Then the paired block at height zero satisfies

```text
2 Re[F_0(i Delta) conjugate(F_0(-i Delta))]
  = -8 phihat(i Delta)^2 sinh(b Delta)^2 < 0.
```

Modulating `f_0` to frequency `exp(k)` preserves support and norm.  The
target block contributes `k` times this negative constant, while all other
blocks vanish asymptotically by uniform strip-Schwartz decay.  To restore the
full main count, begin with a real divisor having that count and, in sparse
fixed-length windows, relocate the `O(log T_k)` real nodes into these
conjugate clusters.  The gap/cluster discrepancy is still `O(log T)`.  The
windows can be chosen long enough that the residual real-node sampling tail
is smaller than the negative cluster.

The sharper construction begins with a critical-line quantile divisor of
density `w(T) asymp log T`.  Choose

```text
d_k=exp(A_k^2),
log T_k asymp d_k,
p_k=exp(-Delta A_k).
```

An interval of length `p_k` contains `m_k asymp p_k d_k` base nodes.  Pair
them and move each pair to the two simple off-line points of displacement
`Delta` at their midpoint.  The completed count changes by zero, and the
in-window discrepancy is at most one.

For any fixed support `a`, weighted Plancherel--Polya bounds make the tail
perturbation at most `C_(a,Delta) sup_(k>K)p_k` times the positive quantile
sampling energy.  It is absorbed for large `K`; the finite head is finite
rank.  Thus every fixed floor is finite.  At support `A_k`, however, an odd
two-boundary bump has vertical paired value of size `-c exp(2Delta A_k)`.
The cluster contributes

```text
-c m_k exp(2Delta A_k)
  asymp -c exp(A_k^2+Delta A_k),
```

while the critical-line background is only `O(d_k)`.  Rapid separation and
strip-Schwartz decay suppress the other clusters.

**Evidence and trust base.**  The construction and the quartet algebra are
A-rated.  The full proof and its normalization are in Sections 7.2--7.4 of
[`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`](results/QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md).
The existing `Stage4SamplingLiterature` interface records only the unsigned
upper-sampling theorem and does not rule out this behavior.

**Exact scope and nonclaim.**  The synthetic divisor is not zeta: it has no
Euler product.  The refined version deliberately does share zeta's
fixed-window semiboundedness and is sparse enough to obey ordinary global
zero-density bounds.  It proves that the missing input must be signed
Euler-product arithmetic controlling the placement of horizontal splitting,
not that the zeta reverse bound is false.

There is a sharp sufficient survivor.  If

```text
nu_2=sum m_j delta_j^2 delta_(gamma_j)
```

is translation bounded, then a Plancherel--Polya estimate applied to
`sinh(delta_j t)f` gives

```text
Q_W(f)>=-C M_2(1+a^2)[sinh(Delta a)/Delta]^2||f||_2^2.
```

Hence the localized-floor exponent equals `Delta`, even with infinitely many
off-line zeros.  This second-moment condition is not known for zeta.  Without
it, the survivor is a signed Garding estimate comparing the even `cosh` and
odd `sinh` traces jointly.

### NG-19 — Natural finite sections of the xi companion are not positive

**Statement.**  The centered function

```text
X(w)=xi(1/2+sqrt(w))/xi(1/2)=sum a_n w^n
```

has an explicit coefficient-defined trace-class companion `K` with
`det(I+wK)=X(w)`.  Its natural `N`-dimensional leading compression satisfies

```text
det(I+wK_N)=sum_(j=0)^N a_j w^j.
```

This finite-section route fails at the first nontrivial level.  The
dimension-two matrix is

```text
[[a_1,-a_2],[1,0]],
```

and rigorous 768-bit Arb balls give

```text
a_1^2-4a_2
  = -0.0004594955082930186652828466279458948... < 0.
```

It has a nonreal conjugate eigenvalue pair, admits no positive metric making
it self-adjoint, is not diagonally symmetrizable, and has indefinite Hermitian
part.  The raw coefficient Hankel minor is also negative.  At degree six the
certified Hurwitz signs are `+,+,-,-,-,-`; the Routh count gives two Taylor
roots in the right half-plane and therefore two companion eigenvalues in the
left half-plane.

**Evidence and trust base.**  The infinite determinant identity and the
finite compression formula are A-rated trace-class/rank-one algebra.  The
strict signs are C-rated FLINT/Arb interval results reproduced by
[`xi_companion_failfast.py`](src/xi_companion_failfast.py).  The complete
operator statement and coefficient enclosures are in
[`TRACE-CLASS-XI-COMPANION-GATE.md`](results/TRACE-CLASS-XI-COMPANION-GATE.md).

**Exact scope and nonclaim.**  This does not refute the infinite companion
identity or RH.  Taylor-section roots may escape to infinity, corresponding
to spurious eigenvalues collapsing to zero.  It closes leading-section
symmetrization, accretivity, oscillation, and raw-moment positivity as the
missing mechanism.

The infinite coefficient escape is not an easier named condition: by the
Edrei--Schoenberg classification, `PF_infinity` of `(a_n)` forces the product
of negative-real linear factors, and RH gives the converse.  Thus complete
Toeplitz total positivity and all-degree Jensen hyperbolicity are RH-equivalent
here.  A survivor must use genuinely infinite arithmetic structure not
visible in the leading compressions.

### NG-20 — The completed multiplier cannot be bounded pointwise at the endpoint scale

**Statement.**  For support radius `a`, direct Fourier compression of the
rank-two pole term gives

```text
Omega_a(t)=Re psi(1/4+it/2)-log pi
  -2 sum_(log n<2a) Lambda(n)n^(-1/2)cos(t log n)
  +4 integral_0^(2a) cosh(u/2)cos(tu)du.
```

At `a=7/16`, where only `n=2` is active,

```text
Omega_a(0)=-2.73971447387<0,
```

although the existing unrestricted certificate proves that the compressed
`PW_a` floor is strictly positive.  More generally, put

```text
B_a=2 sum_(log n<2a) Lambda(n)n^(-1/2).
```

Rational independence of the active prime logarithms and Kronecker recurrence
give `t_j->infinity` with all prime phases tending to one.  The pole symbol
tends to zero on that sequence, while the digamma asymptotic gives

```text
Omega_a(t_j)-(1/2)log(1+t_j^2) -> -B_a-log(2*pi).
```

Since `B_a~4e^a`, every pointwise lower bound with the full principal
coefficient needs the trivial exponential remainder.  It cannot prove the
displacement-sensitive reverse floor rate.

**Evidence and trust base.**  The pole sign, exact prime-main cancellation,
recurrence proof, and endpoint/RH quantifier audit are A-rated in
[`SIGNED-PRIME-GARDING-CHECKPOINT.md`](results/SIGNED-PRIME-GARDING-CHECKPOINT.md).
The scalar evaluation and low-memory scan are reproduced by
[`signed_garding_failfast.py`](src/signed_garding_failfast.py) and its unit
test.  The strict positive compressed floor at `a=7/16` is the existing
separate clipped-symbol certificate.

**Exact scope and nonclaim.**  This does not obstruct the form inequality.
It also does not eliminate a pointwise bound with a coefficient strictly
below `1/2`; the archimedean slack can pay for sufficiently late recurrence.
Such a bound would require a new uniform large-values estimate for the prime
Dirichlet polynomial.  The parsimonious survivor is the compressed endpoint,
not pointwise positivity.

### NG-21 — Triangular packets do not generate the full autocorrelation cone

**Statement.**  Positivity of a Hermitian Toeplitz or compressed convolution
form on every modulated interval indicator, even after allowing every interval
length and position, does not imply positivity of the form.

The smallest discrete example is

```text
    [ 1    0   5/4 ]
T = [ 0    1    0   ].
    [ 5/4  0    1   ]
```

Every consecutive modulated box has value at least `1/2`, but the endpoint
vector `(1,0,-1)` has value `-1/2`.  Dimension three is minimal.

On `L2(0,3/2)`, the even shifted-atom kernel

```text
k=delta_0+(5/4)(delta_1+delta_(-1))
```

has normalized packet value at least `1/6` for every width, position, and
modulation, while antisymmetric separated blocks have Rayleigh quotient
`-1/4`.  The phenomenon is not a distributional loophole: on a length-`L`
interval the real-even entire kernel

```text
k_ent(u)=2cos(pi u/(2L))-1/4
```

is nonnegative on all the same packets but negative on the projection of the
constant function orthogonal to the two exponential modes.

**Evidence and trust base.**  The complete analytic calculations, including
the global sinc inequality for the entire kernel, are in
[`TRIANGULAR-PACKET-CONE-NOGO.md`](results/TRIANGULAR-PACKET-CONE-NOGO.md).
Lean checks the exact finite/rational scalar values in
[`SelbergPacketConeNoGo.lean`](lean/rhbridge/RHBridge/SelbergPacketConeNoGo.lean),
with its focused axiom report in `SelbergPacketConeNoGoAudit.lean`.

**Exact scope and nonclaim.**  The theorem rules out a generic convex-density
or Toeplitz lift from diagonal Fejer packets.  It does not rule out a relation
special to the completed von Mangoldt comb.  The missing information is
polarized interference between separated packets.  In fact one fixed box's
separation orbit has exact growth exponent equal to the maximal horizontal
zero displacement; see
[`FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`](results/FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md).
That survivor is a detector, not an independently proved bound.

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
entry is not promoted merely by appearing there.  Its canonical logical
classification and nearest RH proxy are recorded in
[`results/RH-PROXY-LEDGER.md`](results/RH-PROXY-LEDGER.md).

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

NG-01 and NG-02 attack items 1--2; NG-03 through NG-08, NG-11, NG-12,
NG-16 through NG-21 attack
attempts to manufacture item 4 locally; NG-09 and NG-10 show how locality and
averaging can lose items 2--3; NG-13 through NG-15 isolate quantifier,
topology, target-identification, and boundary-escape failures in the
completion step.  This synthesis guides candidate selection.
It is not, by itself, a proof that every future route must fail.

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
| NG-11 | Green for the finite algebra; Amber for the completed smooth-core application | Independently audit the operator/core hypotheses, differentiation under the kernel integral, dilation normalization, finite-frequency trigamma bound, Kronecker step, and boundary-compatible packet asymptotics; do not promote the floating prime-5 scout to evidence for an infinite statement |
| NG-12 | Green for the abstract Riesz repair and Dirichlet pointwise counterexample; Red for exact zeta shift dependence | Obtain independent review of the form-core and distributional application; any transfer of the Galerkin selected-root failure requires graph/resolvent convergence, while exact full-family covariance would require a separate zeta calculation |
| NG-13 | Green for the scalar floor/coherence theorems; Amber for the analytic kernel identity, Hermite--Biehler family, and Suzuki application | Independently review the raw-versus-de-Branges normalization, infinite-product convergence, exact type, Clark factor, Cartwright criterion, and endpoint support; do not infer strong-resolvent failure from unweighted count divergence |
| NG-14 | Green for the scalar normalization/shift algebra; Amber for the global Fourier-completion statement | Independently review density of the Fourier core in the mixed atomic/Lebesgue space and the varying-space resolvent convention; NG-15 settles natural named-vector compatibility negatively, but do not infer failure of every noncanonical quotient or of an asymptotic unshifted construction |
| NG-15 | Green for the scalar projection algebra; Amber for the analytic application | Independently referee the Riesz projection identity, translation convention, group-mollifier graph-core proof, and generalized functional calculus; keep the RH assumption explicit and do not promote Galerkin norm rows to continuum evidence |
| NG-16 | Green for the abstract floor theorem; Amber for the zeta analytic synthesis and quantitative rate | Independently referee the mollifier-to-screw calculation, every transform sign and factor, the BRS vertical-strip extraction, cutoff sampling estimate, and form-core passage; present the results as an RH-equivalent quantifier audit plus a conditional false-world rate, not as a proof of RH |
| NG-17 | Amber | Independently check the pole/main normalization, Stieltjes boundary terms, zero-strip-to-prime-error input, and modulation countertest; state only the failure of this estimate architecture, not failure of the reverse rate |
| NG-18 | Amber | Independently referee quantile-divisor sampling, `O(1)` count preservation, tail absorption for every fixed support, boundary-bump asymptotics, and the translation-bounded second-moment theorem; do not transfer the synthetic divisor's superexponential floors to zeta |
| NG-19 | Green for the interval signs; Amber for the infinite operator exposition | Re-run the one-thread Arb script and independently check the rank-one determinant, compression indexing, Routh count, and Edrei--Schoenberg specialization; do not infer anything about the limiting spectrum from Taylor-section failures |
| NG-20 | Green for the exact scalar algebra and recurrence; Amber for the analytic synthesis | Independently audit the screw-preprint sign discrepancy, Fourier normalization, strict-gap implication, and use of the quantitative floor theorem; do not promote sampled subleading minima to a global bound |
| NG-21 | Green for the finite/rational scalar algebra; Amber for the analytic cone exposition | Independently referee the continuous operator-domain spelling and the global sinc inequality; keep the conclusion to failure of the generic packet lift, not failure of any zeta-specific mixed-packet theorem |

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
lake env lean RHBridge/VirialCommutatorNoGoAudit.lean
lake env lean RHBridge/GelfandTripleAdjointAudit.lean
lake env lean RHBridge/FormDomainVirialAudit.lean
lake env lean RHBridge/ProjectiveGramInvariantAudit.lean
lake env lean RHBridge/NestedShiftRigidityAudit.lean
lake env lean RHBridge/CofinalShiftPositivityAudit.lean
lake env lean RHBridge/SemiboundedFloorDichotomyAudit.lean
lake env lean RHBridge/BoundaryPhaseCountingAudit.lean
lake env lean RHBridge/BoundaryPhaseCoherenceAudit.lean
lake env lean RHBridge/ClarkSpectralWeightAudit.lean
lake env lean RHBridge/RieszKernelEscapeAudit.lean
lake env lean RHBridge/SelbergPacketConeNoGoAudit.lean
```

These commands check only the named Lean statements.  They do not validate
the A- or L-rated arguments in the reports.  Those require conventional
referee review under the proof standard.  A fresh clean-checkout measurement
remains a release task.  The present working-tree artifacts must also be
committed before any clean-checkout reproduction claim is made.
