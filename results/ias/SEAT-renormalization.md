# SEAT — Renormalization and dynamical systems

Round 1 (independent; no other SEAT file read). Date: 2026-07-26.
Working artifacts: `results/ias/renormalization/` (pre-registration + measurement
scripts and logs for §5). Honesty tiers used throughout:
**THEOREM / COMPUTED / CONJECTURE / SPECULATION.**

---

## §0 Seat card

Toolkit: renormalization-group universality (fixed points, crossover scaling,
marginal operators and their logs); block-spin / decimation constructions and
linear response along the flow; transfer operators and thermodynamic formalism
(Ruelle, Gibbs weights, Lyapunov exponents of cocycles); dynamical zeta
functions with rigor (Giulietti–Liverani–Pollicott, Dyatlov–Zworski, Dolgopyat
gaps, Selberg trace formula); scaling limits of prolate/Toeplitz spectra
(Landau–Widom, Fuchs) read as RG asymptotics. Physics sensibility, mathematics
discipline.

---

## §1 Translation: the envelope program as a renormalization flow

Everything below consumes only repository-certified objects: the truncated
Weil/frame form Q_L, λ(L) = inf Q_L/‖φ‖² (THEOREMS.md header), the invariant
law E := −ln λ = −A + b[N(T*) + μD(T*)] with (A, b, μ) = (11.1–11.8, 1.39–1.51,
6.0–6.7) (results/agent-law-theory.md §4, SYNTHESIS.md §2), the 4π cap past
L ≈ 4.32 (results/agent-deep-windows.md), the marginal law (π²/2)·ln(eT*/t)
with capacity endpoint eT* (law-theory RUN 4), and the kill list
(SYNTHESIS.md §5), which this seat treats as binding law — in particular K2
(no bulk-prolate derivation of the mid-range constants), K5 (no constant
identification from the L-scan alone), K7 (no additive per-zero accounting).

### 1.1 The space the flow acts on, and RG time

State space: pairs (a, ν) — window half-length a = L/4 and a symmetric point
measure ν on the line (the zero configuration), with the value functional
E(a, ν) = −ln λ. The scaling group acts by (a, ν) ↦ (βa, β^{-1}ν); the exact
dilation covariance λ_{a,βν} = (1/β)·λ_{βa,ν} is **COMPUTED to 2·10⁻¹⁵**
(law-theory V4) and is this flow's Ward identity. RG time is s = ℓ = L/2 =
ln(T*/2π): growing the window while rescaling heights by T*(L). The measured
β-linearity E + A = β·(E + A)|_{β=1} (law-theory P3, 1%) is the anomalous
transformation law of the broken dilation symmetry, and it **is** the family/
conductor universality (T*_χ = (2π/q)e^{L/2}): the conductor is pure RG-time
offset. Nothing new claimed here; this fixes coordinates.

### 1.2 The RvM deficit profile is a fixed point of the flow (elementary, new framing)

**THEOREM (calculus-level; two-line verification).** Write u = T/T*(L). The
deficit measure dμ_L(t) = [a/π − ρ(t)]₊ dt of the RvM density
ρ(t) = (1/2π)ln(t/2π) satisfies, exactly,

  dμ_L(uT*) = e^{ℓ} · ln(1/u) du   on u ∈ (0, 1].

One L-independent *shape* ln(1/u)du; total mass e^{ℓ} (recovering NT Round 2's
exact mass identity, SYNTHESIS errata item 3); D(uT*) = u e^{ℓ}(1 − ln u) − 7/8
(so D(T*) = e^{ℓ} − 7/8 and D(eT*) = −7/8 exactly, matching the errata).
Under one RG step (ℓ → ℓ + ds with heights rescaled by e^{−ds}) the rescaled
deficit profile is **invariant**; only its mass multiplies, by e^{ds}.

Reading: the ζ/staircase configuration is not "flowing toward" anything — in
deficit coordinates it already sits ON the self-similar profile at every L,
and RG time only pumps mass through the fixed shape. The law-theory (α, β)
deformations are precisely the transverse directions: β moves along the exact
symmetry (eigenvalue +1, the homogeneity), α tilts the profile (the
discriminating direction that broke the fit degeneracy). This is why the
25-point deformation family was the right linearization experiment. The
discreteness rider stays mandatory (K2/K4): the *profile* is the datum of the
VALUE law only; the exponential smallness itself lives in the sum-vs-integral
gap, and no form-level statement follows.

### 1.3 The one-line form of the law, and the crossover as RG crossover

Let M := e^{ℓ} (deficit mass = T*/2π). The unified mid-range law
(SYNTHESIS §2) is algebraically

  **E + A = b · M · ln(e^{c₀} M),  and the marginal cost dE/dM = b·ln(e^{c₀+1}M),
  capped: dE/dM ≤ 4π.**

Mid-range: cost per unit deficit mass grows like b×(RG age); the crossover is
where b(ln M + c₀ + 1) = 4π, i.e. ℓ = 4π/b − c₀ − 1: L = 4.56 with (1.51,
5.04), L = 4.32 with (1.755, 4) — exactly the two crossover values SYNTHESIS
§2(iv) computes, bracketing where the measured deviations begin. In RG
language the program's two regimes are textbook: a **marginally relevant
coupling** (the grading; see 1.4) drives a slope growing linearly in RG time,
until the trajectory enters the basin of a **fixed point with universal
coupling g\* = 4π**.

**The cap's linearization eigenvalue is −1 (falsifiable).** The measured deep
form ln λ ≈ A′ − 4π e^{ℓ} + p·ℓ (deep-windows final, p ≈ 4.5–6.5) says the
slope g(ℓ) := dE/dc (c = e^{ℓ}) obeys g = 4π − p e^{−ℓ}, i.e.

  dg/dℓ = −(g − 4π),

an autonomous linear flow with eigenvalue exactly −1 at g\* = 4π, for ANY p
(p is amplitude, not exponent). If instead the subleading correction were
c^{θ} (0 < θ < 1) the eigenvalue would be −(1−θ). So "eigenvalue −1" ⟺ "the
subleading term is O(ℓ), the Fuchs (n+½)ln c form" — a scalar, fit-light
discriminator the deep ladders can sharpen (see §4, bet 2 for who should own
p = n + ½). CONJECTURE tier, one derivative above the measured facts.

### 1.4 The marginal law in RG variables; which constants are derivable

A zero at height t crosses its local Nyquist criticality at RG time
ℓ_c(t) = ln(t/2π). The measured marginal worth is, identically,

  f(t) = (π²/2)·ln(eT*/t) = (π²/2)·[1 + ℓ − ℓ_c(t)] :

