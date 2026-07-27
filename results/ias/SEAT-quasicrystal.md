# SEAT — Aperiodic order and crystalline measures

IAS panel, Round 1 (independent; no other SEAT file read). Date: 2026-07-26.
Honesty tiers used throughout: THEOREM / COMPUTED / CONJECTURE / SPECULATION.
One pre-registered computation was run for this seat (§5); predictions were
logged in `results/ias/quasicrystal/prereg.md` BEFORE execution, and the raw
log is `results/ias/quasicrystal/two_scale_test.log`.

---

## §0 Seat card

Toolkit: crystalline measures and Fourier quasicrystals (Guinand, Meyer,
Lev–Olevskii, Olevskii–Ulanovskii, Kurasov–Sarnak, Alon–Cohen–Vinzant);
cut-and-project schemes / model sets and diffraction theory (Hof, Baake–Grimm);
density theorems for exponential systems (Beurling, Landau, Beurling–Malliavin,
Seip); annihilating/uniqueness pairs and quantitative uncertainty (Benedicks,
Amrein–Berthier, Nazarov, Logvinenko–Sereda/Kovrijkine); summation formulas
beyond Poisson; Lee–Yang/stable-polynomial technology (Asano contraction,
Borcea–Brändén preservers).

---

## §1 Translation

### 1.1 The zero comb is the founding crystalline measure, and λ(L) is its finite-window revelation depth

Under RH the symmetric ordinate comb μ_ζ = Σ_γ (δ_γ + δ_{−γ}) (multiplicity
counted) has, by the explicit formula in exactly the repo's §6 normalization,
distributional Fourier transform

  μ̂_ζ = [atoms of weight −(1/π)Λ(n)n^{−1/2} at ±log n] + [a.c. background:
  pole cosh(u/2)-term + the transform of the archimedean density],

i.e. μ_ζ is *crystalline modulo an explicit absolutely continuous background*:
locally finite support, countable closed spectrum {±log n}. This is not an
analogy but the historical origin of the subject: Guinand (Acta Math. 101,
1959) built the first nontrivial crystalline measure from precisely this
formula, and Meyer (PNAS 113 (2016), 3152–3158) reintroduced it as the
motivating example of the modern theory. Dyson's well-known proposal (Notices
AMS 56 (2009), "Birds and Frogs") — classify one-dimensional quasicrystals and
find the zeta comb in the list — is the folklore anchor of this seat.

Where ζ sits in the taxonomy, said precisely (this placement matters):

- μ_ζ is NOT translation-bounded (≈ log T atoms per unit interval at height
  T): it escapes the hypotheses of every classification theorem in the field.
  Lev–Olevskii (Invent. Math. 200 (2015), 585–606: uniformly discrete support
  AND spectrum ⇒ finite superposition of lattice combs) does not apply
  (spectrum {±log n} has gaps → 0, support density grows). The unit-mass
  characterizations (Olevskii–Ulanovskii, C. R. Math. 358 (2020); Kurasov–
  Sarnak, J. Math. Phys. 61 (2020) 083501; Alon–Cohen–Vinzant: every
  one-dimensional N-valued Fourier quasicrystal arises from the Kurasov–
  Sarnak Lee–Yang construction — arXiv:2403.08659 and companion papers,
  scope of the 1D converse UNVERIFIED by me at citation level) also do not
  reach it. **The zeta comb sits in a hole of the classification: positive,
  atomic-dual-mod-a.c., growing density.** The program is, whether it says so
  or not, doing quantitative structure theory in that hole.

- Weil positivity in diffraction language: for a POSITIVE measure μ the
  windowed form Q_L(φ) = ∫|φ̂|² dμ ≥ 0 is trivial. The content of RH is the
  converse direction: the arithmetically prescribed dual data (primes + pole
  + archimedean term) must be the Fourier side OF a positive measure on the
  real line. **RH = realizability of a prescribed diffraction pattern** — the
  crystallographic inverse problem (compare Córdoba's Dirac combs, Lett.
  Math. Phys. 17 (1989)). The Π₁ asymmetry is native here: a non-realizable
  pattern is refuted by one finite window (a negative eigenvalue); realizable
  ones are certified only in the limit.

- The uniqueness-pair dual of the program's pairing already exists as a
  theorem: Bondarenko–Radchenko–Seip, *Fourier interpolation with zeros of
  zeta and L-functions*, Constr. Approx. 57 (2023) 405–461 (arXiv:2005.02996):
  a nice even analytic function is RECOVERABLE from its values at the ζ
  ordinates plus its Fourier transform's values at ±log n. The repo's
  λ(L) > 0 is the frame-quantitative, window-truncated version of exactly
  this recovery statement; the envelope law is its condition-number asymptotics.
  (Cross-seat: the magic-functions seat will know the BRS kernel; see §4.)

Seed question (a) — is there a quantitative theory of finite-window
certification of crystalline measures? **Answer: no unified theory exists, to
this seat's knowledge (absence claim, standard UNVERIFIED caveat).** The
fragments that exist, each covering one degenerate column:

1. constant density on an interval = Landau–Widom / Fuchs eigenvalue
   asymptotics (Fuchs 1964; Landau–Widom 1980) — the program has already
   correctly identified its deep-regime 4π cap as this physics;
2. finitely many frequencies = Turán–Nazarov lemmas;
3. model sets: diffraction of finite patches converges (Hof, Comm. Math.
   Phys. 169 (1995); Baake–Grimm, *Aperiodic Order* I, CUP 2013), with rates
   only via discrepancy in special (bounded-remainder-window) cases
   (UNVERIFIED as a general statement);
4. LP/SDP certificates of infinite positivity statements (Cohn–Elkies
   tradition) — powerful, but with no decay-rate theory in the window size.

The program's measured objects — the invariant law E(L) = −A + b[N(T*) +
μD(T*)], the 4π saturation, the T*_χ family collapse, and the certified
rungs — constitute the first quantitative data set for the missing column:
**the revelation-rate law of a chirped crystalline measure**. In my field's
words: how slowly a Fourier quasicrystal reveals its positivity to a finite
window, when its density drifts. I consider this the program's most exportable
product into aperiodic order, independent of anything it ever proves about RH.

### 1.2 The function-field lab is Lee–Yang, literally — and the dictionary has a measured new row

The Kurasov–Sarnak construction: P a Lee–Yang polynomial in n variables,
ω ∈ ℝ₊ⁿ; the zero set of x ↦ P(e^{iω₁x}, …, e^{iωₙx}) is the support of a
Fourier quasicrystal with spectrum in ℤω₁ + … + ℤωₙ. Dictionary
(THEOREM-level correspondence, assembled here):

| n (variables) | Lee–Yang object | point set | program object |
|---|---|---|---|
| 1 | unitarized L-polynomial p_C(z) = Π(z − e^{iθ_j}) | Γ_C: periodic, 2g atoms per period 2π/ln q | the curve lab (PLAN-algebraic-geometry); RH_C ⟺ p_C Lee–Yang |
| finitely many, incommensurate | product Π_i p_{C_i}(z_i) — reducible LY | union of periodic sets, genuine quasicrystal | **the two-scale lab (§5, new)** |
| countably many: ω = (log 2, log 3, log 5, …) | "Euler object" on 𝕋^∞ — NOT a polynomial; stability = RH | ζ ordinates as the Kronecker-line cut | the real thing |

