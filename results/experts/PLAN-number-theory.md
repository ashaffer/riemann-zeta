# PLAN — Analytic Number Theory

Independent consultant plan for the Positivity Gate program. Written without
reading any other expert's PLAN file. All repo-data claims below are taken from
`results/RESULTS.md` (July 25–26 sections) and `THEOREMS.md`; one light
computation (a refit of the published ladder points, numpy least squares, <1 min)
was run and its outputs are quoted where used.

Author's frame: I treat the program's central measured object as a problem in
the analytic theory of the explicit formula and in the extremal theory of
entire functions of exponential type — the two subjects where analytic number
theory actually owns tools for it.

---

## 1. Reformulation

**The object.** For L > 0, a = L/4, and unit φ ∈ L²[−a, a], the truncated Weil
form is Q_L(φ) = P(φ) + A(φ) − Π(φ) (pole + archimedean − primes; ledger of
`PROGRAM.md` §6), and λ(L) = inf Q_L. Under RH the certified identity reads

  Q_L(φ) = 2 Σ_{γ>0} |φ̂(γ)|²,

so λ(L) is the **lower frame bound of the exponential system {e^{iγx}} at the
zero ordinates, over an interval of length ℓ = L/2**. Since φ̂ is entire of
exponential type a = L/4 and L² on ℝ (Paley–Wiener), λ(L) is equivalently the
minimum of a discrete-restriction quadratic form on the Paley–Wiener space
PW_{L/4}. This is the language in which every measured phenomenon in
§2.14–2.17 becomes a classical-looking extremal problem.

**Densities and the Nyquist height.** The ordinate counting function is
N(T) = N̂(T) + S(T) + O(1/T), N̂(T) = (T/2π) log(T/2πe) + 7/8, with the
unconditional bound |S(T)| ≤ 0.112 log T + 0.278 log log T + 2.510 (Trudgian,
J. Number Theory 134 (2014), 280–292). Local density ρ(t) = (1/2π) log(t/2π).
Sampling (positive lower frame bound) on an interval of length ℓ requires
one-sided density ≥ ℓ/2π = L/4π (Beurling; see Seip, *Interpolation and
Sampling in Spaces of Analytic Functions*, AMS ULECT 33, 2004). Equality
ρ(T) = L/4π occurs exactly at the repo's Nyquist height T*(L) = 2π e^{L/2}.

**The deficit measure — an exact identity organizing the law.** Define

  dμ_L(t) = [ L/4π − ρ(t) ]₊ dt = (1/2π) log⁺(T*/t) dt on [0, T*].

Then the total sub-Nyquist deficit is **exactly**

  μ_L([0, T*]) = T*/2π = e^{L/2}    (verified numerically to 6 digits at
  L = 2.485 and 3.555 in this consultation; the integral is elementary).

The measured law ln λ(L) ≈ 10.2 − 1.755 e^{L/2}(L/2 + 4) therefore says:

  −ln λ(L) ≈ 1.755 · (L/2 + 4) · μ_L(total) :
  **each unit of Nyquist-deficient zero mass costs 1.755·(log(T*/2π) + 4) nats
  of margin.** From the published ladder (RESULTS.md): measured cost-per-unit-
  deficit (10.2 − ln λ)/e^{L/2} = 8.58, 9.23, 9.68, 10.16 across the four solid
  windows vs 1.755(L/2+4) = 8.56, 9.20, 9.65, 10.14. Equivalently, since
  (T/2π)(log(T/2π) + 4) = N̂(T) + 5T/2π − 7/8, the exponent is the linear
  functional 1.755·[N̂(T*) + 5·T*/2π − 7/8] of the counting function — angle
  (b) of my brief in closed form.

