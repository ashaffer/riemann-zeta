# SEAT: quantum chaos / semiclassical analysis

Round-1 independent report. Written 2026-07-26 against: PROGRAM.md §§2.14–2.20 + §3,
ENVELOPE.md, results/RESULTS.md, THEOREMS.md, RH-LEMMA-MAP.md,
results/experts/SYNTHESIS.md (incl. errata + §5 kill list), T1PRIME.md §§0–1,
FULLINF.md §§0–2. No other SEAT file was read. Honesty tiers used throughout:
THEOREM / COMPUTED / CONJECTURE / SPECULATION. Citations are standard-literature
from memory; anything I could not re-verify in this session is marked UNVERIFIED.

---

## §0 Seat card

- Periodic-orbit theory: Gutzwiller trace formula, orbit sums vs spectral sums, the
  primes-as-orbits dictionary (period log p, no Lyapunov factor, "flow" of xp type).
- Spectral statistics: form factor K(τ), diagonal approximation (Berry 1985),
  off-diagonal resummation (Bogomolny–Keating 1996; Sieber–Richter 2001), number
  variance and its arithmetic saturation (Berry 1988; Selberg's CLT; Odlyzko's data).
- Berry–Keating H = xp: phase-space counting N(E) = (E/2π)(ln(E/2π)−1) + 7/8,
  regularization boundaries, Connes' absorption-spectrum reading (Selecta 1999).
- WKB/tunneling: exponentially small eigenvalues as forbidden-region actions;
  turning points, Airy edges; resurgence/trans-series, Stokes phenomena.
- Instruments here: src/model_zeros.py (frame_form on arbitrary ordinates),
  src/spectral_margins.py; I run one pre-registered test in §5.

---

## §1 Translation: the program's objects in quantum-chaos language

The dictionary below is, I believe, exact where marked THEOREM/identity and honest
where marked interpretation. It contains one identification I have not seen written
in the repo: **T\*(L) is the Heisenberg-time crossing**, and the entire envelope
program is a statement about the cost of *imposing spectral zeros in the
sub-Heisenberg (unresolved) regime*.

**1.1 The truncated Weil form is a finite-observation-time trace formula.**
(Identity.) Test functions φ supported in [−a, a], a = L/4; the prime side involves
ψ_φ(log n), supported in |u| ≤ 2a = L/2. So the "observation time" of the
instrument is t_obs = L/2, and the orbit sum contains exactly the periodic orbits
(prime powers, period log n) with period ≤ t_obs — the truncation at e^{L/2} is the
standard trace-formula windowing, made exact by compact support. This is the
finite-resolution explicit formula in precisely the sense of Berry–Keating
(SIAM Rev. 41 (1999) 236): the Riemann–Siegel-like tradeoff between orbit cutoff
and spectral resolution.

**1.2 T\* = 2πe^{L/2} is the Heisenberg-time crossing.** (Identity.) The zero
density at height T is ρ(T) = (1/2π)ln(T/2π); the Heisenberg time there is
τ_H(T) = 2πρ(T) = ln(T/2π). The Nyquist height T\* of the program solves exactly

  τ_H(T\*) = t_obs = L/2.

Zeros below T\* are individually resolved by the window (observation time exceeds
their Heisenberg time; form-factor "plateau" regime, unfolded τ = t_obs/τ_H > 1);
zeros above T\* are unresolved (ramp regime, τ < 1). The family universality
T\*_χ = (2π/q)e^{L/2} is the same identity with the analytic-conductor density
(1/2π)ln(qT/2π): in orbit language the conductor adds a fixed path-length log q to
every period — universality in T\*_χ is automatic in ANY semiclassical reading and
carries no extra information beyond the density (consistent with §2.16's finding
that conductor/parity/pole enter only the offset).

**1.3 λ(L) is the ground state of a windowed frame operator whose kernel is the
Fourier transform of the zero measure.** (Identity under the certified ledger.)
Q_L(φ) = 2Σ_{γ>0}|φ̂(γ)|², so λ(L) = λ_min of the operator on L²[−a,a] with kernel
K(x−y) = 2Σ_{γ>0} cos(γ(x−y)). Its diagonal is the level density; its off-diagonal
profile at lag u is the object whose ensemble average over height windows is the
spectral form factor. So the margin is a **global, all-scale rigidity functional**:
it integrates two-level (and all higher) correlations over every unfolded time
τ ∈ (0, t_obs/τ_H(t_min)], whereas K(τ) is a single-scale local observable. This
single sentence is the resolution of the apparent GUE conflict — see 1.6.

**1.4 The exponent is a phase-space cell count (the answer I can defend for seed
question (a)).** The synthesis' unified law (SYNTHESIS §2, COMPUTED + algebra):

  E(L) := −ln λ ≈ 2π·[D(T\*) − D(T_s)],  D(T) = aT/π − N(T),

with T_s = e^{w}T\* the measured standoff height (w ∈ [1.14, 1.23] over eleven
deep windows; w∞ = 1.2785 candidate saturation). Read as a physicist: aT/π is the
Landau/Nyquist degrees-of-freedom count of the window up to height T — the number
of Planck cells in the phase-space rectangle [−a,a] × [0,T] — and N(T) is the
Berry–Keating regularized area under the hyperbola xp = T (their +7/8 included).
So D(T) is the *surplus of window degrees of freedom over spectral demands*, and

  **E ≈ 2π × (number of net vanishing conditions imposed beyond the Nyquist budget
  in the band [T\*, T_s]) — i.e. 2π nats per super-Nyquist Planck cell.**

Locally: dE/dN(t) = 2π(1 − τ(t)) per zero dodged at height t, τ(t) = t_obs/τ_H(t)
∈ (0,1) in the band. At t = T\* the per-zero cost is 0 — this IS the glide theorem
seen semiclassically (a zero arriving exactly at the resolution edge is free); the
cost per zero rises as τ falls, reaching 2π(1 − 2a/(2a+w)) at the standoff.
CONJECTURE (QC-3 in §2 makes it precise and testable): this is a WKB/tunneling
exponent, the imaginary action of the bandlimiting symbol run under the xp demand
curve, and the minimizer's transform obeys d ln|F|²/dN(t) ≈ −2π(1 − τ(t)) on the
band. Two honesty riders: (i) kill-list K2 stands — the *bulk/continuum* prolate
functional provably does NOT produce the mid-range constants; the cell count above
is over DISCRETE dodged zeros, and the discreteness is load-bearing (density
smoothing makes λ = O(1), law-theory §2.0–2.2); (ii) the 7/8 is not decoration:
the errata's exact D(eT\*) = −7/8 means the Maslov-type constant of the
Berry–Keating count survives *exactly* into the frame-bound bookkeeping — the
phase-space count is literal, not just leading order.

**1.5 The two horizons are Heisenberg-time statements.** (Restatement of proved
material.) T1′'s two horizons read, in τ_H units: the variational/balayage horizon
eT\* is τ_H = t_obs + 1; the proved hard horizon (HardHorizon.lean, THEOREM) e²T\*
is τ_H ≤ t_obs + 2 + ε\*: **an anchored test function can impose zeros only on
frequencies whose Heisenberg time exceeds the observation time by less than two
e-folds.** Measured standoffs sit at τ_H ≈ t_obs + 1.14…1.23, strictly between.
I know of no prior quantum-chaos statement of this "two-e-fold dodging law"; it is
a genuinely new, sharp semiclassical fact this program has produced (as usual,
pending literature check).