Three consequences of reading the table:

(i) **RH for curves IS the Lee–Yang property** (all inverse roots on
|z| = √q ⟺ the unitarized polynomial has all zeros on the unit circle), and
the Weil/Hasse positivity proof is the arithmetic sibling of the Lee–Yang
circle theorem. The program's "fifth obstruction" (ℚ-linear independence of
{log p} kills the Zak reduction; PLAN-algebraic-geometry §1.4 item 4) is, in
this seat's language, exactly the **crystal → quasicrystal transition**: one
frequency = periodic = linear algebra; several incommensurate frequencies =
genuinely aperiodic. The transition can be entered ONE STEP at a time —
two curves over multiplicatively independent q — and that minimal step was
never measured. §5 measures it.

(ii) What transplants back from the curve rows: the wall 4g·ln q and reduced
wall 2(2g−2)·ln q are pure Landau density statements (wall = 4π × density,
verified: 4g ln q = 4π·(g ln q/π)); the flat staircase = the zero-toll/AP
dichotomy (law-theory §2.1 = AG-3(i), converged independently). What does NOT
transplant and is now measured (§5): the union of two incommensurate curve
sets is complete essentially to its combined Landau wall, its margin is O(1)
deep past both individual walls, and it GLIDES (strictly decreasing, no flat
rungs). So the AG seat's "no archimedean place ⇒ no glide" is a statement
about periodicity, not about function fields: **incommensurability alone
restores the glide.** COMPUTED, pre-registered, §5.

(iii) The measured CONTRAST is the sharpest new datum: between its walls the
two-frequency quasicrystal's margin decays by ~1.4 orders TOTAL (0.66 → 0.028
over L = 9 → 13.5), while ζ's margin decays super-exponentially (35+ orders
over a comparable window fraction). At constant density, incommensurability
is CHEAP — completeness costs O(1)-to-polynomial, a small-divisor price. The
super-exponential envelope is therefore priced entirely by the CHIRP (the
drifting density), not by aperiodicity: this refines the law-theory verdict
"the margin is a discreteness effect and a chirp effect" with a controlled
experiment where discreteness and aperiodicity are present but chirp is
absent. Taxonomy, one line each:
  crystal (1 freq): staircase, wall, zero toll [THEOREM, AG-1];
  quasicrystal (finitely many freqs): positive to the Landau wall, glide,
  polynomial-scale toll [COMPUTED, §5; CONJECTURE as a theorem, QC-1];
  chirped crystal (ζ): super-exponential toll b[N + μD], 4π cap [MEASURED].

### 1.3 The Hard Horizon as an annihilating pair, and whether (e, e²) is right

T1′ (kernel-checked in the staircase form) says: (interval [−a,a]; staircase
head up to T̃) is a uniqueness pair for ANCHORED functions once
T̃ > e²T*·e^{ε*}. Placement against the field's uncertainty results:

- It is NOT a Benedicks/Amrein–Berthier situation (both those need two sets
  of finite measure / the finite-count case is classical); the head is a
  finite set, so unanchored uniqueness fails identically — the T1′ §1.4
  counterexample is the standard one, correctly deployed.
- The anchor Hypothesis A is the interesting object, and my field has a name
  for its ceiling: the **Cartwright log-integral budget**. For F = φ̂ of
  exponential type a with ‖F‖₂ = 1, ∫ log⁻|F(t)|/(1+t²) dt < ∞ always, but
  NOT uniformly in φ: mass parked at height T with a Gevrey-2 profile makes
  |F| ~ e^{−c√T} on the anchor band. So Hypothesis A cannot be discharged for
  free; it is genuinely a statement about near-minimizers (mass location),
  exactly as T1PRIME Gap 1 says. What my field adds: the de-anchoring ceiling
  for compactly supported unit functions is quasi-analytic, exp(−Θ(√T̃)) —
  so the true gap between "anchored with κ = O(1)" and "worst case" is
  exp(−ca) vs exp(−c√T̃) = exp(−c·e^{a+1}); any mass-location lemma putting
  Θ(1) of the minimizer's L² mass below C·T* closes most of that gap. (Route
  logged in QC-2.)
- **Is e² the right constant? Field prior: the disk is the wrong domain, so
  probably not sharp.** The e-horizon is a balayage/equilibrium constant (the
  NT Round-2 identity — super-Nyquist surplus on [T*, eT*] = deficit mass —
  is a textbook balayage statement, and I endorse it as exact). The e²-horizon
  comes from Jensen on a DISK of radius T̃: the circle average pays type
  (2/π)aρ along the whole circle, weighting heavily the arcs where nothing
  forces F to be large. The classical repair (Beurling–Malliavin, Koosis,
  *The Logarithmic Integral*) is to run the two-constants/harmonic-measure
  argument in the slit plane ℂ ∖ {|x| ≥ T̃ on ℝ}, where the zeros sit on the
  boundary-adjacent segment and their Green potential seen from the anchor is
  LARGER. Every experience with this substitution says the disk constant is
  lossy. CONJECTURE (QC-3): the sharp anchored horizon is the value of an
  explicit slit-plane equilibrium problem, strictly below e². Two live
  hypotheses for its value: (H-e²) HA's Gap-2 construction really does reach
  e^{2−δ}, and e² is sharp after all; (H-merger) the sharp constant is
  e^{w∞} = 3.594 (w∞ the root of e^w(w−1) = 1) — in which case the hard
  horizon and the C4 variational standoff are ONE height and the two-horizon
  picture collapses into a single balayage geometry. The measured stopping
  heights (3.14–3.41·T*, drifting UP toward 3.59 with L) are consistent with
  the merger and give it more than aesthetic support. Either resolution is a
  theorem worth having; the computation is days-to-weeks for the free-boundary
  seat jointly with HA (§4, bet 2).

### 1.4 Seed (d): rescaling, cut-and-project, and what the family collapse is

The honest negative first: no rescaling makes the zero set a Meyer set or
model set. The unfolding γ ↦ N(γ) produces constant density 1 but destroys
the atomic dual (a nonlinear time change chirps the prime frequencies:
exact atoms at log n exist ONLY in the original variable, where the density
grows). This is intrinsic, not an artifact: **the zeta comb is a chirped
crystal** — a measure whose Bragg structure and whose constant-density
representation live in different coordinates, connected by the exponential
map. law-theory's "the ζ margin is a chirp effect" is the same fact seen
from the value side.

What survives is better than almost-periodicity: a cut-and-project reading
with internal space the adelic solenoid. The Kronecker line x ↦ (x log p)_p
in 𝕋^∞ is the internal orbit; under RH the ordinates are the cut of that
line against the "Euler divisor". The family measurement then has a clean
CPS meaning: T*_χ = (2π/q)e^{L/2} says all Dirichlet families are sections
of ONE adelic scheme with the conductor acting as window volume — one
internal geometry, different windows. SPECULATION as structure, but it makes
a falsifiable prediction this seat registers now: for GL(2)/Δ (Ramanujan),
density (2/2π)log T ⇒ the collapse variable must be e^{L/4}, not e^{L/2} —
which is exactly NT's Q9 experiment. If Q9 lands on e^{L/4}, the CPS/window
reading gains a second family; if not, it dies. (Agreed target, no credit
claimed — the point is that two seats reached it by different roads.)

---

## §2 Candidates

