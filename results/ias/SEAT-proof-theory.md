# SEAT — Proof Theory / Mathematical Logic (Round 1, independent)

Seat of the 8-seat maximum-variance panel. Written 2026-07-26 against: PROGRAM.md
(§§2.14–2.20, §3, §4 Track F), RH-LEMMA-MAP.md, results/RESULTS.md,
results/experts/SYNTHESIS.md (incl. errata + §5 kill list), results/experts/FULLINF.md,
results/experts/T1PRIME.md, results/experts/PLAN-computer-science.md,
lean/README-verify.md, and a direct audit of the repo's pinned mathlib checkout
(`lean/weilcert/.lake/packages/mathlib`, commit `520045ab14`, 2026-07-23 — same commit
as the glide project's snapshot). No other results/ias/SEAT-*.md was read.

Honesty tiers used throughout: THEOREM / COMPUTED / CONJECTURE / SPECULATION.
"AUDITED" marks facts I verified by grep/read in the pinned mathlib this session.

---

## §0 Seat card

Toolkit: proof mining (Kohlenbach-school metatheorems: bound extraction, monotone
functional interpretation, majorizability); reverse mathematics (RCA₀/WKL₀/ACA₀
calibration, conservativity); provability logic and Gödel phenomena (Σ₁-completeness,
Löb, speed-up); proof complexity (lower bounds against restricted proof systems,
SOS/Positivstellensatz degree bounds); formal verification foundations (Lean kernel,
mathlib anatomy, arithmetization-in-proof-assistants state of the art). I treat the
program's instruments as a proof system that has been measuring its own proof sizes.

---

## §1 Translation: the program in proof-theoretic coordinates

**1.1 The Π₁ collapse, stated exactly (the preamble of RH-LEMMA-MAP is correct).**
RH is Π⁰₁: classical routes are Kreisel's error-term arithmetization (Kreisel 1952),
the Davis–Matiyasevich–Robinson explicit Π₁ form (DMR, *Proc. Sympos. Pure Math.* 28,
1976, §8), and Lagarias' elementary equivalent σ(n) ≤ H_n + e^{H_n}ln H_n (Lagarias,
*Amer. Math. Monthly* 109 (2002) 534–543). Hence, provably in PA via provable
Σ₁-completeness: ¬Prov_ZFC(⌜¬RH⌝) → RH, and Indep_ZFC(RH) → RH ∧ Con(ZFC). Track F's
framing is right; §2 (PT-1) specs the Lean artifact at file granularity. Two honesty
riders the repo should carry:

- (i) Lean + mathlib is *stronger* than ZFC (consistency strength ≈ ZFC + ω
  inaccessibles; Carneiro, *The Type Theory of Lean*, 2019). "Kernel-checked" claims
  are theorems of that stronger system. For Π₁ targets this is epistemically inert
  modulo consistency, but the transfer theorem must be stated so that no
  Lean-proves-it ⇒ ZFC-proves-it metatheorem is smuggled in (PT-1 is engineered to
  avoid exactly that trap; see the Tier-1/Tier-2 split).
- (ii) Shoenfield absoluteness (all models of ZFC with standard ω, indeed all
  Σ¹₂-absoluteness contexts, agree on RH) is a *far* formalization target: mathlib has
  a ZF-sets model (`Mathlib/SetTheory/ZFC/`) but no coded proof predicate, no forcing
  (Flypitch, Han–van Doorn 2019-20, did forcing in Lean 3; never ported — UNVERIFIED
  whether any Lean 4 port exists). Track F(i) does not need it; do not let it creep
  into scope.

**1.2 The window family as a Δ₁ family, and where the Π₁-ification really lives.**
Each finite window statement (rational L, Galerkin dimension m) is decidable, and the
repo has *kernel-checked instances* (Level 0 of RH-LEMMA-MAP: `weil_window_positive`
at four ζ/χ windows; `CurveCertE5`; `HardHorizon`). The full criterion "λ(L) ≥ 0 for
all L" quantifies over test functions; the clean arithmetic Π₁-ification of the Weil
side is the ∀m reduction:

  λ(L) ≥ 0 ⟺ ∀m: λ_m(L) ≥ 0 (Galerkin minima, nested V_m, λ_m ↓ λ),

and each "λ_m(L) ≥ 0" is Π₁ because λ_m(L) is a *two-sidedly computable* real — the
repo's certified enclosures (RESULTS.md, hat + spectral certificate tables) are the
constructive content of that claim, live code. CONJECTURE (small, checkable): the
density step (polynomials dense in the form domain, so λ_m ↓ λ) holds with the graph
norm of Q_L; FULLINF F0 gives the frequency-side representation needed. NOTE the
asymmetry: λ(L) itself is today only provably upper-semicomputable (lower rates =
the truncation IOU T(m,L), PLAN-computer-science CS-3(c)); the ∀m trick bypasses
this, which is why the Π₁ form should be stated over (L, m) pairs, never over λ(L).
The Σ₁ (disproof) side is exactly the program's kill criterion: a certified negative
interval-Rayleigh upper bound at one rational rung. The instruments' native
disproof-friendliness (PROGRAM §6) *is* Π₁-ness, with the constants supplied by
CS-4(iv) (disproof poly(γ_b) vs positivity exp(Θ(e^{L/2}L)) — cite, don't redo).

**1.3 The envelope law is a proof-size law.** CS-1(v) (THEOREM, two lines, sharp to
0.997 measured — SYNTHESIS Q5 SETTLED) forces every entrywise-ball certificate at
window L to carry DENP > log₁₀(1/λ(L)) digits per entry; the measured envelope
(mid-range ln λ ≈ 10.2 − 1.755e^{L/2}(L/2+4), 4π-cap deep, PROGRAM §2.20) therefore
*is* a lower-bound curve on proof size in that system. §2 (PT-3) turns this into a
formal speed-up statement and a small kernel-checkable lower-bound artifact.

**1.4 F5 is a fragment-unprovability theorem waiting to be stated as one.** FULLINF
Theorem F5 (THEOREM as stated there): every "certified subspace + a-priori tail"
assembly driven by the form's own logarithmic coercivity (W₊ ≤ C_B* ≈ 10.3 at
L = 7/4, THEOREMS.md Lemma B(iv), sharp by A(iv)) has error ≥ ≈2.8 — five orders
above every margin. Read as metamathematics: F5 is a *size/soundness lower bound
against a restricted proof calculus*, in the exact genre of SOS degree lower bounds
(Grigoriev, *Theor. Comput. Sci.* 259 (2001) 613–622, knapsack/parity). What F5 is
not yet is a *semantic* unprovability theorem (soundness + countermodel). PT-2 below
claims the countermodel is essentially already in FULLINF's own F6 data, and that the
missing "a-priori regularity theorem" of FULLINF §10 is precisely the axiom that
re-injects the support constraint the template's interface forgets.

**1.5 Reverse-mathematics location of the new corpus (seed (d)).**
- Hard Horizon Theorem T1′, staircase form (kernel-checked, `HardHorizon.lean`; paper
  T1PRIME.md §2–3): the proof is Jensen's formula + FTC + explicit constants — no
  compactness, no completeness theory ("Jensen + calculus", T1PRIME §3 audit).
  CONJECTURE (high confidence): T1′-staircase and Corollary 2 are provable in RCA₀
  as-is; Corollary 1 adds Trudgian's S(T) bound (explicit analytic NT), still
  RCA₀/WKL₀-grade. The Lean artifact is strong evidence: nothing in it uses more than
  Δ⁰₁-explicit objects. This is the honest RM headline: *the program's provable
  frontier is logically shallow* — which is good news (see 1.6).
