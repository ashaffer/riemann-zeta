# SEAT: Riemann–Hilbert / integrable systems

Round 1 (independent). Date: 2026-07-26. Sources read: PROGRAM.md §§2.14–2.20+§3,
ENVELOPE.md, THEOREMS.md, RH-LEMMA-MAP.md, results/RESULTS.md,
results/experts/SYNTHESIS.md (incl. errata + §5 kill list), results/agent-law-theory.md,
results/agent-deep-windows.md + agent-deep-windows/runs.csv (incl. the rungs that landed
after that report froze), results/agent-prior-art.md, results/experts/T1PRIME.md,
results/experts/FULLINF.md. No other results/ias/SEAT-*.md was opened.

Honesty tiers used throughout: THEOREM / COMPUTED / CONJECTURE / SPECULATION.
Kill-list compliance stated inline (K2 scope note is load-bearing for this seat:
bulk-prolate derivation of the MID-RANGE constants is dead; the seat's assignment
is the DEEP regime and the discreteness-aware analysis, both explicitly live).

---

## §0 Seat card

Toolkit: Riemann–Hilbert steepest descent (Deift–Zhou) and dbar extensions; Fredholm
determinants of integrable (IIKS) kernels — sine/Airy/Bessel/confluent; Toeplitz,
Hankel, and finite-interval Wiener–Hopf asymptotics with Fisher–Hartwig data
(Widom, Its, Krasovsky, Deift; Kac–Akhiezer); prolate spheroidal operators, the
commuting-ODE miracle, Fuchs/Slepian/Landau–Widom/Widom/Bonami–Karoui eigenvalue
asymptotics; Widom–Dyson-type constant evaluations; discrete orthogonal polynomials
with constrained equilibrium measures and saturation regions (Baik–Kriecherbauer–
McLaughlin–Miller); discrete Riemann–Hilbert problems and Schlesinger/Bäcklund steps
(Borodin); almost-periodic Wiener–Hopf factorization (Böttcher–Karlovich–Spitkovsky).

---

## §1 Translation: what this program's objects are in my field

### 1.1 The form is a finite-interval Wiener–Hopf operator with an almost-periodic-plus-log symbol

The repo already holds the key identity without naming its home: FULLINF Lemma F0
diagonalizes the truncated Weil form in frequency,

  Q_L(φ) = (1/2π) ∫ |φ̂(r)|² Ω_L(r) dr + P(φ),
  Ω_L(r) = Re ψ(1/4 + ir/2) − log π − Σ_{n ≤ e^{L/2}} 2Λ(n) n^{−1/2} cos(r log n),

with P rank two. Read in x-space this says exactly: **Q_L = W_a(Ω_L) + R₂**, the
truncation to the interval [−a, a] (a = L/4) of the convolution operator with symbol
Ω_L, plus a rank-two perturbation. The symbol has (i) a smooth part growing like
log|r| (Lemma A sandwich, THEOREMS.md — this is the coercivity), and (ii) an
**almost-periodic part with frequencies log n and amplitudes 2Λ(n)n^{−1/2}** — and
the exact prime truncation log n < L/2 = 2a is the statement that only AP frequencies
shorter than the interval participate. This is the classical territory of
finite-interval Wiener–Hopf operators (Kac–Akhiezer; Widom; the modern
Riemann–Hilbert treatments of finite-interval WH determinants — the sine-kernel
determinant of Deift–Its–Zhou 1997 is exactly such an object) and of almost-periodic
Wiener–Hopf factorization (Böttcher–Karlovich–Spitkovsky, *Convolution Operators and
Factorization of Almost Periodic Matrix Functions*, Birkhäuser 2002). Two immediate
readings, both I believe new to the repo's ledger:

- **Positivity as factorization.** Ω_L takes negative values (the deficit dip at
  small r: Ω_L(0) ≈ −5.37 − Σ2Λ(n)n^{−1/2} ~ −4e^{L/4}), yet RH says W_a(Ω_L) + R₂ ≥ 0
  for every a with the coupled truncation. For a FIXED symbol with a negative well,
  finite sections eventually go negative (Kac–Murdock–Szegő: the spectrum of W_a
  fills the essential range as a → ∞). Here the symbol deepens its well as a grows
  — RH is the statement that the window never resolves the well. UPT's "uniformity
  in (conductor, prime, sign)" becomes: uniform control of the (partial) AP
  factorization data of the family Ω_{L,χ}. Tier: THEOREM for the identity itself
  (it is F0 restated); CONJECTURE for the usefulness of AP-factorization language.

- **Disproof channel.** A certified negative eigenvalue = certified non-canonical
  behavior of this factorization family at explicit (a, prime set) — the Track D
  asymmetry survives translation intact.

### 1.2 The λ-ladder is a discrete integrable-kernel / constrained-equilibrium problem

Under RH (and for the model staircases unconditionally) λ(L) is the lower frame
bound of {e^{iγx}} on [−a, a]: the bottom of the spectrum of the comb-kernel operator
K(x, y) = Σ_k 2cos(t_k(x − y)) on L²[−a, a], t_k the (staircase) ordinates. Dual/Gram
side: the discrete sinc-kernel matrix G_{jk} = 2 sin(a(t_j − t_k))/(t_j − t_k) at the
N(T)-quantile nodes. In my field this pair is precisely the setting of **discrete
orthogonal polynomials with a density-constrained equilibrium measure**
(Baik–Kriecherbauer–McLaughlin–Miller, *Discrete Orthogonal Polynomials*, Ann. of
Math. Studies 164, 2007; Kuijlaars–Rakhmanov; Dragnev–Saff), where the resolvent is
encoded by a **discrete Riemann–Hilbert problem with simple poles at the nodes**
(Borodin's discrete RHPs; interpolation-problem form of BKMM). Seed question (c) is
answered YES in this precise sense: the nodes are the poles; for the true form the
primes enter equivalently as the AP frequencies of the symbol in 1.1 — two coordinate
systems for one object. Tier: COMPUTED-level dictionary (bookkeeping lemma, RH-2(i)
below); the payoff structure is what BKMM technology was built for:

- In discrete-OP asymptotics, when the equilibrium measure presses against the node
  density (the *upper constraint*), a **saturation region** forms, and exponentially
  small eigenvalue phenomena appear with rate = an explicit constrained-equilibrium
  action. The program measured exactly this (see 1.3): the dodging region [T*, T_s]
  is a saturation region in the BKMM sense. The known failure mode is also
  instructive: everything smooth about the density cancels (K2's "the margin is a
  discreteness effect" is a *theorem* in that world — the constraint is what
  survives smoothing kills).

- The prior-art sweep's §3.3 (Vandermonde/clustered-node σ_min bounds:
  Moitra, Batenkov–Demanet–Goldman–Yomdin, Kunis–Nagel) is the non-asymptotic shadow
  of the same structure; BKMM/RHP is the sharp-constant version.

### 1.3 The deep 4π cap is a saturation action; the DG identity is a g-function identity

Verified algebra (COMPUTED, three lines): with ρ(t) = (1/2π)log(t/2π), a = ℓ/2,
πρ(t) − a = ½ log(t/T*), so the doubled type-deficit integral over the dodging region
is

  2 ∫_{T*}^{T_s} (πρ(t) − a) dt = T* (e^w(w−1) + 1),   T_s = e^w T*,