### QC-1 (The two-scale completeness theorem: what incommensurability buys, with rate)

**Statement (CONJECTURE, now with pre-registered numerical support).** Let
Γ = Γ_{C₁} ∪ Γ_{C₂} for curves over F_{q₁}, F_{q₂}, log q₁/log q₂ irrational
(Diophantine class σ). Let L_w = 4(g₁ ln q₁ + g₂ ln q₂) (the Landau wall of
the union). Then:
 (i) λ_Γ(L) > 0 for every L < L_w — completeness up to the density bound,
     though each constituent is past its own wall;
 (ii) λ_Γ is strictly decreasing between consecutive thresholds
     {2n ln q_i} on (max individual wall, L_w) — the glide, restored by
     incommensurability with no archimedean place;
 (iii) quantitatively, −ln λ_Γ(L) ≲ C(σ)·ln(1/(L_w − L)) + small-divisor sums
     of the rotation number ln q₂/ln q₁ (Ostrowski/three-distance expansion) —
     polynomial-scale, NOT exponential: the toll of aperiodicity at constant
     density.

**Measured support (§5, pre-registered):** λ = 0.656 at L = 9.0 (both curves
past-wall by ≥ 1.2; m- and H-drift ≤ 1.2%, 0.0%); strict decrease 58% across
the threshold-free band [8.0, 9.5] with the single-curve control flat to
7 digits; decay only ~1.4 orders total by L = 13.5; collapse consistent with
0 past L_w = 14.22.

**Proof route.** Zak-fiber the union along one lattice; the second set enters
each fiber as samples of a circle rotation; frame bound via quantitative Weyl
(Erdős–Turán) + Avdonin-style "1/4 in the mean" perturbation of the fiber
frames; alternatively via Levin/Seip generating-function machinery for
finite unions of shifted lattices. (i) may partially exist in the universal-
sampling literature (Olevskii–Ulanovskii, *Universal sampling…*; diligence
task); (ii)–(iii) are, to my knowledge, open as stated.

**Effort.** (i) weeks (or a literature hit); (ii) weeks; (iii) months.
**Interfaces.** AG seat (the lab and exact fibers); HA (Avdonin/Levin);
renormalization seat (the rate in (iii) should renormalize under the Gauss
map of ln q₂/ln q₁ — their cleanest possible entry point into the program);
log-gas (the union at its wall as a two-component incommensurate lattice gas).
**Kill criteria.** Already survived its pre-registered kill test (§5: flat
rungs or collapse at L = 9 would have killed it). Remaining: if a converged
positive margin appears PAST L_w, the Landau bookkeeping is wrong and (i) is
misstated; if the decay in (iii) turns out exponential in 1/(L_w − L), the
small-divisor mechanism is wrong (that outcome would itself be a finding —
it would mean aperiodicity is expensive even at constant density, weakening
the "chirp owns the envelope" reading of §1.2(iii)).

**Program value.** The minimal world with the fifth obstruction ON: it
isolates and prices the one mechanism (incommensurability sustaining
positivity between walls) that ζ must use at every scale, in a setting where
every quantity is still algebraic. It also hands Track E a constraint: any
"tower over the primes" (PROGRAM.md Addendum) adds one frequency at a time —
QC-1 is the n = 2 rung of that tower, and its rate function C(σ) is the first
measurable "growth inequality" datum.

### QC-2 (The anchored pair, rearranged: dodging past the horizon costs the envelope scale)

**Statement (THEOREM-level: a rearrangement of the proved T1′, not new
analysis).** Under (S1), (S2), (S3) of T1PRIME.md with τ = 2a + 2 + δ,
δ > 0, every unit φ satisfies

  sup_{|x₀| ≤ 2π} |φ̂(x₀)| ≤ exp( −[ 2δe^{2a+2} − 2R(2a+1+δ)
      − (4 + 2/π)a − ½ln(2a) ] ).

I.e.: the pair (interval; staircase head through e^{2+δ}T*) is a strong
annihilating pair relative to the anchor band [−2π, 2π], with constant
exp(−2δe^{2a+2}(1 − o(1))). Proof: run the existing L4→L7→L5→L6 chain keeping
−ln|G(0)| as the unknown instead of τ; one rearrangement of T1PRIME §3.

**Why it matters.** The de-anchoring cost 2δe^{2a+2} = (2e²δ)·e^{2a} and the
envelope's deep rate 4π·e^{2a} are the SAME scale (2e² = 14.78 vs 4π = 12.57):
past the hard horizon, anchor mass collapses at exactly the super-exponential
scale the margin itself lives on. This puts the two-horizon picture and the
envelope into one uncertainty budget, and turns Gap 1 (anchor for minimizers)
into a quantitative tradeoff: a near-minimizer that de-anchors to dodge must
pay ~e² per unit of dodge beyond e²T*, while dodging earns at most the
balayage rate — a bookkeeping route to proving near-minimizers are anchored
(compose with a mass-location lemma: Θ(1) L²-mass below C·T*, which is the
measured behavior of every stored minimizer).

**Effort.** Days for the paper form; the Lean form is a light edit of
`lean/glide/Glide/HardHorizon.lean` (same lemmas, different final
rearrangement) — the cheapest new kernel-checked theorem available to the
program. **Interfaces.** HA (owns T1′), Lean/proof-theory seat (artifact),
DG (measure the anchor decay of stored deep minimizers past their stopping
height against the 2e²δ rate — a fit-free test). **Kill criteria.** None for
the statement (it follows from proved material); the INTERPRETATION dies if
measured minimizer anchors decay slower than any e^{−cδe^{2a}} beyond the
stopping height.

### QC-3 (The sharp anchored horizon is a slit-plane balayage constant; is it e² or e^{w∞}?)

**Statement (CONJECTURE with an explicit computation attached).** Define
κ*(a) = sup{ T̃/T* : ∃ unit φ, anchored with κ = O(1), F vanishing on the
staircase head through T̃ }. Then lim_{a→∞} κ* exists and equals the value of
an explicit equilibrium problem: maximize the balayage of the head's Jensen
mass against type-a growth, computed in Ω = ℂ ∖ {|x| ≥ T̃} (harmonic measure/
two-constants), not in the disk. Deliverable-sized sub-statements:
 (i) [upper bound improvement] replacing L5–L6's disk Jensen by the slit-plane
     Green potential yields κ* ≤ K₀ < e² with K₀ explicit (a one-page
     equilibrium computation once the Green function bookkeeping is set up);
 (ii) [lower bound] the BM-window construction of T1PRIME Gap 2 gives
     κ* ≥ e^{2−δ} … OR stalls at the same K₀ — whichever way this goes
     decides between (H-e²) and (H-merger) of §1.3;
 (iii) [merger test, fit-free] if K₀ = e^{w∞} = 3.594, the hard horizon and
     the C4 standoff coincide, and the eleven measured stopping heights
     (3.14 → 3.41, increasing in L) are converging to the HARD horizon, not
     hovering below a variational one.

