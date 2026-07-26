# PLAN — Category theory / structural mathematics (independent consultant round)

Prepared July 26, 2026 (machine clock July 25 convention noted in `PROGRAM.md` §2.14).
Scope read: `README.md`, `PROGRAM.md` §§2.14–2.18, 3, 4, `THEOREMS.md`, `ENVELOPE.md`,
`results/RESULTS.md`, plus the Lean artifacts `lean/weilcert/*` and their generators
(read as artifacts of the certificate category of Lemma 3; no other expert PLAN was read).
All numerical claims below are quoted from `results/RESULTS.md` or were computed in this
session directly from repository files; session-computed numbers are marked [computed here].

Notation as in `THEOREMS.md`: H_L = L²([−L/4, L/4]) extended by zero, Q_L = P + A − Π the
truncated Weil form, λ(L) = inf{Q_L(φ) : ‖φ‖₂ = 1}. RH ⟺ λ(L) ≥ 0 for all L (Weil).
Proved inputs used throughout: λ is non-increasing and continuous with explicit modulus
(Glide Theorem, `THEOREMS.md` Theorem 1); under RH, Q_L(φ) = 2Σ_{γ>0}|φ̂(γ)|², so λ(L) is
the lower frame bound of the exponentials at the zero ordinates on a window of length L/2.
Measured inputs: ln λ(L) ≈ 10.2 − 1.755·e^{L/2}(L/2 + 4.0) over ~35 decades; family
universality in T*_χ = (2π/q)e^{L/2} (slopes in [10.7, 12.3] per unit e^{L/2}/q); the
envelope is a functional of the counting function alone (§2.17 mechanism experiment);
certified rungs down to (1.7997e−20, 1.79972291e−20] at L = 711/200.

---

## 1. Reformulation

**The three-level tower.** The program's data live at three levels, and the open problem
lives entirely in the traffic between them:

1. **The operator ladder.** For each L, the quadratic space (H_L, Q_L); for L ≤ L′ the
   zero-extension ι_{L,L′}: H_L → H_{L′}, an isometry with Q_{L′}∘ι = Q_L exactly
   (Theorem 1, Step 1: entering primes cannot see short supports). So
   W: ((0,∞), ≤) → 𝒬, L ↦ (H_L, Q_L), is a functor into the category 𝒬 of real
   pre-Hilbert spaces with a (lower-bounded, closable) quadratic form, morphisms =
   isometries preserving the form on the nose. Monotonicity of λ is precisely
   functoriality of W composed with the order-reversing "unit-sphere infimum" map
   𝒬 → (ℝ ∪ {−∞}, ≥). The colimit of W is (L²_c(ℝ), Q_Weil), compactly supported test
   functions with the full Weil form, and **RH = positivity of the colimit form**.

2. **Galerkin stages.** Finite-dimensional subspaces V ⊂ H_L (hat, Legendre, prolate…),
   with stage margins λ_V = min of Q_L on the unit sphere of V. Every number in
   `results/RESULTS.md` is a stage margin (Rayleigh–Ritz upper bound for λ(L)).

3. **Certificates.** Kernel-verified rational objects (`lean/weilcert/*`): an integer
   matrix A, a scale DEN, a radius δ, and a kernel proof that every symmetric rational
   (hence real) M with |M − A/DEN|_∞ ≤ δ is positive definite, plus a Bridge proposition
   identifying the true stage matrix inside the ball, with a stated trust base.

**Where the naive colimit argument is trivially true — and why that is not the theorem.**
Because every vector of the colimit lies at a finite stage, "Q_L ≥ 0 for all L ⟹ the
colimit form is ≥ 0" is free; it is the exhaustion argument already recorded in §3. The
open problem is not stagewise-⟹-limit at level 1; it is that only level-3 objects are
accessible, there are finitely many of them, and inf_L λ(L) = 0 to the accuracy of the
program's own instruments (certified: inf_L λ ≤ 1.79972291e−20 unconditionally, modulo
the mpmath.iv trust base; measured descent continues to ~1e−40). The colimit sits **on the
boundary of the positivity cone**: no uniform margin survives the limit, so no formal or
compactness argument can hold the line without renormalization. That is the exact content
of "the naive invariant λ_min ≥ μ > 0 is false" (§2.7) seen categorically.

**The three pieces of added structure that repair stagewise-⟹-limit.** This is the
answer to the question this seat was asked:

- **(S1) Filtration.** If the stages are *nested* — V₁ ⊆ V₂ ⊆ … along the zero-extensions,
  cofinal in the window poset, with ∪V_n a form-core — then the stage margins s_n form a
  single non-increasing sequence with lim s_n = inf_L λ(L), and "s_n ≥ 0 at every stage"
  *does* imply positivity in the limit, envelope collapse notwithstanding
  (Lemma 1). For non-nested stages the implication is false and the repo has already
  measured the failure twice (the hat knife-edge §2.7 → §2.15; the m = 101 plateau §2.8
  → §2.14). Nestedness is the exactness property the naive argument silently assumed.

