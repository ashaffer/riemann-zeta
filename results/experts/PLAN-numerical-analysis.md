# PLAN — Numerical analysis (approximation theory, validated numerics, structured solvers)

Independent expert plan, written without reading the other experts' PLAN files.
Repo data cited from `results/RESULTS.md`, `PROGRAM.md` §2.14–2.18, `THEOREMS.md`,
`results/agent-deep-windows/fit_report.txt`, `results/agent-lean-depth.md`, and the
docstrings of `src/spectral_margins.py`, `src/hp_margins.py`, `src/certified_spectral.py`.
New measurements from this plan's own stress tests live in
`results/experts/numerical-analysis-experiments/` (scripts + logs; 139 s + ~2 min,
single process each — inside the budget).

---

## 1. Reformulation

Every number in this program's ladder is a **Rayleigh–Ritz upper bound** λ_m(L) ≥ λ(L),
computed in a Galerkin space V_m, on the margin λ(L) = inf{Q_L(φ) : ‖φ‖₂ = 1} of the
truncated Weil form (THEOREMS.md conventions: a = L/4, Q_L = P + A − Π). From a
numerical-analysis standpoint the program is therefore two coupled objects:

1. **An approximation-theory object.** λ_m − λ is governed by the regularity of the
   minimizer φ⋆_L. The Euler–Lagrange equation is (c₀I + T + P − Π)φ⋆ = λφ⋆, where T is
   the convolution-type operator with symbol W(r) = Re ψ(1/4 + ir/2) − log π, sandwiched
   by the proved Lemma A (THEOREMS.md): ψ(1/4) + ½log(1+4r²) ≤ Re ψ(1/4+ir/2) ≤ same + 8.
   So T has **logarithmic order** — barely smoothing, barely coercive — and the prime
   part Π = Σ_n (Λ(n)/√n)·Sym(S_{log n}) injects truncated shifts whose indicators
   switch at the interior points x = ±t_n, t_n = |a − log n|. The measured basis
   phenomenology (hat m^{−3.6}: hp ladder 1.39741e-6 → 5.57117e-9 over m = 41→201;
   Legendre plunge-then-creep at L = 2.485: 7.5308e-8 → 3.86882e-10 by m = 24, then
   creep to 3.56788e-10 at m = 64, extrapolating to 3.49–3.50e-10) is a *readout of
   φ⋆'s singular structure*, and the exact form of that structure is decidable by the
   instruments in an afternoon (done below: the clean-corner model is now refuted).

2. **A validated-numerics object.** The envelope law ln λ(L) ≈ 10.2 − 1.755·e^{L/2}(L/2+4)
   (RESULTS.md, day-two second session) dictates the arithmetic: certifying window L
   requires resolving a scale e^{−1.755e^{L/2}(L/2+4)} inside O(1) matrices, so precision,
   Galerkin dimension, and exact-certificate bit-size are all *forced functions of L*.
   These cost laws are provable, and they quantify exactly how far the certified ladder
   and the Lean track can go — and where they must stop.

Under RH the form is the frame form of the exponentials {e^{iγx}} on [−a, a] (§2.14(v)),
so item 1 is simultaneously a statement about frame bounds of exponential systems near
the Nyquist edge T*(L) = 2πe^{L/2} — the plunge ends precisely when the Galerkin space
resolves the band [−T*, T*] (measured plunge-end m*(L) ≈ 1.8·a·T*(L) ≈ 5.6·(L/2)e^{L/2}:
24 at L = 2.485, ≈59 at L = 3.555, ≈128 at L = 4.6, matching the deep-window runs at
m = 112–184).

Four lemmas below: the creep-rate law (L1), its constructive counterpart and the
obstruction theorem the experiment just made necessary (L2), the certified-enclosure
precision law (L3), and the certificate bit-growth law (L4). L1/L2 were stress-tested
today with the kink-enrichment experiment; L3 with a minimal-precision bisection.

---

## 2. Lemma candidates

