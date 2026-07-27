# SEAT — free boundary / potential theory / optimal transport

Round 1, written under the independence rule (no other SEAT file read).
Repo notation throughout: a = L/4, ℓ = L/2, T* = 2πe^ℓ, u = ln(T/2π),
ρ(t) = ln(t/2π)/2π, N(T) = (T/2π)ln(T/2πe) + 7/8, D(T) = (a/π)T − N(T),
E = −ln λ, w = ln(T_s/T*). Honesty tiers: THEOREM / COMPUTED / CONJECTURE /
SPECULATION. All new arithmetic quoted below was re-verified this session
(mpmath, 20 dps; and the FB-T1 run of §5).

## §0 Seat card

Toolkit: classical and thin obstacle problems (Caffarelli; Caffarelli–Salsa–
Silvestre); balayage, capacity, harmonic measure, two-constants theorem;
equilibrium measures with external fields and MRS numbers (Saff–Totik);
constrained equilibrium and saturated-region theory for discrete ensembles
(Rakhmanov; Dragnev–Saff; Baik–Kriecherbauer–McLaughlin–Miller); mass-parameter
flows of equilibrium measures (Buyarov–Rakhmanov); nonlocal variational
regularity incl. the small-order/logarithmic-Laplacian limit; Wasserstein
geometry and displacement interpolation.

## §1 Translation

The program's central objects are, almost verbatim, objects of constrained
potential theory. The dictionary, with the citations I would defend:

1. **λ(L) is a discrete-restriction ground state; its minimizer runs a
   zero-dodging strategy.** Under RH, E(L) = −ln λ is the value of an extremal
   problem for entire functions of exponential type a: make Σ_γ |F(γ)|² small
   at unit L² norm. The minimizer's transform vanishes on ("dodges") the low
   ordinates and pays for it in log-potential. This is a weighted Chebyshev /
   maximin problem of exactly the type Widom treated for translation kernels
   (Widom, Trans. AMS 100 (1961) 252–262; Landau–Widom, JMAA 77 (1980)
   469–481).

2. **The deficit measure and the balayage identity are a constrained sweep.**
   The exact identity of NT Round 2 — the super-Nyquist surplus on [T*, eT*]
   equals the deficit mass e^ℓ — is the mass-balance of a *constrained
   balayage*: sweep the deficit dμ_L = (a/π − ρ)₊dt (mass e^ℓ, on [0,T*]) onto
   [T*, ∞) subject to the density ceiling (ρ − a/π)dt (the only zeros available
   to dodge above Nyquist are the ordinates actually there). Saturating the
   ceiling from the left exhausts the mass exactly at eT*. Constrained sweeps
   of this kind are the saturated-region mechanism of constrained equilibrium
   problems: Rakhmanov, Mat. Sb. 187 (1996); Dragnev–Saff, J. Anal. Math. 72
   (1997) 223–259; the full band/saturated/void phase geometry is
   Baik–Kriecherbauer–McLaughlin–Miller, *Discrete Orthogonal Polynomials*,
   Ann. of Math. Studies 164 (2007) [BKMM]. The constraint density vanishes
   linearly-in-u at the LEFT edge T* (ρ(T*) = a/π exactly): soft entry. The
   right edge eT* is mass-determined: hard edge into remaining constraint.

3. **The stopping height is the free boundary of a self-consistent obstacle
   problem.** The floor phenomenon (DG-2(e): the minimizer's log-envelope
   descends along −A(T) and then floors at the per-sample scale ½ln λ) is
   complementary slackness: λ = 2Σ|F(γ)|² ≥ 2|F(γ_j)|² for every undodged
   ordinate, so the envelope is *obstructed from below* by the self-consistent
   level ½ln(λ/2). The contact set of this obstacle is the measured floor zone;
   its right endpoint is the stopping height T_s that the C4/w(L) protocol
   measures (the action-matching estimator w_E2 is literally the contact-point
   locator). Formulated in §2 (FB-2).

4. **The measured softening (eT*−t)^{3/2} is the soft-edge exponent of
   equilibrium problems** — the generic vanishing F ∼ (edge distance)^{3/2} of
   the effective potential at a band edge (Deift–Kriecherbauer–McLaughlin,
   J. Approx. Theory 95 (1998) 388–475), with the Airy layer of width
   (a·eT*)^{−2/3} as its fluctuation scale — PROVIDED the edge is an
   equilibrium band edge. Q7 (fixed profile vs Airy) is precisely the question
   whether it is; see FB-1(e) for what the existing two data points say.

5. **The Euler–Lagrange operator is a logarithmic-order nonlocal operator on
   an interval, with exterior Dirichlet condition.** The archimedean x-space
   kernel (PROGRAM §2.14) is w(u) = e^{−u/2}/(1−e^{−2u}) ~ 1/(2u) as u → 0:
   the singular part of the EL operator is exactly a 1-D *logarithmic
   Laplacian* (symbol ½ln(1+4r²) by Lemma A, sharp two-sidedly), plus a
   finite-rank pole term and finitely many bounded shift operators (primes).
   The right regularity model is therefore NOT the fractional Laplacian at any
   s > 0 but its s → 0 endpoint: Chen–Weth, Comm. PDE 44 (2019) 1100–1139
   (the Dirichlet logarithmic Laplacian); Jarohs–Saldaña–Weth, J. Funct. Anal.
   279 (2020) 108732 (small-order limits); Feulefack–Jarohs–Weth on small-order
   eigenvalue asymptotics [venue details UNVERIFIED from this offline seat].
   Consequences for the Wall Theorem F5 in §2 (FB-3).