which is exactly SYNTHESIS §2(iii)'s action form of the law. The deep cap
dE/dc = 4π (c = e^ℓ) is E = 2T*, i.e. **e^w(w−1) = 1**, i.e.

  w∞ = 1 + W(1/e) = 1.27846…   (W = Lambert),

and at that stopping height the pointwise excess count is exact and clean
(COMPUTED): 2πD(e^w T*) = e^w T*(1 − w), so e^w(w−1) = 1 ⟺ −D(T_s) = T*/2π = e^ℓ —
at saturation the super-Nyquist excess equals the prime-cutoff count e^{L/2},
the multiplicative twin of the NT-errata balayage identity (surplus on [T*, eT*]
= e^ℓ). In my field's language the action integral is the **g-function/Agmon
integral through the classically forbidden (super-Nyquist) region**, and the
turning point at T* (πρ − a vanishing linearly in log t) is a soft edge — this is
where the measured (eT* − t)^{3/2} softening (law-theory RUN 4(iii); C3(iii)'s Airy
zone) belongs. Seed (b), first half, answered honestly: the L = 4.32 crossover is
NOT the Landau–Widom plunge transition (that identification is dead — law-theory
§2.2 killed LW-plunge shapes, and I concur: the LW plunge width log c has the wrong
sign of L-dependence for the (ℓ + c₀) factor). The correct reading is a **strategy
switch / budget exhaustion**: the discrete dodging action T*(e^w(w−1)+1) exhausts
the fixed bulk barrier 2c = 2T* precisely at e^w(w−1) = 1 (see §3, pump 1). Seed
(b), second half: I know of **no occurrence of e^w(w−1) = 1 in the prolate or
RH-problem literature** (UNVERIFIED as a literature claim; w∞ = 1 + W(1/e) is a
Lambert-point of the specific RvM action, and Lambert-type endpoint equations do
arise in constrained-equilibrium/saturation endpoints, but I cannot cite this
equation). It should be *derived*, not matched (RH-2).

### 1.4 The deep constants (A′, p) are Widom–Dyson-class data; the comparator dictionary

Fuchs's theorem (Fuchs, JMAA 9 (1964), Thm 1; BJK eq. 2.9 transcription in
agent-prior-art §3): 1 − λ_n(c) ~ 4√π (8ⁿ/n!) c^{n+1/2} e^{−2c}. Connes's §6.4
comparator is Fuchs at n = 4 with c = 2πe^ℓ = T* (verified numerically by the
prior-art sweep, §7.1). In the program's chart ln λ = A′ − 4π e^ℓ + p·ℓ this
comparator says:

  action 2c = 4π e^ℓ  (matches the measured cap to 0.4–1.3%);
  p = n + 1/2 = 9/2;
  A′(1−χ₂) = ln[(2¹⁴/3)√2 π⁵] = 14.6757  (χ₂² = λ₄; 1−χ₂ ≈ (1−λ₄)/2),
  A′(1−λ₄) = 15.3688.

The structure (action + half-integer-quantized log-coefficient + a constant) is
exactly the shape of every deep gap/emptiness asymptotic my field owns — compare
ln E_sine(s) = −s²/8 − ¼ log s + (1/12)log 2 + 3ζ′(−1) (Dyson's constant; proofs:
Krasovsky 2004, Ehrhardt 2006, Deift–Its–Krasovsky–Zhou 2007). **A′ is a
Widom–Dyson-type constant for the staircase frame problem — a new constant of that
class — and p is the analog of the −1/4, fixed by the local parametrices, not by
fits.** The measured menu for p: Fuchs-form free fit 6.5, 4π-pinned 4.93, Fuchs n=4
gives 4.5. Note π²/2 = 4.9348 sits on the pinned value to 0.1% — flagged in §2/§5
as a candidate identification and stress-tested there (K5 discipline: no constant
identification from fits alone; this one comes with a mechanism candidate and a
kill test). Seed (d), answered: **π²/2 is the standard exponent quantum of the
in-gap prolate decay laws** — Bonami–Karoui (ACHA 42 (2017); BJK eq. 2.10):
λ_n(c) ~ ½ exp(−π²(n+½)/2 · ∫_Φ^1 dt/(t E(t)²)) — one unit of deleted index costs
π²/2 times a conformal (elliptic-integral) factor; the measured marginal law
(π²/2)·ln(eT*/t) reads as that unit times the factor degenerated to the hyperbolic
distance ln(eT*/t) to the capacity edge in the RvM grading. I know of no
*published* single-node-deficiency frame asymptotic with the constant π²/2 for
growing-density systems (UNVERIFIED absence; the constant-density analog is
literally BK). Deriving it is RH-3.

### 1.5 Kill-list compliance

K2: nothing below derives mid-range (b, c₀, μ) from bulk functionals; the bulk
Fuchs barrier is used only where SYNTHESIS licenses it (deep cap, Q1's live
hypothesis) and only jointly with the discreteness scaffold. K5: the two constant
identifications proposed (p, A′) are stated with mechanisms and pre-registered kill
tests, never from L-scan fits alone. K6/K1: nothing references threshold distance
or corner kinks. K7: no additive per-zero accounting is used anywhere (the action
is an integral with shared suppression built in). K8: keyhole/node phenomena cited
only as pipeline validation.

---

## §2 Candidates

### RH-1 (HEADLINE). The Deep Saturation Asymptotics — (4π, p, A′) for the rigid staircase

**Statement (CONJECTURE, precision-graded).** Let Λ_sm be the smooth RvM staircase
(N(t_k) = k − ½, both signs), a = L/4, and λ(L) the lower frame bound of
{e^{it_k x}} on [−a, a]. Then as L → ∞:

  ln λ(L) = A′ − 4π e^{L/2} + p·(L/2) + o(1),

with
 (i) [rate] the action 4π e^{L/2} = 2T*, equivalently: the stopping height
     saturates at T_s → (1 + W(1/e))-point, e^{w∞}T* = 3.5911·T*;
 (ii) [log coefficient] p ∈ {9/2, π²/2} — primary candidate **p = 9/2** if the
     minimizer's deep universality class is literally Fuchs index n = 4; challenger
     **p = π²/2** if the log-coefficient is instead one BK unit (the marginal-law
     constant reappearing as the prefactor power; mechanism: the anchor zero's
     worth). These differ by 0.43·ℓ — decidable at L ≥ 5.5 (§5);
 (iii) [constant] A′ is a computable Widom–Dyson-type constant. It is NOT the
     Connes/Fuchs comparator constant: pre-registered expectation (§5) is
     A′ − 14.676 ∈ [1.5, 2.5] — same universality class, different determinant,
     different constant. Candidate closed forms are a §3 speculation only.