### Lemma 1 (minimizer regularity and the creep-rate law)

**(a) Statement.** Fix L non-threshold; let P_L = {n = p^k : log n < L/2},
t_n = |a − log n| (interior for a ≠ log n < 2a), and let φ⋆ be the (even, unit) ground
state. Define the source amplitudes J_n = (Λ(n)/√n)·|φ⋆(a)|. Then:

(i) *(local model)* φ⋆ is real-analytic on [−a,a] ∖ ({±t_n} ∪ {±a}); at each ±t_n it
carries a **log-regularized jump**: with σ the profile defined by
σ̂(r) = χ(r)/(ir·W̃(r)) (W̃ = full symbol, W̃(r) = ½log(1+4r²) + O(1)),

  φ⋆(t_n + ξ) − φ⋆(t_n − ξ) = 2c₁·J_n / ln(1/ξ) · (1 + O(1/ln(1/ξ))), ξ ↓ 0,

with c₁ explicit (c₁ = 1 for the model symbol ½log(1+4r²)); secondary, weaker
singularities of the same type at ±|a − log(n/n′)| (at L = 2.485: ±0.2158 = ±|a − log(3/2)|).

(ii) *(rate law)* the orthonormal-Legendre Galerkin ladder obeys

  λ_m(L) − λ(L) = Θ( A_L / (m ln m) ),  A_L ≍ a·(Σ_{n∈P_L} J_n² + J_∂²),

where J_∂ collects the endpoint (±a) singular amplitudes of the log-order operator.
Corollary (effective exponent): d ln(λ_m − λ)/d ln m = −(1 + 1/ln m + o(1)), i.e.
**1.24–1.31 over the measured window m ∈ [24, 64]** — against **3 − o(1)** for a clean
C⁰-function-with-φ′-jump ("corner") model, and ≈ **4** for hats on the analytic bulk
(measured hat transient: m^{−3.6}).

**(b) Proof strategy.** Write the E-L equation as Tφ⋆ = g with
g = (λ − c₀)φ⋆ − (pole part) + Σ_n (Λ(n)/√n)[φ⋆(·+log n)𝟙 + φ⋆(·−log n)𝟙]. The
indicators give g jump discontinuities at ±t_n of magnitude exactly (Λ(n)/√n)φ⋆(∓a).
Invert T through an explicit parametrix with symbol 1/W̃ (Lemma A supplies two-sided
bounds and |r·dW/dr| ≤ 2 + π/2 for symbol estimates); a jump source pushed through 1/W̃
yields the σ-profile; bootstrap analyticity away from the singular set (the shifts map
the singular set to {±t_n ± log n′} — note t_n − log n = −a exactly, so first-generation
kinks map to the *endpoints*, closing the bootstrap). Rate: second-order Rayleigh–Ritz
bound λ_m − λ ≤ ⟨(K−λ)e, e⟩/(1−‖e‖²) for e = φ⋆ − Π_{V_m}φ⋆ plus a spectral-gap term
(gap is comfortable: λ₂/λ₁ ≳ 7 in the measured cascade); compute the frequency tail
∫_{|r|>r_m} |φ̂_sing|²·W̃(r) dr with |φ̂_sing| ~ J/(r·W̃(r)) to get J²/(r_m ln r_m),
r_m ≈ πm/(2a). Lower bound: test against the profile itself (the singular parts at
distinct t_n are asymptotically orthogonal at high frequency).

**(c) Hardest missing step.** Endpoint theory: a Wiener–Hopf-type analysis of interval
restrictions of log-symbol operators (symbol unbounded but slowly varying — outside the
classical algebras), needed both for J_∂ and for proving φ⋆(a) ≠ 0 (currently an
assumption; if φ⋆(a) = 0 the whole singular hierarchy shifts one order down and the
rate becomes Θ̃(m^{−3})). This is genuinely open but self-contained.

