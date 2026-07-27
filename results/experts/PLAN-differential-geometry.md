# PLAN — Differential geometry / spectral geometry consultant

Independent candidate lemmas for the Positivity Gate program, from the viewpoint of
inverse spectral theory (Krein strings, de Branges canonical systems), WKB/Agmon
semiclassics, and trace-formula geometry. Prepared without reading the other experts'
PLAN files. All repo numbers quoted below are from `results/RESULTS.md` /
`PROGRAM.md` §2.14–2.18 / `ENVELOPE.md`; all new numbers are from two light
computations run for this plan (recipes in §2, scripts in the session scratchpad,
~2 minutes total; reproducible from the recipes verbatim).

Notation, fixed throughout: a = L/4, ℓ = L/2, T*(L) = 2π e^{ℓ} (Nyquist height),
ρ(T) = (1/2π) ln(T/2π) (smooth zero density), N(T) = (T/2π) ln(T/2πe) + 7/8
(smooth Riemann–von Mangoldt counting function), and λ(L) = the operator-level
margin = lower frame bound of the exponential system at the zero ordinates on an
interval of length 2a = ℓ (PROGRAM §2.14(v)). Measured law (RESULTS):
ln λ(L) ≈ 10.2 − 1.755 e^{ℓ}(ℓ + 4).

---

## 1. Reformulation.

The object λ(L) is, verbatim, a truncated inverse-spectral quantity: the smallest
eigenvalue of the sampling Gram operator of the Paley–Wiener space PW_a (transforms
of L²[−a, a]) on the measure μ = Σ_γ δ_γ. Three classical geometrizations apply, and
the repo's own measurements select among them.

**(i) The phase-space picture (the one the data has already confirmed).** Plot the
density curve u = ln(T/2π) against the Nyquist level u = ℓ in the (T, u) half-plane.
They cross at T* = 2πe^{ℓ}. Below T* the ordinates are sparser than the Nyquist
density of PW_a; above T* they are denser. Define the **excess-area action**

  A(T; L) = ∫_{T*}^{T} (πρ(t) − a) dt = ½ [ T(ln(T/T*) − 1) + T* ],  T ≥ T*,

the phase-space area trapped between the density curve and the Nyquist line — an
Agmon distance for the frame operator's symbol. The measured envelope exponent is
*exactly* twice this area evaluated at a stopping height T_s ≈ 3.2 T*:

  2A(e^{w}T*; L) = (T*/2π)·2π[e^{w}(w−1) + 1],  and  e^{w}(w−1) = (1.755/2π)(ℓ+4) − 1
  gives w ∈ [1.11, 1.22] (T_s/T* ∈ [3.03, 3.39]) across the entire measured range
  ℓ ∈ [0.875, 2.25], reproducing 1.755·e^{ℓ}(ℓ+4) identically.

So the three-constant law is equivalent to: **λ ≈ exp(−2 × excess area up to a
stopping height glued at ≈ 3.2 T***). Two structural heights bracket this stopping
point rigorously (§2, DG-2): the *count-saturation height* e·T* ≈ 2.72 T*, where the
number of imposed nodes N(T) first exhausts the real-node budget aT/π of exponential
type a (they are equal precisely at u = ℓ+1), and the *Jensen-saturation height*
e²·T*, where the log-weighted zero budget 2∫₀^R N(t)/t dt = 2aR/π of a normalized
type-a function is exhausted (equality precisely at u = ℓ+2). The measured T_s sits
between them. The stress test run for this plan (§2, DG-2(e)) confirms the two
predicted signatures directly on the minimizer: its transform descends along −A(T)
above T* (measured −4.56 vs predicted −4.20 at 2T*, L = 2.485), and its real-node
count saturates the type budget aT/π, not the zero count.

**(ii) The canonical-system picture (Krein–de Branges).** By the inverse spectral
theorem for canonical systems (de Branges 1968; modern treatments: Remling,
*Spectral Theory of Canonical Systems*, de Gruyter 2018, Ch. 5; Romanov,
arXiv:1408.6022, §§4–6), every positive measure μ with ∫ dμ/(1+T²) < ∞ — which
Σδ_γ satisfies, since ρ grows only logarithmically — is the spectral measure of an
essentially unique trace-normed canonical system Ju′ = −zHu, H(t) ≥ 0, and the
associated de Branges chain {B(E_τ)} is an increasing family of spaces of entire
functions of exponential type τ. Truncation at support L is truncation of the chain
at type τ = a = L/4. λ(L) is the bottom of the spectrum of the chain member's
sampling form; the envelope law is a statement about the Hamiltonian's asymptotics;
the family universality in T*_χ = (2π/q)e^{ℓ} says the family Hamiltonians are
**time-translates of one universal germ** (type shift τ → τ + (ln q)/2 moves
ℓ → ℓ − ln q exactly); and the Glide Theorem (THEOREMS.md, Theorem 1) is the frame
avatar of **chain regularity**: the chain depends only on μ, so prime-power
thresholds — which live on the dual (prime) side of the explicit formula — cannot be
events in it. This is the precise inverse-spectral home of the repo's slogan "the
law is a functional of the counting function at maximal rigidity."

**(iii) The flow picture (Berry–Keating / Connes / Deninger).** The variable
u = ln(T/2π), which linearizes everything above, is the time of the xp / scaling
flow: N(T) = (T/2π) ln(T/2πe) + 7/8 is precisely the regularized phase-space count
of H = xp (Berry–Keating, SIAM Rev. 41 (1999), including the 7/8), the Weyl term of
Connes' trace formula on the adèle class space (Selecta Math. 5 (1999)), and the
counting function of Deninger's conjectural foliated dynamical system (Doc. Math.
ICM 1998). Because the repo has *measured* that the margins are a functional of
N(T) plus a rigidity-class offset (RESULTS, model_zeros: smooth staircase matches
true zeros; Poisson costs 1.5–2 orders ≈ 4.5 nats), the envelope constrains any
candidate geometry through exactly two slots: its Weyl datum (must be N(T)) and its
rigidity class (must be maximally rigid). This is Track E's constraint table made
precise, and it cuts both ways: the envelope *cannot* distinguish two geometries
that share those two data (see §5).

The lemmas below make (i)–(iii) into provable statements with numerical gates.

---

## 2. Lemma candidates

### Lemma DG-1 (the staircase canonical system: existence, normal form, and reduction of the envelope to Hamiltonian asymptotics)

**(a) Statement.** Let μ_sm be the symmetric point measure at the smooth-staircase
quantiles ±t_k, N(t_k) = k − ½ (t_1 ≈ 14.6, cf. γ_1 = 14.13). Then:

1. There is a unique trace-normed canonical system H_sm(t) on [0, ∞) with spectral
   measure μ_sm, and the frame quantity λ_sm(L) equals the smallest eigenvalue of
   the sampling form of the de Branges chain member of exponential type τ = L/4.
2. (Normal form.) H_sm is, after rotation, asymptotically diagonal with
   exponentially degenerating eigenvalue ratio: in trace-normalized coordinates
   h₁(t)/h₂(t) = e^{−2w(t)} with w(t) = 4t + O(log t)-type growth fixed by the
   Abelian/Tauberian correspondence between spectral-measure asymptotics and
   endpoint asymptotics (Kasahara 1975, Japan J. Math. 1; Kotani–Watanabe, LNM 923
   (1982); the string form applies to the even subspace with σ(λ) = 2N(√λ) ≍
   λ^{1/2} ln λ, regular variation of index ½ — interior to Kasahara's range, the
   log entering as the slowly varying factor). Equivalently: the resolution height
   of the chain at type τ is T*(τ) = 2πe^{2τ}(1 + o(1)) — the Nyquist law, now as a
   theorem about H_sm rather than a definition.
3. (Reduction.) −ln λ_sm(L) equals, to leading order, twice the Agmon action of the
   two-component system H_sm between the turning point t(T*) and the stopping point
   of DG-2 — so the envelope constants (b, +4) are functionals of the normal form
   in 2 alone, i.e. of N(T) alone. This is the theoretical counterpart of the
   repo's measured density-not-arithmetic verdict.

**(b) Proof strategy.** Step 1 is bookkeeping on top of the inverse theorem
(Remling Ch. 5; Romanov §6): verify the Poisson-integrability of μ_sm, identify the
chain's type-τ member with PW_τ with mutually bounded norms via the density theorem
of the chain (the measure is a zero-free perturbation of a sine-type zero set below
any fixed height). Step 2: even/odd decomposition onto two Krein strings; apply
Kasahara duality to σ(λ) = 2N(√λ); translate string mass asymptotics back to H via
the standard string↔canonical-system dictionary (Remling Ch. 7); the 7/8 and the −1
in N enter as second-order endpoint data. Step 3: write λ_sm(L) as the smallest
eigenvalue of a two-point boundary problem for the transfer matrix of H_sm on
[τ, ∞), then Liouville–Green/WKB for canonical systems (the turning point is where
the rotation rate of the Weyl disk at height T crosses the truncation type — the
T*(τ) law of 2); the exponent is the integral of the off-diagonal decay rate, which
is exactly the excess area of §1(i) after the change of variables u = ln(T/2π).

