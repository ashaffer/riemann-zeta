# PLAN — Theoretical Computer Science (certificate complexity, verified computation, algorithmic spectral theory)

*Independent consultant plan, prepared July 26 (machine clock; house dateline convention per
`PROGRAM.md` §2.14). Sources: `README.md`; `PROGRAM.md` §2.14–2.18, §3, §4 (Tracks B, D, F);
`THEOREMS.md`; `results/RESULTS.md`; `lean/README-verify.md`; `results/agent-lean-depth.md`;
the emitted certificates under `lean/weilcert/` (independently re-scanned this session);
`lean/make_certificate_deep.py`. Other experts' PLAN files were not read. One light
computation was run (a digit-scan of the four checked-in Lean certificates plus model
arithmetic); its outputs are quoted where used.*

---

## 1. Reformulation

The program, in the language of my field, is a **certificate-complexity phenomenon that has
measured itself**.

Weil's criterion (as instrumented here, `THEOREMS.md` preamble): RH ⟺ λ(L) ≥ 0 for all L,
where λ(L) is the operator-level minimum of the truncated form Q_L. Theorem 1 of
`THEOREMS.md` proves λ is non-increasing in L; so RH is the statement that a monotone
function — whose measured values fall along ln λ(L) ≈ 10.2 − 1.755·e^{L/2}(L/2+4)
(`results/RESULTS.md`, spectral ladder; validated over ~35 orders of magnitude) — never
crosses zero. Each finite window is a decidable statement (the CCM property P(n),
`PROGRAM.md` §1, §4 Track A); RH is Π₁ (Track F; Yedidia–Aaronson machine, 5,372 states).
Three consequences frame everything below:

1. **The envelope law is a certificate-precision law.** Any proof about a matrix that
   remains valid on an entrywise δ-ball around it (the design of every Lean window here,
   `THEOREMS.md` Theorem 2) is sound only if δ < λ_min of the stated matrix (Lemma CS‑1(v)
   below — a two-line adversary argument). So the measured envelope *is* a lower bound on
   the digits-per-entry of every future rung: DENP ≳ 0.762·e^{L/2}(L/2+4) − 4.4. The
   certificates must grow super-exponentially in L while the fact they certify (the margin)
   shrinks to zero. Verification-by-computation and proof diverge at a measured rate.

2. **Finite certificates certify Galerkin restrictions, not P(n).** The kernel theorems are
   statements about m-dimensional test spaces. The operator statement λ(L) ≥ 0 needs exactly
   one more ingredient — a certified truncation bound λ(L) ≥ λ_Galerkin(m,L) − T(m,L) —
   which today exists only as measured convergence (`RESULTS.md`, plunge-then-creep
   ladders). With it, Theorem 1's monotonicity makes a *single* rung at the right end of a
   window certify the whole window; without it, the only effective bridge is the Glide
   modulus C·(log 1/h)^{−1/2}, which at envelope-scale margins forces a doubly exponential
   grid e^{(C/λ)²}. All the analytic difficulty has migrated into T(m,L); the CS content is
   to make that migration exact (Lemma CS‑3).

3. **The Π₁ asymmetry has measured constants.** Certifying positivity at support L costs
   exp(Θ(e^{L/2}·L)) bits (envelope-forced); certifying a genuine violation, if one exists
   at height γ_b, costs poly(γ_b) bits at support L ≈ 2 ln(γ_b/2π) (Lemma CS‑4(iv)). The
   instruments are natively better at disproof — `PROGRAM.md` §6 says this qualitatively;
   the lemmas below say it with exponents. A corollary the program should internalize: since
   the resolution height of a window is T*(L) = 2π e^{L/2} (§2.14(v)) and the certification
   wall computed below sits at L* ≈ 5–8, kernel-certified criterion verification tops out at
   effective height T* ≈ 80–340 — nine to ten orders below the Riemann–Siegel frontier
   (3×10¹², Platt–Trudgian, `PROGRAM.md` §1). The "criterion checks trail by nine orders"
   fact of §1 is not an accident of effort; it is forced by exp(e^{L/2}) certificate growth.
   Track A's value is epistemic diversity, not height, and the reach analysis below puts a
   number on where it ends.