**(d) Difficulty.** Conditional-on-(i) rate law (ii): 1–2 weeks of careful classical
work. Unconditional (i) including endpoints: a real paper (months); adjacent to but
distinct from the frontier's Sonin-space machinery.

**(e) Stress test (EXECUTED — `kink_enrichment.py`, 139 s).** Three independent
confirmations from today's run at L = 2.485:
- *Amplitude law:* measured φ⋆(a) = 5.13e-5 (from the enriched minimizer), giving
  J₂ = 2.5e-5, J₃ = 3.3e-5, hence predicted creep A_L/(m ln m) ≈ 1.4e-11 at m = 24
  against measured λ_24 − λ_∞ = 3.7e-11 — right order with a factor ≈2.6 left for the
  endpoint term J_∂ and secondary kinks. A clean O(1)-corner would have predicted a
  creep 10⁶ times larger; a zero-amplitude model would predict none.
- *No finite jump at probe scales:* φ(t₃+ε) − φ(t₃−ε) = −9.88e-2 / −3.77e-2 / −1.87e-2
  at ε = 0.05/0.02/0.01, i.e. ∝ 2ε·(−0.94): pure smooth slope, the singular component
  (predicted amplitude ~J/ln(1/ε) ~ 1e-5) invisible below it — as the LJ model requires,
  and as a visible corner would violate.
- *Exponent:* the docstring decrement fits (β ~ 1–1.2, `src/spectral_margins.py`) match
  the predicted effective exponent 1 + 1/ln m; the corner model's exponent 3 would have
  taken λ_64 to 3.502e-10 (measured: 3.5679e-10) — refuted in the plain ladder and
  independently refuted by the enrichment experiment (Lemma 2).

---

### Lemma 2 (enrichment: the obstruction theorem and the hp repair)

**(a) Statement.** Two branches; today's experiment selects between them.

(i) *(obstruction — now the live branch)* Under Lemma 1(i), for every fixed q and every
enrichment V_{m,q} = V_m ⊕ E_q by q piecewise-polynomial functions with breakpoints in
the singular set {±t_n}, the creep persists at full rate:

  λ_{m,q}(L) − λ(L) ≥ (1 − C_q/ln m) · c₀·A_L/(m ln m).

Piecewise-polynomial enrichment buys a constant factor, never a rate: the profile's
transform ~1/(r ln r · W̃-corrections) is not in the span of the corner transforms
r^{−k}, and the frequency-tail defect is bounded below after projecting out any finite
number of them.

(ii) *(constructive repair)* An hp-Legendre space on meshes geometrically graded (ratio
½, ℓ layers) toward every singular point {±t_n} ∪ {±a}, with degree p per layer and
p ≍ ℓ, restores root-exponential convergence:

  λ_{hp}(L) − λ(L) ≤ C(L) · e^{−b√N},  N = total DOF,  b ≥ ln 2 /√(s+1)-type explicit,

s = number of grading centers — because the log-profile is analytic on each geometric
layer with layer-uniform Bernstein parameter, and the sub-scale-2^{−ℓ} singular energy
is O(2^{−ℓ}/ℓ). The exact enrichment/mesh data at L = 2.485: grading centers
±0.0718972 (= |a − log 2|), ±0.4773623 (= |a − log 3|), ±a = ±0.62125.

**(b) Proof strategy.** (i): frequency-domain lower bound — minimize
∫_{r>r_m}|σ̂ − Σ a_k ĥ_k|²·W̃ dr over corner transforms ĥ_k ~ r^{−k}e^{−irt}; explicit
computation shows the optimal reduction is O(1/ln r_m). (ii): standard hp approximation
theory (Babuška–Guo-type arguments) transplanted to the log-profile, plus the same
Rayleigh–Ritz second-order bound; the only nonstandard input is again Lemma 1(i).

**(c) Hardest missing step.** None beyond Lemma 1(i) — both branches are conditional
theorems of classical type once the local model is granted. (For (ii) at certified
level: the graded-mesh basis must enter the interval assembly; Lemma 3(i) covers it.)