- **(S2) Continuity.** λ continuous (Theorem 1) upgrades "λ ≥ 0 on a dense set of L" to
  "λ ≥ 0 for all L". Proved; closes the topological gap, not the infinite one.

- **(S3) Recursion.** Stage-wise certification is an infinite family of finite theorems.
  It is a single finite proof iff the family is generated — base object plus a certified
  step cert(n) ⟹ cert(n+1) — i.e., iff the certificate assignment extends to a morphism
  out of a natural-numbers object in the certificate category (Lambek–Scott, *Higher
  Order Categorical Logic*, for NNO ⟺ induction). The analytic content of the step is
  exactly the transfer inequality (deficit ≤ rescue). **UPT is the existence of the
  recursion generator.** (Lemma 3.)

**The normalized functor.** Fix a gauge: a continuous non-increasing E: (0,∞) → (0,∞).
The E-renormalized ladder W_E: L ↦ (H_L, Q_L/E(L)) has zero-extensions that expand the
form by E(L)/E(L′) ≥ 1; its margin functor is μ_E = λ/E, and

  **UPT_E :  μ_E factors through [c, ∞) for some c > 0,  i.e.  λ(L) ≥ c·E(L) for all L.**

UPT_E ⟹ RH for any positive gauge; conversely RH ⟹ some gauge works (take E = λ, which
is then continuous, positive, non-increasing) — so the equivalence is cheap and the entire
mathematical content is the *specific* gauge. The measurements dictate it: the §2.17
mechanism experiment (smooth Riemann–von Mangoldt staircase reproduces the margins within
truncation — 2.68972e−10 true vs 2.75124e−10 smooth at L = 2.485, Γcut = 420 — while
Poisson arrivals cost 1.5–2 orders) says the correct E is itself the margin of a
**zeta-free model ladder**: let Q^{mod}_L be the frame form of the exponentials at the
smooth staircase points N(t_k) = k − 1/2 (a computable, arithmetic-free object) and
λ_mod(L) its margin. The data-driven normalization of §3's N_p is division by λ_mod, and

  **UPT (model form):  ∃ c > 0 :  λ_ζ(L) ≥ c · λ_mod(L)  for all L.**

The factorization this effects: [λ_mod(L) > 0 with Landau–Widom asymptotics — provable
territory, no arithmetic, the natural M3 target] × [one comparison constant c — the whole
arithmetic content, where rigidity of the true zeros enters]. Categorically the comparison
is a positivity-domination between two functors on the same index poset; that shell is
bookkeeping, and I say so — but it is the bookkeeping that isolates the residue exactly.

One more reformulation used below. By Theorem 1 the set 𝒫 = {L : λ(L) ≥ 0} is a closed
down-set (a sieve on the window poset): certificates propagate down, refutations propagate
up — the order-theoretic materialization of the Π₁/Σ₁ asymmetry of §6. RH ⟺ 𝒫 is the
maximal sieve ⟺ the certified sub-sieve can be made cofinal.

---

## 2. Lemma candidates

### Lemma 1 (Filtered staircase: exactness of the margin under nested exhaustion)

**(a) Statement.** Let (V_n)_{n≥1} be finite-dimensional subspaces with V_n ⊂ H_{L_n},
L_n ↑ ∞, and ι_{L_n, L_{n+1}}(V_n) ⊆ V_{n+1} (nestedness under zero-extension). Assume
each V_n lies in the form domain of Q (finite log-weighted energy W₊, Lemma B) and that
∪_n ι(V_n) is a form-core of every H_L (exhaustion). Put s_n = min{Q_{L_n}(φ) : φ ∈ V_n,
‖φ‖₂ = 1}. Then:

  (i) s_{n+1} ≤ s_n (a single monotone staircase);
  (ii) lim_n s_n = inf_L λ(L)  ("the stage functor commutes with the filtered colimit");
  (iii) RH ⟺ s_n ≥ 0 for all n; and under RH in fact s_n > 0 for all n, so RH is
        equivalent to the strict positivity of one explicit, computable, monotone
        sequence of algebraic-in-the-data numbers;
  (iv) such systems exist with exponential approximation power: nested hp
        piecewise-polynomial spaces on geometrically refined meshes whose knot sets
        include the window endpoints and the minimizer kink points ±(a − log n) for the
        participating prime powers (kinks measured in §2.15);
  (v) none of (i)–(iii) holds for non-nested stage families: stage margins of non-nested
        families are not invariants of the functor W and can order-invert across windows.