The repo's artifacts are, to my knowledge, the first systematically *measured* instance of
exact-arithmetic PSD-certificate scaling at controlled margins (the m = 12/16/24/48 series,
`results/agent-lean-depth.md` §4–§8): a dataset my field can fit lemmas to. That is what
Section 2 does.

---

## 2. Lemma candidates

Notation for all four: m = Galerkin dimension; DEN = 10^DENP the entry-denominator grid;
A ∈ ℤ^{m×m} the symmetric integer matrix (entries ≈ DEN·Q); λ_un = λ_min(A/DEN); Δ_k = k-th
leading principal minor of B = A − S·I; "digits" = decimal digits; the *as-built design* is
the checked-in one (single global multiplier c = lcm of LDLᵀ column denominators, integer
congruence c²B = Wᵀdiag(g)W with upper-triangular W, plus the inverse witness Winv·W = f·I;
`lean/make_certificate_deep.py`, `THEOREMS.md` Theorem 2).

### Lemma CS‑1 (bit-growth of integer congruence certificates for certified windows)

**(a) Statement.** Let B ∈ ℤ^{m×m} be symmetric with |B_ij| ≤ 10^P and λ_min(B) > 0. Then:

 (i) *(existence)* The fraction-free LDLᵀ exists without pivoting (all Δ_k > 0), and the
 as-built certificate (c, W, g, Winv, f) exists with c | Π_{k<m} Δ_k, g_k > 0.

 (ii) *(size, as-built)* digits(c) ≤ Σ_{k<m} digits(Δ_k) ≤ (m²/2)·(P + ½log₁₀ m + ¼);
 digits(g_k) ≤ 2·digits(c) + digits(Δ_k/Δ_{k−1}); total certificate data
 S_asbuilt = O(m²·digits(c)) = O(m⁴·(P + log m)), the Winv block dominating.

 (iii) *(size, per-column / triangular designs)* Shipping the integer subresultant factor F
 (F_ik = an (i,k) k-minor, so column k carries ≤ k(P + ½log₁₀ k) digits) with the pivot list
 gives S_ff ≤ (m³/6)(P + ½log₁₀ m)(1 + o(1)) data, verified via the rational identity
 B = Σ_k f_k f_kᵀ/(Δ_{k−1}Δ_k) in kernel time Õ(m⁴P); invertibility of a triangular W is
 kernel-free (nonzero diagonal), eliminating the Winv block entirely. The parity
 checkerboard S_kj = 0 for k+j odd (`RESULTS.md`, spectral basis) splits every design into
 two independent m/2 certificates: a further ÷4 in data at fixed design.

 (iv) *(verification)* The congruence check is O(m³) big-integer multiplications; on the
 repo's toolchain (Lean 4.32.1 kernel, `decide`) the measured cost is ≈ 0.8 ms per m³-term
 with only a weak digit factor (`agent-lean-depth.md` §5, §8), i.e. T_decide ≈ 0.8 ms·m³
 until integer sizes reach ~10⁵ digits.

 (v) *(precision floor — the load-bearing clause)* If every symmetric M with
 |M − A/DEN|_∞ ≤ δ has positive form, then δ < λ_un/‖v‖₁² ≤ λ_un, where v is a unit
 minimizing eigenvector. *Proof:* M = A/DEN − δ·Σ with Σ_ij = sign(v_i v_j) is symmetric,
 lies in the ball, and v ᵀMv = λ_un − δ‖v‖₁² with ‖v‖₁ ≥ ‖v‖₂ = 1. ∎ Hence
 DENP ≥ log₁₀(1/δ) > log₁₀(1/λ_un): **the envelope sets the digits; no design escapes it.**

**Corollary (reach of the formal ladder under the measured envelope).** Insert the measured
laws m_env(L) ≈ (3–4)·L·e^{L/2} (fit to the spectral ladders: m = 24/48/80/96–112 at
L = 2.485/2.996/3.555/4.025–4.25, `RESULTS.md`) and DENP(L) ≈ 0.762·e^{L/2}(L/2+4) − 4.4
plus the house identification guard (~+15; `make_certificate_deep.py` asserts ident < δ/100):