**(d) Difficulty.** (i): ~1 week. (ii): 2–3 weeks including a working implementation.

**(e) Stress test (EXECUTED — the kink-enrichment experiment; pre-registered, then run).**
Setup: even-parity block at L = 2.485, dps 50/40, repo conventions reproduced
independently (piecewise-GL assembler; validation: plain even block K=12 matches
`spectral_form(2.485, 24)` = 3.8688156e-10 to rel. 2.2e-21; Gram = I to 2.7e-51;
enriched-mesh vs plain-mesh cross-quadrature agreement 2.2e-21; zero-side oracle
2Σ₄₀|φ̂(γ)|² = 3.05e-10 ≤ λ: OK). Pre-registered: corner-kink Model K predicts
enriched 24+4 ∈ [3.49, 3.52]e-10 (below plain m=64); log-jump Model LJ predicts
marginal gain. **Measured:**

| variant | λ_min |
|---|---|
| plain m=24 (anchor) | 3.8688156e-10 |
| 24 + 2 corners (|x|−t_n)₊ | 3.75432393e-10 |
| 24 + 4 (corners + quadratic corners) | 3.74025364e-10 |
| 32 + 4 | 3.57091208e-10 |
| plain m=64 (repo) | 3.56788e-10 |

**Model K is refuted**: 24+4 lands above even plain m=32; V3 − V2 = −1.69e-11 is
creep-sized (K predicted ≤ 2e-12); the snaps capture 31% (m=24) / 57% (m=32) of the
residual to the 3.50e-10 extrapolation — a constant factor, exactly the obstruction
branch's signature. The repo's phrase "interior derivative kinks" should be retired in
favor of the log-regularized jump; the practical route to operator margins is the hp
mesh of (ii), not snap functions. (Honesty: the measured 24+4 value even exceeded the
pre-registered LJ band [3.55, 3.59]e-10 — corners capture *less* than my LJ estimate;
the constant C_q in (i) is larger than guessed, and/or J_∂ carries more of A_L.)

---

### Lemma 3 (certified enclosures: the two-term precision law and the quadrature-free class)

**(a) Statement.**

(i) *(quadrature-free assembly class — angle (d))* Let the archimedean weight admit a
Laplace-type representation W(r) − W(0) = ∫₀^∞ (1 − cos ru)·w(u) du with w explicitly
enclosable with geometric tails (true for ζ and both Dirichlet parities via Gauss's
digamma integral — `src/hp_margins.py`), and let the test basis consist of piecewise
polynomials with algebraic breakpoints. Then every entry of the truncated-Weil matrix
reduces, with **no oscillatory integral**, to finite rational combinations of the
enclosable constants {ψ(a₀), log π, log p, exponentials of rational multiples of a,
kernel moments ∫ u^s w(u) du}, and interval assembly at p bits yields entrywise
enclosure radius w_entry ≤ 2^{−p}·κ_asm(basis). For the *unnormalized* Legendre basis
(`certified_spectral.py`), coefficient growth ~4^{deg} in the universal F_kj gives
log₂ κ_asm ≈ c_κ·m with c_κ ∈ [2.4, 3.1] **(measured — see (e))**; for a compensated /
orthonormal-scaled assembly, κ_asm = poly(m). Caveat made explicit: the single-center
Bernoulli kernel series converges only for 2a < π, so the current machinery walls at
L < 2π ≈ 6.28; piecewise re-expansion of w about interior centers (radius
√(u₀²+π²)) extends the class to L ≲ 11 with two centers.

(ii) *(certification law)* Outward-rounded interval Cholesky on Q − βG (dimension n)
certifies λ_min > β **iff** λ_min − β ≳ n·w_entry + C·n²·2^{−p}·max_i(Q_ii), so the
minimal working precision is

  **p_min(L, m) = log₂(1/λ(L)) + log₂ κ_asm(m) + Θ(log m).**

