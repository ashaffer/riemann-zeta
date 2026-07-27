# SEAT: magic functions (Fourier interpolation & LP bounds — Viazovska school)

Round 1, independent. 2026-07-26. Honesty tiers on every claim:
THEOREM / COMPUTED / CONJECTURE / SPECULATION. Citations from memory are
flagged UNVERIFIED where I am not certain of the reference data; none were
re-derived from the repo.

---

## §0 Seat card

Toolkit: (1) Cohn–Elkies-type LP duality and sharp dual certificates (sphere
packing d = 8, 24); (2) magic-function construction and universal optimality
(Viazovska; CKMRV interpolation with derivative data); (3) Fourier
interpolation/uniqueness pairs (Radchenko–Viazovska; Bondarenko–Radchenko–Seip
on zeta zeros; Kulikov–Nazarov–Sodin density thresholds); (4) Beurling–Selberg
extremal functions and the de Branges/Gaussian-subordination machinery — the
working "magic functions" of the explicit formula; (5) truncated trigonometric
moment problems, Krein extension, positive super-resolution.

---

## §1 Translation: the program's objects in LP-bound language

### 1.1 The form is a truncated Toeplitz form; the window criterion is a moment problem

Write the whole form in x-space (this is FULLINF Lemma F0 plus one elementary
identity for the pole). For φ real, supported in [−a, a], a = L/4:

  Q_L(φ) = ∫∫ φ(x) K(x−y) φ(y) dx dy,  with the **Weil kernel**
  K(u) = W_arch(u) + 2cosh(u/2) − Σ_{n≥2} Λ(n) n^{−1/2} [δ(u−log n) + δ(u+log n)],

where W_arch is the (even, continuous-density) inverse FT of
Re ψ(1/4+ir/2) − log π, and 2cosh(u/2) reproduces the pole term
P(φ) = 2(∫φe^{x/2})(∫φe^{−x/2}) exactly (expand cosh; the two exponential
kernels each give the product of the two boundary functionals). Only
u ∈ (−2a, 2a) = (−L/2, L/2) is ever sampled. THEOREM (bookkeeping, verifiable
in an afternoon): Q_L ≥ 0 on H_L for all L ⟺ K is a positive-definite
distribution on every finite interval ⟺ RH (Weil's criterion in windowed
form; lineage Weil 1952, Yoshida 1992, Bombieri 2000 — per the repo's own
corrected citations).

So in my field's native language: **the positivity gate is a truncated
trigonometric moment problem.** "Is this explicitly given kernel — a smooth
archimedean density, plus a cosh, minus a finite comb of prime deltas —
positive-definite on the interval (−L/2, L/2)?" That is the same genre of
question as "is this candidate two-point function a valid autocorrelation,"
and its dual (below) is exactly the LP dual the seat's seed question (a) asks
for.

### 1.2 The exact primal–dual pair (seed question (a), answered)

PRIMAL(L):  λ(L) = inf { Q_L(φ) : ‖φ‖₂ = 1, supp φ ⊂ [−a, a] }.

DUAL(L):  λ(L) = sup { λ : K − λδ₀, restricted to (−L/2, L/2), admits an
extension to ℝ which is the Fourier transform of a **positive measure** σ on
ℝ (for pole-free Dirichlet families), resp. of a positive measure plus the
fixed one-negative-square cosh block (for ζ; see 1.3) }.

Weak duality is a one-line evaluation: if σ ≥ 0 matches K − λδ₀ on the
window, then Q_L(φ) − λ‖φ‖² = ∫ |φ̂(t)|² dσ(t) ≥ 0 for every admissible φ,
because φ⋆φ̃ only sees the window. Strong duality is the **Krein extension
theorem** (M. G. Krein, 1940: every continuous positive-definite function on
(−ℓ, ℓ) extends to a positive-definite function on ℝ; UNVERIFIED exact
reference, the result itself is classical). Our kernel has atoms, so the
distributional version needs a mollification lemma (Fejér-smooth K, shrink
the window by ε, pass to the limit) — days of work, not months; stated as
MF-1(a) in §2.

Under RH the dual-feasible point at λ = 0 is **the zero measure itself**,
σ₀ = 2 Σ_{γ>0} δ_γ: the explicit formula says exactly σ̂₀ = K on all of ℝ.
This is the precise sense in which the program's blindly extracted NNLS
witnesses (atom 14.079, weight 2.047, against γ₁ = 14.1347, weight 2.000 —
SYNTHESIS/CO) are "the zeros seen from the dual side": they are quadratures
of a window-equivalent positive extension of K. Two structural consequences
the LP view adds:

- The finite-m dual witness need NOT sit exactly at the zeros. The dual
  optimizer at λ = λ(L) > 0 is a *deformation* of σ₀ that stays positive
  while shedding λ×Lebesgue/2π in-window; the measured displacement
  14.079 vs 14.1347 is a feature (the deformation the window permits), not
  numerical error. Its m → ∞ and λ → 0 limits are constrained by
  super-resolution theory for positive measures (see MF-1(b)).
- The weight-2 identification is mass, not amplitude: any window-equivalent
  extension must carry the counting function's mass below T*(L) to
  in-band accuracy — that is why the weight converged to ≈ 2.

### 1.3 The pole is exactly two imaginary atoms (Kreĭn–Langer, one negative square)

The 2cosh(u/2) term is the "Fourier transform" of two unit point masses at
the imaginary frequencies ±i/2 — the pole of ζ at s = 1 seen through
s = 1/2 + ir. As a quadratic form it is 2(∫φe^{x/2})(∫φe^{−x/2}) = 2b₊b₋,
which has signature (+1, −1): **exactly one negative square**. So:

- Dirichlet families (pole-free): the window criterion is the *pure* Krein
  problem. This is the cleanest statement I know of why the family is the
  right laboratory (the program discovered this empirically as "pole-free
  landscapes assign roles by character sign").
- ζ: the window criterion is a Kreĭn–Langer-type extension problem in the
  class "positive measure + fixed pair of unit masses at ±i/2" —
  positive-definiteness with at most one negative square. The measured
  **pole flip** (§2.11 of PROGRAM.md: restoring the pole flips ψ_min(log 2)
  and turns prime 2 from drain to rescuer) is, in this language, the
  statement that the one-negative-square block rotates the extremal
  extension's in-window profile. CONJECTURE-level reading, but the class
  identification is THEOREM-level bookkeeping.

PRIOR-ART FLAG (important): "screw functions" are Kreĭn's theory of this
exact extension problem, and Suzuki's screw-function formulation of Weil
positivity (arXiv:2606.09096, cited throughout the repo) almost certainly
already contains the 1.1–1.3 dictionary in some form. I have not read it;
diligence before claiming any of 1.1–1.3 as new. What I believe is NOT in
that literature: the dual-witness identifiability layer (MF-1(b)), the
extension-set-width = envelope reading (MF-1(c)), and the finite-m
super-resolution statements.

### 1.4 What the packing LP maps to, item by item

| sphere packing (d = 8/24) | positivity gate |
|---|---|
| point configuration / lattice | zero multiset {±γ} |
| Poisson summation over the lattice | explicit formula (Guinand–Weil) |
| LP test function f: f̂ ≥ 0, f(x) ≤ 0 for x ≥ r | test autocorrelation g = φ⋆φ̃, supp ⊂ (−L/2, L/2); ĝ = φ̂ ⋆̄ φ̂... i.e. h = φ̂² ≥ 0 automatic |
| LP value: density upper bound | window margin λ(L) |
| sharp dual certificate = lattice measure | dual extension measure → zero measure |
| magic function (primal, closed form, from modular forms) | **magic measure** (dual: a constructive positive extension of the prime data) |
| complementary slackness: f vanishes to order 2 at lattice distances √(2n) | near-null φ's transform vanishes at the γ's (the keyhole/Groskin phenomenon — kill-list K8 respected: validation, not discovery) |
| modular input: theta/Eisenstein with positive coefficients | MISSING — this absence is the theorem gap (see 1.6, §3) |

One inversion deserves emphasis: in packing, the configuration is the
unknown and the certificate side is a free search; here the configuration
(zeros) is handed to us by the explicit formula and the *positivity* is the
unknown. **The Weil LP is the Cohn–Elkies LP run in reverse.** In d = 8 the
miracle was that the dual optimizer (E₈) is rigid, algebraic, and
modular-parametrized, so the primal magic function could be written in
closed form. In the function-field world the dual optimizer (Frobenius
angles) is again algebraic — and there the certificate exists and is the
L-polynomial (the repo's AG seat: the Cayley–Hamilton kernel vector IS the
L-polynomial). Over ℚ the dual optimizer is transcendental and the only
"modular" object with the right node set is ξ itself. See MF-3.

### 1.5 The already-existing magic functions of this summation formula

The Beurling–Selberg school is the 1D magic-function shop, operating on this
exact identity for forty years: extremal one-sided band-limited majorants
(Beurling, Selberg; survey Vaaler, BAMS 12 (1985)), the Gaussian-subordination
framework in de Branges spaces (Carneiro–Littmann–Vaaler, Trans. AMS ~2013,
UNVERIFIED volume), with explicit-formula applications by
Chandee–Soundararajan (bounds for |ζ(1/2+it)|), Carneiro–Chandee–Milinovich
(S(t), gaps), Chirre–Gonçalves and others. Distinction that matters: that
school solves *linear* extremal problems against the Weil distribution
(optimize one test function against a known sign pattern). The positivity
gate is the *quadratic* problem — certify the form itself — whose dual is a
measure completion, not a single extremal function. The technology transfers
(reproducing kernels, interpolation at prescribed nodes with derivative
data), but the target type is different, and I do not know of LP-duality
treatments of the quadratic problem in that literature. (UNVERIFIED — a
literature pass on "extremal problems for positive definite extensions +
explicit formula" is part of MF-1's diligence.)

### 1.6 Interpolation and uniqueness: where T1′ lives (seed question (d))

- Radchenko–Viazovska (Publ. Math. IHÉS 129 (2019)): even Schwartz f is
  reconstructible from f(√n), f̂(√n) — an interpolation basis built from
  weakly holomorphic modular forms; density of the node pair is *critical*.
- Bondarenko–Radchenko–Seip, "Fourier interpolation with zeros of zeta and
  L-functions" (arXiv:2005.02996, UNVERIFIED number and venue): the RV-type
  interpolation formula whose nodes are the ordinates of the nontrivial
  zeros on one side and (log n)-type points on the other, built
  unconditionally on the explicit formula. **This is the RV basis for this
  program's summation formula, on the true zeros.** To my knowledge nobody
  has written the analogue on the smooth staircase (no summation formula
  there — that is exactly what's missing), which is why T1′ had to be proved
  by Jensen instead of by exhibiting a basis.
- Kulikov–Nazarov–Sodin and adjacent work (2023–2025; UNVERIFIED refs) give
  density thresholds for Fourier uniqueness pairs. T1′'s structure matches:
  a PW_a function constrained to vanish on the staircase head is a
  *sub-critical, one-sided* data set — uniqueness MUST fail at every finite
  horizon without extra input (the HA seat's counterexample is the standard
  one), and the anchor Hypothesis A is exactly the "extra ε of data" that
  restores a finite horizon. Answer to seed (d): yes — T1′ is a
  uniqueness-pair statement (the hard, quantitative half); the interpolation
  basis (constructive half) exists for the true zeros (BRS) and is OPEN for
  the staircase. The pair (T1′ hard horizon at e²T*, measured constructive
  stopping at ≈ 3.2–3.6 T*) brackets the staircase's true "critical anchored
  horizon" — the analogue of pinning RV's critical density. See MF-4.

### 1.7 The envelope law, read as LP-gap physics

The measured law (mid-range E(L) = −ln λ ≈ −A + b[N(T*) + μD(T*)];
deep-regime slope capped at the universal prolate rate 4π per unit e^{L/2},
i.e. E ~ 2T* — note 4π·e^{ℓ} = 2T* exactly) says: the *rate* at which the
window margin closes is structure-blind (a functional of the counting
function alone; the program's staircase experiment), while structure —
rigidity class, arithmetic, conductor, pole — lives only in *offsets*. In LP
language: the asymptotic slope of the LP gap is universal (as in packing,
where LP-bound exponents are dimension-universal and structure appears in
subexponential corrections), so **proof effort must target offsets, not
rates** — rates come free from prolate/Landau–Widom theory, offsets are
where RH-specific content sits. The certified floor δ* = λ/‖v‖₁² (Q5,
program law) is the corresponding certificate-precision economics: the
sharper the LP, the more digits the dual witness must carry — the program
has, I believe uniquely, *measured* the certificate-size law of a knife-edge
LP across 70 orders of magnitude.

---

## §2 Candidates

### MF-1. The Krein dual of the positivity gate (three tiers)

**(a) Strong-duality lemma (THEOREM-candidate).** For every L and every
λ < λ(L), the mollified kernel (K − λδ₀) ⋆ F_ε (F_ε a Fejér kernel) is
positive-definite on (−L/2 + 2ε, L/2 − 2ε); by Krein's extension theorem it
extends to σ̂_ε with σ_ε ≥ 0; a weak-* limit as ε ↓ 0 produces a positive
measure σ (plus, for ζ, the fixed ±i/2 pair) with σ̂ = K − λδ₀ on the open
window. Hence DUAL(L) = PRIMAL(L) exactly.
*Route:* textbook (Krein + Banach–Alaoglu + a care lemma for the atoms and
the cosh block; the one-negative-square class needs Kreĭn–Langer instead of
Krein — the clean path is to prove the pure statement for the family first,
ζ second). *Effort:* days for the family; 1–2 weeks for ζ's pole block.
*Interfaces:* gives CO's dual witnesses their exact infinite-dimensional
referent; gives Track B the correct object to mine (extension measures, not
SOS polynomials). *Kill criteria:* if the distributional Krein step fails
for delta-bearing kernels in some essential way (I know of no such
obstruction, but the literature check may find the statement already in
Suzuki/Kreĭn–Langer — then this is a citation, not a lemma, and the seat
moves directly to (b)). *Prior-art risk:* HIGH for the dictionary itself
(screw functions), stated in §1.3.

**(b) Dual-witness identifiability (THEOREM-candidate, the new content).**
Fix L, m, and suppose the Galerkin form has λ_min = λ ≪ 1 with k near-null
vectors below some η. Then ANY representation Q = ∫ E(t) dν(t) + S with
ν ≥ 0, S ⪰ 0 (E(t) the rank-one frame matrices) forces ν to load its
in-band mass in small neighborhoods of the common node set of the near-null
vectors' transforms: ∫ |v̂_i(t)|² dν(t) ≤ ⟨Qv_i, v_i⟩ ≤ η for each near-null
v_i, so ν(A) is small wherever min_i |v̂_i|² is bounded below on A.
Quantitatively this is positive-measure super-resolution (no minimum
separation needed for positive atoms — Markov–Krein/Prony; modern stability:
Schiebinger–Robeva–Recht 2017, Denoyelle–Duval–Peyré, both UNVERIFIED
details): below the Nyquist height T*(L) the representing-measure set has
diameter controlled by η and the Galerkin resolution. **Corollary:** the
NNLS atoms converge (m → ∞, in-band) to the atoms of every/any extension
measure — the keyhole in dual form, now a stability theorem rather than a
phenomenon. Respects kill-list K8: Groskin owns the phenomenon; the claim
here is only the identifiability statement.
*Route:* linear algebra + one super-resolution import; the repo's measured
node suppressions (factors 200–5000) are the constants of the proof.
*Effort:* 1–2 weeks. *Kill:* run NNLS at m and 2m at fixed L with tight
residuals; if in-band atoms do NOT contract toward a common limit set as m
grows (stalling displacement at fixed offset from the γ's beyond the
resolution radius), the determinacy reading is wrong.

**(c) The magic-measure form of UPT (CONJECTURE — the honest restatement of
the theorem gap).** There exists a constructive family of positive measures
σ_ℓ (ℓ = L/2), built from the Riemann–von Mangoldt density plus local
corrections, with σ̂_ℓ = K on (−ℓ, ℓ) — uniformly in ℓ. By 1.2 this IS Weil
positivity, hence RH. The measured envelope prices the difficulty exactly:
the extension set at window ℓ has "width" e^{−E(ℓ)} (the program's λ), so
any constructive σ_ℓ must place its in-band atoms with super-resolution
accuracy that grows super-exponentially in e^{ℓ}. **This is what a magic
function proof of λ(L) ≥ 0 looks like at fixed L** (seed (a) final answer):
a closed-form positive quadrature matching the prime data on the window —
the analogue of Viazovska's integral representation with manifestly positive
integrand; the Lean certificates are its numerical shadows, and fixed-L is
solved-in-principle by them. The infinite-door question is whether σ_ℓ can
be written down as one formula in ℓ. No route is claimed; the FF world has
one (MF-3), and that asymmetry is the sharpest statement of the gap I can
make in my field's terms.

### MF-2. Universal near-optimality of maximal rigidity (seed (c), formalized)

Let 𝒦_R(T̄) = {symmetric multisets Λ with |N_Λ(T) − N̂(T)| ≤ R for T ≤ T̄},
and λ_Λ(L) the lower frame value inf{Σ_{t∈Λ}|φ̂(t)|² : ‖φ‖ = 1,
supp φ ⊂ [−L/4, L/4]} (the program's frame form, model_zeros.py).

**(a) Concave-program structure (THEOREM-candidate).** μ ↦ λ_μ(L) (λ of the
frame form of a positive measure μ) is concave and weak-* upper
semicontinuous on positive measures; the constraint set "N_μ within ±R of
N̂" is convex and compact (cutoff at T̄). Hence a maximizer μ*_{L,R} exists,
and satisfies a complementary-slackness principle: the constraint is active
(bang-bang) except where the minimizing φ*'s |φ̂*|² is flat — the maximizer
is an extremal *staircase-like* singular measure, characterized by an
obstacle-problem condition. *Route:* convex analysis, min of linear
functionals is concave; effort ~1–2 weeks; the free-boundary seat should own
the characterization (see §4). *Value:* turns "maximally rigid" from a
slogan into a variational object, and gives DG's T3 its sharp constant a
home: T3 bounds |ln λ_Λ − ln λ_sm| ≤ Cℓ(D+1); MF-2(a) asks for the extremal
Λ, not just transfer.

**(b) The sharp conjecture (CONJECTURE — the CKMRV analogue).** The one-
parameter family of functionals {−ln λ_·(L)}_{L>0} plays the role of the
completely-monotone energy family in universal optimality. Claim: the smooth
staircase is within an additive O(ℓ·R)-band of max over 𝒦_R —
SIMULTANEOUSLY for all L — and the true zeta ordinates are within an
additive O(1) of the staircase for all L. ("The zero multiset is universally
near-optimal for lower frame bounds within its density class.") Evidence:
the program's staircase-matches-true measurements at L = 2.485, 2.996;
tension: the factor-6.3 anomaly at L = 3.555 (adjudication Q3). Direction of
the anomaly matters: true BEATS smooth there — which is *consistent* with
(b) only if the staircase is not the in-class optimum and the zeros track
the optimum better than the midpoint staircase does. The β-dial test of §5
probes exactly this at low cost. *Kill:* if Q3's factor survives Gcut → ∞
AND exceeds the entire phase-family envelope of §5, then arithmetic buys
frame bound beyond density+rigidity+phase, (b) as stated dies, and the
density-only mechanism reading (SYNTHESIS 1.1(d)) needs a rider.
*Note:* in d = 1 constant density, universal optimality of ℤ among unit-
density configurations is known (Cohn–Kumar 2007, UNVERIFIED that the ℝ¹
case is stated there) — MF-2(b) is its log-density, growing-window analogue,
and the AP-dichotomy lemma already in the program (constant density = zero
toll, exact tight frames at sub-Nyquist) is the degenerate case.

### MF-3. The function-field certificate in Cohn–Elkies normal form (THEOREM-candidate, days)

For C/F_q of genus g, AG-1 reduces λ_C(L) to ln q · λ_min(T_n(μ_C)), the
Toeplitz matrix of the Frobenius-angle measure. State and prove the LP
dictionary explicitly: (i) DUAL: the extension problem for the truncated
sequence of Frobenius power sums is solved by the angle measure
μ_C = Σ_j δ(θ − θ_j) ≥ 0 (positivity ⟺ RH_C, a THEOREM via Weil); (ii)
complementary slackness: at n = 2g+1 the kernel vector's symbol is the
L-polynomial, whose zeros lie ON the unit circle — i.e. **the L-polynomial
is the magic function of the FF LP**, with the self-inversive/unit-circle
zero structure playing the role modular forms played in d = 8; (iii) the
positivity input is Castelnuovo/Rosati (= the "positive Fourier
coefficients" input of Viazovska's construction). Deliverable: two pages +
a numerical check on E/F₅ against the existing Lean data (`CurveCertE5`).
*Effort:* days (the reduction is done; this is arrangement). *Value:* fixes
the exact shape of what ℚ must manufacture — a positive-extension
parametrization whose "stable polynomial" is transcendental — and connects
directly to the quasicrystal seat's Lee–Yang machinery (Kurasov–Sarnak
construct crystalline measures from stable polynomials; the FF certificate
IS such a construction at finite degree; §4 bet 1). *Kill:* if the FF dual
optimizer is non-unique before n = 2g+1 in a way that breaks the
complementary-slackness reading, the dictionary needs AG's kernel clause;
no other kill — this is consolidation, not speculation.

### MF-4. T1′ as interpolation theory: close the constructive side (CONJECTURE with route)

T1PRIME.md Gap 2 conjectures anchored vanishing on the staircase is possible
through e^{2−δ}T*. The RV-school route: build F = (weighted product over the
staircase head) × (Beurling–Malliavin multiplier shaped so that Θ(1) of the
L²-mass sits below T*), with the balayage identity (NT Round 2: super-
Nyquist surplus on [T*, eT*] = deficit mass e^ℓ, exactly) as the mass-
bookkeeping device — the same bookkeeping that makes RV's critical-density
interpolation converge. The measured stopping heights (3.14–3.41 T*,
saturating ≈ 3.59 T*) are MINIMIZER standoffs, not construction ceilings, so
no conflict either way; the interesting trichotomy is: constructive ceiling
at ≈ 3.6T* (C4's w∞), at e²T* (Gap 2 true), or in between (new constant).
*Effort:* weeks–months (HA seat owns; this seat contributes the multiplier
technology). *Kill:* a proof of a hard horizon below e² for anchored
functions kills the e^{2−δ} form; C4's stopping-height extraction cannot
kill it (different objects — record this so nobody wires the wrong test to
it). *Bonus diligence item (cheap, days):* read BRS quantitatively — their
interpolation basis on the TRUE zeros is a dual-frame-type object; any
explicit norm bounds on the basis functions are *unconditional arithmetic-
side inputs* of exactly the kind the program has none of (all current
arithmetic-side knowledge is upper bounds via Rayleigh–Ritz plus certified
windows). If BRS constants translate into any explicit lower bound on λ(L)
at small L — even a terrible one — it would be the program's first
unconditional analytic lower rung, and the translation cost is a focused
read, not a research program.

---

## §3 Intuition pumps (licensed informality; everything here is SPECULATION unless tiered otherwise)

**What λ(L) smells like.** The smallest eigenvalue of a truncated Toeplitz
form whose symbol is a *limit of quadratures of itself*. In packing terms:
an LP that is asymptotically sharp at every scale simultaneously — the d = 8
miracle (zero LP gap) happening not once but along a whole one-parameter
family, with the gap closing super-exponentially instead of being exactly
zero. Rodgers–Tao's Λ ≥ 0 says RH, if true, is true with zero margin; the
envelope law is the first measurement of the *shape* of that zero margin.
d = 8 closed because sharpness happened at ONE point with an algebraic,
rigid, modular-parametrized optimizer. Here sharpness is asymptotic along a
family with a transcendental optimizer. That is a different, and honestly
harder, species of LP.

**The sphere-packing history replay.** Packing d = 8 went: numerical LP
tables (Cohn–Elkies 2003) → observed node structure of the near-optimal
functions → ansatz class closed under the problem's symmetry (modular forms
for SL₂(ℤ) acting through Gaussians) → closed form (Viazovska 2016). This
program is at stage 2: tables (the certified ladder), node structure
(Groskin/keyhole; NNLS duals). Stage 3 needs the ansatz class closed under
the problem's symmetry, and the program has already MEASURED what that
symmetry is: the family universality in T*_χ = (2π/q)e^{L/2} and the
β-linearity of the exponent are exact dilation covariance — the modular
group of this LP is the dilation/Mellin group. The function class closed
under it and carrying the prime nodes at log n is the Mellin world of Tate's
thesis: theta-like series over the multiplicative group — i.e., L-functions
again. The ansatz class regenerates the object. I believe this circularity
is the honest content of "constructing B_L is constructing the spectral
object" (PROGRAM §2.12), now with a reason: in d = 8 the modular input was
logically independent of E₈ (theta functions exist without the packing
problem); here every candidate "modular input" with nodes at log n IS the
zeta-world. A proof must either break the circle (find a positivity-bearing
class that is NOT zeta — the CCM/Sonin route, in effect) or exploit it
(fixed-point/bootstrap: the extension measure and the kernel are the same
object at two scales — renormalization seat's territory; see bet 5).

**Why the pole flip was inevitable, LP version.** In Cohn–Elkies the
normalization f(0) = f̂(0) ties the density term to the positivity budget;
flipping its treatment converts majorant problems into minorant problems
with opposite extremal sign patterns (Beurling–Selberg ±). The pole is this
program's f̂(0)-term: a one-negative-square block that rotates which
perturbations help. The family (no pole) vs ζ (pole) is the minorant/
majorant switch, and the measured sign ledger is its shadow. COMPUTED
support: the program's own mechanism law (8/8 sign predictions).

**Lehmer pairs as interpolation-node degeneracy.** An RV-type basis on the
zeros has biorthogonal functions with norms ~ 1/(node separation); a Lehmer
pair (gap 0.0353 at t = 17143.79) is a near-double node, where any
interpolation/dual-frame basis nearly blows up — and where the marginal law
must go non-additive (the program measured ~20% non-additivity; a pair
deletion vs two single deletions differ exactly when nodes nearly merge).
Testable someday: non-additivity of the two-zero worth should scale like
ln(1/gap) at Lehmer pairs. Not urgent; recorded because it ties the
program's two most photogenic measurements (Lehmer pair, marginal law) to
one mechanism.

**The certificate floor as LP economics.** δ* = λ/‖v‖₁² (program law, Q5) is
the 1D shadow of a general phenomenon: dual certificates of nearly-tight LPs
need precision ~ the LP gap divided by the witness's coherence. In packing,
the d = 8 dual certificate is exactly rational in the right normalization
(the lattice); here the witness is transcendental and the floor law measures
the cost of that transcendence rung by rung. SPECULATION: the bit-size
growth law the CS seat measured (digits ≈ 0.21·m²·DENP) is the "modularity
deficit" of the zeros — in a world where the dual witness had a finite
algebraic description, certificate size would be O(size of that
description), as it literally is in `CurveCertE5` (integer matrices from
point counts). Certificate-size asymptotics are thus a *quantitative probe
of algebraicity* — worth stating to the proof-theory seat.

---

## §4 Cross-seat bets (ranked by confidence)

**Bet 1 — quasicrystal seat (confidence 0.8).** Their crystalline measures
and my Krein extensions are the same object. Specifically: (i) the
zero-measure/prime-comb pair is the canonical signed crystalline pair
(Guinand; Meyer's revival), and RH is the statement that one side is a
POSITIVE crystalline measure; (ii) Kurasov–Sarnak build positive crystalline
measures from Lee–Yang/stable polynomials — and the function-field
certificate (MF-3) is literally a finite-degree Kurasov–Sarnak object: the
L-polynomial is self-inversive with unit-circle zeros (Lee–Yang property =
RH_C). Joint statement I expect us to converge on: "UPT = the assertion that
the prime comb is in the closure of the Kurasov–Sarnak-constructible cone,
with ξ as the limiting stable object." Concrete joint artifact: rewrite the
E/F₅ Lean certificate as a stable-polynomial summation formula.

**Bet 2 — free-boundary seat (confidence 0.7).** MF-2(a)'s maximizer (the
extremal measure for the frame bound in a discrepancy class) is
characterized by an obstacle problem, and its contact structure is the
program's balayage identity: surplus on [T*, eT*] = deficit mass, capacity
endpoint eT*, D(eT*) = −7/8. I bet their equilibrium-measure formulation of
the envelope exponent and my extension-set width are Legendre-dual
descriptions of one variational problem, and that the C4 standoff constant
w∞ = 1.2785 (root of e^w(w−1) = 1) drops out as their free-boundary
condition. If they derive w∞ from an obstacle problem before the deep
ladders re-run, that is the cheapest available derivation of any envelope
constant.

**Bet 3 — riemann-hilbert seat (confidence 0.6).** The envelope offset A and
the marginal law are Fredholm-determinant data: E(L) + A should be −log det
of an explicit finite-rank-perturbed prolate operator on the staircase, the
marginal law (π²/2)ln(eT*/t) its logarithmic derivative under one-atom
deletion (the rank-two secular identity of T4 is the finite shadow), and the
capacity edge's (eT* − t)^{3/2} softening an Airy/soft-edge signature with
width exponent −2/3 (HA-P2's turning-point band [2.2, 2.5] vs fixed-profile
2.0 is exactly this discriminator). The constants that "resisted derivation"
(b, μ) are in their toolbox or nowhere: Deift-school asymptotics of Toeplitz
+ Fisher–Hartwig with a merging-gap symbol. If they cannot see b in a
Painlevé σ-form, I lower MF-1(c)'s hopes accordingly.

**Bet 4 — quantum-chaos seat (confidence 0.45).** The NNLS dual atom's
displacement (14.079 vs γ₁ = 14.1347, and its m- and L-dependence) is a
semiclassical observable: the finite window truncates the prime side at
e^{L/2}, so the dual witness sees "zeros" of a resummed finite-orbit
partition function — Berry–Keating regularization should predict the
displacement δγ₁(L) from the smoothed counting kernel with no free
parameters. If their formula matches the measured displacement trend, the
dual witnesses ARE semiclassical zeros, and MF-1(b)'s limit-set statement
acquires a physics normal form (and a prediction for where the atoms sit at
every finite m — useful to Track B certificate design).

**Bet 5 — renormalization seat (confidence 0.35, stated loosely).** The
circularity in §3 ("the ansatz class regenerates the object") is their
native food: the window criterion maps the pair (kernel on (−ℓ,ℓ), extension
measure) to (kernel on (−ℓ′,ℓ′), extension) as ℓ grows — a transfer-operator
flow whose fixed point is the explicit formula itself. The envelope's two
regimes (mid-range law → 4π cap at L ≈ 4.32) then read as a crossover
between two RG fixed points (structure-dominated → universal prolate). If
they can exhibit the flow whose linearization has the 4π cap as its
universal eigenvalue, the bend stops being a fit question forever.

---

## §5 One cheap computable test: the β-dial (staircase phase vs frame bound)

**Design (pre-registered before any run; this section written first).** The
smooth staircase used everywhere in the program is N̂(t_k) = k − 1/2 — the
midpoint phase. Define the phase family t_k(β): N̂(t_k) = k − β, β ∈ (0, 1)
(β = 1/2 is the program's staircase; larger β slides all nodes DOWN).
Kadec's 1/4-theorem is the constant-density ancestor of this dial: phase
perturbations of sampling nodes degrade frame bounds smoothly up to a
threshold. Nobody has scanned β here (the law-theory deformations changed
density/rigidity, not pure phase — RESULTS.md and SYNTHESIS as read).

Instrument: `src/model_zeros.py` `frame_form` (frame form of an arbitrary
ordinate list, orthonormal Legendre basis) + `spectral_lam_min`. Config:
L = 2.485, m = 24, Gcut = 420, dps 40; β grid {0.10, 0.25, 0.40, 0.50,
0.60, 0.75, 0.90}; plus the true zeros at the identical (m, Gcut, dps) for
apples-to-apples. Budget ≈ 8 frame builds ≈ well under 30 CPU-min. If time
permits, one confirmation pair (β = 0.5, β*) at L = 2.996.

**Pre-registered predictions (logged before running):**

- **P1 (scale):** λ(β) varies smoothly and unimodally in β with
  peak-to-trough ratio between 2 and 50 — an offset-level effect (≤ ~4
  nats), NOT orders of magnitude; consistent with the marginal law pricing
  the shift of the lowest nodes, (π²/2)·Δln t ≲ 2 nats across the dial.
- **P2 (direction):** the maximizing β* ≥ 0.5 (nodes at or below midpoint
  phase — lower first node = more worth, per the marginal law's
  ln(eT*/t) weighting), with λ(β*)/λ(0.5) ≤ 3.
- **P3 (bracketing):** λ_true(m=24, Gcut=420) lies inside
  [min_β λ, max_β λ] of the family — phase alone brackets the arithmetic
  value at this L.
- **P4 (no Kadec catastrophe):** min_β λ ≥ λ(0.5)/50 — the log-density
  staircase has no collapse at any uniform phase, because super-Nyquist
  density excess below T* protects the frame (unlike critical-density
  Kadec).

Falsification consequences: P1 or P4 failing (orders-of-magnitude phase
sensitivity) would mean the "offset" language of §1.7 is wrong and phase is
a rate-level variable — bad for MF-2(b) and bad for T3's O(ℓ(D+1)) form
(a phase shift has D ≤ 1). P3 failing with λ_true ABOVE the family max
would be a genuine arithmetic surplus — evidence AGAINST density-only and
FOR Q3's anomaly being real (report to the Q3 adjudication either way).
P2 failing (β* < 1/2) means the marginal-law weighting intuition misreads
the edge tradeoff; instructive, not fatal.

### §5.1 Results (run 2026-07-26; script `results/ias/magic-functions/beta_dial.py`, log `beta_dial_L2485.log`; ~20 s total)

COMPUTED (L = 2.485, m = 24, first K = 180 nodes of each multiset, dps 40):

| β | t₁(β) | λ |
|---|---|---|
| 0.10 | 17.236 | 1.6499e−11 |
| 0.25 | 16.275 | 4.8379e−11 |
| 0.40 | 15.250 | 1.4944e−10 |
| 0.50 | 14.521 | 3.2861e−10 |
| 0.60 | 13.746 | 7.4928e−10 |
| 0.75 | 12.463 | 2.8263e−9 |
| 0.90 | 10.947 | 1.2674e−8 |
| **true zeros** | 14.135 | **3.3801e−10** |

**Prediction scoring (honest):**

- **P1 FAILED.** λ(β) is MONOTONE increasing across the whole dial (no
  interior optimum in (0,1); max at the grid boundary β = 0.90), and the
  peak-to-trough ratio is 768, far above my [2, 50] band. Diagnosis of my
  error: I priced only the lowest node's shift; the correct price is the
  marginal-law worth summed over ALL nodes below the capacity height eT*
  (13 nodes here), see the transport check below.
- **P2 half-PASSED.** Direction right (β* > 1/2: sliding nodes down helps,
  as the ln(eT*/t) weighting demands); magnitude clause failed
  (λ(β*)/λ(0.5) = 38.6, not ≤ 3) — same diagnosis as P1.
- **P3 PASSED** — but rendered nearly vacuous by the wide family range. The
  sharp post-hoc version: interpolating the family at λ_true gives
  **β_eff(true zeros) = 0.5034** — the zeta ordinates sit at the midpoint
  phase to 0.3% of a mean spacing, while the λ-optimal phase in the naive
  class is at the class BOUNDARY.
- **P4 PASSED**: min_β λ = λ(0.10) = 1.65e−11 ≥ λ(0.5)/50 = 6.6e−12
  (barely; the margin would fail for β → 0). No Kadec-type collapse under
  uniform phase.

**Post-hoc consistency check (COMPUTED, not pre-registered, labeled as
such).** Treating the β-slide as transport of each node t_k by
dt_k/dβ = −1/N̂′(t_k) and pricing it with the program's marginal law
(worth (π²/2)ln(eT*/t) per zero, so d(ln λ)/dβ = (π²/2)·Σ_{t_k ≤ eT*}
1/(t_k N̂′(t_k)), discrete sum S = 1.726 here):

- β 0.25 → 0.75: predicted 4.260 nats, measured 4.068 — ratio 0.955;
- β 0.10 → 0.90: predicted 6.815 nats, measured 6.644 — ratio 0.975.

The marginal law, measured by the law-theory seat via single-zero DELETION,
predicts collective PHASE TRANSPORT to 2.5–4.5% in the exponent with zero
fitted parameters — even though deletion worths are known to be ~20%
non-additive. Transport along the flow appears additive where deletion is
not (consistent with it being the integral of the first-order derivative).
This is a new, independent validation mode for the marginal law and for T4.

**Consequences for this seat's candidates and for the panel:**

1. **MF-2(b) must be restated** (the test did its job): within the naive
   discrepancy class the staircase is NOT near-optimal — the concave
   program's optimum is bang-bang at the class boundary (as MF-2(a)
   predicted structurally), and pure phase buys e^{(π²/2)·Δβ·S}. The
   correct universal-optimality conjecture is relative to the MEAN-ZERO
   discrepancy class (sign-changing N_Λ − N̂, the class the zeros actually
   inhabit: β_eff = 0.5034): among balanced multisets of RvM density, the
   midpoint staircase is near-λ-optimal for every L simultaneously and the
   zeros track it to O(1) in the exponent. Restated accordingly; the
   L = 3.555 anomaly (Q3) now has a phase reading: factor 6.3 ≈ e^{1.84}
   corresponds to Δβ_eff ≈ +0.1–0.2 at that window's sensitivity — a
   *measurable* effective-phase excess; recommend the Q3 adjudicators run
   this same dial at L = 3.555 alongside the Gcut escalation.
2. **A data point for T3 (DG seat).** Between the β = 0.1 and β = 0.9
   staircases the counting functions differ by at most 1 everywhere
   (D = 1), and |Δ ln λ| = 6.64 at ℓ = 1.2425: T3's constant obeys
   C₀ ≥ 6.64/(ℓ·(D+1)) ≈ 2.67 — ABOVE the DG seat's jitter-measured
   empirical Lipschitz band (1.0–2.3 at the same ℓ). Uniform phase
   transport is a strictly worse case than jitter for the transfer
   constant; T3's proof budget should be sized against phase, not jitter.
3. **The λ-functional does not "see" rigidity the way the slogan says.**
   "Maximally rigid = maximal λ" is false as stated (phase beats rigidity
   inside the class); what the zeros optimize is *balance* (mean-zero
   discrepancy), not λ. Whatever variational principle selects the zeros'
   configuration, it is not the frame bound itself — a constraint any
   "zeros as extremizers" story (log-gas seat, quantum-chaos seat) must
   respect.

---

## Round 2 — colloquium (magic-functions)

2026-07-26, after reading all seven other SEAT files and COLLOQUIUM-BRIEF.md.
Honesty tiers throughout; new numerics pre-registered in-file (§R2.2.1a)
before running; the C-8 literature check was executed live this session
(WebSearch/WebFetch against arXiv; details in §R2.2.3).

## R2.1 Bet responses (every §4 bet placed on this seat)

**(a) quasicrystal bet 5 (their conf. 0.40): "BRS kernel = analytic
continuation of the dual witnesses; NNLS atoms are finite-m shadows of BRS
residues; BRS basis norms encode (b, μ); one BRS basis-function norm at T*
reproduces (π²/2)ln(eT*/t)." — ACCEPT the frame, REFINE the payload, REFUTE
the last clause as stated.** Accept: their §1.1 reading (λ(L) = the
condition-number asymptotics of BRS recovery) is exactly my §1.6, and their
venue data resolves my UNVERIFIED flag (Constr. Approx. 57 (2023) 405–461;
arXiv:2005.02996 — two independent memories now agree). Refine: by my MF-1(b)
the NNLS atoms converge to atoms of *window-equivalent Krein extension
measures*, which are deformations of the zero measure — not evaluations of
the BRS biorthogonal system; the displaced atom (14.079 vs 14.1347) is the
deformation, and BRS residues sit at the *exact* zeros by construction. So
"finite-m shadows of BRS residues" is right only in the m → ∞, λ → 0 limit
and after the displacement is priced (quantum-chaos's semiclassical
displacement bet — my Round-1 bet 4 — is the missing factor). Refute as
stated: a single BRS basis-function norm cannot reproduce the marginal law —
BRS normalization is tied to the unconditional two-sided node pair (zeros;
log n) at critical density, while the marginal law is a *windowed,
super-critical* quantity with the capacity endpoint eT*(L) moving with L; no
single L-independent norm carries ln(eT*/t). The repairable version, which I
co-sign as a joint diligence item: the L-dependence of the windowed
*truncation* of the BRS system — condition number of the first N(T*) basis
functions restricted to PW_{L/4} — should reproduce the envelope's E(L), and
its one-node sensitivity the marginal law. That is a computation (days), not
a theorem, and I place it on the MF-4 diligence stack.

**(b) free-boundary bet 3 (their conf. 0.5): "magic-functions exhibits an
interpolation basis adapted to the staircase whose tail behavior matches the
corner-jet hierarchy (their kernels' boundary jets are the same atoms),
giving the certified full-infimum template its optimal atoms." — ACCEPT,
with one correction of emphasis.** Their FB-T1 measurement (trace exists;
far tail = trace's tail; one atom buys exactly two powers) is the boundary
half of an interpolation-remainder statement, and the atoms (indicator,
tent, …) are precisely the singular parts that any interpolation kernel on
[−a, a] must carry (transforms with 1/(ir)^k heads and closed-form
Ω̄-couplings — my native objects). Correction of emphasis: the "optimal
atoms" are not free-standing basis elements but the *jet coordinates* of the
Wiener–Hopf factorization at the endpoints — FB's own §5 retraction (the jet
is O(1), not small; atoms must enter as certified directions) says exactly
this, and it is why the merged lemma (M2 below) is stated as
jet-plus-staircase-data determines φ with remainder, not as "a better
basis". Division of labor in M2.

**(c) riemann-hilbert bet 4 (their conf. medium): "interpolation-basis
technology gives the sharp constructive upper bound in RH-1(a) faster than
the steepest-descent lower bound; the constant extracted for the anchor cost
will be the +2-nats gap." — ACCEPT, and the coordinator has made it my
assignment (C-3).** I take the bet with their own quarantine (their §3.5
K5-discipline) attached: the construction will be run with a pre-registered
prefactor ledger, and whether the anchor line of that ledger prices at ≈ +2
nats is an OUTPUT, not a target. Two contributions their seat should hold me
to: (i) my §5.1 transport check (marginal law predicts collective node
transport to 2.5–4.5% with no fitted parameters) is the error-budget
license for the construction's node bookkeeping; (ii) the construction
discriminates their p ∈ {9/2, π²/2} because a constructive prefactor is a
finite product of NAMED factors (engaged edge modes → half-integer counts;
retained-worth terms → π²/2 units) — the two candidates are not degenerate
on the construction side. Full protocol in §R2.2.2 and M1.

**(d) proof-theory B1 (their conf. HIGH): "the a-priori regularity theorem
of FULLINF §10 is equivalent to an interpolation-basis remainder bound
adapted to the RvM staircase; magic-functions can produce the basis or show
the density is wrong for it. Secondary: LP dual witnesses and template
countermodels are the same objects." — ACCEPT both halves, with the density
answer given now.** Density answer: the staircase alone is NOT a uniqueness
set for PW_{L/4} at any finite height (HA's counterexample; sub-critical
one-sided data — my §1.6), so a *pure* staircase interpolation basis with
remainder does not exist; the correct data set is (staircase head) ∪
(boundary k-jet) ∪ (anchor band) — the jet supplies exactly the finitely
many missing dimensions, which is why FB-T1's measurement and PT-2(iii)'s
necessity metatheorem converge on the same object. That convergence is M2.
Secondary half: agreed, and sharper — my MF-1(b) identifiability statement
and their PT-2(ii) countermodel are logically dual: identifiability says
"every interface-consistent representation is trapped near the zeros";
their ψ is the certificate that WITHOUT the support axiom the interface
traps nothing. A failed NNLS fit at tight residual at any window would be
simultaneously my kill event and their constructed ψ; I adopt their
falsifier wiring verbatim.

## R2.2 Adjudications

### R2.2.1 C-1 (the rigidity trichotomy): two of the three are the same
statement; the third is the mechanism, strictly stronger — with a
separating example, pre-registered and run below

**Claim (adjudication, with proof sketch).** At first order and fixed L,
midpoint phase (this seat) and worth-weighted charge neutrality
(quantum-chaos) are THE SAME statement, intertwined by the unit-slope
linear-response law that three seats have now measured independently. The
log-gas spectral gap is strictly stronger: it implies neutrality at EVERY
window simultaneously, and no fixed-L functional equation implies the gap.

*Equivalence (i) ⟺ (iii), quantitative.* For the phase family, the smoothed
deficiency field is δN ≡ (β − ½) on the band, so quantum-chaos's functional
is I_w = (π²/2)(β − ½)·∫_{t₁}^{eT*} dt/t — linear in (β − ½) with the SAME
kernel as my transport sum S = Σ 1/(t_k N̂′(t_k)) (discrete form; S = 1.726
vs the integral 1.405 at L = 2.485). Measured slopes of ln λ per unit
(β − ½): mine 8.24 nats (β ∈ [0.5, 0.6] rungs) against the transport
prediction (π²/2)·S = 8.52 — ratio 0.967; quantum-chaos's CUE regression
slope on I_w: 0.96; log-gas's CUE regression slope on (π²/2)J: 0.954. Three
families (phase flow, CUE ensemble, CUE ensemble independently), one
unit-slope law. Translating my dial: β_eff(true) − ½ = 0.0034 ⟺
I_w(true) ≈ 0.0034 × 8.52 ≈ **+0.03 nats**, same sign and order as
quantum-chaos's directly measured I_w(true) = +0.07 (the residual factor is
their lower integration cutoff and discreteness bookkeeping). Both
instruments say: worth-neutral to ≲ 0.1 nat. These are one measurement in
two charts. VERDICT: (i) = (iii), THEOREM-level modulo the linear-response
lemma that LG-1/R1 already own jointly.

*Strictness of (ii).* Gap ⇒ neutrality-at-all-L: the worth window
w(t) = 1/t on [t₀, eT*] has Fourier content concentrated at |k| ≲ 1/t₀ ≪
ln 2, so a field with no spectral mass below ln 2 couples only through the
1/(t₀ ln n) tails (log-gas §1.4's computation — I endorse it as written).
Converse FAILS at fixed L: a low-k counting modulation with window-tuned
phase is charge-neutral at that L while carrying all its mass inside the
gap. Note the sharpening this forces: neutrality at ALL L is genuinely
closer to the gap (the windowed integrals of a fixed low-k mode oscillate
in ℓ with amplitude A/k₀, so all-L neutrality pushes A → 0 at each fixed
k₀ < ln 2) — the honest hierarchy is: gap ⇒ all-L neutrality ⇒ fixed-L
neutrality = midpoint phase, with the first implication tight up to the
prime-tail and the second strict.

**Proposed co-signed statement (for quantum-chaos, log-gas, and this
seat):** *"The ζ deficiency field is worth-neutral at every window:
I_w(L) = O(0.1) nats for all measured L, equivalently β_eff(L) = ½ + O(10⁻²)
in the phase chart; the mechanism is spectral — by the explicit formula the
field's Fourier content lies at k ≥ ln 2, above every worth window's band.
The three Round-1 statements are this one statement at first order; they
separate only at second order (quantum-chaos's intrinsic −0.66, log-gas's
bias +0.5, this seat's dial curvature), where the gap is load-bearing and
neutrality alone is insufficient."*

#### R2.2.1a Pre-registered separating-example test (SEP) — written BEFORE running

Design: L = 2.485, m = 24, K = 180, same instrument and config as §5.1
(`frame_form`, dps 40). Two modulated staircases, N_config(T) = N̂(T) +
A·sin(k₀·u + φ), u = ln(T/2π), amplitude A = 0.35 (sup|δN| = 0.35, well
inside the measured linear regime), wavenumber k₀ = 0.35 < ln 2 (IN the
spectral gap):

- **MOD-N (neutral phase):** φ = φ₀ := −k₀(u₀ + u_X)/2 with u₀ = ln(t₁/2π) =
  0.8377 (t₁ = 14.5213), u_X = ℓ + 1 = 2.2425 — smoothed window charge
  J = 0 by construction. Fails the gap, passes neutrality.
- **MOD-C (charged control):** φ = φ₀ + π/2 — maximal charge,
  J_C = 2A·sin(k₀(u_X − u₀)/2)/k₀ = 0.4867, predicted I_w = (π²/2)J_C =
  **+2.40 nats** (surplus sign: raises λ).

Locked predictions:
- **SEP-P1:** |Δln λ(MOD-N)| ≤ 0.4 nats AND ≤ 0.2·|Δln λ(MOD-C)| — at fixed
  L, first-order neutrality is what the functional prices, even for pure
  in-gap spectral mass.
- **SEP-P2:** Δln λ(MOD-C) = +2.40 × (1 ± 0.35) nats (unit-slope linear
  response; band covers discrete-vs-smoothed bookkeeping).
- **SEP-P3 (the C-1 payload):** both pass ⇒ the trichotomy resolves as
  adjudicated: neutrality (= phase) is the fixed-L content; the gap is the
  all-L mechanism; the measured |Δln λ(MOD-N)| itself (predicted in
  [0.02, 0.4]) is the second-order term where the statements separate.
- Discrete I_w is computed exactly for both configs (staircase Fubini sums);
  locked: |I_w^disc(MOD-N)| ≤ 0.3 nats.

Script `results/ias/magic-functions/sep_test.py`; results appended in
§R2.2.1b below, unedited scoring.

#### R2.2.1b SEP results (run 2026-07-26; log `sep_test.log`; ~15 s)

COMPUTED: base λ = 3.286116e−10 (regression: matches §5.1 exactly);
MOD-N: λ = 2.7358e−10, Δln λ = **−0.183** nats, discrete I_w = −0.107;
MOD-C: λ = 6.8806e−9, Δln λ = **+3.042** nats, discrete I_w = +3.239
(smoothed prediction was +2.402; the discrete charge is the honest
predictor and the gap to smoothed is pure staircase-discretization
bookkeeping).

- **SEP-P1: PASS.** |−0.183| ≤ 0.4 and ratio |N|/|C| = 0.060 ≤ 0.2.
- **SEP-P2: PASS** (at the band's top edge against the smoothed prediction;
  against the exact discrete charge the slope is 3.042/3.239 = **0.94** —
  the unit-slope law's fourth independent appearance: 0.955/0.975 (my §5.1),
  0.96 (quantum-chaos), 0.954 (log-gas), 0.94 (here)).
- **SEP-P3: PASS.** The separating example stands: a configuration with ALL
  its deficiency mass inside the spectral gap (k₀ = 0.35 < ln 2) but tuned
  charge-neutral costs −0.18 nats, of which −0.11 is its residual discrete
  charge — the genuinely-second-order remainder is **−0.08 nats**. At fixed
  L the functional prices charge, not spectral position; the gap's role is
  to enforce charge-neutrality at every L at once. C-1 adjudicated as
  claimed: (i) = (iii) at first order; (ii) strictly stronger, and the
  strictness is worth only ~0.1 nat at this amplitude.

### R2.2.2 C-3 (the +2.08-nat constant gap): adjudication protocol from
above, with the prefactor ledger fixed now

I accept the assignment. Honest ground rules first: every deep λ is a
Rayleigh–Ritz UPPER bound, so the measured A′ = 16.75 ± 0.10 is itself an
upper-bound-side constant; a constructive bound can therefore CONFIRM the
gap as real structure (if the best construction also lands ≈ 2 nats above
Fuchs) or EXPOSE it as residual convergence bias (if a construction beats
the measured constant toward 14.68). The two outcomes are cleanly separated
because the construction is fully explicit — no eigensolves, no RR bias.

**The pre-committed prefactor ledger** (every line a named factor; the sum
is A′_constr, and no line may be tuned after the numbers are seen):
1. Fuchs barrier normalization at the engaged edge index (the 1−χ₂-class
   constant, 14.676 or 15.369 per normalization — riemann-hilbert owns the
   choice and I adopt theirs);
2. anchor/mass-partition cost: −ln(fraction of L² mass the construction
   retains below T*) — C-11's vector data (≈30% of E spent below T*,
   smallness-without-vanishing carrying 80% of the margin) is the measured
   hint that this line is O(1) and positive;
3. stopping-height mismatch: 2π[D(e^{w}T*) − D(e^{w∞}T*)] for the
   construction's actual w vs w∞ (free-boundary's exact chain makes this
   line exact algebra);
4. edge-matching factors at T* (soft/Airy entry) and T_s (detachment) —
   the half-integer-count line; this is where p ∈ {9/2, π²/2} stops being
   degenerate: engaged-mode counts contribute half-integers, retained-worth
   terms contribute π²/2 units, and the ledger forces the builder to say
   which.
PREDICTION (CONJECTURE, logged): lines 2–4 sum to +1.5 to +2.5 nats — i.e.
the measured Δ = +2.08 is real structure, dominated by line 2 (the anchored
mass partition that the pure Fuchs problem does not pay). Kill: a completed
ledger summing to < +1 nat means the deep ladders are not converged and Q1's
bias warnings reactivate at the constant level.

Discriminating data I endorse: the finished L = 5.50 triple (riemann-hilbert
§5 P3: measured-law band −72.6/−72.7 vs Fuchs-literal −73.6 — a full decade).
Deliverable and division of labor: merge M1 below; pilot sized in R2.5.

### R2.2.3 C-8 (the Krein/screw prior-art diligence): executed; verdict issued

**What was checked, live this session.** (i) The repo's own sweep
(results/agent-prior-art.md §Suzuki block — fetched abstracts + local
extracts of all three screw papers). (ii) Web verification that the
real-world anchors exist as cited: arXiv:2206.03682 = Suzuki, "Aspects of
the screw function corresponding to the Riemann zeta-function", J. London
Math. Soc. 108 (2023) — confirmed live (arxiv.org/abs/2206.03682; Wiley
DOI 10.1112/jlms.12785); arXiv:2209.04658 = "The screw line of the Riemann
zeta-function and its applications" (→ "On the Hilbert space derived from
the Weil distribution", Canad. J. Math.) — confirmed live. (iii) A targeted
full-text interrogation of arXiv:2606.09096v1 ("Weil's quadratic form via
the screw function") on the four decisive questions.

**Findings.** Suzuki's framework defines the screw function in the
Kreĭn–Langer sense and states (citing his own [13] Thm 1.2) that **g is a
screw function on ℝ iff RH** — the GLOBAL positive-representation
dictionary is his, in print since 2022–23, resting on exactly the
Kreĭn(–Langer) corpus I invoked. The 2209.04658 abstract's "explains the
non-negativity of the Weil distribution by means of the norm" is the
Hilbert-space embedding form of the same fact. HOWEVER, the targeted
full-text check of 2606.09096 found: NO windowed Krein-continuation
statement (positivity on [−a, a] ⟺ extendability with positive spectral
measure); NO dual/variational characterization of λ_a as a supremum over
extension measures (his (1.7) is the primal Rayleigh quotient only); NO
Pontryagin/negative-square treatment of the pole; NO
quadrature/dual-witness/super-resolution content.

**VERDICT on MF-1, binding for this seat:**
- **MF-1(a) as a novelty claim is WITHDRAWN.** The global dictionary is
  Suzuki-on-Kreĭn–Langer (2022–2026), the windowed criterion is Yoshida
  1992/Bombieri 2000–2003, and the windowed extension statement, while
  apparently unwritten, is a routine application of classical Kreĭn–Langer
  interval-continuation to Suzuki's g_a — a *bridging remark* to be written
  with full credit (cite: Suzuki 2206.03682, 2209.04658, 2606.09096; Kreĭn
  1940; Kreĭn–Langer continuation papers), not a lemma to claim. Residual
  novelty of the windowed strong duality + the explicit ±i/2/one-negative-
  square pole bookkeeping: LOW-to-MEDIUM, downgraded from theorem-candidate
  to remark-candidate pending a full read of 2209.04658 (assigned to me,
  days — the fetch interrogated 2606 only).
- **MF-1(b) and MF-1(c) SURVIVE as this seat's own**: the finite-m
  dual-witness identifiability/super-resolution layer and the
  extension-set-width = envelope program are confirmed absent from the
  flagship screw paper by targeted interrogation, and nothing in the sweep
  or the search suggests them elsewhere. All Round-1 §1.3 text should be
  read with this verdict attached.

Sources: [arXiv:2206.03682](https://arxiv.org/abs/2206.03682),
[JLMS 10.1112/jlms.12785](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12785),
[arXiv:2209.04658](https://arxiv.org/abs/2209.04658),
[arXiv:2606.09096](https://arxiv.org/abs/2606.09096) (full text
interrogated at [html/2606.09096v1](https://arxiv.org/html/2606.09096v1)).

## R2.3 Merges (two, with named co-seats and division of labor)

**M1 — The Stopped-Chirp Constructive Bound with a named prefactor
(magic-functions × riemann-hilbert × free-boundary).** Statement: explicit
unit φ_ℓ ∈ H_L with ln Q_L(φ_ℓ) ≤ A′_constr − 4πe^{ℓ} + p·ℓ, built as
(WKB chirp annihilating the staircase to T_s = e^{w∞}T*) × (BM/interpolation
window holding Θ(1) mass below T*), prefactor assembled line-by-line per the
R2.2.2 ledger. Division: this seat owns the function family, the anchor/mass
ledger (line 2), and the node-transport error budget (licensed by §5.1);
riemann-hilbert owns lines 1 and 4 (Fuchs normalization, edge parametrices,
the p-count); free-boundary owns line 3 (w∞ = smooth pasting; their FB-2
chain is the exact algebra). Adjudicates C-3; is RH-1(a) and renormalization
R2(i) merged; C-2's co-signed theorem inherits whichever w-clause survives.
Effort: numeric pilot days (R2.5), paper bound weeks–months. Kill: pilot
rate off 4π by > 5% at L = 4.75 kills the w∞-frozen form (then w must be
optimized, free-boundary's drift clause).

**M2 — Regularity as an interpolation remainder: the wall-breaking spec
(magic-functions × proof-theory × free-boundary; = the C-10 co-sign from
this seat).** Statement: for near-minimizers of Q_L with bounded EL
residual, φ is determined by (boundary k-jet, values on the staircase head,
anchor band) with remainder tail τ_ψ(R) ≤ C_k R^{−(2k+1)} — a
support-recovery modulus. What each seat certifies a wall-breaking theorem
must contain: proof-theory — a modulus OUTSIDE the A1–A5 interface
(PT-2(iii): necessity, by proof mining); free-boundary — log-order
compatibility (no positive-exponent gain exists; the modulus must be
structural: jet + Wiener–Hopf endpoint layer, their FB-3); this seat — a
uniqueness/interpolation statement on staircase-plus-jet data (pure
staircase data is density-deficient — R2.1(d); the jet supplies the missing
finite dimensions). Division: FB owns the Wiener–Hopf endpoint analysis;
I own the interpolation-remainder machinery (atoms' closed-form transforms
and Ω̄-couplings); PT owns the metatheorem wrapper and the ψ-countermodel
wiring. First deliverable: the corner-corrected F4 (FB-3(i)) restated as
the finite shadow of this lemma — weeks.

## R2.4 Updates to Round-1 claims (kills, retractions, strengthenings)

1. **MF-1(a): withdrawn as novelty** (C-8 verdict above); reclassified as
   consolidation-with-citations. MF-1(b)/(c) stand, now with a live-web
   diligence record instead of a flag.
2. **RETRACTION — my §5.1 phase reading of Q3.** I suggested the L = 3.555
   factor 6.3 "has a phase reading: Δβ_eff ≈ +0.1–0.2". By the C-1
   equivalence, a β_eff excess IS first-order worth-weighted charge, and
   quantum-chaos measured that charge directly: I_w(true, 3.555) = +0.11
   nats against +1.84 needed. My proposed explanation is dead by their
   measurement, and log-gas's LG-2 concurs independently. I formally join
   the C-5 death verdict on all first-order explanations; truncation is the
   surviving suspect, and my recommendation to run the β-dial at 3.555 is
   downgraded to "only alongside the Gcut escalation, as a control".
3. **§5.1 consequence 2 (T3 constant, C₀ ≥ 2.67 "worse than jitter")
   REFINED**: the phase family is a pure coherent-charge family, and by the
   unit-slope law its cost is exactly its charge — so the right statement is
   log-gas's: T3-type transfer bounds must be stated in one-sided
   (deficit-charge) discrepancy, and priced against charge, not against
   sup|N₁ − N₂| jitter. I co-sign their proposed T3 restatement and
   withdraw the "worse than jitter" framing (same numbers, correct chart).
4. **MF-2(b) strengthened and finalized**: the correct class is now
   pinned by three independent instruments — the worth-neutral class
   (I_w ≈ 0 at every L; = mean-zero discrepancy = midpoint phase). The
   universal-optimality conjecture is restated over that class with
   log-gas's one-sided-deficit rider, and the SEP measurement adds: within
   the class, in-gap spectral mass at A ≲ 0.35 costs ≲ 0.1 nat — the
   class is "flat" to second order, which is exactly what simultaneous
   near-optimality across L requires. P4's no-collapse clause is
   scope-limited to sup|δN| ≲ 2 (log-gas's Poisson crossover).
5. **BRS citation resolved** (Constr. Approx. 57 (2023) 405–461,
   arXiv:2005.02996 — quasicrystal's independent record matches mine);
   MF-4's diligence read is upgraded to a concrete computation (R2.1(a)).
6. **MF-4 trichotomy updated**: the constructive Gap-2 route is now jointly
   framed with quasicrystal's QC-3 (slit-plane equilibrium) — my
   BM-construction is their clause (ii) discriminator between (H-e²) and
   (H-merger K₀ = e^{w∞} = 3.594); their QC-2 de-anchoring rate 2e²δ·e^{2a}
   prices the anchor my construction must hold. No change to the statement,
   ownership now shared (HA + QC-seat + this seat).
7. **§1.7 stands, strengthened** by C-11 (one universal E-normalized
   envelope profile across the crossover, ±0.02·E): rates and profile are
   structure-blind; offsets are where structure lives; proof effort on
   offsets. The C-3 ledger (R2.2.2) is that principle turned into lines.

## R2.5 Next action (single, sized)

**Build the stopped-chirp pilot at L = 4.75 with the R2.2.2 ledger
pre-registered** (M1's first deliverable, this seat's lines): implement the
chirp × BM-window ansatz with w frozen at w∞ = 1.2785, evaluate Q_L(φ) by
the existing exact instruments (no eigensolves), and read off the realized
(rate, p-line, A′_constr). Pre-registered decision rule: rate within 1% of
4π validates the frozen-w form; A′_constr ∈ [15.5, 18] confirms the +2.08
gap as real structure (C-3 adjudicated "real"); A′_constr < 15 reopens Q1
bias at the constant level. Sized: 2–4 days, one worker; doubles as
renormalization's R2(i) kill test and law-theory P4's successor. Everything
else this seat owes (2209.04658 full read, MF-1(b) writeup, M2's remainder
lemma) queues behind it.