- "Envelope holds for all L" (two-sided, staircase class — SYNTHESIS T5): a true
  Π₂-flavored statement about explicitly coded objects. My answer to seed (d)'s
  equivalence question is NO: no reversal to a known RM principle is plausible,
  because no set-existence axiom is exercised — candidate proofs (DG/HA routes in
  SYNTHESIS T5) are explicit-constants constructions. The only place genuine RM
  strength could enter the program is minimizer *existence* (weak sequential
  compactness of the L² ball ≡ Bolzano–Weierstrass territory ≡ ACA₀, Simpson SOSOA
  III.2/X.2) — e.g. if the F5-missing regularity theorem is proved via an
  eigenfunction-bootstrap on an actual minimizer. And even then: RH is Π₁, ACA₀ is
  conservative over PA for arithmetic sentences, WKL₀ over PRA for Π₂
  (Friedman/Harrington; Simpson IX.3), so no net strength survives to the
  conclusion. Folklore made precise: if RH is provable by the ordinary analysis this
  program uses, it is provable in PA — and given the PNT precedents in weak systems
  (Sudac, *Theor. Comput. Sci.* 257 (2001): PNT in I∆₀+exp-adjacent systems;
  Cornaros–Dimitracopoulos), plausibly far lower. Track F(iii)'s conservativity
  deliverable can cite rather than reprove all of this.

**1.6 Proof mining: where a regularity theorem must come from (seed (b), second
half).** "inf over the unrestricted unit ball of Q_L is ≥ 0" per L is ∀-only, so
proof mining's guaranteed-extraction metatheorems (Kohlenbach, *Applied Proof
Theory*, 2008, Ch. 15–17) are trivial on it; the extractive content sits in the
statements with ∃-margins: "λ(L) > 0" (Σ over the reals) and UPT itself
("∃ normalization + ∃c > 0 uniform"). Monotone functional interpretation applies to
proofs of such statements in WE-PA^ω + QF-AC + WKL and delivers *majorizing moduli*
uniform in all majorizable parameters. Two consequences, stated as claims:

- (i) CONJECTURE (metatheorem application, checkable by a specialist in weeks): any
  classical proof of "∀L: inf_{‖φ‖=1, supp φ ⊆ I_L} Q_L(φ) > 0" formalizable in the
  usual extractive systems yields a *computable* lower-bound modulus f(L) > 0. The
  program's envelope then prices every future proof: the extracted f must satisfy
  f(L) ≤ λ(L) ≈ exp(−4π e^{L/2}(1+o(1))) — the measurements are a *moduli forecast*
  for a theorem that does not exist yet. No other RH program has this.
- (ii) The necessity twist (PT-2(iii) below): since the (Galerkin data + W₊ budget)
  interface provably cannot certify positivity (F5, semanticized in PT-2), any
  extractable proof must carry a modulus of some *additional* a-priori property of
  near-minimizers — and the only candidate property the form's support constraint
  offers is frequency decay. FULLINF §10's "best guess at the shape of the missing
  mathematics" is thus not a guess: in moduli form, a support-to-frequency-decay
  regularity statement is *forced* to appear inside any classical proof of
  unrestricted positivity. Proof mining converts the wall into a specification.

**1.7 What "kernel-checked" buys Track F.** The repo's Level-0 artifacts are proofs
in a fixed strong system with audited axiom sets ([propext, Classical.choice,
Quot.sound] only — lean/README-verify.md). For the transfer theorem, what matters is
subtler: the *statement* ¬Prov_ZFC(·) is about a coded proof predicate, an object
mathlib does not have at all (audit, §5). The person-day map in PT-1 is built on that
audit, not on optimism.

---

## §2 Candidates

### PT-1 (Track F(i), the Lean spec): the Transfer Theorem at file granularity

**Statement architecture (Tier 1, finishable).** Fix a Σ₁ arithmetic sentence
`Cert` ("a certified computation detects an off-critical-line zero"; format below).
Formalize, in one Lean project importing both mathlib and a logic library:

  (T1-a) `theorem transfer (T : Theory L_arith) (hT : RecursivelyAxiomatized T)
          (hQ : Q_sub T) : ¬ Provable T ⌜Cert⌝ → RiemannHypothesis`

  via the contrapositive chain ¬RH ⟹ Cert is true in ℕ ⟹ T ⊢ Cert
  (semantic Σ₁-completeness of any r.e. T ⊇ Q). Corollary, one day:
  `Indep T ⌜Cert⌝ → RiemannHypothesis ∧ Con T`.

Crucially, Tier 1 states the hypothesis on `Cert`, **not** on a set-theoretic ¬RH
sentence. That choice removes the two poison pills: (1) no coded ZFC-derivation of
"Cert → ¬RH_set" is needed (which would require proof-translation infrastructure that
does not exist); (2) only the *completeness* direction ¬RH ⟹ Cert is needed in Lean —
the soundness direction (Cert ⟹ ¬RH) never enters the transfer proof. Soundness is
still worth having (it is the formal disproof-verifier, Track D), but it is severable.

**Which Π₁ formulation minimizes the burden (seed (a)'s sharp question).** Four
candidates, judged against the AUDITED mathlib snapshot:

| Π₁/Σ₁ form | needs (long poles) | verdict |
|---|---|---|
| **Jensen-disk certificate** (new proposal): Cert = ∃ rationals (c, r, k), Re c > 1/2, disk D̄(c,r) ⊂ {Re > 1/2}, such that the certified evaluator at precision k verifies circleAverage(ln‖ζ‖, c, r) − ln‖ζ(c)‖ > 0 | certified ℚ-interval ζ-evaluator on disks in the strip (Euler–Maclaurin with explicit remainder), proven against `riemannZeta`; Jensen — **already in mathlib** (`Analysis/Complex/JensenFormula.lean`, `MeromorphicOn.circleAverage_log_norm`; AUDITED) and already exercised by this repo's HardHorizon build | **minimal for the transfer theorem.** Completeness direction needs only: FE reflection (`riemannZeta_one_sub`, AUDITED), nonvanishing Re ≥ 1 (`riemannZeta_ne_zero_of_one_le_re`, AUDITED), zero discreteness (`riemannZetaZeros` + `IsCompact.inter_riemannZetaZeros_finite`, AUDITED — new file, 2026), Jensen, evaluator convergence. **No explicit formula, no Robin, no argument principle** (which mathlib lacks — §5) |
| Repo-native Weil-window form: Cert = certified negative rung (interval-Rayleigh) at rational (L, m) | Level 4 of RH-LEMMA-MAP: Guinand–Weil in Lean ("research-grade, many months") + converse-Weil quantitative (NT-4) + the ∀m density lemma (§1.2) | larger for the transfer *alone*, but the cost is **shared** with the program's own Level 4; if Level 4 gets built anyway, this becomes the preferred form (the Σ₁ witness format is then literally the program's kill criterion) |
| DMR Π₁ form | its own bespoke effective explicit-formula analysis (η-criterion) | dominated: all the analysis, none of the reuse |
| Lagarias/Robin | Robin's theorem formalized (explicit-formula + Nicolas machinery, none in mathlib or PrimeNumberTheoremAnd per T1PRIME §7's audit of the RvM gap) | dominated; hardest of the four |

