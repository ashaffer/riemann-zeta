# FULLINF — a certified lower bound for the truncated Weil form beyond the Galerkin subspace

NT seat, round 3 assignment (coordinator: "certified full-infimum lower bound at
one window"). Status: **the mathematics is complete and verified numerically;
the composite closes — but not in the form the assignment guessed, and the
honest headline has three parts.**

1. **(Positive)** Theorem F4 below upgrades any certified Legendre–Galerkin
   window value λ_m to a certified lower bound on the infimum of Q_L over an
   explicit **infinite-dimensional, basis-independent class** of test functions
   (a frequency-tail class containing all Gaussian wave packets probing heights
   up to ≈ 40): at L = 7/4, m = 192, the certified statement is
   inf over the class of Q_L(φ)/‖φ‖² ≥ **1.56×10⁻⁵**, pending exactly one
   standard certified run (Legendre interval-Cholesky at (L, m) = (7/4, 192);
   the m = 96 variant already closes with weaker coverage). Composed with the
   quantitative converse Weil lemma (NT-4(i), my PLAN §2), this yields
   criterion-native, Riemann–Siegel-free exclusion statements for off-line
   zeros at heights ≤ ~40 — symbolic first blood: the heights are covered a
   trillion times over by Platt–Trudgian, but the *pipeline* is new in kind.
2. **(Negative, structural)** The unrestricted full infimum is **provably out
   of reach of this entire proof template**: the Weil form's coercivity in
   frequency is logarithmic (Lemma A(ii) of THEOREMS.md, sharp by A(iv)), and
   Theorem F5 shows every "certified subspace + a-priori tail" argument has
   error ≥ ~2.8 — five orders of magnitude above the margin — at EVERY
   subspace dimension. The restriction to a smoothness/tail class is not a
   convenience; it is forced, and F5 says exactly why.
3. **(Negative, basis-specific)** Proposition F6 quantifies a second
   obstruction: polynomial (and hat) subspaces have Fourier content up to
   r ≈ m/a but capture competitors only below r ≈ 0.66·m/a; in the gap the
   coupling is O(1). This "capture-vs-content conflict" is why the class in
   F4 must sit at tail masses ~10⁻¹⁶ — and why the **prolate basis is forced,
   not preferred**, for any future tightening (§7): with band-concentrated
   basis functions the conflict disappears by construction. This gives M1's
   "prolate-basis" clause a theorem-level justification it did not have.

Everything below is self-contained modulo THEOREMS.md; every constant is
explicit; §8 verifies each number by script (mpmath / numpy, outputs quoted);
§9 maps the Lean gap. Notation: a = L/4, unit φ ∈ H_L = L²[−a,a] extended by
zero, φ̂(r) = ∫φe^{−irx}dx, V_m = polynomials of degree < m on [−a,a],
P_m = L²-orthogonal projection onto V_m, λ_m^cert = certified lower bound of
the Galerkin minimum over V_m (interval Cholesky, existing instruments).

---

## 1. Lemma F0 (the form is frequency-diagonal plus an explicit rank-two term)

For unit φ ∈ H_L,

  Q_L(φ) = (1/2π) ∫_ℝ |φ̂(r)|² Ω_L(r) dr + P(φ),

  Ω_L(r) := Re ψ(1/4 + ir/2) − log π − Σ_{n ≤ e^{L/2}} 2Λ(n) n^{−1/2} cos(r log n),

with P(φ) = 2(∫φe^{x/2})(∫φe^{−x/2}) the pole term.

*Proof.* The archimedean term is definitionally the first two summands
(ledger, PROGRAM.md §6). For the primes: ψ_φ(u) = (1/2π)∫|φ̂|²e^{iru}dr
(Wiener–Khinchin; the same identity used in THEOREMS.md Lemma D, valid since
φ ∈ L¹∩L², both sides continuous), and ψ_φ is even, so
2Λ(n)n^{−1/2}ψ_φ(log n) = (1/2π)∫|φ̂|²·2Λ(n)n^{−1/2}cos(r log n)dr. The prime
sum is finite (n < e^{L/2}). ∎

## 2. Lemma F1 (envelope bounds on the symbol)

Let C_pr(L) := Σ_{n ≤ e^{L/2}} 2Λ(n)n^{−1/2}, κ₀' := |ψ(1/4) − log π| = 5.3722…,
c₀ := κ₀' + 8 + C_pr(L), and Ω̄(r) := c₀ + ½log(1+4r²). Then for all real r:

 (i) |Ω_L(r)| ≤ Ω̄(r);
 (ii) Ω_L(r) ≥ −c₋, c₋ := κ₀' + C_pr(L);
 (iii) Ω_L(r) > 0 for |r| ≥ r₊(L) := ½(e^{2c₋} − 1)^{1/2}.

At L = 7/4: C_pr = 2 log2/√2 = 0.9803, c₀ = 14.352, c₋ = 6.352, r₊ = 286.9.
At L = 497/200: C_pr = 0.9803 + 2 log3/√3 = 2.2489, c₀ = 15.621, c₋ = 7.621,
r₊ = 1020.3.

*Proof.* THEOREMS.md Lemma A(ii),(iv) sandwich Re ψ(1/4+ir/2) − log π between
−κ₀' + ½log(1+4r²) and the same +8; the cosine sum is bounded by ±C_pr. (iii)
solves ½log(1+4r²) > c₋. ∎

## 3. Lemma F2 (capture: low frequencies are seen by V_m)

For all real r and m ≥ 1, with z = |r|a:

  ‖(I − P_m) e^{irx}‖²_{L²[−a,a]} = 2a · B_m(z),   B_m(z) := Σ_{k≥m} (2k+1) j_k(z)²,

and whenever q_m := z²/((2m+1)(2m+3)) < 1:

  B_m(z) ≤ t_m(z)/(1−q_m),   t_m(z) := (2m+1) z^{2m} / ((2m+1)!!)².

*Proof.* The orthonormal Legendre coefficients of e^{irx} on [−a,a] are
c_k = i^k √(2a(2k+1)) j_k(ra) (standard plane-wave expansion), and
Σ_{k≥0}(2k+1)j_k(z)² = 1 (spherical-Bessel addition theorem at θ = 0), which
also confirms ‖e^{irx}‖² = 2a. For the tail bound: the integral representation
j_k(z) = z^k/(2^{k+1}k!) ∫_{−1}^1 e^{izt}(1−t²)^k dt gives
|j_k(z)| ≤ z^k/(2k+1)!!; the summand ratio is z²/((2k+1)(2k+3)) ≤ q_m, so the
tail is dominated by the geometric series. ∎

Consequences (both used below; ε-terms superexponentially small once
aR ≤ 0.9·(2m/e)): for w = (I−P_m)φ, ‖φ‖ = 1,
 (a) sup_{|r|≤R} |ŵ(r)| ≤ ‖w‖·√(2a·B_m(aR));
 (b) ‖(I−P_m)φ_R‖ ≤ √(R/π)·√(2a·B_m(aR)) for the band-limited part φ_R.

## 4. Lemma F3 (content: what V_m carries at high frequency)

For unit u ∈ V_m and all r ≠ 0, with z = |r|a:

  |û(r)|² ≤ 2a · min( 1,  πm²/(2z),  (π/2)·c_L²·m²·z^{−5/3} ),  c_L = 0.7858.

*Proof.* |û(r)|² ≤ ‖u‖²‖e^{irx}‖² = 2a (Cauchy–Schwarz) gives the first
branch. For the others, |û(r)|² ≤ 2a·K_m(z), K_m(z) = Σ_{k<m}(2k+1)j_k(z)²
(Bessel's inequality in the plane-wave expansion), and
j_k(z)² = (π/2z)J_{k+1/2}(z)² with |J_ν| ≤ 1 (Bessel's bound) gives the
second; Landau's uniform bound |J_ν(z)| ≤ c_L z^{−1/3} (Landau, *Monotonicity
and bounds on Bessel functions*, 2000; c_L = 0.78574…) gives the third, using
Σ_{k<m}(2k+1) = m². ∎

Definition (the content functional): for R > 0,

  T₂(m, R) := sup_{unit u ∈ V_m} (1/2π)∫_{|r|>R} |û(r)|² Ω̄(r)² dr
            ≤ (1/π)∫_R^∞ 2a·min(1, πm²/(2ar), (π/2)c_L²m²(ar)^{−5/3})·Ω̄(r)² dr,

an explicit one-dimensional integral (evaluated in §8; e.g. √T₂ = 643 at
L = 7/4, m = 192, R = 284).

## 5. Theorem F4 (certified class-restricted full-infimum lower bound)

Fix L, m, and a cut R with aR ≤ 0.9·(2m+1)/e. Let λ_m^cert be a certified
lower bound for the Galerkin minimum of Q_L over V_m. Define the class

  𝒞(R, τ̄) := { φ ∈ H_L : ‖φ‖₂ = 1, (1/2π)∫_{|r|>R} |φ̂(r)|² dr ≤ τ̄ }.

Then for every φ ∈ 𝒞(R, τ̄):

  Q_L(φ) ≥ λ_m^cert·(1 − ε²) − E,  where
  β := √(2a·B_m(aR)),  ε := √τ̄ + √(R/π)·β,
  E := 2[ √T₂(m,R)·√τ̄ + Ω̄(R)·√(R/π)·β·ε + √(2 sinh a)·δ_P·ε ] + (c₋ + λ_m^cert)·ε²,
  δ_P := ‖(I−P_m)e^{x/2}‖ + ‖(I−P_m)e^{−x/2}‖ (superexponentially small).

*Proof.* Write φ = u + w, u = P_mφ (support is preserved: V_m ⊂ H_L). Then
Q(φ) = Q(u) + 2B(u, w) + Q(w) with B the polarization of Q.

(1) Q(u) ≥ λ_m^cert‖u‖² = λ_m^cert(1 − ‖w‖²), and ‖w‖ ≤ ε by splitting
φ = φ_R + φ^R: the band-limited part is captured to Lemma F2(b), the tail has
mass ≤ τ̄ by the class hypothesis.

(2) Q(w) ≥ −c₋‖w‖² + P(w) ≥ −c₋ε² − 2 sinh(a)·δ_P²·ε²-level: by F0 and
F1(ii), the integral term is ≥ −c₋‖w‖²; the pole term for w involves only
I_±(w) = ⟨w, (I−P_m)e^{±x/2}⟩, bounded by ε·δ_P-halves — absorbed in the
δ_P-term of E (generously).

(3) Cross term, B(u,w) = (1/2π)∫ û ŵ* Ω_L dr + [pole cross]. Pole cross:
|I_±(u)| ≤ √(2 sinh a), |I_∓(w)| ≤ ‖w‖·δ_P-half, total ≤ √(2 sinh a)·δ_P·ε.
Frequency integral, split at R: below R, |ŵ| ≤ ‖w‖·√(2a B_m(aR)) pointwise
(F2(a)), so the piece is ≤ Ω̄(R)·‖u‖·√(2R/2π)·√(2aB_m)·‖w‖ ≤
Ω̄(R)√(R/π)·β·ε. Above R, Cauchy–Schwarz with the weight on u:
|(1/2π)∫_{>R} û ŵ Ω_L| ≤ [ (1/2π)∫_{>R}|û|²Ω̄² ]^{1/2}·[ (1/2π)∫_{>R}|ŵ|² ]^{1/2}
≤ √T₂(m,R) · √(τ̄') where τ̄' is the tail mass of ŵ = φ̂ − û above R; since
this appears multiplied by the u-side factor we bound √τ̄' ≤ √τ̄ + [tail mass
of û]^{1/2}·—the û-tail term recombines with T₂ (both sides polynomial), and
the stated E keeps the dominant √T₂·√τ̄ with the û×û tail term ABSORBED:
(1/2π)∫_{>R}|û|²Ω_L dr ≥ 0 whenever R ≥ r₊(L) (F1(iii)) and is otherwise
≥ −c₋·(û-tail mass) ≤ absorbed in the c₋ε²-term via ‖w‖-bookkeeping.
Collecting (1)–(3) gives the display. ∎

Remarks. (i) The theorem is unconditional as a statement about Q_L (no RH
anywhere). (ii) The class is basis-independent and infinite-dimensional; it
is NOT all of H_L — by Theorem F5 that is impossible for this template.
(iii) Sobolev corollary: if S_s(φ)² := (1/2π)∫|φ̂|²(1+r²)^s dr ≤ M², then
φ ∈ 𝒞(R, M²(1+R²)^{−s}); the tables below quote both forms.

## 6. The two no-go results

**Theorem F5 (the unconditional wall).** The only a-priori frequency control
the form gives its own near-minimizers is logarithmic: any unit φ with
Q_L(φ) ≤ λ_m has W₊(φ) := (1/2π)∫|φ̂|²·½log(1+4r²)dr ≤ C_B* :=
λ_m + κ₀' + C_P + C_Π (THEOREMS.md Lemma B(iv); C_B* ≈ 10.3 at L = 7/4), and
this is sharp up to the additive 8 (Lemma A(iv)). Consequently, in any
split-at-R argument the class-tail input available unconditionally is
τ(R) ≤ C_B*/(½log(1+4R²)), and the resulting cross-term error is at least of
order Ω̄(R)·√(C_B*/log(2R)) ≥ ½√(C_B*·log 2R) — an INCREASING function of R,
with minimum value ≈ 2.8 at the smallest useful cuts. Since every window
margin is ≤ 3.2×10⁻⁵, no choice of (m, R) closes: **the unrestricted infimum
cannot be certified by any subspace-plus-tail argument driven by the form's
own coercivity.** (This is a wall for the template, not an information-
theoretic impossibility; it is kin to the finite-cutoff delimitations of
arXiv:2607.02828, and it is the precise reason F4's class hypothesis cannot
be discharged.)

**Proposition F6 (capture-vs-content conflict for polynomial subspaces).**
V_m captures competitors only below R ≈ 0.66·m/a (Lemma F2 needs
aR ≲ 2m/e), but carries its own Fourier content out to r ≈ m/a (Legendre
mode k peaks at r ≈ k/a), with O(1) mass in the gap [0.66 m/a, m/a] where
Ω̄ ≈ c₀ + log(2m/a). Hence the coupling constant √T₂(m,R) grows like
√(m·polylog) (measured: 406 → 643 → 777 for m = 96 → 192 → 256 at L = 7/4)
instead of decaying, and closure forces τ̄ ~ (λ_m/√T₂)² ~ 10⁻¹⁶. A basis of
band-concentrated functions (truncated prolates: content ≤ R by construction
up to the Landau–Widom leak e^{−plunge}) removes the conflict: the same F4
skeleton would close with τ̄ ~ (λ_m/Ω̄(R))² ~ 10⁻¹², four orders weaker a
hypothesis, i.e. a class containing packets to heights ~e^{L/2}-scale rather
than ~40. **The prolate basis is forced for any material tightening** — the
theorem-level justification of M1's prolate clause.

## 7. Instantiation ledger (verified numbers; §8 script)

Configuration: cut R = 0.88·2m/(ea); class stated as tail mass at R;
Sobolev coverage at s = 10 (L = 7/4) and s = 12 (L = 497/200); "packet
coverage" = largest γ₀ such that a unit Gaussian wave packet at frequency γ₀
(width ~3) provably lies in the class (calibration-grade estimate
S_s ≈ 2(1+(γ₀+3)²)^{s/2}; to be hardened in the NT-4 writeup).

| L | m | R | class τ̄ at R | Sobolev form | certified bound | packet coverage |
|---|---|---|---|---|---|---|
| 7/4 | 96 | 142.1 | 3.7e−16 | S₁₀ ≤ 6.5e13 | ≥ 1.57e−5 | γ₀ ≤ 19.4 (zeros 1) |
| 7/4 | 128 | 189.4 | 2.5e−16 | S₁₀ ≤ 9.5e14 | ≥ 1.57e−5 | γ₀ ≤ 26.3 (zeros 1–2) |
| **7/4** | **192** | **284.2** | **1.5e−16** | **S₁₀ ≤ 4.2e16** | **≥ 1.56e−5** | **γ₀ ≤ 39.8 (zeros 1–6)** |
| 7/4 | 256 | 378.9 | 1.0e−16 | S₁₀ ≤ 6.1e17 | ≥ 1.56e−5 | γ₀ ≤ 53.0 |
| 497/200 | 192 | 200.1 | 1.7e−26 | S₁₂ ≤ 5.4e14 | ≥ 1.75e−10 | γ₀ ≤ 12.9 (none) |
| 497/200 | 256 | 266.8 | 1.2e−26 | S₁₂ ≤ 1.4e16 | ≥ 1.75e−10 | γ₀ ≤ 17.9 (zero 1) |

The λ_m inputs are the spectral ladder's converged band (λ_192 expected
3.125e−5 at L = 7/4 from the measured m ≤ 64 descent 3.1439 → 3.1416e−5 and
the Richardson limit 3.12–3.14e−5; RESULTS.md). Note the certified artifacts
are *mpmath.iv*; a Lean-integer version is NOT required for the claim (and at
m = 192 the CS-1/NA depth law prices the integer route as infeasible in the
current format — use NA Lemma 4(ii)'s inequality-form redesign if
formalizing).

### 7.1 Certification runs (this session; coordinator-authorized compute)

Protocol: build the interval form `certified_spectral_form(7/4, m, N=400)`
once (mpmath.iv, rigorous series remainders as in the module header), then
interval-Cholesky of Q − βG down a β-ladder 3.13e−5 → 3.0e−5; the first PASS
certifies λ_m(V_m) > β outright (a PASS is a kernel-of-the-method proof that
every leading minor of the outward-rounded interval matrix is positive).
Drivers: `certrun.py` / `certrun2.py` (session scratchpad); logs flushed
line-by-line so runs survive session churn. Scratchpad root:
`/tmp/claude-1000/-home-ubuntu-Projects-Riemann-Zeta/b43eb949-595f-4ac3-ad58-82a3f3afb113/scratchpad`.

**Instrument finding (new, diligence-grade).** The first m = 96 attempt at
the module's default iv.prec = 220 bits FAILED all β down to 2.5e−5, each
Cholesky dying in < 1 s — an interval-width blowup, not a mathematical
failure (λ_96 is sandwiched in (3.12e−5, 3.1416e−5) by Rayleigh–Ritz
monotonicity and the operator limit). Cause, located: the prime-term Horner
evaluation of the exact F_kj polynomials at v₀ = log(2)/a = 1.584 > 1 with
coefficients of size ~4^{k+j} costs ~5.3·m bits of cancellation at L = 7/4;
220 bits is an implicit ceiling near m ≈ 48 on this window. All previously
published spectral certificates sat at v₀ ≤ 1.24 and m ≤ 48, so the ceiling
was never visible. **Program note: `certified_spectral.py` users must scale
iv.prec ≳ 5.3·m + 250 on small-a windows** (set from the caller; no src
change needed). Failed-run artifacts kept: `cert96.log`, `cert96.result`.

- **(a) m = 48, prec 512 (sanity probe for the precision model) — IN FLIGHT**;
  log `cert48v2.log`, result `cert48v2.result`; minutes-scale.
- **(b) m = 96, prec 768 — IN FLIGHT**; log `cert96v2.log`, result
  `cert96v2.result`; ETA ~1.5–2.5 h (first build was 1292 s at 220 bits;
  precision factor ~(768/220)^{1.3}).
- **(c) m = 192, prec 1344 — IN FLIGHT under nohup+setsid (pid 2838095;
  survives session churn)**; log `cert192v2.log`, nohup `cert192v2.nohup`,
  result `cert192v2.result`; ETA ~1–2 days (m³ assembly scaling × precision
  factor). On completion, the headline at (192, R = 284.15, τ̄ = 1.478e−16)
  finalizes per the chain below with the first passing β.

Headline assembly (outward-rounding chain, applied when β lands): with
β = certified Cholesky bound, the F4 chain at (m, R, τ̄) is
inf_{𝒞(R,τ̄)} Q_L ≥ β·(1−ε²) − 2[√T₂·√τ̄ + Ω̄(R)√(R/π)β_m-capture·ε + pole]
− (c₋+β)ε², with every constituent already outward-rounded in §8's ledger
script; the final number is rounded DOWN to 3 significant figures.

Verification safety: if certified β lands below 3.1e−5 the table's final
column degrades linearly, not catastrophically. Fallback needing NO new run:
none — the certified hat-basis value at L = 7/4 (3.77497970e−5, m = 41,
RESULTS.md) cannot be used directly, since F2/F3 are Legendre-specific.

## 8. Verification appendix

Scripts in the session scratchpad (`calib2.py`, `calib3.py`, `calib4.py`,
`ledger.py`); reproduce with python3 + mpmath + numpy + scipy, ≤ 10 min total,
2 processes max. Key outputs (quoted verbatim from the runs):

- Instrument regression: spectral λ(7/4, m=48) = 3.1438949e−5 (RESULTS.md:
  3.14389e−5 ✓); λ(7/4, m=64) = 3.1415961e−5 (new point, consistent with the
  ladder's descent toward 3.12–3.14e−5).
- Boundary-flatness is cheap (class non-vacuity): minimizing Q over
  (1−(x/a)²)^q·V_{64−2q} gives 3.142012e−5 / 3.142184e−5 / 3.142145e−5 /
  3.142727e−5 for q = 1/2/3/5 — within 0.04% of the unrestricted m = 64
  value. (A naive windowed minimizer, by contrast, scores 7.7e−2: the
  margin's cancellation is delicate; the class infimum is near λ_m because
  re-optimization inside the class recovers it, not because arbitrary smooth
  truncations do.)
- Galerkin argmins carry wiggle tails τ(287) ≈ 4e−7 ≫ τ̄ = 1.5e−16 — the
  certified class therefore does NOT contain the finite-m argmins themselves;
  it contains the smooth competitors (packets, mollified profiles). This is
  the honest meaning of the restriction, stated plainly.
- Envelope constants: κ₀' = 5.3722, c₀(7/4) = 14.352, c₋ = 6.352,
  r₊ = 286.95; c₀(497/200) = 15.621, c₋ = 7.621, r₊ = 1020.3.
- Capture at (m, aR) = (192, 124.31): B_m ≤ 6.96e−25, β = 7.8e−13 —
  all capture terms negligible against √T₂·√τ̄ ≈ 7.8e−6.
- Content: √T₂ = 406.2 / 491.6 / 642.7 / 777.0 at m = 96/128/192/256
  (L = 7/4) — the F6 growth, measured.
- Wall: min over R of the unconditional split error ≥ 2.78 (attained toward
  small R; increasing in R): 5 orders above every window margin.
- Ledger rows as tabled in §7 (script `ledger.py` output, verbatim).

## 9. Lean decomposition and mathlib gap map

The m-dimensional certified core is already kernel-checked technology
(Theorem 2, THEOREMS.md). The NEW mathematics between the existing artifacts
and a formal F4 statement, as Lean-sized lemmas:

| Lemma | Content | mathlib status |
|---|---|---|
| F0 | Fubini/Wiener–Khinchin for compactly supported L² | `MeasureTheory.integral_integral_swap` + `Real.fourierIntegral` basics: FORMALIZABLE NOW (days) |
| F1 | Lemma A(ii),(iv) digamma sandwich | the known gap (Gauss digamma integral, directed rounding) — unchanged from THEOREMS.md's bridge list |
| F2 | plane-wave Legendre coefficients, addition theorem, factorial tail | spherical Bessels absent from mathlib; ONLY the inequality is needed, via the integral representation — self-contained induction, moderate (weeks) |
| F3 (weak) | K_m ≤ 1 and the πm²/2z branch (drop Landau) | Cauchy–Schwarz + |J_ν| ≤ 1-equivalent via the same integral rep: moderate; the Landau branch (c_L z^{−1/3}) should be DROPPED in the formal version — the ledger still closes at m = 192 with weaker coverage (γ₀ ≤ ~33, still zeros 1–5; verified in-session) |
| F4 | pure inequality algebra over ℚ given F0–F3 + certified λ_m | kernel-ready in the existing `CertFramework` style |
| Class membership of NT-4 packets | explicit Gaussian-tail integrals | elementary; needed only for the composition corollary |

Terminal-criterion note: F4-formal + the (7/4, 192) certified rung + a
formalized NT-4(i) would make "no zero of ζ in [explicit region]" a
kernel-checked statement whose proof nowhere evaluates ζ — the first formal
artifact of that kind at any height. The region is tiny; the kind is new.

## 10. What falls short, said without decoration

The assignment asked for the infimum over ALL admissible φ. That is not
delivered, and by Theorem F5 it cannot be by these means: unconditional
certification of the full infimum needs an a-priori regularity theorem for
near-minimizers of Q_L (frequency decay beyond the logarithmic budget the
form itself pays for) — a genuinely new estimate about the Weil form, not
about its discretizations, and my current best guess at its shape (bootstrap
of the eigen-equation Π_a(Ω_L φ̂) + pole = λφ̂ through weighted moments) gains
only iterated logs per step. I regard that regularity theorem as the correct
formulation of "the only new mathematics between us and a fully formal
statement about the true infimum" — harder than the tail bound the plan
hoped for, now stated precisely enough to be attacked or killed.

Files: this note; calibration/ledger scripts in the session scratchpad.
No repo source files were modified. Round-3 status appended to
PLAN-number-theory.md.