**(c) Hardest missing step.** Two: (α) Kasahara-type Tauberian theorems give the
*leading* regular variation of the Hamiltonian, but the envelope's subleading (ℓ+4)
and the offset 10.2 require the *second-order* term of the normal form — Abelian
directions are fine, the Tauberian converse at second order is not off-the-shelf;
(β) the rigorous WKB error control for canonical systems near a logarithmically
slow turning point (the standard Liouville–Green error integrals are borderline
because the two Hamiltonian eigenvalues degenerate only exponentially in t, not
polynomially).

**(d) Difficulty.** Parts 1–2 at leading order: months (a competent
canonical-systems analyst; the tools exist). Part 3 with constants: the same
research program as DG-2 — they land or fail together. Nothing here needs RH: μ_sm
is explicit. The transfer to ζ's actual zeros is DG-3's job, and the frame reading
of λ(L) itself is conditional on RH (unconditionally, Q_L is the explicit-formula
form; this caveat is inherited from PROGRAM §2.14(v) and stated once here for all
lemmas).

**(e) Numerical stress test (repo could run first).** Layer-stripping
reconstruction: discretize μ_sm below Γ_cut = 500, run the standard
Gelfand–Levitan/Krein-accelerant recursion to reconstruct H_sm(t) on t ∈ [0, 1.2]
(range covering L up to 4.8), and test prediction 2 directly: the reconstructed
h₁/h₂ ratio should fall on ln(h₁/h₂) ≈ −8t + C, and the eigenvalue counting of the
truncated system at type τ should reach height 2πe^{2τ}. Then shoot the transfer
matrix to get λ from H_sm and compare against the measured table (3.13e−5 /
3.50e−10 / 4.2e−15 at L = 1.75 / 2.485 / 2.996). Cost: hours of implementation,
minutes of compute; it consumes only numpy. First-stage sanity for this plan was
run in the scratchpad: a direct Galerkin solve of the μ_sm frame problem (Legendre
m = 48, cutoff 12 T*) gives λ_sm(2.485) = 2.04e−10, consistent with the repo's
model_zeros value 2.75e−10 at Γ_cut = 420 given the different truncations — the
model and instrument agree before any Hamiltonian is built.

### Lemma DG-2 (WKB/Agmon envelope for the smooth model: the exponent is the excess phase-space area up to a stopping height)

**(a) Statement.** For the smooth model of DG-1, with A(T; L) the excess area of
§1(i) and F = φ̂ the transform of the unit-norm minimizer:

1. (Envelope.) On T* ≤ T ≤ T_s, the local maxima of |F| obey
   ln |F(T)| = ln |F(T*)| − A(T; L) + O(transition layers), with an Airy-type layer
   at T* and a floor at the per-sample scale ~ ½ ln λ; the descent stops at
   T_s ∈ [c₁T*, c₂T*] with 2 ≤ c₁ ≤ c₂ ≤ e² universal.
2. (Node budget.) The number of real zeros of F in [0, T] saturates the type
   budget: #nodes(T) = aT/π + O(log) for T ≤ T_s — in particular below T* the
   minimizer carries ≈ aT*/π − N(T*) non-ordinate nodes (its surplus degrees of
   freedom), and it dodges ordinates only while aT/π ≥ N(T), i.e. up to at most
   e·T*.
3. (Two-sided exponent bracket, rigorous target.)
   2π e^{ℓ}(1 − o(1)) ≤ −ln λ_sm(L) ≤ 2π(e²+1) e^{ℓ}(1 + o(1)) = 52.7 e^{ℓ}(1+o(1)),
   the lower bound from the count-saturation construction (dodge all quantiles to
   eT*; achieved value ≤ e^{−2A(eT*)} = e^{−T*}), the upper from the Jensen budget:
   a normalized type-a function cannot vanish on the quantiles beyond e²T* because
   2∫₀^R N(t)/t dt = (R/π)(ln(R/2π) − 2) exceeds 2aR/π once ln(R/2π) > ℓ + 2.
   The measured exponent 1.755(ℓ+4)e^{ℓ} ∈ [8.6, 11.0]·e^{ℓ} sits inside this
   bracket throughout the measured range.
4. (Sharp constant, conjectural.) −ln λ_sm(L) = 𝒥(ℓ)(1 + o(1)) where 𝒥 is the
   value of the explicit obstacle problem: minimize ∫ e^{−2σ(T)} dμ_sm over
   admissible envelopes σ ≥ 0 (σ admissible iff e^{−σ} majorizes some unit-norm
   type-a transform: a Beurling–Malliavin-type cone), subject to
   (1/2π)∫ e^{−2σ} dT = 1. The claim to prove or refute: 𝒥(ℓ) = b·e^{ℓ}(ℓ + c) +
   O(ℓ) with b, c absolute — and the derived (b, c) must reproduce the measured
   (1.755, 4.0) within fit uncertainty (b is only measured to ~1%: 7/4 = 1.750,
   √π = 1.772, ln 6 = 1.792 are all live; the derivation must *output* the
   constant, cf. §5).