**(b) Proof strategy.** (i) is Rayleigh–Ritz plus strictness of zero-extension
(Q_{L′}∘ι = Q_L, Theorem 1 Step 1). (ii): "≥" is immediate since s_n ≥ λ(L_n) ≥ inf λ.
For "≤": given L, a unit φ ∈ H_L with Q_L(φ) ≤ λ(L) + ε, mollify (φ_δ → φ in the W₊-form
norm; the archimedean weight is ½log(1+4r²) + O(1) by Lemma A(ii)/(iv), so form-norm
control is an H^s-control for any s > 0 plus L²·log, and P, Π are form-bounded by Lemma
B(i)), then interpolate into V_n for n large by the exhaustion hypothesis; continuity of
Q in the form norm transfers the Rayleigh quotient up to ε. Monotone convergence of s_n
plus cofinality of (L_n) gives lim s_n = inf_L λ(L). (iii): the squeeze
s_n ≥ λ(L_n) ≥ inf λ = lim s_n. If all s_n ≥ 0 then inf_L λ = lim s_n ≥ 0, which is RH by
Weil plus exhaustion over supports; conversely RH gives s_n ≥ λ(L_n) ≥ 0. Strictness
under RH: λ(L) > 0 for each fixed L is classical — the zero ordinates' lower Beurling
density is infinite, so after thinning to a separated subsequence, Beurling–Landau
sampling gives a positive lower frame bound (H. J. Landau, Acta Math. 117 (1967);
Beurling, Collected Works II; Olevskii–Ulanovskii for the modern form) — exactly the
classical input already flagged in `ENVELOPE.md`'s caveats. (iv): hp spaces on nested
meshes are nested when refinement adds knots and raises degrees, and zero-extension of a
piecewise polynomial is a piecewise polynomial once the old window endpoints are knots of
the new mesh; exponential convergence for piecewise-analytic targets with point
singularities is the standard hp theorem (Babuška–Guo 1986; Schwab, *p- and hp-FEM*,
Oxford 1998), applicable because the minimizers are analytic away from the finitely many
kink points. (v) is proved by the recorded counterexample in (e).

**(c) Hardest missing step.** The form-core/density argument with the log-weight is mild
but must be written honestly (mollification near the support endpoints without leaving
H_L: dilate-then-mollify, the same maneuver as Theorem 1 Step 2). The strictness input is
cited classical, not reproved. Nothing else is missing; I can write (i)–(iii) in full.

**(d) Difficulty.** Low–medium. This is the one I commit to writing out completely.

**(e) Concrete check against the repo.** Two checks, one already in the data:
(1) *Recorded inversion witnessing (v):* in the hp hat ladder at m = 61
(`results/RESULTS.md`, day-two hp section), λ_Gal(L = 2.19) = 3.819e−7 <
λ_Gal(L = 2.485) = 4.13636e−7, while the operator ordering is the reverse
(λ(2.1942) ≈ 5.77e−8 ≫ λ(2.485) ≈ 3.5e−10): non-nested hat grids at different L
order-invert; at m = 41, 81, 101 the same pair happens to order correctly — the stage
numbers of non-nested families carry no ordering information about W. By contrast every
recorded fixed-L Legendre ladder (nested across m) is strictly monotone, as (i) requires.
(2) *New instrument:* implement one nested hp chain V₁ ⊂ V₂ ⊂ … through the windows of
2, 3, 4, 5 and confirm a single monotone certified staircase; its values should track the
envelope of §2.15 while the hat wall (m^{−3.6} transient) disappears. This is a
`src/spectral_margins.py`-scale exercise and directly upgrades Track A's ledger from a
two-parameter (L, m) grid to one invariant sequence.

---

### Lemma 2 (Scaling-site descent: the ladder is an ℕ^×-equivariant cosheaf; the margin is a scale invariant; the prime terms are the site's matrix coefficients)

**(a) Statement.** Let τ_c φ(x) = φ(x − c). Then:

  (i) Q(τ_c φ) = Q(φ) for every compactly supported φ and every c ∈ ℝ: each of P, A, Π
      is translation-invariant (P because the factors rescale by e^{±c/2} and cancel;
      A because it is a functional of |φ̂|²; Π because it is a functional of ψ_φ).
      Consequently, defining H_I and Q_I for an arbitrary bounded interval I (prime sum
      truncated at e^{|I|}, which is exact on H_I), the margin λ(I) depends only on |I|,
      and λ(I) = λ(2|I|) in the repo's normalization I = [−L/4, L/4], |I| = L/2.
  (ii) In multiplicative coordinates u = e^x, windows are intervals Ω ⊂ (0, ∞) with
      aspect ratio ρ(Ω) = sup Ω / inf Ω, translation becomes the scaling action of
      ℝ^×_+, and (i) says: the assignment Ω ↦ (H_Ω, Q_Ω) is an ℝ^×_+-equivariant
      precosheaf of quadratic spaces (extension by zero as the cosheaf maps), and the
      margin descends to a single function of ρ, non-increasing and continuous in ρ by
      the Glide Theorem. Restricting the equivariance to ℕ^× ⊂ ℝ^×_+ and the opens to
      bounded intervals, the ladder is a precosheaf on the underlying category of the
      Connes–Consani scaling site 𝒮 = [0, ∞) ⋊ ℕ^× (Connes–Consani, C. R. Acad. Sci.
      354 (2016) 1–6; Selecta Math. 23 (2017) 1803–1850), equivariant for the site's
      monoid action.
  (iii) The arithmetic part of the form is a weighted sum of matrix coefficients of that
      action: with (U_n φ)(u) = φ(u/n) the site's scaling operators,
      Π(φ) = 2 Σ_n Λ(n) n^{−1/2} ⟨φ, U_n φ⟩ (in x-coordinates ⟨φ, τ_{log n}φ⟩ = ψ_φ(log n)),
      and the participation rule of the truncation is the site's overlap condition:
      n contributes on Ω iff nΩ ∩ Ω ≠ ∅ iff n < ρ(Ω) = e^{L/2}. The monotonicity engine
      of Theorem 1 ("entering primes cannot see short supports") is the vanishing of
      matrix coefficients along site morphisms with disjoint overlap.
  (iv) (Functorial statement of the measured family law; measured, not proved.) For a
      real primitive character mod q the twisted ladder is the same precosheaf with
      weights χ(n) on the matrix coefficients, primes dividing q deleted, pole deleted,
      parity kernel swapped. The measured universality (slopes d ln λ / d(e^{L/2}/q) all
      in [10.7, 12.3]; `results/RESULTS.md` family section) is precisely: *to leading
      exponential order the twisted margin is the pullback of one universal decay profile
      along the site's scaling morphism by q, with conductor, parity, and pole entering
      only the prefactor* — T*_χ = (2π/q)e^{L/2} is the site's q-rescaling read at the
      Nyquist height.