(iii) *(cost horizon of the certified ladder)* With m*(L) ≈ 5.6·(L/2)e^{L/2} (measured
plunge-end law, §1) and the envelope, p(L) ≈ 2.53·e^{L/2}(L/2+4) bits + overhead:
concretely λ ~ 10^{−103} / 10^{−185} / 10^{−329} and (m, p) ≈ (340, 400) / (650, 700) /
(1220, 1150) at L = 6 / 7 / 8. Assembly O(m²·N_series) and factorization O(m³) interval
ops keep this workstation-feasible to L ≈ 7–8 and infeasible past L ≈ 9: **the certified
ladder saturates at finitely many windows** — a provable quantitative complement to the
finite-cutoff delimitations of arXiv:2607.02828.

**(b) Proof strategy.** (i) is the repo's own construction (`certified_margins.py` /
`certified_spectral.py`) generalized to the piecewise class — the new content is the
κ_asm bookkeeping (Horner condition numbers of the exact polynomials) and the piecewise
kernel re-expansion. (ii) is Rump-style verified-Cholesky analysis; for the hat basis
(Q = Toeplitz + rank-2) a validated Schur-algorithm variant gives the same law in O(n²)
ops (Bojanczyk–Brent–de Hoog–Sweet stability for PD Toeplitz, with the rank-2 pole
folded in by bordering rather than interval Sherman–Morrison).

**(c) Hardest missing step.** Nothing deep: the validated O(n²) Toeplitz path's rounding
analysis with bordering is fiddly; κ_asm for the compensated assembly needs a clean
statement. This lemma is engineering-grade mathematics with high program value.

**(d) Difficulty.** Low–medium; a tools paper. The payoff items — compensated assembly
(2.5× precision saving, below) and the L < 2π wall removal — are days of work each.

**(e) Stress test (EXECUTED — `precision_law_test.py`).** The repo's ζ, L = 711/200,
m = 40 rung (λ ~ 1.7997e-20, certified at 220 bits) was re-certified at reduced
precision: **True at 220 and 190 bits; False at 160, 145, 130, 100, 88, 76, 64.** So
p_min ∈ (160, 190]: the eigenvalue scale accounts for 66 bits, leaving a measured
assembly overhead of 95–125 bits = (2.4–3.1)·m — the naive model (p_min ≈ 80) is
refuted and the coefficient-growth term of (i) is confirmed as the dominant cost.
Falsifiable consequence logged in §3 (P3).

---

### Lemma 4 (bit growth of exact rational certificates — the Lean-track wall and its bypass)

**(a) Statement.**

(i) *(growth law)* For the program's integer congruence format (c²B = Wᵀdiag(g)W,
`lean/make_certificate.py`) built by exact fraction-free LDLᵀ on an n×n PD integer
matrix with DENP-digit entries: the leading minors obey Hadamard's bound
digits(Δ_k) ≤ k(DENP + ½log₁₀ k + O(1)), whence

  digits(c) ≤ ½·n²·DENP·(1+o(1)),  digits(g) = 2·digits(c)·(1+o(1)),

and total certificate data ≈ n·digits(g) ≈ n³·DENP digits. The measured law
(`results/agent-lean-depth.md`: digits(c) ≈ 0.21·m²·DENP to ≤4% across four windows,
602 → 1283 → 3377 → 15145; digits(g)/digits(c) = 2.04/2.02/2.01/2.00) sits a factor
≈2.4 inside the bound: **the blow-up is intrinsic to the dense exact-LDLᵀ format, not
an implementation artifact.** Coupled to the envelope through DENP ≥ E(L) =
log₁₀(1/λ(L)), kernel-checking cost ≈ m³·(m²·DENP)^{1/2} walls at (m, DENP) ≈ (96, 32),
i.e. at the p = 3 window's certified depth — as the Lean-depth session measured.