**Proof route.** Standard potential theory: harmonic measure of the slit
plane (explicit via the Joukowski map), the head's counting function as a
boundary charge, balayage onto the slit; the NT Round-2 identity (surplus on
[T*, eT*] = e^ℓ) is the first moment of the same charge and calibrates the
setup. **Effort.** (i) days–weeks; (ii) is HA's existing Gap-2 program;
(iii) free once (i) lands. **Interfaces.** free-boundary seat (this is their
native machinery — the obstacle-problem/balayage formulation; also the
(eT* − t)^{3/2} softening at the capacity edge should fall out as the generic
free-boundary exponent), HA, DG (C4). **Kill criteria.** If the slit-plane
computation returns K₀ ≥ e²(1 − o(1)), the disk was not lossy, (H-merger)
dies, and e² stands — a clean negative worth recording. If K₀ < 3.4, it
contradicts measured stopping heights and the setup has a bug (oracle:
stopping heights are data).

---

## §3 Intuition pumps (all SPECULATION, labeled)

**IP-1: RH as infinite-variable Lee–Yang, and UPT as Asano contraction.**
The one world where an RH-type statement is proved by induction on sites is
Lee–Yang theory: the circle theorem is proved by ASANO CONTRACTION — a local
surgery that adds one site while preserving stability. The Borcea–Brändén
classification (J. Amer. Math. Soc. 22 (2009); Invent. Math. 177 (2009))
characterizes ALL linear operations preserving stability. UPT asks: transfer
positivity from Q^{(≤p)} to Q^{(≤p′)} — one prime at a time. If the per-prime
step could be exhibited as (the quadratic-form shadow of) a stability-
preserving operation on a torus function with one new variable z_p, the
induction would close by classification rather than by estimate. Two concrete
handles the repo already owns: (a) the sign ledger — the arithmetic all-plus
signing being the UNIQUE positive signing (GT G4(A), 1-of-32) is exactly the
FERROMAGNETIC hypothesis of Lee–Yang (the circle theorem fails for
antiferromagnets; the wrong signings fail at O(1)); (b) the pole flip — the
pole term is what makes ζ's couplings ferromagnetic (§2.11), i.e., the
partition-function reading assigns the pole the role of the external-field
normalization. First falsifiable step: write the truncated form's prime part
as a restriction of a multi-affine symbol on 𝕋^{π(e^{L/2})} and check whether
the p-step is Grace–Walsh–Szegő-representable; a NO is cheap and kills it.