**(b) Proof strategy.** For 1–2: Euler–Lagrange equation of the frame quotient +
Poisson-type resummation of the frame kernel over the staircase: the j-th harmonic
∫ρ(T)e^{iTu}cos(2πjN(T))dT has its stationary phase on the resolution curve
u = j·ln(T/2π), with Legendre-transform action −2πj e^{u/j}; the j = 1 branch is
the WKB characteristic and gives the envelope; node saturation follows from
Jensen's formula applied to the near-minimizer (its L² normalization pins the
circle-mean of ln|F|). For 3, lower: a Levin sine-type construction (Levin,
*Lectures on Entire Functions*, AMS 1996) with prescribed zero set = quantiles
below eT* continued at critical density above; the discrepancy of that set against
its Nyquist comparison is O(N-fluctuation-free), so sine-type existence is in
Levin's class. For 3, upper: Jensen/Carleman budget as stated — elementary. For 4:
this is a Widom-type extremal problem (Widom, Trans. AMS 88 (1958) and 100 (1961),
extreme eigenvalues of translation kernels; Landau–Widom, JMAA 77 (1980)); the
modern route is potential theory on the admissible cone via the Beurling–Malliavin
multiplier theorem (Mashreghi–Nazarov–Havin, St. Petersburg Math. J. 17 (2006);
Poltoratski's Toeplitz approach), plus the recent quantitative PSWF eigenvalue
bounds (Bonami–Jaming–Karoui; Karnik–Zhu–Romberg–Davenport) for the sharp-band
comparison. A discriminating negative result is already available: the sharp-band
prolate model (replace the graded density by a hard band at T*) yields exponent
~ 2π² e^{ℓ}/ln ℓ — smaller than measured by a factor ≍ ℓ ln ℓ — so *the graded
log-density is essential*; no sharp-band/prolate-only derivation can produce the
law, which sharpens what "Sonin-space asymptotics" must mean in ENVELOPE.md's
closing question.

**(c) Hardest missing step.** The tightness of the admissible cone in 4:
Beurling–Malliavin multipliers lose ε of exponential type, and here an ε type-loss
costs e^{εe^{ℓ}} in the eigenvalue — the multiplier construction must be run with
type loss o(e^{−ℓ}), far beyond the standard statements. This is the precise
technical wall; everything else in 1–3 is classical-methods engineering.

**(d) Difficulty.** 1–2: months (the stress test below already verifies both
numerically). 3: months, publishable alone as the first rigorous two-sided
exponent for the staircase frame problem. 4: likely-open at sharp-constant level;
research program. Note the internal tension worth resolving on paper first: if the
measured (ℓ+4) growth persists as ℓ → ∞ it crosses the Jensen ceiling 52.7e^{ℓ} at
ℓ ≈ 26 (L ≈ 52, λ ~ 10^{−10¹²}) — so *either* the law bends far beyond any
measurable range, *or* the optimal strategy asymptotically abandons zero-dodging
for smallness-without-vanishing (harmonic-measure cost, not Jensen cost). Settling
which — a pure entire-functions question — is the cheapest deep test of the whole
framework, and is invisible to numerics (§5).

**(e) Numerical stress test — RUN for this plan; results.** Galerkin solve of the
μ_sm frame problem, then evaluate the minimizer's |F| on a grid and extract local
maxima. (Recipe: orthonormal Legendre basis on [−a,a], m = 40–48; quantiles to
12 T*; frame matrix 2Σ_k Re v_k v_k^†, eigh; ~40 lines of numpy, ~1 min.)
Measured, L = 2.485 (T* = 21.77): envelope drop ln|F(T)/F(T*)| at
T/T* = 1.5 / 1.75 / 2.0: −2.95 / −3.76 / −4.56 against predicted −A(T) =
−1.18 / −2.50 / −4.20 — 8% agreement at 2T* after the near-edge Airy layer
(measured steeper than WKB close to T*, as expected); descent then floors at
−5.0 ± 0.3 (per-sample floor; ½ln λ − ref = −3.3) with stopping in [2.0, 2.3]T*
at this depth, consistent with c₁ = 2, and the total λ matching 2A at 3.16T* —
the floor zone between 2.3T* and 3.2T* contributes the remainder. Node census:
13 nodes below 3.2T* against type budget aT_s/π = 13.8 and zero count
N_sm(3.2T*) = 16.5 — the budget, not the zero count, is saturated (same at
L = 1.75: 6 vs 6.7 vs 8.8). Both signatures of statement 1–2 pass. The repo's
sharper follow-up: repeat on the *true-zeros* minimizer in the hp/spectral
pipeline at L = 2.996 (predictions: drop −5.4 ± 0.8 at 2T* = 56.2; stopping in
[2, 2.7]·28.1; node census below T* ≈ aT*/π = 6.7 with only ~3 at ordinates), and
the keyhole vector at L = 3.2, m = 61: predicted total nodes below T* = 31.1 is
aT*/π ≈ 8, of which 4 at ordinates — i.e. 1–2 more non-ordinate nodes than the
two already disclosed (7.640, 13.655) should exist below 31.1.

### Lemma DG-3 (the exponent is Lipschitz in the counting function: rigidity enters only the offset)

**(a) Statement.** Let μ₁, μ₂ be symmetric locally finite point measures whose
counting functions satisfy sup_{T ≤ e²T*(L)} |N₁(T) − N₂(T)| ≤ D, both with
log-type density near N(T). Then

  | ln λ[μ₁](L) − ln λ[μ₂](L) | ≤ C(ℓ) · (D + 1),  with C(ℓ) ≤ C₀ · ℓ,

C₀ absolute. Consequences: (i) with μ₁ = ζ-zeros, μ₂ = μ_sm and D = sup|S(T)|
(argument of ζ; |S(T)| ≤ 0.112 log T + 0.278 log log T + 2.51 unconditionally,
Trudgian, J. Number Theory 134 (2014); numerically |S| < 1 through every height
these windows see), the envelope law transfers between the smooth model and ζ with
at most O(ℓ)-size offset changes — which is exactly what the repo measured (true
vs smooth: |Δln λ| = 0.02 at L = 2.485, 0.16 at 2.996, +1.84 at 3.555, RESULTS
model_zeros table); (ii) Poisson ordinates have D growing like the local maximum
of a random walk, ≍ √(N ln ln N), which correctly predicts a super-constant but
sub-exponent cost — measured −4.53 nats at L = 2.485, −4.51 at 2.996.

**(b) Proof strategy.** Transplantation by finite Blaschke-free products: a
near-minimizer F for μ₂ vanishes at the low μ₂-points; multiply by
m(z) = Π_{k≤K} (1 − z²/t_{1,k}²)/(1 − z²/t_{2,k}²) (poles cancelled by those
zeros), an entire factor of exponential type 0, so support/type is unchanged. The
sup-norm of log|m| on ℝ for two interlacing-with-discrepancy-D sequences is
controlled by Levin's perturbed-sine-function estimates (Levin 1996; Avdonin's
"1/4 in the mean" circle): sup log|m| ≤ C·D·ln(local point count) ≤ C·D·ℓ — this
is where C(ℓ) ≍ ℓ enters. Then compare frame sums termwise. The converse direction
is symmetric.

**(c) Hardest missing step.** The frame value is exponentially small while the
transplantation estimate is a sup-norm bound: one must run the comparison at the
level of ln λ (multiplicative), not λ (additive), which requires the μ₁-frame sum
of the transplanted function to be dominated *pointwise at the sample points* —
fine for the dodged low points (both vanish), delicate in the floor zone where the
two sequences' points interleave with the minimizer's ridge structure. A wrong-way
factor e^{C·D·ℓ} is acceptable (it is the claimed bound); losing a factor
polynomial in the point count K ~ e^{ℓ}ℓ is not. This step is honest work but not
deep; the statement is the most provable of the four.

**(d) Difficulty.** Months, self-contained, and the highest value-per-effort in
this plan: it converts the repo's measured "density, not arithmetic" verdict into
a theorem, it is the formal bridge (with DG-2) from the smooth model to ζ, and its
finite-dimensional core (Lipschitz dependence of ln λ_min on sample positions for
a fixed Galerkin section) is certifiable by the repo's existing interval machinery
(rank-2 updates), i.e. Lean-adjacent.

**(e) Numerical stress test — RUN for this plan; results.** Jittered staircases at
L = 2.485, m = 48: iid Gaussian jitter of the quantiles with σ = α × local
spacing, three seeds each. Measured |Δ ln λ| against sup|ΔN| = D:
α = 0.1 (D ≈ 0.23–0.31): 0.22–0.41; α = 0.3 (D ≈ 0.77–1.13): 0.01–1.73;
α = 1.0 (D ≈ 2.6–3.1): 1.27–3.36. Empirical Lipschitz constant 1.0–2.3 at
ℓ = 1.24 — the claimed bound (C₀ℓ per unit D, let alone 4π) has an order of
magnitude of slack, and jitter can *raise* λ (+3.36 at one seed), as the
interleaving mechanism predicts. Repo follow-ups that would sharpen the lemma:
(i) repeat at L = 2.996 to test C(ℓ) ∝ ℓ (predict the D ≈ 1 response grows by
~ℓ₂/ℓ₁ = 1.21); (ii) the GUE point of prediction P3 below — the one rigidity
class between smooth and Poisson, currently unmeasured.

### Lemma DG-4 (the glide is chain regularity; the derivative envelope law)