(ii) *(bypass: rounded-Cholesky inequality certificates)* Exactness of the congruence is
unnecessary. For PD integer B with λ_min = μ, set s = ⌈log₁₀(n‖B‖/μ)⌉ and
W̃ = round(10^s·chol(B)): then B − 10^{−2s}W̃ᵀW̃ has entrywise bound absorbable into a
verified diagonal slack, and the kernel needs only *integer inequalities*. Every
certificate integer then has ≤ E(L) + log₁₀ m + log₁₀ κ + O(1) digits — **linear in
depth instead of m²·DENP**: at the (m = 48, E ≈ 15) window, ~25-digit integers instead
of the measured 30,319-digit g's; kernel cost drops to ≈ m³·E^{1/2}. This moves the
formal-verification wall from L ≈ 3.6 out to the certified ladder's own arithmetic
horizon (Lemma 3(iii)).

**(b) Proof strategy.** (i): Bareiss/Hadamard classics plus an audit of the repo's
specific c-and-W construction (two Cholesky passes explain the factor-2 pattern
c ~ 2× single-pass, g ~ 2c). (ii): standard verified-numerics rounding argument
(as in rational SDP certification); the only work is casting the residual bound as a
kernel-friendly integer statement (Gershgorin slack on B − 10^{−2s}W̃ᵀW̃).

**(c) Hardest missing step.** For (ii): matching the existing Lean framework, which
verifies an *equality* by kernel reduction — an inequality-form checker (decide on
integer comparisons; already used for g > 0) must replace it; no new mathematics,
some new Lean.

**(d) Difficulty.** (i): days. (ii): 1–2 weeks including the Lean prototype.

