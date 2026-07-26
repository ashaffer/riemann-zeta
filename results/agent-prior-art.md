# Prior-art and reference sweep

**Agent report — research only.** Executed 2026-07-26 (web search + fetches only; no contact,
no posting, no submission). Scope: audit the four "believed new" items of this program
(PROGRAM.md §2.14–2.18, THEOREMS.md, ENVELOPE.md) against the frontier corpus and the
adjacent mathematics, and assemble the Landau–Widom reference package for the parallel
theory effort. Quotes below were extracted either (a) locally from downloaded arXiv
HTML/PDF (exact, marked **[local extract]**) or (b) via fetch-summarization of a page
(marked **[via fetch]**). Every negative claim carries its search log (§8).

---

## 0. Executive summary — the four claims

| # | Program claim | Verdict | One-line reason |
|---|---|---|---|
| 1 | **Envelope law** ln λ_min ≈ 10.2 − 1.755·e^{L/2}(L/2+4), universal over real Dirichlet characters in the rescaled Nyquist height | **Adjacent — partially anticipated** | Super-exponential decay of the truncated-form ground eigenvalue, with an explicit Fuchs-prolate comparator formula and a graph-level "envelope" comparison, is already in Connes (arXiv:2602.04022 §6.4), with numerics in CC zeta-cycles (2106.01715: 2.389×10⁻⁴⁸ at λ²=11) and Groskin (2605.20224: λ_min to 10⁻³³⁴, finite-N fit, extrapolation onto Connes's prediction). **Surviving deltas:** the support-normalized three-constant law with the (L/2+4) log-correction and out-of-sample tests; the *family universality* across Dirichlet characters (nothing in the corpus treats families); the certified two-sided enclosures; the smooth-staircase/Poisson rigidity experiment. Also a substantive *tension* to resolve (§7.2). |
| 2 | **Glide Theorem** (margin monotone + continuous through prime-power thresholds, explicit modulus) | **Continuity: killed as new. Explicit modulus: survives.** | Continuity of the lowest eigenvalue λ_a in the support half-length a is Theorem 1.3 of Suzuki, arXiv:2606.09096 (submitted 8 June 2026 — seven weeks before THEOREMS.md), and was *asserted* for the even/odd infima by Bombieri (2000, Thm 5; 2003, Thm 4.4) with "details of the proof not fully provided". No source states a *modulus of continuity* (Suzuki's proof is qualitative semicontinuity; his paper contains zero occurrences of "modulus"), and none states the monotonicity clause explicitly (it is an inclusion triviality). Recommend reframing Theorem 1 as *effective/quantitative* continuity, citing Bombieri and Suzuki. |
| 3 | **Kernel-checked (Lean) positivity window** | **Supported — no prior art found in-domain** | No Lean/Coq/Isabelle work touches Weil positivity, the explicit formula, or verified zeta-zero numerics (mathlib: zeta/L-functions/FE/RH-statement only; PNT+ scope: PNT & PNT-APs; Isabelle AFP: zeta FE, PNT; no verified zero computations anywhere found). Caveat for honest claiming: the *generic technique* — kernel-checked rational PSD/SOS certificates with a posteriori rounding — is standard art (Harrison 2007; Martin-Dorel–Roux JAR 2016 / ValidSDP; Magron et al.; a May-2026 Lean SOS pipeline). Novelty is "first in the Weil-positivity domain," not "first verified PSD certificate." |
| 4 | **Digamma sandwich** ψ(¼)+½log(1+4r²) ≤ Re ψ(¼+ir/2) ≤ same + 8 | **Folklore-level; no recorded statement found** | Three targeted searches found only real-argument digamma inequality literature (Alzer/Qi/Gautschi school) and generic asymptotics. The two-sided vertical-line sandwich as stated was not located anywhere; it is, however, derivable in spirit from DLMF §5.11-type bounds (ψ(z) = ln z − 1/(2z) + O(1/z²), |arg z| < π). Keep the "worth recording / novelty modest" framing of THEOREMS.md. |

Bonus finding (Task 6): the Chowla-hunt record D = 14693 lies **five orders of magnitude inside**
already-computed territory — Alderson–Rubinstein computed L(½, χ_d) for −5×10¹⁰ < d < 1.3×10¹⁰
(Exp. Math. 2012), and Omar (ANTS-VIII 2008) verified L(½,χ) ≠ 0 for all real characters of
modulus < 10¹⁰. No published "smallest central value" *table* was found, but the values existed
in bulk by 2012. "Record of our scan" is the correct and only defensible framing.

---

## 1. Task 1 — margin continuity and margin decay in the frontier corpus

### 1.1 What each paper says (abstract-level, with the load-bearing quotes)

**Connes–Consani, "Weil positivity and Trace formula, the archimedean place", Selecta Math. 27 (2021), no. 4, paper 77; arXiv:2006.13771.**
Abstract **[via fetch]**: "We provide a potential conceptual reason for the positivity of the Weil
functional using the Hilbert space framework of the semi-local trace formula… We explore in great
details the simplest case of the single archimedean place. The root of the positivity is the trace
of the scaling action compressed onto the orthogonal complement of the range of the cutoff
projections associated to the cutoff in phase space, for cutoff parameter equal to 1. We express
the difference between the Weil distribution and the Sonin trace… in terms of prolate spheroidal
wave functions, and use as a key device the theory of hermitian Toeplitz matrices…"
Full-text check **[via fetch]**: positivity proven for support (1/2, 2) (equivalently [2^{−1/2}, 2^{1/2}]
in the main theorem); a constant "13 < c < 17" bounding the Weil-functional/Sonin-trace gap; **no**
statement of margin-vs-support continuity/monotonicity; **no** Dirichlet-character version.
*Verdict: adjacent (frame of the whole program); does not anticipate claims 1–2.*

**Connes–Consani, "Spectral triples and ζ-cycles", Enseign. Math. 69 (2023) 93–148; arXiv:2106.01715.**
Abstract **[via fetch]**: "We exhibit very small eigenvalues of the quadratic form associated to the
Weil explicit formulas restricted to test functions whose support is within a fixed interval with
upper bound S. We show both numerically and conceptually that the associated eigenvectors are
obtained by a simple arithmetic operation of finite sum using prolate spheroidal wave functions
associated to the scale S…"
Full-text findings **[via fetch]**: "For instance, we find that when λ² = 11 the smallest positive
eigenvalue is 2.389×10⁻⁴⁸." And a continuity statement *for their perturbed operator*: "For a fixed
value of k the positive non-zero eigenvalues λ_n(D(λ,k)) arranged in increasing order, vary
continuously with λ."
*Verdict: adjacent-strong for claim 1 (deep small-eigenvalue numerics, prolate eigenvector
construction — 2021); adjacent for claim 2 (continuity is asserted for the perturbed Dirac operator
D(λ,k), not for the Weil-form margin itself). Note: their λ²=11 point sits essentially ON our
envelope — see §7.1.*

**Connes–Consani–Moscovici, "Zeta zeros and prolate wave operators", arXiv:2310.18423 (2023).**
Abstract **[via fetch]**: semilocal prolate operator; "We prove the stability of the semilocal Sonin
space under the increase of the finite set of places…" No margin-vs-support statements, no P(n)
statement in the abstract. *Verdict: irrelevant to claims 1–2 directly; see citation-hygiene flag §7.3.*

**Connes–Consani–Moscovici, "Zeta Spectral Triples", arXiv:2511.22755 (27 Nov 2025).**
Abstract **[local extract of key lines]**: "Our approach constructs self-adjoint operators obtained as
rank-one perturbations of the spectral triple associated with the scaling operator on the interval
[λ⁻¹, λ]. The construction only involves the Euler products over the primes p ≤ x = λ² …
Numerical experiments show that the spectra of the operators converge towards the zeros of
ζ(1/2+is) as the parameters N, λ → ∞."
Body **[local extract]**: Proposition 3.4: "the lower bound of QW_λ is the limit, when N → ∞, of the
smallest eigenvalue of the restriction of QW_λ to the linear span E_N…" Theorem 5.10 (regularized
determinant of the rank-one-perturbed operator = −i λ^{−iz} ξ̂(z)); §8 "The missing steps": "one
must prove that its smallest eigenvalue—whose existence is ensured by Theorem 3.6—is simple and
that its corresponding eigenvector ξ_λ is even." Also: "(2) The extremely small numbers ε_λ that
occur as eigenvalue[s]…"
*Verdict: adjacent (the operator A_λ with QW_λ(f,f) = ⟨A_λ f|f⟩ is exactly our λ(L) object in
multiplicative coordinates); contains **no** continuity/monotonicity-in-λ claims and no decay law.*

**Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time", arXiv:2602.04022 (3 Feb 2026).**
The single most important prior-art item for claim 1. §6.3–6.4 **[local extract, exact]**:

> "Let λ>1, and QW_λ be the restriction of the Weil quadratic form to test functions whose support
> is within the interval [λ⁻¹,λ]. By the result of André Weil discussed in §4.1, the positivity of
> QW_λ for all λ>1 is equivalent to RH. This positivity can be proved for small values of λ (see
> [111],[24]). There is (see [25,31]) for each λ>1 a canonical lower bounded, unbounded selfadjoint
> operator A_λ with compact resolvent, in the Hilbert space L²([λ⁻¹,λ],du/u) such that
> QW_λ(f,f) = ⟨A_λ f | f⟩ (19).
> The numerical computation of the smallest eigenvalue ε(λ) of A_λ, done in [25], shows that ε(λ)
> tends exponentially fast to 0 as a function of μ = λ². In fact a careful analysis reveals a
> striking similarity (Figure 1) between the behavior of ε(λ) and of the angular function 1−χ₂(λ).
> In terms of the length L = 2 log λ of the support [λ⁻¹,λ] of the test functions for QW_λ, the
> convergence to 0 of the minuscule quantities like 1−χ₂ is exponential of exponential
> [footnote 19: see [47], Theorem 1. Note that χ_k(λ)² = λ_{2k}(a) with a = √(2π)λ in the notations
> of this theorem]:
>   **1−χ₂ ∼ (2¹⁴/3)·√2·π⁵·e^{−4π e^L + (9/2)L}.**
> Figure 1: Graphs of log(ε(√x)) and log(1−χ₂(√x)) as functions of x."

Here [47] = W. H. J. Fuchs, JMAA 9 (1964) 317–330; [111] = H. Yoshida (1992); [24] = CC Selecta
2021; [25] = CC zeta-cycles; [31] = "A. Connes, C. Consani, H. Moscovici, *Riemann Zeros via Weil
Forms: From Prolate Functions to Cohomology*, in preparation" **[local extract of bibliography]**.
*Verdict for claim 1: **partially kills.** The statements "the margins decay exponential-of-exponentially
in the support" and "the comparator is a prolate (Fuchs) eigenvalue asymptotic with explicit
constants" are in print (Feb 2026), including a figure comparing the two log-curves — i.e., an
envelope comparison. What is NOT there: a fitted quantitative law for ε(λ) itself, any threshold/
glide analysis, any family version, any certification. Note Connes's comparator is exactly Fuchs's
theorem at n=4 — verified numerically in §7.1 — and is pure-exponential in e^L, whereas our
measured law carries the extra (L/2+4) factor; see §7.2 for the tension.*

**Connes–van Suijlekom, "Quadratic Forms, Real Zeros and Echoes of the Spectral Action", Commun. Math. Phys. (2025)** (cited as [32] in 2602.04022 and as the truncation source in Groskin). Not fetched in full; role: source of the CvS truncated Weil form (prime cutoff c) and the Carathéodory–Fejér self-adjointness input used by 2511.22755. *Verdict: adjacent (defines the other truncation).*

**Suzuki, "Aspects of the screw function corresponding to the Riemann zeta function", J. Lond. Math. Soc. 108 (2023) 1448–1487; arXiv:2206.03682.**
Abstract **[via fetch]**: "We introduce a screw function corresponding to the Riemann zeta-function…
Typical results are several equivalent conditions for the Riemann hypothesis in terms of the screw
function. One of them can be considered an analog of so-called Weil's positivity or Li's
criterion. In addition, we prove a few partial but unconditional results for such equivalents."
No support-parameter statements in the abstract. *Verdict: adjacent.*

**Suzuki, "The screw line of the Riemann zeta-function and its applications", arXiv:2209.04658** (published as/related to "On the Hilbert space derived from the Weil distribution", Canad. J. Math., FirstView — cited as [14] in 2606.09096).
Abstract **[via fetch]**: "…derive three necessary and sufficient conditions for the Riemann
hypothesis as applications. One of them explains the non-negativity of the Weil distribution by
means of the norm." *Verdict: adjacent.*

**Suzuki, "Weil's quadratic form via the screw function", arXiv:2606.09096 (8 June 2026).**
Abstract **[via fetch]**: "We establish a unified framework for understanding the results on the Weil
quadratic form obtained by Yoshida (1992), Bombieri (2001, 2003), Connes–Consani (2023), and
Connes–Consani–Moscovici (2025+) from the perspective of the screw function… we formulate a
conjecture stating that a self-adjoint operator whose eigenvalues are the imaginary parts of the
nontrivial zeros … can be obtained as the limit, as a → ∞, of self-adjoint operators arising from
nonlocal realizations of the first-order differential operator on the finite interval [−a,a]."
The paper that decides claim 2. Key passages **[local extract, exact]**:

> "**Theorem 1.3.** The lowest eigenvalue λ_a is continuous in a."

> "Indeed, in [1, Theorem 5] (and [2, Theorem 4.4]), analogues of the infimum in (1.7) are
> considered on the spaces of even and odd functions, and their continuity with respect to a is
> asserted, but the details of the proof are not fully provided there. In contrast, by exploiting
> the asymptotic expansion (2.2) of the screw function near the origin, which involves a
> logarithmic singularity, one can prove the continuity of the lowest eigenvalue λ_a without
> imposing any parity restriction."

> "Since the continuity of λ_a can be established without assuming RH, Theorem 1.3 immediately
> yields, as a corollary, another proof of Yoshida's result [17] that RH is equivalent to the
> nondegeneracy of Q_W^a for every a>0. Indeed, the failure of RH is equivalent to the existence of
> some a>0 for which λ_a [< 0] … it follows that if RH is false, then Q_W^a must be degenerate for
> some value of a by continuity of λ_a."

> "**Theorem 1.4.** For sufficiently small a>0, the lowest eigenvalue λ_a is positive, simple, and
> satisfies λ_a = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a) as a → 0+, for some constant μ₁>0.
> Furthermore, the corresponding eigenfunction is even."