**(a) Statement.** (1) The map τ ↦ B(E_τ) of the de Branges chain of μ is
continuous (no jump intervals) at every type, because jump intervals of a chain
are determined by the spectral measure alone and μ has none at the relevant types;
prime-power thresholds L = 2 log n are points of the *prime side* of the explicit
formula, not of μ — so Theorem 1's glide is the frame shadow of chain regularity
(de Branges' ordering theorem for chains; Remling Ch. 6, Romanov §5). (2)
Quantitative upgrade: λ is differentiable in L away from a null set with

  d ln λ / dL = −(b/2) e^{ℓ}(ℓ + 5) (1 + o(1)),  b ≈ 1.755,

i.e. the modulus in THEOREMS.md Theorem 1 (C·(log 1/h)^{−1/2}) improves to a
Lipschitz bound with the envelope's own derivative as the constant — via the
Hadamard-type variational formula for the growing-interval Rayleigh quotient (the
derivative is a boundary-flux term of the minimizer at x = ±a, computable from the
same near-minimizer control as Lemmas B–E of THEOREMS.md).

**(b) Proof strategy.** (1) is a translation exercise once DG-1.1 is in place.
(2): differentiate Q_L along the zero-extension family; the first variation is
2·(boundary concentration of the minimizer) − (entering-prime coupling)², both
already bounded in THEOREMS.md (Lemmas C, E); the missing piece is a matching
*lower* bound on boundary concentration, which the WKB envelope of DG-2 supplies
(the minimizer's edge mass is pinned by its node-saturated structure).

**(c) Hardest missing step.** The lower bound on edge concentration — currently
nothing in THEOREMS.md forbids a minimizer with anomalously small boundary flux;
DG-2.2 is the needed input, so this lemma is downstream of DG-2's easier half.

**(d) Difficulty.** (1): days-to-weeks (statement hygiene). (2): months,
conditional on DG-2.1–2.

**(e) Numerical stress test.** Finite differences on the existing pipeline at a
certified anchor: at L = 2.20 the prediction gives d ln λ/dL = −(0.8775)·e^{1.1}·6.1
= −16.1, i.e. λ(2.21)/λ(2.19) = 0.725 ± 0.02; the repo's measured glide grid at
the p = 3 threshold already brackets this (5.6383e−8 → 1.0245e−8 over
dL = −0.001 → +0.100 is an average slope −16.9; the ±0.001 crossing gave −13.7
against the law's −16.3 at m = 48 resolution). A three-point stencil at m = 64
would decide at the few-percent level in seconds.

---

## 3. Predictions

All falsifiable with existing repo instruments; P1's smooth-model halves were
already run for this plan and passed (§2, DG-2(e), DG-3(e)).

**P1 (WKB signatures on the true-zeros minimizer).** For the spectral-basis
minimizer of the actual form: (i) at L = 2.996 (T* = 28.10), the transform's
log-envelope drop from T* to 2T* is −5.4 ± 0.8 (the excess-area value A(2T*) =
5.43, after the Airy layer); (ii) descent stops between 2T* and eT* with the total
margin matching twice the area at ≈ 3.2T* (predicted stopping-consistency height
90 ± 8); (iii) node censuses are type-budget-saturated, not zero-count-saturated:
at L = 3.2, m = 61, the bottom vector has ≈ 8 nodes below T* = 31.1 — the 4
ordinates plus ≈ 4 non-ordinate nodes, i.e. 1–2 beyond the two already disclosed
(7.640, 13.655). Falsifier: envelope drop at 2T* off by more than a factor ~2 in
the log, or a node census pinned to N(T) instead of aT/π — either kills the
excess-area mechanism.

**P2 (the law's next rungs, from the area reading — numbers logged here first).**
(i) Segment slope: the decomposition d(ln λ)/d(e^{ℓ}) = −1.755(ℓ+5) reproduces the
measured per-segment slopes 10.70/11.24/11.62 as 10.65/11.19/11.66 (0.3–0.5%);
the *next* ζ segment, between the p = 7 (L = 4.025) and n = 9 (L = 4.5) windows,
must come in at slope −12.5 ± 0.3 per unit e^{ℓ} once both endpoints converge.
(ii) Absolute depth: λ(ζ, L = 4.75) = 1.6×10⁻⁴⁸, with the Rayleigh–Ritz upper
bound descending into [5×10⁻⁴⁹, 8×10⁻⁴⁸] (needs dps ≈ 120 assembly, same recipe
as the repo's L = 4.5 run). (iii) Family, same germ: anchoring on the measured
q = 3, L = 6 value 2.5363e−31 and using ℓ_χ = L/2 − ln q in the law,
λ(q = 3, L = 7) descends toward ≈ 5×10⁻⁵⁵ (predicted band [1×10⁻⁵⁶, 5×10⁻⁵⁴];
the anchor is itself a descending upper bound, so the bias is one-sided and
known). A clean miss on (iii) with (i)–(ii) passing would falsify specifically
the time-translation (universal-germ) reading of conductor dependence.

**P3 (rigidity class: the missing GUE point).** Generate ordinates with GUE
spacing statistics at the smooth density (unfold CUE eigenphases of dimension
≈ 2N(Γ_cut), rescale by N^{-1}), and run the repo's model_zeros comparison at
(L = 2.485, Γ_cut = 420, m = 48), where true/smooth/Poisson = 2.690e−10 /
2.751e−10 / 2.895e−12. Prediction: λ_GUE ∈ [3×10⁻¹¹, 3×10⁻¹⁰] — within ≈ 2 nats
of the true zeros and at least 3× closer (in log) to true than to Poisson,
because GUE number-variance is logarithmic (D_eff ≈ 1) while Poisson's is linear.
Falsifier: λ_GUE at the Poisson offset kills the discrepancy mechanism of DG-3
(and with it the claim that the offset measures a rigidity class); λ_GUE
indistinguishable from true/smooth would say number variance below the ln-level
is invisible, sharpening the constraint table (Track E) to "counting function
only, rigidity class irrelevant" — either outcome is information.

---

## 4. Interfaces

**Needs.**
- From numerical analysis: (i) the P2 deep points (dps ≈ 120 ladder at L = 4.75;
  q = 3 at L = 7); (ii) a 10-line envelope-extraction utility on top of
  `spectral_margins.py`'s minimizer for P1; (iii) a CUE/GUE ordinate generator for
  P3; (iv) eventually, the layer-stripping reconstruction of DG-1(e).
- From number theory: rigorous sup|S(T)| inputs on the relevant windows for
  DG-3(i) (Trudgian-type bounds suffice unconditionally), and the family version
  with the analytic conductor qT/2π replacing T/2π throughout (the DG lemmas all
  generalize verbatim under ℓ → ℓ − ln q — this is the universality mechanism).
- From harmonic analysis / de Branges expertise: the two walls named above —
  quantitative Beurling–Malliavin with type loss o(e^{−ℓ}) (DG-2.4) and
  second-order Tauberian normal form (DG-1.2). Both are their machinery
  (Mashreghi–Nazarov–Havin; Poltoratski; Ortega-Cerdà–Seip, Ann. of Math. 155
  (2002), for the frame-characterization side). Offered in exchange: the obstacle
  problem of DG-2.4 stated in their language, with a verified numerical solution
  to calibrate against at every step.
- From the category-theory / Connes–Consani direction: nothing blocking; offered
  *to* them, three constraint-table rows (Track E), stated as theorems-modulo-DG:
  (row 1) any candidate geometry (scaling site, Deninger foliation, xp
  realization) reproduces the entire envelope iff its Weyl datum is N(T) — the
  envelope cannot see periodic-orbit (prime) data at all (DG-3 + measured glide);
  (row 2) conductor = time translation of the scaling flow by (ln q)/2 in type —
  testable via P2(iii), and matching Connes' Weyl term where the conductor enters
  the volume; (row 3) the only slots where arithmetic finer than N(T) can appear
  are the offset (measured 10.2 for ζ) and the rigidity class (P3) — so a
  candidate is *confirmed* by the margin data only through those two numbers, and
  the frameworks' predicted offsets are the discriminating computation to request
  from each (Connes, Selecta 1999; Connes–Consani, Selecta 2021; Connes–Moscovici,
  PNAS 119 (2022); Deninger, ICM 1998).
- From formal methods (Track A): DG-3's finite core (Lipschitz of ln λ_min of a
  fixed Galerkin section under sample-point perturbation, via rank-2 interval
  updates) is the natural next kernel-checked statement after
  `weil_window_positive` — it would certify that the measured envelope is stable
  against ordinate uncertainty, closing the loop between the certificate ladder
  and the law.

**Compositions.** DG-2 + DG-3 is the theorem-shaped version of ENVELOPE.md's
sharpest question (are b and +4 derivable from the counting function): DG-2 on the
smooth model, transferred to ζ by DG-3, with the family by ℓ → ℓ − ln q. DG-1 is
the geometric object all of it lives on; DG-4 closes the loop with the repo's own
Theorem 1.

---

## 5. Honest assessment

**The strongest objection: this program provably attacks the arithmetic-free part
of the problem.** The repo's own decisive measurement (model_zeros; RESULTS) is
that the envelope is a functional of N(T) plus a rigidity offset. Everything my
field can compute — Hamiltonian normal forms, Agmon actions, Weyl asymptotics,
equilibrium problems — therefore lands on quantities that are *identical* for the
zeta zeros and for a smooth staircase with no arithmetic in it. RH is not there.
The uniform positivity transfer needs the sign of Q_L, which is the residue of two
O(1)-scale quantities (deficit and rescue ledgers) cancelling to e^{−S(L)}; the
geometry supplies S(L) — the normalization N_p that PROGRAM §3 says must divide
out the envelope — but not the sign. The realistic best case for these lemmas is:
(i) the correct renormalized form of UPT with its envelope proved rather than
fitted, (ii) a certified constraint table for Track E, and (iii) genuinely
publishable inverse-spectral mathematics (DG-2.3, DG-3) — not RH. The failure mode
to fear is spending the program's attention proving beautiful asymptotics for a
model problem while the door stays where Weil left it.

Secondary cautions, stated plainly. (1) *History:* the de Branges route carries
the field's most cautionary provenance — de Branges' own RH announcements, and
Conrey–Li (IMRN 2000) showing his positivity conditions fail numerically. The
lemmas here use the chain machinery descriptively (existence, asymptotics), never
the positivity conditions; but a program that walks this hallway should say so at
every door. (2) *Numerology risk:* b is measured to ~1%; 7/4, √π, and ln 6 are all
within range. Any derivation that "finds" one of these by fitting has found
nothing; DG-2.4 is only meaningful if the constant is an output, after which the
repo should refit the ladder with the derived functional form frozen. (3) *The
bracket tension:* my Jensen ceiling (52.7·e^{ℓ}) conflicts with the measured
(ℓ+4)-growth beyond ℓ ≈ 26 — untestable numerically forever (λ ~ 10^{−10¹²}), so
one of "the law bends" / "smallness-without-vanishing takes over" / "the ceiling
argument has a hole" must be settled by proof, and until it is, extrapolations of
the law past L ≈ 5 (including my P2) carry a stated model risk. (4) *Conditioning:*
the frame reading of λ(L) is RH-conditional; all DG statements are about the
smooth model (unconditional) plus a transfer whose ζ-side input (sup|S|) is
unconditional, but the identification of Q_L with a frame form is not — inherited,
as everywhere in this repository, from the explicit formula's two-sidedness. (5)
*One-sidedness:* every deep measured value cited is a Rayleigh–Ritz upper bound;
my predictions inherit that bias direction and say so where it matters.

---

## Round 2 — honing (differential geometry)

Written after reading `SYNTHESIS.md` and the cited sibling PLANs (independence rule
lifted). Three items as requested: (a) verdict on the merged T3 statement and the
§2 algebra, with the identity checked symbolically; (b) the fullest proof sketch of
the Rigidity Transfer Theorem; (c) the verbatim-executable w(L) protocol for C4.
One verification computation was run for this round (sympy + mpmath, scratchpad;
outputs quoted below); no repo files other than this one are touched.

### (a) Verdict on the merged T3 and the synthesis §2 algebra

**The central identity is exactly right.** With D(T) = (a/π)T − N(T) and
A(T; L) = ∫_{T*}^{T}(πρ − a)dt, symbolic check (sympy) confirms

  2A(T; L) = 2π[D(T*) − D(T)]  — exactly, not asymptotically,

because N′(T) = (1/2π)ln(T/2π) = ρ(T) *exactly* for the RvM smooth staircase (the
e inside ln(T/2πe) is what makes the derivative constant-free), and the 7/8 cancels
in the difference. Downstream consequences re-verified exactly:
2π[D(T*) − D(e^{w}T*)] = T*(e^{w}(w−1)+1); the drift equation reproduces my Round-1
band (recomputed: w = 1.147 at L = 2.485, 1.237 at L = 5.0); w∞ = 1.27846 solves
e^{w}(w−1) = 1 and gives slope cap 2π(1+1) = 4π = 12.5664; crossovers at
L = 4.32 (b,c₀ = 1.755, 4) and 4.56 (1.51, 5.04) confirmed.

**One slip, which cancels:** the synthesis header says D(eT*) = 0. Exactly,
D(eT*) = −7/8 (the zero of D sits at eT*(1 − (7/8)e^{−ℓ−1}), exponentially close to
eT*). The slip is harmless everywhere it is used: in §2(iii) the displayed
consequence 2A(eT*) = T* is *exact* because the two 7/8's cancel:
2π[D(T*) − D(eT*)] = 2π[(e^{ℓ} − 7/8) − (−7/8)] = 2πe^{ℓ} = T*. Nothing downstream
changes; the header line should read "D(eT*) = −7/8".

**§2(i)–(ii) verified:** N(T*) + μD(T*) = e^{ℓ}(ℓ − 1 + μ) + (7/8)(1 − μ), so
μ = c₀ + 1 exactly as stated; NT's deficit-measure mass ∫₀^{T*}(a/π − ρ)dt = e^{ℓ}
exactly (D(T*) differs from it by the boundary constant N(0⁺) = 7/8); NT's closed
form is the (b, μ) = (1.755, 5) member of the invariant family — all checked. I
accept the reparameterization verdict on my own seat: my "action reading" is a
change of variables on the measured range, not independent confirmation; its one
new degree of freedom is the stopping height, which is why C4 is the right use of
it. I also accept K5 as it applies to me: my Round-1 P2 numbers were stated in
(1.755, 4.0) coordinates and should be read as that member of the degenerate
family; the w-protocol below is deliberately built to be insensitive to which
member is used (drift references from (1.755, 4) and (1.51, 5.04) differ by ≤ 0.013
at calibration L and ≤ 0.003 at deep L — table below).

**Merged T3 statement: endorsed, with four refinements.**
1. The constant should be written C(ℓ)·(D+1) with C(ℓ) = κ₀·(ℓ + 2 + ln(ℓ+1) +
   ln(1/δ₀)) rather than bare C₀·ℓ — the ℓ enters as ln K, K = N(e²T*) ≤
   (ℓ+1)e^{ℓ+2}, and a separation parameter δ₀ must appear (see H3 below);
   for ℓ ≥ 1 this is the synthesis' form.
2. The hypothesis needs the separation clause (H3) explicitly; the Poisson
   corollary then goes through a grouping/thinning variant (gap G4 below), not the
   main statement. As stated ("both of log-type density") a Poisson realization
   violates no hypothesis but breaks the transplantation at near-coincident pairs.
3. A tail clause is required and is currently hidden: the discrepancy hypothesis
   caps at e²T*, but λ depends on both tails. The theorem either imports T1(iii)
   (worth beyond eT* is O(1) — the synthesis' own interlock) or adds hypothesis
   (H4). This is boxed gap G3, and it is one more reason T1 outranks T3 in the
   schedule: T3's clean form *consumes* T1(iii).
4. Q3 (the factor 6.3 = 1.84 nats at L = 3.555) does **not** threaten T3 as
   stated: with D = sup|S| ≈ 1 and C(ℓ = 1.78) ≈ 2–4 the anomaly sits inside the
   theorem's budget with room. What Q3 threatens is law-theory §3.5's *shared
   constants* claim (offset equality, not offset boundedness). The synthesis'
   framing "T3's sharp form is in trouble" should be split: bounded-transfer T3 is
   safe either way Q3 resolves; only a sharpened "offset → 0" variant is at stake.
   The CO-2(e) rider (values transfer, forms do not; λ_rel = 2.6e−5) is endorsed
   verbatim as clause (iii) of the theorem.

### (b) Proof sketch: the Rigidity Transfer Theorem (fullest version)

**Statement (for the record).** Let Λ₁, Λ₂ ⊂ (0, ∞) be locally finite (extended
symmetrically), with counting functions N₁, N₂ and
(H1) sup_{0<T≤e²T*} |N₁ − N₂| ≤ D;
(H2) both within D+1 of the RvM staircase N on (2πe, e²T*] (log-type density);
(H3) both δ₀-separated relative to local mean spacing: t_{k+1} − t_k ≥
     δ₀·2π/ln(t_k/2π);
(H4) tail clause: Λ₁ = Λ₂ on (e²T*, ∞), or both of log-type density there plus the
     capacity input T1(iii).
Then |ln λ[Λ₁](L) − ln λ[Λ₂](L)| ≤ κ₀(D+1)(ℓ + 2 + ln(ℓ+1) + ln(1/δ₀)) + κ₁, with
κ₀, κ₁ absolute. Corollaries: (i) ζ ↔ staircase with D = sup|S(T)| — at L = 5 the
window is e²T* = 2πe^{4.5} = 565.5, where Trudgian (J. Number Theory 134 (2014))
gives unconditionally |S| ≤ 0.112 ln T + 0.278 ln ln T + 2.510 ≤ 3.73 (numerically
sup|S| ≈ 1.1 there), so the envelope transfers with an O(ℓ)-size offset,
unconditional on the model side; (ii) Poisson via the grouped variant; (iii) the
CO-2(e) rider: transfer of values only, no form-level equivalence exists.

**Route A (primary): the configuration flow.** This replaces my Round-1
transplantation as the cleaner mechanism; the Blaschke-product route survives as
fallback (Route B).

*Step 0 (pairing and flow).* Pair the sequences monotonically by index inside
(0, e²T*]; by (H1)+(H2), displacements satisfy |Δ_k| := |t_k^{(1)} − t_k^{(2)}| ≤
(D+1)/ρ̄(t_k), ρ̄ = local mean density. Flow linearly: t_k(s) = (1−s)t_k^{(2)} +
s·t_k^{(1)}, s ∈ [0, 1]. Two free facts: convex combinations of two increasing
sequences are increasing (order preserved), and gaps interpolate linearly, so
δ₀-separation is preserved *with the same constant* along the whole flow. No
collisions, ever — this is what kills the coincidence problem that Route B has to
fight with exceptional sets.

*Step 1 (Danskin envelope derivative).* λ(s) = min_{‖φ‖=1} Q_s(φ),
Q_s(φ) = 2Σ_k |F(t_k(s))|² (+ fixed tail). By Danskin's theorem (Danskin 1966;
Bonnans–Shapiro Ch. 4) λ is Lipschitz in s with a.e.
|λ′(s)| ≤ max_{φ ∈ M(s)} |∂_s Q_s(φ)| = max 2|Σ_k Δ_k·(|F|²)′(t_k(s))|,
M(s) the minimizer set. No simplicity of λ_min is needed. [Standard; days.]

*Step 2 (the multiplicative sample bound — the crux).* For a *minimizer* φ ∈ M(s),
the Euler–Lagrange identity in Fourier form reads

  λ F(t) = 2 Σ_k F(t_k) K_a(t − t_k) (+ symmetric term),  K_a(u) = 2 sin(au)/u,

i.e. F is reproduced from its own sample values through the PW_a kernel.
Differentiating at a sample t_j and splitting the k-sum at |k − j| ≤ M:

  |F′(t_j)| ≤ C ρ̄(t_j) · max_{|k−j|≤M} |F(t_k)| + (far-field spillover),

because near-diagonal kernel derivatives are ≤ C a·ρ̄ per neighbor after summation
against separation (H3), while the far field decays like 1/|t_j − t_k| against
density ρ̄ — a logarithmically divergent sum that must be paid: cutting at M and
dyadically decomposing the far field costs the factor ln K + ln(1/δ₀) ≈
ℓ + ln(ℓ+1) + ln(1/δ₀), and this is precisely where the theorem's C(ℓ) originates.
Then

  Σ_k |Δ_k| |(|F|²)′(t_k)| ≤ 2 max_k [|Δ_k| ρ̄(t_k)] · C(ℓ) · Σ_k (max-local |F|)²
                           ≤ C(ℓ)(D+1) · C_M · Q_s(φ)/2,

using |Δ_k|ρ̄ ≤ D+1 and the finite-overlap of the local maxima (each sample counted
≤ 2M+1 times). Hence |λ′(s)| ≤ C(ℓ)(D+1)·λ(s) — multiplicative, which is the whole
game — and Grönwall over s ∈ [0,1] gives |Δ ln λ| ≤ C(ℓ)(D+1). Note where additive
routes die: any use of a global Plancherel–Pólya/Bernstein bound (Σ|F′(t_k)|²/ρ̄ ≤
C a²‖F‖²) in place of the local EL bound produces |λ′| ≲ (D+1)·a·√λ·‖F‖ — additive
in √λ, useless at λ ~ e^{−100}. The EL self-consistency is not decoration; it is
the only known source of locality at the samples.

*Step 3 (tail).* Under (H4) first clause, the tail terms of Q_s are s-independent
and ride along. Under the second clause, insert two intermediate measures agreeing
above e²T* and invoke T1(iii) to price the swap at O(1) [gap G3].

**Boxed gaps.**
- **[G1] The local dominance lemma** (Step 2's far-field control, uniform along the
  flow): prove Σ_{|k−j|>M} |F(t_k)| |K_a′(t_j − t_k)| ≤ ½ ρ̄(t_j)·max-local|F| +
  e^{−cM}-type remainder for M ≍ ℓ + ln(1/δ₀), for minimizers along the flow. This
  is the theorem's real content. Tools: dyadic far-field decomposition + Levin's
  perturbed-sine-type comparison for the near field (Levin, *Lectures on Entire
  Functions*, AMS 1996) — HA's toolbox per the synthesis allocation; the flow
  construction has already removed the coincidence sets that make the naive version
  false. Estimated: the wall; weeks–months. Empirical slack is large: jitter data
  gives net constant 1.0–2.3 at ℓ = 1.24 where the claim allows κ₀·4.05 ≈ 2.4–4
  even with κ₀ = 0.6–1.
- **[G2] Danskin regularity along the flow** (measurable selection of minimizers,
  a.e. differentiability): standard convex analysis; days; cite Danskin,
  Bonnans–Shapiro.
- **[G3] The tail swap** = T1(iii) import (or accept hypothesis H4 first clause,
  which already covers corollary (i) if the staircase is used above e²T* on both
  sides — note the ζ-corollary then needs the ζ-tail swapped once, which is again
  T1(iii); there is no route around the capacity input, only postponement).
- **[G4] The Poisson corollary's grouping**: thin Λ_Poisson to a maximal
  δ₀-separated subset (frame form decreases; one-sided), account the removed
  points as a density-defect increment to D; the LIL-scale D ≍ √(N ln ln N) then
  gives the measured super-constant, sub-exponent cost. Weeks; independent of G1.

**Constants and the Lean-adjacent core.** Explicit target: κ₀ ≤ 10 (proof-grade),
κ₀ ≈ 0.25–0.6 empirical (from the Round-1 jitter table: measured net 1.0–2.3
against ℓ + 2 + ln(ℓ+1) = 4.05 at ℓ = 1.24). The finite core to certify (NA + Lean
per T3's route): for a fixed Galerkin section, moving one sample t_k by Δ changes
the assembled frame matrix by a rank-2 update with interval-computable norm;
chaining K such moves along the Step-0 flow gives a kernel-checkable
|Δ ln λ_min^{(m)}| bound — no G1 needed at fixed m, because the section is finite;
G1 is exactly what survives m → ∞. This split (certify the finite statement now,
prove G1 for the limit) is the recommended execution order.

### (c) The w(L) protocol — C4's stopping height as bend adjudicator, verbatim

**Prefatory honing (important; from this round's computation).** C4's contrast
claim needs one correction before anyone spends compute. There are *three*
hypotheses, not two, and they separate differently in w:

- **Drift** (no bend): w follows e^{w}(w−1) = (b/2π)(ℓ+c₀) − 1.
- **Abrupt saturation**: w jumps to w∞ = 1.2785 at the crossover (T_s = 3.59T*).
- **Smooth cap** (slope pinned at 4π, w evolving continuously): differentiating
  E + A = T*(e^{w}(w−1)+1) under dE/dc ≡ 4π gives the consistency ODE
  w′(ℓ) = (1 − e^{w}(w−1))/(e^{w}w) from (ℓ_c, w_c) — verified by integration this
  round: w(4.5/4.75/5.0) = 1.2199/1.2271/1.2334, i.e. within 0.003 of the drift
  values 1.2201/1.2285/1.2368. **Under the smooth cap, w-levels do not
  discriminate at reachable L.** Only abrupt saturation is level-detectable:
  Δw ≈ 0.05–0.06 vs drift at L = 4.5–5.0, i.e. ΔT_s ≈ 12 at L = 4.5 (≈ 4.3 nodes),
  against Airy-layer blur (aT_s)^{−2/3} ≈ 2.6% (≈ 0.03 in w) — a 2:1 signal-to-blur
  margin, real but not comfortable. Consequently the protocol has three readouts:
  the *convergence gate* (which is where the bias question actually gets decided),
  the *level test* (decides abrupt saturation only), and the *shape test* (the
  only observable that separates smooth-cap from drift). C4 remains the right
  experiment; its decision table just has one more row than the synthesis states.

**Reference table** (computed this round; drift values under (b,c₀) = (1.755, 4)
and (1.51, 5.04) — the spread between the two family members is the quoted ±):

| L | T* | w_drift (±family) | T_s/T* drift | w abrupt | w smooth-cap |
|---|---|---|---|---|---|
| 2.485 | 21.77 | 1.147 ± 0.013 | 3.15 | — (pre-crossover) | — |
| 2.996 | 28.10 | 1.167 ± 0.010 | 3.21 | — | — |
| 4.25 | 52.61 | 1.212 ± 0.003 | 3.36 | 1.2785 | 1.214 |
| 4.50 | 59.61 | 1.220 ± 0.002 | 3.39 | 1.2785 | 1.220 |
| 4.75 | 67.54 | 1.229 ± 0.000 | 3.42 | 1.2785 | 1.227 |
| 5.00 | 76.54 | 1.237 ± 0.001 | 3.44 | 1.2785 | 1.233 |

**Step 1 — configurations.** Minimizer coefficient vectors c (spectral Legendre
basis, as in `spectral_margins.py` / the deep-windows runs) at:
calibration: (L = 2.485, m = 48 and 64), (L = 2.996, m = 64);
deep: (4.25, m = 128 and 144), (4.50, top two m in runs.csv), (4.75, m = 144 and
160), (5.00, m = 144 and 176). Reuse stored eigenvectors if the deep-windows agent
kept them; otherwise re-solve at the dps recorded in runs.csv for that (L, m)
(the two largest re-solves dominate the cost; everything else is minutes). Export
c at full working precision.

**Step 2 — envelope extraction.** For each configuration: evaluate
F(T) = |Σ_j c_j f̂_j(T)| (same spherical-Bessel/GL quadrature as assembly; mpmath
dps ≥ max(50, ⌈0.8·E_m⌉/2) so the floor is resolved — at L = 5 use the assembly
dps) on a log-uniform grid of 4096 points in u = ln(T/2π) ∈ [ℓ − 0.7, ℓ + 1.8].
Record local maxima (u_e, ln F_e); set ref = max ln F_e on |T/T* − 1| ≤ 0.1;
ε(u) = ln F_e − ref.

**Step 3 — estimators (report all four per configuration).**
- **w_E1 (floor crossing):** floor = min ε over u ∈ [ℓ, ℓ+1.8]; w_E1 = smallest
  u − ℓ with ε(u) ≤ floor + 1.
- **w_E2 (action matching; primary):** solve T*(e^{w}(w−1)+1) = E_m + A with
  E_m = −ln λ_m (Aitken-corrected where the ladder supports it) and A = 11.5;
  report the A-sensitivity band by rerunning with A = 11.1 and 11.9 (at deep L
  this moves w by ≤ 0.004 = 0.4·∂w/∂A, ∂w/∂A = 1/(T*e^{w}w) — computed: ≤ 0.005
  at L = 4.25, shrinking with L; this is why E2 is fit-insensitive exactly where
  it matters).
- **Node census:** count real nodes of F (deep minima of |F| below 10⁻³·max) in
  [0, xT*] for x = 3.36, 3.59 (the drift and abrupt reference heights); the
  abrupt-vs-drift contrast is 4–6 nodes at L ≥ 4.5.
- **Shape function:** y(x) = [−dε/du]/(2πe^{u}) against x = u − ℓ on
  x ∈ [0.20, w_E1 − 0.05], derivative by centered differences on a monotone fit of
  the envelope maxima. Graded-area prediction: y = x (line of slope 1 through the
  origin) along the entire descent, at every L. Any capped mechanism: y = x up to
  a break x_b, then sub-linear.

**Step 4 — calibration.** At L = 2.485 and 2.996: check w_E2 against the drift
row (expected 1.147/1.167 ± 0.02 — pre-registered here; my Round-1 run measured
the descent floor E1 at w_E1 ≈ 0.69–0.83 at L = 2.485, so expect and record
Δ_cal = w_E2 − w_E1 ≈ 0.35–0.45); Δ_cal is then applied to deep w_E1 as the
secondary estimate. If the calibration w_E2 misses the drift row by > 0.05, stop:
the estimator pipeline, not the physics, is broken (oracle discipline).

**Step 5 — decision rules (in order; verdicts U / B_abrupt / B_smooth / D).**
1. *Convergence gate (per deep L, two m-rungs):* require
   |w_E2(m_top) − w_E2(m_prev)| ≤ 0.01 AND node-census change ≤ 1. Fail ⇒ verdict
   **U** for that L: unconverged — Rayleigh–Ritz bias not excluded; supports NA's
   reading in Q1; do not proceed to level/shape claims at that L. (This gate is
   itself the bias diagnostic: a basis that cannot yet represent the full dodging
   zone shows T_s still growing with m.)
2. *Level test (converged L only):* w_E2 ≥ 1.26 at both L = 4.75 and 5.00 ⇒
   verdict **B_abrupt** (bend confirmed, abrupt-saturation mechanism). w_E2 in
   [1.20, 1.25] ⇒ levels non-discriminating (as predicted for drift AND smooth
   cap); go to 3. w_E2 ≤ 1.18 at deep L ⇒ inconsistent with all three hypotheses
   ⇒ treat as pipeline bug until the calibration row re-verifies.
3. *Shape test:* piecewise-linear fit of y(x); a break x_b with post-break slope
   ≤ 0.5, detected at both L = 4.75 and 5.00 with consistent x_b (± 0.03) and
   F-test p < 0.01 against the single-line model, stable across the top two
   m-rungs ⇒ verdict **B_smooth** (bend, smooth-cap mechanism). Otherwise ⇒
   verdict **D**: drift intact at reachable L — the deep ΔE deviations are
   convergence bias (Q1 resolves per NA), and the saturation clause is deleted
   from C4 per the synthesis' own §2(iv) instruction.
4. *Baseline row (mandatory, cheap):* repeat Steps 2–3 on the smooth-staircase
   model at the same (L, m) (my Round-1 scratchpad recipe, minutes per point). Per
   T3, all estimators must agree with the true-zeros values within ± 0.02 in w;
   a discrepancy > 0.05 flags an arithmetic effect in the stopping height itself —
   which would contradict the density-functional picture and is itself
   discovery-grade (treat as bug first, per program law).

**Deliverable:** one table (configuration × {λ_m, E_m, w_E1, w_E2 ± A-band, node
censuses, x_b or "none", verdict}), plus the calibration row and the baseline row.
Everything except the two deep re-solves is O(minutes); the verdict feeds Q1
jointly with NA's creep-corrected fit (decision rule per synthesis Q1: bend is
confirmed only if (a), (c) and this measurement agree).

---

## Round 3 — vector shape test

Assignment (coordinator, 2026-07-26): execute the vector-level shape test (Round-2
protocol Step 5.3) end to end. Context from `results/agent-deep-windows.md` (read
first, as instructed): scalar protocol executed — convergence gates PASS through
L = 4.75; level test excludes B_abrupt (w_E2(4.75) = 1.224 < 1.26); scalar shape
analog (secant slopes in the p = 4.5 gauge: 12.53/12.42/12.58 vs 4π = 12.566,
drift references 12.93–13.31) favors B_smooth at 3–6% separation with ≤ 0.5% bias
headroom; deep rate 4π to 0.4–1.3%; onset L = 4.32. The formal B_smooth verdict
awaits this test, since the deep runs did not store minimizer vectors.

### Part A — pre-registration (committed before any curve was computed)

Full pre-registration: `results/experts/dg-vectors/PREREGISTRATION.md`
(timestamped 19:27 UTC; thresholds, estimators, reference numbers, and the
verdict decision table are fixed there and applied verbatim below). Summary of
what was committed in advance:

- **Configurations:** (4.50, m = 160 and 144), (4.75, m = 160 and 144) at
  dps 75/65 — the m = 144 rungs restore my Round-2 m-stability clause, which the
  coordinator's two-configuration assignment alone cannot satisfy; null control
  (3.555, m = 112 and 128) at dps 50/40. Two workers (core cap respected).
- **Scope disclosure, made before the data:** the Legendre coefficient of e^{iTx}
  is ∝ j_k(aT), which decays only past order k ≈ aT, so the node-representable
  edge of the basis is T_edge ≈ m/a: x_edge = 0.87/0.76 at L = 4.50 (m = 160/144),
  0.69/0.59 at L = 4.75 — the direct y(x) break window x ∈ [1.0, 1.25] is out of
  basis reach at every affordable configuration, and a naive break found there
  would be truncation artifact. The pre-registered discrimination therefore runs
  through two bias-robust vector observables: **x_nodes** (the last-node height:
  m-stable = mechanism-limited vs shifting by ln(160/144) = 0.105 =
  truncation-tracking) and the **graded-activity ratio**
  G = Δln λ / Δ2A(x_nodes) between the m-rungs (graded dodging active in the
  newly resolved shell ⇒ G ≈ 1; capped/nodeless outer mechanism ⇒ G ≪ 1) — plus
  the y(x) = x graded-line check inside the resolved zone, and the control null.
- **Verdict rules** (C1 pipeline gate, C2 graded core β₀ ∈ [0.85, 1.15], C3
  discriminator (m-stable early node edge OR G ≤ 0.2 at both deep L), C4 control
  null, C5 B_abrupt exclusion): B_smooth CERTIFIED iff all five; NOT CERTIFIED if
  C3 indeterminate; U on any gate failure or G ≥ 0.5. **Pre-committed falsifier
  of B_smooth:** edge-tracking node zones with G ∈ [0.5, 2] at both deep L —
  that would be drift's graded dodging still absorbing action at the graded
  rate, reverting the deep deviations to Q1-bias territory.

### Part B — execution and results

**Execution.** All six decision configs + smoke ran to completion
(`results/experts/dg-vectors/`: run_vec.py workers, vec_/env_/meta_ files, logs;
one session interruption absorbed — all artifacts landed intact and timestamped
before it, verified by line counts and log tails). Ordering discipline holds:
pre-registration 19:27 UTC, amendments 1/1b 19:34–35 UTC (with `ls` proof that no
decision envelope existed), first deep envelope 19:44:55 UTC. Smoke rung
reproduced the certified anchor to all printed digits.

**C1 (pipeline) — PASS.** Every λ reproduces runs.csv to all printed digits
(7.92448858514e-41, 8.13421925362e-41, 1.86366090828e-47, 2.04044762883e-47,
2.12668062431e-22); gaps λ₂/λ₁ = 1.8e3–6.0e3; ‖c‖ = 1. New rung 3.555/128 =
2.10258824104e-22 — NOTE: 0.8% *below* the pre-registered Aitken bracket edge
2.119e-22, the same staircase-Aitken failure mode the deep agent documented at
L = 4.25 (monotone RR descent intact; no gate references this bracket, reported
for the record). w_E2 reproduces the deep agent's scalar table to ±0.0003 at
every config (1.2192/1.2243/1.1970 at 4.50/4.75/3.555).

**The discriminator measurements (pre-registered estimators, frozen thresholds):**

| config | λ | x_dodge | x_spacing | flag | w_E1 | w_E2 | tail16 |
|---|---|---|---|---|---|---|---|
| 4.50/160 | 7.9245e-41 | 0.6235 | 0.3513 | DISAGREE | 0.845 | 1.2192 | 9.0e-43 |
| 4.50/144 | 8.1342e-41 | 0.6235 | 0.3513 | DISAGREE | 0.786 | 1.2191 | 3.5e-42 |
| 4.75/160 | 1.8637e-47 | 0.6535 | 0.5644 | DISAGREE (0.089) | 0.843 | 1.2243 | 8.0e-49 |
| 4.75/144 | 2.0404e-47 | 0.6345 | 0.6845 | OK | 0.857 | 1.2240 | 7.0e-46 |
| 3.555/112 | 2.1267e-22 | 0.5955 | 0.7195 | DISAGREE | 0.819 | 1.1970 | 4.8e-25 |
| 3.555/128 | 2.1026e-22 | 0.5955 | 0.7195 | DISAGREE | 0.819 | 1.1971 | 8.3e-25 |

- **Node-edge m-shifts:** 4.50: 0.0000; 4.75: +0.0190; control: 0.0000 — against
  the truncation-tracking prediction +0.105 (deep) / +0.134 (control). All
  m-STABLE. Registration quality inside the dodge zone is spectacular: alignment
  d ≤ 0.02 local spacings at both deep L through the entire prefix (control:
  d ≤ 0.04 to x = 0.56, then gradual detachment 0.13/0.18/0.24 — a visible
  transition zone).
- **Graded-activity ratio:** G(4.75) = 0.0906/1.575 = **0.058** ≤ 0.2.
  G(4.50) = 0.0261/0.000 — **undefined** (identical x_dodge at both m ⇒ 0/0).
- **Spacing-flag diagnoses** (each break inspected against the actual zero list):
  4.50 at x = 0.351: ΔT = 2.756 vs zero-gap 2.690 vs sinc 2.793 — the two
  lattices are 4% apart there; the classifier lost by 0.03. Estimator power,
  not deregistration (alignment d = 0.01–0.02 through that region). 4.75/144:
  one SAMEZERO double-dip (two nodes registered to γ at 138.116 — a tangency).
  Control: the classifier detached at 0.72, two gaps *after* alignment detached
  (0.60) — transition-zone width. None of the three causes indicates the primary
  estimator misfired; all three flags stand as frozen.
- **y(x) and C2:** the frozen 5-maxima grouping yields n_fit = 1–3 groups in the
  registered zone (and 0 at the control, whose oscillation spacing violates the
  frozen span-0.12 rule) — **C2 is UNEVALUABLE as frozen** (spec starvation: the
  Round-2 grouping was calibrated for a fit zone reaching x ≈ 1.1; the
  registration cap shrank it to x ≤ 0.6). Post-hoc (labeled) 4-max windows:
  y/x slides ≈ 1.1–1.4 (Airy layer, x ≈ 0.26) → 0.54 (x ≈ 0.38) → 0.2–0.6
  (x ≈ 0.5), identical at m = 144/160; slope noise between windowings is large
  (±0.3), but the robust cumulative version is decisive — see F3.

**Formal verdict (strict application of the frozen table): B_smooth NOT
CERTIFIED.** No gate failed; the pre-committed falsifier of B_smooth did NOT
fire (edge-tracking with G ∈ [0.5, 2] was the kill condition; measured shifts
0.000–0.019 vs tracking 0.105, and G = 0.058); C5 holds (w_E2(4.75) = 1.2243 <
1.25, B_abrupt stays excluded); but certification is blocked by: (i) the frozen
DISAGREE flags (diagnosed above, yet I may not amend thresholds post-data);
(ii) C2's grouping starvation; and (iii) — decisive and more interesting than
either — **the null control refuted the discriminating premise of C3 itself**:
early, m-stable registration-termination is not a deep-L cap signature; it is
the generic behavior at every L, including the pre-crossover control (x_dodge =
0.5955 there, equally m-stable). The vector channel, as designed, does not
separate drift from smooth-cap; the null check did exactly the job nulls are
for. The bend therefore remains adjudicated by the scalar evidence (deep
agent's secant slopes on 4π to 0.4–1.3%, drift refs 3–6% away, bias headroom
≤ 0.5%) — which this test leaves **unopposed but uncertified**. Q1's decision
rule (synthesis: (a) NA creep-corrected fit + (c) hp-graded run + (d) this
measurement must agree) should replace (d)'s role with the findings below.

**Findings (the vector data's actual payoff; all m-stable, all cross-checked
at two L or more):**

- **F1 — Registration terminates early and universally.** Node-to-zero locking
  (d ≤ 0.02) holds from below T* out to x_dodge ≈ 0.60/0.62/0.65 at
  ℓ = 1.78/2.25/2.375, then detaches to the free sinc lattice (spacing π/a).
  x_dodge sits *below* even the m = 144 basis edge (0.76 at 4.50) with margin —
  mechanism-limited, not basis-forced, independently of the m-comparison.
- **F2 — The constant-action-share law.** 2A(x_dodge)/E = 0.192/0.192/0.195/
  0.210/0.198/0.198 across all six configs: registration ends when the dodged
  zone has delivered ≈ 20% of the exponent, at every L, both regimes. The
  remaining ~80% of the Weil-margin exponent is carried by NODELESS suppression.
  This is the measured resolution of my Round-1 §5 bracket tension
  (smallness-without-vanishing wins, and not marginally), and it is the
  structural input T5/H3's ansatz needs: canonical product over dodged zeros
  only to ≈ 1.9T*, times a smooth corrector carrying 4/5 of the action.
- **F3 — The E-normalized envelope profile is universal and crossover-blind.**
  −ε(x)/E at stations x = 0.3/0.6/0.8/1.0: 0.142/0.222/0.217/0.239 (3.555),
  0.124/0.198/0.215/0.230 (4.50), 0.115/0.198/0.213/0.221 (4.75) — one profile
  to ±0.02·E spanning the L = 4.32 crossover. Nothing in the vector marks the
  bend onset. (This is the strongest form of the null result: not only the
  estimators but the entire scaled profile is L-universal.)
- **F4 — 30% of the exponent is spent BELOW T*.** Absolute measurement from the
  same vectors (sub-T* extension run): the minimizer's bulk sits at the lowest
  frequencies (ln|F| = −0.8 at 0.09T*, monotone descent through −10.2 at
  0.37T*, −28.7 at 0.80T*, L = 4.50), and ln|F(T*)|/E = 0.298/0.300/0.302 at
  the three L. The floor sits at (pre-T* drop) + (relative floor) = E/2 + 3±1
  nats at all three L — exactly the per-sample frame scale, closing the
  bookkeeping. Consequence: the turning-point picture "flat well to T*, Agmon
  descent after" is quantitatively wrong for the true minimizer — 60% of the
  total drop happens before T* (the Landau-type transition band opens an octave
  below the Nyquist crossing, where between-zero recovery room starts closing).
- **F5 — Two self-corrections owed by this seat.** (i) My Round-1 P1 claim
  ("envelope follows the excess-area action, 8% at 2T*") was a shallow-L
  accident: at L = 4.50 the measured drop at 2T* is 1.7× the graded area, at
  x = 0.3 it is 7× — the pointwise Agmon-area envelope is refuted at depth;
  only the *integral* bookkeeping (w_E2) survives. (ii) The Round-1 node-census
  "type-budget saturation" conflated registered and free sinc nodes; with the
  registration lens the budget is NOT saturated — T1(ii)'s node-count clause
  should be restated registration-aware (HA notified via this report).

**Recommendations.** (1) Retire the vector shape test as a bend adjudicator;
the bend rests on Q1(a)+(c) plus the scalar slopes. (2) The new discriminating
object this data suggests: the sub-T* profile share (F4's 0.30·E) and the
dodge share (F2's 0.20·E) as functions of L at higher precision — if the 4π
cap has a mechanism signature anywhere in the vector, it is a drift in these
shares past L ≈ 4.3, currently bounded by ±0.02. (3) Certify one deep vector
rung (4.50/160) by interval Rayleigh to convert F1–F2 into certified
statements (CO/NA machinery, minutes). (4) C3-composite (capacity endpoint in
the de Branges chain) gains a measured target: the registration endpoint
e^{0.62}T* ≈ 1.87T* and its 20% share are now the quantities HA's H1(ii)/T1(ii)
effective-horizon analysis must reproduce — note 1.87T* is well inside eT*,
so the capacity endpoint is an upper horizon, not the registration endpoint.
All data, scripts, logs, and the frozen pre-registration with its two
timestamped amendments: `results/experts/dg-vectors/`.