| L | margin | m_env | DENP | digits(c) as-built | S as-built | S per-col+parity | matrix stmt alone |
|---|---|---|---|---|---|---|---|
| 2.485 | 3.9e−10 | 24–30 | 26–28 | 3.4–5×10³ | 0.7–1.4 MB | ~30 KB | ~4 KB |
| 2.996 | 4.3e−15 | 47–48 | 30–31 | 1.4–1.5×10⁴ | ~10 MB | ~130 KB | ~16 KB |
| 3.555 | 2.2e−22 | 74–80 | 38–39 | 4.4–5.2×10⁴ | 75–105 MB | ~0.6 MB | ~60 KB |
| 4.025 | 1.4e−30 | 96–112 | 44–48 | 0.9–1.3×10⁵ | 250–500 MB | 1.5–3 MB | ~170 KB |
| 5.0 | 1.2e−56 | ~213 | ~74 | 7×10⁵ | ~10 GB | ~30 MB | ~1.3 MB |
| 5.5 | 9e−77 | ~301 | ~94 | 1.8×10⁶ | — | ~110 MB | ~3.5 MB |
| 8.0 | 1e−328 | ~1530 | ~350 | — | — | — | ~400 MB |

Three walls: **as-built** L* ≈ 3.0 (the m = 48 file is 10.6 MB and its build was left as a
placeholder, `agent-lean-depth.md` §6); **redesigned** (per-column + triangular-W + parity,
the options already sketched in §8 there) L* ≈ 5.0–5.5; **any entrywise-ball design**
L* ≈ 7–8, where merely *stating* the matrix to sound precision passes ~0.4 GB. Preconditioning
and design changes move polynomial factors (m⁴ → m³ → m² in data); clause (v) shows nothing
moves the e^{L/2}(L/2+4) digit floor, so the asymptotic reach in L changes only through
log-factors. The only way past the wall is to change the *statement* (normalized forms,
operator-level lemmas) — which is the mathematics, not the engineering.

**(b) Proof strategy.** (i)–(ii): Sylvester/subresultant theory for fraction-free
elimination (Bareiss) + Hadamard's bound digits(Δ_k) ≤ k(P + ½log₁₀ k); lcm ≤ product.
(iii): the classical identity B = F·diag(1/(Δ_{k−1}Δ_k))·Fᵀ with integer F; kernel-side
rational summation. (iv): count multiplications; calibrate the constant on the measured
profile. (v): as displayed — it is complete above.

**(c) Hardest missing step.** A matching *lower* bound on digits(c) — i.e. proving the
compounding is real for these matrices (no systematic cancellation in the minors). The
measured constant 0.21·m²·DENP sits a factor ~2.4 inside Hadamard, stable over m = 16→48,
which is strong evidence; a proof would need anti-concentration for minors of
Toeplitz-plus-low-rank matrices with envelope-forced conditioning (the spectrum spanning
DENP decades forces Σ_k digits(Δ_k) ≥ Ω(m·DENP) but the full m²·DENP needs more). Honest
status: upper bounds provable now; lower bound research-grade.

**(d) Difficulty.** (i)–(iv): routine-to-moderate, a careful fortnight (the per-column
kernel-time accounting is the fiddly part). (v): done. Lower bound: open-ended.

**(e) Check against repo data.** Independent scan of the four checked-in certificates run
this session (longest integer literal; total digit characters):
`Weilcert.lean` 1226 / 43,152; `WeilcertFamily.lean` 2589 / 138,570; `WeilcertDeep.lean`
6779 / 696,379; `WeilcertDeeper.lean` 30,319 / 10,508,160 — reproducing
`agent-lean-depth.md` §4 for m = 16/24/48 (0.14/0.69/10.48 MB) and the digits(g) column.
The fit digits(c) ≈ 0.21·m²·DENP: measured/model = 0.83 (m=12, small-m regime, as flagged
there), **0.994 (m=16), 0.997 (m=24), 1.043 (m=48)**. Effective total-size exponent between
the m = 24 and 48 points: S ~ m^3.8·DENP — between my m³ (per-column) and m⁴ (as-built lcm)
laws, as the partial lcm-sharing predicts. Discrepancy flagged for the ledger: the m = 12
row of `agent-lean-depth.md` §4 lists g at 2430 digits, but both my scan (max literal 1226)
and `RESULTS.md` ("g <= 1226, c,f ~ 602") say ~1226; the m ≥ 16 rows are generator-measured
and check out exactly.