**Proof route.** Two-sided, deliberately split:
 (a) Upper bound with the right (rate + log) — the constructive side: chirp ×
    canonical product over the staircase to T_s, optimized at T_s = e^{w∞}T*; this
    is T5's shaped upper bound with the stopping height *imposed*, and the
    (e·c/(4n))-type bookkeeping of Widom's fixed-c large-n regime controls the
    normalization. Effort: weeks–months, joint with HA/law-theory P4 (their
    numerical ansatz is the pre-test: if E_ansatz misses by a growing factor, this
    dies before any hard analysis).
 (b) Lower bound (the field's contribution): dbar/RH steepest descent for the
    discrete sinc kernel at RvM quantiles, BKMM saturation machinery; the
    saturation-region g-function reproduces (i) at leading order and the local
    parametrices at the two edges (soft/Airy at T*, free-boundary edge at T_s) fix
    p; the constant A′ comes from the global parametrix normalization — the same
    pipeline that produced the Widom–Dyson constant proofs. Effort: research-grade,
    6–18 months for (p, A′); the rate alone is the realistic first paper.
 (c) A cheap conditional shortcut for the rate's lower side: the CC Sonin-space
    compression inequality (Connes–Consani Selecta 2021 bound the Weil functional
    below by prolate/Sonin data on their window; UNVERIFIED whether their
    machinery yields λ ≥ const·(1−χ₂-type) uniformly in the deep window — if it
    does, the floor is exactly the Fuchs barrier and (i) follows from (a)+(c)).

**Interfaces.** Consumes T3 (rigidity transfer) to carry the result from the
staircase to ζ; consumes C4's vector-level stopping-height test (DG) as the
mechanism check; feeds M3 directly: the UPT normalization N_p of PROGRAM §3 is
*this* envelope, and a proved deep law turns "divide out the envelope" from
phenomenology into definition. Feeds Track E: (4π, p, A′) are three more constants
any Hilbert–Pólya candidate must reproduce.

**Kill criteria.** (1) DG's vector-level shape test refutes the smooth cap → (i)
dies as stated (rate becomes an inequality). (2) The finished L = 5.50 ladder's
Aitken limit off the §5 forecast band by > 1.5 nats → (ii)-primary dies. (3) A′(p)
drift monotone > 0.5 nats across L = 4.25–5.5 at both p candidates → the whole
one-log-term chart is wrong (a second log-scale is present) → back to (b) with a
two-parametrix ansatz. (4) Family deep ladders (q = 3, 5, 7) showing cap rate ≠ 4π
in T*_χ units kills universality of (i).

### RH-2. The dictionary lemma + the constrained-equilibrium scaffold

**Statement.** (i) [bookkeeping lemma — days–weeks, COMPUTED-checkable] The
resolvent of the staircase frame operator is encoded by an explicit discrete RHP:
M(z) meromorphic with simple poles at ±t_k, residue condition with nilpotent
weight carrying e^{±2iaz}, and λ(L) = the smallest z²-spectral point where the RHP
loses solvability; equivalently the Gram determinant is a discrete-IIKS Fredholm
determinant. (ii) [scaffold — months] The associated constrained equilibrium
problem (external field from the log-symbol; upper constraint = the node density
ρ(t)dt) has a saturation region [T*, T_s(L)], the free endpoint solving the
Lambert-point equation of §1.3 in the deep limit; the leading exponential rate of
λ(L) is twice the constrained-energy deficit = the DG action identity, proved
rather than fitted.

**Route/effort.** (i) is Borodin-style bookkeeping; (ii) is a transplant of BKMM
Chapters 4–7 with a log-density lattice instead of a linear one. First test
mandatory (kill-or-live in one day): the formalism must reproduce EXACTLY the
solved AP dichotomy of law-theory §2.1 (tight frame 2π/s₀ sub-Nyquist; λ = 0
super-Nyquist, via anti-periodization = the theta-divisor degenerating). If it
cannot, stop.

**Interfaces.** This is the free-boundary seat's obstacle problem in my
coordinates (the variational inequality of the constrained equilibrium IS an
obstacle problem — I place a §4 bet on the meet); it is also T5's missing
technology and would upgrade C4 from identity-with-hypothesis to mechanism.

**Kill criteria.** Failure at the AP calibration; or the dbar error terms
provably cannot close below the exponentially small scale (known hard point:
exponentially-small-in-gap analysis requires the full theta-divisor asymptotics —
if the staircase's non-stationary phase produces a dense divisor, the method
stalls and says so explicitly).

### RH-3. The marginal law as a one-node Schlesinger step (π²/2 derived)

**Statement (CONJECTURE).** Deleting one node at height t from the staircase is a
rank-one Schlesinger/Bäcklund transformation of the discrete RHP of RH-2(i); the
exponent worth equals twice the g-function evaluation at the deleted node,

  f(t) = 2[g₊ − g₋](t) + o(log) = (π²/2)·ln(eT*/t)·(1 + o(1)),  t ≤ (1−δ)eT*,

i.e. the measured Bonami–Karoui constant is the residue of one BK index unit under
the RvM grading, and the capacity endpoint eT* is the point where the constrained
equilibrium's effective band edge sits (D-balayage height; NT errata item 3).

**Route/effort.** The identity layer is HA's H2(i) secular formula — already
verified exact in the FF pilot; my seat's addition is the asymptotic evaluation of
|ψ̂₋(t₀)|²/λ₋ via the RHP reproducing kernel, weeks–months, natural joint
deliverable with HA (they own gluing; I own the parametrix evaluation). The FF
calibration C1 (AG seat) is the control: at constant density the same computation
must return worth ≡ 0 (their exact dichotomy), and π²/2 must emerge only under
grading — a sharp internal consistency check.

**Kill criteria.** NA's P3 closure test failing > 40% (already HA's falsifier);
or the RHP evaluation producing a t-profile ≠ ln(eT*/t) shape (e.g., ln²) —
law-theory's nine-point plateau at 0.98–1.04 × π²/2 says this dies only if the
measurement was systematically fooled.

### RH-4. The AP-symbol program (structural; cheapest statements, longest horizon)

**Statement cluster (CONJECTURE/SPECULATION).** (i) Kac–Akhiezer two-term
asymptotics for ln det of W_a(Ω_L): the second (Szegő-type) term is
∫₀^∞ u·|(log Ω_L)^∧(u)|² du, and the AP part of Ω_L makes it a sum over prime
powers — *the explicit formula reappears as the Szegő correction of the truncated
Weil determinant*. Making this exact for the coupled truncation (symbol growing
with the interval) is new territory: the natural first theorem is the two-term
expansion for FIXED prime set as a → ∞ across one window. (ii) UPT reformulated:
positivity for all L = uniform canonical AP factorization along the family
Ω_{L,χ} with the coupling log n < 2a; the "ledger inequality" (PROGRAM §2.10)
becomes a statement about partial AP indices under sign twists. Effort: (i)
months; (ii) is a language, not yet a lemma — its value is that factorization
indices are integers: a *discrete* obstruction category for the disproof channel.

**Kill criteria.** If the rank-two pole term cannot be absorbed into the symbol
normalization on the window (I expect it can — finite rank perturbs determinant
asymptotics multiplicatively), or if (i)'s coupled truncation destroys the
two-term structure at the first window (numerically checkable with existing
instruments in an afternoon).

---

## §3 Intuition pumps (all SPECULATION unless marked)

1. **Budget exhaustion selects w∞.** The minimizer dodges zeros as long as the
   accumulated dodging action T*(e^w(w−1)+1) is below the bulk concentration
   barrier 2c = 2T* (the Fuchs cost of simply being tiny across the whole
   super-Nyquist region). Dodging past e^w(w−1) = 1 buys nothing — the bulk
   barrier already delivers the suppression. Hence the cap is *exactly* 4π per
   unit e^{L/2} and the stopping height is the Lambert point 1 + W(1/e): the
   mid-range law is "discreteness is winning", the deep law is "the prolate
   barrier has caught up". This reading makes the two-regime structure a MIN of
   two convex costs — and predicts the crossover is smooth (as measured: the
   scalar shape test favored B_smooth) because the switch is between strategies
   of a common variational problem, not between phases.