6. **The T3 flow is displacement interpolation.** DG Round 2's Step-0
   configuration flow (linear interpolation of increasing sequences, order and
   separation preserved, no collisions) is Wasserstein displacement
   interpolation of the two counting measures (McCann's convexity mechanism);
   Danskin differentiation along it is the standard envelope-derivative along
   a geodesic. Offered observation: check displacement convexity of
   s ↦ ln λ(s) on the existing jitter data — if it holds even empirically, the
   G1 far-field estimate only needs to be proved at the ENDPOINTS of the flow,
   not uniformly along it (convexity pins the interior).

7. **Prior-art positioning.** The claim "eT* is an MRS number" (seed (b)) is,
   in this dictionary: eT* is the endpoint of the support of a constrained
   equilibrium/balayage problem, determined by a Mhaskar–Rakhmanov–Saff-type
   mass condition (Mhaskar–Saff, Constr. Approx. 1 (1985); Saff–Totik,
   *Logarithmic Potentials with External Fields*, Grundlehren 316, Springer
   1997, Ch. IV). The count-saturation identity N(eT*) = (a/π)eT* + O(1)
   (DG §1(i); exact zero of the signed integral, coordinator errata #2) IS the
   MRS condition of the constrained problem — zeroth-moment form, because the
   constraint is graded rather than the field.

## §2 Candidates

### FB-1. The Constrained-Sweep Theorem (eT* as an MRS/balayage endpoint) — seed (b)

**Statement (CONJECTURE, theorem-shaped).** Let σ = ρ(t)dt on [T*, ∞) and
ν₀ = (a/π)dt. Consider the constrained minimization
  min { ∫∫ ln|1 − s²/t²|⁻¹ dη(s) dη(t) − 2∫ U(s) dη(s) } over
  η ≥ 0 on [T*, ∞), η ≤ σ − ν₀, η([T*,∞)) = e^ℓ,
where U is the (explicit) log-potential of the deficit measure μ_L. Then:
(i) the minimizer η* is the saturated sweep: η* = (ρ − a/π)dt on [T*, A_ℓ]
with A_ℓ = eT*(1 + O(e^{−ℓ})) — the constraint binds everywhere on its
support, and A_ℓ is determined by the mass condition
∫_{T*}^{A}(ρ − a/π)dt = e^ℓ (the NT Round-2 identity, exact);
(ii) [the value statement] the variational horizon of the frame problem is
A_ℓ: the single-zero marginal worth f(t) equals 2[U^{η*}(t) + U^{μ_L}(t) − F_eq]
on the saturated zone and 0 beyond A_ℓ, reproducing law-theory RUN 4's
support endpoint; (iii) [MRS form] A_ℓ is the unique solution of the
count-saturation equation N(A) = (a/π)A + O(1), i.e. eT* is an MRS number for
the constrained problem, and the lower-bound construction value 2A(eT*) = T*
(THEOREM already, by DG-2.3's route: dodge-all-quantiles + the exact algebra
2π[D(T*) − D(eT*)] = T*).

**Why this is the right formalization.** The obstacle-problem structure is
forced: constrained equilibrium = double obstacle problem for the potential
(where η = constraint: potential inequality one way; where η = 0: the other),
and the phase boundary between "saturated" and "void" is a free boundary
determined by mass balance when the constraint is approached from a region
where it binds — exactly BKMM's saturated-region geometry, transplanted from
discrete OPs to the frame problem. What the seat adds beyond the panel's T1′:
the *identification of which classical problem this is*, which imports a
complete existence/uniqueness/regularity theory (Dragnev–Saff) and a
ready-made edge taxonomy (band–saturated junction: square-root vanishing of
σ − η*; band–void: (·)^{3/2} of the effective potential; hard edges:
discontinuous). The left edge T* is a saturated–void junction with LINEAR
(in u) constraint vanishing — a degenerate/marginal case — and the right edge
eT* is mass-determined. The taxonomy PREDICTS: worth-profile softening near
eT* of soft-edge type only if the junction at eT* is band-type; if the sweep
is saturated all the way to A_ℓ (as claimed), the edge is HARD and the
softening must come from the finite-a Airy smearing of a hard edge, width
(a·eT*)^{−2/3} in relative height. This is exactly SYNTHESIS Q7 — the
adjudication differentiates my (i) from a genuinely band-type alternative.

**(e) What the existing data already says about Q7 (COMPUTED this session,
from the published RUN-4 table, no new runs).** The two softened worth points
sit at u = γ/T* = 2.020 (L = 2.485, suppression 0.50) and u = 1.996
(L = 2.996, suppression 0.56) — nearly identical u, nearly identical
suppression — which reads fixed-profile; but in the Airy variable they sit at
ξ = 2.84 and 3.95 widths below the edge, and deeper-ξ-yet-closer-to-1 is also
the correct Airy direction. Two points cannot separate the hypotheses. The
seat's calibrated refinement for HA-P2's four surgeries at L = 3.4:
Airy scaling calibrated on the L = 2.485 point predicts u_half ≈ 2.29
(the LOW edge of HA's stated [2.2, 2.5]); fixed profile predicts 2.0 ± 0.1.
Also COMPUTED: the one-cut artanh profile π²[artanh√(1−x) − √(1−x)]
(x = t/eT*) is DEAD as a global worth shape — it predicts 4.54 at the
(L = 2.485, γ = 14.5) point where the pure log predicts 6.94 and 6.923 is
measured. The bulk has ZERO additive offset; any equilibrium derivation must
produce a density uniform-in-u deep in the bulk with edge corrections
confined to the last e-fold. This kills the naive "one-cut with edge at eT*"
ansatz before anyone spends effort on it — the constraint really is active
(saturated sweep), not spread (band).

**Proof route.** (1) Existence/uniqueness/characterization of η*: verbatim
Dragnev–Saff (their Theorems 2.1–2.6 genre) after the change of variables
u = ln(t/2π) which makes all kernels convolution-type on the half-line; the
log-kernel in u is exact up to a bounded correction (ln|1−e^{2(u−v)}|-type
kernels; bounded distortion lemma needed — routine). (2) Saturation of the
constraint on [T*, A]: verify the variational inequality using the explicit
potential of μ_L — a finite computation with the Frullani-type integrals
already in THEOREMS.md Lemma A's toolkit. (3) The value statement (ii) is the
real work: connect the equilibrium potential gap to the rank-two secular
identity of T4/H2 (worth = ln(1 + 2|ψ̂₋(t₀)|²/λ₋)); the bridge lemma is a
defect-Green's-function identity, stated below as the concrete first
computation.

**The concrete first computation (offered to HA/NA; minutes-scale).** Define
the finite sum, for a staircase quantile t₀ ≤ eT*:
  G(t₀) = Σ_{quantiles t_k ≤ eT*, k ≠ 0} ln|1 − t₀²/t_k²|
        − [same sum with t_k replaced by the budget lattice of density a/π].
CONJECTURE: 2·G(t₀) = (π²/2)ln(eT*/t₀)·(1 + o(1)) in the bulk. If this finite
sum reproduces the measured worth (it is a pure arithmetic check against the
RUN-4 table), the marginal law is a potential-gap statement and T4's constant
derivation reduces to a Riemann-sum estimate — the equilibrium route to π²/2.
If it misses by an O(1) factor, the worth is NOT a bare potential gap and the
secular identity's denominator (λ₋-normalization) carries structure the
equilibrium picture lacks — either outcome redirects months of effort.

**Effort.** (1)–(2): weeks (a competent Saff–Totik practitioner). (3): months,
shared with T4. **Interfaces.** Consumes: NT's exact identities (R-series),
Lemma A. Feeds: T1′ semantics, T4's constant, C3's chain reading, Q7 design.
**Kill criteria.** The G(t₀) sum missing by a growing factor kills the
potential-gap reading; a Q7 verdict of "fixed profile" with the u_half = 2.0
value kills the hard-edge-Airy sub-claim of (i) (but not the sweep itself —
it would mean the smearing is potential-shaped, i.e. the finite-ℓ constraint
edge is resolved by the kernel, not by fluctuations); a violation of the
saturation inequality in (2)'s finite check kills (i) outright.

### FB-2. The self-consistent obstacle problem for the stopping height — seed (a)

**The exact algebra first (COMPUTED, re-verified this session; the identities
are exact).** Surplus(w) := ∫_{T*}^{e^w T*}(ρ − a/π)dt = (T*/2π)[e^w(w−1)+1];
Surplus(1) = e^ℓ = deficit mass (balayage identity); E + A = 2π·Surplus(w) for
the action bookkeeping E + A = 2π[D(T*) − D(e^wT*)]. Therefore:

  **the 4π cap ⟺ E + A = 2T* ⟺ Surplus(w∞) = 2e^ℓ ⟺ e^{w∞}(w∞−1) = 1,
  w∞ = 1.27846, T_s/T* = 3.5911.**

The smooth-cap hypothesis is EXACTLY the statement: *the sweep runs a second
epoch — past the balayage height eT*, dodging continues until the swept
surplus equals twice the deficit.* Moreover the DG Round-2 consistency ODE
w′(ℓ) = g(w) = (1 − e^w(w−1))/(e^w w) has w∞ as its unique positive fixed
point with g′(w∞) = −1 exactly (verified): the cap, if the mechanism is right,
is an exponentially attracting fixed point of the stopping-height flow, with
w − w∞ ~ Ce^{−(ℓ−ℓ_c)}. This sharpens C4's protocol: the approach RATE to
w∞ is a parameter-free prediction (unit rate in ℓ), checkable on the same
deep vectors the DG seat is already processing.

**Statement of the variational problem (the seat's formalization of seed (a)).**
Fix the smooth staircase Λ_sm. For a symmetric finite S ⊂ Λ_sm ("dodge set")
and F = φ̂, φ ∈ L²[−a,a], ‖φ‖ = 1, F|_S = 0, put λ(S, F) = 2Σ_{t∈Λ∖S}|F(t)|².
Then E(a) = −ln inf λ. Continuum relaxation: over log-envelope potentials
Φ(T) = −∫ ln|1 − T²/s²| dδν(s), δν admissible iff δν = ν − ν₀ for the zero
measure ν of some F in the (Beurling–Malliavin) type-a cone, with the anchor
normalization Φ ≈ 0 on the mass-carrying zone [0, T*]:

  E = max over admissible Φ and dodge zones of  min_{t ∈ Λ∖S} 2Φ(t),

a maximin (weighted-Chebyshev) problem whose optimality system is an OBSTACLE
problem: the active set {2Φ = E} is the floor/contact zone [T_c, T_s], the
saturated zone [T*, T_d] carries δν = (ρ − a/π)dt (full dodging), and the free
boundaries satisfy (α) smooth fit at the floor entry T_c (C¹ matching of the
descending envelope to the floor — this is what makes the w_E2 action-matching
estimator consistent), and (β) the exchange condition at T_s: dodging one more
ordinate must not raise the floor, which is the multiplier balance between the
type budget (Jensen from the anchor — T1′'s hypothesis A, exactly) and the
marginal envelope gain. CONJECTURE (the seed's question, answered as far as
this seat can honestly take it): in the deep regime the multiplier of the
type-budget constraint activates (fillers below T* are exhausted at the FIRST
epoch's end, eT* — this is FB-1), the second epoch's suppression is bought by
the outer function (two-constants/harmonic-measure pricing, Nevanlinna;
Garnett–Marshall, *Harmonic Measure*, CUP 2005), and the optimality system
closes with the mass condition Surplus(T_s) = 2·Deficit — i.e.
**e^w(w−1) = 1 IS the free-boundary condition, in mass-balance form: the
free boundary stops when the constrained sweep has repaid the deficit twice —
once in zeros, once in smallness.** Status: the equivalence chain above the
box is exact arithmetic (THEOREM-level given the action identity); what is
conjectural is that the optimality system of the maximin problem produces the
second epoch with EQUAL mass — the factor 2 is measured (4π to 0.4–1.3%), not
yet derived. This converts the smooth-cap hypothesis into a sharply posed
free-boundary claim rather than a fit.

**Proof route.** (1) Γ-convergence of the discrete maximin to the continuum
obstacle problem: standard potential-theoretic discretization (Saff–Totik
Ch. I techniques + the separation of the staircase); (2) the optimality
system and phase diagram: convex duality — the maximin's dual variable is a
probability measure on the undodged ordinates (where the floor is attained),
and stationarity in Φ gives the balayage structure; (3) the second-epoch
pricing: the outer-function contribution to Φ on [eT*, T_s] costs harmonic
measure of the floor zone in the upper half-plane relative to the anchor —
the two-constants theorem gives the exchange rate; the CONJECTURE is that
this rate equals the first epoch's (per unit swept mass), whence the factor 2.
(4) Error control at the Airy layers. **Hardest step**: (3), and beneath it
the same wall DG-2(c) named — Beurling–Malliavin multipliers with type loss
o(e^{−ℓ}) (Mashreghi–Nazarov–Havin, St. Petersburg Math. J. 17 (2006);
Poltoratski's Toeplitz program). I do not claim a route through that wall;
I claim the problem statement above is the correct one to spend it on, and
that (1)–(2) alone already yield a publishable structure theorem (phases:
saturated / floor / free, two free boundaries, drift solution mid-range).

**Effort.** (1)–(2): months. (3): research program (the wall). **Interfaces.**
Consumes: T1′ (the anchor hypothesis is the Jensen budget's normalization),
FB-1 (first epoch), DG's C4 vector data (the falsifier). Feeds: C4-as-theory
(the 60–90-day allocation item), the renormalization seat (the flow w′ = g(w)
with its attracting fixed point is an RG statement), and the honest
asymptotics of the envelope beyond measurable range. **Kill criteria.** The
C4/B_smooth vector test failing (G ∈ [0.5, 2] edge-tracking per the DG
pre-registration) kills the second-epoch mechanism; a drift verdict in Q1
deletes the saturation clause and FB-2 reverts to the mid-range structure
theorem only; if the derived second-epoch exchange rate is NOT 1:1 in swept
mass, the measured 4π (0.4–1.3%) kills the specific pricing in (3) — note
4π is measured tightly enough that the factor-2 claim is genuinely
falsifiable by theory.

### FB-3. Corner-jet regularity and the F5 counterattack — seed (c)

**Direct verdict on the seed question (does CSS apply?).** No — and the reason
is structural, not technical. The EL operator's singular part has symbol
½ln(1+4r²) (Lemma A, sharp both ways): it is an elliptic operator of
LOGARITHMIC order, the s → 0 endpoint of the fractional family. Everything in
the CSS package needs s > 0: (i) the coercivity (−Δ)^s gives tail control
τ(R) ~ R^{−2s}; at s = 0 this degenerates to exactly Lemma B(v)'s logarithmic
budget — **Theorem F5 is the s = 0 endpoint of the standard fractional
coercivity scale, and it is sharp**; the "exponent CSS would give" is
literally zero. (ii) Almgren/frequency monotonicity and blow-up classification
need the scaling group r ↦ λ^{2s}: the log-symbol is scale-COVARIANT only
additively (dilation x → sx shifts the symbol by −ln s · Id — this is visible
in the repo's own mathematics: Theorem 1's dilation proof controls exactly
this shift via |r ∂_r W| ≤ 4). Blow-up limits therefore cannot see the
operator's order and the compactness machinery gains nothing per scale — in
precise agreement with FULLINF §10's empirical finding that bootstrap gains
iterated logs per step. The correct model theory is the logarithmic Laplacian
(Chen–Weth, Comm. PDE 44 (2019); Jarohs–Saldaña–Weth, JFA 279 (2020)), whose
known regularity is: interior gains logarithmic, boundary behavior of
log-type — never a positive exponent. Conclusion: **the a-priori regularity
theorem F5 asks for does not exist as a decay statement; the correct
replacement is a STRUCTURE statement.**

**The replacement (the seat's main proposal).** The minimizer's high-frequency
tail is not unknown mass to be bounded; it is the explicit Fourier tail of its
boundary jet. For φ supported on [−a, a] with one-sided boundary values
φ(±a∓), φ′(±a∓), …, integration by parts gives
φ̂(r) = [jump terms]/(ir) + [derivative-jump terms]/(ir)² + …, so the tail is
a finite-dimensional EXPLICIT family plus a remainder that genuinely decays.
**Corner-Jet Decomposition (CONJECTURE, now with measured support — §5):**
every Galerkin argmin (and, conjecturally, every near-minimizer with bounded
EL residual) satisfies φ = j_k(φ) + ψ_k, where j_k is the explicit k-jet
extension (k boundary atoms: indicator, tent, …, each with closed-form
transform and closed-form Ω̄-weighted integrals) and τ_{ψ_k}(R) ≤ C_k R^{−(2k+1)}.
FB-T1 (§5) measured, at (ζ, L = 7/4): the trace exists and is m-stable
(|φ_m(a)| = 0.0120/0.0107/0.0106 at m = 32/48/64), the raw tail is the
trace's tail quantitatively (h_φ → 1; τ_φ(287) = 3.8e−7, matching FULLINF's
independently measured 4e−7 — that number is now EXPLAINED), and one atom
buys exactly the predicted two powers of r (h_ψ → 1 in the r⁻⁴ law,
τ_ψ(1000)/τ_φ(1000) ≈ 0.036 → the asymptotic gain is real, though at R = 287
the payoff is only ×10 because the derivative trace is O(1)–O(5), not small).

**Why this breaks F5's wall rather than contradicting it.** F5 forbids
subspace-plus-tail arguments whose tail input comes from the form's
coercivity. The corner template needs NO coercivity: the k atoms enter the
certified block as k extra DIRECTIONS (exactly as the pole enters as rank 2),
with all couplings exact rationals/known special values — the certified
problem becomes (m+k)-dimensional, and the class hypothesis applies only to
the k-times-corrected remainder ψ_k, at tail exponent R^{−(2k+1)}. Arithmetic
of the payoff at F4's own operating point (L = 7/4, R = 284, τ̄-need ~1.5e−16):
k = 3 atoms suffice if C₃ ≲ 15 — i.e. the class hypothesis collapses from
"Sobolev s = 10 with M ~ 4e16" to "third derivative of the remainder bounded
by ~a constant", a class that (unlike F4's) plausibly CONTAINS the actual
argmins. What remains a-priori: bounds on the jet and on ψ_k's k-th
derivative for near-minimizers. That is where the honest difficulty
relocates, and it is a Wiener–Hopf question, not an ellipticity question:
near ±a the EL equation is a half-line convolution equation with symbol
c + ½ln(1+4r²) − λ (Krein's theory: M. G. Krein, Uspekhi Mat. Nauk 13 (1958);
AMS Transl. (2) 22 (1962)); the factorization of a log-growing symbol
produces endpoint behavior with log-scale corrections only (contrast
Carleman/Symm first-kind log-kernel equations, endpoint (a²−x²)^{−1/2}) —
consistent with a finite nonzero trace, which is what FB-T1 measures. The
prime shifts couple the endpoint layer only to interior points at distance
ln n (bounded operators; and any interior structure they generate is
log-regularized, consistent with kill-rule K1 — the retired "kink" language
is not needed or used here).

**Deliverable ladder.** (i) Weeks: the corner-corrected F4 — restate FULLINF
Theorem F4 with the k = 1 atom as an explicit extra direction; every
constituent is already in the repo's certified-arithmetic vocabulary;
prediction: the class covering the argmins themselves at L = 7/4 becomes
certifiable (F4's own §8 showed the argmins violate the current class by nine
orders). (ii) Months: the half-line Wiener–Hopf endpoint analysis for the
symbol c + ½ln(1+4r²) − λ: existence of the trace, the log-layer beneath it,
and jet bounds for exact minimizers. (iii) The near-minimizer version (bounded
EL residual) — this is the piece that would retire F5's obstruction for the
full-infimum program. **Interfaces.** Consumes: Lemma A, FULLINF F2/F3
machinery, CertFramework. Feeds: NT-4 composition (zero-exclusion pipeline
with an honest class), NA's inequality-form Lean redesign (k atoms = k more
rows), CS pricing. **Kill criteria.** FB-T1's P1/P2 failing would have killed
this on day one (they passed); the template dies if the jet of near-minimizers
is NOT a-priori boundable at fixed L (Wiener–Hopf analysis coming out
degenerate — e.g. trace instability in m beyond the measured rungs: the next
rung m = 96/128 measuring |t_m| drifting by > 20% would be a red flag);
and if C₃ at the F4 operating point exceeds ~10³ the payoff arithmetic fails
and prolates win after all (F6's alternative).

### FB-4. The π²/2 as a plunge/capacity constant — seed (d), brief

The measured marginal coefficient π²/2 should be read as the Landau–Widom/
Slepian plunge slope, not as a Robin constant of a static condenser: in the
sinc-kernel spectral problem the low eigenvalues obey ln(1/λ_n) ≈
π²(n − 2c/π)/ln c (Fermi-profile plunge; Landau–Widom, JMAA 77 (1980);
non-asymptotic versions: Bonami–Karoui, Constr. Approx. 43 (2016);
Bonami–Jaming–Karoui [exact venue UNVERIFIED offline]) — a per-mode slope π²
against the repo's per-deleted-pair π²/2, with the pair/parity bookkeeping
(each ± pair is one even-sector constraint) supplying a factor 2 that must be
tracked, not assumed. The honest potential-theoretic content available for
proof: in Widom's framework the sub-plunge decay rate is the Green's
function/harmonic-measure datum of the phase-space forbidden region, so the
correct target identity is worth(t) = 2·(equilibrium potential gap at the
deleted node) — which is FB-1(ii)'s bridge lemma, testable by the G(t₀) finite
sum above BEFORE any asymptotics are attempted. I deliberately fold seed (d)
into FB-1 rather than listing a separate lemma: if the G(t₀) test passes, the
"which capacity is it" question answers itself by computation; if it fails,
no Robin-constant reading was going to be right.

## §3 Intuition pumps (all SPECULATION unless tagged)

1. **The deficit is repaid twice: once in zeros, once in smallness.** Epoch 1
   ([T*, eT*]): relocate the e^ℓ filler nodes from below T* into the dodge
   zone — count-neutral, Jensen-cheap; ends exactly when fillers are exhausted
   (the balayage identity; note D(T*) = e^ℓ − 7/8 is the filler count,
   THEOREM-level arithmetic). Epoch 2 ([eT*, ≈3.6T*]): no zeros remain to
   relocate; suppression is bought as smallness-without-vanishing at the
   two-constants exchange rate, and the epoch completes when the second e^ℓ of
   surplus is swept: Surplus = 2·Deficit ⟺ e^w(w−1) = 1 ⟺ the 4π cap. The
   split it predicts for the action between descent zone and floor zone is
   ~42/58 at L = 2.485 — compatible with DG-2(e)'s measured "floor contributes
   the remainder". Cheap falsifier inside existing protocols: C4's node census
   should show the node count saturating at the budget through epoch 1 and
   then FLAT node counts (no new dodging zeros) through the floor zone — an
   observable the DG extraction already computes.

2. **Hele-Shaw reading of the ℓ-flow (Buyarov–Rakhmanov).** As ℓ grows, the
   deficit mass e^ℓ is injected and the saturated zone's free boundary A_ℓ
   advances: the family of constrained sweeps indexed by mass is exactly a
   Buyarov–Rakhmanov mass flow (Sb. Math. 190 (1999)), i.e. a Hele-Shaw/
   obstacle-problem front in the u-half-plane; d(value)/d(mass) = the Robin
   constant of the moving support. This would make dE/de^ℓ (the quantity the
   whole envelope program measures!) literally a Robin-constant readout, and
   the 4π cap the terminal Robin constant when the front stalls at w∞. If
   FB-1(1)–(2) land, this becomes a theorem schema, and "measure the envelope
   slope" = "measure the capacity of the sweep".

3. **The marginal worth is a Kantorovich potential.** The sweep is a transport
   problem (move deficit mass from [0,T*] to the surplus zone); the measured
   worth profile f(t), supported exactly on [0, eT*] and vanishing at the
   endpoint, has the shape and the complementary-slackness signature of the
   dual potential of that transport. Non-additivity of ~20% (K7) is then
   natural: dual potentials price marginal, not joint, relocations. If FB-1's
   G(t₀) identity passes, this stops being a metaphor: the worth IS the dual
   variable of the constrained sweep.

4. **s = 0 twice (tagged: half observation, half speculation).** The program's
   zero-slack theme (Λ = 0; margins collapsing to the knife-edge) has an exact
   operator-theoretic mirror: the archimedean operator sits at s = 0 of the
   fractional scale — zero polynomial coercivity, purely logarithmic ellipticity
   (this half is THEOREM-level, Lemma A + F5-sharpness). The speculative half:
   this is WHY the problem is hard in a structured way — every classical
   regularity/positivity technology (CSS, Almgren, capacity gains) delivers
   its conclusions in powers, and the Weil form only has logs to pay with.
   Techniques native to log-order problems (Wiener–Hopf factorization of
   log-symbols, Krein strings at spectral edge, iterated-log bootstraps) are
   the correct import list, and the corner-jet template of FB-3 is the first
   installment.

## §4 Cross-seat bets (ranked by confidence)

1. **Riemann–Hilbert seat (0.8).** They will independently identify the
   dodge-zone structure as BKMM's constrained-equilibrium phase geometry and
   propose steepest descent on the graded-lattice frame problem. Bet: their
   Airy-parametrix computation at the eT* junction settles Q7, and their
   answer to the marginal constant is the same object as FB-1(ii)'s potential
   gap — with the π²-vs-π²/2 pair bookkeeping resolved on their side. Joint
   deliverable if both seats agree: the worth-profile edge shape with
   constants.

2. **Log-gas seat (0.6).** The rigidity-class offset (smooth = true; Poisson
   +4.5 nats; GUE pending Q6) is a linear-statistics variance functional of
   the ensemble. Bet: λ_GUE lands within ~1.5 nats of the smooth staircase
   (inside DG-P3/NT-P2's shared band), and their DHK-style rigidity toolbox is
   what closes T3's G1 exceptional-set gap. Secondary bet: they will price the
   Poisson cost as the LIL of the counting discrepancy and get 4.5 nats to
   within a factor 2 from first principles.

3. **Magic-functions seat (0.5).** The C2 dual-witness quadrature (nodes at
   zeros, weights ≈ 2) is a Fourier-interpolation object: bet they exhibit an
   explicit interpolation basis adapted to the staircase whose tail behavior
   matches the corner-jet hierarchy of FB-3 (their kernels' boundary jets are
   the same atoms), giving the certified full-infimum template its optimal
   atoms — prolate-grade tails with closed-form couplings.

4. **Renormalization seat (0.4).** The dilation-shift covariance of the
   log-symbol + the stopping-height flow w′ = g(w), g′(w∞) = −1: bet they
   arrive at the same ODE as an RG flow with the 4π cap as its IR fixed point
   and the mid-range (ℓ + c₀) growth as the crossover scaling; if their
   beta-function derivation fixes the factor 2 of FB-2(3) independently, the
   smooth cap is derived twice and I will consider it settled.

5. **Proof-theory seat (0.3).** Bet: the corner-corrected F4 (FB-3(i)) is the
   cheapest route to a kernel-checked statement quantifying over an
   infinite-dimensional class that CONTAINS the numerical argmins — i.e. the
   first formal artifact about "the minimizers we actually see", and they
   will locate it lower in the reverse-math hierarchy than the prolate
   alternative (finitely many explicit atoms vs an eigenbasis that needs its
   own existence theory).

## §5 The cheap test — FB-T1, pre-registered and run

Pre-registration: `results/ias/free-boundary/PREREGISTRATION-FBT1.md`
(2026-07-26 21:34:55 UTC, before any curve was computed). Script + raw output
+ JSON: same directory (`fbt1_trace_tails.py`, `fbt1_output.txt`,
`fbt1_results.json`). Configuration: ζ, L = 7/4, spectral Legendre m = 32/48/64
(dps 35/28), boundary traces, period-averaged transform windows at
r = 500–3000, tail masses at R = 287 and 1000, corner-corrected remainder
ψ = φ − (c₀+c₁x)·1. Total runtime 107 s, one worker.

**Regression gate: PASS.** λ_48 = 3.143895e−5 (RESULTS EXPECTED 3.14389e−5),
λ_64 = 3.141596e−5 (FULLINF 3.1415961e−5). Minimizer purely even
(odd fraction ~1e−28); φ(a) = φ(−a) to machine.

**P1 (trace exists): PASS.** |t_m| = 0.011984 / 0.010710 / 0.010620 at
m = 32/48/64 — inside the pre-registered [0.005, 0.05], and within 20% of the
0.013 blind-inverted from FULLINF's tail before the run.

**P2 (the far tail is the trace's tail): PASS (mechanism), with an understood
finite-r correction.** h_φ → 1 from above on every rung (1.004–1.14 at m = 32;
1.06–1.60 at m = 48/64, the excess at r ≤ 1000 quantitatively explained by the
measured O(1) derivative trace entering at (φ′(a)/φ(a)r)²); log-log slope
−2.08 (m = 32), −2.25/−2.23 (m = 48/64, vs gate −2 ± 0.2 — the same admixture,
marginal as gated, mechanism unambiguous). τ_φ(287) = 3.8e−7 vs FULLINF's
independently measured ≈ 4e−7: **the Wall-theorem-adjacent tail measurement is
now explained as the boundary trace, quantitatively.**

**P3 (one atom buys two powers): STRUCTURE CONFIRMED, PAYOFF GATE FAILED AS
REGISTERED.** h_ψ → 1 in the r⁻⁴ law (0.94–0.95 at r = 3000; clean slope
−4.03 at m = 32); but τ_ψ(287)/τ_φ(287) = 0.084–0.106 against the
pre-registered ≤ 3e−4. Cause identified in the data: the derivative trace is
large (φ′(a) = 1.88/4.28/4.66, not O(t)) — my pre-registered guess about the
jet's size was wrong, and is retracted. Consequence absorbed into FB-3 as
stated above: corner atoms must enter as certified DIRECTIONS (jet unknowns in
the block), not as small corrections; the payoff argument runs on tail
EXPONENTS (measured: −2 → −4 per atom, as predicted), not on trace smallness.

**P4 (m-drift, reported not gated):** |t_48/t_32| = 0.894, |t_64/t_48| = 0.992
(sign flips are eigenvector convention). The first ratio lands on H_log's 0.90,
the second on H_const's 1.00 — inconclusive as anticipated at three rungs;
the top-rung stability mildly favors a genuine nonzero trace of the operator
minimizer (consistent with the s → 0/Wiener–Hopf expectation of FB-3, and
inconsistent with any power-law boundary vanishing). Next rung (m = 96/128,
minutes-to-hours) is the natural follow-up and is pre-declared in FB-3's kill
criteria: |t_m| drifting > 20% there is a red flag against the template.

**Net effect of the test:** FB-3 survives its two would-be killers (P1, P2),
gains a quantitative explanation of FULLINF's tail number, loses one
quantitative sub-claim (jet smallness — retracted), and acquires a sharpened
follow-up gate. Exactly what a pre-registered test is for.

---

*Files written by this seat: this file;
`results/ias/free-boundary/PREREGISTRATION-FBT1.md`,
`fbt1_trace_tails.py`, `fbt1_output.txt`, `fbt1_results.json`.
No repo source files touched.*

---

## Round 2 — colloquium (free-boundary)

Written after reading all eight Round-1 seat files, COLLOQUIUM-BRIEF.md
(C-1…C-11), and the DG seat's Round-3 Part B vector results
(PLAN-differential-geometry.md, the source of C-11). Honesty tiers throughout.
All new arithmetic quoted below was re-verified this session (mpmath, 20 dps);
the one new numeric (FB-T2) is pre-registered in §R2.5 below, in-file, before
its run.

### R2.1 Bet responses (all six bets placed on this seat)

**B←RH (riemann-hilbert §4 bet 1, their highest).** *"Their obstacle problem is
the constrained-equilibrium variational inequality of RH-2(ii); coincidence set
= saturation region; they derive the drift law and the Lambert point from
balayage; smooth fit = the 3/2/Airy softening."* — **Object identification:
CONFIRMED, independently.** My FB-1/FB-2 and their RH-2(ii) cite the same
machinery (BKMM saturation, Dragnev–Saff) from opposite ends; the coincidence
set = saturated sweep dictionary is exact. **Derivations: partially delivered.**
What I hold at THEOREM level is the identity web (§R2.2(a)–(b)), including that
their Lambert point and my root are the same number, verified analytically. The
drift law remains descriptive matching for both of us; neither seat has yet
derived the cap independently of the action identity — the honest state is
"equivalence web proved, one independent derivation missing" (their pump 1,
min-of-two-costs, is the candidate I find most likely to close first). **Smooth
fit = softening: qualified.** C-11's F5(i) refutes the pointwise Agmon envelope
at depth, so the C¹-matching must be stated on the integrated (action/count)
variables, not the pointwise envelope; and the Q7 update below now leans
fixed-profile over Airy at the worth edge. Their glue offer (upper from
construction, lower from BKMM descent, free-boundary optimality system from me)
is accepted — Merge A.

**B←renorm (renormalization §4 bet 1, high).** *"Smooth pasting reproduces
e^w(w−1) = 1 in one page; the mid-range drift is the same free boundary before
detachment."* — Same verdict as B←RH: the pasting condition is now PROVED
EQUIVALENT to the cap (given the action identity), not yet derived from an
independent variational principle; the one-page derivation does not exist yet
and I will not pretend the equivalence is one. Two of their items I adopt with
attribution: their eigenvalue-−1 clause and my g′(w∞) = −1 are the SAME
statement (both ⟺ subleading term O(ℓ), i.e. the Fuchs p·ℓ form) — recorded in
§R2.2(e) so the panel counts one fact, not three. Their R2(i) stopped-chirp
construction is the upper-bound lane of Merge A; my three-zone revision
(§R2.2(d)) changes its gluing spec: the chirp should be stopped at the measured
REGISTRATION endpoint (~2T*), not at e^{w∞}T*, with nodeless suppression
carrying the outer action — this is a material design correction from C-11.

**B←log-gas (§4 bet 1, conf 0.8).** *"eT*, the balayage identity, and the
(eT*−t)^{3/2} softening come out of ONE obstacle problem in u = ln t; they write
it in Round 2 with contact set ending at eT*; the string tension π²/2 appears as
their Lagrange multiplier."* — **The obstacle problem was written in Round 1
(FB-1), with the contact/saturated set ending at eT* by the exact mass
condition: that half of the bet pays.** The multiplier half is exactly my
FB-1(ii) bridge conjecture (worth = 2 × potential gap of the constrained sweep;
their string tension = my Kantorovich-potential pump — same object, two
dialects), and it is now put to a pre-registered numeric test in §R2.5 (FB-T2):
if the bare potential-gap sum reproduces the measured worth profile, "π²/2 =
Lagrange multiplier of the sweep" is quantitatively live; if not, the
λ₋-normalization carries O(1) structure and the string picture needs dressing.
The 3/2-softening clause I now hold at reduced confidence (Q7 update, §R2.2(d)):
their own f₈ replication (ratio 0.53 at u ≈ 2.0, same instrument-independent
value as RUN 4's 0.50) is a THIRD half-suppression point at u ≈ 2.0, and C-11's
registration endpoint sits at the same height — the softening is starting to
look registration-limited (fixed profile), not capacity-edge-Airy. Their LG-4
revision (pairwise W ≥ 0: capacity-dilation + edge-rehardening) reads naturally
in my frame — deleting a constraint node moves the balayage endpoint, so the
free boundary responds to deletions — and I endorse their revision-1 clause
(one-sided sup-DEFICIT hypotheses in transfer statements) as the obstacle
asymmetry itself: the infimum prices the worst local deficiency; surpluses do
not refund. That clause should be adopted into T3's hypotheses.

**B←MF (magic-functions §4 bet 2, conf 0.7).** *"MF-2(a)'s maximizer is
characterized by an obstacle problem whose contact structure is the balayage
identity; extension-set width and equilibrium exponent are Legendre-dual; w∞
drops out as their free-boundary condition."* — **Accepted with one crucial
disambiguation: there are THREE distinct obstacle problems now in circulation,
and conflating them will produce wrong theorems.** (i) FB-2: over test
functions at FIXED configuration (free boundary = stopping structure; the w∞
problem). (ii) MF-2(a): over CONFIGURATIONS in a discrepancy class (free
boundary = where the constraint |N_Λ − N̂| ≤ R binds; their β-dial measured its
bang-bang structure directly — optimum at the class boundary, confirming their
concave-program prediction). (iii) FB-1: over the swept DEFICIT MEASURE
(free boundary = eT*). These are pairwise dual, not equal. Their β-dial finding
3 ("the zeros optimize balance, not λ") constrains (ii) only — it does not
touch FB-2, which never claimed the zeros extremize anything. I take ownership
of the characterization lemma for (ii) they offered (bang-bang + obstacle
condition; their measured boundary optimum is the existence proof of the
bang-bang phase), and note their transport check (marginal law prices phase
transport to 2.5–4.5%) is the strongest evidence yet for the linear-response
kernel FB-1(ii)/FB-T2 tests on the deletion side.

**B←QC (quantum-chaos §4 B3, medium-high).** *"The drift law is the
moving-boundary equation and e^w(w−1) = 1 the C¹ smooth-pasting condition of a
1D obstacle problem with obstacle the Nyquist line; if derived, QC-4's
third-order transition follows for free."* — Pasting-equivalence proved,
derivation open (as above). Their QC-4 transition-order claim gets my
co-signature at CONJECTURE tier: for one-phase obstacle problems with a
saturating scalar free parameter, C² pasting of the value with a jump in the
third derivative is the generic order — their "obstacle problems saturate
third-order generically" is the correct free-boundary folklore, and the
finite-difference test they propose is the right cheap check. One correction
their B3 needs from C-11: the obstacle is NOT the Nyquist line seen pointwise
(F4: 30% of the exponent is spent BELOW T*; the transition band opens an
octave below the crossing) — the correct obstacle is the self-consistent floor
(confirmed by their own F4-closing bookkeeping: floor = E/2 + 3±1 nats), with
the Nyquist geometry entering through the integrated budget.

**B←QX (quasicrystal §4 bet 2, conf 0.55; merger sub-bet 0.25).** *"The
slit-plane computation lands K₀ < e²; sub-bet: K₀ = e^{w∞} = 3.594 (horizon
merger); second bet: the 3/2 is derivable in a page from C4's formulation."*
— **I accept ownership of the slit-plane equilibrium computation (QC-3(i));
it is this seat's declared next action (§R2.6).** Prior on K₀ < e²: 0.6 (disk
Jensen is lossy; the two-constants argument in the slit plane sees the head's
charge at larger Green potential — I agree with their mechanism). Prior on
exact merger: LOWERED to ≤ 0.15, from their 0.25, for the reason in
§R2.2(c): C-11 shows the measured "stopping heights" are ACTION-BOOKKEEPING
heights, not vanishing heights (actual registration dies at ≈ 1.9T*), so the
empirical drift 3.14 → 3.41 toward 3.59 is no longer evidence about the
anchored-vanishing horizon at all. The merger survives as a clean separate
conjecture with a decisive computation attached — exactly what it should be.
The 3/2-in-a-page bet: currently BLOCKED by Q7's unresolved edge mechanism
(if fixed-profile wins, the 3/2 is not a free-boundary exponent here and that
bet dies; my calibrated Airy discriminator u½(L=3.4) ≈ 2.29 vs fixed 2.0
stands, and I now expect the fixed side to win — flipped expectation recorded).

### R2.2 Adjudications

**(a) C-2, Layer 0 — the identity web (THEOREM tier; pure calculus, each item
one to three lines, all re-verified this session).** With E = −ln λ, c = e^ℓ,
T_s = e^w T* defined by the action bookkeeping E + A = 2π[D(T*) − D(T_s)]:

1. **Lambert form ≡ this seat's root.** w∞ := root of e^w(w−1) = 1 satisfies
   w∞ = 1 + W(1/e): substitute w = 1 + v, then ve^v = 1/e. Same number,
   1.2784645427…; e^{w∞} = 3.5911214767…. RH seat's form and mine are one.
2. **The equivalence menu.** Given the action identity, the following are
   equivalent statements about a limit: dE/dc → 4π ⟺ (E+A)/T* → 2 ⟺
   Surplus(w) := ∫_{T*}^{e^wT*}(ρ − a/π)dt → 2e^ℓ ("the sweep repays the
   deficit twice") ⟺ w → w∞.
3. **The exact second-epoch identity (new, 7/8-clean):**
   D(eT*) − D(e^{w∞}T*) = e^ℓ exactly (the 7/8's cancel; equivalently
   −D(e^{w∞}T*) = e^ℓ + 7/8). The super-Nyquist excess accumulated between
   the balayage height eT* and the cap height e^{w∞}T* equals the deficit
   mass — the balayage identity's second epoch, in D-form. (RH seat's
   "−D(T_s) = e^ℓ" is this modulo the 7/8.)
4. **The three −1's are one.** My g′(w∞) = −1 (attracting fixed point of
   w′ = (1 − e^w(w−1))/(e^w w)), renormalization's cap eigenvalue −1
   (dg/dℓ = −(g − 4π)), and the Fuchs subleading form p·ℓ are pairwise
   equivalent: each says corrections to the cap decay like e^{−ℓ}, i.e. the
   subleading term in E is O(ℓ). One fact, three notations.

**(b) C-2 — draft co-signed statement (for the five seats named in the
brief).**

> **The w∞ Saturation Theorem (candidate; co-sign slots: free-boundary,
> riemann-hilbert, renormalization, quantum-chaos, quasicrystal).**
> Let λ(L) be the lower frame bound of the smooth RvM staircase on
> [−L/4, L/4], E = −ln λ, c = e^{L/2}.
> (I) [THEOREM — proved, the identity web (a)1–4] The Lambert point
> w∞ = 1 + W(1/e) is the unique positive root of e^w(w−1) = 1; the statements
> "dE/dc → 4π", "(E+A)/T* → 2", "Surplus = 2·Deficit in the limit",
> "D(eT*) − D(T_s) → e^ℓ", and "w(L) → w∞ with unit-rate exponential
> approach ⟺ subleading O(ℓ)" are mutually equivalent given the action
> bookkeeping defining w(L).
> (II) [MEASURED] dE/dc = 4π to 0.4–1.3% by three scalar routes past
> L ≈ 4.32 (deep-windows final); B_abrupt excluded; the vector-channel
> discriminator returned NOT CERTIFIED with its falsifier unfired and its
> premise refuted by the null control (C-11) — the scalar evidence stands
> unopposed and uncertified.
> (III) [CONJECTURE — the co-signed claim] lim_{L→∞} dE/dc = 4π, equivalently
> any (hence every) item of the menu; approach at unit exponential rate.
> Candidate mechanisms on record: budget exhaustion / min-of-two-costs
> (riemann-hilbert pump 1), second-epoch mass balance (free-boundary FB-2),
> RG fixed point with eigenvalue −1 (renormalization §1.3), smooth pasting
> (quantum-chaos B3). These are reparameterizations of one missing
> derivation, not four derivations.
> (IV) [SEPARATED — not part of the theorem] The horizon-merger hypothesis
> (sharp anchored-vanishing horizon = e^{w∞}T*) is a distinct conjecture
> about a different object (feasibility ceiling, not variational standoff);
> see (c). It is neither a corollary nor a hypothesis of (I)–(III).

**(c) C-2 — the horizon-merger adjudication (quasicrystal's H-merger):
SEPARATE CONJECTURE, and its quoted empirical support must be re-based.**
Three reasons. (1) Different objects: T1′/QC-3 bound where ANY anchored
function can vanish on the staircase head; w(L) is defined by action
bookkeeping on the optimizer. (2) C-11's F1 breaks the evidential link: the
optimizer's actual vanishing (registration) terminates at x_dodge ≈ 0.60–0.65,
i.e. ≈ 1.9T* — far below both eT* and T_s. The eleven "stopping heights in
(e, e²)T*" are w_E2 ACTION heights; as vanishing data they say only that
registration ends well inside the variational horizon, which is trivially
consistent with T1′. The observed drift of w_E2 toward 3.59 is bookkeeping
convergence under the cap, not feasibility saturation — so the merger loses
the data support quoted for it (my prior: exact merger ≤ 0.15; K₀ < e²
still likely at 0.6). (3) Under the second-epoch/min-of-costs mechanisms the
optimizer stops strictly inside feasibility (Jensen slack to w = 2 remains at
w∞). **Consequence for T1PRIME/HardHorizon consumers: the "consistency: all
eleven stopping heights inside (e, e²)" clause should be restated as a
statement about action heights, and the genuinely feasibility-flavored
measured number is now the registration endpoint ≈ e^{0.62}T*, safely below
the eT* variational horizon.** The slit-plane computation (§R2.6) decides
K₀ regardless.

**(d) C-11 — folding the vector findings into the obstacle formulation.**
Do they pin the free-boundary condition? **They pin the phase structure, kill
one mechanism, confirm the obstacle, and do NOT pin the cap.** Itemized:

- **Confirmed: the self-consistent floor.** F4's bookkeeping (floor = E/2 +
  3±1 nats at all three L, the per-sample frame scale) is exactly the
  obstacle of FB-2 §1-item-3 — the complementary-slackness level ½ln(λ/2).
  The obstacle formulation's core survives with a measured constant.
- **Refuted: pointwise-Agmon descent and (my) filler mechanism.** F5(i)
  kills envelope-follows-−A(T) at depth; F1/F5(ii) kill the Round-1 pump-1
  clause "epoch 1 = relocate the D(T*) fillers, registration to eT*":
  registration dies at ≈ 1.9T* ≪ eT* and the node budget is NOT saturated.
  Retraction recorded in §R2.4. The exact mass-balance algebra is untouched
  (it never referenced fillers); the two-epoch reading survives only in
  integrated form, with the measured split ≈ 1/5 zero-swept vs 4/5 nodeless
  (F2), not the 1/1 split my pump guessed.
- **The revised FB-2 phase diagram (three zones + floor), which any
  derivation must now reproduce:** sub-T* transition band carrying
  0.30·E (F4); registered/contact zone [T*, e^{x_d}T*], x_d ≈ 0.60–0.65,
  carrying 0.19–0.21·E (F2); nodeless suppression zone carrying the
  remaining ≈ 0.50·E down to the floor. L-universal profile to ±0.02·E
  across the crossover (F3) — the free-boundary structure is
  crossover-blind, which is itself evidence the cap is a saturation of a
  single variational family (supports QC-4's smooth third-order reading).
- **A sharp speculative reading, offered for pre-registration by whoever
  next runs deep vectors (SPECULATION tier, arithmetic exact):** if the cap
  holds and the dodge share converges, then share → [1 − e^{x_d}(1−x_d)]/2.
  The choice x_d = ln 2 (registration endpoint → exactly 2T*) gives share =
  ln 2 − ½ = 0.19315 — dead center of the measured 0.192–0.210. Falsifiable:
  x_dodge at the next deep rungs should drift toward 0.693 and the share
  toward 0.1931; a share settling elsewhere kills the 2T* reading.
- **Q7 update (edge mechanism).** Three instrument-independent
  half-suppression points now sit at u ≈ 2.0 (RUN 4's two + log-gas's f₈
  replication), and C-11 places the registration endpoint at the same
  height: the worth softening is now more plausibly REGISTRATION-LIMITED
  (fixed profile in u) than capacity-edge-Airy. My Round-1 Airy-calibrated
  discriminator u½(L = 3.4) ≈ 2.29 vs fixed-profile 2.0 ± 0.1 stands
  unchanged as the test; my expectation flips to the fixed side. If fixed
  wins: FB-1(i)'s hard-edge-plus-Airy sub-clause dies, the ACTIVE edge of
  the sweep moves to the registration endpoint (~2T*), and [2T*, eT*]
  becomes a passive tail whose exact eT* mass-balance endpoint remains the
  WORTH-support endpoint (RUN 4 stands — value-derivative support and
  registration are different objects, and the data keeps them distinct).

**(e) C-10 — co-signed specification with proof-theory: what a wall-breaking
regularity theorem must contain.** Joint statement, both seats' inputs cited:

> A theorem breaking F5's wall must: (1) [necessity — PT-2(ii),(iii)] use the
> support constraint as an explicit hypothesis (it is invisible to the
> template interface, and proof mining shows any extractable positivity proof
> carries a modulus of some near-minimizer property beyond that interface);
> (2) [form of the modulus — FB-3] NOT be a polynomial-decay modulus: the EL
> operator is log-order (s = 0 endpoint; F5 is sharp there), so no
> CSS/Almgren-type gain exists; the available true statement is a STRUCTURE
> theorem — finite explicit boundary-jet part (atoms with closed-form
> transforms and certifiable couplings) plus a remainder with genuine decay
> R^{−(2k+1)}, with jet magnitudes carried as certified unknowns, not assumed
> small (FB-T1: trace ≈ 0.011 m-stable; derivative trace O(1)–O(5); tail =
> trace tail quantitatively); (3) [extraction route] obtain the jet and
> remainder bounds from the EL equation by half-line Wiener–Hopf
> factorization of the log-symbol (Krein), for exact minimizers first, near-
> minimizers (bounded EL residual) second — the second step is the wall's
> true residue; (4) [terminal form] land as an (m+k)-dimensional certified
> block plus ONE class hypothesis on the k-times-corrected remainder,
> kernel-checkable in the existing CertFramework format — the shape PT-2's
> speed-up analysis says a per-window-feasible statement must have.
> Falsifiers: PT-2's ψ-packet computation (if every interface-consistent
> packet keeps Q^{F0} ≥ 0, the template secretly suffices and (1) collapses);
> FB-T1's next rung (trace drifting > 20% at m = 96/128 kills the jet
> stability the structure theorem needs).

I additionally endorse PT-2(ii)'s countermodel design with a free-boundary
gloss: the packet ψ is "boundary data without a boundary" — tail mass that
imitates no trace. That is precisely what the corner-jet class excludes, which
is why (2) and (1) fit together as specification and necessity.

**(f) Brief notes on C-1, C-5, C-6 (not this seat's to own).**
- **C-1:** the three reductions are, at first order, THE SAME linear
  functional of the discrepancy field δN with kernel (π²/2) d ln t on
  [t₀, eT*]: log-gas's J, quantum-chaos's I_w (same integral, sign
  convention), and magic-functions' β_eff (the functional inverted through
  the pure-phase family — their transport sum S = Σ 1/(t_kN̂′(t_k)) is the
  same kernel in β-coordinates). Equivalent as tested; a separating example
  must live where linearity dies — log-gas measured that boundary at
  sup-deficit ≳ 2 (extreme-value crossover). Suggested joint statement: "one
  kernel, three coordinates; distinct only at second order."
- **C-5 (Q3):** concur with the two death verdicts; from this seat's side, a
  sustained 1.84-nat offset would need an effective-phase excess
  Δβ_eff ≈ 0.1–0.2 (MF's calibration) for which no mechanism exists in the
  constrained-sweep picture. Truncation remains the default; the Gcut
  escalation formally closes it.
- **C-6:** endorse the charge-matched rerun protocol, and adopt log-gas's
  one-sidedness into all transfer statements this seat touches: deficit-side
  hypotheses only. That asymmetry is obstacle-problem complementary
  slackness, and it is a feature of the correct formulation, not a nuisance.

### R2.3 Merges (two)

**Merge A — the w∞ package (free-boundary + riemann-hilbert + renormalization
+ quantum-chaos + quasicrystal; law-theory instrument).** Deliverable: the
co-signed statement of R2.2(b) plus its first proofs. Division of labor:
Layer-0 identity web — DONE (this seat, §R2.2(a)); upper bound at the cap
rate — renormalization R2(i)'s stopped construction, REVISED per C-11 (stop
registration at ≈ 2T*, nodeless corrector carries ≈ 4/5 of the action;
law-theory P4 numerics as the pre-test), with riemann-hilbert's RH-1(a)
normalization bookkeeping; lower bound — riemann-hilbert RH-2(ii) (BKMM
saturation, discrete RHP); optimality system and free-boundary conditions —
this seat (FB-2 three-zone revision; Γ-convergence layer); transition order —
quantum-chaos QC-4 finite differences; horizon side-question — this seat +
quasicrystal via the slit-plane computation (§R2.6). Kill governance: Q1's
existing decision rule, plus the share-drift falsifier of R2.2(d).

**Merge B — the wall-breaking specification (free-boundary + proof-theory +
magic-functions; NT/HA as owners of FULLINF).** Deliverable ladder: (1) the
co-signed specification of R2.2(e) recorded as program law alongside F5;
(2) corner-corrected F4 at L = 7/4 with the k = 1 atom as a certified extra
direction (this seat, weeks; FULLINF's certified-arithmetic vocabulary);
(3) PT-2(ii)'s ψ-countermodel run (NT/HA, pre-registered in PT-2); (4) MF's
interpolation-remainder technology as the candidate optimal-atom family
(their B1: if an RvM-adapted interpolation basis exists, its boundary jets
are the atoms; if the density is wrong for it, that is negative information
the specification absorbs); (5) Lean pricing via PT-3/CS. Success criterion:
a certified class statement at (7/4, m ≈ 96) whose class CONTAINS the
numerical argmins — the exact deficiency FULLINF §8 exposed in F4.

### R2.4 Updates (kills, retractions, strengthenings)

1. **RETRACTED (killed by C-11 F1/F5(ii)):** Round-1 §3 pump 1's mechanism
   clause — "epoch 1 relocates the D(T*) fillers into [T*, eT*]; registration
   ends when fillers exhaust at eT*." Registration measured to die at
   ≈ 1.9T*; node budget not saturated. The exact identities (balayage,
   second-epoch D-form) and the integrated two-epoch reading survive; the
   mechanistic split is measured at ≈ 1/5 zeros / 4/5 smallness (F2), not
   1/1. My Round-1 42/58 "action split" consistency check was bookkeeping on
   the wrong zones; withdrawn.
2. **DOWNGRADED:** FB-1(i)'s hard-edge-Airy sub-clause at eT* (Q7 lean now
   fixed-profile; expectation flipped, discriminator unchanged). FB-1's
   constrained-sweep mass identity and the eT* worth-support endpoint are
   NOT downgraded — they are value-side statements the vector data leaves
   intact.
3. **STRENGTHENED:** FB-2 upgraded to the three-zone + floor phase diagram
   with measured shares (0.30/0.20/0.50, floor at E/2 + 3±1) as its
   adequacy conditions; the fixed point g′(w∞) = −1 now unified with
   renormalization's eigenvalue and the Fuchs form (one fact); Lambert-form
   identity verified (C-2 Layer 0).
4. **PRIOR MOVED:** horizon merger K₀ = e^{w∞}: 0.25 → ≤ 0.15 (evidence
   re-based per R2.2(c)); K₀ < e² stays at ≈ 0.6.
5. **UNCHANGED:** FB-3/FB-T1 in full (Round 2 only strengthened the
   necessity side via PT-2); the FB-T1 next-rung gate (m = 96/128 trace
   stability) stands.

### R2.5 Pre-registered micro-test FB-T2 — the defect-potential sum
(the FB-1(ii)/log-gas-multiplier bridge, written BEFORE the run)

**Question.** Is the measured marginal worth a bare potential gap of the
constrained sweep? Conjecture FB-1(ii) in finite form: f(t₀) ≈ 2G(t₀), where
G(t₀) = Σ_{staircase t_k ≤ H, k≠0} ln|1 − t₀²/t_k²| −
Σ_{budget lattice t′_j ≤ H} ln|1 − t₀²/t′_j²|, budget lattice = density a/π at
phase ½ (t′_j = (j−½)π/a), evaluated at two truncations H: the balayage
endpoint eT* (primary, per FB-1) and the registration endpoint e^{0.62}T*
(secondary, per C-11 — a bonus discriminator between balayage-edge and
registration-edge potentials). Configurations: L = 2.485 (13 staircase points
≤ eT*, 12 budget points — the 7/8 mismatch is real and kept) and L = 2.996.
Comparators: RUN 4's measured worths (law-theory report §3.4) at the shared
heights; pure-log (π²/2)ln(eT*/t₀) elsewhere. No eigensolves; pure sums;
< 1 CPU-min.

**Pre-registered gates (before any sum is computed):**
- **G1 (scale+shape, primary, at H = eT*):** for the bulk points (u = t₀/T*
  ≤ 1.6; five per L): ratio R(t₀) = 2G(t₀)/f_meas ∈ [0.4, 2.5] for ≥ 7 of
  the 10, AND the OLS slope of 2G against ln(eT*/t₀) within 35% of
  π²/2 = 4.935.
- **G2 (edge direction):** at the softened points (u ≈ 2.0), 2G under-shoots
  the pure log (the model must reproduce the measured suppression direction,
  ratio-to-log < 0.8).
- **G3 (truncation discriminator, reported not gated):** whether H = eT* or
  H = e^{0.62}T* gives the better G1 slope — evidence for balayage-edge vs
  registration-edge potential.
- **Kill consequence:** G1 failing kills the bare-potential-gap reading of
  the marginal law (FB-1(ii) as stated; log-gas's multiplier bet pays out
  NO), and the worth must be priced through the λ₋-normalized secular
  identity only (T4's route unchanged — this test cannot harm T4, only my
  shortcut to it).

**Results (appended after the run, unedited above this line):** see
`results/ias/free-boundary/fbt2_output.txt` — scored in §R2.5.1 below.

**R2.5.1 FB-T2 outcome: the bare-potential-gap model is DEAD (gates fired as
designed).** Script `fbt2_defect_potential.py`, output `fbt2_output.txt`,
< 1 s. **G1: FAIL, 0/9 bulk points in band** — 2G is large and NEGATIVE at
every height (e.g. −10.6 vs measured +5.28 at t₀ = 20.7, L = 2.485), and the
bulk slope of 2G against ln(eT*/t₀) is 14.7 / 19.7 at the two L against
π²/2 = 4.93 (ratios 2.98 / 4.00). **G2: FAIL** (wrong sign throughout, not
merely soft at the edge). **G3:** the registration-edge truncation is mildly
less wrong (slope ratios 2.11 / 3.44 vs 2.98 / 4.00) — recorded, decides
nothing given G1. Post-hoc observation, K5-quarantined: the slope ratios sit
suspiciously near the integers 3 and 4; no weight attached.

**Consequence (the honest lesson, worth the run).** The marginal worth is NOT
a frozen-configuration potential gap: freezing the deleted staircase and
comparing to a fixed-phase budget lattice misses the RE-OPTIMIZATION of the
minimizer, which is O(potential) itself — consistent with log-gas's LG-4
revision (deletion dilates the whole sweep: a global free-boundary response,
not a local one). FB-1(ii) is hereby REVISED: the worth must be read as an
envelope-theorem (Danskin) derivative of the VALUE along the deletion family
— which is exactly T4's rank-two secular route, and exactly why
magic-functions' transport check succeeded (differentiating the value along a
parameter is valid with the frozen minimizer; my bare product is the
minimizer of nothing). Log-gas's multiplier bet pays NO in its bare form; the
multiplier reading survives only evaluated on the re-optimized sweep. My
shortcut to π²/2 is closed; T4's route is untouched, and this seat's
equilibrium contribution to it must go through the constrained-equilibrium
g-function (Merge A's lower-bound lane), not through frozen sums.

### R2.6 Next action (single, sized)

**The slit-plane anchored-horizon computation (QC-3(i), joint deliverable
with the quasicrystal seat): days-scale.** Compute the sharp anchored-
vanishing horizon constant K₀ by replacing T1′'s disk Jensen with the Green
potential/two-constants argument in Ω = ℂ ∖ {x ∈ ℝ : |x| ≥ T̃} (Joukowski
map; head charge = the staircase counting function; the balayage identity as
the first-moment calibration). Payoffs: decides the horizon-merger conjecture
either way (K₀ = e^{w∞} vs K₀ ∈ (3.6, e²] vs disk-not-lossy); tightens the
kernel-checked HardHorizon constant if K₀ < e² (a light Lean edit per
quasicrystal QC-2's precedent); completes clause (IV) of the co-signed C-2
statement; and it is the one Round-2 item on this seat's list that no other
seat can do faster. Sized: 2–4 days paper-grade, one page of potential
theory plus bookkeeping; no compute beyond spot-checks.

### R2.7 Incorporations — the renormalization, riemann-hilbert, and
proof-theory R2 sections (landed after §§R2.1–R2.6 were written)

**(a) C-2 consolidated — the statement of record, superseding §R2.2(b).**
Three independent drafts now exist (mine R2.2(b); renormalization R2.2
(i)–(iv); riemann-hilbert R2.2 (I)–(II)) and they are compatible clause by
clause. As owner of the exact chain I consolidate: **the co-signed statement
is riemann-hilbert's R2.2 draft** — whose (I)(a),(b) is my Layer-0 identity
web plus renormalization's chart equivalence, whose (II) carries one
mechanism clause per seat, and whose separation rider on the horizon merger
matches my R2.2(c) — **augmented by their (I)(c) chart dictionary, which I
adopt as a new Layer-0 clause:** w(ℓ) = w∞ − [p·ℓ + (A′ − A)]e^{−ℓ}/
(2π(1 + e^{w∞})) + O(ℓ²e^{−2ℓ}), verified against all five converged w_E2
values to ≤ 0.001 (a consistency identity across charts, not independent
confirmation — their own correct flag). Two corrections to my §R2.2 are
accepted from their sections:
1. **g′(w∞) = −1 is structural, not evidence** (riemann-hilbert): at ANY
   root of e^w(w−1) = 1 the flow has g′ = −N′/D = −1 identically. My
   "attracting fixed point" observation and renormalization's eigenvalue
   are the same ALGEBRAIC fact; the falsifiable content is entirely in the
   subleading form being O(ℓ) (equivalently the flatness of A′(p) across
   windows, which riemann-hilbert measured). §R2.2(a)4 is amended
   accordingly — "one fact, three notations" stands, with its tier
   corrected from observation to identity.
2. **The approach is resonant** (both seats): w∞ − w ≍ ℓe^{−ℓ}, not pure
   e^{−ℓ} — the p·ℓ forcing makes the w-flow non-autonomous at exactly the
   order the ODE is written. Clause (III) of my R2.2(b) draft ("unit-rate
   exponential approach") is amended to "unit-rate resonant approach
   O(ℓe^{−ℓ})". Renormalization's regime map is adopted with it: the drift
   branch reaches w∞ only at ℓ* ≈ 3.28 (L ≈ 6.6), so every existing deep
   window is mid-crossover, and the pre-registered qualitative expectation
   (approach from below, no overshoot, residuals vs drift growing more
   negative through L ≈ 5.5–6) is co-signed.
Horizon-merger priors now on record across seats: FB ≤ 0.15 (re-based per
R2.2(c)), riemann-hilbert 0.4, renormalization abstains. The spread is
honest disagreement about whether a variational standoff can coincide with
a feasibility ceiling; my R2.6 slit-plane computation remains the decider
and both seats endorse it as designed.

**(b) C-10 counter-signature.** I **countersign the proof-theory seat's
five-clause Wall-Breaking Specification verbatim** (their R2.2, C-10 — it
subsumes my four-clause version of §R2.2(e), with clause 4 answering the
modulus-extraction question YES for the corner-jet route). The binding
demands of their clause 4 are accepted into FB-3's execution plan: the
Wiener–Hopf jet bounds of FB-3(ii)/(iii) will be stated and proved in Π₂
moduli form — an explicit majorant C_k(ρ, L), uniform in the EL-residual
bound ρ (they will be consumed at Galerkin argmins, never at exact
minimizers) — with no compactness or unquantified Fredholm step. Their
clause-5 arithmetic (at (7/4, 192) the k = 3 corner class allows tail mass
≈ 3×10⁻¹⁹·C₃ in the gap band where the PT-2 countermodel needs ε ≈ 5×10⁻⁸:
the atoms re-inject the support constraint at the boundary, which is where
it lives) is adopted as FB-3's design target, and NA's countermodel re-run
inside the corner-corrected interface is the joint falsifier. Noted with
thanks: their repricing of my Round-1 bet 5 (0.3 → 0.7 conditional on the
jet bound landing extraction-friendly), and their formalization-distance
ordering (corner atoms = k extra CertFramework rows, months; prolate = a
spectral-theory development, far longer) — which is F6's economics restated
in person-days and raises FB-3(ii)'s priority within Merge B′ (their M-
merges) accordingly.

**(c) FB-5 (NEW; THEOREM, calculus tier) — the κ-capacity corollary,
delivered as requested (renormalization R2.2: "one-page corollary of
FB-1"). It is five lines.** Let ρ_κ(t) = (a/π)(t/T*)^κ, κ > 0, be the
power-graded density (RvM is the κ → 0 limit in u-coordinates), and define
the capacity endpoint A_κ by the FB-1 mass condition: super-Nyquist surplus
on [T*, A_κ] = sub-Nyquist deficit on [0, T*]. Then, with x = A_κ/T*:
  deficit = (a/π)∫₀^{T*}[1 − (t/T*)^κ]dt = (a/π)T*·κ/(κ+1);
  surplus = (a/π)T*·[(x^{κ+1} − 1)/(κ+1) − (x − 1)];
  balance ⟺ x^{κ+1} − 1 − (κ+1)(x−1) = κ ⟺ x^{κ+1} = (κ+1)x
  ⟺ **x^κ = 1 + κ, i.e. A_κ = (1+κ)^{1/κ}·T*.** ∎
Checks: κ → 0 gives A → e·T* (the balayage identity, recovered); κ = 1
gives A = 2T* (the Weyl/Selberg grading); matches renormalization's R3(i)
8-digit numerics. Edge structure riders for the equilibrium proof: the
left junction stays soft for every κ (constraint density vanishes at T*
with u-slope ∝ κ — the RvM case is the marginal, slowest-vanishing member),
the right endpoint stays mass-determined (hard) for all κ. The full FB-1
generalization (existence/uniqueness/saturation of the constrained sweep at
general κ, Dragnev–Saff route) is accepted as this seat's deliverable (i)
of renormalization's Merge A — weeks, and the κ-family gives T4 its
solvable first case at κ = 1 exactly as they argue. K5 note: the numerical
coincidence of A₁ = 2T* with the κ→0 registration-endpoint speculation of
§R2.2(d) (x_d → ln 2) is flagged and NOT identified — different objects
until a derivation says otherwise.

**(d) Merge-B road (1): already adjudicated NO-GO by FB-T2.**
Riemann-hilbert's Merge B ordered "FB's G(t₀) finite sum runs FIRST as the
go/no-go"; §R2.5.1 ran it before their section landed: the bare
potential-gap sum misses by SIGN and by O(1)+ in magnitude at every tested
height. Road (1) is closed; roads (2)–(3) (rank-two secular identity +
one-node Schlesinger/parametrix) now carry T4 alone, and their promised
π²-vs-π²/2 parity/pair audit is unaffected (it lives on the secular road).
Renormalization's Merge-B clause listing "worth = potential-gap identity
G(t₀) — free-boundary" must be struck or restated in Danskin form: the
worth is the envelope derivative of the VALUE along the deletion family,
priced on the re-optimized sweep — which is also why the three
transport-side validations (block-spin, CUE regression, β-dial) all
succeeded while the frozen-configuration sum failed. Their κ = 1
marginal-worth scan (renorm R2.5) is untouched and remains the right
external calibration of the LAW; I co-sign its pre-registration as written.

**(e) Renormalization's C-4 Deficit Mechanism box: co-signed as written**,
with the FB-T2 rider above attached to clause (3) (the kernel is a Gateaux
derivative of Φ along optimized families — the box already says exactly
this, and FB-T2 is the measurement showing the frozen-sum shortcut is not
an admissible reading of it). Their C-11 reconciliation offer
(riemann-hilbert R2.2 C-11 item 2: charge-side vs potential-side accounting
differ by an exact integration by parts of the g-function against the
deficit measure) is accepted as a joint one-page lemma with DG — it is the
formal version of my §R2.2(d) three-zone restatement, and it would convert
the measured 30/20/50 shares from phenomenology into equilibrium data.
Next action (§R2.6) unchanged.