Recommendation: Tier 1 on the Jensen-disk form now; restate on the Weil form when/if
Level 4 lands (the transfer theorem is form-agnostic — two Cert instances, same glue).

**Mathlib-today inventory for the logic half (AUDITED, commit 520045ab14).**
Present: `Mathlib/Logic/Godel/GodelBetaFunction.lean` (β-function sequence coding —
the seed of representability, nothing more); `Computability/` (Partrec, `Nat.Partrec.Code`,
halting problem, Rice, `REPred`, reducibility + `TuringDegree`, `RecursiveIn`);
`NumberTheory/Dioph.lean` + `PellMatiyasevic.lean` (Matiyasevich's `pow_dioph`;
**no** full DPRM — no theorem "every r.e. set is Diophantine", confirmed §5);
`ModelTheory/` (FOL syntax/semantics, `Encoding.lean` Gödel-numbering of
terms/formulas, compactness via ultraproducts, new `Arithmetic/Presburger/` with
Definability/Semilinear). Absent: any syntactic proof calculus with a derivability
predicate (§5, T1 confirmed); any provability/consistency arithmetization; the
arithmetical hierarchy; Σ₁-completeness in any form; incompleteness.
So mathlib alone cannot state `Provable T ⌜Cert⌝` today.

External substrate: the **FormalizedFormalLogic/Foundation** library (Lean 4, builds
on mathlib) has FOL with derivations + Gödel–Henkin completeness, arithmetics
(𝐈𝚺₁, PA), arithmetized metamathematics with the Hilbert–Bernays–Löb derivability
conditions, Gödel I & II for theories ⊇ 𝐈𝚺₁, Löb, and provability-logic (GL)
infrastructure [post-2024 state: last verified by me at the level of their 2024–25
announcements; exact current theorem list UNVERIFIED — first task below is a pin +
audit, half a day]. Semantic Σ₁-completeness over a parameterized r.e. T ⊇ Q is
either present or a short exercise over their calculus. Isabelle precedent for the
whole genre: Paulson's Gödel I & II (2013–14). DPRM precedents if the Diophantine
dress is ever wanted: Coq (Larchey-Wendling–Forster 2019), Isabelle (Bayer et al.).

**Person-day map (honest; single person familiar with mathlib analysis + one person
familiar with Foundation).**

| # | item | substrate | est. (pd) |
|---|---|---|---|
| F(i).0 | statement architecture; pin Foundation against a compatible mathlib; audit its Σ₁-completeness form | Foundation + mathlib | 3–6 |
| F(i).1 | **certified ζ evaluator** on rational disks in the strip: ℚ-interval arithmetic layer + Euler–Maclaurin (or η-series) with explicit remainders, correctness vs `riemannZeta`, convergence moduli | mathlib analysis | **60–120 (pacing item)** |
| F(i).2 | completeness lemma ¬RiemannHypothesis → Cert: FE reflection + conjugation symmetry, WLOG Re ρ > 1/2; discreteness ⟹ good disk + radius avoiding zeros; Jensen mass > 0; evaluator eventually confirms | mathlib (all named ingredients AUDITED present except the evaluator) | 15–30 |
| F(i).3 | arithmetization of Cert: the evaluator's decision at (c, r, k) as a computable/PR predicate on ℕ-codes; representability in Q/𝐈𝚺₁ | Foundation machinery (bespoke: β-function route, +30–50) | 20–40 |
| F(i).4 | semantic Σ₁-completeness instance for r.e. T ⊇ Q | Foundation (bespoke: 30–60) | 5–10 |
| F(i).5 | transfer glue + Indep → RH ∧ Con corollary + (optional) PA-internalized version via their D1–D3 | Foundation | 5–10 |
| F(i).6 | **Tier 2**: T = ZFC named in its own language — arithmetize L_∈-syntax, interpret Q in ZF (finitely many coded derivations of the Q-axiom translations + substitution bookkeeping) | Foundation-style, new | 40–80 |

Tier-1 total: **≈110–215 pd** Foundation-assisted; add ≈80–140 pd if the logic core
must be bespoke. Tier 2 adds 40–80 pd, or waits for Lean-proof-export tooling
(MM0/Lean4Lean direction, Carneiro — SPECULATION as an interface, not a plan).
Note the risk register: Foundation pins its own mathlib; if version alignment with
the analysis side fails, the project splits into two lake projects communicating
through a shared `Cert : ℕ → Prop` defined in core Lean — designed for from day one.

**Kill criteria.** (K-a) If F(i).1 exceeds ~150 pd of real effort, stop and re-scope
to the Weil-window Cert riding Level 4 (single shared long pole). (K-b) If
Foundation's Σ₁-completeness cannot be instantiated for a *parameterized* r.e. T
within F(i).4's budget, downgrade Tier 1 to T = 𝐈𝚺₁ fixed (still delivers the
inoculation artifact: any claimed independence-of-¬RH-over-anything ⊇ 𝐈𝚺₁ yields RH).
(K-c) The artifact is worthless if Cert's completeness direction silently assumes RH
somewhere (e.g. via a zero-free-region shortcut); the acceptance test is that F(i).2
compiles with `RiemannHypothesis` appearing *only* as the negated hypothesis.

**Value.** Pins the three-outcome landscape as a kernel-checked fact; permanently
disposes of the crank-independence failure mode; and F(i).1 is dual-use — it is the
program's formal disproof-*receiver* (the machine that would check the catastrophe if
Track D ever produces one), which is the strongest program-internal reason to build it.

### PT-2 (seed (b)): the Template Calculus Theorem — F5 as semantic unprovability

**Statement (to prove).** Define the *split-template calculus* 𝒯(m, R): a proof is a
finite chain of inequalities about a candidate pair (u, w) ∈ V_m × L²(ℝ), u = P_mφ,
w = φ − u, using only these axioms: (A1) certified Galerkin positivity
Q(u) ≥ λ_m^cert‖u‖²; (A2) the coercivity budget W₊(φ) ≤ C_B* (THEOREMS.md Lemma
B(iv)); (A3) the symbol envelope |Ω_L| ≤ Ω̄, Ω_L ≥ −c₋ (FULLINF F1); (A4)
capture/content estimates for V_m (FULLINF F2/F3); (A5) bilinear composition
(Cauchy–Schwarz, triangle, splitting at any finite set of cuts R). Then:

 (i) [soundness] every 𝒯-derivable lower bound on Q_L(φ) is valid for all unit
 φ ∈ H_L — this is just F4's skeleton, already proved;
 (ii) [countermodel = semantic wall] there exists a unit ψ ∈ L²(ℝ), *not supported
 in I_L*, whose interface data (P_mψ, tail mass, W₊(ψ), symbol integrals) satisfies
 every axiom instance available to 𝒯, with Q^{F0}(ψ) < 0 (Q extended to L²(ℝ) by the
 F0 formula). Hence no sound derivation from (A1)–(A5) alone can conclude
 inf_{H_L} Q ≥ 0: **the support constraint is invisible to the template's interface,
 and it is the load-bearing hypothesis.** F5's quantitative wall (error ≥ 2.8)
 becomes an unprovability theorem for the fragment;
 (iii) [necessity, via proof mining] any classical, extractable proof of
 unrestricted positivity must therefore carry a modulus of a near-minimizer property
 *outside* the interface; combined with the F0 frequency representation, that
 property is a support-to-frequency-decay modulus — FULLINF §10's a-priori
 regularity theorem, now *necessary* in moduli form, not just sufficient.