**Remark (the pole is the only non-local term).** In the x-space kernel representation
(§2.14) the archimedean coupling between disjoint blocks at gap g decays like e^{−g/2}
(kernel e^{−u/2}/(1 − e^{−2u})), and the prime coupling is atomic at u = log n with weight
Λ(n)e^{−u/2}: together, the explicit-formula measure. The pole P = 2m₊(φ)m₋(φ) is a
rank-2 form whose cross-block coupling does not decay with the gap. So the pole-free
family cosheaves are e^{−gap/2}-quasilocal while ζ's is not, purely because of the pole —
the cosheaf-theoretic face of the pole flip (§2.11: the pole is what reverses the
stabilizer roles). I state this at the level of the form's cross terms only; I make no
claim about margins of disconnected opens.

**F₁ commentary (dictionary, flagged as such).** In Borger's take on F₁ (λ-rings:
"Λ-rings and the field with one element", arXiv:0906.3146) descent data to F₁ *is* a
commuting family of Frobenius lifts indexed by ℕ^×; in Deitmar's (monoid schemes,
"Schemes over F₁", 2005) the underlying F₁-object forgets addition and keeps the
multiplicative monoid. Under either reading, (iii) says: the arithmetic part of the Weil
form is the pairing of φ against its Frobenius orbit, and the §2.17 mechanism experiment
("the decay constant is a functional of N(T) alone; local statistics enter only the
offset; the true zeros sit at the maximally rigid offset") says the envelope is defined
over the density skeleton — the F₁-shadow — while arithmetic proper is a bounded offset.
The correct normalization N_p of §3 divides by an F₁-object (the model-ladder gauge of §1).

**(b) Proof strategy.** (i)–(iii) are short exact computations, all displayed above or in
`THEOREMS.md`'s conventions; the only care is that truncation-at-e^{|I|} is exact on H_I
(support of ψ_φ), which is the ledger's own observation. (ii) additionally needs Glide
continuity, which is proved. (iv) is a *statement*, offered as the precise target shape;
its proof is UPT-adjacent and not claimed.

**(c) Hardest missing step.** For (i)–(iii): none. For (iv): everything — it is the
family-uniform transfer inequality in disguise; the lemma's role is to fix its functorial
form (one profile, pullback along q, offset prefactor) so that any proposed proof or
refutation has a canonical statement to hit.

**(d) Difficulty.** (i)–(iii) easy and self-contained (a page); (iv) open.

**(e) Concrete check against the repo.** Translation invariance is falsifiable in the
instruments: rebuild the spectral form on an asymmetric window [c − L/4, c + L/4]
(the pole moments acquire factors e^{±c/2} that must cancel in the product; archimedean
and prime blocks are unchanged) and confirm λ to solver precision against the symmetric
window — a ~30-line modification of `src/spectral_margins.py`. The participation rule
(iii) is already the code's truncation convention (prime powers n < e^{L/2},
`PROGRAM.md` §6), and the family universality data for (iv) are the twelve slopes in
`results/RESULTS.md` (q = 3, 5, 7 at L up to 7, all in [10.7, 12.3] against ζ's
[10.7, 11.6], Rayleigh–Ritz one-sided).

---

### Lemma 3 (The certificate category: soundness = composability, closure = recursion — and a coherence breach found in the repo's own artifacts)

**(a) Statement.** Define the category **Cert**:

- *Objects:* tuples 𝒞 = (L, m, 𝔅, A, DEN, δ; π, β) where L ∈ ℚ_{>0}, 𝔅 is an ordered
  basis of an m-dimensional subspace V_𝔅 ⊂ H_L lying in the form domain, A ∈ Sym_m(ℤ),
  DEN ∈ ℕ, δ ∈ ℚ_{>0}; π is a kernel-verified proof of
  BallPos(A/DEN, δ): every symmetric M ∈ ℚ^{m×m} with |M − A/DEN|_∞ ≤ δ satisfies
  xᵀMx > 0 for x ≠ 0; and β (the bridge) is a proposition, with stated trust base,
  that the true stage matrix Q^{𝔅}_L satisfies |Q^{𝔅}_L − A/DEN|_∞ ≤ δ′ for a stated
  δ′ ≤ δ. The *conclusion* of 𝒞 is concl(𝒞): λ_{V_𝔅}(L) > 0.