**π²/2 nats per e-fold of RG time elapsed since the zero's scale went
super-Nyquist, plus one e-fold of grace** (the capacity/balayage e-fold —
NT's exact surplus identity). π²/2 is the Landau–Widom plunge density
(Landau–Widom, J. Math. Anal. Appl. 77 (1980) 469–481: #{n : λ_n ∈ (ε, 1−ε)} =
(2/π²)·ln c·ln((1−ε)/ε) + o(ln c); Bonami–Karoui profile per the transcriptions
in results/agent-prior-art.md §3 — precise BK venue UNVERIFIED here), i.e. the
**Lyapunov rate of the prolate plunge cocycle**. That the same constant appears
as a per-zero, per-RG-time rate is exactly what an RG reading demands: the
marginal direction (the grading, which in rescaled coordinates decays like
ln u/ℓ — logarithmically slowly, the definition of marginal) generates the
(ℓ + c₀) log-correction, precisely as a marginal operator generates logs.

**Answer to this seat's seed question (a): b and μ are NOT eigenvalues.** The
honest RG classification of the measured constants:

| constant | RG meaning | derivable? |
|---|---|---|
| g\* = 4π | fixed-point coupling (prolate/Fuchs universal rate) | YES — frontier's own asymptotics; T5-deep/C4 territory |
| eigenvalue −1 | irrelevant-direction rate at the cap | YES — equivalent to the (n+½)ln c subleading form (§1.3) |
| π²/2 | marginal-direction amplitude per zero (LW plunge rate) | YES — T4's target; the one mid-range constant in reach |
| capacity e (and its grading family, §2 R3) | balayage endpoint of the fixed profile | YES — exact calculus (verified §2 R3) |
| b ≈ 1.51, μ ≈ 6.0–6.7 | **crossover amplitudes**: integrals over the whole trajectory between the free end and the cap | NOT by linearization at either end — only by a global two-sided construction (T5) or by integrating T4's marginal calculus with the ~20% screening |
| A ≈ 11.1–11.8 | non-universal offset (matching at the first zero) | not universal; don't chase |

This matches — and explains — law-theory's §0 finding that "the bulk constants
resisted derivation": crossover amplitudes are trajectory data, invisible to
any fixed-point expansion. It sharpens the program's target list: spend
derivation effort on (4π, −1, π²/2, capacity), and get (b, μ) only from a
matched construction. The kill-list is respected: this is not a bulk-prolate
derivation claim (K2) — the fixed point governs the DEEP regime, where the
Fuchs cap is Q1's live hypothesis, now measured.

### 1.5 Transfer-operator translation, and the labs where the analog of RH is a theorem (seed (c))

The prime ladder Π(φ) = 2Σ_p Σ_k (log p)·p^{−k/2}·ψ_φ(k log p) is the
symmetrized matrix element ⟨φ, 𝓛φ⟩ of the weighted shift/transfer operator
𝓛 = Σ_{p,k} (log p) e^{−(k log p)/2} S_{k log p}: Gibbs weight at inverse
temperature ½ (the critical line) over a suspension flow whose periodic
orbits have lengths log p and entropy 1 (orbit growth e^{x}/x = PNT) — the
Berry–Keating "Riemann flow" (Berry–Keating, SIAM Review 41 (1999) 236–266),
kept rigorous by never asserting the flow exists: only the trace does. Window
truncation at e^{L/2} = keeping orbits of period ≤ RG time. Two rigorous
laboratories realize this structure with the analog of RH a THEOREM:

- **Axiom-A/Anosov flows**: dynamical zeta functions continue meromorphically
  (Giulietti–Liverani–Pollicott, Ann. of Math. 178 (2013) 687–773;
  Dyatlov–Zworski, Ann. Sci. Éc. Norm. Supér. 49 (2016) 543–577), with
  essential spectral gaps à la Dolgopyat (Ann. of Math. 147 (1998) 357–390):
  resonance-free strips = the zero-free-region analog. These give *strips*,
  not lines — the Anosov world's own "RH" generally FAILS beyond the gap;
  useful as a negative control (an Euler product + trace formula alone does
  not force a critical line; cf. §2.2's Davenport–Heilbronn lesson).
- **The Selberg lab (the sharp one)**: geodesic flow on a compact/arithmetic
  hyperbolic surface X = Γ\ℍ. Selberg's trace formula (J. Indian Math. Soc.
  20 (1956) 47–87) is an EXACT explicit formula: "primes" = primitive closed
  geodesics (lengths ℓ_γ, counts growing e^{x}/x), "zeros" = r_j with
  Δ-eigenvalues ¼ + r_j². Self-adjointness of Δ forces r_j real-or-imaginary
  — RH-up-to-small-eigenvalues is a theorem, with small eigenvalues (λ_j < ¼)
  the exact analog of exceptional/Siegel real zeros: for real even φ they
  contribute φ̂(it)φ̂(−it) = (∫φe^{tx})(∫φe^{−tx}) — the same sign-indefinite
  pole-shaped product as the repo's real-zero channel. For congruence groups
  λ₁ ≥ 975/4096 (Kim–Sarnak; appendix to Kim, J. Amer. Math. Soc. 16 (2003)),
  Selberg's λ₁ ≥ ¼ open. So the windowed-positivity instrument ports verbatim
  and its disproof channel (certified negativity ⇒ small eigenvalue) becomes a
  THEOREM-CALIBRATED detector there.

**The conceptual dividend, stated plainly: the envelope decay is NOT the
obstruction to RH.** Both solved labs — function field (staircase-to-wall,
AG-1) and Selberg (to be measured, §2 R3) — have super-exponentially decaying
windowed margins while their RH-analog is a theorem. The decay is frame
theory of a graded spectrum; the theorem-content is the SIGN's uniformity
(CO-3's "trajectory rides the positivity-cone boundary"). Any pitch of the
envelope law outward should say this in the first paragraph.

### 1.6 The function-field lab is a lattice RG; the archimedean place makes RG time continuous (seed (d))

For C/F_q the zero set is 2π/ln q-periodic: the dilation flow has a DISCRETE
scale invariance with lattice spacing ln q (Frobenius = one RG step, exactly).
Textbook consequence of discrete scale invariance: log-periodic structure —
and the curve's margin is indeed a pure staircase with jumps at L = 2n ln q
(AG-1(c) staircase clause), the log-periodic "wobble" in its rawest form. Over
ζ the value group is dense (log p's ℚ-independent — AG §1.4's fifth
obstruction), scale invariance is continuous, and the margin is provably
jump-free — THEOREMS.md Theorem 1 (glide), whose engine (Lemma A) is purely
archimedean. Slogan, honesty-tier CONJECTURE-as-framing: **the archimedean
place is the continuum limit of RG time; the digamma term is the generator of
the continuous flow, and the Glide Theorem is the statement that ζ's
renormalization has no lattice.** What breaks FF-style termination over ℚ is
not lost self-similarity (§1.2: the deficit profile IS self-similar) but
unbounded mass: dim H¹ = 2g < ∞ becomes "effective genus" M = e^{ℓ} growing
with RG time — the wall retreats to infinity at exactly the rate the envelope
measures. The Golod–Shafarevich-shaped question of PROGRAM.md's Addendum
takes its RG form: the tower is the ladder of frequency e-fold shells, and
the growth inequality that would be UPT is the cap dE/dM ≤ 4π.

---

## §2 Candidates

### R1. The Deficit-Dipole Lemma (differential rigidity transfer; the marginal law as linear-response kernel)

**Statement (CONJECTURE, now with direct measured support — §5).** Fix the
smooth staircase at window ℓ, and let the configuration be perturbed by a
count-preserving displacement of the zeros inside a block
[T₁, T₂] ⊂ (t_min, (1−δ)eT*): zero k moves from γ_k to t_k. Then

  ΔE = −(π²/2) Σ_k ln(γ_k / t_k) · (1 + η),   |η| ≤ η₀(δ) < 1,

with η the interaction dressing (measured ≈ +0.17…+0.26 at L = 2.485, §5),
and the first factor **independent of L** (the T* in the marginal potential
cancels in differences — a sharp invariance: the response depends only on the
RG-time displacements Σ ln(γ_k/t_k), not on the window). Sign convention:
moving zeros DOWN (earlier RG time) lowers E (raises λ).

**Route.** This is the differential form of T3 (Rigidity Transfer) with an
explicit kernel: (i) HA's rank-two secular identity (T4(i)) applied per moved
node gives the exact one-node response; (ii) summation over the block with
the screening bound is exactly T3's hardest step in an easier, compactly
supported setting (the displacement field vanishes outside the block, so the
exceptional-set control near coincidences is local); (iii) the L-invariance
clause follows free from the telescoping of the marginal potential. Effort:
inequality version (|ΔE| ≤ (π²/2)(1+η₀)Σ|ln γ_k/t_k|) — weeks, riding T3's
skeleton; the sharp kernel with η(δ) — months, needs T4(ii).

**Interfaces.** DG (T3 owner: this is a strictly weaker, strictly sharper-
statement pilot of T3 — a good first theorem for the same machinery); HA
(T4); law-theory (instrument; RUN 4 is the rank-one boundary case).

**Kill criteria.** (a) §5's test — RUN (passed: ratios 1.17/1.26 in the
pre-registered band, both directions, basis-stable). (b) The L-invariance
test: the same block displacement at L = 2.996 must give the same first-order
ΔE = −0.573·(1+η) within the dressing band; a drift with L kills the kernel
reading (pre-registered as the follow-up: predicted ΔE(avg) ∈ [−0.74, −0.57]
at L = 2.996 for the identical [18, 36] block move). (c) Any violation of the
sign clause anywhere in the worth-support kills it outright.

### R2. The Cap Fixed-Point Theorem (stopped-chirp upper bound + eigenvalue −1)

**Statement (CONJECTURE).** (i) [construction] There exist unit test functions
φ_ℓ ∈ H_L with

  Q_L(φ_ℓ) ≤ exp(−4π e^{ℓ} + C·ℓ),

i.e. the cap rate 4π is achieved by an explicit "stopped chirp": the WKB
chirp of law-theory §2.4 (phase S(x) = πe^{2x}, annihilating the staircase to
leading order) run only to the stopping height T_s = e^{w∞}T*, w∞ = 1.2785
(root of e^{w}(w−1) = 1), glued to the top prolate mode above T_s. (ii) [RG
form] dE/dc ≤ 4π + o(1), and the approach obeys d(dE/dc)/dℓ = −(dE/dc − 4π):
linearization eigenvalue −1, equivalently subleading term p·ℓ with p = n + ½
for the engaged prolate level n (Fuchs, J. Math. Anal. Appl. 9 (1964)
317–330 — the same comparator Connes arXiv:2602.04022 §6.4 uses at n = 4;
identification per results/agent-prior-art.md).

**Route.** (i) is law-theory P4 + HA H3 with the stopping height imposed
rather than optimized; the cost bookkeeping is DG's action identity
E + A = 2π[D(T*) − D(T_s)] (SYNTHESIS §2(iii)), which at w = w∞ gives exactly
4πe^{ℓ}. The RG contribution is the matching argument at T_s: below, the
canonical-product/chirp potential; above, the prolate plunge; smooth fit at
the free boundary determines w∞ (this is where the free-boundary seat should
be able to derive e^{w}(w−1) = 1 from smooth pasting — §4 bet 1). (ii) is a
data-side commitment plus the Fuchs subleading form. Effort: (i)
weeks–months (upper bounds only, no wall entered); (ii) is measurement +
bookkeeping. Interfaces: DG (C4, vector shape test), deep-windows (ladders),
free-boundary seat, riemann-hilbert seat (Fuchs/Painlevé subleading).

**Kill criteria.** DG's vector-level shape test returning "drift" kills the
fixed point reading (then the cap is an artifact of the current depth and
(b, μ) stand alone); a converged deep secant slope > 4π + 0.5% kills (ii);
failure of the stopped-chirp numerics to reach within O(ℓ) of 4πe^{ℓ}
(cheap: law-theory P4's implementation with w frozen at w∞) kills (i) as
stated.

### R3. The Graded-Lab Family (power-law gradings; the Selberg/Weyl point; universality of the marginal profile)

**Statement.** For densities ρ_κ(t) = (a/π)(t/T*)^{κ} (power grading κ > 0;
the RvM log-grading is the κ → 0 limit; the hyperbolic-surface Weyl grading
is κ = 1):

  (i) **THEOREM (calculus level, verified numerically here to 8 digits,
  `results/ias/renormalization/`):** the balayage/capacity endpoint of the
  deficit profile is

    t_cap(κ) = (1 + κ)^{1/κ} · T*,

  monotone decreasing from e·T* (κ → 0: the measured ζ capacity height,
  law-theory §2.3/NT's surplus identity) to 2·T* at κ = 1. The super-Nyquist
  surplus on [T*, t_cap] equals the deficit mass exactly, for every κ —
  NT Round 2's identity is the κ → 0 member of an exact one-parameter family.

  (ii) **CONJECTURE (RG universality of the marginal direction):** the
  single-zero deletion worth for the κ-graded staircase is

    f_κ(t) = (π²/2)·ln(t_cap(κ)/t)·(1 + o(1)),  t ≤ (1−δ)t_cap,

  i.e. the profile shape ln(capacity/t) and the constant π²/2 are
  grading-independent (fixed-point response); the grading enters ONLY through
  the capacity endpoint. The κ → 0 case is the measured law; the constant-
  density case (κ-profile degenerate) correctly gives worth ≡ 0 (law-theory
  §2.1's exact dichotomy; C1(ii)'s lattice limit).

  (iii) **The Selberg instantiation:** at κ = 1 this is a measurable statement
  about a system where the Hilbert–Pólya operator EXISTS (Δ on Γ\ℍ) and
  positivity is a theorem modulo small eigenvalues (§1.5). The windowed
  Selberg form's envelope, capacity height 2T*, and marginal profile give the
  program a second solved-side calibration point, differing from the FF lab
  in exactly one structural feature: graded (κ = 1) vs constant density. The
  FF lab calibrates discreteness-without-grading; Selberg calibrates
  grading-without-arithmetic-mystery.

**Route.** (i) is done (above). (ii): the instrument exists — law-theory's
`law_core.py` staircase generator generalized to power laws is a ten-line
change; measure worths at 6–8 heights for κ = 1 and κ = ½ (hours). Theory:
T4's two-stage mechanism (rank-two secular identity + defect potential) is
grading-agnostic in stage (i); stage (ii)'s equilibrium computation changes
only through the density — if the π²/2 route works for the log grading it
works for κ > 0, and PROVING it first at κ = 1 (where the density is
polynomial and the extremal problem is classical Weyl territory) may be
strictly easier. Effort: measurement days; κ = 1 proof attempt weeks–months
alongside T4. Interfaces: HA (T4), AG (the spliced ladder AG-3 interpolates
the OTHER axis: constant-density blocks approximating gradings; C1(ii)),
quantum-chaos seat (Selberg trace formula mechanics), law-theory instrument.

**Kill criteria (either outcome is information).** Marginal coefficient at
κ = 1 ≠ π²/2 beyond 10% ⇒ the universality reading dies; the marginal
constant is log-grading-specific, which would be the first evidence that
ANYTHING in the value law is special to the RvM class — pointing back toward
arithmetic and against the density-functional consensus (T3's foundations
would need re-inspection). Capacity endpoint ≠ 2T* at κ = 1 ⇒ (i)'s balayage
semantics is the wrong mechanism for the worth support and T1′'s variational-
horizon reading needs revisiting. Pre-registered predictions for the first
run: t_cap = 2T*, coefficient π²/2 ± 10%, edge softening in the last
(1+κ)-fold.

---

## §3 Intuition pumps (all SPECULATION unless tiered otherwise)

**P1 — b = 3/2 and the screening constant 3/π².** The additive (unscreened)
integral of the marginal law over the fixed deficit profile overshoots the
measured slope: per-zero cost π²/2 versus measured bulk b. Their ratio is
b/(π²/2) = 0.306 ± 0.012 against 3/π² = 0.30396 — equivalently **b = 3/2
exactly**, inside law-theory's deformation-invariant error bar (1.51 ± 0.06;
K5-compliant: this comes from the deformation data, not the L-scan). If T4
delivers π²/2, the remaining mid-range content of b is one dimensionless
screening constant 3/π² ~ the fraction of a zero's marginal worth that
survives when ALL zeros try to collect it simultaneously. A log-gas
equilibrium computation of the screened energy of the profile ln(1/u)du is
the natural home (§4 bet 3). Similarly μb ≈ 9.1 sits near 3π — recorded here
only so a derivation has a target to hit or kill; no weight attached.

**P2 — Spec ℤ as a curve of genus e^{ℓ}, and the cap as its growth
inequality.** The deficit mass M = e^{ℓ} plays dim H¹ = 2g: the FF wall
2(2g−2)ln q says "the window exhausts H¹"; over ℚ the effective genus grows
by a factor e per RG step, so the wall retreats forever, and the price of
that retreat is the envelope. UPT in this language: a growth inequality along
the shell tower — cost per new unit of H¹-mass bounded (mid-range b·(RG age),
capped at 4π) with a SIGN that never flips. The Golod–Shafarevich shape the
Addendum asked for: relations (prime terms) never outrun generators (zero
shells) by more than the cap allows.

**P3 — Berry–Keating in the chirp.** The minimizer's WKB phase S(x) = πe^{2x}
(law-theory §2.4) pairs support point x with height r = 2πe^{2x} — the
generating function of the xp / dilation dynamics: x is RG time, r is the
conjugate action. The keyhole vectors are then semiclassical states of the
dilation flow, and the (ℓ + c₀) log-factor is the flow's Ehrenfest-time
enhancement. The quantum-chaos seat can probably make the "+c₀ ≈ 5" a
log-Ehrenfest constant; I bet it is (capacity e-fold) + (edge zone) + O(1)
bookkeeping rather than anything arithmetic.

**P4 — Discrete vs continuous scale invariance as a diagnostic.** Any residual
DISCRETE scale structure in a proposed positivity-bearing object should
produce log-periodic wobble in its envelope (as the FF staircase does). The
measured ζ envelope is wobble-free through 70 orders (glide + smooth law).
So: candidates for the missing operator whose construction favors a preferred
scale lattice (q-deformations, adelic truncations at a finite prime set)
should show a wobble the data excludes — a cheap Track-E audition criterion
this seat offers the constraint table: **fit residuals of the envelope against
a log-periodic modulation; amplitude bound from the existing ladder is
already ≲ 0.1 nat.** (COMPUTED-adjacent: the residual tables in
agent-law-theory/fits.py output would give the bound; not run here.)

**P5 — Why the margin must be tiny: zero slack is fixed-point criticality.**
Rodgers–Tao Λ ≥ 0 says RH has zero margin globally; the RG picture localizes
this: the rescaled configuration sits exactly AT Nyquist criticality at u = 1
for every ℓ (§1.2) — the system is self-tuned to the critical surface, and
critical systems have power/exponential-thin margins as a matter of
universality, with no contradiction to positivity. This defuses the recurring
temptation (PROGRAM.md §2.7-era) to read small margins as near-failure: a
critical fixed point's margin is SUPPOSED to be thin at exactly this rate.

---

## §4 Cross-seat bets (ranked by confidence)

1. **Free-boundary seat (confidence: high).** The stopping height is an
   obstacle-problem free boundary and w∞ = 1.2785 is a smooth-fit constant.
   Bet: writing the minimizer's log-envelope descent as an obstacle problem
   for the potential of the deficit measure, the smooth-pasting condition at
   T_s reproduces e^{w}(w−1) = 1 in one page, and the mid-range drift w(ℓ)
   is the same free boundary before it detaches. Payoff: C4 becomes a
   theorem-shaped mechanism, not a fit; joint deliverable with R2(i).

2. **Riemann–Hilbert seat (confidence: medium-high).** The subleading p·ℓ
   term and the (eT*−t)^{3/2} capacity-edge softening are Painlevé/Airy
   data. Bet: (a) p = n + ½ with n the engaged prolate level, from the
   known connection-problem asymptotics of the prolate (sine-kernel)
   Fredholm determinant; (b) the softening zone width scales (a·eT*)^{−2/3}
   (C3(iii)'s Airy claim), derivable without new analysis from turning-point
   asymptotics. Either derivation also fixes the eigenvalue-−1 clause of R2.

3. **Log-gas seat (confidence: medium).** b and μ as screened electrostatic
   energy of the fixed profile ln(1/u)du. Bet: the equilibrium problem
   "logarithmic energy of the deficit charge against the super-Nyquist
   conductor [T*, eT*]" yields E + A = b·M ln(e^{c₀}M) with computable
   (b, c₀), and the screening constant lands at 3/π² (P1) or kills it. The
   ~20% non-additivity (law-theory §3.4, and my §5's +0.17/+0.26 dressing)
   is the interaction energy — a quantity log-gas methods are built for.

4. **Quasicrystal seat (confidence: medium-low).** The AP dichotomy (tight
   frame below Nyquist / infinite kernel above; law-theory §2.1) and the
   zero-toll of constant density are crystalline-measure facts. Bet: from
   Kurasov–Sarnak-type stability (stable polynomials/crystalline measures,
   J. Math. Phys. 61 (2020) — venue reasonably confident, UNVERIFIED here),
   ANY Fourier-quasicrystal spectrum has zero toll, so the entire envelope
   cost is attributable to aperiodic grading — sharpening "density, not
   arithmetic" to "grading, not arithmetic". Secondary: log p incommensurability
   (AG's fifth obstruction) as a Diophantine input to the fiber reduction.

5. **Proof-theory seat (confidence: low-stakes).** The cap prices Track A's
   certificate ladder: with dE/dM ≤ 4π, a certified window at RG time ℓ
   costs exp(Θ(e^{ℓ})) bits (δ < λ/‖v‖₁², Q5 law). Bet: the reverse-math
   strength map should record that windowed-positivity-to-height-T
   statements are Π₁ with certificate size doubly exponential in ln T —
   i.e. the finite fragments are feasibly checkable only to ℓ ≈ 6–7, a
   PRECISE feasibility horizon worth a line in the Track F cartography.

---

## §5 The cheap test (run; pre-registered; one worker, ~4 CPU-min total)

**Design (seed (b) made quantitative).** One block-spin/decimation step on the
smooth staircase at L = 2.485: inside [T₁, T₂] = [18, 36], replace the 4
graded zeros (k = 2..5) by equal-count constant-density (chord) positions —
the elementary move of the spliced-ladder construction. Also the reflected
(anti-averaged) configuration: same displacement magnitudes, opposite
direction. Linear response from the measured marginal law predicts
|ΔE| = (π²/2)|Σ_k ln(γ_k/t_k)| — L-independent, interaction-free baseline.

**Pre-registration** (`preregister_blockspin.log`, written before any
measurement): |ΔE(avg)| = 0.5734, |ΔE(rev)| = 0.5553; acceptance ratio
[0.65, 1.35] pass, [0.5, 2.0] qualified, else KILL.

**Honesty note — a sign slip, caught by the measurement.** The
pre-registration prose asserted the WRONG SIGN (it reasoned "zeros lower are
worth more, so E increases"; the marginal law's own convention — deletion
REMOVES a positive rank-one, so deletion raises E, so a zero's presence at
lower height LOWERS E — forces the opposite). The magnitudes and bands were
pre-registered correctly; the sign prediction was an error of this seat, and
the re-derivation is unambiguous (no free choice). Both files kept as
written; this note is the correction, in the repository's own tradition of
logging its catastrophes.

**Results** (`measure_blockspin.log`; law-theory's exact-Bessel builder,
Gcut = 840, nested m = 48/64; E = −ln λ):

| config | E (m=48) | E (m=64) | ΔE (m=64) | prediction (corrected sign) | ratio |
|---|---|---|---|---|---|
| base | 21.7712 | 21.8057 | — | — | — |
| block-averaged | 21.0978 | 21.1331 | **−0.6726** | −0.5734 | **1.173** |
| reflected | 22.4711 | 22.5046 | **+0.6989** | +0.5553 | **1.259** |

Basis stability: ΔE moves by < 0.0011 between m = 48 and 64 (differences are
basis-independent to 0.2%). E_base = 21.81 reproduces law-theory's quoted
E_total ≈ 21.8 at this L. COMPUTED.

**Verdict: PASS (both directions, inside the primary band).** The measured
marginal law acts as a genuine linear-response kernel for local, count-
preserving redistributions of the grading, with an interaction dressing of
+17% (softening direction) and +26% (sharpening direction) — quantitatively
consistent with law-theory's independently measured ~20% non-additivity.
Secondary observation: the net second-order term (ΔE_avg + ΔE_rev = +0.026
measured vs −0.018 additive) gives a small POSITIVE interaction curvature
(+0.044) along the dipole mode: the staircase is locally a strict minimum of
E against grading-preserving dipole deformations beyond first order —
consistent with the maximal-rigidity offset finding of §2.17.

Physics read: one decimation step of coarse-graining LOWERS the cost E —
the grading is measurably the operator that generates the cost, block by
block, at the marginal-law rate. This is direct support for R1, for T3's
differential form, and for the block-spin construction underlying AG-3/C1;
the pre-registered follow-up (R1 kill (b): same block at L = 2.996, predicted
first-order ΔE identical) is the cheapest next discriminator on the board.

---

*Files: `results/ias/renormalization/preregister_blockspin.py` + `.log`
(prediction, written first), `measure_blockspin.py` + `.log` (measurement).
No repository file outside `results/ias/` was modified.*

---

## Round 2 — colloquium (renormalization)

Written after reading all eight Round-1 seat files + COLLOQUIUM-BRIEF.md
(C-1…C-11). New numbers in this section are ARITHMETIC ON PUBLISHED DATA
(formulas stated inline; one verification script run, no new eigensolves);
the one genuinely new experiment is pre-registered in §R2.5 and NOT run.
Tiers as before.

### R2.1 Bet responses (every bet placed on this seat)

**FB → renorm (their §4 bet 4, conf. 0.4): "same ODE as an RG flow; 4π cap as
IR fixed point; if their beta-function fixes the factor 2, settled twice."**
LANDED, with one division of labor to record. My Round-1 §1.3 (written blind)
has the identical structure in the slope chart: g := dE/dc obeys
dg/dℓ = −(g − 4π) iff the subleading term is p·ℓ; their w-chart flow
w′ = G(w) = (2 − h(w))/(e^w w), G′(w∞) = −1, is the SAME eigenvalue in a
different coordinate (equivalence verified in R2.2 below). What I can and
cannot deliver on the factor 2: the fixed-point structure fixes the FORM
(cap value + eigenvalue −1 + pℓ subleading), but the factor 2 — why the
second epoch sweeps exactly one more deficit mass — is a matching/pricing
constant, i.e. trajectory data, and my §1.4 classification says it will NOT
come from linearization on my side. FB-2(3)'s two-constants pricing (or
RH-1(b)'s parametrix) is the right owner; I co-sign the target and supply
the regime map (R2.2), not the derivation. Their sub-bet stands unresolved,
correctly priced.

**quasicrystal → renorm (their §4 bet 1, conf. 0.70): Gauss-map
renormalization of the two-scale rate; margin dip at the Ostrowski scale for
near-Liouville ratios.** ACCEPTED — this is the cleanest new-experiment
assignment the colloquium has given this seat, and the mechanism is textbook
circle-map renormalization: their Zak fibers sample a rotation by
ln q₂/ln q₁, and frame conditioning of finite rotation orbits is governed by
the three-distance/Ostrowski structure, which renormalizes under the Gauss
map. Refinements for the experiment design: (i) tunability is real but
discrete — using prime powers, q₁ = 2, q₂ = 3^k gives rotation numbers
k·ln3/ln2, and scanning k (plus q-pairs like (2, 5), (3, 5), (2⁴, 3³) —
ratio near 1) samples a usable spread of continued-fraction types; a true
Liouville ratio is not reachable, but a large-partial-quotient ratio is
(pick (q₁, q₂) minimizing |ln q₂/ln q₁ − p/q| at small q). (ii) Prediction I
co-register with theirs: the inter-wall margin profile λ(L), plotted against
the Ostrowski expansion of the window length in units (2 ln q₁, 2 ln q₂),
dips at window lengths realizing near-coincidences of the two threshold
lattices (small three-distance gaps), with dip depth controlled by the
partial quotient; golden-type ratios give the flattest profile. Their
second bet — that I would read the chirp as an RG flow and β-linearity as
exact covariance — landed verbatim (my §1.1–1.2, written independently):
convergence, no coordination.

**log-gas → renorm (their §4 bet 5, conf. 0.3): the L ≈ 4.32 crossover is an
FHK-class freezing transition; RG on the chirp transfer operator reproduces
the drift equation.** SPLIT VERDICT. The drift equation is reproduced — but
by the action-identity algebra (SYNTHESIS §2(iii)), not by anything
FHK-specific; my R2.2 arithmetic shows the published stopping heights track
the linearized drift solution with law-theory's deformation-invariant
constants. On "freezing": the mechanism per the C-2 cluster is a variational
parameter hitting a smooth-pasting boundary — same broad family as freezing
(both are boundary-saturation of an optimizer), but the honest
discriminator is transition order and fluctuation structure, and the
measured smooth cap + C-11's single universal E-normalized profile across
the crossover favor one-saddle/smooth-pasting over saddle-exchange or
REM-style freezing. Where their FHK instinct IS vindicated: their own P5
result (linear response below sup|δN| ≈ 2, extreme-value/worst-local-deficit
functional above) is genuine measured FHK-type structure — in the ENSEMBLE
direction, not in L. I'd re-aim the bet there.

**magic-functions → renorm (their §4 bet 5, conf. 0.35): the window-extension
map as a transfer-operator flow whose fixed point is the explicit formula;
"exhibit the flow whose linearization has the 4π cap as its universal
eigenvalue."** ACCEPTED with a coordinate correction. Their fixed-point
reading is my §1.2 in dual clothes: the kernel-side statement "the ansatz
class regenerates the object" is the measure-side statement "the rescaled
deficit profile ln(1/u)du is flow-invariant" (and MF's own β_eff = 0.5034
measurement is a precision confirmation that the zeros sit ON that fixed
profile — see R2.4). The correction: 4π is not an eigenvalue of the
linearized flow; it is the fixed-point VALUE of the slope coupling, and the
linearization eigenvalue there is −1 (§1.3, R2.2). Mid-range is not a second
fixed point — it is the crossover trajectory of a marginally-driven drift.
With that substitution their bet becomes exactly the C-2 co-signed statement,
and "the bend stops being a fit question" is precisely what R2.2's residual
table starts to deliver.

**proof-theory → renorm (their §4 bet B4, low-medium): a transfer-operator
toy where the "support axiom" is the boundary condition, and no finite-rank
truncation certifies positivity while the full operator does.** ACCEPTED as
a framing, with the sharpening they'll want: in thermodynamic formalism the
positivity certificate for a transfer operator is CONE INVARIANCE (Birkhoff
contraction of a projective cone), an order-theoretic datum that no fixed
finite-rank projection preserves; Ulam/Galerkin truncations retain the
moment data and lose the cone — which is a solvable-model version of
PT-2(ii)'s "the interface forgets the load-bearing hypothesis." The natural
toy: doubling-map transfer operator, Ulam basis, explicit sign-indefinite
interface data consistent with all moment constraints. I price it at days
of writing and MEDIUM value (it illustrates F5-semantics, it does not
advance the envelope program), so I'll co-author if they drive; not my next
action.

### R2.2 Adjudications

**C-2 (the w∞ cluster) — same fact, three charts; draft statement for
co-signature.** Verified this session (arithmetic, script in shell log):
w∞ = 1 + W(1/e) = 1.27846454… satisfies e^{w∞}(w∞ − 1) = 1 exactly — the
riemann-hilbert Lambert form, the free-boundary root, and my cap coupling
are one number. The chart equivalence, in two lines: with the action
identity E + A = 2πe^ℓ·h(w), h(w) = e^w(w−1) + 1, h′ = e^w w,
(a) pinning the slope dE/dc ≡ 4π forces w′ = (2 − h)/(e^w w) = G(w) — FB's
ODE — with G(w∞) = 0, G′(w∞) = −1 exactly; (b) writing instead
E = −A′ + 4πc − pℓ gives dg/dℓ = −(g − 4π) — my slope chart, eigenvalue −1
for ANY p; (c) matching the two charts near the fixed point forces
w∞ − w(ℓ) ≍ ℓe^{−ℓ} in the relaxation regime (the secular ℓ is new small
print: eigenvalue −1 with a resonant forcing term, not pure exponential).

*Draft theorem for co-signature (tier split explicit):*
**(i) [THEOREM — algebra given the action identity]** TFAE: dE/dc → 4π;
w → w∞ = 1 + W(1/e) (unique positive root of e^w(w−1) = 1); the swept
super-Nyquist surplus → 2× the deficit mass; −D(T_s) → e^ℓ.
**(ii) [THEOREM given (i)]** w∞ is the unique positive fixed point of the
pinned-slope flow, attracting with G′(w∞) = −1; equivalently the slope
approaches 4π with unit RG rate iff the subleading term is O(ℓ).
**(iii) [CONJECTURE — the mechanism clause]** the minimizer's standoff
follows the drift branch h(w) = (b/2π)(ℓ + c₀) mid-range and relaxes onto
w∞ past ℓ* = 4π/b − c₀; the second epoch is priced 1:1 in swept mass (the
factor 2). Measured support: 4π to 0.4–1.3%; C-11's universal profile;
the residual table below. NOT derived; owners FB-2(3)/RH-1(b).
**(iv) [riders]** B_smooth not formally certified (C-11); QC-3's
horizon-merger (sharp anchored horizon = e^{w∞}T*) is a SEPARATE hypothesis
that would identify this fixed point with T1′'s constant — adjudicated by
the FB/QC slit-plane K₀ computation, which I endorse as designed and do not
prejudge. I co-sign (i)+(ii) as stated, (iii) as conjecture-with-support.

*New arithmetic contribution (COMPUTED — published w_E2 values from
agent-deep-windows.md vs the linearized drift w_drift = w∞ +
[(b/2π)(ℓ+c₀) − 2]/h′(w∞), with law-theory's deformation-invariant
(b, c₀) = (1.51, 5.04)):*

| ℓ | 0.875 | 1.2425 | 1.498 | 1.7775 | 2.0125 | 2.125 | 2.25 | 2.30 | 2.375 |
|---|---|---|---|---|---|---|---|---|---|
| w_meas − w_drift | −.0088 | −.0070 | −.0048 | −.0027 | −.0033 | −.0043 | −.0052 | −.0060 | −.0067 |

Reading: (1) all nine gate-passing stopping heights sit within |Δw| ≤ 0.009
of the linearized drift line — the mid-range clause of (iii) restated in the
w-chart (circular with the mid-range law by construction of w_E2, so this is
a COORDINATE CHECK, not independent verification; stated plainly). (2) The
residuals are U-shaped: shrinking to −0.003 mid-range (linearization error
dominates at small ℓ, where w is far from w∞), then growing NEGATIVE again
from ℓ = 2.0 to 2.375. Negative = measured w below drift = E below the
mid-range chart = exactly the bend, visible as a monotone trend in a chart
with no fitting. (3) Regime map: the drift branch reaches w∞ only at
ℓ* = 3.28 (L = 6.56), while the slope crossover is at ℓ_c = 2.28 (L = 4.56):
between L ≈ 4.6 and 6.6 the system is in mid-crossover — every existing deep
window included — and pure-relaxation behavior (w∞ − w ≍ ℓe^{−ℓ}) should
only dominate past L ≈ 6.5. Pre-registered qualitative expectation for any
future deep vectors: w approaches w∞ FROM BELOW without overshoot, residuals
vs drift growing more negative through L ≈ 5.5–6.

**C-3 (the new constant p = 4.85 ± 0.10, A′ = 16.75 ± 0.10).** Does my
one-line law reproduce them? Honest answer in three parts. (1) NO to p as a
prediction: within my §1.4 classification p is the AMPLITUDE of the −1
mode — trajectory/matching data, like b and μ — and the C4 mechanism
generates the p·ℓ FORM automatically (R2.2(c): the drift ODE with the action
identity forces a secular ℓe^{−ℓ} approach, i.e. a pℓ term in E) while
leaving its coefficient to the matching problem. The fixed point fixes
(4π, eigenvalue −1); it cannot fix p. RH-seat's measured A′-flatness at
p ∈ {9/2, π²/2} (spreads 0.074–0.095) is exactly consistency of the FORM.
(2) A discriminator my framework DOES supply: if p is grading/BK-sourced
(their challenger π²/2 — one marginal unit from the anchor zero), p is
family-universal in T*_χ units; if it is pole-sourced (their pump 4:
Fuchs index n = 4 from pole rank × parity, p = n + ½), pole-free Dirichlet
forms cap with p ≈ ½ or 5/2. One deep family ladder (q = 3, per their
pump 4) separates. My wager, stated for the record at 60/40: p is
family-DEPENDENT (amplitudes of irrelevant corrections generically absorb
local data — the pole included), against the universal-π²/2 reading; either
outcome sharpens C-3. (3) A′ − A′_Fuchs = +2.08: I endorse their
"same universality class, different determinant" as the standard RG split —
rate/exponent-form universal, prefactor constants basin-specific; the
+2-e-fold numerology stays quarantined (their K5 note, co-signed).
*The L = 5.50 triple (coordinator's discriminator): NOT yet adjudicating.*
Arithmetic on the published triple (1.9854e−64 / 1.441e−67 / 4.296e−69):
ln-decrements −7.23, −3.51, ratio 0.486 — still plunge-phase (compare the
collapse-phase signatures 0.05–0.15 at L = 4.60/4.75 before their limits
landed); a geometric extrapolation gives log₁₀λ ≈ −69.8, three decades ABOVE
the Fuchs-form band (−72.6), which mid-plunge Aitken always is. Verdict:
the triple cannot separate p = 9/2 from π²/2 or the comparator yet; the
m ≳ 200–216 rung RH-seat requested remains the decider.

**C-4 (chirp trichotomy × grading-as-marginal-operator × log-gas low-pass) —
the single mechanism statement.** The three seats' findings compose without
tension once the exponent is read as a functional of the DEFICIT MEASURE:

> **Deficit Mechanism Statement (draft for co-signature: renorm, quasicrystal,
> log-gas, free-boundary; magic-functions for the transport clause).**
> For windowed frame margins of symmetric point configurations:
> (1) the super-exponential exponent is a functional of the Nyquist-deficit
> measure dμ_L alone — E + A = Φ[dμ_L], with Φ ≈ b·M·ln(e^{c₀}M) mid-range
> and dΦ/dM capped at 4π (M = deficit mass);
> (2) configurations with NO deficit pay no exponent: periodic sub-Nyquist =
> exact tight frame (zero toll, THEOREM, law-theory §2.1); incommensurate
> unions below their Landau wall = prefactor/conditioning cost only
> (measured: ~23× across the whole inter-wall band, QC §5 — small-divisor
> physics, not deficit physics);
> (3) at fixed deficit profile, perturbations are priced by the linear-
> response kernel f(t) = (π²/2)ln(t_cap/t) — the Gateaux derivative of Φ —
> in the small-discrepancy regime sup|δN| ≲ 2, crossing over to an
> extreme-value (worst-local-deficit, surplus-non-refunding) functional
> beyond (log-gas P5);
> (4) the grading (drifting density) is precisely the operator that
> manufactures deficit at every scale; it is marginal (its rescaled profile
> is flow-invariant, §1.2), and its logs are the (ℓ + c₀) factor.
> Discreteness rider (K2): Φ's argument is the deficit measure of the
> DISCRETE configuration; density-smoothing destroys the value; nothing here
> is a bulk functional. Additivity rider (K7): the kernel is marginal only;
> global per-zero accounting still fails.

Four independent instruments now measure clause (3)'s kernel: my block-spin
dipoles (ratios 1.17/1.26), log-gas's CUE ensemble (r = 0.991, slope 0.954),
MF's β-dial phase transport (0.955–0.975 over 4–7 nats), law-theory's RUN 4
(the original). The residual second-order structure is real and now has
three measured faces to unify: my concentrated-dipole ENHANCEMENT (+17/+26%)
vs their distributed-mode slopes ≈ 0.95, log-gas's revised pair law
(W > 0 growing toward the capacity edge), and the deficit/surplus asymmetry.
Joint one-afternoon proposal (log-gas + renorm): a block-size scan of the
block-spin test (1, 2, 4, 8 zeros at matched total displacement) to measure
where dipole enhancement turns into distributed-charge response — the
finite-wavelength structure of Φ's Hessian.
*Also resolved into the statement:* QC's restored-glide finding
(incommensurability alone glides, no archimedean place) — see my retraction
in R2.4; and their trichotomy column (ii) is clause (2)'s measured content.

**The κ-family capacity result vs FB's MRS/balayage route — can they prove
t_cap = (1+κ)^{1/κ}·T*? YES, and it is a one-page corollary of their FB-1.**
Their constrained-sweep formalization determines the endpoint by exactly the
mass condition ∫_{T*}^{A}(ρ − a/π)dt = deficit mass; for ρ_κ ∝ t^κ that
equation IS my η^{κ+1} = (κ+1)η computation (§2 R3(i), verified to 8
digits), giving A = (1+κ)^{1/κ}T*. Two structural notes for their proof:
the LEFT edge stays soft for every κ > 0 (in u = ln t the constraint density
vanishes linearly at u* with slope ∝ κ — their "degenerate/marginal"
left-junction analysis carries over verbatim), and the RIGHT edge stays
mass-determined. Assignment I propose and accept my half of: FB owns the
Dragnev–Saff/BKMM equilibrium proof at general κ; I own the family design
and the universality conjecture R3(ii); and their G(t₀) potential-gap test
gains a one-parameter battery — if worth = potential gap, it must hold at
every κ with capacity (1+κ)^{1/κ}, a far sharper kill than one grading.

**C-1 (rigidity trichotomy) — one paragraph, offered not owned.** The three
reductions agree at linear order and differ at second: QC-chaos's I_w is the
charge functional ∫δN d(marginal kernel); MF's β_eff is the same charge in
a one-parameter chart (a uniform phase β − ½ produces δN ≈ const, and
β_eff = 0.5034 says the zeros' charge is ~0); log-gas's spectral gap below
ln 2 is the MECHANISM that makes ζ's charge vanish (no Fourier content where
the kernel's window lives). Separating example for the second order: a
configuration with large δN oscillating entirely above ln 2 — zero charge,
zero β_eff shift, zero gap violation, but nonzero quadratic cost. So: one
statement at linear response; three inequivalent refinements beyond. The
trichotomy should be co-stated as "charge = phase = gap-filtered discrepancy
(first order), with the Hessian unresolved" — the same Hessian the C-4
block-size scan probes.

### R2.3 Merges (two, with division of labor)

**MERGE A — the κ-graded laboratory ladder (renorm + free-boundary +
riemann-hilbert + quantum-chaos + log-gas).** One-parameter family of
solvable-side labs between the FF lattice (κ-degenerate) and ζ (κ → 0):
power-graded staircases with exact capacity endpoints (1+κ)^{1/κ}·T*.
Deliverables and owners: (i) capacity-family theorem via constrained sweep —
FB (proof), renorm (family design + the exact endpoint formula, done);
(ii) pre-registered marginal-worth scans at κ = 1 and κ = ½ — renorm
(instrument + runs; pre-registration in R2.5), log-gas (ensemble variant at
κ = 1: does the linear-response/extreme-value crossover sit at the same
sup|δN| ≈ 2?); (iii) parametrix/secular evaluation of the worth profile at
κ = 1, where the density is polynomial and the equilibrium problem is
classical — riemann-hilbert (their RH-3 machinery, easier first case than
the log grading); (iv) the Selberg instantiation memo (κ = 1 IS the Weyl law
of a hyperbolic surface; positivity a theorem modulo small eigenvalues;
windowed Selberg positivity as a theorem-calibrated detector) —
quantum-chaos (trace-formula bookkeeping), renorm (frame semantics).
Value: adjudicates π²/2-universality (the sharpest open edge of C-4), hands
T4 a solvable first case, and adds a second solved-side calibration world
with grading but no arithmetic mystery.

**MERGE B — the Deficit Functional lemma (renorm + log-gas + quasicrystal +
free-boundary, with HA's T4 as the identity layer).** Promote the C-4
mechanism statement (R2.2 box) to a lemma program: Φ is Gateaux-
differentiable at graded configurations with kernel (π²/2)ln(t_cap/t)
(clauses: L-invariance of redistribution response — renorm, R1; ensemble/
variance form and the sup-deficit crossover — log-gas, LG-1/LG-3 revised;
zero-deficit column with polynomial conditioning — quasicrystal, QC-1;
worth = potential-gap identity G(t₀) — free-boundary, FB-1(ii); rank-two
secular identity underneath everything — HA/T4, cite not redo). First
falsifiers already scheduled: my L = 2.996 block-spin invariance test, their
G(t₀) finite sum, the C-4 block-size scan. This merge is deliberately the
theorem-shaped consolidation of what four instruments already measure.

### R2.4 Updates (kills, retractions, strengthenings)

1. **Partial retraction (§1.6 slogan).** "The archimedean place is the
   continuum limit of RG time; the digamma is what makes the flow
   lattice-free" — REFINED after quasicrystal's P-B (glide restored by two
   incommensurate lattices, no archimedean place): the correct criterion is
   the DENSITY OF THE GENERATED SCALE GROUP. One lattice (FF): discrete
   scale invariance, devil's-staircase margin. Two incommensurate scales:
   the group is dense, the Zak reduction fails, the margin moves
   continuously. ζ has BOTH a dense prime-scale group AND the archimedean
   continuum — the digamma is sufficient, not necessary, for the glide.
   P4's wobble-audit criterion survives in sharpened form: log-periodic
   wobble requires a single preferred lattice; ζ's envelope wobble-freedom
   through 70 orders excludes preferred-scale candidates, but incommensurate
   multi-scale candidates are NOT excluded by smoothness alone.
2. **Round-1 bet scorecard (this seat's own bets, graded honestly).**
   FB/smooth-fit: substantially landed (exact chain + G′(w∞) = −1 delivered;
   factor 2 still open — correctly, per my amplitude classification).
   RH/p = n + ½ and Airy: on track (p = 4.85 ± 0.10 measured; 9/2 vs π²/2
   open). Log-gas/screened-energy derivation of b: NOT attempted in Round 1
   (they went ensemble-direction, productively); request renewed — the
   screened electrostatic energy of the fixed profile ln(1/u)du remains, to
   me, the most plausible home for b = 3/2 (P1 unchanged, SPECULATION).
   Quasicrystal/zero-toll: my strict form was WRONG (constant-density
   aperiodic toll is polynomial, not zero — their measured 23×); the
   exponent-level form ("no deficit ⇒ no super-exponential toll") is
   confirmed and is now clause (2) of the C-4 box. Proof-theory/certificate
   pricing: landed independently (their PT-3).
3. **Strengthening (§1.2, via magic-functions).** MF's β_eff = 0.5034 is a
   precision measurement that the zeros sit ON the flow-invariant profile
   (mean-zero discrepancy in the marginal-kernel window), while the
   λ-OPTIMUM of the naive class is bang-bang at the class boundary. Two
   consequences adopted: (a) my P5 sharpens — "self-tuned criticality" means
   the zeros sit at the fixed profile, NOT at the λ-maximum; the slogan
   "maximally rigid offset" should be read "fixed-profile (balanced)
   offset" program-wide; (b) any "zeros as λ-extremizers" story is dead on
   their data (their consequence 3), which my framework never needed and
   now explicitly disclaims.
4. **Strengthening (R1).** Three independent instruments now validate the
   marginal kernel as linear response (block-spin 1.17/1.26; CUE ensemble
   0.991/0.954; β-transport 0.955–0.975). R1's kernel clause is upgraded
   from "supported by one test" to "supported by three instruments, with a
   measured second-order discrepancy (dipole enhancement vs distributed
   slopes) assigned to the C-4 block-size scan." The L-invariance follow-up
   (kill (b)) stays pre-registered as written.
5. **Strengthening (R2).** The C-2 chart equivalence and the drift-residual
   table (R2.2) fold into R2's statement (ii); C-11's universal
   E-normalized profile across the crossover is adopted as vector-level
   support for the one-saddle/smooth-pasting reading (and I note C-11's
   30%-of-E-below-T* number as a warning against reading the action
   identity as a POINTWISE action density — it is zone bookkeeping only).

### R2.5 Next action (single, sized) — pre-registered here

**Execute Merge A(ii), first rung: the κ = 1 (Weyl-graded) marginal-worth
scan.** Instrument: ten-line generalization of law-theory's
`law_core.staircase_zeros` to N_W(T) = (T/T₀)² (zeros t_k = T₀√(k − ½));
frame builds at m = 48/64 (nested), dps 50, Gcut ≈ 2.5·t_cap. Configuration
(fixed now): a = 0.62125 (L = 2.485 for comparability), T₀ = 2π√5/a ≈ 22.62,
giving T*_W = aT₀²/2π ≈ 50.6 (from N′(T*) = a/π), deficit mass
M = (aT₀/2π)² = 5, predicted capacity t_cap = 2T*_W ≈ 101.2. Runs: base λ +
single-zero deletions at k = 1, 2, 3, 5, 7, 9, 12, 15, 18, 21 (t_k ≈ 16 to
102). Size: ~half a day including the instrument edit; ≤ 45 CPU-min, one
worker.

**Pre-registered predictions (logged here, before any code is written):**
- P1 (endpoint): deletion worth < 0.05 for zeros beyond 2·T*_W (κ = 1
  capacity), with the support edge at 2T*_W ± 10% — NOT at e·T*_W ≈ 137
  (log-grading value). Discriminates balayage semantics per grading.
- P2 (universality): plateau ratio f(t_k)/ln(2T*_W/t_k) = π²/2 ± 10% for
  t_k ≤ 0.6·t_cap (basis/truncation drift controlled to ≤ 3% as in RUN 4).
- P3 (edge): softened profile (ratios falling to ~0.5 and below) in the
  last e-fold... stated for κ = 1 as t ∈ (0.6, 1)·t_cap, same shape as the
  log-grading edge.
- KILL: P2 failing (plateau off π²/2 by > 10% with drift controlled) kills
  R3(ii)'s grading-universality — the marginal constant would be
  log-grading-specific, the first evidence that anything in the value law
  is special to the RvM class, and Merge A's theory items re-aim at WHY.
  P1 failing kills the balayage/capacity semantics outside κ → 0 and sends
  FB-1's generalization back to the drawing board. Either failure is a
  finding; success hands T4 a solvable proof target at κ = 1.