2. **The explicit formula as a Szegő correction.** In RH-4(i) the prime sum sits
   where u·|ĝ(u)|² sits in Kac–Akhiezer/Szegő strong limits. The zero side (comb
   kernel) and prime side (AP symbol) are the two classical expansions of one
   finite-interval WH determinant — Guinand–Weil is, operator-theoretically, the
   equality of a Widom trace formula's two evaluations. If a version of this
   survives rigor, "adding the prime p" (Track C) is adding one AP frequency to a
   symbol — and the ledger inequality is a perturbation statement about
   determinants under one-frequency symbol updates, a genuinely Toeplitz-native
   question.

3. **Poisson echoes / theta-divisor reading of "density, not arithmetic".** Poisson
   resummation of the staircase comb kernel Σ_k e^{it_k u} over the harmonic index
   turns it into arch-part + Σ_{m≥1} stationary-phase echoes with phase 2πm N(t).
   For the true zeros the echoes ARE the primes (explicit formula); for the smooth
   staircase they are a continuum of harmonics with the same phase function. The
   measured λ-equality of true vs smooth (§2.17) says the frame bottom feels only
   the phase 2πN(t) mod 2π — the theta-divisor — not the echo amplitudes. That is
   exactly what a Riemann–Hilbert outer parametrix would predict: amplitudes enter
   the O(1) prefactor (the offset, where Poisson loses 1.5–2 decades), phases enter
   the action.

4. **The index n = 4 as pole rank × parity (and a family discriminator).** In the
   CC framework the comparator eigenvalue is χ₂, i.e. prolate index 2k = 4 at
   k = 2 — plausibly the two pole vectors e^{±x/2} (rank-two R₂) each costing one
   angle index, doubled by evenness. If so, **pole-free Dirichlet forms should cap
   with a DIFFERENT log coefficient** (k = 0 or 1: p = 1/2 or 5/2 in T*_χ units)
   while ζ keeps p ≈ 9/2. If instead p = π²/2 is a BK unit (mechanism 1.4), p is
   family-universal. One deep family ladder (q = 3, L ≈ 7–8, m to convergence)
   discriminates three hypotheses at once. This is my seat's cheapest genuinely
   new *measurement* proposal beyond §5.

5. **A′ numerology, quarantined (K5).** The §5 extraction (see outcome) gives
   A′(p = 9/2) = 16.75 ± 0.10 against the Connes/Fuchs 1−χ₂ constant 14.676:
   Δ = 2.08, e^Δ ≈ 8.0. "A′ = A′_Fuchs + 2" (two extra e-folds — the
   anchored-Jensen horizon is at e²T*, two e-folds above Nyquist) predicts 16.676,
   0.08 below the measured mean — inside the window spread, memorable, and almost
   certainly a trap; it earns exactly one falsification attempt at L = 5.5/6.0 and
   no theory investment until then. Worse: ln(2^{29/2}π⁵) = 15.7734 matches the
   measured A′(π²/2) = 15.768 to 0.005 — a four-digit coincidence of exactly the
   kind K5 was written for. Same quarantine, same test, no investment.

---

## §4 Cross-seat bets (ranked by confidence)

1. **Free-boundary seat (highest).** Their obstacle problem for the minimizer's
   envelope is the constrained-equilibrium variational inequality of RH-2(ii) in
   different clothes; the coincidence set is my saturation region [T*, T_s]. BET:
   they derive the stopping-height law with e^w(w−1) = (b/2π)(ℓ+c₀) − 1 in the
   drift regime and the Lambert point 1 + W(1/e) at the cap, from balayage onto
   the constraint — and their smooth-fit (C^{1,1}) condition at the free boundary
   is the (eT*−t)^{3/2} / Airy softening. If we both land it independently, the
   two proofs glue into RH-2(ii)'s hardest half.