- *Morphisms* 𝒞 → 𝒟: witnesses that (L_𝒞, V_𝒞) ≤ (L_𝒟, V_𝒟) in the stage order, i.e.
  L_𝒞 ≤ L_𝒟 and ι_{L_𝒞, L_𝒟}(V_𝒞) ⊆ V_𝒟, together with the exact base-change matrix.
  Composition is composition of inclusions.

Then: (i) *Soundness.* concl is a functor Cert → (Prop, ⟸): if 𝒞 → 𝒟 then
concl(𝒟) ⟹ concl(𝒞), by restriction of positive-definite forms along ι (which preserves
Q exactly). (ii) *Coherence (the composable-bridges law).* Any two objects joined by a
morphism satisfy the compatibility inequality on the common block, in basis-matched
coordinates: |A_𝒞/DEN_𝒞 − Res(A_𝒟/DEN_𝒟)|_∞ ≤ δ′_𝒞 + δ′_𝒟. Violation proves at least one
bridge false as stated. (iii) *Closure.* If the certified objects contain a chain whose
stage system (V_n) satisfies Lemma 1's hypotheses (nested, cofinal, exhausting), then
"all rungs certified with margin" ⟹ RH by Lemma 1(iii); conversely under RH such an
all-certified chain exists (each strict rational-ball positivity is verifiable at finite
precision). The chain is a *finite proof* iff it is generated by a base object and a
certified step — a morphism out of a natural-numbers object in Cert (Lambek–Scott) — and
the analytic content of the step is the §3 transfer inequality: **UPT = the recursion
generator exists.** (iv) *Compactness form of Track B's hypothesis.* Fix a complexity
bound B in envelope-normalized units and let 𝒲_n be the (finite) set of valid certificate
objects at stage n with data-size ≤ B, with the restriction maps of (ii). If every 𝒲_n is
nonempty, then the inverse limit is nonempty (finite branching; König), i.e. a single
coherent infinite certificate tower exists. Boundedness of normalized complexity is the
entire content; this is the precise form of §4-Track-B's "bounded certificate size per
window is the transfer lemma in machine-readable form".

**(b) Proof strategy.** (i) restriction of PD forms to subspaces, plus Q_{L′}∘ι = Q_L.
(ii) triangle inequality between the two bridges through the common true matrix; the
base-change matrix makes "common block" exact. (iii) Lemma 1(iii) plus: a true strict
positivity of a ball around a rational matrix is witnessed at some finite interval
precision (monotone convergence of outward-rounded enclosures); NNO ⟺ induction is
standard categorical logic. (iv) König's lemma for finitely-branching trees of nonempty
finite sets. All proofs are short; I can write them in full.

**(c) Hardest missing step.** None inside the lemma — by design it quarantines the open
mathematics into the recursion generator (the step certificate), which is UPT itself. The
honest limitation: (iii)-converse produces a tower, not an algorithmically enumerable one
with known rate; the rate is again the envelope (Lemma 4).

**(d) Difficulty.** Easy as mathematics; its value is that the repo's Lean artifacts
already instantiate it, and the coherence law (ii) has teeth — see (e), where it caught
a real breach.

**(e) Concrete check against the repo — EXECUTED, with a finding.** The four kernel
artifacts are objects of Cert: `WeilCert` (ζ, L = 497/200, m = 12, DEN = 10²⁴,
δ = 10⁻²⁰), `WeilCertDeep` (same L, m = 24, DEN = 10²⁸, δ = 10⁻¹⁴), `WeilCertDeeper`
(ζ, L = 749/250, m = 48, DEN = 10³⁰, δ = 10⁻¹⁹), `WeilCertFamily` (χ₋₇, L = 5, m = 16,
DEN = 10²⁴, δ = 10⁻⁹). Because zero-extended polynomials are not polynomials, the
Legendre stages at different L are not nested: the diagram has exactly one nontrivial
morphism, WeilCert → WeilCertDeep (P₀..P₁₁ ⊂ P₀..P₂₃ at the same L) — across windows it
is discrete, which is itself the Lemma-1(v) diagnosis of the current artifact set.
I checked the coherence law (ii) on that one morphism [computed here, exact rational
arithmetic on the Lean integer data]:

- max |mRat₁₂ − mRat₂₄| on the leading 12×12 block = **1.4579e−17** (at entry (6,6));
  all 72 parity-allowed entries differ by more than 10⁻²⁴; the 72 parity-zero entries
  agree exactly.