Proof method (his §4, **[local extract]**): scaling transformation of the Rayleigh quotient to the
fixed interval (−1,1) (w(t) = v(at) — the same dilation trick as THEOREMS.md Theorem 1 Step 2),
compact embedding of a log-Sobolev-type space H^log(−1,1), then upper semicontinuity
(limsup_{a→a₀} λ_a ≤ λ_{a₀}) via C_c^∞ approximation and lower semicontinuity via the compact
embedding. **The proof is qualitative: the paper contains no modulus of continuity ("modulus": 0
occurrences; "explicit constant": 0 occurrences) and no monotonicity statement ("monoton" occurs
once, for a cutoff function).** His bibliography **[local extract]**:
[1] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers. I",
Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 11 (2000), no. 3,
183–233 (2001). [2] E. Bombieri, "A variational approach to the explicit formula", Comm. Pure
Appl. Math. 56 (2003), no. 8, 1151–1164. [17] H. Yoshida, "On Hermitian forms attached to zeta
functions", Zeta functions in geometry (Tokyo, 1990), 281–325, Adv. Stud. Pure Math. 21,
Kinokuniya, Tokyo, 1992.
*Verdict for claim 2: **kills the continuity statement as new** (in print 8 June 2026, predating the
July 25/26 Glide Theorem; asserted by Bombieri in 2000/2003; windowed nondegeneracy criterion due
to Yoshida 1992). **Survives:** the explicit modulus C·(log 1/h)^{−1/2}, the elementary
self-contained engine (Lemma A log-sandwich instead of compact embeddings), and the explicitly
stated monotonicity clause. Suzuki's Theorem 1.4 is also adjacent to claim 1 at the *small-a* end:
an exact λ_a → ∞ asymptotic (log(1/a) law) — the opposite end of the envelope.*

**Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I", Rend. Lincei (9) Mat. Appl. 11 (2000) 183–233.**
Abstract **[via fetch of EUDML record]**: "This Memoir studies Weil's well-known Explicit Formula in
the theory of prime numbers and its associated quadratic functional, which is positive semidefinite
if and only if the Riemann Hypothesis is true. We prove that this quadratic functional attains its
minimum in the unit ball of the L²-space of functions with support in a given interval [−t,t] …
if the Riemann Hypothesis is false but only with finitely many non-trivial zeros off the critical
line we show that the number of negative eigenvalues is precisely one-half of the number of zeros
failing to satisfy the Riemann Hypothesis, provided the truncation is big enough."
*Verdict: the original windowed variational study (2000). Continuity-in-t asserted inside (per
Suzuki's [1, Theorem 5] citation) with incomplete details. Also directly relevant to Track D:
negative-eigenvalue counting under RH-failure.*

**Groskin, "High-Precision Approximation of Riemann Zeros via the Truncated Weil Form", arXiv:2605.20224 (May 2026, v2).**
Abstract **[via fetch, quoted]**: "The Connes-van Suijlekom truncated Weil quadratic form, indexed by
a cutoff c (controlling the primes p≤c in the operator), has a ground state whose Fourier-Mellin
zeros provably lie on the critical line; whether they converge to the Riemann zeros as c→∞ is open
(Connes 2026; Connes-Consani-Moscovici 2025). We present, to our knowledge, the first public
implementation of the CvS Galerkin matrix at sixteen cutoffs (c=13 through 67, plus c=100). Across
c=13–67 at N=100, the first-zero error |γ₁−γ₁^Riemann| shrinks monotonically from ∼2×10⁻⁵⁵ to
∼1.5×10⁻¹⁶⁸ … The smallest-positive even-sector eigenvalue reaches ∼10⁻³³⁴ at c=100, N=250
(275-OOM span), whose eigenvector recovers γ₁,…,γ₁₀ to 307-329 matching digits. … Aitken-Δ² on the
c=100 N-sweep gives log₁₀|λ_∞^(even)|≈−536.76 and −533.70, approaching the Connes 2026 Section 6.4
heuristic continuum prediction (≈−530.38) monotonically in N."
Body **[via fetch, quoted]**: "The fit |log₁₀λ_min|≈13.24·c^0.634 on c≤67 at N=100 is shown to be a
finite-N rate"; "log₁₀(1−χ₂(c=100))≈6.37−545.75+9.00≈−530.38"; "1−χ₂(λ)∼(2¹⁴/3)√2·π⁵·e^(−4πe^L+9L/2)
where L = log c"; "log₁₀|λ_min| decreases monotonically with N at fixed c=100".
*Verdict for claim 1: **adjacent-strong.** Systematic smallest-eigenvalue decay measurements across
sixteen cutoffs with a fitted (finite-N) law and extrapolation onto Connes's explicit continuum
prediction — in the CvS prime-cutoff normalization. Our support-normalized law, threshold-glide
measurements, family universality, and interval certification are not there. (Keyhole/zero-recovery
novelty was already conceded to this paper in PROGRAM.md §2.14(vi).)*

**Groskin, "A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form", arXiv:2607.02828 (2 July 2026).**
Abstract **[via fetch, quoted]**: "…We prove two exact finite theorems about this truncation. First,
every real even Galerkin coefficient vector v determines, in closed form, a band-limited
Guinand-Weil test function g_v whose zero sum over the nontrivial zeros of zeta equals the
quadratic value ⟨v, Q v⟩ exactly… Second, beyond the Galerkin band the omitted archimedean tail is
a totally positive Cauchy-Stieltjes increment." Plus "a two-sided certification rule with an
explicit budget B_T ~ (2N+1)ρ log(T)/(π²T)".
*Verdict: adjacent to Track A certification (finite-cutoff certification budget); no continuity/
monotonicity or envelope statements ("does not address continuity/monotonicity of eigenvalues or
general decay envelopes" per full-text check). PROGRAM.md §1's description of 2607.02828 is
accurate.*

### 1.2 Continuity/monotonicity prior-art bottom line (claim 2)

- Continuity of the windowed Weil-form minimum in the support parameter: **asserted** Bombieri 2000
  (Thm 5) & 2003 (Thm 4.4) for even/odd infima ("details … not fully provided" — Suzuki's words);
  **proved** Suzuki arXiv:2606.09096 Thm 1.3 (June 2026), qualitative.
- Continuity of eigenvalues of the *perturbed Dirac operator* in λ: asserted in CC zeta-cycles.
- **No source found stating** (i) an explicit modulus of continuity, (ii) monotonicity of λ in the
  support, or (iii) any threshold-crossing ("glide") analysis at prime powers.
- The Glide Theorem's honesty note ("experts may regard it as folklore-provable") was prescient but
  understated: it is not merely folklore-provable, it is proven in the June 2026 literature.

### 1.3 Decay-law prior-art bottom line (claim 1)

The chain CC-zeta-cycles (2021 numerics) → Connes 2602.04022 §6.4 (explicit Fuchs comparator,
"exponential of exponential", Figure-1 envelope comparison) → Groskin 2605.20224 (16-cutoff decay
data + extrapolation onto the comparator) constitutes real prior art for "the margins of the
truncated Weil form follow a smooth super-exponential decay law governed by prolate asymptotics."
The program's ENVELOPE.md question "whether b ≈ 1.755 and the +4.0 offset are derivable from
Landau–Widom/Sonin asymptotics" has, in the frontier's own normalization, *already been answered
affirmatively at the heuristic level by Connes* (his §6.4 comparator IS a prolate asymptotic — see
§7.1). ENVELOPE.md and the cover-email draft should cite 2602.04022 §6.4 and 2605.20224 explicitly
and position the note as: support-normalized law + log-correction + family universality +
threshold glide + certified enclosures.

### 1.4 Family (Dirichlet) universality — absence documented

No paper found treating truncated Weil-form margins for Dirichlet L-functions numerically or
theoretically. CC Selecta 2021 is archimedean-ζ only ("No L-functions or Dirichlet character cases
are mentioned" — full-text check); 2511.22755, 2602.04022, both Groskin papers, and all three
Suzuki papers are ζ-only (Suzuki 2606.09096 full text: 0 occurrences of "conductor"; "Dirichlet"
occurs only as "Dirichlet form/boundary"). Searches run: §8, queries Q10–Q11. **The family
universality claim (one decay constant in T*_χ = (2π/q)e^{L/2}) stands as unanticipated.**

---

## 2. Task 2 — exponential systems at the zeta ordinates

**Direct hits: none.** No literature was found computing or bounding lower frame bounds for the
exponential system {e^{iγx}} at the ordinates of zeta zeros on any interval. Nearest items:

1. **A. Bondarenko, D. Radchenko, K. Seip, "Fourier interpolation with zeros of zeta and
   L-functions", Constr. Approx. 57 (2023) 405–461; arXiv:2005.02996.** Constructs Fourier
   interpolation bases whose interpolation nodes are the nontrivial zeros; "a duality principle for
   Fourier interpolation bases in terms of certain kernels of general Dirichlet series with variable
   coefficients … admit meromorphic continuation … and satisfy a functional equation" [via fetch].
   *Adjacent: uniqueness/interpolation at the zeros (dual side of sampling/frames), no frame bounds.*
2. **J. Ortega-Cerdà, K. Seip, "Fourier frames", Ann. of Math. (2) 155 (2002) 789–806.**
   Characterization of sampling sequences/Fourier frames for Paley–Wiener space (completing
   Beurling's density theory). *Adjacent: qualitative frame existence at supercritical lower
   Beurling density — exactly the "classical" fact recorded in PROGRAM.md §2.14(v); no rates.*
3. **H. J. Landau**, "Necessary density conditions for sampling and interpolation of certain entire
   functions", Acta Math. 117 (1967); **A. Beurling**, collected works (balayage/sampling). The
   density-⇒-frame machinery behind "each fixed-L margin is strictly positive under RH". *Supports;
   qualitative only.*
4. **A. M. Lindner, "On lower bounds of exponential frames", J. Fourier Anal. Appl. (≈1999)**
   (found via Springer BF01261608): explicit lower frame bounds for exponential systems in
   Avdonin-type and Duffin–Schaeffer-type settings. *Adjacent: quantitative lower frame bounds, but
   for near-uniform (bounded-density) sequences, not growing-density ones.*
5. **M. Bownik, J. T. van Velthoven, "On exponential frames near the critical density",
   arXiv:2411.19562 (2024).** Abstract **[via fetch, exact]**: "Given a relatively compact set
   Ω ⊆ ℝ of Lebesgue measure |Ω| and ε>0, we show the existence of a set Λ ⊆ ℝ of uniform density
   D(Λ) ≤ (1+ε)|Ω| such that the exponential system {exp(2πiλ·)1_Ω : λ∈Λ} is a frame for L²(Ω)
   with frame bounds A|Ω|, B|Ω| for constants A,B only depending on ε." *Adjacent: quantitative
   frame bounds at (1+ε)-supercritical density — but for *constructed* Λ, not for a given
   arithmetic sequence.*
6. **Borichev–Gröchenig–Lyubarskii-type results on Gabor frame constants near critical density**
   (found: "Frame Constants of Gabor Frames near the Critical Density"): lower frame bound
   degradation rates as density → critical, in the Gabor setting. *Adjacent.*
7. **The quantitative Nyman–Beurling literature — the classic precedent for a "margin decay law
   with a zero-determined constant" in a windowed RH criterion.** From Burnol's paper
   **[local extract from arXiv:math/0103058 PDF, exact]**:
   > "**Theorem 1.2 (Báez-Duarte, Balazard, Landreau and Saias [2])** Let us write D(λ) for the
   > Hilbert-space distance inf_{f∈B_λ} ‖χ−f‖. We have
   > liminf_{λ→0} D(λ)·√(log(1/λ)) ≥ √( Σ_ρ 1/|ρ|² )"
   > (zeros "counted only once independently of their multiplicities")
   > "**Theorem 1.3** [Burnol] We have: liminf_{λ→0} D(λ)·√(log(1/λ)) ≥ √( Σ_ρ m_ρ²/|ρ|² )
   > … the zeros are counted according to the square of their multiplicities. … The following
   > 'toy-model' gives us reasons to expect that the lower bound in fact gives the exact order of
   > decrease of D(λ)."
   Citations: L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias, "Notes sur la fonction ζ de
   Riemann, 3", Adv. Math. 149 (2000) 130–144; J.-F. Burnol, "A lower bound in an approximation
   problem involving the zeros of the Riemann zeta function", Adv. Math. 170 (2002) 56–70
   (arXiv:math/0103058). *Adjacent-supportive: establishes the genre "windowed-criterion margin
   decays with an explicit law whose constant is a sum over zeros" — useful precedent to cite when
   claiming the envelope law's genre is meaningful.*

Also noted: the superresolution/Vandermonde literature (§3.3) is the modern quantitative theory of
λ_min of exponential Gram matrices at supercritical density on an interval — the finite-dimensional
shadow of λ(L).

**Non-finding statement.** Searches Q12–Q16 (§8) found no work on frames/Riesz bases/sampling with
frequencies at zeta ordinates, no "logarithmic density" frame-bound computations, and no lower
frame bounds for growing-density sequences on fixed intervals beyond items 4–6 above. The
identification "λ_min(L) = lower frame bound of the exponential system at the zero ordinates" as a
*measured* object appears to be this program's own framing (PROGRAM.md §2.14(v)); Connes 2602.04022
works with the equivalent operator A_λ but does not use frame language.

---

## 3. Task 3 — Landau–Widom asymptotics: exact statements (theory feed)

Notation: Q_c = sinc-kernel (time-and-band-limiting) operator on [−1,1] with bandwidth c
(kernel sin(c(x−y))/(π(x−y))); eigenvalues 1 > λ₀(c) > λ₁(c) > … > 0; critical index n_c = 2c/π.
All formulas below are **[local extract, exact]** from Bonami–Jaming–Karoui, arXiv:1804.01257
("Non-Asymptotic behaviour of the spectrum of the Sinc Kernel Operator and Related Applications"),
§2.2, with their reference numbers resolved from the bibliography.

**Three regions** (BJK, intro): "The slow evolution region, where for n_c−n ≳ log(c), the change in
the λ_n(c)'s is very slow… The fast decay region, where for n−n_c ≳ log(c) we have λ_n(c) → 0 at a
super-exponential speed. The plunge region … |n−n_c| ≲ log(c). Thus the width of this region is
≈ log(c) for c large."

**(LW) Landau–Widom counting formula.** [H. J. Landau, H. Widom, "Eigenvalue Distribution of Time
and Frequency Limiting", J. Math. Anal. Appl. 77 (1980) 469–481.] For ε ∈ (0,1/2),
Λ_ε = {k : λ_k(c) ≥ ε}; then for c ≫ 1:
> **|Λ_ε| = (2c/π) + (1/π²)·log((1−ε)/ε)·log(c) + o(log c).**  (BJK eq. 2.8)
Equivalently: inside the plunge the eigenvalues fall through (ε, 1−ε) along the profile
λ_{⌊2c/π + (b/π²) log c⌋} ≈ 1/(1+e^b) (invert the counting formula; the classical plunge-profile
reading, cf. Slepian 1965).

**(F) Fuchs's theorem** (the low-end/slow-region asymptotic; the source of Connes's §6.4 comparator).
[W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in the theory of band-limited
signals", J. Math. Anal. Appl. 9 (1964) 317–330, Theorem 1.] For fixed n ≥ 0, c ≫ 1:
> **1 − λ_n(c) ∼ 4√π · (8ⁿ/n!) · c^{n+1/2} · e^{−2c}.**  (BJK eq. 2.9)

**(W) Widom's fixed-c, large-n asymptotic** (the fast-decay region; the n·log n regime).
[H. Widom, "Asymptotic behavior of the eigenvalues of certain integral equations. II", Arch.
Rational Mech. Anal. 17 (1964) 215–229.]
> **λ_n(c) ∼ ( e·c / (4(n+½)) )^{2n+1} =: λ_n^W(c).**  (BJK eq. 2.7)
i.e. ln λ_n ≈ −(2n+1)·ln(4(n+½)/(ec)) — factorial/(n ln n)-type decay once n ≫ c.

**(BK) Bonami–Karoui explicit plunge-to-decay formula.** [A. Bonami, A. Karoui, "Spectral Decay of
Time and Frequency Limiting Operator", Appl. Comput. Harmon. Anal. 42 (2017) 1–20.] With E the
complete elliptic integral of the second kind and Φ the inverse of Ψ: t ↦ t/E(t), valid for
πn/2 − c larger than some multiple of ln n:
> **λ_n(c) ∼ ½ exp( −π²(n+½)/2 · ∫_{Φ(2c/(π(n+½)))}^{1} dt/(t·E(t)²) ).**  (BJK eq. 2.10)
And (their Corollary 3) there exist δ₁ ≥ 1, δ₂, δ₃ ≥ 0 such that for n ≥ 3, c ≤ πn/2:
> **A(n,c)⁻¹·(ec/(2(2n+1)))^{2n+1} ≤ λ_n(c) ≤ A(n,c)·(ec/(2(2n+1)))^{2n+1},
> A(n,c) = δ₁·n^{δ₂}·(c/(c+1))^{−δ₃}·e^{(π²/4)·c²/n}.**  (BJK eq. 2.11)

**(O) Osipov's nonasymptotic counting bound.** [A. Osipov, "Certain upper bounds on the eigenvalues
associated with prolate spheroidal wave functions", Appl. Comput. Harmon. Anal. 35 (2013) 309–340.]
> **|Λ_ε| ≤ 2c/π + K(log c)²,** K independent of c and ε.

**(I) Israel's nonasymptotic plunge estimates.** [A. Israel, "The Eigenvalue Distribution of
Time-Frequency Localization Operators", arXiv:1502.04404.] Improved nonasymptotic bounds in a
neighborhood of the plunge (BJK: "an improved non-asymptotic estimate"). See also A. Israel,
A. Mayeli for higher-dimensional versions.

**(KRD) Karnik–Romberg–Davenport nonasymptotic bounds.** [S. Karnik, J. Romberg, M. A. Davenport,
"Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate
spheroidal sequences", Appl. Comput. Harmon. Anal. 55 (2021) 97–128; arXiv:2006.00427.] Abstract
**[via fetch, exact]**: "…we establish two novel non-asymptotic bounds on the number of DPSS
eigenvalues between ε and 1−ε. Also, we obtain bounds detailing how close the first ≈2NW
eigenvalues are to 1 and how close the last ≈N−2NW eigenvalues are to 0. Furthermore, we extend
these results to the eigenvalues of the prolate spheroidal wave functions (PSWFs)…" (Their bounds
have the shape #(ε,1−ε) ≲ log N·log(1/ε) with explicit constants, plus exponential-closeness bounds
past the plunge; consult the paper for the constants.) Earlier companion: Karnik–Zhu–Romberg–
Davenport, "The fast Slepian transform", arXiv:1611.04950.

**Also relevant:** D. Slepian, "Some asymptotic expansions for prolate spheroidal wave functions",
J. Math. Phys. 44 (1965) 99–140 (plunge-profile expansions); D. Slepian, H. O. Pollak, Bell Syst.
Tech. J. 40 (1961) 43–64; H. J. Landau, H. O. Pollak, Bell Syst. Tech. J. 40 (1961) 65–84 and 41
(1962) 1295–1336; H. J. Landau, "The eigenvalue behavior of certain convolution equations", Trans.
AMS 115 (1965) 242–256; Osipov–Rokhlin–Xiao, *Prolate Spheroidal Wave Functions of Order Zero*,
Springer (2013) — the standard book treatment.

### 3.3 Smallest eigenvalue of exponential-system Gram matrices at supercritical density

No result found for the *specific* regime of the program (density ratio growing logarithmically,
window fixed): the closest quantitative literature, with statement shapes:

- **A. Moitra, "Super-resolution, extremal functions and the condition number of Vandermonde
  matrices", STOC 2015.** Nodes on the unit circle with separation > 1/N: condition number bounded;
  below 1/N it blows up — the subcritical/supercritical dichotomy for σ_min of N-row Fourier
  matrices.
- **D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, "Conditioning of partial nonuniform Fourier
  matrices with clustered nodes", SIAM J. Matrix Anal. Appl. (2020); arXiv:1809.00658.** "sharp
  lower bounds for the smallest singular value of a rectangular Vandermonde matrix … when some of
  the nodes are separated by less than the inverse bandwidth … polynomial in the reciprocal of the
  super-resolution factor, while the exponent is controlled by the maximal number of nodes which
  are clustered together" [via search summary]. I.e., σ_min ≍ N^{1/2}·(SRF)^{−(p−1)}-type laws for
  cluster multiplicity p.
- **S. Kunis, D. Nagel, "On the smallest singular value of multivariate Vandermonde matrices with
  clustered nodes", Linear Algebra Appl. (2020); arXiv:1907.07119**, and **Kunis–Nagel–?,
  "Single-exponential bounds for the smallest singular value of Vandermonde matrices in the
  sub-Rayleigh regime", Appl. Comput. Harmon. Anal. (2021); arXiv:2107.09326**: "the decay is only
  single exponential in the size of the largest cluster, and the bound holds for arbitrary small
  minimal separation distance" [via search summary].
- **Batenkov–Goldman, "Super-resolution of generalized spikes and spectra of confluent Vandermonde
  matrices", ACHA (2023); arXiv:2203.11923** — confluent/derivative-node generalization.
- **Classical factorial-decay anchors:** H. Widom, H. Wilf, "Small eigenvalues of large Hankel
  matrices", Proc. AMS 17 (1966); B. Beckermann, "The condition number of real Vandermonde, Krylov
  and positive definite Hankel matrices", Numer. Math. 85 (2000) — exponential/factorial λ_min decay
  for structured Gram matrices; the archetype of e^{−cN}-to-e^{−cN log N} smallest-eigenvalue laws.

**Reading for the theory effort:** our measured exponent −1.755·e^{L/2}(L/2+4) ≈ −(const)·N*·ln N*
(N* ≈ zeros below the Nyquist height) sits in the **Widom fixed-c/large-n regime (W)** — the
(n ln n) law — whereas Connes's §6.4 comparator is the **Fuchs fixed-n/large-c regime (F)** — the
pure e^{−2c} law. The plunge formulas (LW), (BK) interpolate between them. Deriving b ≈ 1.755 and
the +4.0 offset means locating λ_min(L) precisely on the (BK) crossover with the Riemann–von
Mangoldt density substituted for the flat Nyquist density. §7.2 quantifies the tension.

---

## 4. Task 4 — formal verification prior art

**(a) Weil positivity / explicit formula: nothing found.**
- **D. Loeffler, M. Stoll, "Formalizing zeta and L-functions in Lean", Ann. Formalized Math. /
  arXiv:2503.00959 (2025).** Mathlib now has: Riemann zeta and Hurwitz zeta, Dirichlet characters
  and L-series, analytic continuation and functional equations, Dirichlet's theorem, and "a formal
  statement of the Riemann hypothesis" [via fetch/search]. No explicit formula, no Weil form, no
  numerics.
- **PrimeNumberTheoremAnd (Kontorovich–Tao et al., GitHub).** README objective **[via fetch]**: "The
  objective of this project is to formalize in Lean the Prime Number Theorem (with classical error
  term), as well as related results such as the Prime Number Theorem in Arithmetic Progressions."
  Stretch goal: "…to obtain the Chebotarev density theorem." **No mention of the explicit formula,
  Guinand–Weil, or Weil positivity.**
- **Isabelle AFP "Zeta_Function" (M. Eberl, 2017)** **[via fetch]**: Hurwitz/Riemann zeta via
  Euler–Maclaurin continuation, functional equation ("reflection formula … and Hurwitz's formula"),
  special values, Euler's proof of infinitude of primes; **"no mention of numerical computations or
  zero verification."** Related AFP: Prime_Number_Theorem (Eberl–Paulson, 2018). Historical:
  Avigad et al., Isabelle PNT (elementary proof, 2005); Carneiro, Metamath PNT (2016).

**(b) Verified numerics for zeta (zero computations): nothing found.** Searches Q20–Q21 (§8) found
no kernel-verified computation of zeta zeros in any proof assistant. Platt–Trudgian-style rigor is
interval arithmetic *outside* proof kernels. Nearest formal artifact: the Coq verification of the
irrationality of ζ(3) (Chyzak–Mahboubi–Sibut-Pinote, 2019) — a posteriori verification of computer
algebra, different domain. (Verified interval-arithmetic *infrastructure* exists: CoqInterval
(Melquiond et al.), Isabelle `approximation` tactic (Hölzl) — relevant to the Bridge Proposition
gap, since these are exactly "interval-verified special functions" ecosystems, though digamma is
not known to be covered in either.)

**(c) Verified positive-definiteness / SOS certificates (generic technique): rich prior art.**
- **J. Harrison, "Verifying nonlinear real formulas via sums of squares", TPHOLs 2007** — HOL Light;
  the origin of kernel-checked rational SOS certificates.
- **É. Martin-Dorel, P. Roux, "A reflexive tactic for polynomial positivity using numerical solvers
  and floating-point computations", CPP 2017**, and **P. Roux, "Formal Proofs of Rounding Error
  Bounds — With Application to an Automatic Positive Definiteness Check", J. Automated Reasoning
  (2016)**; the **ValidSDP** Coq library: "mostly a Coq proved implementation of OSDP, enabling to
  automatically and efficiently prove that polynomials are positive … its ability to return
  verified results (against numerical errors)" [via search]. Verified float Cholesky ⇒ PSD checks
  of concrete matrices — the direct generic ancestor of `weil_window_positive`'s certificate style.
- **V. Magron et al., "Formal Proofs for Nonlinear Optimization", arXiv:1404.7282** (Coq,
  semialgebraic bounds, "sceptical" certificate checking).
- **Lean-side SOS pipeline (2026):** "From LLM-Generated Conjectures to Lean Formalizations:
  Automated Polynomial Inequality Proving via Sum-of-Squares Certificates", arXiv:2605.15445
  (May 2026) — SOS certificates checked in Lean for polynomial inequalities.

**Verdict for claim 3:** the statement "first formally verified window of Weil positivity" is
**supported** — nothing in (a)/(b) comes near it, and Track A's framing (the Bridge gap = interval
special functions in mathlib) is consistent with the actual mathlib/AFP state. Claim it precisely:
the *domain* is new; the *certificate technology* (integer congruence / rational Cholesky-style
kernel checks, perturbation ball) is established art (Harrison 2007 → ValidSDP → Lean SOS 2026),
and THEOREMS.md's phrasing already leans this way. No change needed beyond citing Harrison and
ValidSDP as technique ancestry.

---

## 5. Task 5 — the digamma sandwich

Claim audited: ψ(¼) + ½log(1+4r²) ≤ Re ψ(¼+ir/2) ≤ ψ(¼) + ½log(1+4r²) + 8 (Lemma A(ii),(iv)),
plus the derivative bound |r ∂_r Re ψ(¼+ir/2)| ≤ 2+π/2.

**Result: not found anywhere; folklore-level.** Three targeted searches (§8, Q22–Q24) surfaced only:
real-argument digamma inequalities (Alzer; Qi; Gautschi/Kershaw genre; e.g. "Sharp inequalities for
the psi function and harmonic numbers", arXiv:0902.2524; "Bounds for the logarithm of the Euler
gamma function and its derivatives", arXiv:1508.03267), the standard asymptotic ψ(z) ~ ln z − 1/(2z)
(DLMF §5.11, valid |arg z| < π), and Wikipedia/MathWorld generalities ("Apart from Gauss's digamma
theorem, no such closed formula is known for the real part in general"). Nothing on two-sided
elementary bounds for Re ψ along a fixed vertical line. The inequality is an easy consequence of
Gauss's integral plus 1/t ≤ (1−e^{−t})^{−1} ≤ 1+1/t and a Frullani evaluation — exactly as proved in
THEOREMS.md — and equivalents are implicitly derivable from DLMF error-bounded Stirling forms.
**Verdict: "new as stated, low standalone value" is the correct posture; no citation exists to
displace it, and none is needed to defend it.**

---

## 6. Task 6 — small central values L(½, χ_d) near d = 14693

1. **The values were computed en masse long ago.** M. W. Alderson, M. O. Rubinstein, "Conjectures
   and experiments concerning the moments of L(1/2, χ_d)", Experimental Mathematics 21 (2012),
   no. 3, 307–328; arXiv:1110.0253: values of L(½, χ_d) computed for **−5×10¹⁰ < d < 1.3×10¹⁰** to
   test CFKRS moment conjectures (and Diaconu–Goldfeld–Hoffstein/Zhang lower-order terms). The
   program's |D| ≤ 10⁵ hunt is ~5 orders of magnitude inside this range; L(½, χ_14693) = 0.00180 is
   in principle recoverable from that computation's data. No per-discriminant table is published in
   the paper; the dataset lived with Rubinstein (UWaterloo).
2. **Nonvanishing is verified far past 14693.** S. Omar, "Non-vanishing of Dirichlet L-functions at
   the Central Point", ANTS-VIII, Springer LNCS 5011 (2008): proves/verifies **L(½,χ) ≠ 0 for all
   real characters χ of modulus < 10¹⁰**, via an algorithm for the order of vanishing feasible to
   conductors near 10¹⁶ [via search summaries of the paper and its citers, e.g. arXiv:2603.22124].
3. **LMFDB state, checked directly (2026-07-26):** the Dirichlet character page
   https://www.lmfdb.org/Character/Dirichlet/14693/b exists (modulus 14693, conductor 14693,
   order 2, even, real quadratic, field ℚ(√14693)) **but no L-function object is served**:
   https://www.lmfdb.org/L/Character/Dirichlet/14693/b returns **HTTP 404**, and the JSON API is
   Cloudflare/recaptcha-gated to scripted access. This independently confirms PROGRAM.md §2.15's
   "LMFDB has the character 14693.b but serves no L-function at that conductor." (LMFDB's degree-1
   L-function coverage stops far below conductor 14693.)
4. **No published "smallest central value" table found** for quadratic Dirichlet L-functions
   (searches Q25–Q27). The extreme-value literature goes the other way (large values, e.g.
   "Extreme central values of quadratic Dirichlet L-functions with prime conductors",
   arXiv:2306.16886). The symplectic 1.50 exponent matches the known CFKRS/Katz–Sarnak small-value
   heuristics, as PROGRAM.md §2.10 already concedes.

**Verdict:** D = 14693 is "record of our scan" only, exactly as the repository already states; the
correct diligence citation set is Alderson–Rubinstein (values), Omar (nonvanishing to 10¹⁰), and
the LMFDB 404 check above. To upgrade the record claim one would have to obtain Rubinstein's raw
dataset and extract argmin |L(½,χ_d)| over |d| ≤ 10⁵ — an action item, not a search item.

---

## 7. Flags for the parallel theory effort

### 7.1 Verified dictionary: Connes §6.4 ≡ Fuchs n=4 (and CC's 2021 point sits on our envelope)

- Fuchs (F) at n = 4 with c = 2π e^{L_C} (L_C = Connes's support length = our L/2):
  1−λ₄ ~ 4√π·(8⁴/4!)·(2πe^{L_C})^{4.5}·e^{−4πe^{L_C}}; with χ₂ = √λ₄, 1−χ₂ ≈ (1−λ₄)/2. The
  prefactor evaluates to 2.3617×10⁶ vs Connes's (2¹⁴/3)√2π⁵ = 2.3635×10⁶ (0.08% = rounding), and
  the exponents match term for term (e^{−4πe^L}, +9L/2 from c^{4.5}). **Connes's comparator is
  literally Fuchs's Theorem 1 at n=4.** (This also fixes a small inconsistency in his footnote's
  "a = √(2π)λ": the formula as printed corresponds to prolate bandwidth parameter 2πλ².)
- CC zeta-cycles' single deep point: λ² = 11 (our e^{L/2} = 11, L = 4.796), smallest eigenvalue
  2.389×10⁻⁴⁸. Our envelope predicts ln λ = 10.2 − 1.755·11·(2.398+4) = −113.3, i.e. 10^{−49.2}.
  The Fuchs/Connes comparator with corrections gives ≈10^{−49.0}. All three agree within ~1.5
  decades at this depth (measured −47.6 vs predicted −49.2/−49.0) — the 2021 numeric sits
  essentially on our envelope, which both validates the law against an independent computation and
  confirms the two truncations measure the same physics at this depth (before diverging; §7.2).

### 7.2 The substantive tension to resolve (this is the sharp question now)

At c = e^{L/2} = 100 the two laws **diverge materially**: our envelope gives
|ln λ| ≈ 1.755·100·(4.605+4) = 1510 (log₁₀ ≈ −656), while Connes's comparator/Groskin's
extrapolation give log₁₀ ≈ −530 (|ln λ| ≈ 1221; Groskin's Aitken: −536.76/−533.70, "approaching
the … prediction monotonically"). Three possible resolutions, all checkable: (i) the CvS
prime-cutoff truncation and the support truncation are genuinely different quantities in the deep
regime; (ii) our (L/2+4) log-factor is a mid-range fit that must bend toward the pure-exponential
Fuchs law beyond L ≈ 4.2 (ENVELOPE.md already admits "a mild upward bend … is not yet excluded" —
this gives it a concrete predicted magnitude and direction); (iii) Groskin's finite-N extrapolation
is unconverged. Discriminating experiment: push the certified spectral ladder to L ≈ 5.5–6
(e^{L/2} ≈ 16–20) where the two predictions already differ by >15 decades.

### 7.3 Citation hygiene in PROGRAM.md

- §1 "The live program" attributes the P(n)-windowed criterion to arXiv:2310.18423; that paper's
  abstract is the semilocal prolate-operator paper and contains no P(n) statement. The windowed
  criteria actually in print are: Yoshida 1992 (RH ⟺ nondegeneracy of Q_W^a for every a>0, per
  Suzuki), Bombieri 2000/2003 (variational windows), CCM 2511.22755 (the N,λ → ∞ strategy), and
  the CvS/CCM finite matrices per Groskin. Recommend re-pointing that sentence (or citing the CCM
  "in preparation" [31] title via 2602.04022's bibliography).
- The rigidity-of-the-prime-2 statement ("1.9999/2.0005") could not be located in 2006.13771's
  text by this sweep (it may be in a talk/other paper); re-source before citing.
- ENVELOPE.md should cite 2602.04022 §6.4 + 2605.20224 up front; the cover email's question (b)
  should acknowledge Connes's own Fuchs-based comparator and pose the question as the *log-factor
  discrepancy* (§7.2), which is a sharper and more respectful question than "is it derivable".

### 7.4 What remains genuinely unclaimed in the corpus (as of this sweep)

1. The support-normalized fitted envelope with out-of-sample validation (interpolation, threshold
   band, two-window extrapolation).
2. Threshold-glide *measurements* and any quantitative modulus of continuity (the Glide Theorem's
   modulus, even if the continuity itself is Suzuki's).
3. Dirichlet-family margins in any form: the conductor rescaling T*_χ = (2π/q)e^{L/2}, the
   universality of the decay constant, the sign ledger, the pole flip.
4. Interval-certified two-sided margin enclosures at any depth (Groskin 2607.02828 gives
   certification *budgets*, not certificates).
5. The smooth-staircase vs Poisson replacement experiment (density-vs-rigidity attribution of the
   envelope constant).
6. The Lean-kernel-verified positivity window (claim 3).

---

## 8. Search log (auditability of absences)

Fetches (all arXiv/publisher pages, read-only): 2006.13771 (abs + ar5iv full), 2106.01715 (abs +
ar5iv full), 2310.18423 (abs), 2511.22755 (abs + full HTML, local), 2602.04022 (full HTML, local),
2206.03682 (abs), 2209.04658 (abs), 2606.09096 (abs + full HTML, local), 2605.20224 (abs + v2 HTML),
2607.02828 (abs/full), eudml.org/doc/252338 (Bombieri 2000), math/0103058 (abs + PDF, local
pdftotext), 1804.01257 (abs + ar5iv full, local), 2006.00427 (abs), 2005.02996 (via search),
2411.19562 (abs), 1403.7079 (abs), 2603.22124 (HTML), github.com/AlexKontorovich/PrimeNumberTheoremAnd,
isa-afp.org/entries/Zeta_Function.html, lmfdb.org/Character/Dirichlet/14693/b,
lmfdb.org/L/Character/Dirichlet/14693/b (404), lmfdb.org API (recaptcha-blocked, noted).

Searches (WebSearch, 2026-07-26):
Q1 "Connes 2026 arXiv truncated Weil quadratic form ground state smallest eigenvalue prediction";
Q2 Connes "Past, Present and a Letter Through Time" arXiv;
Q3 "Weil positivity" OR "Weil explicit formula" quadratic form "Dirichlet" character truncated numerical eigenvalue;
Q10–Q11 (family variants of Q3, plus Suzuki full-text grep for "character"/"conductor": 0 hits);
Q12 frame Riesz basis exponentials frequencies "zeros of the Riemann zeta function" sampling completeness;
Q13 Bondarenko Radchenko Seip "Fourier interpolation" zeros zeta;
Q14 "lower frame bound" OR "frame constants" exponential system interval density log growing/unbounded;
Q15 Baez-Duarte Balazard Landreau Saias Burnol Nyman-Beurling "d_N" "1/log N";
Q16 smallest singular value Vandermonde nodes unit circle clustered super-resolution Moitra Batenkov;
Q17 Karnik Romberg Davenport "Improved bounds" prolate DPSS nonasymptotic;
Q20 "formally verified"/"formal proof" numerical verification zeta zeros interval arithmetic Isabelle Coq Lean;
Q21 formally verified positive definiteness certificate matrix Cholesky Coq ValidSDP Harrison SOS;
Q22 inequality digamma complex argument real part bound logarithm psi(1/4 + it);
Q23 mathlib Lean "Riemann zeta" functional equation "Dirichlet L" formalization;
Q24 "psi(1/4)" OR digamma "log(1+4r^2)"/"log(1+4t^2)" inequality bound;
Q25 Rubinstein quadratic Dirichlet L central values data tables download;
Q26 Chowla nonvanishing L(1/2) quadratic numerical verification smallest/minimum central value;
Q27 "10^10" nonvanishing central point real characters + Alderson Rubinstein Experimental Mathematics range;
Q28 Omar "Non-vanishing of Dirichlet L-functions at the central point" ANTS 2008.

Nothing was contacted, posted, or submitted; the only file written is this report.