**1.6 The rigidity finding is Berry's number-variance saturation, observed by a
new instrument.** (Interpretation, with rigorous anchors.) The measured facts:
smooth RvM staircase reproduces true-ζ λ within truncation error; Poisson costs
1.5–2 orders (≈ 4.5 nats at L = 2.485); GUE not yet measured (SYNTHESIS Q6 = my
§5). The apparent paradox — zeta zeros have GUE local statistics (Montgomery,
Odlyzko), yet the frame bound says "maximally rigid" — dissolves at once in form-
factor language:

- GUE number variance grows: Σ²(n) = (1/π²)(ln 2πn + γ + 1) + o(1) for the sine-
  kernel process (Mehta; constant term UNVERIFIED to the digit, prefactor solid).
- Zeta number variance SATURATES: rigorously, Var S(T) = (1/2π²)(ln ln T)(1+o(1))
  (Selberg's CLT); semiclassically, Σ²(n; T) follows GUE only up to
  n_max ≈ τ_H(T)/t_min = ln(T/2π)/ln 2 — the shortest orbit (prime 2) sets the
  outer scale — and then saturates at Σ²_sat = O(ln ln T) (Berry 1988,
  Nonlinearity 1, 399; confirmed on Odlyzko's data).
- The frame bound at support L integrates rigidity over N(T_s) ≈ e^ℓ·ℓ levels —
  vastly beyond n_max ≈ ℓ/ln 2. So the margin is dominated by exactly the scales
  where zeta is rigid-beyond-GUE. "True zeros sit at the maximally-rigid offset"
  = "the zeta discrepancy field is saturated (bounded) at frame scales", which is
  Selberg + Berry, not a new mystery. A synthetic 180-level GUE set never
  saturates; it should pay a variance-sized toll — quantified and pre-registered
  in §5.
- The pretty structural reason WHY the zero side behaves rigid here: the explicit
  formula moves the non-universal small-τ orbit spikes (the primes) to the OTHER
  column of the ledger. The Weil form is the trace formula with the short-orbit
  contributions subtracted explicitly; what remains of the spectral side is rigid
  to Selberg-variance accuracy. The "arithmetic" the margin cannot see was
  subtracted by construction. (Interpretation; its theorem-shaped form is T3.)

**1.7 Seed question (d), answered honestly.** Does any Berry–Keating
regularization predict b ≈ 1.51, μ ≈ 6.0–6.7? **No — and I claim that is the
right answer, not a failure.** By SYNTHESIS §2, (b, μ) are chart coordinates of a
drifting standoff height w(L); the BK-predictable quantities are the invariants:
2π per Planck cell (the action unit), the 4π cap (= 2 cells per unit T\*/2π at
saturation), w∞ = 1.2785 as the root of e^w(w−1) = 1 (a smooth-pasting condition,
see bet B3), and the exact 7/8. If C4's saturating-standoff mechanism survives Q1,
(b, μ) need no derivation — they are mid-range effective parameters of the drift.
If Q1 resolves "bias" (no bend), then b ≈ 1.51 demands a derivation and my seat
has no route to it; I would then bet the constant lives in log-gas/Fredholm
territory (defect-potential calculus, T4), not in any xp regularization.

---

## §2 Candidates

### QC-1. The rigidity-spectrometer lemma (offset = number-variance functional)

**Statement (CONJECTURE).** Let μ be a symmetric point process with RvM mean
density, conditioned to K levels in the frame band at support L, and let Σ²_μ(n)
be its number variance at scale n. Then the offset from the rigid staircase
satisfies, for ℓ = L/2 in the measured range,

  ln λ[μ](L) − ln λ[smooth](L) = −Θ(1)·c(ℓ)·𝔇_μ,  𝔇_μ := E[sup_{T ≤ T_s}|N_μ − N̂|],

with c(ℓ) ≤ C·ℓ (the T3/DG-3 form), and consequently the ensemble ladder
Poisson : semi-Poisson : GUE : rigid has offsets in ratio ≈ √K : √(K/2) : √ln K : 0.
Numerically at (L, K) = (2.485, 180): Poisson 𝔇 ≈ 10, measured cost 4.5 nats
(COMPUTED, RESULTS.md), calibrating c·Θ ≈ 0.4 nats per unit 𝔇; GUE 𝔇 ≈ 1.9
predicts ≈ 0.8 nats.
**Proof route:** rank-two secular calculus (T4(i), already priced "days") summed
against a Gaussian linear-statistics CLT for the displacement field
(Costin–Lebowitz for determinantal μ); the sup-discrepancy enters through T3's
transplantation machinery. **Effort:** measurement — done in §5 (hours); theorem —
rides on T3 (months), with the determinantal case possibly easier than general μ.
**Interfaces:** log-gas (variance/hyperuniformity), DG (T3), NT (Selberg input).
**Kill criteria:** (i) §5's kill line — if GUE costs within 3× of Poisson, dead;
(ii) if semi-Poisson (a later cheap run) fails to land between, the sup-discrepancy
functional is the wrong norm.

### QC-2. Saturation transfer: the true-vs-smooth offset is a Selberg-variance
### fluctuation, sign-indefinite, of size ~ ℓ·|S|

**Statement (CONJECTURE, sharp and falsifiable).** For the true ordinates,

  ln λ_ζ(L) − ln λ_smooth(L) = O(ℓ · sup_{T\* ≤ T ≤ T_s}|S(T)|),

with the sign set by the alignment of S(T) in the standoff band (a locally sparse
stretch, S < 0, RAISES λ_ζ above λ_smooth) — not a definite-sign cost. Typical
size ℓ·σ_S ≈ ℓ·√((1/2π²)ln ln T\*) ≈ 0.5–1.5 nats in the measured windows, growing
only like ℓ√(ln ln T\*) forever — smaller than E by a factor ~ e^ℓ, so
"density-not-arithmetic" is safe asymptotically, but the FLUCTUATION is real and
predicts that Q3's factor 6.3 at L = 3.555 (true BEATS smooth by 1.8 nats;
COMPUTED, RESULTS.md) may be genuine, not truncation: 1.8 nats is exactly the
predicted order, and the predicted sign mechanism is checkable — compute S(T) on
[T\*, 3.4T\*] = [37, 127] and correlate with the per-window offset sign across L.
**Proof route:** T3 with Selberg's CLT replacing the worst-case Trudgian input
(unconditional; Selberg's theorem is unconditional). **Effort:** the correlation
check is an afternoon with existing instruments; the theorem-form is T3 plus
bookkeeping. **Interfaces:** DG/T3, NT (S(T) constants), log-gas.
**Kill criteria:** if Q3's factor 6.3 dies as Gcut → ∞ (the synthesis' settling
experiment) AND the sign of (ln λ_ζ − ln λ_smooth) fails to track the band-local
mean of S(T) across ≥ 4 windows, then the coupling of the margin to the
discrepancy field is much weaker than ℓ·|S| and QC-2 is dead as stated.

### QC-3. The per-cell WKB slope (instanton identification made measurable)

**Statement (CONJECTURE).** On the standoff band T\* ≤ t ≤ T_s, the minimizer's
transform obeys

  d ln|F(t)|² / dN(t) = −2π(1 − τ(t)) + o(1),  τ(t) = (L/2)/ln(t/2π),

i.e. the envelope of |F|² drops by exactly 2π(1−τ) nats per zero dodged — the
differential form of E = 2π[D(T\*) − D(T_s)], and the precise sense in which
−ln λ is a tunneling action: 2π per super-Nyquist Planck cell, with the forbidden
region the area between the Nyquist line aT/π and the BK hyperbola N(T).
Integrated consequence (already implied by C4 algebra, stated here as the WKB
check): at saturation, two cells per unit T\*/2π — the 4π cap.
**Proof route:** none new needed for the measurement; the theorem-form is C3's
canonical-system/turning-point program (HA+DG own it) with this seat contributing
the WKB ansatz and the Airy matching at t = T_s (detachment point) and at the
capacity edge eT\* (the (eT\*−t)^{3/2} softening already measured is the Airy
zone; predicted width exponent (a·eT\*)^{−2/3}, HA-P2's number).
**Effort:** measurement = hours on the EXISTING deep minimizer vectors (DG's
extraction utility; no new eigensolves); theorem = subsumed in T5/C3.
**Interfaces:** DG (C4 stopping-height extraction — same vectors, one more
observable), riemann-hilbert (Airy/Painlevé local model), HA.
**Kill criteria:** measured mid-band slope off 2π(1−τ) by > 20% after basis-bias
control kills the per-cell action reading (and with it my §1.4); if instead the
slope is constant in t (t-independent), the "local cost" picture is wrong and only
the integrated identity survives.

### QC-4. The crossover at L = 4.32 is a third-order boundary-saturation
### transition, not a Stokes jump

**Statement (CONJECTURE).** With c = e^ℓ, the true envelope E(c) is C¹ at the
crossover c_c (where the mid-range slope reaches 4π) with continuous second
derivative and a jump in the third — the pulled-to-pushed/Majumdar–Schehr
universality class of constrained-optimization transitions — because the
mechanism is a variational parameter (the standoff w(L)) reaching its smooth-
pasting boundary w∞, not an exchange of two competing exponentials. A first-order
slope jump (abrupt saturation) is already EXCLUDED by the deep-windows level test
(COMPUTED); this candidate upgrades "smooth cap" to a transition ORDER.
In resurgence language: no Stokes line is crossed at L = 4.32; the mid-range law
and the 4π cap are one saddle whose internal parameter saturates. The trans-series
question of seed (c) then relocates: the genuinely resurgent object is the
BASIS-convergence creep (Θ(A_L/(m ln m)), an algebraic series superposed on
spectral convergence), not the envelope itself. SPECULATION: the o(1) corrections
around the cap should organize as (L/2)-polynomial × e^{−(w∞-band) corrections},
with the first "instanton" the capacity-edge Airy tail.
**Proof route/measurement:** second and third finite differences of the converged
E across L ∈ [3.8, 4.75] (existing numbers; the m-convergence error bars from
runs.csv decide feasibility); theory via the free-boundary reading (bet B3).
**Effort:** the difference test is an afternoon; a proof is C4-as-theory (60–90
day horizon per the synthesis allocation).
**Kill criteria:** a resolved discontinuity in dE/dc at c_c (first-order) or in
d²E/dc² larger than the convergence budget (second-order) kills it; so does Q1
resolving "bias" (no bend at all — then there is no transition to classify).

---

## §3 Intuition pumps (licensed informality; everything here SPECULATION unless
tiered otherwise)

- **The notch-filter reading (Connes' absorption picture, operationalized).**
  λ(L) is the residual transmittance of the best notch filter of time-length L/2
  that must null every absorption line (zero) it is exposed to. Below T\* the
  notches are free — sub-Nyquist interpolation, the exact tight-frame calibration
  of the AP dichotomy (COMPUTED anchor: constant-density sub-Nyquist costs
  nothing). Above T\* each notch costs e^{−2π(1−τ)}. RH is the statement that the
  filter can never do better than dark: transmittance may be exponentially small
  but never negative — "you cannot build an amplifier out of absorption lines."

- **Dodging zeros you cannot resolve.** The margin's exponential smallness is the
  price of *anticipating* rigidity beyond the resolution limit: the minimizer
  vanishes on ~2e^ℓ zeros whose Heisenberg times exceed its observation time. The
  reason rigid spectra are CHEAP to dodge (λ larger) and Poisson expensive: frame
  conditioning. A rigid sequence at RvM density is as close to an orthogonal
  exponential system as its density allows; clumps create near-parallel frame
  vectors and crush λ. So the measured "true = maximally rigid" is an extremal
  statement about the conditioning of the zeta spectrum — Hilbert–Pólya-flavored:
  whatever operator carries the zeros, its spectrum is as well-conditioned as its
  counting function permits (echoes the below-GUE small-gap counts of §2.1).

- **What is ln λ? A tunneling exponent under the xp hyperbola.** Phase plane
  (x, ξ): the window owns the strip |x| ≤ a; the spectrum demands vanishing on the
  Planck cells under the Berry–Keating hyperbola. Between T\* and T_s the demand
  curve is above the window's Nyquist line: a classically forbidden wedge. E is
  2π × (its cell count) — the standard shape of exponentially small Toeplitz/
  prolate eigenvalues as forbidden-phase-space actions (Landau–Widom, Fuchs; and
  the reason the deep rate 4π/unit-c is basis-free physics). The instanton is the
  complex trajectory of the bandlimiting symbol crossing the wedge; its endpoints
  are the turning points at T\* (entry, free) and T_s (detachment, Airy). Seed (a)
  answered: the "potential" is the xp demand curve seen by the window's symbol,
  and the deficit term μD(T\*) in the invariant law is the wedge's area measured
  from the Nyquist side. What the instanton picture does NOT give (K2, program
  law): the mid-range constants — the wedge is filled with DISCRETE cells and the
  bulk-area approximation provably fails there. Discreteness is not a correction
  to this instanton; it is its quantization.

- **UPT in this seat's language.** The uniform transfer lemma is the missing
  QC folklore theorem: "the short-orbit sum controls its own spectral
  back-reaction, uniformly in the cutoff." Diagonal-vs-off-diagonal: Weil
  positivity with support L/2 is a positivity constraint tying the orbit sum
  (primes ≤ e^{L/2}, 'diagonal' data) to the full spectral measure — exactly the
  sum-rule bootstrap by which Bogomolny–Keating (PRL 77, 1472 (1996)) resum
  off-diagonal pairs from the Hardy–Littlewood conjecture. That the program's
  wall (F5: a-priori regularity of near-minimizers; T1PRIME Gap 1: the anchor
  hypothesis) is a *concentration* statement fits the pattern: in QC, every
  attempt to close the diagonal/off-diagonal loop stalls on controlling how much
  of the wavefunction hides at scales the orbit sum cannot see. Same wall, two
  dialects.

- **What λ(L) smells like.** Three smells, one object: (i) the lowest eigenvalue
  in the Landau–Widom plunge of a prolate operator whose "band" is chirped to the
  RvM density; (ii) a Fredholm minor — det of the sine-kernel-type operator with
  2N(T_s) imposed roots, over det without — which is why I expect the
  riemann-hilbert seat to own the deep constants; (iii) the Gaussian-ensemble
  probability of a large spectral deviation, e^{−β·(area)}, with β = 2 and area =
  the wedge — a Coulomb-gas large deviation with the zeros as the gas. Smell
  (iii) is the log-gas bet below.

---

## §4 Cross-seat bets (ranked by confidence)

**B1 — riemann-hilbert (HIGH).** The deep regime is theirs: the 4π cap is Fuchs's
exponent, and I bet the saturation constant w∞ = 1.2785 (root of e^w(w−1) = 1)
appears as a matched-asymptotics/smooth-pasting constant in a steepest-descent
analysis of the constrained chirped-sine-kernel Fredholm determinant. Concretely:
the standoff detachment at T_s is a Painlevé-II/Airy local model; the capacity
edge carries the measured (eT\*−t)^{3/2} softening with width scaling
(a·eT\*)^{−2/3}. If they can produce the o(1) term in E at the cap (the p·(L/2)
coefficient, measured 4.5–6.5), that single number is the sharpest available test
of the whole Fredholm reading.

**B2 — log-gas (HIGH).** Three interlocking bets. (i) The ensemble offset is a
number-variance functional (QC-1 = their hyperuniformity ladder): Poisson (non-
hyperuniform) −4.5 nats, GUE (log-hyperuniform, class II) sub-nat to ~1 nat — my
§5 pre-registration is jointly ours (it is also SYNTHESIS Q6) — and zeta-at-frame-
scales behaves class-I (bounded variance, Berry/Selberg saturation). (ii) The
L = 4.32 crossover is a third-order pulled-to-pushed transition (QC-4): the
standoff is a constrained Coulomb-gas equilibrium and its boundary saturation is
the Majumdar–Schehr class. (iii) The marginal law's π²/2 is a defect-potential
(single-charge extraction) energy in their gas — the Bonami–Karoui constant is a
Coulomb energy, and T4's "gluing gap potentials" step is a log-gas electrostatics
computation they can do faster than HA.

**B3 — free-boundary (MEDIUM-HIGH).** The standoff height T_s(L) is a free
boundary. NT's exact identity (super-Nyquist surplus on [T\*, eT\*] equals deficit
mass e^ℓ) is a balayage statement; the minimizer's log-envelope should be the
balayage of the deficit measure onto the window's allowed region, and I bet the
drift law e^w(w−1) = (b/2π)(ℓ+c₀) − 1 and the saturation condition e^w(w−1) = 1
are respectively the moving-boundary equation and the C¹ smooth-pasting condition
of a one-dimensional obstacle problem whose obstacle is the Nyquist line aT/π.
If they derive w∞ = 1.2785 from smooth pasting, QC-4's transition order follows
for free (obstacle problems saturate third-order generically), and C4 gets its
mechanism theorem.

**B4 — quasicrystal (MEDIUM).** The smooth RvM staircase is a chirped crystal
(a deterministic, perfectly rigid, non-periodic point set); the AP dichotomy
(constant-density lattice costs nothing — tight frame by Poisson summation) is
the crystalline-measure degenerate case, and the zeta pair (zeros, primes) is a
crystalline measure in the Guinand–Meyer sense. Bet: any Lee–Yang/crystalline
construction matching N(T) and the saturated-variance class reproduces the ENTIRE
measured envelope — the frame bound cannot distinguish zeta from a sufficiently
rigid deterministic fake. That is simultaneously a gift (T3's transfer has a
natural home in their Meyer-set rigidity theory) and a warning label on the
program: the envelope constrains Hilbert–Pólya candidates only through N(T) and
rigidity class (as §2.17 already says), so the RH-content of the margin lives
entirely in the sign, not the size. If they can build a crystalline measure with
RvM density whose frame bound VIOLATES the envelope by more than the QC-2
fluctuation, both QC-1 and T3's sharp form are in trouble.

**B5 — proof-theory (MEDIUM-LOW, but cheap to check).** The certificate depth law
δ\* = λ/‖v‖₁² (measured sharp to 0.997) says the ball-certificate cost IS the
instanton action: log(1/δ\*) ≈ E + O(log), since ‖v‖₁² grows only polynomially
(participation ratio of the minimizer). Bet: any Π₁ certification of window
positivity, in any basis (F6's prolate upgrade included), pays at least the
phase-space count — 2π nats per super-Nyquist cell — so the formal ladder's reach
is priced by semiclassics, and the "certification budget must beat e^{−E}" clause
of ENVELOPE.md is not an artifact of the current pipeline but a lower-bound
shadow of the tunneling exponent. A proof-mining version ("certificate size ≥
forbidden-cell count") would be the first complexity-theoretic statement with
semiclassical content in this program.

---

## §5 Pre-registered computable test: the GUE rung of the rigidity ladder
## (seed question (b); = SYNTHESIS adjudication Q6)

**Question.** Does form-factor lore correctly price the frame-bound cost of GUE
local statistics — between rigid (free) and Poisson (−4.5 nats) — and does that
reconcile "true zeros = maximally rigid" with GUE local statistics via the
saturation argument of §1.6?

**Protocol (fixed before any run).** Instrument: src/model_zeros.py `frame_form`,
identical configuration to the recorded mechanism experiment: L = 2.485, m = 48,
dps 50, K = 180 ordinates per model (the recorded run's "Gcut = 420" retains all
180). GUE ordinates: sample CUE (dim 256, Mezzadri QR recipe), sort eigenangles,
unfold to unit density u_k = (θ_k + π)·256/2π, anchor x_k = u_k − u_1 + 1/2, take
k = 1..180, map through the SAME inverse used by the repo's Poisson model:
γ_k = N_smooth^{-1}(x_k). Three seeds (1, 2, 3). Anchors from RESULTS.md at this
exact configuration (COMPUTED, recorded): true 2.68972e-10, smooth 2.75124e-10,
Poisson 2.89509e-12. I additionally recompute the smooth anchor once to validate
the harness. Budget: 4 eigensolves, single worker; fallback to 2 seeds if a pilot
run exceeds 8 minutes.

**Pre-registered predictions (logged BEFORE running; numbers derived in QC-1).**
Let Δ := ln λ_GUE − ln λ_smooth (nats; negative = cost).

- **P1 (location).** Median over seeds: Δ ∈ [−2.0, −0.3]; central estimate
  Δ ≈ −0.8 (λ_GUE ≈ 1.2e-10), from 𝔇_GUE ≈ 1.9 (sine-kernel Σ²(180) ≈ 0.87,
  sup-discrepancy ≈ 2σ) at the Poisson-calibrated rate 0.4 nats per unit 𝔇.
- **P2 (Q6's band).** For the median seed: |ln λ_GUE − ln λ_smooth| ≤
  (1/3)·|ln λ_GUE − ln λ_Poisson| — at least 3× closer to smooth than to Poisson
  in log distance.
- **P3 (fluctuation).** Seed-to-seed spread max−min of ln λ_GUE over 3 seeds in
  [0.2, 1.5] nats — visibly sample-dependent (a log-correlated discrepancy field),
  unlike the deterministic models.
- **KILL.** If median λ_GUE ≤ 3·λ_Poisson (≤ 8.7e-12), the variance-functional
  reading (QC-1) is dead, and GUE local statistics genuinely contradict the
  maximal-rigidity reading — the frame bound would be dominated by local clumping,
  not integrated variance, and §1.6's reconciliation fails.
- **Interpretation grid** (cost = −Δ): < 0.3 → the margin couples to the
  discrepancy field even more weakly than variance predicts (only extreme
  excursions matter); 0.3–2.0 → QC-1 confirmed as priced; 2.0–3.5 → variance
  functional right in kind, wrong in constant (c(ℓ) steeper than Poisson
  calibration); ≥ kill line → dead as above.

Results to be appended below after the run, unedited.

---

## §5R Post-run results (appended after the pre-registration above; §§0–5 were
not edited after the runs)

All artifacts in `results/ias/quantum-chaos/`: `gue_frame_test.py/.out`
(pre-registered run), `gue_frame_ext.py/.out` (post-hoc extension, 9 more
seeds + band diagnostic), `worth_weighted_check.py/.out` and `gue_iw_corr.out`
(post-hoc mechanism checks, no eigensolves). Total compute ≈ 8 CPU-min.
Harness validation: recomputed smooth anchor = 2.75124e-10, exact match to
the recorded value.

**Raw result (COMPUTED, 12 CUE seeds, L = 2.485, m = 48, K = 180).**
Δ := ln λ_GUE − ln λ_smooth per seed:
+3.81, −1.64, +2.02, +0.17, +1.33, +1.72, +4.64, −0.87, +1.33, +2.40, −0.83,
+2.72. Median +1.53, mean +1.40, spread 6.28 nats. Every seed sits ≥ 2.91
nats above the recorded Poisson value; median distance to Poisson 6.1 nats.

**Scoring the pre-registered predictions, honestly:**
- **KILL line: NOT fired**, by a wide margin. GUE local statistics do NOT
  contradict the maximal-rigidity finding; the frame bound is not dominated by
  local clumping. The reconciliation of §1.6 survives (in corrected form
  below).
- **P2: PASSED.** Median seed is 3.3–4× closer to smooth than to Poisson in
  log distance (ratio 0.25–0.31 vs the pre-registered ≤ 1/3).
- **P1: FAILED as stated.** The median is +1.53, not in [−2.0, −0.3] — and
  positive. The definite-sign "GUE pays a variance cost" model is wrong for
  single samples.
- **P3: FAILED as stated.** Spread 6.28 nats ≫ the predicted [0.2, 1.5]:
  fluctuations carry per-level worth quanta of order (π²/2)ln(eT\*/t) ≈ 2–8
  nats, not smooth-variance size.

**The mechanism, found and quantified post hoc (labeled as such).** A
diagnostic recorded before its run in `gue_frame_ext.py` predicted the sign
correlation BACKWARDS (I wrote "level deficit ⇒ cheaper dodging ⇒ Δ > 0"; the
observed anti-agreement was 11/12 the other way). The corrected sign is
elementary and I should have had it in the pre-registration: the frame form is
a sum of positive rank-ones, so deleting levels LOWERS λ (that is the marginal
law's sign), and a realized SURPLUS of levels below the capacity height raises
it. Integrating the marginal law by parts gives the first-order functional

  Δ ≈ I_w := (π²/2) ∫_{t₀}^{eT\*} ΔN(t) dt/t   (worth-weighted net charge),

and the regression across all 12 seeds (`gue_iw_corr.out`) is

  **Δ = 0.96·I_w − 0.66, Pearson r = 0.963, residual sd ≈ 0.52 nats.**

Unit slope: the marginal worths ADD at this fluctuation size (fractional-level
charges spread across the band — no conflict with kill-list K7, which concerns
coherent whole-zero removals, where ~20% non-additivity is measured).

**The corrected physical statement (the seat's main deliverable from this
test).** The frame-bound offset from the rigid staircase decomposes as

  offset = (realized worth-weighted charge, slope 1) + (intrinsic
  local-statistics cost),

with measured intrinsic costs: rigid 0 (definition), **GUE −0.66 ± 0.15
nats** (the regression intercept; SE from residuals), Poisson ≈ −2.0 to −2.7
nats (one seed: recorded offsets −4.55/−4.67 at L = 2.485/2.996 minus that
seed's realized charges −1.87/−2.68, `worth_weighted_check.out`). The
charge-corrected GUE cost lands inside the originally pre-registered P1 band
[−2.0, −0.3] — the pre-registration failed on single samples because realized
charge (±3–5 nats for 180-level GUE blocks) dominates the intrinsic cost, and
zeta is precisely the sequence for which that dominant term VANISHES:

  **I_w(true ζ ordinates) = +0.07, +0.07, +0.11 at L = 2.485, 2.996, 3.555**
  — worth-neutral to ~0.1 nats, two orders below GUE-sample charges.

This is Selberg/Berry saturation in its sharpest form: not merely bounded
variance but near-cancellation of the log-averaged discrepancy (an S₁-type
statement — Littlewood's S₁(T) = O(log T), numerically tiny), and it upgrades
§1.6: "maximally rigid" = worth-neutral, and the reason zeta beats even GUE's
intrinsic −0.66 at these heights is the measured below-GUE stiffness of the
low zeros (§2.1's 65–73% small-gap counts) combined with the worth weight
ln(eT\*/t) concentrating on exactly those low, extra-stiff zeros — which also
predicts the near-rigid offset persists at ALL L (the weight is always
bottom-anchored). QC-1 should be restated with I_w replacing the
sup-discrepancy functional; QC-2's sign-indefinite-fluctuation clause is
confirmed in mechanism but its magnitude clause transfers to the charge term.

**Two adjudication contributions for the panel (COMPUTED):**
- **Q3 (the factor 6.3 at L = 3.555):** NOT first-order charge.
  I_w(true, 3.555) = +0.11 against the measured +1.84; the residual +1.7 nats
  is > 3× the GUE residual scatter (0.52). First-order rigidity fluctuation is
  ruled out as the explanation; my data therefore leans TRUNCATION (the
  synthesis' suspicion) or a genuinely anomalous second-order local effect —
  the Gcut-escalation settling experiment remains the decider, and my
  pre-registered factor-3 criterion for the charge explanation FAILED (stated
  plainly).
- **Poisson diligence flag:** the recorded "Poisson costs 1.5–2 orders" is a
  ONE-SEED number (seed 7 at all three L), and that seed's realized charge is
  −1.9 to −2.7 nats — roughly HALF the recorded cost is sample fluctuation,
  not intrinsic clump cost. The ensemble-mean Poisson cost is closer to 1
  order (intrinsic −2.0 to −2.7 nats) with ±2–3 nat seed scatter. ENVELOPE.md
  §2b and T3(ii)'s Poisson corollary should quote the decomposition, or rerun
  with charge-matched (I_w-conditioned) samples — cheap with the scripts here.

**One falsifiable prediction left on the table** (for any seat or the deep-
windows agent): compute I_w and Δ for ~10 GUE seeds at L = 2.996 and 3.555 —
the intrinsic intercept should stay at −0.5 to −0.9 nats (weak L-dependence,
it is a local-statistics quantity) while the charge variance grows with the
band; and a semi-Poisson ensemble should land its intercept near −1.3 to −1.8
nats (log-midway). If the intercepts drift with L like the charge does, the
decomposition is wrong and QC-1′ dies.

---

## Round 2 — colloquium (quantum-chaos)

Written 2026-07-26 after reading all seven other seat files and
COLLOQUIUM-BRIEF.md. No repo file outside this seat's own was touched. All
numerics in this section are arithmetic on PUBLISHED Round-1 numbers (no new
eigensolves); the one proposed new run is pre-registered in §R2.5 and NOT
executed this round. Honesty tiers as before.

### R2.1 Bet responses (bets placed on this seat by others)

**log-gas §4 bet 3 (0.65): "Berry saturation and LG-2's prime-sum bound are
literally the same object through the explicit formula." ACCEPT — certified,
and upgraded to an independent replication.** The two seats ran the SAME
experiment (Q6) in Round-1 independence with different samplers, different
frame builders, and different functional conventions, and got the same law.
The identity: my I_w := (π²/2)∫δN(t) dt/t equals −(π²/2)·J[Γ] in their (LR)
notation (their J = −∫δN d ln t; their ΔE = −my Δ). Replication table
(COMPUTED, published numbers):

| quantity | quantum-chaos (12 anchored CUE seeds) | log-gas (10 free + anchored CUE) |
|---|---|---|
| regression slope Δ on I_w | 0.96 | 0.954 |
| Pearson r | 0.963 | 0.991 |
| intrinsic intercept (cost) | 0.66 ± 0.15 | 0.48 (bias +0.57 ± 0.16) |
| ζ charge functional | I_w = +0.073 | −(π²/2)J = +0.071 |
| anchored-sample sd | 1.92 | 1.48 (free: 3.60) |

My sampler pins x₁ = 0.5 (anchored by construction), which is why my spread
(1.92) matches their ANCHORED ensemble (1.48), not their free one (3.60) —
their P4 window-phase finding retroactively explains my sd, and their free-CUE
block shows my Round-1 P3 "spread" prediction failed even harder than I
scored. Berry saturation (my §1.6) and their ln-2 spectral gap are one
mechanism: Σ²-saturation IS the statement that the ζ counting noise has no
spectral mass below the lowest prime frequency (Parseval on the explicit
formula), and the frame functional's weight is a low-pass filter at
k ≲ 1/t₀ ≪ ln 2. Bet certified at THEOREM-shaped tier (the equivalence; the
lemma form goes to Merge M-A).

**riemann-hilbert §4 bet 3 (medium-high): two-saddle interference, w∞ as
saddle coalescence, prime amplitudes only in offsets. REFINE, two-thirds
accepted.** (i) Amplitudes-enter-offsets: accepted and independently produced
(my §1.6 ledger reading = their pump 3's theta-divisor reading — converged,
co-signable). (ii) Two-saddle/Stokes reading of the cap: REFUTED as mechanism,
including by their own pump 1 ("MIN of two convex costs … predicts the
crossover is smooth"): a genuine two-saddle exchange gives a slope-
discontinuous (first-order) transition, which the deep-windows level test
already excludes; the panel-consistent mechanism is boundary saturation of a
variational parameter (my QC-4 + FB-2's smooth pasting + renormalization's
eigenvalue −1). "Saddle coalescence" should be renamed smooth pasting.
(iii) Their Lambert form w∞ = 1 + W(1/e): verified exact (two lines;
e^{w}(w−1) = 1 ⟺ (w−1)e^{w−1} = 1/e). My QC-4 transition-order test (second/
third differences across L ∈ [3.8, 4.75]) is the remaining discriminator and
now has no live opponent predicting a Stokes jump.

**quasicrystal §4 bet 4 (0.45): Poisson penalty ≈ c·√(N ln N), growing with
L; cap = Heisenberg/Ehrenfest saturation of the form factor. REFINE /
PARTIALLY REFUTE.** The penalty is not a symmetric-variance draw: the measured
decomposition (my §5R + log-gas P5) is one-sided — deficit-amplified extreme-
value cost plus a realized charge that in the recorded seed was −1.9 to −2.7
nats of the −4.6 total. I accept the DIRECTION (the median penalty should grow
with L) but the functional is the worth-weighted extreme deficit, not √(Σ²);
the quantitative answer is exactly what the C-6 protocol (§R2.3) will return.
On the cap: T* = Heisenberg-time crossing is my dictionary and I co-sign that
half; "Ehrenfest saturation" is renormalization's P3 phrase, and I do not
endorse it as a derivation target (K5).

**magic-functions §4 bet 4 (0.45): Berry–Keating predicts the NNLS dual-atom
displacement δγ₁(L) with no free parameters. ACCEPT as a well-posed
semiclassical calculation** (the dual atom is the centroid of the lowest
spectral line as seen at observation time t_obs = L/2, shifted by the window's
leakage against the asymmetric background). First check before any formalism:
the SIGN — leakage against the rising zero density above pulls the atom UP,
so the measured DOWNWARD displacement (14.079 < 14.135) must come from the
pole/archimedean background; if a two-line stationary-phase estimate cannot
produce the sign, the bet dies cheaply. Effort: days; sequenced after Merge
M-A. Their β-dial, meanwhile, is absorbed into C-1 below — it is the same
functional in one dimension.

**renormalization P3 (c₀ as a "log-Ehrenfest constant", QC to derive):
ACCEPT the deflationary half, DECLINE the derivation.** Under the C4/w-drift
algebra c₀ = μ − 1 is a chart coordinate of the drifting standoff (my §1.7);
"bookkeeping, not arithmetic" — agreed. I decline to hunt an Ehrenfest
constant for it (K5 discipline). Separately, their R3(iii) request for Selberg
trace-formula mechanics is accepted as an interface: I will spec the windowed
Selberg form (κ = 1 lab, small-eigenvalue channel = the pole-shaped
sign-indefinite block) on request — days, not weeks.

### R2.2 Adjudications

**C-1 (rigidity trichotomy) — verdict: ONE first-order statement, three
projections; separation exists and is exactly the intrinsic term.**

The shared object is the linear response of the frame exponent to a counting
perturbation δN at RvM density:

  Δ ln λ = ∫ w(t) dδN(t) + [intrinsic] + O(2nd),  w(t) = (π²/2) ln(eT*/t),

i.e. after parts, Δ = I_w − c_int(local class) with I_w = (π²/2)∫δN dt/t.

(1) QC charge-neutrality and LG spectral-gap are the SAME functional measured
and mechanized: I_w ≡ −(π²/2)J (identity of definitions), independently
implemented, agreeing on ζ to 3% (+0.073 vs +0.071) and on slope/r (table
above). The gap statement (δN_ζ has no Fourier content below ln 2, the weight
is a low-pass filter at k ≲ 1/t₀) is the MECHANISM: it explains the measured
neutrality and predicts it for every L — strictly the strongest of the three
formulations. Berry saturation is this statement integrated (Parseval);
Selberg's CLT is its unconditional variance-level shadow.

(2) MF midpoint-phase is the same functional read along ONE direction —
uniform phase transport, for which δN = −Δβ at every staircase point and
I_w = (π²/2)·Δβ·S with their transport sum S = Σ 1/(t_k N̂′(t_k)). COMPUTED
(published numbers only): their m = 24 family gives Δ_true = ln(3.3801/3.2861)
= +0.0282, so the charge functional predicts β_eff − ½ = Δ_true/((π²/2)S) =
0.0282/8.52 = **0.00331 against their measured 0.0034** — agreement to 3%.
The midpoint-phase measurement IS charge neutrality in the uniform-phase
coordinate.

(3) THE SEPARATING EXAMPLE (requested by the brief): a charge-matched Sine₂
sample. It has I_w = 0 by construction, hence is exactly charge-neutral and
exactly "spectral-gap-compliant at the functional's window" — yet its λ sits
the intrinsic term below the staircase (pooled intercept 0.57 ± 0.13 nats),
so its effective phase reads β_eff ≈ 0.5 − 0.57/((π²/2)S) ≈ **0.433, not
0.5034**. So midpoint-phase ≠ charge-neutrality at second order: β_eff
conflates the charge term (zero for this example) with the intrinsic
local-statistics term (nonzero for Sine₂). The ζ ordinates pass BOTH tests —
charge-neutral (I_w ≈ +0.07) AND intrinsic ≈ 0 — and the second fact is
extra information: it is the below-GUE stiffness of the low zeros (§2.1's
small-gap counts), which the worth weight ln(eT*/t) samples heavily.
β_eff = 0.5034 silently certifies both.

Proposed joint statement for the panel (goes to Merge M-A): *for symmetric
configurations at RvM density with sup|δN| ≤ 2 on [0, eT*],
ln λ[Γ](L) − ln λ[smooth](L) = (π²/2)∫δN(t)dt/t − c_int + err, where c_int
depends only on the local-statistics class (rigid: 0; Sine₂: 0.57 ± 0.13
measured, two seats pooled; ζ at accessible heights: ≤ 0.1), and err is
second-order with the one-sided (deficit-amplified) form beyond sup|δN| ≈ 2
(log-gas P5).* QC owns the mechanism clause (explicit formula/saturation),
LG owns the variance/DLR theory, T4's secular identity is the proof engine,
T3/DG consumes.

**C-5 (Q3 factor 6.3) — co-signed death verdict, with riders.** My I_w(true,
L = 3.555) = +0.11 vs +1.84 required: the excess is 3.3σ of the GUE residual
scatter (0.52) around the charge line — not a first-order rigidity effect.
LG-2's low-k budget says the same with a mechanism. By the C-1 equivalence,
MF's "phase reading" of Q3 (Δβ_eff ≈ +0.1–0.2) is NOT an alternative
explanation: the phase functional is the charge functional, and the charge
isn't there. Verdict: first-order rigidity explanations of Q3 are dead;
remaining live options are Gcut truncation (both seats' lean; parsimonious)
or an anomalous second-order local effect. The Gcut-escalation experiment
(SYNTHESIS Q3 settling protocol) remains the formal decider. PRE-COMMITTED
consequences: if the excess survives Gcut → ∞, my QC-2 magnitude clause and
LG-2's quadratic bound both need repair, and the second-order (rank-two
secular) machinery must be run on the actual configuration before any
arithmetic conclusion is drawn.

**C-6 (Poisson diligence) — the charge-matched rerun protocol for ENVELOPE.md
§2b (owner deliverable).**

Protocol (instruments exist; no new code beyond glue):
1. CONFIG: L ∈ {2.485, 2.996} (add 3.555 only after Q3's Gcut escalation
   lands), m = 48, dps 50, K = 180 levels, Gcut-equivalent 420 at L = 2.485
   — the recorded mechanism-experiment configuration exactly.
2. INSTRUMENT CROSS-CHECK: 4 seeds run through BOTH frame builders
   (model_zeros.frame_form and law-theory law_core.lam_min_frame) and BOTH
   CUE samplers (this seat's QR/default_rng; log-gas's) — printed-digit
   agreement required on the anchors (rigid, true, Poisson-7) before the
   ensemble runs.
3. ENSEMBLES: ≥ 20 CUE seeds (10 free + 10 anchored) and ≥ 10 Poisson seeds
   per L. Per seed, REPORT (λ, Δ, I_w, sup-deficit, sup-surplus) — I_w and
   sup±δN are eigensolve-free.
4. DECOMPOSITION: per ensemble, regression Δ = s·I_w + c; report (s, c, r,
   residual sd). For Poisson additionally report the one-sided diagnostics
   (log-gas P5): per-seed excess over linear response, split by deficit/
   surplus side — the crossover to extreme-value behavior is expected at
   sup|δN| ≳ 2 and the surplus side should be non-refunding.
5. CHARGE-MATCHED NUMBER: the intrinsic Poisson cost = median Δ over seeds
   conditioned to |I_w| ≤ 0.3 (rejection sampling; ~1/3 of Poisson draws
   qualify), OR equivalently the regression intercept if linearity holds —
   report both; disagreement between them is itself the nonlinearity
   measurement.
6. ENVELOPE.md §2b REWRITE (after the run): replace "Poisson costs 1.5–2
   orders" with the distributional statement: "Poisson: intrinsic
   (charge-corrected) cost X ± Y nats [expected ≈ 2.0–2.7 from the seed-7
   decomposition], one-sided deficit-amplified, PLUS realized-charge scatter
   of order ±(π²/2)√(Var J) ≈ ±11 nats linear-response scale; the recorded
   1.5–2 orders was one seed, roughly half of it that seed's realized
   charge." The true/smooth rows of §2b stand unchanged (ζ charge neutrality
   is the finding). T3's Poisson corollary (ii) should simultaneously adopt
   the one-sided sup-DEFICIT hypothesis (log-gas revision 1).
7. BUDGET: ~70 eigensolves ≈ 25–40 CPU-min at the measured 6 s/solve, one
   worker. Pre-registration bands in §R2.5.

**C-11 (vector findings vs QC-3) — the node-ledger version of QC-3 is
REFUTED; the tunneling version is CONFIRMED and sharpened.** My Round-1 QC-3
conflated two readings of "2π per super-Nyquist cell". The vector data
separates them: the dodged (node) zone carries ≈ 20% of the exponent and
smallness-WITHOUT-vanishing carries 80% — so the per-NODE ledger ("|F|²
drops by 2π(1−τ) per zero dodged", my Round-1 phrasing) is dead as a
pointwise mechanism, and I retract it. But this is exactly the signature of
the TUNNELING reading: in WKB, exponential suppression is carried by the
evanescent envelope (the outer function), not by node placement — an
instanton amplitude is |F|-smallness, not interpolation. C-11's 80/20 split
says the action 2π[D(T*) − D(T_s)] is paid ~80% in evanescence and ~20% in
node bookkeeping; the ≈30%-below-T* share is turning-point leakage (the
soft-edge/Airy zone at T* has finite width), which is qualitatively standard
and quantitatively OPEN — my naive width estimate (aT*)^{−2/3} looks too
small for 30% and I flag that as a real tension for the Airy-layer picture,
not a rounding issue. Restated QC-3 (goes to Merge M-B): *on the stored deep
minimizers, the FREQUENCY-side envelope slope d ln|F(t)|²/dN(t) on
[T*, T_s], with the node contribution separated (Jensen mass at nodes vs
outer-function descent), integrates to E with an evanescent share ≈ 0.8 and
matches the g-function derivative of the constrained-equilibrium problem
(RH-2) away from the two edge layers.* The universal E-normalized profile
across the crossover (C-11's ±0.02·E collapse) is strong support for the
single-variational-problem picture underlying both QC-4 and FB-2.

**C-2 (w∞ cluster) — co-sign, with tier discipline.** I co-sign: THEOREM
(exact algebra): 4π cap ⟺ Surplus(w∞) = 2·Deficit ⟺ e^{w}(w−1) = 1, with
w∞ = 1 + W(1/e) = 1.27846 and g′(w∞) = −1 (equivalently: subleading term
p·ℓ). CONJECTURE (mechanism, one clause): w∞ is the smooth-pasting point of
the two-epoch constrained sweep (FB-2 formalization; renormalization R2's
fixed point; my QC-4's transition-order prediction — C² with third-derivative
jump — is the falsifiable rider and I ask that it be attached to the co-sign
as the test). The quasicrystal horizon-merger hypothesis (hard horizon =
e^{w∞}T*) must NOT be bundled into the statement: it is a separate conjecture
with its own kill test (the slit-plane computation, QC-3-quasicrystal), and
bundling would let one falsification take down an exact-algebra theorem.

**C-3 (p = 9/2 vs π²/2) — one physics prior, one endorsement.** Semiclassical
prior: log-coefficients of deep gap asymptotics come from local parametrices
and are half-integer-quantized (Maslov-type counting), favoring 9/2; π²/2
would mean the marginal-law unit reappears as a prefactor power, which no
mechanism on the table produces. Weakly held (the L = 5.50 triple decides;
their P3 forecast is the right test). I endorse RH's pump-4 family
discriminator (pole-free deep family ladder separates pole-rank readings of
n) as the cheapest mechanism-level test.

**C-7 — endorsed.** "λ_GUE" is a distribution; DG-P3/NT-P2 should be restated
as statements about (bias, Var J). One reconciliation note for the record:
my 12-seed mean Δ = +1.40 vs log-gas's free mean −1.34 differ by realized
mean charge (my sample drew mean I_w ≈ +2.1; theirs −1.9) — a ~2σ
fluctuation of a heavy log-correlated statistic across different generators,
plus possible mild bias from my x₁-pinning; the C-6 run's ≥ 20 pooled seeds
with both samplers settles the ensemble mean properly. Neither seat's
MECHANISM conclusion depends on it (slopes and intercepts agree).

### R2.3 Merges (2)

**M-A (with log-gas; consumers DG/T3, renormalization R1; engine HA/T4):
The First-Order Response Lemma.** Statement as in C-1 above. Division of
labor: log-gas — (VAR)/covariance theory, determinantal CLT inputs
(Costin–Lebowitz), the one-sided crossover clause; quantum-chaos — the
explicit-formula/spectral-gap mechanism clause and the unconditional ζ
corollary via Selberg's CLT (offset ≤ C·ℓ·σ_S with σ_S² = (1/2π²)ln ln T*,
plus the S₁-type cancellation sharpening); renormalization contributes the
measured dressing band η = +0.17…+0.26 (their §5) as the second-order
budget; HA's T4(i) secular identity is the proof engine; DG's T3 consumes
(the lemma is T3's sharp constant on the sup|δN| ≤ 2 class). First
deliverable: the joint statement + the pooled-data table, two pages; effort
days for the statement, the proof rides T4(i) (weeks).

**M-B (with riemann-hilbert + DG-vectors; feeds C-2 mechanism and RH-1(b)):
The Evanescent-Action Extraction.** One protocol, three consumers: on the
stored deep minimizers (L = 4.25–5.0), extract in the FREQUENCY variable
(i) the envelope slope d ln|F(t)|²/dN(t) on [T*, T_s]; (ii) the node/
evanescent split of the accumulated exponent (Jensen mass at nodes vs outer
descent) — C-11 predicts ≈ 20/80; (iii) the two edge layers (widths and
profiles at T* and T_s). RH seat supplies the g-function/parametrix
predictions (their §1.3 object IS my per-cell integrand: g′ = 2π(1−τ) away
from edges); I supply the form-factor bookkeeping and the tunneling-share
accounting; DG executes on the existing vectors (their extraction utility,
no new eigensolves). Pre-registered expectations: mid-band slope within 20%
of 2π(1−τ(t)); evanescent share 0.7–0.9; T*-layer width the open question —
report, don't gate. Kill: mid-band slope off by > 20% after basis-bias
control kills the per-cell action reading at operator level (and with it my
§1.4 as more than integrated bookkeeping).

### R2.4 Updates to Round-1 claims

1. **QC-1 → QC-1′ (restated).** The functional is I_w (charge), not
   sup-discrepancy; the ensemble ladder clause (√K : √(K/2) : √ln K : 0) is
   RETIRED in favor of the (bias, Var J) pair per C-7; the large-fluctuation
   regime adopts log-gas's one-sided deficit form. The two-seat replication
   upgrades the core regression from single-instrument COMPUTED to
   replicated-COMPUTED.
2. **QC-2 (strengthened).** The C-1 equivalence plus MF's transport check
   (marginal law predicts collective phase transport to 2.5–4.5% with zero
   fitted parameters) validate the kernel; sharpened prediction now on
   record: under Gcut escalation the true-vs-smooth offset at L = 3.555
   lands at |Δ| ≤ 0.5 nats (I_w says +0.11).
3. **QC-3 (partial retraction + restatement).** The pointwise node-ledger
   clause is RETRACTED (refuted by C-11's 20% dodged-zone share); the
   tunneling/evanescent version is the surviving claim and is now Merge M-B's
   protocol. The (aT*)^{−2/3} Airy-width estimate is flagged as in tension
   with the 30%-below-T* share — open, reported as such.
4. **QC-4 (strengthened).** Boundary-saturation now carries FB's smooth
   pasting, renormalization's eigenvalue −1 (exact for any p), and RH's own
   smoothness argument; no seat defends a Stokes jump. The third-derivative
   test stands as the order discriminator; RH's Lambert closed form
   w∞ = 1 + W(1/e) is adopted into my statement of it.
5. **§5R caveat added.** My 12-seed positive mean charge (mean I_w ≈ +2.1,
   10/12 positive band-dN) is either a draw fluctuation or mild
   sampler/pinning bias — flagged; the ensemble-MEAN question is deferred to
   the C-6 run. No mechanism conclusion changes.
6. **Co-ownership recorded.** The Poisson diligence flag is now joint
   QC/log-gas property (C-6); the protocol above is the deliverable I owed.

### R2.5 Next action (single, sized, pre-registered)

**Execute the C-6 protocol run** (steps 1–5 of the protocol; the §2b rewrite
follows it): L ∈ {2.485, 2.996}, ≥ 20 CUE (free + anchored, both samplers) +
≥ 10 Poisson seeds per L, ~70 eigensolves, ≤ 40 CPU-min, one worker, one
session including analysis. It settles THREE open items at once: C-6
(ENVELOPE §2b distributional rewrite), the QC-1′ kill test (intercept drift:
pre-registered band c_int(Sine₂, L = 2.996) ∈ [−1.0, −0.2] nats; drift
tracking the charge variance kills the decomposition), and log-gas's Var J
growth discriminator (pre-registered: Var J up by factor 1.1–1.5 from
L = 2.485 to 2.996 per the class-II ln-growth; flat Var J means the weight,
not the process, dominates). Poisson bands, pre-registered: intrinsic
(charge-matched) cost 2.0–3.2 nats at both L; ≥ 70% of seeds deficit-side
amplified beyond linear response; median raw cost growing with L. If the
panel prefers, the same session can append the 4-seed instrument cross-check
to the coordinator's record as the standing two-builder oracle for all
future ensemble claims.