- Stated budgets: ≤ 5e−60 enclosure + 5e−25 rounding for m = 12 (`THEOREMS.md`, Bridge
  Proposition) and ≤ 4.9e−29 for m = 24 (file header). Coherence bound ≈ 5.5e−25.
  **Violation by ≈ 7.5 orders of magnitude: at least one bridge is false as stated.**
- Attribution [computed here]: the discrepancies are bounded by 1.49e−16 *relative* to
  entry size (max over the block; 2⁻⁵³ = 1.11e−16), and re-simulating the m = 12 emission
  from the m = 24 midpoints through a dps-15 float bottleneck reproduces the emitted
  24-digit integers of `Weilcert.lean` exactly at 121 of 144 entries. The cause is
  visible in `lean/make_certificate.py` line 19: the 220-bit interval endpoints are
  passed through `mp.mpf` at ambient precision before rounding, and the `mp.mp.dps = 50`
  in `src/certified_spectral.py` sits inside the `__main__` demo block, so the import
  path runs at dps 15. The deep generator (`lean/make_certificate_deep.py`) rounds in
  exact `Fraction` arithmetic and is clean.
- Consequences, typed carefully: the kernel theorem `WeilCert.weil_window_positive` is
  intact (it is a true statement about its stated ball); but the m = 12 **Bridge
  Proposition's budget is false as stated**, and since 1.46e−17 ≫ δ = 10⁻²⁰, the true
  Galerkin matrix lies *outside* the certified ball: the m = 12 formal chain to ζ breaks
  at the bridge. The intended corollary survives anyway **through the morphism**: the
  m = 24 ball (δ = 10⁻¹⁴ ≫ its honest identification error) contains the true 24×24
  matrix, and positive-definiteness restricts to the 12-dimensional subspace. The
  category repaired what it caught. Repair options (either is minutes): re-emit m = 12
  with exact rounding, or re-certify with δ ≥ 10⁻¹² (the stage margin 7.5308e−8 supports
  any δ < 7.5e−8/12 ≈ 6e−9 through the m·δ shift construction).
- Program recommendation: promote coherence checking to a standing oracle — every new
  certificate is interval-compared on common blocks against every comparable existing
  one. Note for the pathology ledger: this breach was invisible to all five per-artifact
  validation layers and was caught only by demanding that two artifacts *compose*; call
  it the first categorical oracle save (fifth entry in the catastrophe ledger, benign
  and repairable).

---

### Lemma 4 (The envelope prices the ladder: a precision floor for ball certificates)

**(a) Statement.** (i) If BallPos(N, δ) holds then δ < λ_min(N); moreover the repo's
shift construction (B = A − S·I with S = m·DEN·δ) requires λ_min(A/DEN) > m·δ. (ii) If in
addition a bridge places the true stage matrix Q^{𝔅} within δ′ ≤ δ/2 of A/DEN, then
m·δ < λ_min(Q^{𝔅}) + m·δ′, hence δ < λ_min(Q^{𝔅})/(m − 1/2)·(1 + o(1)); at any stage that
resolves its window (λ_stage ≤ C·λ(L)), every valid certificate of the repo's type
satisfies

  log₁₀(1/δ) ≥ [1.755·e^{L/2}(L/2 + 4.0) − 10.2]/ln 10 − log₁₀(C·m) + O(1),

conditional on the measured envelope; DEN ≥ 1/(2δ′) is forced by the grid, so per-entry
integer size grows ∝ e^{L/2}·L digits and total certificate data ∝ m(L)²·e^{L/2}·L with
m(L) at least the Landau dimension of the window — empirically the Weyl staircase count
(measured 1 → 6 over L = 1.50 → 3.45 as successive γ_k cross T*(L)). **The measured
envelope is the complexity gauge of Track A's Curry–Howard ladder: it prices every future
rung in advance.**

**(b) Proof strategy.** (i): M = N − δI is in the ball, so λ_min(N) > δ; the m·δ variant
is the artifacts' own Cauchy–Schwarz bound |xᵀEx| ≤ m·δ·|x|² for entrywise perturbations
(sharp for E = −δ·ssᵀ, s a sign vector). (ii): eigenvalue perturbation plus substitution
of the envelope; the envelope input is measured, so the displayed bound is conditional
and flagged as such. Complete otherwise.

**(c) Hardest missing step.** None; the only conditionality is the envelope law itself,
which is the program's central measured object.

**(d) Difficulty.** Easy. Its value is operational: it converts the envelope from a
descriptive law into an a-priori budget for Tracks A and B.

**(e) Concrete check against the repo — verified across all four Lean rungs**
[computed here from the artifact data, stage margins from `results/RESULTS.md`]:

| rung | m | δ | m·δ | stage margin | slack = margin/(m·δ) |
|---|---|---|---|---|---|
| WeilCert (ζ, 497/200) | 12 | 1e−20 | 1.2e−19 | 7.5308e−8 | 6.3e11 |
| WeilCertDeep (ζ, 497/200) | 24 | 1e−14 | 2.4e−13 | 3.86882e−10 | 1.6e3 |
| WeilCertDeeper (ζ, 749/250) | 48 | 1e−19 | 4.8e−18 | 4.3462e−15 | 9.1e2 |
| WeilCertFamily (χ₋₇, 5) | 16 | 1e−9 | 1.6e−8 | ≥ 7.5699e−7 | ≥ 47 |