### Lemma CS‑2 (compilation: interval positivity proof → kernel certificate; the minimal trusted base)

**(a) Statement.** Fix m, δ, and DEN = 10^DENP. Suppose an interval computation delivers
(H1) rational-endpoint enclosures [Q̲_ij, Q̄_ij] of a symmetric matrix Q_true with max
halfwidth w, and (H2) an outward-rounded interval-Cholesky certificate that
λ_min(mid) ≥ β > m·δ·(1+η) for some η > 0, with (H3) w + 1/(2DEN) < δ/100. Then the exact
midpoint-rounding to the 1/DEN grid yields A ∈ ℤ^{m×m} such that the as-built (resp.
per-column) integer congruence certificate for B = A − ⌈m·DEN·δ⌉·I **exists**, its sizes obey
Lemma CS‑1(ii)–(iii) with P = DENP, the kernel-verified conclusion is "every symmetric M
with |M − A/DEN|_∞ ≤ δ has positive form", and Q_true lies in that ball. Total certificate
size S(δ) = Θ(m³·(log₁₀(1/δ) + log m)) in the per-column design; kernel time per CS‑1(iv).
Moreover the **trusted base splits exactly**: the ball theorem needs only the kernel (three
standard axioms, `lean/README-verify.md`); the identification of Q_true with the analytic
Weil matrix is the Bridge (computer-assisted; trust base "mpmath.iv enclosures of exp, log,
π, γ and directed rounding", `THEOREMS.md`); and closing the Bridge inside Lean requires
precisely: (M1) arbitrary-precision verified enclosures of γ (for ψ(1/4) = −γ − π/2 − 3log2)
and of log 2, log 3, log π, e^{±rational} with directed rounding; (M2) the two tail lemmas
already stated with explicit constants in the repo (Bernoulli-kernel tail |g_r| ≤ 250/π^{r+1},
`RESULTS.md`; geometric pole/Bessel and kernel tails, `THEOREMS.md` Bridge); (M3) a ℚ-interval
outward-rounding layer. `THEOREMS.md` itself delimits: Bernoulli generating series present in
mathlib, "Gauss's digamma integral and directed-rounded evaluation — absent." Everything
L- and m-dependent is *data*, not new formal mathematics: the mathlib delta is O(1) lemmas.

**(b) Proof strategy.** Rounding and shift soundness: entrywise-to-spectral bound
‖E‖₂ ≤ m·max|E_ij| (Schur), exactly the generator's Cauchy–Schwarz shift S = m·DEN·δ;
existence of the factorization from λ_min(B) > 0 (Weyl + H2, H3); sizes from CS‑1. The
statement is engineered to have machine-checkable hypotheses: (H3) is the generator's
`assert ident < delta/100`, (H2) is `certified_margins`/`certified_spectral` interval
Cholesky, and the exact-Fraction endpoint extraction of `make_certificate_deep.py` discharges
the rounding hypothesis.

**(c) Hardest missing step.** M1: a verified Euler–Mascheroni enclosure at hundreds of
digits inside mathlib (Brent–McMillan with error bounds, formalized) — the one genuinely
new formalization object; M3 is engineering; M2 is short analysis. Nothing conceptual.

**(d) Difficulty.** The compilation theorem itself: moderate, provable now (it is
essentially an abstraction of code that already runs). The mathlib delta: months of
formalization work, parallelizable, with M1 the pacing item.

**(e) Check against repo data.** The lemma's hypotheses are satisfied with big margins by
all three new windows: exact identification bounds 4.948e−29 / 4.933e−25 / 4.998e−31
against δ = 1e−14 / 1e−9 / 1e−19 (margins 2.0e14×–2.0e15×), and shift headroom
λ_un/(mδ) = 611× / 253× / 346× (`agent-lean-depth.md` §3). The **negative case study is the
checked-in m = 12 Bridge**: midpoints passed through 53-bit floats cost ~1.46e−17 > the
claimed δ = 1e−20 (§7(i) there) — exactly the failure mode hypothesis (H3) excludes; my
lemma is the statement whose machine-checked hypotheses make that class of bug impossible.
This also fixes the honest reading of Theorem 2: kernel statement intact, Bridge δ needs
restating at 1e−16 (ample headroom exists).

### Lemma CS‑3 (bit complexity of the level-n criterion; the precision reduction made exact)

**(a) Statement.** Let SignWeil(L, m, b) be: given rational L, decide the sign of
λ_un(L, m) under the promise |λ_un| ≥ 2^{−b}. Then:

 (i) *(upper, unconditional)* SignWeil ∈ TIME Õ(m³b + m²b²): assemble the m² entries via the
 repo's exact-rational-plus-tail series to ⌈b⌉ + O(log m) bits (O(b)-term series per entry),
 then one exact/p-adic-lifted factorization.

 (ii) *(calibrated by the envelope)* At envelope-resolving parameters — n = e^{L/2}
 participating prime-power scale, m_env ≈ 7·n·ln n, b_env(n) ≈ 2.53·n(ln n + 4) − 14.7 bits
 — the cost is Õ(n⁴), the certificate (per-column design) Õ(n³), and the promise is the
 envelope law itself with an O(1)-factor slack.

 (iii) *(floor, entry-oracle model)* Any decider reading Q through entries-to-precision-2^{−t}
 oracles needs t > log₂(‖v‖₁²/λ_un)⁻¹-precision, i.e. Ω(b) bits per entry on Ω(m²) entries:
 Ω̃(n³) total. Given the repo's *certified upper bounds* on λ (interval-Rayleigh side of every
 enclosure), this floor is unconditional at every built window — no envelope assumption.

 (iv) *(the P(n) reduction)* Modulo one lemma — a certified truncation bound
 T(m, L) ≥ λ_Galerkin(m, L) − λ(L) with T(m_env, L) < ½λ(L) — monotonicity (Theorem 1(1))
 reduces the full window criterion at level n (all supports up to the window's right end L*)
 to the single call SignWeil(L*, m_env, b_env): P(n) decided in Õ(n⁴). Without T, the only
 effective ∀L bridge is the Glide modulus, which at margin λ needs grid step
 h ≤ exp(−(C_glide/λ)²) — doubly exponential in e^{L/2}; this is the precise sense in which
 the program can certify rungs but not yet windows.

**(b) Proof strategy.** (i): series truncation counts from `certified_spectral.py`'s rigorous
tails; Dixon lifting / rational reconstruction for the Õ(m³b) solve. (ii): substitution of
the two measured laws (m_env fit; the envelope with its <1%-in-exponent validation record).
(iii): Lemma CS‑1(v) plus an adversary that answers oracles consistently with both signs
until the precision threshold. (iv): zero-extension monotonicity is already proved
(`THEOREMS.md` Theorem 1, Step 1); the arithmetic of the grid-vs-modulus claim is Lemma
B/C bookkeeping.

**(c) Hardest missing step.** The truncation bound T(m, L) — analysis, not CS: quantitative
polynomial approximation of near-minimizers whose only non-smoothness is the measured
derivative kinks at x = ±(a − log p) (`RESULTS.md`, plunge-then-creep), with tails
controlled by the log-weighted energy W₊ of `THEOREMS.md` Lemma B. My role is to have made
its required strength exact: T must beat the envelope at m_env, i.e. decay faster than
e^{−1.755 e^{L/2}(L/2+4)} at m ≈ 7n ln n — a Bernstein/Jackson-type statement with explicit
constants. This is the single lemma separating the certified ladder from certified P(n).

**(d) Difficulty.** (i)–(iii): moderate; a clean paper's worth. (iv) as a reduction:
easy given (iii); the T-lemma itself: hard analysis, right-sized for the numerical-analysis
consultant (see Interfaces).

**(e) Check against repo data.** b_env vs practice: at L = 2.485, b_env = 31.3 bits
(9.4 digits); the built certificate uses DENP = 28 with δ = 1e−14 — floor respected with the
design's deliberate ~600× headroom (`agent-lean-depth.md` §3: λ_un/(mδ) = 611). At
L = 2.996: b_env = 47.6 bits = 14.3 digits vs DENP = 30, δ = 1e−19 ✓. The m_env fit
reproduces the measured ladders within ±20% at all five solid windows. The precision floor
(iii) evaluated at the certified λ_un = 1.467e−10 (m = 24) forbids any sound ball radius
above 1.5e−10; the shipped δ = 1e−14 ✓; same check passes at m = 16 and m = 48.

### Lemma CS‑4 (Track D: the Odlyzko–te Riele window attack as an optimization with certified failure modes)

**(a) Statement.** For an even unit window w supported in [−L/4, L/4] and t ≥ 0 let
φ_t(x) = cos(tx)·w(x) and F_w(t) = Q_L(φ_t)/‖φ_t‖². Then:

 (i) RH ⟹ F_w(t) ≥ 0 for all (t, L); and unconditionally F_w(t) ≥ λ(L).

 (ii) F_w(t) = [W_arch(t) + P_w(t)]/‖φ_t‖² − (Σ_{n<e^{L/2}} 2Λ(n) n^{−1/2} ψ_w(log n)·cos(t log n))/‖φ_t‖²·(1+o(1))
 + E_w(t), with W_arch(t) sandwiched by ψ(1/4) + ½log(1+4t²) ± 8 (`THEOREMS.md` Lemma A)
 and E_w(t) an explicit oscillatory-integral remainder = O(W₊(w)/t). Minimizing F over t is
 therefore, up to certified error bars, the problem of aligning cos(t log n) ≈ +1
 simultaneously for the participating prime powers — an inhomogeneous simultaneous
 Diophantine approximation on the ray t·(log 2, log 3, log 5, …) mod 2π, the exact engine
 of Odlyzko–te Riele 1985 (`PROGRAM.md` §4 Track D(iii), §7), searchable by LLL on the
 standard (q-scaled) lattice.

 (iii) **Certified failure modes.** (F1) *Lattice dual bound:* from the Gram–Schmidt norms
 of the reduced basis, a rigorous lower bound on the alignment defect valid for **all**
 t ≤ T_max — so an unsuccessful search exits with a theorem "no test function in this
 modulated family certifies negativity at support L with t ≤ T_max", with explicit
 constants. (F2) *Linear forms in logarithms:* Baker–Wüstholz gives an unconditional,
 effective (astronomically weak, but nonzero) defect bound for all t — the family can be
 proven to *never* achieve exact alignment. (F3) *Envelope floor / alarm:* by (i),
 a certified interval evaluation of F_w(t) can never fall below the certified enclosure of
 λ(L); any dip below it is, by program law (`README.md`, the discipline), an implementation
 bug until the zero-side oracle convicts mathematics — at which point it is a disproof
 certificate of RH. The attack is thus sound-by-construction: every outcome is either a
 certificate of failure over the searched region or a certified catastrophe.

 (iv) *(quantitative Π₁ asymmetry)* If RH is false with an off-line zero at height γ_b
 (necessarily γ_b > 3×10¹², the verified region), a violating window needs support only
 L ≈ 2 log(γ_b/2π) — resolution T*(L) ≥ γ_b — and certifying Q_L(φ) < 0 for one explicit φ
 costs Õ(γ_b) bit operations at poly(log γ_b)-digit precision (the violation magnitude, not
 the envelope, sets the precision). Against this, *positivity* certification at the same
 support costs exp(Θ(e^{L/2}L)) = exp(Θ(γ_b log γ_b)) bits by Lemma CS‑1. Disproof is
 exponentially cheaper than exhaustion; this is Track D's co-equal priority, with exponents.

**(b) Proof strategy.** (ii): stationary-phase-free elementary bounds — the oscillatory
term is ∫w(x)w(x+u)cos(t(2x+u))dx, integrable by parts once against W₊-controlled
derivatives (Lemma A(iii) machinery). (F1): λ₁(lattice) ≥ min‖b*_i‖ plus transference —
textbook, but stated as an exit *certificate* of the search harness. (F2): cite effective
constants; compute them once for {log 2, …, log 7}. (iv): explicit test function
cos(γ_b x)·w; count prime-sum terms n < e^{L/2} ≈ γ_b/2π.

**(c) Hardest missing step.** Making E_w(t) small enough *with certified constants* that
(F1)'s defect bound translates into a useful bound on min_t F_w — i.e. the certified gap
between the trigonometric surrogate and the true form. If E's certified constant is sloppy,
the failure certificate is vacuous even when the search is honest.

**(d) Difficulty.** Formulation + harness: weeks (all pieces exist in `src/weil_core.py` /
`certified_*` form). (F2) constants: known but painful. Interpretive value: modest and
should be advertised as such — see §5.

**(e) Check against repo data.** Immediate cheap experiment: at L = 2.485, w = the m = 24
minimizer, sweep t ∈ [0, 50]: prediction min_t F_w(t) ∈ [1, 40]·λ(L) with λ(L) the
certified 3.8687–3.8688e−10 (`RESULTS.md`) — the modulated family should approach but not
beat the envelope. High-t anchors for the harness: the scan's Lehmer pairs
t = 17143.7865 (gap 0.0353) and t = 7005.0629, where local alignment is best and F dips
lowest. The prime-side data and ψ_w autocorrelations needed are already exact rationals in
the certificate pipeline.

---

## 3. Predictions

**P1 (certificate digits at the 1e−30 window — the p = 7 rung, L ≈ 4.025).** Any sound
entrywise-ball certificate there must carry DENP ≥ 31 (Lemma CS‑1(v) with
λ_un ≈ 10^{−30.5±0.5}). With house guard conventions (DENP = 44–48) at envelope-resolving
m = 96–112: **as-built design: digits(c) = digits(f) = (0.9–1.3)×10⁵, digits(g) ≈ 2× that,
total data 250–500 MB, kernel decide ≥ 12–30 min per congruence lemma — it will not build
on this machine as designed. With the §8 redesign (triangular W, per-column scaling, parity
split): 1.5–3 MB total and a green build in ≲ 30 min.** Falsified by generating the window
(`make_certificate_deep.py` extended with a `zeta_p7` spec) and counting.

**P2 (the m = 48 stretch window as emitted).** `WeilcertDeeper.lean` (10.6 MB, checked in,
build left as PLACEHOLDER in `agent-lean-depth.md` §6): a solo build attempt on this
machine goes green in 8–30 min wall with peak RSS 9–15 GB (decide(key_int) ≈ 80–200 s
idle-equivalent, from the 0.8 ms·m³ law with a ~1.5× digit factor at 3×10⁴-digit
integers), **or** aborts on memory if less than ~9 GB is free — it will not fail for any
other reason (the data was exactly pre-verified in Fractions). Immediately checkable.

**P3 (the precision law binds every future rung).** No valid ball certificate at the p = 5
window (L = 3.555) will ever have δ ≥ 10^{−22}; the first certified enclosure there will
land in [1.9, 2.2]×10^{−22} (G-normalized, m ≥ 80) with DENP ≥ 23 forced and ≈ 38–40 as
built. More generally every future window's (δ, DENP) will satisfy δ < λ_un < the
interval-Rayleigh upper bound — a coarser-δ "certificate" appearing anywhere in the ledger
would mean either an unsound certificate or a wrong certified λ, both program-level alarms.

---

## 4. Interfaces

**Needs.**
1. *From numerical analysis (structured solvers):* the truncation lemma T(m, L) of
   CS‑3(c) — certified Galerkin-to-operator gap beating the envelope at m_env; and
   exact-arithmetic displacement-structured elimination (Schur/GKO over ℚ) so certificate
   *generation* at m ≥ 96 stays in memory. Distinct question they own: does fraction-free
   elimination on Toeplitz-plus-low-rank matrices (the hat-basis form: Toeplitz archimedean
   + banded shift-Toeplitz primes + rank-2 pole, `PROGRAM.md` §6, Track C) admit generator
   recurrences whose *integer sizes* also compress — i.e. can certificate data reach
   Õ(m·DENP) matching the O(m·DENP) description of the matrix itself? My Hadamard accounting
   is silent there; an answer either way moves the walls table.
2. *From convex optimization / SOS (Track B):* rational SOS certificates of the
   *normalized* form (envelope divided out, `PROGRAM.md` §2.15 consequences). The sharp
   joint question: after N_p-normalization the margins are Θ(1) — but positivity is
   congruence-invariant, so where does the DENP go? My conjecture: into the digits of the
   normalizing congruence itself (any P with P ᵀQP well-conditioned needs ~DENP-digit
   entries unless it has analytic/displacement structure); Track B's per-prime-block
   certificate hypothesis is exactly the hypothesis that such *structured* normalizers
   exist. My size laws are the objective function for that mining: report certificate
   digits, not just feasibility.
3. *From the Lean track:* adopt CS‑2's hypothesis discipline as the emission contract (it
   is `make_certificate_deep.py`'s asserts, elevated to a stated lemma); the m = 12 Bridge
   restatement at δ = 1e−16; and the redesign choice from CS‑1(iii) — my recommendation:
   parity split + triangular-W first (pure deletion of the largest block, no new
   mathematics), per-column scaling second, Bareiss-with-recompute only if RAM, not disk,
   binds. I offer the size/time accounting for whichever is chosen, and the P1/P2 numbers
   as acceptance tests.

**Offers.**
1. To Track A: the walls table (CS‑1 corollary) as the ladder's published feasibility
   envelope — including the honest headline that criterion-native certification saturates
   at effective height T* ≈ 80–340, and that this is *forced*, not fixable.
2. To Track B: Lemma CS‑1 as the yardstick that turns "certificate structure" claims into
   numbers (a per-prime block decomposition is interesting iff its digit count beats the
   0.21·m²·DENP lcm law).
3. To Track D: the CS‑4 harness spec with its three exit certificates; composition with the
   Lehmer-pair scanner is immediate.
4. To Track F: CS‑3 and CS‑4(iv) as the quantitative face of Π₁-ness — deciding-P(n) in
   Õ(n⁴) against Ω̃(n³), disproof-poly vs positivity-exp — slots directly into the
   reverse-mathematics/strength-map deliverable and the Yedidia–Aaronson bookkeeping.
5. To Track E: the invariance clause of CS‑1(v) as a constraint-table entry: any
   Hilbert–Pólya candidate that "explains" the envelope must equivalently explain why every
   computational certificate of the truncated positivity costs e^{Θ(e^{L/2}L)} bits — a
   proof of UPT is precisely an O(1)-size certificate, and nothing in between exists.

---

## 5. Honest assessment

The strongest objection to this program: **all four lemmas are about one vehicle — entrywise
ball certificates for Galerkin restrictions — and the walls I compute are walls of that
vehicle, not of the mathematics.** The oracle-model lower bounds (CS‑1(v), CS‑3(iii)) bind
algorithms that treat Q as data; a proof that exploits what Q *is* — Euler product plus
functional equation — escapes them entirely, and "escaping my lower bounds" is not a bug
but the literal definition of proving RH here. Certificate complexity measures the
obstruction with precision; it cannot move it. The associated failure mode for the program
is mistaking ever-sharper measurement of the wall for progress through it: a 3 MB kernel
certificate at the 1e−30 window (P1) would be a genuinely new kind of verified-computation
artifact and would still say nothing about L = 5.

Second objection, conditionality: the envelope law is measured (35 orders, three
out-of-sample hits) but not proved, and `RESULTS.md` itself flags that a mild upward bend
beyond L ≈ 4.2 is not excluded; every "reach" number above inherits that caveat (the
precision *floors* do not — they rest on the certified Rayleigh upper bounds — but the
walls' locations do). CS‑3's clean Õ(n⁴) additionally owes the truncation lemma, which is
an IOU written against another field.

Third, CS‑4 risks being theater: certified failure over a measure-zero family of modulated
windows, below heights where 2×10¹³ zeros are already verified, excludes nothing a number
theorist didn't already believe excluded. Its defensible value is narrow: it industrializes
Track D's bookkeeping so that *if* the pipeline ever produces a negative number, the
certificate discipline (four fake catastrophes caught in four scaling steps, per the
pathology log) is already wrapped around it.

Finally, a scope confession: nothing here engages the actual open lemma (UPT / the uniform
factorization of §2.12). My field's contribution is to have proved exactly how expensive it
is to keep *not* having that lemma — the price list, in digits, of finitism at this gate —
and to keep the disproof channel priced correctly. That is real, publishable, and useful
infrastructure; it is not the door.