**Angle (a) in one sentence each.** Does the law *follow from* known
zero-statistics? The slope functional needs only N̂ plus bounded displacement
γ_k = γ̂_k + O(1), which is **unconditional** (S(T) ≪ log T gives absolute
displacement ≤ 2π·0.112 + o(1) ≈ 0.71 asymptotically; ≤ ~3 uniformly): no
pair correlation, no zero-density theorems needed for the slope. Does the law
*imply* known statements? At current precision it constrains only the counting
function and the rigidity class (the repo's own §2.17 smooth-staircase result);
it neither implies nor is implied by pair correlation beyond an O(1) offset.
This is Lemma NT-2's content.

**Angle (d): where exactly is the RH tension?** Nowhere in the decay. Under RH,
λ(L) is a strictly positive, non-increasing (Theorem 1) function collapsing
super-exponentially; a positive function may approach 0 as fast as it likes.
The RH-equivalent statement is the *sign* λ(L) ≥ 0 for every L, and the
quantitative leverage runs entirely through support length, not margin depth:
if a zero ρ₀ = 1/2 + δ₀ + iγ₀ exists (δ₀ > 0), the form goes certifiably
negative once L ≳ (2/δ₀) log(C log γ₀ / δ₀²) (Lemma NT-4), so full-infimum
positivity at support L excludes only off-line zeros with
δ ≳ (2/L)·log log γ. The melting margins are the frame-theoretic price of the
growing deficit mass μ_L and carry *no* RH-content by themselves; the
RH-content of the ladder is linear in L while the measurement cost is
doubly exponential. This asymmetry is the sharpest strategic fact my field can
contribute, and it cuts both ways (see §5).

**Angle (f) in one number.** Platt–Trudgian (Bull. LMS 53 (2021), 792–797)
verified RH to height T₀ = 3·10¹². Converting that capital into unconditional
truncated-Weil positivity (Lemma NT-4(ii)) buys, on H¹-bounded test classes,
only L ≲ 2.7 — because the tail penalty decays like 1/T₀ while λ(L) collapses
like exp(−1.755 e^{L/2}(L/2+4)), and the two curves cross just past the p = 3
window. Thirty years of zero verification purchases about one prime window of
unconditional positivity. Quantifying this exchange rate precisely is itself a
publishable observation about the field's verification monoculture.

---

## 2. Lemma candidates

Notation as above; Γ̂ = {±γ̂_k} is the smooth staircase (N̂(γ̂_k) = k − 1/2),
and for any symmetric sequence Γ, Λ_Γ(L) denotes the lower frame bound
inf{ 2Σ_{γ∈Γ, γ>0} |φ̂(γ)|² : ‖φ‖₂ = 1, supp φ ⊂ [−L/4, L/4] }.

### Lemma NT-1 (Staircase envelope bracket; "Widom with drift")

**(a) Statement.** There exist absolute constants 0 < b₋ ≤ b₊ < ∞, C ≥ 0 and
L₀ such that for all L ≥ L₀:

  b₋ · e^{L/2} (L/2 − C) ≤ −ln Λ_Γ̂(L) ≤ b₊ · e^{L/2} (L/2 + C).

Sharp form (the real target, conjectural): there exist b and c₀ with

  −ln Λ_Γ̂(L) = b · e^{L/2} (L/2 + c₀) + O(L),

where b and c₀ are explicit functionals of the potential theory of dμ_L.
Candidate closed forms to discriminate numerically before proving anything:
b ∈ {2 (electrostatic |·|² doubling), 7/4, √π ≈ 1.7725} and
c₀ ∈ {2 + log 2π ≈ 3.838, 4}. (The repo's fit is b = 1.755, c₀ = 4.0; my
refit of the four solid windows gives (a, b, c₀) = (10.58, 1.656, 4.40) with
a flat degenerate valley in (b, c₀) — the family is over-parameterized on the
measured range, which is exactly why frozen-parameter runs are needed.)

**(b) Proof strategy.**
*Upper bound on Λ (test-function side).* (1) Take the canonical product
F₀(z) = Π_{γ̂_k ≤ T*} (1 − z²/γ̂_k²) and multiply by a band-edge mollifier G of
exponential type L/4 − τ (prolate or Gaussian-truncated) so F = F₀·G ∈ PW_{L/4}
∩ L². (2) Compare log|F₀| against the full-Nyquist comparison function E of
type L/4 (sine-type with zeros at density L/4π): the difference of potentials
is exactly the logarithmic potential of the deficit measure,
D(t) = ∫ log|1 − t²/s²| dμ_L(s). At the band edge the computation is exact:
D(T*) = (T*/2π)[4 − Σ_{n≥1} 1/(n(2n+1)²)] ≈ 3.85·e^{L/2}. (3) The missing
(L/2)-factor in the exponent must come from the above-band samples: F cannot
vanish at the super-Nyquist ordinates t > T*, and the value
Σ_{γ̂ > T*}|F(γ̂)|² is controlled by the decay budget of G plus the growth of
the product; carrying the kernel log(T*/s) + log(T*/2π) through the deficit
integral gives ∫(1/2π) log(T*/s)[L/2 + log(T*/s)]ds = e^{L/2}(L/2 + 2) — the
measured shape, with b = 2 and c₀ = 2 + corrections. (4) Optimize τ.
*Lower bound on Λ (the UPT-relevant side).* Quantitative sampling below the
minimizer's scale: split at height T*(1+δ); above it the sequence is
uniformly super-Nyquist and separated-after-thinning, so a quantitative
Marcinkiewicz–Zygmund / Plancherel–Pólya argument with Remez-type constants —
Kovrijkine's method (Proc. AMS 129 (2001), 3037–3047) and Nazarov's Turán
lemma (Algebra i Analiz 5 (1993)) — gives Σ_{γ>T*(1+δ)}|φ̂(γ)|² ≥
(cδ)^{C·ℓT*} ‖φ̂‖²_{above-band}; below it, bound the in-band mass a unit
PW-function can hide in the sub-Nyquist gaps by the same Remez technology run
on the gap structure of Γ̂. The two regimes meet at exponent const·e^{L/2}·L —
the bracket.

**(c) Hardest missing step.** A second-order Landau–Widom asymptotic for
concentration/sampling problems whose density drifts *across* the band
(here: logarithmically). Widom (Arch. Rational Mech. Anal. 17 (1964)) and
Landau–Widom (J. Math. Anal. Appl. 77 (1980), 469–481) treat fixed bands and
constant density; the (L/2 + c₀) structure vs plain e^{L/2} is precisely the
drift term, and no off-the-shelf theorem produces it. Secondary gap: the
literature's sampling constants are for sets, not for *discrete sub-Nyquist
node families*, and the sub-Nyquist gap-hiding estimate has to be built.

**(d) Difficulty.** Bracket: months. Sharp (b, c₀): research-program — but it
is the program's own M3 target ("derive b and the offset from Landau–Widom/
Sonin asymptotics"), so this is the mainline, not a detour.

**(e) Numerical stress tests to run BEFORE proof attempts.**
1. *Density-shift discrimination* (cheap; `src/model_zeros.py` machinery).
   Run the staircase model with N_h(T) = (T/2π)(log(T/2πe) + h) for
   h = −1, 0, +1. Every candidate kernel predicts deficit mass e^{L/2−h}, but
   kernel-candidate A predicts an unchanged (L/2 + c₀) factor while candidate
   B (edge-potential + global-type) predicts (L/2 − h + c₀ + h·(kernel
   weight)). One overnight grid decides the kernel shape before any analysis
   is attempted. Note the q-family data *already* discriminates partially:
   density shift h = log q with measured slopes 11.2–12.3 per e^{L/2}/q
   against 1.755(L/2+4) = 11.0–11.9 at the family's mid-L favors the
   analytic-conductor kernel (global term log(qT*/2π) = L/2).
2. *Frozen-parameter fits* (minutes; done in part during this consultation).
   Refit the solid windows with b frozen at 2, 7/4, √π. My run: free fit
   b = 1.656, c = 4.40, RSS 1.6e−4; frozen b = 2 forces c = 3.23 with RSS
   1.5e−2 (~100× worse) — on the measured range b = 2 with constant c is
   disfavored, so if the sharp analysis yields b = 2 it must also yield an
   L-dependent c(L) = c∞ + O(1/L). That is a concrete analytic signature to
   look for in the Widom-drift computation.
3. *Exact-AP calibration.* Compute Λ for pure arithmetic progressions at
   densities (1±ε)·Nyquist, where answers are classical, to calibrate the
   Remez/MZ constants of the lower-bound machinery.
4. *Function-field laboratory (angle e).* For a genus-g curve the ordinates
   are 2g angles on the unit circle (Weil: RH is a theorem; angles ~ USp(2g)
   by Katz–Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*,
   AMS 1999). The FF analogue: minimize Σ_j |P(e^{iθ_j})|² over trigonometric
   polynomials of degree ≤ n, ‖P‖_{L²} = 1 — Nyquist at n = g. Sample θ from
   USp(2g) (numpy, minutes) or from hyperelliptic point counts over small F_p,
   and measure −ln λ vs the deficit-integral prediction b_FF·(g−n)·(log(g/n)
   + c) as n/g varies. This calibrates the entire deficit-potential mechanism
   in the one world where the underlying RH is proved.

### Lemma NT-2 (Rigidity transfer: bounded displacement moves only the offset)

**(a) Statement.** There exist absolute constants C₁, C₂ such that: for any
two symmetric sequences Γ = {±g_k}, Γ′ = {±g_k′} whose counting functions are
within O(1) of N̂ and with sup_k |g_k − g_k′| ≤ Δ ≤ 1,

  | ln Λ_Γ(L) − ln Λ_{Γ′}(L) | ≤ C₁ (1 + Δ) e^{L/2} + C₂ L  for all L ≥ 2.

Corollary (unconditional input): since |γ_k − γ̂_k| ≤ C_disp absolutely
(from |S(T)| ≤ 0.112 log T + … , Trudgian 2014; asymptotically ≤ 0.71,
conservatively ≤ 3 for all k — itself a 10-line lemma worth recording), under
RH: ln λ(L) = ln Λ_Γ̂(L) + O(e^{L/2}). **The (L/2 + c₀) slope structure of the
envelope is identical for the true zeros and the smooth staircase; everything
arithmetic beyond Riemann–von Mangoldt + S(T) ≪ log T lives in the O(e^{L/2})
offset.** This upgrades the repo's §2.17 measurement ("density, not
arithmetic") from observation to theorem-shape, and identifies exactly which
classical inputs it needs — none deeper than Backlund-era bounds.

**(b) Proof strategy.** Do NOT attempt eigenvalue perturbation: the bottom of
the spectrum is exponentially clustered (the §2.12 cascade), so operator-norm
perturbation loses everything. Work at the level of log-potentials:
(1) express the two frame problems through their canonical-product/de Branges
structure functions E_Γ, E_Γ′ (de Branges, *Hilbert Spaces of Entire
Functions*, Prentice-Hall 1968); (2) the hypothesis |g_k − g_k′| ≤ Δ with
matched counting gives |log|E_Γ(t)| − log|E_Γ′(t)|| ≤ CΔ·ρ(t)·(harmonic-
conjugate factor) pointwise off small exceptional neighborhoods, whence
potential differences integrate to ≤ CΔ·(total relevant mass) = CΔ·O(e^{L/2});
(3) push the comparison through the NT-1 bracket (i.e., compare each sequence
to its own equilibrium problem, not to each other's minimizers). Literature
anchors: Kadec's 1/4-theorem and Avdonin's "1/4 in the mean" (both at critical
density, O(1) loss) are the nearest existing perturbation statements; what is
needed is their sub-Nyquist, quantified-exponential-loss analogue.

**(c) Hardest missing step.** Losslessness at log scale: a displacement
argument that never passes through a spectral gap (there is none — the cascade)
and never pays more than e^{CΔe^{L/2}}. The exceptional-set control near
coincidences g_k ≈ g_k′ is where a naive potential comparison leaks.

**(d) Difficulty.** Months for the stated one-sided form; the sharp constant
(does C₁ → 0 for mean-zero rigid displacements? — the measured Poisson-vs-true
gap of only 1.5–2 orders suggests strong cancellation) is likely-open.

**(e) Numerical stress tests.**
1. *Adversarial displacement* at (L, m) = (2.485, 48) and (2.996, 48), spectral
   basis, staircase ordinates displaced by: (i) alternating ±Δ; (ii) coherent
   rarefaction (+Δ below T*, 0 above — predicted worst case); (iii) mean-zero
   random ±Δ; Δ ∈ {0.1, 0.25, 0.5, 1.0}. Lemma predicts |Δ ln λ| ≤ C(1+Δ)e^{L/2}
   with **no change in the fitted L/2-slope across windows**. A slope change
   under bounded displacement kills the lemma as stated — a clean kill
   criterion costing one afternoon of compute.
2. *GUE interpolation* (Prediction P2 below): unfolded GUE ordinates should
   land between smooth and Poisson, close to smooth. Quantifies which
   displacement statistics (variance ~ log log T*) drive the offset.

### Lemma NT-3 (Conductor and degree rescaling from the analytic conductor)

**(a) Statement.** (i) *Family form.* For primitive real χ mod q (pole-free
form, ledger normalization), with N_χ(T) = (T/2π) log(qT/2πe) + O(log qT)
(classical; Iwaniec–Kowalski, *Analytic Number Theory*, AMS Colloq. 53, Ch. 5)
and family Nyquist height T*_χ = (2π/q) e^{L/2}: under GRH_χ,

  −ln λ_χ(L) = b · (e^{L/2}/q) · (L/2 + c₀) + O(L + log q),

with the SAME b, c₀ as ζ; parity and pole shift only the O(L + log q) term,
with the parity shift computable to first order from the archimedean kernel
difference Re ψ(3/4 + ir/2) − Re ψ(1/4 + ir/2) (reflection-formula integrals
in the style of THEOREMS.md Lemma A). Deficit-mass identity:
∫₀^{T*_χ} [L/4π − ρ_χ(t)] dt = e^{L/2}/q + O(log q). (ii) *Degree form —
the new falsifiable structure.* For a self-dual degree-d L-function of
conductor q_π (density (d/2π) log(t/2π) + (1/2π) log q_π + O(1/t)), the
Nyquist height is T*_π = 2π (e^{L/2}/q_π)^{1/d}, the deficit mass is
d·(e^{L/2}/q_π)^{1/d}, and

  −ln λ_π(L) ≈ b · d · (e^{L/2}/q_π)^{1/d} · ( L/2d + c₀^{(d)} ),

i.e. for GL(2) the collapse runs on e^{L/4}, not e^{L/2} — margins at support
L behave like ζ's at support L/2 + 2 log q_π adjustments. This is angle (c)
answered by construction: T*_χ is the height at which the *analytic conductor
density* (1/2π) log 𝔠(χ, t) reaches the Nyquist density of the support.

**(b) Proof strategy.** Entirely parasitic on NT-1: rerun the deficit-potential
computation with ρ_χ (resp. ρ_π); the unconditional inputs (explicit formula
for L(s,χ), counting with explicit error, e.g., Selberg-era bounds) are
classical. The offset functionals need the archimedean comparisons only.

**(c) Hardest missing step.** Nothing new for the slope beyond NT-1 itself.
For the offset: uniformity in q when χ(p) = 0 deletes small primes from the
window structure (smooth q could break the O(log q) error term); for degree
d ≥ 2: the Ramanujan bound is assumed in writing the prime side — for GL(2)
holomorphic forms it is a theorem (Deligne), so start there.

**(d) Difficulty.** (i): days-to-weeks conditional on NT-1's bracket; its
*measured* verification is already half-done in the repo. (ii): stress-test
now, proof research-program (it inherits NT-1's gap).

**(e) Numerical stress tests.**
1. *Universal second constant.* Refit the q = 3, 5, 7 ladders (RESULTS.md, day
   two, third session) in the variable x = e^{L/2}/q with the 3-parameter law
   a_q − b·x·(L/2 + c_q): prediction c_q = 4.0 ± 0.7 and b = 1.755 ± 0.1 for
   all three q. Currently only segment slopes are tabulated (11.2–12.3);
   the refit is free — the data already exists.
2. *Parity offset.* a_odd − a_even against the computed archimedean functional
   (q = 5 even vs q = 3, 7 odd), same fits.
3. *The GL(2) port — the sharpest single test in this plan.* Build the
   explicit-formula form for Ramanujan Δ (level 1, weight 12): prime side from
   τ(p) (exact integers, trivially computable to p ≤ e^{L/2} — a dozen
   primes); archimedean side = Γ_ℂ(s + 11/2)-kernel, same Gauss-integral
   treatment as Lemma A; no pole. Prediction: the margin ladder collapses on
   T* = 2π e^{L/4}: at L = 5, −ln λ_Δ ≈ 3.51·e^{1.25}·(1.25 + c₀^{(2)}) ⇒
   λ_Δ(5) ~ 1e−28±3 — roughly **28 orders of magnitude above** ζ's predicted
   1e−56 at the same support. A wrong analytic-conductor picture misses by
   e^{L/4} vs e^{L/2} — unmissable even at m = 32. Estimated effort: one
   session with the existing hp/spectral machinery.

### Lemma NT-4 (Quantitative converse Weil: off-line leverage and the
unconditional exchange rate)

**(a) Statement.** (i) *Leverage.* There are absolute constants C₅, C₆, c₇
such that: if ζ has a zero ρ₀ = 1/2 + δ₀ + iγ₀ with δ₀ ∈ (0, 1/2], γ₀ ≥ 2,
then for every

  L ≥ L₀(δ₀, γ₀) := (2/δ₀) · log( C₅ · log(γ₀) / δ₀² ),

the FULL infimum satisfies λ(L) ≤ −c₇ · δ₀² · e^{δ₀ L/2 − C₆} < 0.
Contrapositive: full-infimum positivity λ(L) ≥ 0 excludes all zeros in the
explicit region { (δ, γ) : δ ≥ (2/L) log(C₅ log γ / δ²) } — leverage linear
in L, only log-log in height. (ii) *Unconditional near-positivity.* With
T₀ = 3·10¹² (Platt–Trudgian) : unconditionally, for every L and every unit
φ ∈ H_L with ‖φ′‖₂ ≤ M,

  Q_L(φ) ≥ 2 Σ_{0<γ≤T₀} |φ̂(γ)|² − C₈ (1 + M²) e^{L/4} (log T₀)² / T₀,

whence unconditional strict positivity of Q_L on H¹-balls for all L below the
crossing of the measured envelope with the tail penalty — numerically
L ≲ 2.7 for M = O(1). (The certified rungs themselves are already
unconditional statements about Q_L's Galerkin restrictions; the content here
is the full-inf/functional-class version and its explicit T₀-exchange rate.)

**(b) Proof strategy.** (i) is Weil's converse made quantitative (Weil,
Comm. Sém. Math. Lund 1952; the cleanest modern account of the quadratic
functional is Bombieri, Rend. Mat. Acc. Lincei 11 (2000), 183–233). Build an
even unit wave packet φ with φ̂ having a *simple zero at γ₀*: then the zero
quadruple {ρ₀, 1−ρ₀, conjugates} contributes 4 Re[φ̂(γ₀ + iδ₀)²] ≈
−4α²δ₀² |ĝ(iδ₀)|² < 0 (the simple zero rotates the phase to make the square
real-negative), of size ~ δ₀² e^{δ₀ L/2} · (envelope factors), while the total
positive on-line mass of a height-γ₀ packet is ≤ 2πρ(γ₀)·(1 + o(1)) ≈
log γ₀ — an upper-frame-bound computation needing only the counting function.
Optimize widths; collect constants. (ii) is bookkeeping: zeros below T₀ are
on-line and contribute the nonnegative main term; hypothetical off-line pairs
above T₀ are bounded by 4|φ̂(γ + iσ)|² with σ ≤ 1/2, integration by parts
gives |φ̂(γ + iσ)| ≤ e^{σL/4}(√(L/2) + C‖φ′‖₂)/|γ|, and summing against
dN(t) ≪ log t dt over t > T₀ gives the stated penalty; optionally sharpen the
e^{L/4} with a zero-density estimate N(σ, T) ≪ T^{(12/5)(1−σ)} log^C T
(Huxley, Invent. Math. 15 (1972)) since near-σ = 1 zeros are few.

**(c) Hardest missing step.** For (i): none conceptual — care with the
evenness constraint (φ real even forces φ̂ real even, which is exactly what
the simple-zero trick accommodates) and with uniformity of the on-line mass
bound. For the *usefulness* of (i): it consumes **full-infimum** lower bounds
on λ(L), and the program's certificates (interval Cholesky) bound only
Galerkin restrictions — the missing technology is a certified lower bound for
the infimum over all of H_L, which is NT-1's Remez machinery or a dual/SOS
certificate (see §4). For (ii): sharpening M-dependence.

**(d) Difficulty.** (i): days-to-weeks. (ii): days. Both are honest theorems
of classical type; neither advances UPT alone — their value is compositional.

**(e) Numerical stress tests.**
1. *Calibrate the leverage on a real off-line zero.* The repo already owns one:
   Davenport–Heilbronn, ρ = 0.8085 + 85.699i (δ₀ = 0.3085). Build the
   zero-side frame form for DH ordinates (or the full DH explicit formula —
   its Dirichlet coefficients are explicit) and measure the support L* at
   which λ_DH goes negative; compare with L₀(0.3085, 85.7) ≈ 6.5·(log(C₅·
   4.45/0.095)) ≈ 25 ± (constants). Direct measurement of C₅, C₆ before
   proving them.
2. *Synthetic injection.* Add a fake zero pair at (δ₀, γ₀) = (0.1, 50) to the
   staircase model and locate the sign flip of the frame form vs L; repeat on
   a (δ₀, γ₀) grid to map the empirical L₀ surface.
3. *The exchange rate.* Compute ‖φ′‖₂ for the actual spectral minimizers at
   L = 1.75, 2.485, 2.996 (differentiating the Legendre expansion is exact)
   and tabulate the crossing of C₈(1+M²)e^{L/4}(log T₀)²/T₀ with the measured
   λ(L): verify the L ≈ 2.7 unconditional frontier claimed in §1.

---

## 3. Predictions

**P1 (slope refinement; discriminates the sharp form of NT-1).** The deep
windows currently pull the effective b downward only because they are
unconverged Rayleigh–Ritz upper bounds: computing b_eff(L) = (10.2 − ln λ)/
(e^{L/2}(L/2+4)) on the published points gives 1.759, 1.761, 1.761, 1.759 on
the four solid windows and 1.740, 1.737, 1.722 on the three descending deep
points (my refit run). Prediction: as m → ∞ the deep b_eff values **rise back
to 1.755 ± 0.02** (they are biased low by one-sidedness, and the repo already
reports them "descending toward" the law). Discriminating experiment for
b = 2-with-drifting-c vs b = 1.755-constant: a certified two-sided enclosure
at L = 5.0 — the two hypotheses predict λ ≈ 1.2e−56 vs ≈ 2.5e−57 (factor
~4.7). Falsified if the converged deep points settle materially below the law
(b_eff < 1.70) or if the L = 5 enclosure excludes both candidates.

**P2 (rigidity class; tests NT-2's mechanism).** Replacing the true ordinates
by unfolded GUE/CUE-sampled ordinates (through N̂, same truncation Γ_cut = 420,
m = 48, L = 2.485 — the exact configuration of RESULTS.md's model-zeros table)
will give λ_GUE ∈ [1.0, 2.7]×10⁻¹⁰: strictly between Poisson (2.9e−12) and
smooth (2.75e−10), but **within one order of the true zeros** (2.69e−10), i.e.
much nearer smooth than Poisson, with the true−GUE gap growing at most like
log log T*. Falsified if GUE sits at Poisson level (would kill the
variance-controls-offset reading and with it NT-2's sharp form).

**P3 (family and degree scaling; tests NT-3).** (i) Refitting the q = 3, 5, 7
ladders in x = e^{L/2}/q with a_q − b x (L/2 + c_q) yields c_q = 4.0 ± 0.7 and
a common b = 1.755 ± 0.1 across all three conductors and both parities —
conductor, parity, and pole in the intercepts a_q only. (ii) The GL(2) port
(Ramanujan Δ): the margin ladder collapses on T* = 2πe^{L/4}; numerically
λ_Δ(L = 5) ≈ 1e−28±3, i.e. ~28 orders above ζ at equal support, and the fitted
exponent is d·(e^{L/2})^{1/d}-shaped with d = 2. Either half failing falsifies
the analytic-conductor derivation of the family rescaling.

---

## 4. Interfaces

*(Written blind to the sibling plans, per the independence rule; compositions
name the discipline, not the document.)*

**What my lemmas NEED.**
- From **harmonic analysis**: (1) a variable-density Landau–Widom second-order
  asymptotic (the NT-1(c) gap — the single most valuable import); (2) explicit
  Remez/Turán/Kovrijkine constants for Paley–Wiener restriction to discrete
  node sets at sub- and super-critical density; (3) prolate/Sonin-space
  diagonalization data for the band-edge mollifier optimization.
- From **convex optimization**: dual (SOS/moment) certificates that lower-bound
  the FULL infimum λ(L) over H_L — not a Galerkin restriction — with certified
  basis-truncation tails. Without this, NT-4(i)'s leverage is vacuous
  (§2, NT-4(c)).
- From **numerical analysis**: two-sided convergence brackets for the
  Rayleigh–Ritz descent ("still descending" points promoted to enclosures —
  P1 consumes this at L = 5); certified eigensolves at 1e−60; structured-
  perturbation sensitivity for the NT-2 displacement runs.

**What I OFFER.**
- The deficit measure dμ_L with its exact mass e^{L/2}, as the program's
  normalization: propose N_p[Q_L] = exp(+b(L/2+c₀)e^{L/2})·Q_L, restating UPT
  as "normalized margins bounded below" — the renormalization §2.15 called for,
  now with a candidate closed form to fit against.
- The unconditional displacement bound |γ_k − γ̂_k| ≤ C_disp (a 10-line lemma
  from Trudgian's S(T) bound) — the license for every staircase-model
  computation the repo runs.
- Explicit-formula bookkeeping, counting-function error terms, and the
  quantitative converse-Weil mechanics (NT-4) as a service to any track.

**Named compositions.**
1. **"Widom-with-drift" (× harmonic analysis):** NT-1's bracket + HA's
   variable-density plunge asymptotics ⇒ derivation of (b, c₀) — this IS
   milestone M3's stated analytic target, decomposed into a number-theoretic
   reduction (done here) and a pure-HA asymptotic (theirs).
2. **"Certificate-to-zero-exclusion pipeline" (× convex optimization):**
   an SOS/dual certificate of λ(L) ≥ λ₋ over all of H_L + NT-4(i)
   ⇒ unconditional, criterion-native exclusion regions for off-line zeros —
   the first RH-partial-verification independent of the Riemann–Siegel
   monoculture, which is Track A's declared purpose.
3. **"Function-field envelope theorem" (× algebraic geometry):** NT-1(e)(4)'s
   circle extremal problem + the Hodge-index/intersection-positivity toolkit
   on C × C ⇒ a *proved* envelope law where RH is a theorem (Weil/Deligne),
   calibrating which part of the law is positivity-geometry and which is
   density-analysis, and providing the proof-template the arithmetic case
   must imitate.
4. **"Displacement sensitivity as error model" (× numerical analysis):**
   NT-2's bound d(ln λ)/dΔ ≤ C e^{L/2} gives a physical scale for how much
   eigenvalue movement any perturbation (basis truncation included) may cause;
   use it as a convergence diagnostic for the deep rungs, and conversely use
   their certified perturbation runs as measurements of C₁.

---

## 5. Honest assessment

The strongest objection to this program is that **it may explain everything
and prove nothing**. The envelope law is — by the repo's own best experiment
(§2.17: smooth staircase reproduces the margins; Poisson costs 1.5–2 orders)
— a density functional. My lemmas NT-1, NT-2, NT-3 would, if fully proven,
derive b and c₀, certify the family rescaling, and upgrade "density, not
arithmetic" to a theorem; and at that point the primes would still have
entered only through the certified *identity*, never through an *inequality*
that transfers positivity. Complete success on NT-1–NT-3 advances the
description of the RH-side of Weil positivity and moves the UPT gate by
approximately zero: the law's slope is insensitive to exactly the arithmetic
that distinguishes ζ's zeros from any rigid comparison sequence, and the
offset — the one place arithmetic could hide — is the part my potential-theory
methods control worst (one-sided, O(e^{L/2})-fuzzy). The single lemma with
irreducible RH-content, NT-4, is honest about its dependency: its leverage
activates only when composed with a full-infimum lower-bound technology that
does not currently exist in the repo (all certificates are Galerkin-
restricted), and its unconditional half quantifies how brutal the exchange
rate is — 3×10¹² verified zeros purchase unconditional H¹-class positivity
only to L ≈ 2.7, one window past where the program started. Secondary
objections, stated plainly: the b = 2 electrostatic heuristic behind NT-1's
sharp form is the same genre of reasoning that produced the κ ≈ 0.4 threshold
artifact this repo already had to retract; all deep-window data feeding my
fits are one-sided Rayleigh–Ritz upper bounds; and the smooth-vs-true
comparison at L = 3.555 (9.91e−22 vs 1.58e−22, a factor 6 the *wrong* way,
flagged as truncation uncertainty in RESULTS.md) is an unresolved systematic
sitting directly under NT-2's sharp-form claims. If the collaboration round
cannot produce full-infimum certificates, the correct summary of my
contribution will be: good frame theory, calibrated instruments, zero inches
of gate.

---

## Round 2 — honing (number theory)

Written after reading `SYNTHESIS.md`, `results/agent-law-theory/report.md`
(§3.5, §4), and PLAN-differential-geometry (DG-3). Every algebraic claim below
was re-derived independently in this session (mpmath, 20 dps; commands quoted
where a number is new).

### (a) Verdict on SYNTHESIS §2 — the algebra checked line by line

I re-derived every identity in §2 from my own deficit-measure definitions
without reusing the synthesis's steps. Verdict: **§2 is correct in full.**
Item by item:

**(i) ✓ Exact.** N̂(T*) = e^ℓ(ℓ−1) + 7/8 and D(T*) := (a/π)T* − N̂(T*)
= e^ℓ − 7/8: both verified symbolically and numerically (ℓ = 1.2425:
1.715084 / 2.589263; ℓ = 2.25: 12.734670 / 8.612736 — exact to all printed
digits). Hence N + μD = e^ℓ(ℓ − 1 + μ) + (7/8)(1 − μ), so μ = c₀ + 1 exactly,
with the (7/8)(1−μ) constant absorbed into A. ✓

**(ii) ✓ Exact, with the 7/8 bookkeeping made precise.** My deficit mass is
∫₀^{T*}(1/2π) log(T*/t) dt = T*/2π = e^ℓ **exactly**; the synthesis's
D(T*) = e^ℓ − 7/8. So the precise statement is: **mass(dμ_L) = D(T*) + 7/8**
(law-theory's own D(T*) = T*/2π convention has no 7/8 and equals my mass on
the nose; the three "D"s in circulation differ only by this O(1), which lives
in A). My closed-form identity (T/2π)(log(T/2π)+4) = N̂(T) + 5T/2π − 7/8 is
confirmed exact, so my "+4 reading" is indeed the (b, μ) = (1.755, 5) member
of E = −A + b[N(T*) + μD(T*)]. The identification "NT ≡ law-theory: one law"
**stands**. I further verified law-theory's §3.5 claim on my own ladder data:
their (A, b, c₀) = (11.106, 1.5122, 5.04) and my (10.2, 1.755, 4.0) are the
same curve on the fit window (my §2 already noted the flat degenerate valley);
their deformation family is the instrument that breaks the degeneracy, mine
(frozen-parameter refits) is not. **Consequence I accept**: my §2 candidate
closed forms b ∈ {2, 7/4, √π} are retired under kill-rule K5 — my b = 7/4
entry was precisely the kind of within-degeneracy numerology K5 outlaws
(2 log j₀ = 1.75530 died the same death). Deformation-invariant coordinates
(1.51 ± 0.06, μ = 6.0–6.7) are the statement of record; my deficit-measure
*form* survives unchanged, in sharper coordinates.

**(iii) ✓, with one convention nit and one new exact identity.** DG's action
identity: I verified E + A = 2π[D(T*) − D(e^w T*)] = T*(e^w(w−1) + 1) by
direct algebra (D(e^wT*) = e^we^ℓ(1−w) − 7/8), and re-solved the w-band
independently: w(ℓ=0.875) = 1.1182, w(ℓ=2.25) = 1.2201 against DG's quoted
[1.11, 1.22]. ✓ Nit: **D(eT*) = −7/8 exactly, not 0** (verified numerically:
−0.875000). The exactly-zero statement is the density-model signed integral:
∫₀^{eT*}(a/π − ρ̂(t)) dt = D(eT*) + 7/8 = 0 **exactly**. And the cleanest
form of the capacity endpoint in my language — an identity nobody stated and
I verified exactly (both windows, 6 digits): **the super-Nyquist surplus on
[T*, eT*] equals the sub-Nyquist deficit below T***:

  ∫_{T*}^{eT*} (ρ̂(t) − a/π) dt = e^ℓ = mass(dμ_L)   (exactly).

So eT* is the *balayage height* of the deficit measure — the first height at
which the cumulative signed deficit returns to zero. This is, I believe, the
right semantic for T1: the exponent integrates structure out to the height
where the missing zeros below T* have been fully repaid, and not one step
further. I offer this identity to the T1 writeup (HA-owned, NT co-owner per
the allocation).

**(iv) ✓ Arithmetic confirmed.** w∞ = 1.27846 (e^{w}(w−1) = 1 solved:
residual 3e−6), bracket = 2, dE/dc cap = 4π = 12.5664; crossovers L = 4.32
(1.755, 4) and 4.56 (1.51, 5.04) re-derived from dE/dc = b(ℓ + c₀ + 1). The
saturating-w hypothesis (C4) is correctly labeled a hypothesis; I note that
**my deficit reading survives either Q1 outcome**: the law remains "cost per
unit deficit mass", and only the potential's growth is at stake — unbounded
(≈ b(ℓ + c₀)) if bias, capped at exactly 4π if bend. My P1 is under pressure
exactly as Q4 records (deep Aitken b_eff 1.72–1.74 descending, my falsifier
1.70 not yet fired); I hold the prediction open pending Q1(a,c,d) and accept
the synthesis's decision rule.

### (b) NT input package for T3 (the merged Rigidity Transfer Theorem)

I concede the merge direction: DG-3's counting-discrepancy form
|ln λ[μ₁] − ln λ[μ₂]| ≤ C₀·ℓ·(D + 1) is the right primary hypothesis (my
NT-2 displacement form |Δ ln λ| ≤ C₁(1+Δ)e^ℓ is weaker where both apply and
should survive only as the variant for point-displacement hypotheses where a
counting sup is unavailable). What NT owes T3 is the unconditional input,
constants-exact. Here it is, in final form.

**Lemma R1 (counting license — unconditional, constants explicit).** For all
T ≥ e:

  |N_ζ(T) − N̂(T)| ≤ S₀(T) + 1/(48πT) + ε₃(T) ≤ S₀(T) + 0.007 =: D₀(T),

where N̂(T) = (T/2π)log(T/2πe) + 7/8, S₀(T) = 0.112 log T + 0.278 log log T
+ 2.510, and ε₃ is the cubic tail of the Riemann–Siegel theta expansion
(|ε₃| ≤ 7/(5760πT³)). Sources, exact: |S(T)| ≤ S₀(T) for T ≥ e is Trudgian,
*An improved upper bound for the argument of the Riemann zeta-function on the
critical line II*, J. Number Theory 134 (2014), 280–292, Theorem 1; the
remainder N − N̂ − S = θ(T)/π + 1 − N̂ = 1/(48πT) + O(T^{−3}) is the standard
theta expansion (Edwards, *Riemann's Zeta Function*, §6.5). Diligence note:
Hasanalizade–Shen–Wong (J. Number Theory 235 (2022), 219–241) give
0.1038 log T + 0.2573 log log T + 9.3675; the leading constant is better but
the constant term is worse until log T ≈ 800 — **Trudgian 2014 is the right
citation at every height this program will ever touch.**

*T3 plug-in, evaluated.* T3 needs D = sup_{T ≤ e²T*}|N_ζ − N̂|. Since D₀ is
increasing: D ≤ D₀(e²T*) = 0.112(ℓ + 2 + log 2π) + 0.278 log(ℓ + 3.8379)
+ 2.517. Numerically across every measured window (computed this session):
D₀ = 3.476, 3.538, 3.580, 3.626, 3.663, 3.701 at ℓ = 0.875, 1.2425, 1.498,
1.7775, 2.0125, 2.25. So **(D + 1) ≤ 4.71 on the entire measured range**, and
T3's corollary bound reads |ln λ_ζ − ln λ_sm| ≤ 4.71·C₀·ℓ there — with DG's
measured empirical Lipschitz 1.0–2.3, an order of magnitude of headroom over
every measured offset including the Q3 anomaly (1.84 nats), exactly as the
synthesis states. Growth note for the writeup: D₀(e²T*) = 0.112·ℓ + O(log ℓ),
so the unconditional corollary offset is O(ℓ²), not O(ℓ) — the O(ℓ·(D+1))
form should be quoted with D's ℓ-dependence displayed, or referees will read
an O(ℓ) claim the input does not support.

**Lemma R2 (displacement license — the 10-line lemma, now with its
constants).** Let γ_k be the k-th ordinate (all zeros, multiplicity counted)
and γ̂_k the staircase point (N̂(γ̂_k) = k − 1/2). Proof in full: if
γ_k ≥ γ̂_k + δ then N(γ̂_k + δ−) ≤ k − 1 while N̂(γ̂_k + δ) ≥ k − 1/2 +
δ·ρ̂(γ̂_k) (ρ̂ increasing), so δ·ρ̂(γ̂_k) + 1/2 ≤ D₀(γ̂_k + δ); the left
displacement is symmetric. Hence, with τ_k = min(γ_k, γ̂_k), Γ_k = max:

  |γ_k − γ̂_k| ≤ (D₀(Γ_k) − 1/2) / ρ̂(τ_k),  ρ̂(t) = log(t/2π)/2π.

Evaluated (this session): the bound is **4.14** for heights ≥ 10³, **2.26**
for ≥ 10⁶, **1.47** for ≥ 10¹², asymptotically **2π·0.112 = 0.7037**.
Below 10³ the bound is weak but the truth is strong: measured over the first
80 zeros (mpmath zetazero vs staircase), max |γ_k − γ̂_k| = **0.994 at
k = 34** (first five: −0.387, +0.366, −0.482, +0.686, −0.690). So the
finite-range constant is certifiable by a one-afternoon interval computation
against the repo's zero list, giving the clean citable statement:
**|γ_k − γ̂_k| ≤ 4.2 for all k ≥ 1** (conjecturally ≤ 1.1 from the data;
the ≤ 4.2 version needs only R1 above 10³ plus the finite check below it).

*Scope notes for the merged theorem, stated once and precisely.*
(1) R1 and R2 are **unconditional** — they count all zeros, on-line or not.
(2) The identification of the frame value Λ_{ζ-ordinates}(L) with the Weil
minimum λ(L) is where RH enters; T3's corollary (i) should say "under RH" —
**except** that for e²T* ≤ 3·10¹² (i.e. ℓ ≤ log(3·10¹²/2π) − 2 = 24.9,
L ≤ 49.8) every zero the window sees to its capacity horizon is on the line
by Platt–Trudgian (Bull. LMS 53 (2021), 792–797), and the residual
RH-dependence is confined to the tail terms my NT-4(ii) bounds explicitly.
For every support this program will measure this decade, T3-with-R1 is a
theorem about ζ itself, no hypothesis. (3) The CO-2(e) rider is part of the
statement I endorse: this is a transfer of VALUES; no form-level equivalence
follows (relative margin 2.6e−5, measured).

*What I retain from NT-2 as stated in Round 1:* the displacement-hypothesis
variant (for comparisons where only sup|γ_k − γ'_k| is controlled, e.g. the
adversarial-displacement stress runs), and stress test NT-2(e)(1) unchanged —
it is now T3's pre-proof test alongside DG's jitter data, and the Q6 GUE
point is the shared falsifier (DG-P3 = NT-P2, one experiment).

### (c) Honest assessment, updated for the panel

The composite program changes my Round-1 verdict in one direction and
sharpens it in another. Sharpened: "may explain everything and prove
nothing" is now *load-bearing consensus* — the synthesis's §1.1(g) records
three seats naming the UPT residue identically and no seat claiming a route,
and the 90-day allocation deliberately banks perimeter theorems (T1–T5)
while conceding the gate is not attackable this quarter; my verdict was not
pessimism, it was the panel's own map. Changed: my Round-1 claim that the
offset was "the one place arithmetic could hide" was **wrong in an
instructive way** — law-theory's §3.5 shows the true zeros and the staircase
share all three constants including the offset (A: 11.106 vs 11.128), while
CO-2(e) shows the arithmetic is loudly present at *form* level (the two
forms' keyholes sit at different points; relative margin 2.6e−5, not O(1)).
The arithmetic is not hiding in the value functional at all: it lives in the
form-equivalence, the keyhole positions, and GT's 1-of-32 signing rigidity —
which means the RH-content search space is now correctly fenced, and it is
not where my Round-1 lemmas were digging. The SINGLE result that would most
change my verdict is unchanged in kind and now has a concrete owner and
format: **a certified full-infimum lower bound λ(L) ≥ λ₋ > 0 over all of
H_L at one window** — C2's dual-witness quadrature extended from the
Galerkin section to H_L with certified tails (CO's witness theory + NA's
inequality-form kernel checking supply every ingredient except the tail
bound, which is classical Paley–Wiener bookkeeping I will draft). Composed
with NT-4(i) (quantitative converse Weil, Davenport–Heilbronn-calibrated,
scheduled days 30–60), it converts one rung of the certified ladder into an
unconditional, criterion-native zero-exclusion region — the first output of
this program with irreducible RH-content, and the first partial verification
of RH in history that owes nothing to Riemann–Siegel. If that lands, my
verdict becomes "explains everything, proves the perimeter, and has drawn
first blood on the gate." If it cannot be made to land, the Round-1 closing
sentence stands verbatim.

---

## Round 3 — status: the full-infimum composite (see results/experts/FULLINF.md)

Assignment executed; outcome three-part, all constants verified by script.
(1) **Delivered**: Theorem F4 — certified lower bound for Q_L over an
infinite-dimensional frequency-tail class 𝒞(R, τ̄), from any certified
Legendre–Galerkin rung; at (L, m) = (7/4, 192) the bound is ≥ 1.56e−5 with a
class covering Gaussian packets to height ≈ 40 (first six zeros), pending one
standard certified interval run (hours-scale; queued, not run — 2-worker cap).
The m = 96 variant (minutes-scale run) already covers γ₁. Composition with
NT-4(i) gives the first Riemann–Siegel-free zero-exclusion pipeline; region
tiny, kind new. (2) **Wall theorem (F5)**: the UNRESTRICTED infimum is
unreachable by any subspace-plus-tail template — the form's own coercivity is
logarithmic (Lemma A sharp), forcing split-errors ≥ ~2.8 at every dimension,
five orders above every margin. The missing mathematics is an a-priori
regularity theorem for near-minimizers of Q_L; stated precisely in FULLINF
§10. (3) **Basis no-go (F6)**: polynomial subspaces suffer a quantified
capture-vs-content conflict (√T₂ grows like √m: 406 → 777 across m = 96 →
256); truncated-prolate bases remove it by construction — M1's prolate clause
is now forced by theorem, not preference. New measured points: λ(7/4, 64) =
3.1415961e−5; boundary-flat class minima within 0.04% of unrestricted
(q = 1,2,3,5 windows); m = 48 regression exact vs RESULTS.md.