The floor is respected at every rung and the slack has collapsed 6.3e11 → 47 as the
ladder deepened: the artifacts are already converging onto the information-theoretic
floor, as the lemma predicts. One flagged anomaly for the CS seat: the exact-fraction
LDLᵀ inside the generators inflates the congruence integers far beyond the floor (cInt at
m = 24 is ≈ 4,600 digits against a ≈ 30-digit floor) — roughly two orders of compression
are available from rounded/rescaled factorizations, which matters before anyone attempts
rungs near L ≈ 6 (margins ~1e−31 by the envelope; family analog measured 2.5363e−31 at
q = 3, L = 6).

---

## 3. Predictions

Structural constraints this framing places on what the other seats will likely propose.

1. **Any proposed normalization N_p must be a function of the aspect ratio e^{L/2} alone
   (equivalently of T*), scale-invariant in the sense of Lemma 2(i)–(ii).** Proposals
   referencing threshold distance dist(L, ∂W_p) are doubly dead — killed at operator
   level by the measured non-collapse (§2.15) and by the Glide Theorem; proposals
   referencing absolute position of the window violate proved translation invariance.

2. **Any derivation of b ≈ 1.755 and the +4.0 offset must factor through the counting
   function N(T) only.** The §2.17 mechanism experiment (smooth staircase matches the
   true zeros within truncation; Poisson costs 1.5–2 orders; all three share the slope)
   forbids derivations of the *decay constant* that consume GUE pair correlation or
   prime-side arithmetic; those inputs may lawfully appear only in the offset. Expect the
   analytic seat to propose Landau–Widom/prolate asymptotics — that is consistent, and
   the model-ladder gauge of §1 is the clean place for it to land.

3. **Interlacing/free-probability proposals (Track C) will need exactly two case
   families, not infinitely many.** By Lemma 2(iii) the per-prime updates are matrix
   coefficients of the site action, conjugate under scaling; what distinguishes cases is
   (sign pattern χ(n), participation n < ρ) — and the pole, the unique non-quasilocal,
   rank-2 term, must be carried as a separate global summand (it cannot be absorbed into
   any local/banded perturbation scheme). An MSS-style averaging over prime subsets is an
   average over the divisor lattice of the truncated monoid; the individual-vs-ensemble
   gap they must bridge is a colimit-vs-object gap, not a member-vs-ensemble gap.

4. **The formal-methods seat should stop adding independent rungs.** By Lemma 3(iii) no
   finite set of per-window artifacts can close the ladder; by Lemma 4 the marginal cost
   of rung L grows like e^{L/2}·L digits. The leverage object is the *step certificate*
   (a certified implication between consecutive nested stages) plus the bridge-coherence
   oracle of Lemma 3(e) — which has already caught one real breach that per-artifact
   verification missed. Prediction: if they formalize anything next, the cheapest
   permanent value is (a) the coherence checker, (b) re-emission of `Weilcert.lean` with
   exact rounding.

5. **SOS mining (Track B) will find nothing stable per-window in the current bases.**
   Certificate structure can only be compared along morphisms; the per-window Legendre
   objects are pairwise incomparable (no nesting), so "certificate structure across
   thresholds" is undefined in the current artifact set. Mine in a nested hp system
   (Lemma 1(iv)) and look for the step morphism (near-block-triangular relation between
   consecutive W factors on the common subspace); Lemma 4 gives the a-priori size budget,
   and the observed 150× integer-size overshoot says current certificates are far from
   canonical form.

6. **Object candidates (Track E) are constrained through two functors only.** Any
   Hilbert–Pólya candidate is auditioned by (density functor, rigidity offset) — nothing
   finer is visible at frame-bound level (§2.17) — and any F₁/site-theoretic candidate
   must reproduce Lemma 2(iii)'s shape: arithmetic = matrix coefficients of the monoid
   action, pole = the unique global rank-2 term, envelope defined over the density
   skeleton with arithmetic in the offset.

---

## 4. Interfaces

**Needs.**
- *From analytic number theory:* (n1) Landau–Widom/Sonin asymptotics for the model
  ladder margin λ_mod(L) (smooth-staircase frame bound) — the provable half of the
  normalized UPT of §1; (n2) the classical Beurling–Landau strictness input for Lemma
  1(iii) in citable, constants-explicit form; (n3) any known comparison principle
  between frame bounds of two separated sequences with equal counting functions and
  different rigidity — the shape of the missing constant c.
- *From computer science / formal methods:* (c1) interval-verified digamma/Bernoulli
  enclosures in mathlib (the declared Bridge gap of `THEOREMS.md`); (c2) implementation
  of the Cert coherence oracle (Lemma 3(e)) and the exact-rounding re-emission of
  `Weilcert.lean`; (c3) a design for step certificates as a Lean-checked implication
  schema (the NNO morphism), consuming Lemma 1's nested hp stages.