**(e) Stress test (proposed, cheap).** Emit a rounded-Cholesky certificate for the
already-certified ζ, L = 749/250, m = 48 window and measure integer sizes: prediction
≤ 30 digits per entry (vs 30,319 measured for exact g's), kernel check time seconds
(vs the measured 158 s wiFun elaboration limit). Falsifies (ii) if rounding cannot
absorb the residual at s within 2 of the formula.

---

## 3. Predictions

**P1 (enrichment ceiling — pre-registered follow-up to today's refutation).** No
enrichment of the m = 24 even block at L = 2.485 by ≤ 10 piecewise-polynomial functions
with breakpoints in {±t₂, ±t₃} reaches below 3.55e-10. Specifically, adding cubic
corners (|x|−t_n)₊³ to V2 (i.e. 24+6) lands in **[3.725, 3.741]e-10** — within 1.5e-12
of V2's 3.74025e-10, because the obstruction (Lemma 2(i)) caps the gain at O(1/ln m).
(For calibration: today's measured 24+2 = 3.75432e-10, 24+4 = 3.74025e-10.)

**P2 (hp repair).** An hp-Legendre space geometrically graded (ratio ½, 3–4 layers)
toward {±t₂, ±t₃, ±a} at L = 2.485 with ~40 even-parity DOF reaches **λ ≤ 3.51e-10**
(beating plain m = 64's 3.56788e-10), and at ~60 DOF pins the operator margin f(3) to
three digits (predicted **3.49–3.50e-10**, the docstring extrapolation). If instead
hp-refinement stalls at the V2/V3 level, Lemma 1's local model is wrong and the
singularity is not at the predicted locations — a clean kill condition.

**P3 (precision law at the next rung).** For the ζ, L = 749/250, m = 48 certified rung
(λ ~ 4.346e-15, 47.7-bit scale; measured c_κ ∈ [2.4, 3.1] gives overhead 115–149 bits):
interval-Cholesky certification **succeeds at 200 bits and fails at 150 bits**
(p_min ∈ (150, 200]). One `certify_spectral` call per precision to falsify. Corollary
prediction: a compensated (orthonormal-scaled) assembly drops p_min for the L = 711/200,
m = 40 rung from the measured (160, 190] to below 110 bits.

---

## 4. Interfaces

**Needs.**
- *From harmonic analysis:* endpoint behavior of interval-restricted log-symbol
  operators (Wiener–Hopf outside the classical algebras) — the missing step of Lemma 1;
  and the Landau–Widom/Sonin asymptotics that would connect A_L and the profile
  constants to the envelope's b ≈ 1.755 and offset +4.0 (ENVELOPE.md's sharpest
  question; my creep constants are the finite-m shadow of the same asymptotics).
- *From the Lean track:* an integer-inequality kernel checker (decide-based) to receive
  Lemma 4(ii)'s rounded certificates.
- *From convex optimization (Track B):* block-structured SOS formats to compare against
  Lemma 4(ii) — per-prime blocks vs rounded-Cholesky is exactly the certificate-
  compression question, and Lemma 4(i) proves the dense format both will beat.

**Offers.**
- *To the envelope program (biggest offer):* a creep-corrected joint fit. The deep-window
  refits (`results/agent-deep-windows/fit_report.txt`) show the law's b drifting
  1.64 → 1.08 → 0.94 as deeper *unconverged* points enter — Rayleigh–Ritz bias
  masquerading as an envelope bend. Lemma 1 supplies the two-parameter correction
  λ_m(L) = λ(L) + A_L/(m ln m): fit λ(L) and A_L jointly and the "mild upward bend"
  question (RESULTS.md, day-two fourth session) becomes decidable with existing data,
  no new deep runs.
- *To all measurement tracks:* the hp basis (Lemma 2(ii)) — predicted to reach current
  deep-window accuracy at ~⅓ the DOF (m ≈ 40–60 vs 112–176), which compounds with
  Lemma 3's p(L) into roughly an order of magnitude on total certified-ladder cost.
- *To the Lean track:* Lemma 4(ii) certificates (linear-in-depth integers), plus Lemma
  3's O(n²) validated Toeplitz path for hat-basis windows.
- *To computer science / complexity:* Lemma 3(iii) and 4(i) as theorems delimiting
  finite certification — the program's own instruments proved where they stop; useful
  jointly with arXiv:2607.02828 for an honest statement of what any finite numerics can
  ever certify here.
- *To harmonic analysis:* measured singular data for the minimizer: φ⋆(a) = 5.13e-5 at
  L = 2.485, amplitude law J_n = (Λ(n)/√n)|φ⋆(a)|, no visible finite jump at ε ≥ 0.01 —
  constraints any proposed Sonin-space description must reproduce.

---

## 5. Honest assessment

The strongest objection: **everything above is about the instrument, not the theorem.**
All four lemmas sharpen the measurement and certification of λ(L) — but positivity of
λ(L) for *every* L is RH itself, and my own Lemma 3(iii)/4(i) prove the certified
ladder saturates at finitely many windows (L ≈ 8–9 at best). This program's numerical
track can therefore *never* close UPT; its value is exclusively (a) precision data
feeding the analytic tracks (the envelope constants, the rigidity offset), (b) the
disproof channel (a certified negative eigenvalue is a theorem), and (c) proved
meta-theorems about what finite computation can see. I consider that value real but
strictly auxiliary.

Second objection, to my own lemmas: the entire regularity story (L1, and through it L2)
rests on an unproven E-L local model whose hardest ingredient — endpoint theory for
log-symbol operators, including φ⋆(a) ≠ 0 — is exactly the part nobody has done, and
the supporting evidence is a creep exponent measured over 1.4 octaves of m plus one
refuted alternative. Today's experiment killed the corner model decisively, but it does
*not* uniquely confirm the log-jump model: an endpoint-dominated singular structure
(J_∂ ≫ Σ J_n) is consistent with everything measured today (the snaps captured 31–57%,
and interior-vs-endpoint contributions were not separated). P2 is designed to be the
discriminating experiment; if hp grading toward the *interior* points contributes
nothing once endpoint grading is present, Lemma 1's interior model loses its teeth even
if the rate law survives. Finally, the precision-law constants (c_κ ∈ [2.4, 3.1]) come
from a single (L, m) bracket; P3 is the immediate check that they transfer.