2. **Log-gas seat (high).** The action/rate is density-functional; the OFFSETS are
   where local statistics live (A mid-range, A′ deep; Poisson costs 1.5–2 decades;
   true ζ sits at the maximally-rigid offset). BET: the offset difference between
   point processes is the fluctuation free energy — computable as an integral of
   the number-variance kernel against the squared g-function derivative — and the
   GUE point (Q6) will land within ~1 nat of the smooth staircase, far from
   Poisson, because number variance ~ log is rigidity class, not Poisson class.
   Their machinery should also settle whether A′(true ζ) − A′(staircase) → 0
   (Q3's factor-6.3 anomaly at L = 3.555 is the current threat to that).

3. **Quantum-chaos seat (medium-high).** The doubled type-deficit action
   2∫(πρ − a)dt is an *excess phase-space action* above the Heisenberg/Nyquist
   crossing; the Poisson echoes of pump 3 are their periodic-orbit sums (phase
   2πmN(t) = m × spectral counting = the "Heisenberg-time harmonics"). BET: they
   reproduce the 4π cap as a two-saddle (m = 1 echo vs boundary) interference
   bound and read w∞ as the saddle-coalescence point; and they will independently
   flag that the prime amplitudes only enter offsets — matching pump 3.

4. **Magic-functions seat (medium).** The deep minimizer (chirp × product,
   stopping at T_s) is a one-sided extremal band-limited function with prescribed
   vanishing — their native genre (Beurling–Selberg with nodes on a chirped
   lattice). BET: their interpolation-basis technology gives the sharp
   constructive upper bound in RH-1(a) faster than my steepest-descent lower
   bound arrives, and the constant they extract for the anchor cost will be the
   +2-nats gap of pump 5 — deciding whether it is real structure or RR bias.

5. **Quasicrystal seat (exploratory).** Ω_L's AP part is a finite approximant of
   the crystalline-measure side of the explicit formula. BET (low confidence,
   high payoff): the mid-range→deep crossover corresponds to the scale where the
   truncated AP symbol stops resolving the "quasicrystal" (window shorter than
   the pattern's repetition scale), and their Lee–Yang/crystalline rigidity
   theorems give a clean statement of WHY all-plus signing is the unique positive
   one (C5) — sign twists destroy the crystalline positivity certificate.

---

## §5 The cheap computable test (pre-registered, then executed)

**Test.** Pinned-action constant extraction on the recorded deep-window ladders —
pure arithmetic on runs.csv numbers (< 1 CPU-second, no eigensolves):
compute A′(p) = ln λ_lim + 4π e^{L/2} − p·(L/2) per converged deep window
(Aitken limits of the deepest triples, including the three rungs that landed after
the deep-windows report froze: 4.60/m=160, 5.00/m=160, the full 5.50 triple), for
p ∈ {9/2, π²/2, 11/2, 6.5}; flatness across L selects p; the flat value is the
measured Widom–Dyson-type constant A′; compare against the exact Connes/Fuchs
comparator constants 14.6757 (1−χ₂) and 15.3688 (1−λ₄).

**Pre-registered predictions (logged before running `extract_constants.py`;
disclosure: coarse by-hand previews of rows of this arithmetic were done while
planning — the script is the authority and nothing below was adjusted after it
ran).**

- P1: the 4π-pinned free fit gives p ∈ [4.3, 5.1] — consistent with 9/2, marginal
  for π²/2, excluding 11/2 and the free-fit 6.5 (which I predict was carried by
  unconverged raw upper bounds, not the Aitken limits).
- P2: A′ is NOT the comparator constant: A′ − 14.676 ∈ [+1.5, +2.5] — same class,
  different determinant. (Fuchs-literal (p, A′) = (4.5, 14.676) jointly REJECTED.)
- P3: the resulting law forecasts the L = 5.50 true limit at
  log₁₀λ ∈ [−73.2, −72.3]; the recorded m = 184 rung (4.3e−69) is ≥ 4 decades
  above it and mid-plunge, adjudicating nothing yet; the finished ladder + one
  m ≥ 200 rung should land in the band (this is also deep-windows' own band —
  agreement there is consistency, not novelty; the novelty is P2's Δ).
- P4 (falsifier): if flatness demands p > 5.5, both §2 identifications die and
  RH-1(ii) reverts to "p unknown, parametrix-determined".

**Outcome (script: results/ias/riemann-hilbert/extract_constants.py; full output
in extract_constants.out alongside; COMPUTED tier).**

Aitken limits of the deepest triples (all convergence-flagged OK on the fit set):
λ_lim = 5.2286e−35 / 7.8546e−41 / 2.1002e−43 / 1.8612e−47 at L = 4.25/4.50/4.60/4.75
(the new m = 160 rung moves L = 4.60 below the deep-windows report's quoted Aitken
2.336e−43 → 2.100e−43 — its staircase descent continued, exactly as SYNTHESIS Q1
warned); L = 5.00 soft (6.57e−55 indicative); L = 5.50 mid-plunge, excluded.

- **P1: PASS.** 4π-pinned free fit over the four converged windows:
  **p = 4.81, A′ = 16.05** (residuals ≤ 0.044); sensitivity: drop L = 4.60 →
  p = 4.88; raw deepest rungs (no Aitken) → p = 4.85; L = 4.25 at its staircase
  bracket floor → p = 4.92. Combined reading: **p = 4.85 ± 0.10 (stat) with a
  one-sided systematic toward smaller p** (all λ are RR upper bounds and the bias
  grows with L, inflating the fitted slope). p = 11/2 and the old free-fit 6.5 are
  excluded (A′ flatness spreads 0.17 and 0.41, the latter monotone); **both 9/2
  (spread 0.095) and π²/2 (spread 0.074) survive**, π²/2 mildly favored by the
  central values, 9/2 favored by the bias direction — not separable on this data,
  exactly as pre-registered.
- **P2: PASS — the headline number.** A′(p = 9/2) = 16.752 mean (window spread
  0.095): **Δ = +2.076 above the Connes/Fuchs 1−χ₂ constant 14.6757**
  (e^Δ = 7.98), and +1.38 above the 1−λ₄ normalization. The literal Fuchs-n=4
  pair (4.5, 14.676) is jointly rejected by ~2 nats of constant at matched action
  and log-slope. Interpretation (CONJECTURE tier): the deep staircase/ζ frame
  problem lies in the Fuchs universality class — same action 2c, half-integer-
  compatible log coefficient — but its prefactor is a DIFFERENT Widom–Dyson-type
  constant, i.e. a genuinely new constant for RH-1(b) to compute. The soft
  L = 5.00 point reads A′ = 17.08 at p = 9/2, +0.33 above the fit — the right
  sign and size for its residual RR bias, consistent rather than contradicting.
- **P3: LOGGED.** Measured-law forecasts: log₁₀λ(5.50) = −72.6 to −72.7 (my band
  [−73.2, −72.3] ∋ all variants; deep-windows' own Fuchs-form band −72.6 ± 0.1
  agrees); Connes/Fuchs-literal predicts −73.6 — **one full decade below: the
  finished L = 5.50 ladder (m ≈ 200–216 + Aitken) separates P2's Δ from zero at
  ~10σ of its window spread.** At L = 6.00 the separation grows to ~1 decade
  (−96.4 vs −97.4). This is the single cheapest decisive follow-up measurement
  this seat can request.
- **P4: not triggered** (no flatness demand for p > 5.5).

Standing corrections this run makes to the record: the deep-windows report's
4π-pinned p = 4.93 was computed against the pre-final L = 4.60 value; with the
landed m = 160 rung the pinned extraction moves to 4.81–4.92 across variants
(same conclusion, updated center), and the L = 4.60 limit of record should be
≈ 2.10e−43, not 2.336e−43.

---

## Round 2 — colloquium (riemann-hilbert)

Written after reading all seven other seat files + COLLOQUIUM-BRIEF.md
(C-1…C-11). Honesty tiers as before. New numerics in this section: only the
C-3 discriminator arithmetic (decision rule written BEFORE the triple was
scored; inputs are all previously published numbers; verification script
`results/ias/riemann-hilbert/c3_discriminator.py` + `.out`).

### R2.1 Bet responses (every bet placed on this seat)

**FB bet 1 (0.8) — ACCEPT, convergence confirmed.** The free-boundary seat
predicted I would independently identify the dodge zone as BKMM
constrained-equilibrium/saturation geometry and propose steepest descent on
the graded-lattice frame problem: both happened verbatim (my §1.2, RH-2),
under Round-1 independence — the identification is now two-seat convergent
and I co-sign their FB-1/FB-2 formalization. Joint Q7 deliverable accepted:
in BKMM the saturated-band junction is Airy *in the dual* (saturation ↔ void
under μ ↦ σ − μ), so my parametrix reading predicts Airy softening with
width (a·eT*)^{−2/3} at the capacity edge — i.e. HA-P2 should land u_half
≈ 2.29, not 2.0 (FB's calibrated number; I adopt it). On the π² vs π²/2
bookkeeping I owe them: REFINE, not yet resolve. FB's quoted "plunge slope
π²" is the plunge-PROFILE rate (ln(1/λ_n) ≈ π²(n − n_c)/ln c, the Fermi
profile); the deep-decay unit is π²/2 per index (BK). These are different
regimes and must not be mixed. The staircase deletion is rank-two — one
index in EACH parity sector — and the per-sector/per-pair factor audit is a
half-page computation I take as my slice of Merge B (R2.3). Not done here;
promised, with the honest risk that it produces π²/4-per-index tension
rather than closure.

**Log-gas bet 2 (0.7, π²/2 on this seat) — ACCEPT half, REDIRECT half.**
(i) π²/2 via the BK/defect-potential route: accepted, it is RH-3 = my slice
of Merge B. (ii) "the Sine₂ frame-cost distribution is a Painlevé-V
computation": REDIRECT — their own data refutes the framing they offered
me. corr(u₁, ΔE) = 0.945 and corr(ΔE, (π²/2)J) = 0.991 say the spread is a
LINEAR statistic of the configuration read through the worth kernel; its
distribution is therefore Gaussian-with-log-variance by the determinantal
CLT (Costin–Lebowitz/Soshnikov class), and I endorse their Var J band
[0.4, 0.9] (measured 0.575) as a covariance quadrature, no Painlevé needed.
Where Painlevé/Fisher–Hartwig genuinely enters is the intrinsic intercept
(−0.66 ± 0.15 nats): that is a local, gap-probability-adjacent object — the
right target for my machinery, and a cleaner one than the full distribution.

**Renormalization bet 2 (medium-high) — ACCEPT (a) with a sharpening that
partially deflates it, ACCEPT (b).** (a) p = n + ½: adopted as primary
hypothesis (RH-1(ii)); my post-freeze extraction gives p = 4.85 ± 0.10 with
one-sided RR bias toward smaller p — compatible with 9/2, tight against
π²/2. The sharpening: their "cap eigenvalue −1" clause is AUTOMATIC algebra,
not evidence — at any root of e^w(w−1) = 1, the FB flow w′ = g(w) =
(1 − e^w(w−1))/(e^w w) has g′ = −N′/D = −1 identically (N′ = −e^w w = −D).
The falsifiable content is not the eigenvalue; it is the RESONANT approach
(R2.2, C-2(I)(c)): the forcing p·ℓ makes the approach ℓe^{−ℓ}, not Ce^{−ℓ} —
the flow is non-autonomous at exactly the order their ODE is written.
COMPUTED support: my §5 flatness of A′(p) across four windows at fixed p is
precisely the statement that the subleading term is O(ℓ) and not c^θ —
their eigenvalue-−1 clause, confirmed at the only level at which it is
falsifiable. (b) Airy width (a·eT*)^{−2/3}: accepted, same object as FB's Q7
clause above.

**Quantum-chaos B1 (HIGH) — ACCEPT.** w∞ as a matched-asymptotics constant
in steepest descent of the constrained chirped-kernel problem: yes — in my
coordinates it is the free-endpoint condition of the constrained
equilibrium (Merge A). Their Painlevé-II/Airy local model at the detachment
point T_s: agreed. The "o(1) term p" they called the sharpest test of the
Fredholm reading: delivered as measurement (p = 4.85 ± 0.10, §5); its
derivation is RH-1(ii) and remains the seat's hard deliverable.

**Magic-functions bet 3 (0.6) — PARTIAL ACCEPT, one clause REFUTED.**
Accept: E + A as −log det of an explicit structured determinant; the
marginal law as its log-derivative under one-atom deletion (Merge B); the
capacity-edge Airy discriminator. REFUTE the dichotomy "b in a Painlevé
σ-form or nowhere": b is a crossover/trajectory amplitude (I co-sign the
renormalization seat's classification table) — σ-form ODEs govern few-scale
transition regimes, and the mid-range (b, μ) is an integral over the whole
crossover trajectory. The correct object in my field is the full g-function
of the constrained equilibrium (BKMM), at T5 price. So MF should NOT lower
MF-1(c)'s hopes when no σ-form materializes; that test was miscalibrated.
Their β-dial result is absorbed into my scaffold as a rider (R2.4, U3).

### R2.2 Adjudications

**C-2 — the w∞ cluster: draft co-signed statement (FB, renorm, QC,
quasicrystal, RH; DG data).**

> **The w∞ Saturation Statement (draft for co-signature).**
> Notation: E = −ln λ, ℓ = L/2, c = e^ℓ, T* = 2πc, D(T) = (a/π)T − N̂(T);
> stopping chart w(ℓ) defined by E + A = 2π[D(T*) − D(e^w T*)]
> = T*(e^w(w−1) + 1).
>
> **(I) THEOREM (exact algebra; provable today; no mechanism assumed).**
> (a) The following are equivalent as ℓ → ∞: dE/dc → 4π; E + A = 2T*(1+o(1));
> the swept surplus 2π[D(T*) − D(T_s)] → 2·(deficit mass e^ℓ)·2π/2π [FB mass
> form: Surplus = 2·Deficit]; e^w(w−1) → 1; −D(T_s) → e^ℓ [RH excess-count
> form]; τ_H(T_s) → t_obs + w∞ [QC form]; dE/dM → 4π, M = e^ℓ [renorm form].
> The root is w∞ = 1 + W(1/e) = 1.2784645, equivalently the fixed point of
> w = 1 + e^{−w}; T_s/T* → e^{w∞} = 3.5911.
> (b) At the root, e^{w∞}·w∞ = 1 + e^{w∞}; consequently the autonomous flow
> w′ = g(w) has g(w∞) = 0 and g′(w∞) = −1 *identically* — the eigenvalue −1
> is structural, not empirical.
> (c) **Chart dictionary (this seat's contribution).** If moreover
> E = 4π e^ℓ − p·ℓ − A′ + o(1), then
>   w(ℓ) = w∞ − [p·ℓ + (A′ − A)]·e^{−ℓ} / (2π(1 + e^{w∞})) + O(ℓ²e^{−2ℓ}):
> the deep-chart pair (p, A′) and the stopping-height approach law are ONE
> datum; the approach is resonant (ℓe^{−ℓ}), i.e. the w-flow is
> non-autonomous at the order the ODE is written. Consistency check
> (COMPUTED, hand-verifiable): with (p, A′) = (4.85, 16.75) from my §5 and
> A = 11.5 (the w_E2 estimator's own offset), the formula reproduces all
> five converged w_E2 values — 1.2141/1.2194/1.2214/1.2244/1.2290 predicted
> vs 1.2136/1.2192/1.2211/1.2243/1.2282 measured at L = 4.25…5.00 — to
> ≤ 0.001. This is a CONSISTENCY identity (both charts transform the same
> λ data through the same action algebra), NOT independent confirmation;
> its value is that five seats' languages are now one formula.
> **(II) CONJECTURE (the mechanism; one clause per seat).** For the rigid
> staircase, E satisfies (I)'s saturation because the dodging maximin's
> optimality system is a constrained-sweep obstacle problem whose free
> boundary stops when the swept surplus has repaid the deficit twice [FB];
> equivalently the discrete dodging action exhausts the bulk Fuchs barrier
> 2c at c = T* [RH]; equivalently dE/dM flows into the 4π fixed point [ren];
> with third-order (pulled-to-pushed) crossover at L ≈ 4.32 [QC]. The
> quasicrystal seat's horizon-merger hypothesis (sharp anchored horizon
> = e^{w∞}T*) is COMPATIBLE with but NOT implied by this statement; it is
> QC-3's slit-plane computation and stays a separate claim (my prior: 0.4 —
> T_s is variational, the hard horizon is a type/Jensen obstruction; they
> need not coincide).
> Kill criteria: DG vector-test drift verdict; converged deep secant slope
> off 4π by > 0.5%; the L ≥ 5.5 ladder violating (I)(c)'s dictionary by
> more than the A-band.

**C-3 — my constant: the L = 5.50 triple discriminator, decision rule
pre-registered, then scored.**

Decision rule (written before scoring the triple; all thresholds derived
from constants already published in §5):
- My law (p ∈ [4.5, 4.93], A′ = 16.75 ± 0.15) forecasts
  log₁₀ λ∞(5.50) ∈ [−72.9, −72.5]. Fuchs-literal (p = 4.5, A′ = 14.676)
  forecasts −73.62 ± 0.1. Decision boundary: **−73.2** (λ = 6.3e−74).
- A converged limit above 6.3e−74 → my A′ stands, Fuchs-literal rejected a
  second time. Between 1.0e−73 and 6.3e−74 → gray zone, escalate to L = 6.
- Upper-bound logic (no convergence needed): ANY single RR rung
  < 1.0e−73 kills my A′ outright; < 1.5e−74 kills both candidates.

Scoring the triple (runs.csv: 1.9854e−64 / 1.4414e−67 / 4.2959e−69 at
m = 152/168/184): value ratios 7.3e−4 then 0.0298 — INCREASING by 41×,
the staircase/plunge pathology; the geometric model's own diagnostic fails,
so the triple's Aitken (4.20e−69, essentially the last rung) is INVALID as
a limit estimator. The last rung sits log₁₀ = −68.37, i.e. **4.8 decades
above the decision boundary**. Verdict: **NOT ADJUDICATED — the triple
cannot discriminate; neither side is selected by existing data.**
EXTRAPOLATION (labeled, method = deep-windows' own plunge-pattern band):
limit expected 10^{−72}…10^{−75}, containing BOTH candidates. What decides
cheaply: one m ≈ 208–216 rung — if it lands ≤ 1.0e−73 my A′ dies
immediately (upper-bound logic); if it lands ≥ 3e−73 with decrement ratio
flattening ≥ 0.2, my A′ is favored and Fuchs-literal is under pressure
pending the Aitken of the completed triple. This is R2.5's next action.

**C-11 — reconciling the universal E-normalized profile with the BKMM
saturation picture.** Three reconciliations, one small lemma proposed:
1. *Universal profile = fixed-point g-function.* The deficit shape is
   L-invariant (renorm §1.2) and the only moving datum is the endpoint,
   which drifts by δ(ℓ) = w∞ − w(ℓ) ≈ 0.05–0.065 over the measured range
   (C-2(I)(c)). Predicted profile collapse: deviations O(δ) ≈ ±0.02–0.05
   of E — quantitatively consistent with the measured ±0.02·E universal
   curve. It ALSO explains the null control that refuted the vector
   discriminator's premise: in the g-function picture the crossover never
   changes the profile SHAPE, only the endpoint law w(ℓ) — so
   registration-termination is early everywhere, exactly as DG found.
2. *"30% of E below T*" vs "action density supported on [T*, T_s]".* No
   contradiction: these are charge-side vs potential-side accountings of
   one integral. The action identity E + A = 2∫(πρ − a)dt localizes the
   CHARGE in [T*, T_s]; the vector envelope measures the POTENTIAL, and
   balayage is nonlocal — the swept charge depresses the envelope below T*
   (and 20% of the exponent in the dodged zone, 80% as
   smallness-without-vanishing, matches the constrained-equilibrium split:
   saturated region carries the constraint/zeros, void region carries the
   slack/smallness). Proposed reconciliation lemma (one page, offered to
   DG+FB): the two accountings differ by an exact integration by parts of
   the g-function against the deficit measure; the measured 20/30/80 splits
   are then computable equilibrium data, not new phenomenology.
3. *Registration-aware node census.* DG's self-correction (pointwise Agmon
   fails at depth, integral bookkeeping survives) is what BKMM predicts:
   pointwise WKB is invalid across the theta-divisor oscillations in the
   saturated region; only integrated (measure-level) statements survive.

**C-1 (brief, unsolicited).** QC's I_w = (π²/2)∫ΔN dt/t and LG's (π²/2)J
are literally the same functional (sign convention aside); MF's
β_eff = 0.5034 is the charge-matched phase: a uniform β-shift produces
δN ≡ (β − ½), whence I_w ∝ (β − ½). So the trichotomy is ONE statement —
"the worth-weighted charge vanishes" — in the linear regime, and the
separating example already exists in LG's own Poisson data (seed 8:
near-neutral J, sup-deficit 4, pays +6.3 nats): beyond sup|δN| ≈ 2 the
functional is extreme-value, not linear, and the three readings genuinely
separate. Recommend the co-statement carry the regime split explicitly.

### R2.3 Merges (two)

**Merge A — "The w∞ Saturation Theorem" (FB owner; RH, renorm, QC co;
DG data; quasicrystal observer status pending QC-3).** Statement = R2.2
C-2 draft. Division of labor: FB proves (II)'s obstacle/mass-balance
mechanism (their FB-2 route, Γ-convergence + duality); I supply (i) the
discrete→continuum licensing (BKMM transplant, gated by the mandatory
AP-dichotomy calibration of RH-2 — one day, kill-or-live), (ii) the chart
dictionary (I)(c) with the resonant-term bookkeeping, and (iii) the Fuchs
bulk-barrier upper bound c = T* (with MF's constructive technology if they
join). Renorm owns the flow/crossover restatement and the κ-graded family
generalization (their R3: capacity (1+κ)^{1/κ}T* — my scaffold predicts the
κ-family cap by the same action integral, a free consistency test). QC owns
the transition-order clause. Timeline: (I) is writable in days; (II) is the
60–90-day C4-as-theory slot, now with three independent routes to one
statement.

**Merge B — "π²/2 by three roads" (HA owner of record via T4; FB, LG, RH
co).** One target: f(t) = (π²/2)ln(eT*/t) derived. Roads and division:
(1) FB's G(t₀) potential-gap finite sum — minutes of arithmetic, runs
FIRST as the go/no-go (if it misses by O(1), the potential-gap road dies
and only the secular road remains); (2) HA's rank-two secular identity
(exact layer, done in the FF pilot); (3) my parametrix evaluation of
|ψ̂₋(t₀)|²/λ₋ via one-node Schlesinger on the discrete RHP (RH-3), which
also owes FB the π²-vs-π²/2 parity/pair factor audit (half page); (4) LG's
linear-response frame fixes the regime of validity (sup|δN| ≲ 2, one-sided
beyond) and supplies the ensemble-side validation data already in hand.
Renorm's R3(ii) κ-graded universality check is the external calibration:
π²/2 must be grading-independent or the mechanism is wrong. Kill: FB's
G(t₀) miss; NA's P3 closure failure > 40%; κ = 1 coefficient off π²/2 by
> 10%.

### R2.4 Updates (kills, retractions, strengthenings)

- **U1 (C-3 status).** p = 9/2 vs π²/2: unresolved by data (my §5 flatness
  mildly favored π²/2; the sensitivity variants sit 4.81–4.92; RR bias
  points down toward 9/2). Round-2 prior shift TOWARD 9/2 on theory: the
  Maslov/parametrix quantization argument (renorm + my RH-1(ii)) predicts
  half-integer p, and no mechanism for π²/2-as-prefactor-power survived
  colloquium scrutiny (my Round-1 "anchor-zero worth" mechanism has a sign
  problem, acknowledged in Round 1). π²/2 stays alive as a measured
  coincidence pending the L = 5.5 decision.
- **U2 (numerology quarantine).** The two quarantined items (A′ = A′_Fuchs
  + 2 = 16.676; ln(2^{29/2}π⁵) = 15.773 vs A′(π²/2) = 15.768) CANNOT be
  killed cheaply: the killer is the same L = 5.50 m ≳ 208 ladder (≥ 40 min
  per rung at dps 100/90 — outside colloquium budget). Quarantine
  maintained, zero theory investment, decision rule now explicit in R2.2.
- **U3 (RH-2 strengthened by two riders).** (i) One-sided-deficit rider
  (from LG P5's measured asymmetry): the BKMM constraint is intrinsically
  one-sided (upper constraint = deficit-side sensitivity), so the
  continuum-limit lemma will naturally be stated in sup-DEFICIT hypotheses
  — my scaffold agrees with LG's §6.1 revision of T3's hypotheses, and this
  is now a design requirement, not an accident. (ii) Phase rider (from
  MF's β-dial): within a fixed density class the equilibrium optimum is
  bang-bang in phase (MF-2(a)), so RH-2's extremal statements must be
  relative to the mean-zero (charge-matched) class, per MF's restated
  MF-2(b).
- **U4 (retraction).** My Round-1 bet 5 on the quasicrystal seat ("the
  mid-range→deep crossover = the window ceasing to resolve the
  quasicrystal") is RETRACTED as a mechanism: their two-scale measurement
  (C-4) shows aperiodicity at constant density costs only polynomially —
  the chirp owns the super-exponential toll, and the crossover is the
  budget-exhaustion point (C-2), not a resolution transition. The Lee–Yang
  /C5 half of that bet stands.
- **U5 (Round-1 bet 3, QC, partial settlement).** The "amplitudes enter
  offsets, phases enter the action" half of my Poisson-echo pump is now
  independently supported (LG's spectral-gap-at-ln 2 mechanism; QC's
  worth-weighted charge with unit slope); the two-saddle derivation of the
  4π cap remains unclaimed by QC — bet reduced, not settled.
- **U6 (strengthening from C-11).** The vector campaign's 20/80 split and
  universal profile are absorbed into RH-2 as predicted equilibrium data
  (R2.2 C-11 items 1–2); RH-2 gains a second falsifiable output: the
  profile-collapse residual should scale like δ(ℓ) ≈ (pℓ + A′ − A)e^{−ℓ}/
  28.85 — testable on the existing vectors at two more L without new
  eigensolves.

### R2.5 Next action (single, sized)

**Land one deep rung at L = 5.50, m = 208 (dps 100/90), single worker,
~35–45 min (m²-scaled from the recorded m = 184 rung: 1613 s assembly +
65 s solve), then — only if the first rung does not already kill my A′ by
the upper-bound rule — complete the equal-step pair m = 224 (~50 min) for
a valid-ratio Aitken.** This is the C-3 decider under the pre-registered
rule of R2.2: it adjudicates my (p, A′) against Fuchs-literal, kills or
spares both quarantined numerology items, discharges the sharpest test QC
named for the Fredholm reading, and closes the last open clause of
C-2(I)(c)'s dictionary at a sixth window. Owner: deep-windows agent
(re-engagement per SYNTHESIS §7); this seat consumes and scores. My
pre-commitment: if any rung lands below 1.0e−73, I retract A′ = 16.75 and
the two quarantined identifications in the same breath, and RH-1(iii)
reverts to "A′ unknown, extraction repeats at L = 5.5/6.0".

### R2.6 The m = 208 rung — executed (coordinator-authorized), scored; ratchet policy for m = 224/240

**Execution record (COMPUTED; artifacts in results/ias/riemann-hilbert/:
run_rung_5p50_m208.py, rung_5p50_m208.log/.json, rungs.csv, Q checkpoint).**
Protocol notes for the ledger: (i) this seat ran the rung itself under
coordinator authorization (the deep-windows agent's instrument
`spectral_form` unchanged; the u-quadrature split additively over 4 worker
processes with exact `_mpf_`-tuple exchange — differs from serial only in
summation order at dps+15); (ii) at m > 184 the instrument's own `gl_nodes`
rule jumps 192 → 384 points in x and u (m+4, m+8 > 192), so the deep
report's "identical 192-pt rules" clause ends at m = 184 — the rule is the
unchanged code's own, still exact on all polynomial overlap factors, and
the R2.5 cost estimate (m²-scaled) was wrong by ~4× single-threaded; the
authorized 4 workers restored it. Gates: G1 serial anchor
(2.485, 24) → 3.8688156e−10 PASS; G2 parallel-vs-serial entrywise
< 1e−40 on the anchor config + identical λ PASS; G3 nested-basis
monotonicity PASS. Assembly 2805 s @ 4 workers (co-tenant load 14 → 2.5
during the run), solve 113 s @ dps 90; bottom gap λ₂/λ₁ ≈ 9.2×10³ (no
level-crossing artifact, deep-agent discipline satisfied).

**Result: λ(5.50, m = 208) = 4.21478011593e−71 (log₁₀ = −70.3752),
ratio to m = 184 = 0.00981 (24 steps; per-16-step ≈ 0.046).**
Scored against the R2.2 rule: 2.8 decades above the −73.2 decision
boundary, value ratio ≪ 0.2 — **NOT ADJUDICATED, still in the plunge**
(per-16 ratio sequence now 7.3e−4 → 0.030 → 0.046, rising slowly exactly
as the 4.75/5.00 ladders did before their abrupt flattening). No
retraction triggered; no candidate favored.

**Pre-registered ratchet policy (written before the m = 224 launch, per
coordinator instruction, to prevent indefinite escalation).** Let
r := λ(224)/λ(208) (16-step value ratio). My forecast-band for the LIMIT
is [1.26e−73, 3.2e−73]; Fuchs-literal's is ≈ 2.4e−74; both flatten, on
the deep-ladder precedent, within ~1 decade of their limit — i.e. by
λ ≈ 2e−72 (mine) or ≈ 2.4e−73 (Fuchs). Honest expectation: r ∈
[0.05, 0.25], λ(224) ≈ 2e−72 – 1e−71 — **m = 224 may well STILL be
plunging and non-adjudicating.** Policy:
- λ(224) < 1.5e−74 → both candidates dead (unchanged).
- λ(224) < 1.0e−73 → mine dead; pre-committed retractions execute
  immediately (A′ = 16.75, both quarantined numerology items). The
  residual Fuchs-vs-lower question is not this seat's claim; an m = 240
  rung for it is a panel decision (priced below), not mine.
- λ(224) ≥ 1.0e−73 with r ∈ [0.15, 0.6] → flattening onset: **the
  completed-triple Aitken on (208, 224, 240) is the endgame** — run
  m = 240, apply R2.2's boundary to the Aitken limit. This is the true
  decider; a valid-ratio triple should pin the limit to ±30% (the 4.50
  ladder's geometric-model precedent: +0.09%).
- λ(224) ∈ [1.0e−73, 3e−73] with r < 0.15 → mine DOWNGRADED to
  disfavored even before m = 240 (a still-plunging rung inside my limit
  band implies the limit undershoots the band), pending m = 240
  confirmation.
- λ(224) > 3e−73 with r < 0.15 (still plunging above the zone) → run
  m = 240; **HARD STOP after m = 240 regardless of outcome.** If m = 240
  still shows r < 0.15 with λ ≥ 1e−73, the plunge is inconsistent with
  the flattening scale of BOTH candidates and further m at L = 5.5 is
  the wrong spend: the discriminator moves to L = 6.0 (forecast
  separation −96.4 vs −97.4, a full decade, fresh ladder). No m = 256
  under any outcome of this policy.

**Pricing (measured base: m = 208 = 2805 s assembly + 113 s solve @ 4
workers).** m = 224: ×(224/208)² ≈ 3260 s + 140 s ≈ 55 min worst case,
likely ~40 min on the now-quiet machine. m = 240: ×1.33 ≈ 3730 s + 170 s
≈ 65 min. Full endgame (224 + 240 + Aitken arithmetic) ≤ 2 h wall at 4
workers, respecting NT's 1-core certification rerun.