- *From algebraic geometry / F₁:* (a1) whether the pre-cosheaf of Lemma 2 extends to a
  sheaf-theoretic object on the scaling topos in Connes–Consani's own terms, and whether
  their archimedean Sonin-space positivity (Connes–Consani, "Weil positivity and trace
  formula: the archimedean place", Selecta Math. 27 (2021), arXiv:2006.13771) can be
  written as a positive square *of cosheaf maps*, so that prime addition becomes
  "extending a positive square along one monoid generator"; (a2) the tropical/idempotent
  structure sheaf's role, if any, for the envelope's (T*/2π)(ln(T*/2π)+4) shape.

**Offers.**
- The strict-ladder specification and the single-staircase reduction (Lemma 1): one
  monotone certified invariant replacing the (L, m) grid, with the hp basis spec
  including kink-adapted meshes.
- The Cert category specification with soundness/coherence proofs (Lemma 3) — already
  field-tested: it found and repaired the m = 12 bridge breach.
- The complexity floor (Lemma 4) as an a-priori budget for all certificate work.
- The site-descent statement (Lemma 2) as a common index category for all seats.

**Named compositions.**
- **Lemma 2 ∘ (a1):** if CC's archimedean square is a cosheaf square, Track C's prime
  addition is extension of a positive square along U_p — the categorical shape of M3
  ("transfer on prolate subspaces").
- **Lemma 1 ∘ (n1):** the normalized staircase s_n/λ_mod(L_n) — M2's gate ("is f(p)
  bounded below after normalization?") becomes a single-sequence question with the
  measured envelope as the null hypothesis.
- **Lemma 3(iv) ∘ Track B mining ∘ (c3):** bounded-complexity certificate search with
  König compactness behind it: either a step schema materializes (UPT in machine form)
  or complexity growth is itself the obstruction data, quantified by Lemma 4.
- **Lemma 3(iii) ∘ Track F:** locate the step implication's proof-theoretic strength
  (if the step is provable in ACA₀, the folklore "if provable by ordinary analysis then
  provable in arithmetic" applies to UPT itself) — cartography, per Track F's mandate.

---

## 5. Honest assessment

**The strongest objection: positivity is not categorical.** The natural categorified
homes of quadratic forms — Witt groups, Grothendieck–Witt, L-theory, Poincaré
∞-categories (Lurie's L-theory lectures; Calmès–Dotto–Harpaz–Hebestreit–Land–Moi–
Nardin–Nikolaus–Steimle) — invert or quotient exactly the information that matters here:
definiteness is not an invariant of any of the equivalences those theories respect. Worse,
the program's own measurements show the colimit object sits *on the boundary* of the
positivity cone (certified inf ≤ 1.8e−20, descending to ~1e−40 measured): there is no
open categorical condition to transport, and every exactness statement I can prove
(Lemmas 1, 3, 4) is soft — the strict content of RH-by-this-route is one analytic
comparison inequality (the gauge/model-ladder domination of §1) plus one recursion
generator (the step certificate), and category theory proves neither. If the
collaboration hoped this seat would produce the transfer inequality, the answer is no,
and I say so plainly.

**Second objection: the F₁/scaling-site content may be decoration.** Lemma 2 uses only
the abelian ℝ^×_+-invariance of the explicit formula — one line of Fourier bookkeeping —
and none of Connes–Consani's actual depth (tropical structure sheaf, Sonin spaces, the
square of the site). The genuine alignment is single but real: the prime terms are
matrix coefficients of the very monoid action that defines their site, and the
participation rule is the site's overlap condition — the semilocal trace formula and this
program's truncation are looking through the same keyhole. Whether that alignment can be
made to *carry weight* (a1 above) is a question I hand to the AG seat, without promising
its answer is yes.

**Third objection: the proved lemmas are graduate exercises.** True. Their defense is
retrodictive and operational, not mathematical depth: (1) both of the program's measured
self-corrections — the threshold knife-edge (§2.7 → §2.15) and the m = 101 plateau
(§2.8 → §2.14) — were instances of reading non-nested stage data as if it were an
invariant of the ladder functor, which Lemma 1(v) makes impossible to repeat, and Lemma
1(iv) supplies the basis family on which the mistake cannot arise; (2) the coherence law
of Lemma 3 found a real breach (double-precision bottleneck in `make_certificate.py`,
bridge budget off by ~7.5 orders, `Weilcert.lean`'s ball missing the true matrix) that
five layers of per-artifact validation missed, and simultaneously exhibited the repair
(restriction from the m = 24 object); (3) Lemma 4 turns the envelope into an a-priori
budget, which is what an engineering program needs from its theory seat. That is
bookkeeping — with consequences. On the brief's own terms (option d): after honest
analysis, this field's sharp contribution toward a *proof* is limited to the
reformulation "UPT = gauge comparison against a zeta-free model ladder + a recursion
generator for its certificates", and the best organizational lemmas above. I believe
those two residues are the correct coordinates of the door, and that they were worth one
consultant's day — but the door itself will be opened, if at all, by the analysis, not
by the bookkeeping.
