# RH-LEMMA-MAP: from this repository's formal artifacts to `RiemannHypothesis`

Mathlib states RH (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`:
`def RiemannHypothesis : Prop`). This document is the honest dependency map
from what is FORMALIZED HERE to that statement, level by level, with each gap
named and sized. It is the program's Track-A/F ledger (PROGRAM.md §4) in
actionable form, and the index of "lemmas that help pursue the final goal."

## The standing objective and its three-outcome structure

The program's ultimate goal (standing directive, 2026-07-26): proof, disproof,
or proven ZFC-independence of RH, pursued by incremental lemma accumulation.
The outcomes are NOT symmetric, and the lemma streams serve them differently:

- **DISPROOF** — the finitely-certifiable branch (RH is Π₁). Our machinery is
  sign-symmetric: a certified negative eigenvalue with all window primes
  included is a kernel-checkable finite disproof. Disproof-side lemmas:
  NT-4 (quantitative converse Weil: an off-line zero at (½+δ₀, γ₀) forces
  λ(L₀) < 0 at explicit L₀ — turns zero-hunting into margin-hunting), CO-4
  (the odd-sector one-scalar channel θ(L) ≤ 1), Track D's four hunters, and
  the certificate depth law (which prices how deep a disproof certificate
  must go). Every certified-positivity tool doubles as a disproof tool.
- **PROOF** — requires the uniform statement (UPT, §3 of PROGRAM.md). Served
  by Levels 0–5 below plus the panel's merged targets (SYNTHESIS.md §3):
  the envelope normalization is now quantitatively pinned, so UPT has a
  concrete normalized form to aim at.
- **PROVEN INDEPENDENCE** — the collapsing branch: since RH's falsity has a
  finite certificate, a proof of ZFC ⊬ ¬RH already yields RH's truth
  (provable-Σ₁-completeness; PROGRAM.md Track F). So independence is not a
  separate hunt: it is served by the SAME formal infrastructure, and its one
  concrete lemma is Track F(i) — formalize the transfer theorem
  ¬Prov_ZFC(¬RH) → RH. Our Lean stack (five windows, the framework, the
  sandwich) is the natural substrate; the mathlib ingredients are provability
  logic (present in part) + the Π₁ certificate encoding of a zero-counting
  discrepancy (absent; a delimitable project). Any claimed independence route
  that does not pass through this collapse is wrong by arithmetic.

## Level 0 — kernel-checked today (axioms: propext, Classical.choice, Quot.sound)

| artifact | statement | file |
|---|---|---|
| `WeilCert.weil_window_positive` | every rational 12×12 matrix within 1e−20 of `mRat` (ζ, L=497/200) has positive quadratic form — data regenerated 2026-07-26 after pathology #5 | `lean/weilcert/Weilcert.lean` |
| `WeilCertDeep.weil_window_positive` | same at m=24, δ=1e−14 (1e−10-scale window) | `WeilcertDeep.lean` |
| `WeilCertDeeper.weil_window_positive` | same at m=48, δ=1e−19 (1e−15-scale window); 10-min kernel check | `WeilcertDeeper.lean` |
| `WeilCertFamily.weil_window_positive` | **first GRH-side window**: χ₋₇, L=5, m=16; certified 3.54950e−6 < λ_min ≤ 3.54961e−6 | `WeilcertFamily.lean` |
| `Bridge.legendre` + `Bridge.overlap_k_j` (49 pairs) | Legendre polynomials + ALL shifted-overlap integral identities for k+j ≤ 12, pure FTC | `BridgeLegendre.lean`, `BridgeOverlap.lean` |
| `CertFramework` / `CertInstance` | n-generic certificate framework; `WeilCert` re-derived through it | `CertFramework.lean`, `CertInstance.lean` |
| `CurveCertE5.*` (36 thms) | **first END-TO-END kernel-checked window** (function-field side): E: y²=x³+x+1/F₅ — point count #E(F₅)=9 by `decide` over ZMod 5, Gram matrices DEFINED from it, positivity (rung 2), Cayley–Hamilton kernel vector (rung 3), sign-flip witness, plus genus-2/F₇ block (incl. the 2401-check F₄₉ count). NO interval arithmetic anywhere — unlike the ζ rows above, the bridge itself is kernel-checked; only classical paper math (Parseval–Zak + Riemann–Roch) remains outside | `CurveCertE5.lean` |
| `GlideKernel.laplace_sin` | ∫₀^∞ e^{−at} sin(st) dt = s/(a²+s²) (a>0) | `lean/glide/Glide/Basic.lean` |
| `GlideKernel.frullani_cos` | ∫₀^∞ e^{−at}(1−cos bt)/t dt = ½log(1+b²/a²) | same |
| `GlideKernel.kernel_lower/upper` | ½log(1+4r²) ≤ ∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t})dt ≤ ½log(1+4r²)+8 | same |

Certificate scaling (measured, `results/agent-lean-depth.md`): digits(c) ≈
0.21·m²·(digits per entry); kernel decide time ≈ m³·√digits — the formal
ladder's reach is priced (see also PLAN-computer-science.md walls). Standing
oracle since pathology #5: nested certificates at the same L must agree on
overlapping blocks within their combined rounding budgets.

## Level 1 — the Bridge (computer-assisted → formal)

Gap: prove IN LEAN that the truncated Weil matrix at (L = 497/200, Legendre
m = 12) lies in the 1e−20 ball around `mRat` (today: interval arithmetic with
stated trust base; THEOREMS.md Bridge Proposition — corrected 2026-07-26, see
pathology log #5). Sub-lemmas, status as of 2026-07-26:
1. **Overlap polynomials** — ✅ DONE (bridge-formal agent): `Bridge.overlap_k_j`
   for ALL 49 pairs k+j ≤ 12, pure FTC proofs, plus `Bridge.legendre` with
   degree/leading-coefficient lemmas (mathlib had only shiftedLegendre) and
   the scaled ledger identity T_kj(u) = a·F_kj(u/a). 84/84 theorems on the
   three standard axioms. Files: lean/weilcert/Bridge{Legendre,Overlap}.lean;
   generic framework: CertFramework.lean (arbitrary n; WeilCert re-derived).
2. **Kernel-moment identities**: Bernoulli generating identity EXISTS formally
   (`bernoulli'PowerSeries_mul_exp_sub_one`); the ANALYTIC z/(e^z−1) with
   radius-2π coefficient bounds is absent. Effort: 8–15 person-days.
3. **Pole vectors**: elementary positive-series bounds. Effort: days.
4. **Numeric enclosures**: π to 20 digits exists (`Real.pi_gt_d20`), e to
   1e−20 (`exp_one_near_20`), log 2 to 1e−10 (extensible); γ is the bottleneck
   (mathlib: only 1/2 < γ < 2/3; no Euler–Maclaurin). Effort: 10–20 pd. NOTE:
   the integer-congruence design needs NO γ at Level 1; γ enters at Level 2.
Total bridge estimate (bridge-formal agent's audit): ≈ 60–115 person-days,
three parallelizable long poles (Gauss integral, analytic Bernoulli, γ).

## Level 2 — Gauss's digamma formula (the identification lemma)

Gap: `Re (Complex.digamma (1/4 + I*r/2)) − Complex.digamma (1/4) =
∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t}) dt`. Mathlib has `Complex.digamma`
(logDeriv Gamma, recurrence, special values incl. γ) but NOT Gauss's integral.
Route: Binet/Gauss via the Gamma integral representation + differentiation
under the integral (mathlib has the dominated-convergence machinery). This
lemma converts `kernel_lower/upper` into the digamma sandwich of THEOREMS.md
Lemma A — the exact form used by the Glide Theorem. Effort: weeks; a clean,
publishable mathlib contribution on its own.

## Level 3 — the Glide Theorem, formal

Gap: formalize THEOREMS.md Theorem 1 (monotonicity + explicit-modulus
continuity of λ(L)). Needs: L² on an interval (mathlib ✓), Fourier–Plancherel
(mathlib ✓), the kernel sandwich (✓ Level 0 + Level 2), the elementary
a-priori lemmas B–E (routine given the above), and the dilation bookkeeping.
Effort: months. Prior art note: qualitative continuity is Suzuki
(arXiv:2606.09096, Thm 1.3), asserted earlier by Bombieri; what would be new
in mathlib is the whole framework — the truncated Weil form itself has never
been formalized.

## Level 4 — the finite criterion, formal

Gap: state IN LEAN the windowed Weil criterion: "for every L, the truncated
form Q_L is positive semidefinite on C_c^∞(−L/4, L/4)" and prove its
equivalence with `RiemannHypothesis`. Ingredients: the explicit formula
(Guinand–Weil) in Lean — the serious item; mathlib has `riemannZeta`, the
functional equation, `ArithmeticFunction.vonMangoldt`, Hadamard factorization
pieces; the explicit formula itself is a known missing keystone (also needed
by PrimeNumberTheoremAnd-style projects). Effort: a research-grade
formalization project (many months), but with independent value far beyond
this program.

## Level 5 — RH

By Level 4's equivalence, RH = "Level-0-style certificates exist at every L" —
which is exactly PROGRAM.md §3's UPT plus exhaustion. The measured envelope
law (ENVELOPE.md) says what the certificates must survive: margins
~exp(−1.755·(T*/2π)(log(T*/2π)+4)) mid-range, saturating at the universal
prolate rate exp(−4π·T*/2π + O(L)) past L ≈ 4.32 (the measured 4π cap,
2026-07-26 — deep-windows final; the cap slightly SOFTENS the asymptotic
price of depth relative to the old chart). No finite process closes Level 5;
the map exists so that every finite step lands in the right place.

## The two lemmas most worth proving next (informal mathematics)

1. **The envelope law as a theorem about counting functions** (the mechanism
   experiment licenses this): for the SMOOTH staircase γ̃_k (N(γ̃_k) = k−1/2),
   prove two-sided bounds of the shape
   c₁·E(L) ≤ −log λ̃(L) ≤ c₂·E(L), E(L) = (T*/2π)(log(T*/2π) + c₀),
   via Landau–Widom/Turán methods. This is now a statement in pure harmonic
   analysis — no zeta input at all — and the law-theory agent + harmonic-
   analysis expert are on it.
2. **The transfer inequality on one window pair** (PROGRAM §3 scaled down):
   an explicit inequality transferring positivity from window W_p to W_{p'}
   for ONE pair (2→3) with the measured normalization — the minimal
   non-trivial instance of UPT, and a concrete target for the expert panel's
   harmonization round.

*Prior-art annotations per results/agent-prior-art.md: margin-decay
"exponential of exponential" appears in Connes arXiv:2602.04022 §6.4 with a
Fuchs-prolate comparator; qualitative continuity is Bombieri/Suzuki; the
support-normalized 3-constant law, family universality, mechanism experiment,
explicit modulus, and all Level-0 artifacts are this program's own (pending
the standing caveat).*