**Proof route (concrete, mostly assembled from FULLINF's own lemmas).** For (ii):
take u = the true Galerkin minimizer part, and w = ε · (gap-aligned packet): F6
proves u carries O(1) Fourier mass in the gap [0.66·m/a, m/a] where Ω̄ ≈ c₀ + log(2m/a);
choose ŵ = −sign(û Ω)·|û|·1_gap normalized, so the cross term achieves its
Cauchy–Schwarz value: B(u, w) ≈ −ε·√T₂-scale. Then Q(u + εw) ≈ λ_m − 2ε√(T₂-scale)
+ O(ε²c₋) < 0 already at ε ≈ λ_m/√T₂ ≈ 3.1×10⁻⁵/643 ≈ 5×10⁻⁸ (FULLINF §8 measured
√T₂ = 643 at (7/4, 192)), with W₊(w-part) ≈ ε²·log-scale — astronomically inside the
unconditional budget C_B* ≈ 10.3. All axiom instances hold for ψ = (u + εw)/‖·‖
because they never mention support. The pole-term bookkeeping (P(ψ) for
non-supported ψ via the F0 formula's analytic continuation of the e^{±x/2} moments)
is the one real check. COMPUTED pre-registration for the owning seat (NT/HA), not
run here: a numerical ψ built this way at (L, m) = (7/4, 192) will show
Q^{F0}(ψ) < −10⁻⁵ with interface data passing all A1–A4 instances; falsifier: if
*every* such packet keeps Q^{F0} ≥ 0, then the interface secretly implies positivity
and the regularity theorem is *derivable* from the template — an upside surprise
that would redirect the whole FULLINF program.

**Effort.** (i) days (it is F4 re-read); (ii) 2–4 weeks incl. the pole bookkeeping;
(iii) 2–3 weeks for a specialist to state the metatheorem application cleanly.
**Interfaces.** NT seat (F5/F6 owner), HA seat (Lemma A/B machinery), magic-functions
seat (§4, bet 1). **Kill criteria.** The packet computation above; and (iii) dies if
the eventual positivity proof is *not* formalizable in an extractive system (would
itself be a sensational logical datum). **Tier now:** (i) THEOREM (restatement);
(ii) CONJECTURE with explicit route; (iii) CONJECTURE (metatheorem application).

### PT-3 (seed (c)): the Window Speed-up Theorem and the Floor-Witness artifact

**Statement (three layers, decreasing certainty).**

 (a) THEOREM (assembled; write-up only): at every *built* window, unconditionally
 (resting on the certified interval-Rayleigh upper bounds, not the envelope): any
 sound entrywise-ball certificate at (L, m) has δ < λ_un/‖v‖₁² (CS-1(v)) and hence
 total size ≥ the CS-1 floors; numerically, no δ ≥ 10⁻²⁰ ball certificate exists at
 L = 711/200 (SYNTHESIS Q5, δ* = 4.489×10⁻²¹ — settled program law).

 (b) CONJECTURE-conditional THEOREM (conditional on the measured envelope/4π cap):
 in the ball-certificate proof system Π_ball, every proof of the window statement
 P(window L) has size ≥ exp(c·e^{L/2}) bits. Consequently, if ZFC ⊢ UPT by a proof π,
 then the family {P(n)} exhibits Gödel-type speed-up of ZFC over Π_ball
 (ZFC-proof sizes O(|π| + log n) by instantiation vs exp(c·√n̂)-scale in Π_ball) —
 the classical configuration of Gödel 1936 / Ehrenfeucht–Mycielski (*Bull. AMS* 77
 (1971) 366–367), here with *measured* constants. Answer to seed (c)'s question:
 yes — the program's own data already implies UPT, if provable at all, is not
 provable "window-by-window" through any proof whose window-instantiations factor
 through ball certificates; the uniform proof must carry O(1) information per window,
 i.e. an identity/factorization, not an estimate ledger. (Scope honesty, inherited
 from PLAN-computer-science §5: this binds one vehicle; escaping it is what proving
 RH means. The metamathematical content is calibrational, and it is real.)

 (c) Lean micro-artifact, new, cheap — **the Floor Witness**: kernel-check the
 *impossibility* statement at L = 711/200: exhibit rational v and the sign matrix Σ,
 and verify by exact rational arithmetic that M = A/DEN − 10⁻²⁰·Σ satisfies
 vᵀMv < 0, i.e. "no sound 1e−20-ball certificate exists at this window." One
 rational vector, `CertFramework` technology, far lighter than any positivity rung.
 To my knowledge this would be the program's (and possibly anyone's) first
 kernel-checked *proof-complexity lower bound* artifact for a live open-problem
 proof family.

**Effort.** (a) 3–5 days write-up; (b) 1–2 weeks (the formal system Π_ball must be
defined with the same care as PT-2's 𝒯 — one shared definitional section serves
both); (c) 3–6 days (data exists: the m = 40 eigenvector from the Q5 adjudication).
**Interfaces.** CS seat (owns CS-1/CS-3; this formalizes their §4-offer to Track F),
Lean track, CO seat (the v vector). **Kill criteria.** (c) is self-checking (kernel);
(b) dies wherever the envelope does — it inherits Q1/Q2's resolution and should cite
the 4π cap as measured, not as truth.

### PT-4 (seed (d) + Track F(ii)/(iii)): the strength map, done by citation

**Statement.** A short THEOREMS.md-style note (no new mathematics, high program
value): (i) T1′-staircase + zero-desert are RCA₀-formalizable [CONJECTURE, evidence =
the Lean artifact's own resource profile; a proof-theorist referee pass, days];
(ii) the conservativity chain for Π₁ targets (ACA₀→PA, WKL₀→PRA, with the PNT-in-weak-
systems precedents) — the precise content of "if provable by ordinary analysis, then
provable in arithmetic"; (iii) the moduli-forecast lemma of §1.6(i); (iv) the
independence-signature audit: the two known *natural* mechanisms for Π₂/Π₁
independence from PA-scale systems are fast-growing witness bounds
(Paris–Harrington/Goodstein genre) and consistency-coding diagonalization; the window
family has PR-bounded decision complexity Õ(n⁴) (CS-3) and doubly-exponential — i.e.
tame — certificate growth, so the *measured* corpus shows neither signature. Also
maintain (Track F(iv)) the machine bookkeeping: Yedidia–Aaronson 5,372 states
(*Complex Systems* 25, 2016), community-reduced to 744 states (O'Rear, 2016–17;
current record UNVERIFIED — a one-afternoon diligence item).
**Effort.** 1–2 weeks total, mostly scholarship. **Kill criterion.** None needed —
each clause is independently citable or cheaply refereed; retract any clause that
fails the referee pass.

---

## §3 Intuition pumps (all SPECULATION, labeled as such)

**IP-1: Window positivity behaves like partial consistency statements.** The family
P(n) with its measured exp(e^{L/2})-certificate floor is structurally parallel to
{Con_n(T)} (consistency up to proofs of size n), for which Pudlák proved
polynomial-ish lower and upper bounds on T-proof sizes (Pudlák, "On the length of
proofs of finitistic consistency statements", 1986/87). The zero-slack facts
(Rodgers–Tao Λ ≥ 0; the safety-factor decay to 1.0 in PROGRAM §2.12) are the analytic
face of the same phenomenon: nothing is provable "with room to spare." If one takes
the analogy seriously, the productive question is not "is RH independent" but "what
is the weakest natural theory in which the P(n) have short proofs" — a graded
provability ladder in place of a binary. A concrete probe exists: does P(n) have
short proofs in systems with stronger *analytic* axioms (e.g. explicit-formula-as-
axiom)? That is exactly the repo's oracle stack read as a proof system, and the
zero-side oracle's O(N(T*)) evaluation cost against the primal's exp(e^{L/2}) is a
measured exponential separation between "proofs from the zeros" and "proofs from the
primes" — the two sides of the explicit formula are proof systems of measurably
different strength for the same Π₁ family, which is, to this seat's knowledge, a
configuration without precedent in proof complexity. (COMPUTED inputs: C2/CO-1
witness sizes vs CS-1 primal sizes; the framing is the speculation.)

**IP-2: The envelope as an independence sniffer.** Natural PA-independence has a
growth-rate fingerprint (Ketonen–Solovay: Paris–Harrington forces
Ackermann-and-beyond witness growth). The program can *measure* the witness growth of
its own uniformities: the envelope, the m_env(L) law, the depth law are all
doubly-exponential — many floors below any independence-grade hierarchy. Standing
instrument proposal: if any future uniformity constant in this program is ever
measured to grow faster than every fixed tower of exponentials in the window index,
flag it — that would be the first empirical independence signature ever observed in
a natural problem. Its absence to date is (weak, heuristic) evidence *against* the
independence outcome and *for* the collapse branch being vacuously true.

**IP-3: Tier-2 by proof export, not by hand.** The blocked half of PT-1 (hypothesis
on ¬RH_set itself) needs a coded ZFC-derivation of "Cert → ¬RH_set". No human writes
that. But a Lean-to-ZFC proof exporter (MM0-style, Carneiro) applied to the F(i).2
soundness direction would *manufacture* it. If such tooling matures, Tier 2 collapses
from 40–80 pd of interpretation-grinding to an engineering run — and, more
grandly, every kernel-checked artifact in this repo becomes a certified
ZFC-provability fact, closing the §1.1(i) honesty gap wholesale. Worth a standing
watch, not a workstream.

**IP-4: What the speed-up theorem says the proof looks like.** PT-3(b) + K4
("envelope divides out of the VALUE, never the FORM") + the function-field laboratory
(UPT there IS dim H¹ < ∞, an identity, certificate = the L-polynomial — one O(1)
object per curve) jointly triangulate: the missing proof, if it exists, presents as a
*factorization identity with an O(1) description that specializes to every window*,
not as a scheme of per-window estimates. That is a proof-theoretic derivation of what
the program already believes for analytic reasons (§2.12's "uniform factorization
problem"), and it is why this seat's honest posterior puts more mass on "provable,
by an identity not yet written" than on "independent."

---

## §4 Cross-seat bets (ranked by confidence)

**B1 → magic-functions (HIGH).** PT-2(iii) says any proof of unrestricted positivity
must contain a support-recovery modulus — a quantitative statement that compact
support forces frequency-tail decay *for near-minimizers*. Fourier interpolation
(Radchenko–Viazovska genre) is the one modern technology whose entire content is
"support/vanishing data at a discrete set determines the function with explicit
remainders." Bet: the a-priori regularity theorem of FULLINF §10 is equivalent to an
interpolation-basis remainder bound adapted to the RvM staircase; their seat can
either produce the basis or show the density is wrong for it. Secondary bet: their
LP dual witnesses and my template countermodels are the same objects (both live in
"data consistent with the axioms, negative on the target"), so a failed LP bound at
some window would *constructively* hand PT-2 its ψ.

**B2 → quasicrystal (MEDIUM-HIGH).** PT-3(b)'s conclusion — O(1) information per
window or no proof — is a rigidity statement about summation formulas: crystalline-
measure / Lee–Yang structures are the only known mechanism generating infinitely many
positivity windows from one finite description (cf. the function-field side, where
the mechanism is Riemann–Roch finiteness). Bet: any UPT-shaped identity will present
as a crystalline-measure positivity (Kurasov–Sarnak-adjacent), and conversely their
seat's no-go results for crystalline measures with RvM-density support would be
genuine negative information about the whole identity route — worth soliciting
explicitly.

**B3 → log-gas (MEDIUM).** The RM/proof-mining analysis says the program's provable
frontier is explicit-constants analysis (RCA₀-grade), and SYNTHESIS T4's marginal law
(π²/2 per deleted zero) is the next constant to be *derived*. Bet: the one-defect
equilibrium computation they own is fully extractive (no compactness), hence will
formalize at the same grade as T1′ — I stake the claim that T4(i)'s rank-two secular
identity + the Coulomb-gas defect potential becomes the program's *second* analytic
Lean artifact within a quarter of being proved on paper, and I offer PT-4's referee
pass as the certification lane.

**B4 → renormalization (LOW-MEDIUM, intuition-grade).** The template calculus 𝒯 is a
truncated RG scheme: (A1) is the relevant/finite-dimensional sector, (A2)–(A4) the
irrelevant-tail bounds, and PT-2(ii) says the truncation *loses a conserved quantity*
(support) that the flow cannot regenerate. Bet: in a transfer-operator toy (dynamical
zeta with finite Markov partition standing in for the primes), the analogous
"support axiom" is the boundary condition selecting the physical eigenfunction, and
one can prove there that no finite-rank truncation scheme certifies positivity while
the full transfer operator does — a solvable model of F5-semantic. If their seat can
exhibit it, PT-2 gains a template and the panel gains a shared toy.

---

## §5 Pre-registered cheap test: the mathlib inventory audit (run this session)

Pre-registered (in-session, before grepping) four claims about the pinned mathlib
(`lean/weilcert/.lake/packages/mathlib`, commit `520045ab14`, 2026-07-23), then
checked by grep/read. Verbatim outcomes:

| # | claim (pre-registered) | outcome |
|---|---|---|
| T1 | no syntactic proof calculus with derivability for `FirstOrder.Language` (semantic satisfiability/compactness only) | **CONFIRMED** — no derivation/provability object anywhere in `ModelTheory/`; "completeness" hits are docstrings (Presburger axiomatization notes, Encoding TODO) |
| T2 | no arithmetical hierarchy, no arithmetized provability/consistency predicate | **CONFIRMED** — sole hit: `Logic/Godel/GodelBetaFunction.lean` (β-function only) |
| T3 | the argument principle is present in some form (Jensen/ValueDistribution cluster) | **FALSIFIED as stated** — no argument principle, no residue theorem, no Rouché (searched: `argPrinciple`, `winding`, `residue`, `Rouche` across `Analysis/`); what exists is Jensen's formula (`JensenFormula.lean`), `Meromorphic/Divisor`, `ValueDistribution/` (Cartan, First Main Theorem). I mis-predicted the frontier's exact edge; the PT-1 spec was therefore routed through Jensen, which IS present — and the miss is itself load-bearing information: *any* Π₁-certificate design for ζ-zeros that assumes winding-number machinery in mathlib is currently wrong |
| T4 | `Dioph.lean` stops short of full DPRM (no "every r.e. set is Diophantine") | **CONFIRMED** — `pow_dioph` (Matiyasevich's exponential step) is the terminal theorem; zero references to `Partrec`/`REPred` in the file |

Score 3/4, misses reported. Bonus AUDITED finds folded into PT-1: `riemannZetaZeros`
discreteness/compact-finiteness (new 2026 file `LSeries/ZetaZeros.lean`),
`riemannZeta_ne_zero_of_one_le_re` (`LSeries/Nonvanishing.lean`),
`riemannZeta_one_sub`, `Complex.digamma` (`Gamma/Digamma.lean`), Jensen
(`MeromorphicOn.circleAverage_log_norm`), and `ModelTheory/Arithmetic/Presburger/`
as evidence of a live (but still provability-free) arithmetic stream in mathlib.

---

*Seat summary in one line: the logic seat's deliverables are (PT-1) a finishable
kernel-checked transfer theorem whose pacing item doubles as the program's formal
disproof-receiver, (PT-2) F5 upgraded from a quantitative wall to a semantic
unprovability theorem whose countermodel is already latent in FULLINF's F6 — with
proof mining showing the missing regularity theorem is necessary, not optional,
(PT-3) the measured envelope restated as a formal speed-up/lower-bound theorem with
a cheap kernel-checked Floor Witness, and (PT-4) the strength map that says, with
citations: this corpus is logically shallow, the difficulty is mathematical — which
is exactly the configuration in which proofs, when they come, come with explicit
constants.*

---

# Round 2 — colloquium (proof-theory)

Written 2026-07-26 after reading all eight Round-1 seat files and
`results/ias/COLLOQUIUM-BRIEF.md` (C-1…C-11). Tiers as before; new checks are
pre-registered in §R2.6 BEFORE any run. Round-1 content above is unedited;
corrections are stated here, not silently patched.

## R2.1 Bet responses (bets placed on this seat)

**(a) Magic-functions ↔ this seat: "interpolation bases are the missing
support-recovery axiom."** Bookkeeping first: the HIGH-confidence bet was placed
BY this seat ON magic-functions (my §4 B1); their Round-1 file converges on the
same object independently (SEAT-magic-functions §1.6 — BRS interpolation on the
true zeros exists, the staircase basis is the open constructive half; and their
§4 bet 3 to free-boundary: interpolation-kernel boundary jets should match the
corner-jet hierarchy). Verdict: **CONVERGED, and sharpened by FB-T1's
measurement.** The support-recovery axiom cannot be a raw frequency-decay
statement — free-boundary measured that actual near-minimizers have
trace-driven r⁻² tails with O(1) constants (FB-T1 P1/P2: |φ(a)| ≈ 0.0106,
τ_φ(287) = 3.8e−7 = FULLINF's mystery tail). So the axiom the three seats now
jointly point at is: **boundary-jet data (finite, explicit, exact) +
interpolation-type remainder bound with an explicit modulus.** My PT-2(iii) is
updated accordingly (§R2.4, U1). Residue of the bet still open for their seat:
whether a BRS-type basis adapted to the *staircase* exists with computable
remainder constants — that is now the precise constructive question under the
axiom.

**(b) Renormalization: the "solvable F5 toy."** Credit correction for the
record: the LOW-MED bet on a transfer-operator toy of F5-semantic was placed BY
this seat ON renormalization (my §4 bet 4); their Round-1 file does not take it
up — **the ask stands, unclaimed.** What they DID place on this seat (their §4
bet 5): record in the Track-F cartography that windowed-positivity certificates
cost exp(Θ(e^ℓ)) bits, hence a feasibility horizon ℓ ≈ 6–7. **ACCEPTED with one
precision**: the horizon is design-relative (entrywise-ball certificates;
PLAN-computer-science CS-1's walls table L* ≈ 5–8 is the authority — cite,
don't re-derive), and it becomes a *theorem-grade* line in the cartography only
at built windows, via certified Rayleigh upper bounds (my PT-3(a)). The Floor
Witness (§R2.2) is its first kernel-checked instance. Their §1.5 "conceptual
dividend" (both solved labs have super-exponentially decaying margins while
the RH-analog is a THEOREM) is adopted into my PT-3(b)/IP-4 reading: margin
decay is orthogonal to provability; the speed-up statement binds certificate
FAMILIES, never truth — this is now said explicitly wherever PT-3 is quoted.

**(c) Quantum-chaos B5 (certificate cost = instanton action; "certificate size
≥ forbidden-cell count" as a proof-mining statement).** PARTIAL ACCEPT. What is
provable today: instance-level size ≥ log₁₀(1/λ) digits/entry from CS-1(v) +
certified upper enclosures — and with the envelope, E nats ≈ the phase-space
action, so their identification is a correct *reading* of an existing bound,
valuable as semantics. What is genuinely open and NOT a relabeling: a
basis-independent ("any Galerkin scheme, any certificate format") lower bound
of 2π nats per super-Nyquist cell would need a new adversary argument in an
operator-oracle model — the entry-oracle version is CS-3(iii); the
basis-independent version must survive the F6 caveat (prolate bases move
constants). Recorded as an open problem attached to PT-3; I do not currently
see the adversary.

**(d) Free-boundary bet 5 on this seat (corner-corrected F4 is the cheapest
kernel-checked statement over a class CONTAINING the numerical argmins; and
this seat will locate it lower than the prolate alternative).** ACCEPT, both
halves, with the honest calibration: in reverse-math terms both routes land in
RCA₀ (explicit-constants analysis; no set existence) — the true ordering is
**formalization distance**, not logical strength. Corner route: k explicit
atoms with closed-form rational/special-value couplings enter `CertFramework`
as k extra rows — months-scale. Prolate route: needs an eigenbasis with no
closed forms plus Landau–Widom asymptotics formalized — a spectral-theory
development of its own, far longer. Their bet as stated (0.3) was underpriced;
I put it at 0.7 conditional on FB-3(ii)'s Wiener–Hopf jet bound landing in
extraction-friendly form (see C-10, §R2.2).

## R2.2 Adjudications

### C-10 (co-signed statement with free-boundary: what a wall-breaking theorem must contain)

Joint statement, offered for the free-boundary seat's counter-signature —
each clause carries its owner and tier:

> **The Wall-Breaking Specification.** Any theorem that certifies the
> unrestricted infimum of Q_L (retiring FULLINF F5's obstruction) must contain:
> 1. [PT, THEOREM once PT-2(ii)'s bookkeeping is done; semantic F5] an input
>    about near-minimizers NOT derivable from the template interface
>    {certified Galerkin data; W₊ ≤ C_B*; symbol envelope; bilinear
>    composition} — because that interface is consistent with negativity
>    (gap-band countermodel, mass ε ≈ λ_m/√T₂ ≈ 5×10⁻⁸ at (7/4, 192)).
> 2. [FB, THEOREM-level structural verdict] that input cannot be a
>    positive-exponent decay statement derived from coercivity: the EL
>    operator sits at the s = 0 (logarithmic) endpoint, where the CSS
>    package degenerates and F5 is sharp. Moreover raw-tail decay beyond
>    trace-driven r⁻² is FALSE for actual minimizers (FB-T1, measured).
> 3. [FB, CONJECTURE with measured support] the minimal known candidate
>    satisfying 1–2 is the Corner-Jet Decomposition: finitely many explicit
>    boundary atoms (exact data — no modulus needed) + remainder ψ_k with
>    τ_{ψ_k}(R) ≤ C_k R^{−(2k+1)}.
> 4. [PT, the modulus-extraction requirement — the seat's answer to the
>    coordinator's question] the corner-jet route SATISFIES the proof-mining
>    necessity demand of PT-2(iii), PROVIDED FB-3(ii)/(iii) is stated and
>    proved in Π₂ moduli form: "for every EL-residual bound ρ there is an
>    explicit C_k(ρ, L)" — a majorant, not an existence claim. The atoms are
>    finite exact data (extraction-trivial); the entire a-priori content is
>    the ONE modulus C_k(ρ). Two warnings, binding: (i) if the Wiener–Hopf
>    endpoint analysis invokes compactness or a Fredholm alternative without
>    quantitative inverse bounds, the extraction metatheorems still
>    guarantee a modulus EXISTS (WKL-formalizable proofs extract), but the
>    program should demand the explicit constant directly — the repo's
>    entire corpus (T1′, Glide, FULLINF) has set that standard; (ii) the
>    modulus must be uniform in the residual, since it will be consumed at
>    Galerkin argmins (nonzero residual), not at exact minimizers.
> 5. [joint falsifier, pre-registered §R2.6-T2] the countermodel search
>    re-run INSIDE the corner-corrected interface must come up empty at
>    moderate C_k. Arithmetic of why we expect emptiness: the PT-2 packet
>    lives at band |r| ≈ m/a ≈ 440 (L = 7/4, m = 192) where the k = 3
>    corner class allows tail mass ≤ C₃·(m/a)^{−7} ≈ 3×10⁻¹⁹·C₃ — five-plus
>    orders below the ε ≈ 5×10⁻⁸ the countermodel needs. The corner axiom
>    excludes the countermodel exactly where the old interface admitted it:
>    **the atoms re-inject the support constraint at the boundary, which is
>    where it lives.** If a countermodel is nonetheless found inside 𝒯+jet,
>    clause 3 is refuted as sufficient and the calculus needs a further
>    axiom — that outcome would be a finding, not a failure.

Division of labor: PT owns clauses 1, 4 and the calculus definitions (one
shared definitional section with PT-3's Π_ball — Merge M1); FB owns 2, 3 and
the Wiener–Hopf program; NT supplies F6 data; NA runs the falsifier search.

### C-9 (the Lean-ready queue, ranked by value-per-person-day against the terminal criterion)

The terminal criterion (standing objective) is a kernel-checked certificate on
one of the three branches. None of the three items IS that; they price
differently as steps toward it:

| rank (value/pd) | item | cost | value, honestly stated |
|---|---|---|---|
| 1 | **QC-2** (annihilating-pair rearrangement of T1′) | 2–5 pd (paper form is a rearrangement of proved material; Lean is an edit of `lean/glide/Glide/HardHorizon.lean` — same lemma chain L4→L7→L5→L6, different final unknown) | a genuinely new kernel-checked ANALYTIC theorem at near-zero cost; quantifies de-anchoring at the 2e²δ·e^{2a} scale, turning T1PRIME Gap 1 into a tradeoff; highest ratio on the board, modest absolute value |
| 2 | **Floor Witness** (PT-3(c); full dispatch spec below) | 3–6 pd | first kernel-checked IMPOSSIBILITY artifact (certificate-size lower bound at a live window); creates the negative wing of the artifact stack that the Π₁ asymmetry has always implied; also a formal regression of Q5's settled δ* |
| 3 | **PT-1** (transfer theorem, Tier 1) | 110–215 pd | the only item ON a branch of the terminal criterion (independence-collapse), and its pacing item F(i).1 is the disproof branch's formal verifier; absolute value highest, ratio lowest — run as a scheduled workstream, NOT as a panel-week task |

Recommended sequencing: dispatch 1 and 2 now (jointly ≤ 11 pd — Merge M2);
de-risk 3 by its F(i).0 step alone (3–6 pd: pin Foundation, audit its
Σ₁-completeness statement form) before committing the full map.

**Floor Witness — dispatch spec (precise enough to hand off).**
*Statement (Lean, weilcert project):* for the explicit rational symmetric
matrix `A : Matrix (Fin 40) (Fin 40) ℚ` (the (L, m) = (711/200, 40) window
data) and `δ = 1/10^20`:
`∃ M, M.IsSymm ∧ (∀ i j, |M i j − A i j| ≤ δ) ∧ ∃ x : Fin 40 → ℚ, x ⬝ᵥ M.mulVec x < 0`
— i.e. the 1e−20 ball around A contains a matrix with a negative direction,
hence NO sound ball certificate at δ ≥ 1e−20 exists at this window (the
statement kernel-checked; its identification with the true Weil form rides
the usual computer-assisted Bridge, stated as always).
*Witness construction:* M := A − δ·ssᵀ with s = sign(x) (the CS-1(v)
adversary, rank-one — so the check reduces to the single exact-ℚ inequality
`x ⬝ᵥ A.mulVec x < δ·(Σᵢ |xᵢ|)²`); x = rational eigenvector approximation
(denominator 10¹⁵ suffices: with λ₂ ≈ 1.07e−17 ≫ λ₁ ≈ 1.80e−20, angular error
θ ≤ 0.04 keeps the Rayleigh quotient within the needed 2×; SYNTHESIS anchor
numbers).
*Data generation:* extend `lean/make_certificate_deep.py`: emit A at
DENP = 25 from `certified_spectral` midpoints via the 60-dps path (pathology
#5 discipline), v at 30 digits, x by truncation; run the standing
coherence oracle against the certified interval enclosure at the same window.
*Kernel cost:* one 40×40 rational quadratic form, ~40-digit entries — seconds.
*Audit:* the three standard axioms; no native_decide; success bands
pre-registered in §R2.6-T1. *Effort:* 2 pd generator + 1–2 pd Lean + 1 pd
audit/writeup.

### C-7 (metamathematical read: does ensemble ≠ number change what disproof-side certificates can claim?)

Three-part answer, each part load-bearing:

1. **Nothing changes for soundness.** A disproof certificate is an
   instance-level Π₁/Σ₁ fact about THE configuration; no ensemble statement
   enters its validity. Log-gas's finding (λ_GUE has sd 3.6 nats; 4.7 orders
   across ten seeds; window phase u₁ explains ~89% of variance) is a fact
   about a *different measure space* and cannot touch a kernel-checked
   negative rung. The kill criteria of PROGRAM §4/§6 stand verbatim.
2. **The evidentiary layer changes, in the direction the program's law
   already points.** Any reasoning that prices near-misses or "suspiciously
   small" measured margins via GUE lore must now be distributional: under the
   correct null model, single-window margin fluctuations are fat and
   phase-dominated, so a low margin at one window is WEAK evidence of
   anything. C-7 is the quantitative justification of the standing oracle
   discipline ("negativity is a bug until confirmed") — the null against
   which a catastrophe must be judged has ±3.6-nat scatter, and on the
   Poisson side extreme-value amplification (log-gas P5: the infimum prices
   the worst local deficit; surpluses do not refund). Restated for the prior
   panel per the coordinator's request: DG-P3/NT-P2-style point claims about
   λ_GUE are category errors; the invariants are (bias, Var J) functionals.
3. **For this seat's own artifacts: instance-level bounds are immune,
   ensemble-averaged pricing is now meaningless.** PT-3(a)'s lower bounds
   use certified Rayleigh enclosures at the actual window — untouched. But
   any future "expected certificate size over an ensemble of
   configurations" statement would inherit the 4.7-order spread and say
   nothing; certificate economics must stay per-window, as the depth law
   (CS-1(v), Q5) is stated. Corollary worth recording: ζ's configuration
   sits at ≈ 0 ± 0.1 nats from the rigid staircase against an ensemble sd
   of 3.6 — measure-atypical in exactly the direction of the §2.17
   maximal-rigidity finding; the ensemble-to-instance gap (the MSS
   obstruction's shadow, PROGRAM §4 Track C) is thus MEASURED here, and it
   reinforces IP-2: independence-signature hunting, like disproof hunting,
   must be run on the instance, never on a surrogate ensemble.

## R2.3 Merges (2)

**M1 — "The Template Calculus and its Corner Extension" (with free-boundary;
NT data, NA search).** One joint note, one shared definitional section: the
calculus 𝒯 (PT-2's A1–A5), its ball-certificate sibling Π_ball (PT-3), and
the extension 𝒯+jet (A6 := corner-jet axiom, FB-3). Three results: (a)
semantic wall for 𝒯 (PT owns; NT's F6 constants); (b) corner-corrected F4 at
L = 7/4 over a class containing the argmins (FB owns; FULLINF machinery);
(c) the 𝒯+jet adversary search (NA runs; pre-registered §R2.6-T2). Replaces
FULLINF §10's "named missing mathematics" with a specification both seats
co-sign (C-10 statement above). Timeline: definitional section + (a), 2–4
weeks PT-side; (b) on FB's stated ladder.

**M2 — "The impossibility wing" (with quasicrystal; Lean track executes; CS
reviews sizes).** Ship QC-2 and the Floor Witness together as the program's
first two kernel-checked NEGATIVE statements — one analytic (anchored
functions cannot dodge past the horizon without exponential de-anchoring),
one certificate-theoretic (no coarse ball certificate exists at a named
window) — with a two-page joint framing note: the Π₁ asymmetry made formal,
both directions. QC seat owns QC-2's math (already THEOREM-tier as a
rearrangement); PT owns the Floor Witness spec/audit and the framing note;
total ≤ 11 pd.

## R2.4 Updates (kills, retractions, strengthenings)

**U1 (correction to §1.6(ii)/PT-2(iii) — the necessity claim, sharpened by
FB-T1).** Round 1 said the forced modulus "is a support-to-frequency-decay
regularity statement." FB-T1's measurement refutes the RAW-decay version:
near-minimizers have trace-driven r⁻² tails with O(1) constants, so no
modulus of raw decay beyond r⁻² can be true. Corrected statement: the forced
modulus is for the JET-CORRECTED remainder (or another support-re-injecting
decomposition); FB-3 is its minimal known instantiation. The necessity
argument itself (some interface-transcending modulus must appear in any
extractable proof) is unchanged — it is strengthened, since one more
candidate class (raw decay) is now measured out.

**U2 (PT-3(b) rider).** The deep-regime constants are under active revision
(C-3: riemann-hilbert's p = 4.85 ± 0.10, A′ = 16.75, Fuchs-literal rejected;
the L = 5.50 triple landed). PT-3(b)'s speed-up form is insensitive — it
needs only size ≥ exp(c·e^{L/2}) for some c > 0 — but every quoted constant
should cite the C-3 adjudication, not the old chart. No kill.

**U3 (PT-1 map, post-colloquium).** Unchanged in structure and totals. One
addition: toolchain topology — QC-2 lives in the glide project, the Floor
Witness in weilcert, PT-1 in its own project importing Foundation; no shared
build risk among the three. No new prior-art exposure surfaced for PT items
in any seat file (C-8 concerns MF-1's Krein dictionary, not the logic layer).

**U4 (Round-1 §4 bets, scored where the colloquium already decides them).**
B1 (magic-functions): substantially CONFIRMED as convergence, residue stated
in R2.1(a). B2 (quasicrystal, crystalline identities as the O(1)-per-window
format): STRENGTHENED by their measured trichotomy — the chirp owns the
super-exponential toll, and their IP-1 (UPT as Asano contraction /
stability-preserver classification) is exactly an O(1)-description-per-step
proof format; the falsifiable first step they name (Grace–Walsh–Szegő
representability of the p-step) is the right kill test. B3 (log-gas, T4
formalizes at RCA₀ grade): unchanged; their P3/P6 linear-response precision
(r = 0.991, slope 0.954) raises my confidence the eventual proof is
explicit-constants. B4 (renormalization toy): open, restated in R2.1(b).

**U5 (no kills).** Nothing in the eight files or C-1…C-11 kills or weakens
PT-1, PT-2's countermodel route, PT-3, or PT-4. The one Round-1 sentence I
retract is the raw-decay phrasing corrected in U1.

## R2.5 Next action (single, sized)

**Build and kernel-check the Floor Witness** per the C-9 dispatch spec:
3–6 pd, weilcert project, success bands pre-registered below. Chosen over
PT-1's F(i).0 because it is self-contained, creates the impossibility genre
M2 needs, and its data-generation step doubles as a formal regression of the
Q5 program law (δ* = λ/‖v‖₁²) — two standing panel items retired by one
artifact. (PT-1's F(i).0 de-risk is the queued second action; M1's
definitional section runs in parallel on paper.)

## R2.6 Pre-registered checks (logged before any run; none run at Round-2 writing)

**T1 (Floor Witness generation).** Predictions: (i) the exact-rational
Rayleigh-per-coherence value x ⬝ᵥ A.mulVec x / (Σ|xᵢ|)² lands in
**[3.5, 5.5]×10⁻²¹** (reproducing Q5's δ* = 4.489×10⁻²¹ within eigenvector-
truncation slack); (ii) headroom factor vs δ = 1e−20 ≥ **1.8×**; (iii) the
coherence oracle vs the certified interval enclosure passes within combined
budgets. Kill: if (i) lands ABOVE 1e−20 the witness fails and Q5's settled
number is wrong — program-level alarm, report to coordinator before anything
ships.

**T2 (𝒯+jet adversary search; NA executes under M1).** Prediction: within
the corner-corrected interface at (L, m, k) = (7/4, 192, 3) and C₃ ≤ 15, the
gap-band countermodel family of PT-2(ii) has NO member with Q^{F0} < 0
(excluded mass margin ≥ 10⁴, per the C-10 clause-5 arithmetic); within the
UNCORRECTED interface the search succeeds at ε ∈ [2, 20]×10⁻⁸ with
Q^{F0} ≤ −10⁻⁵. Either half failing sends M1 back to the definitional
drawing board — pre-committed.