**IP-2: phason stiffness.** In quasicrystal physics, a finite patch admits
phason deformations invisible to windowed observables; λ(L) is precisely the
phason stiffness of the zero set at scale L, and the envelope law says the
stiffness of the chirped crystal is exp(−b[N + μD]). The Poisson penalty
(1.5–2 orders) is random-tiling phason entropy; the maximal-rigidity offset
of the true zeros says the zeta "tiling" is at its zero-temperature,
perfectly ordered point (log-gas seat's language will differ; §4 bet 3).
The 4π cap is the stiffness saturating at the free (Fuchs/prolate) edge.

**IP-3: the adelic window ledger.** If the family collapse in T*_χ is one
adelic CPS with conductor = window volume (§1.4), then "conductor, parity,
pole enter only the offset" is the CPS statement that window SHAPE never
changes the revelation rate, only its calibration — and the GL(2) run (Q9)
is the next section of the same scheme. A CPS-native derivation of the
offset's parity dependence (ψ(1/4) vs ψ(3/4) dips) would be the first
structural, non-fitted constant in the program.

---

## §4 Cross-seat bets (ranked by confidence)

1. **Renormalization seat (0.70).** The two-scale rate (QC-1(iii)) is a
   function of the continued-fraction expansion of ln q₂/ln q₁ and
   renormalizes under the Gauss map: badly approximable ratios give the
   SLOWEST margin decay between walls; a near-Liouville pair (e.g. tune q₂
   so ln q₂/ln q₁ has a huge CF coefficient) shows a measurable margin dip
   at the corresponding Ostrowski scale. One afternoon on the §5 instrument
   settles it. Additional bet: they will read the chirp (§1.4) as an RG flow
   in log-height and the β-linearity/family collapse as exact covariance.

2. **Free-boundary seat (0.55).** QC-3: the slit-plane computation lands
   K₀ < 6 (strictly inside e²); conditional sub-bet at 0.25: full merger
   K₀ = e^{w∞} = 3.594. Second bet, independent: the (eT* − t)^{3/2}
   capacity-edge softening measured by law-theory is the generic obstacle-
   problem free-boundary exponent and they will derive it in a page from
   C4's formulation.

3. **Log-gas seat (0.55).** The rigidity-offset ordering true ≈ smooth <
   GUE < Poisson (in −ln λ) matches one-component-plasma energy-fluctuation
   ordering, and the pending Q6 GUE point lands within ~2 nats of the smooth
   staircase (inside the DG-P3/NT-P2 bands) — i.e., the offset is a number-
   variance functional, nothing finer (consistent with §2.17 and T3).

4. **Quantum-chaos seat (0.45).** The Poisson penalty is ≈ c·√(N(T*) ln N)
   nats (number-variance scaling), hence GROWS slowly with L rather than
   staying the constant "1.5–2 orders" — testable at L = 3.6/4.0 with the
   existing model_zeros instrument; they will phrase the 4π cap as the
   Heisenberg/Ehrenfest saturation of the window's form factor.

5. **Magic-functions seat (0.40).** The Bondarenko–Radchenko–Seip kernel
   (§1.1) is the analytic continuation of the program's dual witnesses: the
   NNLS atoms (14.079/weight 2.047) are finite-m shadows of BRS residues,
   and the norm growth of the BRS interpolation basis along the frequency
   ladder encodes (b, μ). If they can compute one BRS basis-function norm
   at Nyquist height T*, it should reproduce the marginal law's
   (π²/2)ln(eT*/t) profile.

---

## §5 The cheap test (run; pre-registered; ≤ 2 CPU-min)

**Protocol** (full pre-registration in `results/ias/quasicrystal/prereg.md`,
written before execution; script `two_scale_test.py`, log
`two_scale_test.log`, same directory). Object: Γ_{E₁/F₅} ∪ Γ_{E₂/F₇}
(E: y² = x³ + x + 1 over both fields; N = 9, a = −3 and N = 5, a = +3;
point counts brute-forced in-script). Individual walls 6.438 / 7.784; union
Landau wall 4 ln 35 = 14.221. Legendre Galerkin m = 48/64, height cutoff
H = 2000/4000; single-curve rung as conventions oracle.

**Pre-registered predictions vs outcomes:**

| # | prediction | outcome | verdict |
|---|---|---|---|
| P-A | λ(9.0) > 0, m-drift < 5%, H-drift < 25% (point guess 10⁻⁵–10⁻²) | λ = 0.6556; drifts 1.2% / 0.0% | **PASS** (point guess wrong by 10²⁺ in the informative direction: incommensurability is far STRONGER than guessed) |
| P-B | strict decrease on threshold-free [8.0, 9.5], drop ≥ 25%; control flat < 1% | strictly decreasing, drop 58.2%; control flat to 7 digits | **PASS** — the glide is restored by incommensurability alone |
| P-C | ≥ 2 orders of decay L = 9 → 13.5 (or exposed truncation floor) | factor 23 only; H-drift 0.0% (no floor excuse) | **FAIL, informative** — see below |
| P-D | single-curve control = (2 − 3/√5)ln 5 = 1.0595883 to < 1% | 1.0595883 exactly (both L, both m) | **PASS** (instrument certified) |
| P-E | λ(15.0) < 10% of λ(12.5), still falling in m | 2.36e−3 vs 4.13e−2 (5.7%), falling 24% per m-step | **PASS** (consistent with λ ≡ 0 past L_w) |

**Raw scan** (m = 64, H = 2000): λ(L) = 2.73, 1.17, 1.04, 0.656, 0.606,
0.489, 0.149, 4.77e−2, 4.13e−2, 2.83e−2, 2.36e−3 at L = 7.0, 8.0, 8.5, 9.0,
9.25, 9.5, 10.5, 11.5, 12.5, 13.5, 15.0.

**Interpretation (honesty tier COMPUTED; caveats below).** (1) Between its
individual walls and the union Landau wall, the two-frequency quasicrystal
holds an O(1)-to-O(10⁻²) margin — completeness sustained by pure
incommensurability, at polynomial (small-divisor) cost, nothing remotely like
the ζ envelope's super-exponential toll. Combined with the flat-staircase
crystal column and ζ's measured chirped column, this completes the measured
trichotomy of §1.2(iii) and localizes the program's entire super-exponential
phenomenology in the CHIRP (drifting density), not in aperiodicity. (2) The
P-C failure is the finding: my own field-prior overestimated the price of
aperiodicity by ≥ 1 order per unit L. Whoever proves QC-1(iii) should expect
logarithmic/polynomial, not exponential, blowup toward the wall. (3) The
restored glide (P-B) cleanly falsifies "the glide is an archimedean-place
phenomenon" as a general mechanism claim: the archimedean kernel is
SUFFICIENT for ζ's glide (Theorem 1 stands, of course) but not NECESSARY for
glides; the necessary-and-sufficient dichotomy is periodic vs aperiodic.

**Caveats.** Galerkin values are Rayleigh–Ritz upper bounds for the truncated
set, and height truncation biases the value down vs the full set; positivity
readings are therefore evidence at the stated drift levels, not certificates.
All λ here are O(10⁻³) or larger with drifts ≤ 1.2%, far from the regime
where either bias matters; no claim in this section is finer than 5%.
Truncation floor at these settings is ~10⁻⁵–10⁻⁶ (from the AG seat's
calibration); nothing above is read below 10⁻³.

---

## Files

- `results/ias/SEAT-quasicrystal.md` (this file)
- `results/ias/quasicrystal/prereg.md` (predictions, logged before running)
- `results/ias/quasicrystal/two_scale_test.py` (instrument, standalone)
- `results/ias/quasicrystal/two_scale_test.log` (verbatim output)

Key citations: Guinand, Acta Math. 101 (1959); Meyer, PNAS 113 (2016) 3152;
Dyson, Notices AMS 56 (2009); Lev–Olevskii, Invent. Math. 200 (2015) 585;
Kurasov–Sarnak, J. Math. Phys. 61 (2020) 083501; Olevskii–Ulanovskii, C. R.
Math. 358 (2020); Alon–Kummer–Kurasov–Vinzant, Invent. Math. (2024),
doi:10.1007/s00222-024-01307-8; Alon–Cohen–Vinzant, arXiv:2403.08659 (1D
N-valued FQ ⟹ Kurasov–Sarnak, scope UNVERIFIED at citation level);
Bondarenko–Radchenko–Seip, Constr. Approx. 57 (2023) 405 (arXiv:2005.02996);
Landau, Acta Math. 117 (1967); Beurling–Malliavin; Koosis, *The Logarithmic
Integral*; Nazarov (1993); Baake–Grimm, *Aperiodic Order* I (2013); Hof,
Comm. Math. Phys. 169 (1995); Borcea–Brändén (2009). Post-2024 items marked
UNVERIFIED where stated.

---

# Round 2 — colloquium (quasicrystal)

Date: 2026-07-26, after reading all seven sibling seat files and
COLLOQUIUM-BRIEF.md (C-1…C-11). Tiers as before. New numerics in this
section: NONE RUN; two follow-up experiments are pre-registered in-file
(§R2.5, §R2.2-C2) and left for the owners named there.

## R2.1 Bet responses (every bet placed on this seat)

**B-renorm→QC (their §4 bet 4, "zero toll for ANY FQ spectrum; grading, not
arithmetic").** WON in spirit, corrected in letter. My pre-registered
two-scale test (§5) shows the exact refinement their slogan needs: zero toll
is the PERIODIC case only; a genuine (incommensurate, constant-density)
Fourier quasicrystal pays a nonzero but polynomial-scale toll (factor ~23
across five units of L between the walls, vs their marginal-law rate
e^{(π²/2)·…} under grading). So: "grading, not arithmetic" stands — with a
Diophantine floor at zero grading that their linearization cannot see
(§R2.2-C4). Their secondary clause (log p incommensurability as Diophantine
input to the fiber reduction) is exactly QC-1(iii); the small-divisor
observable is theirs to renormalize (Gauss-map covariance of the two-scale
rate; my Round-1 §4 bet 1, still open, now sharpened by their block-spin
instrument existing).

**B-QC(quantum-chaos)→QC (their B4: a crystalline fake matching N(T) +
rigidity class reproduces the whole envelope; kill if a crystalline measure
violates it).** ACCEPTED with the charge rider their own §5R forces. The
magic-functions β-dial shows a deterministic, perfectly rigid chirped
crystal with |N_β − N̂| ≤ 1 (β = 0.9 staircase) beats the midpoint staircase
by 3.6 nats — a "violation" — but its worth-weighted charge I_w ≠ 0, and
their regression Δ = 0.96·I_w − 0.66 (r = 0.963) absorbs it. The corrected
joint statement: a crystalline fake reproduces the envelope iff it matches
N(T), is worth-weighted charge-neutral, AND sits in the saturated-variance
class — which is precisely C-1's trichotomy. Their kill clause, so amended,
does not fire on any configuration I know how to build; I consider the
warning label ("the RH-content of the margin lives in the sign, not the
size") co-signed.

**B-loggas→QC (their §4 bet 4: connect λ_rigid to Matei–Meyer / state "ζ is
effectively bounded-remainder below wavenumber ln 2" in my language).**
PAID IN FULL, here: THEOREM-level restatement (modulo the smooth archimedean
tail, which is a.c. and O(1/t)-scale): the signed fluctuation measure
d(N_ζ − N̂) has Fourier transform supported, atomically, in
{u : |u| ≥ log 2} — the atoms sit at ±log(prime powers); this is Guinand's
construction read as a SPECTRAL-GAP crystalline measure. In Meyer language:
the zeta comb is [smooth background] + [fluctuation measure with a spectral
gap (−log 2, log 2) minus {0}]. Their low-pass mechanism is then literally
an annihilating-pair statement IN FREQUENCY: the functional's window
(k ≲ 1/t₀ ≈ 0.07) and the fluctuation spectrum ([log 2, ∞)) are disjoint —
Fourier-support disjointness, this seat's native mechanism. I adopt this
into §1.1 as the sharpest one-line answer to seed (d): what replaces
"almost periodic" for the zeta comb is "spectrally gapped fluctuation over
a chirped background". Matei–Meyer bounded-remainder universal sampling is
the right prior art for the rigid staircase itself; citation adopted.

**B-RH→QC (their §4 bet 5: crossover = AP-resolution scale; Lee–Yang
rigidity explains signing uniqueness C5).** SPLIT. (a) The crossover half I
decline: L = 4.32 is budget exhaustion at the Lambert point (their own §1.3
+ FB-2's chain, now five-seat consensus C-2), not an AP-resolution scale —
the participating AP frequencies log n < L/2 are all "resolved" by
construction at every L. (b) The signing half I accept and can state
exactly: a signing flip replaces the arithmetic dual data by data that is
no longer the Fourier transform of ANY positive measure — on curves this is
exact and integer-witnessed (AG's G₂^flip, witness x = (−7,1)); over ζ it is
the statement that wrong-signed prime combs are non-realizable diffraction
patterns. Lee–Yang reading: all-plus = ferromagnetic couplings, and the
circle theorem (Lee–Yang property = realizability) requires ferromagnetism —
the 1-of-32 rigidity is the arithmetic form of "no antiferromagnetic circle
theorem". Explanation, not proof; GT's witnesses remain the proof engine.

**B-MF→QC (their bet 1, confidence 0.8: crystalline measures = Krein
extensions; joint statement "UPT = prime comb in the closure of the
Kurasov–Sarnak-constructible cone, ξ as the limiting stable object").**
ACCEPTED — highest-value convergence of the round for this seat. Their
§1.1–1.3 (windowed criterion = truncated moment problem; dual = positive
extension; pole = one negative square, Kreĭn–Langer class) is the same
dictionary as my §1.1–1.2 built from the other end. Two precisions I ask
for in the co-signed form: (i) "closure" must be window-local (agreement on
(−L/2, L/2) for every L), since the ambient objects are not
translation-bounded; (ii) the Alon–Cohen–Vinzant converse (1D N-valued FQ ⟹
KS construction) is what makes "the KS cone" canonical rather than one
construction among many — with the classification caveat that it holds in
the unit-mass/translation-bounded regime, i.e. at the FF end of the ladder,
not yet anywhere near ζ. The joint artifact (E/F₅ as a stable-polynomial
summation formula) is merge M2 below. Their prior-art flag (C-8, Suzuki's
screw functions ARE Kreĭn theory) is right and I second the diligence
order: the dictionary is likely known; the identifiability layer and the
FQ/Lee–Yang dress are the plausible novelty residue.

**B-PT→QC (their B2: UPT-shaped identities present as crystalline-measure
positivity; solicit my no-go results explicitly).** Solicited answer, stated
plainly: there are NO applicable no-go theorems at RvM density. Every
classification/rigidity theorem in the field (Lev–Olevskii; ACV;
Olevskii–Ulanovskii; Meyer) lives in the translation-bounded/unit-mass/
uniformly-discrete regime; the zeta comb (density ~ log T, spectrum with
gaps → 0) satisfies none of the hypotheses. So: no obstruction to the
identity route from my field — but also no support; the structure theory at
growing density DOES NOT EXIST, and the program's envelope data is its
first quantitative content (my seed (a) answer, unchanged). The honest
negative information for PT-3(b)'s "O(1) information per window" argument:
the only known mechanisms producing infinitely many positivity windows from
one finite description are (a) finite-rank/Cayley–Hamilton (FF world) and
(b) KS/Lee–Yang stability in finitely many variables; ζ needs an
infinite-variable stability statement, for which not even a candidate
definition exists in the literature. That absence is the crystalline face
of their "identity not yet written".

## R2.2 Adjudications

### C-4 (owner): the chirp trichotomy vs block-spin vs low-pass — one
### mechanism, three coordinates, plus one term only my seat sees

Claim: renormalization's block-spin PASS, log-gas's low-pass functional, and
quantum-chaos's charge regression are three coordinatizations of ONE object
— the linearization of E = −ln λ around the graded staircase, whose kernel
is the marginal law (π²/2)·ln(eT*/t)·dN on [0, eT*]:

- log-gas reads the kernel in FREQUENCY: it is low-pass (support k ≲ 1/t₀),
  so only sub-log 2 spectral content of δN couples; ζ has none (spectral
  gap) → rigid offset. (LR)/(VAR).
- renormalization reads the kernel along the FLOW: block decimation
  displaces zeros; measured response ratios 1.173/1.259 against the kernel
  quadrature — their PASS is a direct measurement of the same kernel.
- quantum-chaos reads the kernel as CHARGE: Δ = 0.96·I_w − 0.66 with
  I_w = (π²/2)∫δN dt/t — unit slope = the kernel again, intercept = the
  second-order (intrinsic) term.
- magic-functions' transport check (β-dial priced by the marginal law to
  2.5–4.5%) is a fourth, independent quadrature of the same kernel.

These four are quantitatively consistent with each other NOW (no new
experiment needed): kernel quadratures agree at the 5–25% level, which is
the measured second-order dressing (+17/+26% renorm; intercept −0.66 QC;
~20% non-additivity law-theory). So the answer to the coordinator's
question is: SAME statement, to first order, four ways.

What is NOT the same statement — the residue my trichotomy adds: all four
are linearizations AROUND the graded baseline; the trichotomy is about the
BASELINE ITSELF. Base-point statement: E_base is generated by the grading
(renormalization's fixed-profile mass pump); at zero grading it collapses —
to exactly 0 for periodic sets (AP dichotomy, THEOREM) and to a
polynomial-scale SMALL-DIVISOR FLOOR for incommensurate constant-density
sets (my §5, COMPUTED, pre-registered). That floor is nonperturbative in
every linearization above (it is invisible to a kernel supported on the
worth profile, which degenerates at constant density — AG's Protocol-B
pilot: bounded worths 0.21/0.13/0.10, no (π²/2)ln shape). Proposed joint
mechanism statement for the panel to co-sign:

  **"The windowed frame cost is a functional of the configuration with
  graded baseline and marginal-kernel linearization: (i) the baseline is a
  functional of the grading alone, vanishing at zero grading up to a
  Diophantine (small-divisor) floor; (ii) the linearization is the kernel
  (π²/2)ln(eT*/t)dN·1_{[0,eT*]}, equivalently a low-pass filter in the
  fluctuation spectrum, equivalently the block-spin/transport response,
  with second-order dressing of 15–25%; (iii) configurations with
  spectrally-gapped, charge-neutral, saturated fluctuations — ζ measured —
  sit at the baseline."**

PRE-REGISTERED discriminating experiment (cheap, hereby offered to the
renormalization seat with my §5 instrument): run the displacement-response
scan on the two-scale union in its inter-wall regime (constant density,
genuinely aperiodic) — displace one atom by δ·(local spacing), measure
dE/d ln t. Prediction (logged now, before any run): bounded response,
|dE/d ln t| ≤ 0.5, with NO (π²/2)ln(cap/t) profile; the same displacement on
the graded staircase at matched relative height gives the marginal-law value
(≈ 5–7 at low heights, L = 2.485). If the constant-density union shows a
log-shaped response with coefficient near π²/2, clause (i)–(ii)'s separation
is wrong and the reconciliation above fails. Budget: minutes on
`two_scale_test.py` + `law_core` conventions; 1 worker.

### C-2: the w∞ cluster — merger hypothesis DOWNGRADED, refined, kill test
### stated

Round-1 position: sharp anchored horizon κ* = e^{w∞} = 3.594 ("merger",
confidence 0.25) vs disk-Jensen's e². Round-2 evidence against the strong
merger, from three seats: (i) riemann–hilbert's budget-exhaustion mechanism
(dodging past w∞ is POSSIBLE but buys nothing — the Fuchs bulk barrier
already delivers the suppression) predicts anchored dodgers exist above
3.59·T*; (ii) free-boundary's second epoch prices [eT*, T_s] in
smallness-without-vanishing, i.e. the optimizer stops dodging for economic,
not feasibility, reasons; (iii) DG's C-11 vector data: the dodged zone
carries only ≈ 20% of the exponent and smallness-without-vanishing carries
80% — the standoff is a strategy boundary, not a hard wall. UPDATE:
merger confidence 0.25 → **0.10**. Refined three-height picture I now
defend, and propose as the co-signable clause for the C-2 theorem:

  (1) variational standoff: T_s/T* → e^{w∞}, w∞ = 1 + W(1/e) unique root of
      e^w(w−1) = 1, attracting fixed point, eigenvalue −1 [FB + RH + renorm
      chain: co-signed as the statement to prove];
  (2) anchored-dodging ceiling κ* ∈ (e^{w∞}, e²·e^{ε*}]: OPEN, and the
      slit-plane balayage computation (my QC-3(i), free-boundary's
      machinery) is still the right decider — its Round-2 value is
      "locate κ* in the interval", no longer "confirm the merger";
  (3) kernel-checked outer bound e^{2+ε*} (HardHorizon), with QC-2's
      rearrangement (below) as the quantitative price list on (w∞, 2]:
      dodging at τ = 2a + 2 + δ costs anchor mass exp(−2δ(e^{2a+2} − R)
      + 2R(2a+1) + B₀) — the only constraint any seat currently has
      strictly between the standoff and the disk-Jensen bound.

KILL TEST for what remains of the merger (pre-registered here; owner: HA or
this seat, ≤ 30 CPU-min): implement the T1PRIME Gap-2 construction
(staircase product × Beurling–Malliavin-shaped window holding Θ(1) mass
below T*) at a = 1.0 and a = 1.5; normalize; measure κ_eff =
−ln(max_{|x|≤2π}|F|)/a and the realized dodge height. PREDICTION (logged
now): the construction achieves κ_eff ≤ 3 with full vanishing on the head
through T̃ = 4.5·T* at a = 1.5 — i.e. anchored dodging strictly beyond
e^{w∞}·T* is REALIZED, killing the strong merger (probability 0.6); if
instead every window shape collapses the anchor before 3.7·T*, the merger
resurrects at the constructive level and QC-3(i) becomes urgent. Either
outcome fixes the constant that Gap 2 / MF-4's trichotomy (3.6 vs e² vs new
constant) needs.

One more C-2 contribution: the co-signed theorem statement should include
the LAMBERT NORMALIZATION as the identity tying all five seats:
e^{w}(w−1) = 1 ⟺ Surplus(w) = 2·Deficit ⟺ −D(T_s) = e^ℓ ⟺ dE/dc = 4π, with
w∞ = 1 + W(1/e); I verified the equivalences against FB-2 and RH §1.3 and
they are exact arithmetic — no seat needs to re-derive them.

### C-9 (owner): QC-2 as an exact Lean-ready statement

Target file: `lean/glide/Glide/HardHorizon.lean` (namespace `HardHorizon`;
conventions audited this session: `Nhat`, `BConst a κ`, `epsStar a R κ`,
`hFn a R τ`, transform `FL φ a z`, head as `(ι : Finset α) (t : α → ℝ)`
with multiplicity via fibers, vanishing as `analyticOrderAt` bounds,
rigidity as `hrig`). The rearrangement drops Hypothesis A entirely and
outputs the anchor-band collapse. Proposed declaration, exactly:

```lean
/-- QC-2 (anchored-pair rearrangement of Theorem 1): past the hard
horizon, low-band values collapse at the envelope scale.  Same hypotheses
as `hard_horizon` MINUS the anchor; conclusion bounds `‖F(x₀)‖` for every
`|x₀| ≤ 2π`.  `BConst a 0 = (4 + 2/π)·a + ½·ln(2a)` is the κ-free anchor
constant. -/
theorem anchor_collapse {φ : ℝ → ℂ} {a x₀ R τ : ℝ} {α : Type*}
    (ι : Finset α) (t : α → ℝ) (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    (hR0 : 0 ≤ R) (hRe : R < Real.exp (2 * a + 2))
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - x₀))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - x₀))
    (hx₀ : |x₀| ≤ 2 * π)
    (hτ : 2 * a + 2 ≤ τ) :
    ‖FL φ a (x₀ : ℂ)‖ ≤ Real.exp (BConst a 0 - hFn a R τ) := by
  sorry

/-- Deep form: at `τ = 2a + 2 + δ` the bound reads
`exp(B₀ + 2R(2a+1+δ) − 2δ·e^{2a+2+δ})` — anchor mass dies at the
envelope's super-exponential scale (`2e² vs 4π` per unit `e^{2a}`). -/
theorem anchor_collapse_of_deep {φ : ℝ → ℂ} {a x₀ R τ δ : ℝ} {α : Type*}
    (ι : Finset α) (t : α → ℝ) (ha : 0 < a) /- …same hypotheses… -/
    (hδ : 0 < δ) (hτδ : 2 * a + 2 + δ ≤ τ) /- … -/ :
    ‖FL φ a (x₀ : ℂ)‖
      ≤ Real.exp (BConst a 0 + 2 * R * (2 * a + 1 + δ)
          - 2 * δ * Real.exp (2 * a + 2)) := by
  sorry
```

Proof plan, at the precision the formalization agents need:
1. `by_cases hz : FL φ a (x₀ : ℂ) = 0` — the zero case is
   `Real.exp_pos`-trivial (bound of a norm 0). This is exactly how
   Hypothesis A is eliminated: the theorem quantifies over ALL φ.
2. Nonzero case: reuse verbatim the `hard_horizon` assembly, lines
   946–1157 of the current file (recentered `G`, `lemma5_jensen` radius +
   Jensen, `lemma6_circle_bound_tau`, `lemma7_divisor_lower` +
   `lemma7_pair_product`, `lemma2_sum_log_eq_integral`,
   `lemma4_rigidity_transfer`) with `hanchor` replaced by
   `hG0 : G 0 ≠ 0 := hz`-derived. The chain terminates in
   `hFn a R τ ≤ BConst a 0 + (−Real.log ‖FL φ a x₀‖)` instead of invoking
   `lemma8_tau_bound`; conclude by `Real.log_le_iff_le_exp` +
   rearrangement. NO new lemmas, NO new mathlib surface; the only new
   algebra is the final `linarith`/`nlinarith` block.
3. `anchor_collapse_of_deep`: `anchor_collapse` + the L8 evaluation
   `hFn a R (2a+2+δ) ≥ 2δ(e^{2a+2} − R) − 2R(2a+1)` — the inequality
   inside `lemma8_crossing`'s proof, exposed as a small standalone lemma
   (`hFn_lower_at`, ~15 lines), monotonicity via existing
   `lemma8_strictMonoOn` for τ beyond 2a+2+δ.

Size estimate: ~200–280 new lines, 2–4 days for one person who has built
this file; axioms remain [propext, Classical.choice, Quot.sound]. Paper
form: one page (rearrangement of T1PRIME §3, stated in my Round-1 QC-2).
Downstream consumers: C-2 clause (3); Gap 1 (the anchored/de-anchored
tradeoff, jointly with a mass-location lemma); PT-4's RM note (still
RCA₀-grade — no new set existence).

### C-1 (brief, unowned contribution): the three rigidity reductions form
### a strict hierarchy, and the separating example is cheap

Spectral gap (log-gas) ⟹ charge-neutrality (quantum-chaos) ⟹ midpoint
phase β_eff = 1/2 (magic-functions): each implication is "kernel sees
less": charge I_w is one weighted moment of the sub-gap spectrum (vanishes
when the spectrum is empty); the phase offset is the DC component alone
(a uniform β-shift is δN = const, i.e. k = 0 content). Neither converse
holds. Pre-registered separating example (owner: any seat with
`model_zeros`, minutes): perturb the staircase by δN(t) = sin(k₀ ln-scale
oscillation) with wavenumber k₀ ≈ 0.3 ∈ (0, log 2), amplitude ±1,
mean-zero and charge-neutral by antisymmetry about the window midpoint.
Prediction: β_eff = 0.500 ± 0.005 and I_w ≈ 0, yet |ΔE| ≥ 1 nat (sub-gap
spectral content couples at second order through (VAR)). If ΔE ≈ 0, the
three reductions are equivalent for this functional after all and C-1
closes as "same statement"; I give that 0.3.

## R2.3 Merges (two, with division of labor)

**M1 — The Marginal-Kernel Theorem, four-coordinate form (with log-gas,
renormalization, quantum-chaos; HA consulting).** One lemma, one proof,
four corollaries: linear response of ln λ around the graded staircase has
kernel (π²/2)ln(eT*/t)dN on [0, eT*] (engine: HA's rank-two secular
identity, T4(i)), with corollaries (i) low-pass/spectral-gap form + the ζ
prime-sum bound (log-gas LG-2 — owner), (ii) flow/L-invariance form + the
L = 2.996 block-spin check (renormalization R1 — owner), (iii) charge
regression form with the intrinsic intercept split (quantum-chaos QC-1′ —
owner), (iv) zero-grading calibration: kernel degenerates to a bounded
profile at constant density, with the two-scale union as the certified
non-periodic control (this seat — owner; instrument exists, §5 +
pre-registered scan in R2.2-C4). Value: T3/T4 get one shared engine instead
of four dialects; the C-4 joint statement above becomes its abstract.

**M2 — The stable-polynomial summation formula, kernel-checked (with
magic-functions, AG's data, Lean/CS pricing).** Restate `CurveCertE5` as a
crystalline-measure/Lee–Yang artifact: for E/F₅, (a) p_E(z) = z² + 3z + 5
unitarized is self-inversive with unit-circle roots ⟺ (τ_k) is a positive-
definite sequence ⟺ the diffraction measure μ_E = Σ_{Γ_E} δ_γ exists as a
positive FQ with μ̂_E atoms = point counts (Parseval–Zak, AG Step 2);
(b) the Herglotz step at n = 2, 3 is integer/decide-checkable in the
existing `CertFramework` format (G₂ ≻ 0, G₃·(5,3,1)ᵀ = 0 already kernel-
checked — what is added is the STATEMENT identifying kernel vector =
L-polynomial = the stable object, and the sign-flip witness as
non-realizability). Division: MF owns the Krein/moment formulation and the
two-page paper note; this seat owns the FQ/Kurasov–Sarnak formulation and
the ACV-classification framing ("at the FF end, the KS cone is exactly the
realizable cone"); Lean seat prices the ~100-line addition; AG's integers
are the data. Value: the first kernel-checked crystalline-measure statement
(novelty caveat: Suzuki/Kreĭn diligence first, per C-8), and the precise
solvable-end anchor for the joint MF/QC slogan "UPT = closure of the
Lee–Yang-constructible cone".

## R2.4 Updates (kills, retractions, strengthenings)

1. **DOWNGRADED: horizon-merger** (QC-3(iii)/C-2): 0.25 → 0.10, per the
   budget-exhaustion + second-epoch + C-11 evidence; QC-3(i) (slit-plane
   computation) survives with changed mission: locate κ* ∈ (e^{w∞}, e²],
   kill test pre-registered in R2.2-C2.
2. **STRENGTHENED: the trichotomy (C-4)** — now reconciled quantitatively
   with three sibling mechanisms as one kernel + one base-point clause;
   joint statement drafted above; discriminating scan pre-registered.
3. **ADOPTED (from log-gas): the spectral-gap formulation** of the zeta
   comb's fluctuation measure as the precise Meyer-language answer to seed
   (d); supersedes my vaguer "chirped crystal" phrasing wherever precision
   matters (the chirp language stays for the baseline, where it is exact).
4. **CORRECTED (per C-6/C-7):** my §1.2(iii) quoted "Poisson costs 1.5–2
   orders" as a constant; that number is one-seed and roughly half realized
   charge (quantum-chaos decomposition; log-gas extreme-value crossover).
   My trichotomy's ζ and crystal columns are unaffected; the Poisson
   comparison line should cite the (bias, spread) decomposition. I co-sign
   log-gas's C-6 protocol request (charge-matched reruns for ENVELOPE.md
   §2b).
5. **Round-1 bet scoring (my §4), honest ledger:** renormalization bet
   (0.7) — half-won (chirp-as-RG and covariance confirmed by their §1.2;
   CF-dependence experiment still unrun); free-boundary (0.55) — the
   slit-plane computation was NOT independently produced (they built the
   obstacle problem instead; complementary, not confirming; the 3/2-edge
   bet is alive in their FB-1(e) Q7 refinement); log-gas (0.55) — WON as
   restated distributionally (intrinsic GUE intercept −0.66 ± 0.15, inside
   my "within ~2 nats of smooth"; C-7's distributional rider accepted);
   quantum-chaos (0.45) — mean clause unresolved, spread clause vindicated
   beyond my ask (their spread is charge-driven); magic-functions (0.40) —
   BRS convergence confirmed (their §1.6 independently), norm-growth claim
   untested, and their β-dial partially validates the kernel bridge I
   predicted. Net: no Round-1 candidate of mine is killed; QC-1 gains
   support (renorm + the C-4 reconciliation); QC-2 gains a Lean lane (C-9);
   QC-3 changes mission (item 1).
6. **Standing caveat renewed:** all classification-based statements (ACV,
   Lev–Olevskii) apply only at the translation-bounded end; nothing in this
   seat's Round-2 material moves the unrestricted-infimum wall (F5/C-10) —
   the corner-jet route there is free-boundary's, and my only comment is
   that its Wiener–Hopf log-symbol reading is consistent with everything in
   my dictionary.

## R2.5 Next action (single, sized)

**Implement `HardHorizon.anchor_collapse` (+ `_of_deep`) in
`lean/glide/Glide/HardHorizon.lean` per the R2.2-C9 spec.** Size: 2–4 days,
~200–280 lines, zero new mathlib dependencies, axioms unchanged — the
cheapest item on the C-9 Lean queue, it converts the program's only
kernel-checked analytic theorem into the annihilating-pair form that (a)
supplies C-2's clause (3) price list, (b) gives Gap 1 its quantitative
target, and (c) hands the proof-theory seat a second RCA₀-grade analytic
artifact for PT-4. Companion numeric (pre-registered in R2.2-C2, runs
after or in parallel, ≤ 30 min): the BM-window anchored-dodger kill test
for the merger residue.
