# SYNTHESIS — harmonization of the nine-expert panel

Moderator's synthesis, 2026-07-26. Sources: the nine PLAN files in this directory,
`results/agent-law-theory.md` (complete), `results/agent-deep-windows.md` (INTERIM —
used with its post-interim `runs.csv` and `fit_report.txt`, which materially update
the interim verdict; gaps marked), `results/RESULTS.md`, `RH-LEMMA-MAP.md`,
`THEOREMS.md`. Two computations were run for this synthesis with repo instruments
(`src/spectral_margins.py`, dps 50/45):

- **Anchor**: (L=2.485, m=24): λ = 3.8688156e-10, ‖v‖₁² = 3.0391, λ/‖v‖₁² = 1.273e-10
  — reproduces PLAN-convex-optimization CO-2(e) to all printed digits.
- **CO P2(b) adjudicated**: (L=711/200, m=40): λ₁ = 1.7997229e-20 (matches the
  certified enclosure), λ₂ = 1.071e-17, ‖v‖₁² = **4.0094** (CO predicted 3.9 ± 0.6),
  entrywise ball radius δ* ≈ λ/‖v‖₁² = **4.489e-21 < 1e-20** (CO predicted
  (4.6 ± 0.8)e-21). **A δ = 1e-20 ball certificate at that window is impossible; CO's
  prediction is verified.** No existing artifact conflicts: the coordinator's precis
  conflated two windows — the δ = 1e-19 Lean artifact (`WeilcertDeeper`) lives at
  L = 749/250 with margin 4.3462e-15 (headroom 48·1e-19 ≪ λ, fine); **no Lean ball
  certificate exists at L = 711/200** (that window has only the 220-bit mpmath
  interval enclosure). Precis item 5's parenthetical is corrected accordingly.

Notation as in THEOREMS.md: a = L/4, ℓ = L/2, T* = 2πe^{ℓ}, E = −ln λ,
N(T) = (T/2π)ln(T/2πe) + 7/8, D(T) = (a/π)T − N(T) (Nyquist deficit; D(T*) = e^{ℓ} − 7/8,
D(eT*) = 0).

---

## 1. Convergence map

### 1.1 Corroborations (independent seats, same object)

**(a) The capacity endpoint eT*** — three seats, one horizon, none having read the
others:
- law-theory (RUN 4, §3.4): single-zero worth measured supported on exactly [0, eT*]
  at both L = 2.485 and 2.996 (worth < 0.05 beyond eT*, out to γ = 746); §2.3 gives the
  reason: D(eT*) = 0 (deficit closes at the capacity height).
- harmonic analysis (H1): the hard horizon — F ∈ PW_a vanishing on the staircase
  through (1+δ)eT* forces F ≡ 0 — with difficulty "days" for part (i) (parts (ii)/(iii),
  the effective versions, are weeks–months). Route: Levinson density + Jensen.
- differential geometry (§1(i), DG-2): the two structural saturation heights are
  count-saturation at eT* (N(T) = aT/π exactly at u = ℓ+1) and Jensen-saturation at
  e²T*; the measured stopping height 3.03–3.39·T* sits between them; DG's executed
  stress test confirmed the minimizer's node census saturates the type budget aT/π,
  not the zero count.
Precis item 1 verified. This is the program's most theorem-shaped fact (law-theory
P1 says so; HA prices it in days; DG has already run the confirming node census).

**(b) The marginal law (π²/2)ln(eT*/t)** — law-theory measured the coefficient at
0.98–1.04 × π²/2 across nine (t, L) points for t ≲ 0.6 eT* (no fitted parameters);
HA's H2 supplies the proof mechanism in two stages: (i) an exact rank-two secular
identity (days; same-day stress test P3 specified) reducing the worth to
ln(1 + 2|ψ̂₋(t₀)|²/λ₋), and (ii) the defect-potential computation where π²/2 is the
Landau–Widom/Bonami–Karoui exponent unit (per the prior-art transcriptions). Precis
item 2 verified. Caveat both seats state: the worth is NOT additive over zeros
(law-theory: additive model fails the α-derivative by 3.4×; sums overshoot ~20%) —
the lemma must stay strictly marginal.

**(c) The invariant law** — number theory's deficit measure (total mass exactly
e^{ℓ}), law-theory's E = −A + b[N(T*) + μD(T*)], and DG's excess-area action are
reconciled in §2 below: **NT and law-theory are algebraically the SAME functional;
DG's action is the same curve iff its stopping height drifts with L** — and the deep
data turns that drift into the discriminating question. Precis item 3 answered in §2.

**(d) Density-not-arithmetic** — DG-3 (|Δ ln λ| ≤ C₀·ℓ·(D+1) under counting
discrepancy D; jitter-tested, empirical Lipschitz 1.0–2.3 at ℓ = 1.24, an order of
magnitude inside the claim; finite core certifiable by rank-2 interval updates, i.e.
Lean-adjacent) + NT-2 (displacement form; the unconditional 10-line input
|γ_k − γ̂_k| ≤ C from Trudgian's S(T) bound) + the §2.17 mechanism experiment.
Precis item 4 verified, with two refinements: (i) NT-2's stated bound
(C₁(1+Δ)e^{ℓ·2/…} = O(e^{L/2})) is much WEAKER than DG-3's O(ℓ) — they have different
hypotheses (displacement vs counting discrepancy); the merged target (§3, T3) takes
DG-3's form with NT-2's unconditional input; (ii) CO-2(e)'s preconditioning negative
result is the mandatory rider: **the value-law is a density functional, the
form-equivalence is arithmetic** (relative margin against the smooth-staircase frame
is 2.6e-5, not O(1) — the two forms' keyholes sit at different points). Any statement
of "density, not arithmetic" without this rider now overclaims.

**(e) The certificate/duality cluster** — the tightest cross-seat agreement in the
panel, three independent derivations of one floor:
- CS-1(v) and CO-2 derive the SAME precision floor δ < λ/‖v‖₁² (CS by the adversary
  sign-matrix, CO with the sharp constant and gap correction, measured ratio 0.997);
  CT's Lemma 4 is the same floor in category dress, verified across all four Lean
  rungs (slack 6.3e11 → 47, collapsing onto the floor as predicted).
- The floor is now MEASURED at the fifth window: this session's δ* = 4.49e-21 at
  (711/200, m=40). Program law going forward: every ball certificate prices at
  δ < λ/‖v‖₁², with ‖v‖₁² drifting slowly (2.35 → 3.04 → 3.51 → 4.01 measured at
  L = 1.75/2.485/2.996/3.555).
- CS-1/CS-2 (bit growth digits(c) ≈ 0.21·m²·DENP, measured 0.994–1.043 of model at
  m = 16/24/48; the compilation contract whose hypothesis (H3) is exactly the
  pathology-#5 failure mode) + NA Lemma 4(ii) (rounded-Cholesky inequality
  certificates, LINEAR in depth instead of m²·DENP — the single biggest design win
  available: ~25-digit integers where 30,319-digit ones ship today) + CT Lemma 3 (the
  Cert category; its coherence law found the real m=12 bridge breach that five
  per-artifact layers missed — now pathology #5, repaired, standing oracle) + AG-2(e)
  (curve-side integer certificates need NO bridge at all) + GT G4(A) (signing
  rigidity: arithmetic all-plus is the unique positive signing, 1 of 8 at L = 3.0 and
  1 of 32 at L = 4.04, wrong signings failing at O(10⁻¹)–O(1) against a +8e-7 margin).
  Precis item 5 verified except the artifact conflation corrected above.

**(f) The function-field laboratory** — AG-1 (exact staircase law
λ_C(L) = ln q · λ_min(T_{n(L)}(μ_C)); verified to six digits on E/F₅ (rung
1.059588 = (2 − 3/√5)ln 5) and genus-2/F₇ (3.891820, 3.002638); wall at 2r·ln q),
AG-2 (function-field UPT = Cayley–Hamilton; uniformity IS dim H¹ < ∞; the kernel
vector IS the L-polynomial — the exact statement of which the keyhole is the
ℚ-shadow), AG-3 (spliced ladder toward RvM density), AG-4 + NT-1(e)(4) (USp(2g)
calibration; the measured CDF exponent 1.50 has a provable symplectic counterpart),
and the Ihara margin-meter. Precis item 6 verified with one credit correction: the
Ihara interface is AG's offer (AG §4); the graph-theory seat explicitly declined
composition with AG ("no composition claimed" — its honest §5). AG's own §5 lists the
four degenerations that make the curve solvable; the two miracles ℚ must manufacture
are the archimedean glide (no curve counterpart) and uniformity-without-finiteness.

**(g) The UPT residue, named identically by three seats that cannot prove it**:
CT §1 ("UPT = gauge comparison against a zeta-free model ladder + a recursion
generator"), CO-3 ("the arithmetic trajectory rides the boundary of the positivity
cone"; endpoint distances = envelope; the residue pinch 3e-10 at L = 2.485; the
CC-rigidity refinement 10⁻³ → 1.5e-8), GT G3(ii) (the leverage Gram after envelope
normalization; τ-sums cross 1 near L ≈ 5.3 so no triangle-inequality assembly
survives). Three notations, one open lemma; none of the nine plans claims a route
through it, and all five "honest assessment" sections that touch it say so plainly.

### 1.2 Conflicts (adjudicated in §6)

1. **Bend vs bias** (deep-windows verdict (ii) vs numerical analysis' Rayleigh–Ritz
   bias claim) — the panel's sharpest live conflict; evidence now split BOTH ways
   (§6, Q1). The deep-windows INTERIM claim "convergence bias is excluded" is
   overclaimed relative to its own post-interim runs.csv: at L = 4.25 the m=128→144
   decrement INCREASED (5.4303 → 5.2589e-35, past the quoted Aitken limit 5.42e-35);
   L = 4.75 dropped 7.3× from m=128 to m=144/160 (1.488e-46 → 2.040e-47 → 1.864e-47);
   L = 5.0 is still plunging (2.94e-53 at m=144 → 7.01e-55 at m=176). Meanwhile the
   bend side's strongest card stands: pairwise deep slopes 12.56/12.43 per unit
   e^{ℓ} against 4π = 12.566 (0.1–1%).
2. **The value of b**: NT-P1 (converged deep b_eff rises back to 1.755 ± 0.02) vs
   law-theory (1.755 was a degenerate-fit parameter; deformation-invariant
   b = 1.51 ± 0.06, c₀ = 5.04) vs the deep 4π cap. NT-P1 is already under pressure
   (deep Aitken b_eff ≈ 1.72–1.74 and trending down, though not yet past NT's own
   1.70 falsifier); law-theory's deformation methodology is the stronger instrument
   (it BROKE the degeneracy rather than refitting inside it).
3. **NT-2 vs DG-3 bound strength** — not a contradiction (different hypotheses) but a
   merge obligation; resolved in T3.
4. **Smooth-vs-true factor 6.3 at L = 3.555** (true 9.909e-22 vs smooth 1.577e-22 at
   Gcut = 420) — flagged by NT (§5) and law-theory (caveats); sits directly under
   T3's sharp form. Adjudication Q3.
5. **Precis corrections summary**: item 5's Lean-artifact parenthetical (corrected
   above); item 6's Ihara credit (AG, not GT); item 1's "days" applies to H1(i) only;
   item 7's prolate kill needs the scope note of §5 (K2) — the deep-regime Fuchs cap
   is NOT killed, it is Q1's live hypothesis.

---

## 2. The unified law

Coordinator's question 3: are law-theory's E = −A + b[N(T*) + μD(T*)], number
theory's deficit-measure reading, and DG's excess-area action the same functional?
**Answer: the first two are identical by elementary algebra; the third is a
reparameterization that coincides on the measured range and DIVERGES from the fixed-
(b, c₀) form asymptotically — and the deep-windows data is precisely the
discriminator between them.** The algebra, explicitly:

**(i) Law-theory ≡ its own invariant form.** With T* = 2πe^{ℓ}:
N(T*) = e^{ℓ}(ℓ−1) + 7/8 and D(T*) = (a/π)T* − N(T*) = e^{ℓ} − 7/8. So
N(T*) + μD(T*) = e^{ℓ}(ℓ − 1 + μ) + O(1) = e^{ℓ}(ℓ + c₀) + O(1) with **μ = c₀ + 1**
— exactly law-theory §4. ✓

**(ii) Number theory ≡ law-theory.** NT's deficit measure dμ_L = [a/π − ρ(t)]₊dt has
total mass ∫₀^{T*}(1/2π)ln(T*/t)dt = T*/2π = e^{ℓ} exactly — i.e. **NT's total
deficit mass IS D(T*)** (up to the 7/8). NT's closed form
(T/2π)(ln(T/2π)+4) = N̂(T) + 5·T/2π − 7/8 is an exact identity (check:
N̂ + 5T/2π − 7/8 = (T/2π)(ln(T/2π) − 1 + 5) ✓), i.e. NT's b = 1.755, "+4" reading is
the (b, μ) = (1.755, 5) member of law-theory's family E = −A + b·N(T*) + bμ·D(T*).
Law-theory's deformation experiments then break the (b, c₀) degeneracy that the
L-scan alone cannot see and select (b, μ) = (1.51 ± 0.06, 6.0–6.7) over (1.755, 5):
same functional, sharper coordinates. **NT and law-theory are one law.** The unified
mid-range statement of record:

  **E(L) = −A + b·[N(T*) + μ·D(T*)],  A = 11.1–11.8, b = 1.39–1.51, μ = 6.0–6.7**
  (cleanest single determination (A, b, c₀=μ−1) = (11.13, 1.509, 5.04); the repo's
  (10.2, 1.755, 4.0) is the same curve on the old fit window to ±0.01),

with β-linearity (E + A degree-1 homogeneous in the height scale) proved to be the
family/conductor universality (law-theory §4.1, HA H4(i)'s exact dilation
covariance, CT Lemma 2's scale invariance — three seats, one mechanism).

**(iii) DG's action is the same object through one further identity.** DG's excess
area obeys (elementary, verified here):

  2A(T; L) = 2π[D(T*) − D(T)],

so DG's "exponent = twice the excess area up to a stopping height T_s = e^{w}T*"
reads **E + A = 2π[D(T*) − D(T_s(L))] = T*·(e^{w}(w−1) + 1)**. Two immediate
consequences. First, DG's lower-bound construction (dodge all quantiles to eT*)
gives value 2A(eT*) = 2πD(T*) − 0 = T*, i.e. **the capacity endpoint eT* = the zero
of D = law-theory's §2.3** — the clusters interlock exactly. Second, with a FIXED w
this form is pure b′e^{ℓ} (no ℓ-factor): the measured (ℓ + c₀) growth is carried
ENTIRELY by a stopping height that drifts, w(L) solving
e^{w}(w−1) = (b/2π)(ℓ + c₀) − 1. Checked against DG's own numbers: at ℓ = 0.875 this
gives w = 1.12, at ℓ = 2.25 w = 1.22 — DG's quoted band [1.11, 1.22] exactly. So on
the measured range all three parameterizations are one curve; DG's is not an
independent confirmation but a change of variables — with one genuinely new degree
of freedom (the stopping height) that becomes decisive asymptotically:

**(iv) The discriminating data point.** If the (ℓ + c₀) growth persists, w(L) → ∞
(and eventually collides with DG's Jensen ceiling 2π(e²+1)e^{ℓ} at ℓ ≈ 26 — DG's own
flagged internal tension). If instead the stopping height SATURATES at the value
w∞ = 1.2785 solving e^{w}(w−1) = 1 (T_s → 3.59·T*), then dE/dc caps at exactly
**2π·(e^{w∞}(w∞−1)+1) = 4π per unit c = e^{ℓ}** — which is the Fuchs/prolate
universal rate the deep-windows agent reports at L ≥ 4.25 (pairwise slopes
12.56/12.43 vs 4π = 12.566), with the crossover where the mid-range local slope
b(ℓ + c₀ + 1) reaches 4π: L = 4.32 with (1.755, 4), L = 4.56 with (1.51, 5.04) —
bracketing exactly where the measured deviations begin (+0.90 nats at L = 4.25).
**The unified candidate law, mid-range and deep in one formula:**

  E(L) + A = 2π[D(T*) − D(e^{w(L)}T*)], w(L) drifting per (iii) then saturating at
  w∞ ≈ 1.28,

which simultaneously: reproduces the three-constant law on the measured range,
resolves DG's Jensen-ceiling tension (4π e^{ℓ} sits inside [2πe^{ℓ}, 52.7e^{ℓ}]
forever), and reproduces the Fuchs cap. It is a HYPOTHESIS, not a finding: whether
w saturates is exactly the bend-vs-bias question (Q1), and it now has a
mechanism-level test that bypasses fit degeneracy entirely — measure the stopping
height on the deep minimizers directly (composite C4, §4). If Q1 resolves "bias",
the saturation clause is deleted and the fixed-(b, μ) invariant form of (ii) stands
alone; either way the mid-range algebra of (i)–(ii) is settled now.

---

## 3. Top five proof targets

Ranked by provability × program value. Format: merged statement / composite route
(seat → step) / hardest step + owner / difficulty / pre-proof stress test.

### T1. The Capacity Endpoint Theorem (eT* is the exact horizon)

**Merged statement** (best of HA-H1, law-theory-P1, DG-2.2): Let Λ_sm be the smooth
staircase, a > 0, F = φ̂ with φ ∈ L²[−a, a], φ ≠ 0. (i) [hard horizon] For every
δ > 0 there is a₀(δ): for a ≥ a₀, F cannot vanish on all of Λ_sm ∩ [0, (1+δ)eT*].
(ii) [effective horizon] If ‖φ‖ = 1 and Σ_Λ|F|² = e^{−E} with E ≥ C·a·e^{2a}, then F
has N_sm(T)(1 − o(1)) near-real zeros through every T ≤ (1−δ)eT*, and its node count
saturates the type budget aT/π (not the zero count). (iii) [worth support] the
single-zero marginal worth vanishes beyond eT*: E_Λ = E_{Λ∩[0,eT*]} + O(a·small).

**Composite route**: NT supplies the classical inputs in citable constants-explicit
form (Levinson/Polya density, Jensen with L²-normalization, the displacement license
|γ_k − γ̂_k| ≤ C from Trudgian) → HA owns the proof of (i) (its own price: days) and
the Turán–Nazarov block machinery for (ii) → DG contributes the node-budget
verification (already executed at L = 2.485 and 1.75: nodes 13 vs budget 13.8 vs
zero-count 16.5) and the canonical-system reading → law-theory's RUN-4 is the
measured target (support endpoint at eT* at both L, the (eT*−t)^{3/2} softening).

**Hardest step + owner**: the lattice-adapted Turán lemma for (ii) — keeping the
per-block loss at O(m ln m) so the total stays o(E); HA owns it (it is also H3's and
H1(iii)'s shared wall). (i) has no hard step.

**Difficulty**: (i) days–weeks; (ii) weeks–months; (iii) with vanishing loss: months.
(i) alone is already the program's first provable NEW theorem: unconditional, about
an explicit arithmetic-free object, and it fixes the "+c₀" semantics (the exponent
integrates structure to eT*, not T*).

**Pre-proof stress test**: HA H1(e)(2) zero-tracking (count F's real zeros against
N_sm through 1.2·eT* on the true minimizer at L = 2.485, m = 64) + HA P2's
edge-narrowing (u½ at L = 3.4: turning-point predicts [2.2, 2.5], fixed profile
2.0 ± 0.1) + the (1+δ)-window worth check.

### T2. The function-field exact ladder, certified and formalized

**Merged statement** (AG-1 + AG-2(i),(iii),(iv) + the Lean rung + GT-G4(A)-on-curves):
(1) the staircase law λ_C(L) = ln q·λ_min(T_{n(L)}(μ_C)) with jumps at 2n·ln q, wall
at 2r·ln q, and the equivalence RH_C ⟺ all T_n ⪰ 0 (with finite integer certificates
of falsity); (2) function-field UPT with provenance: cᵀT_n c = Tr(x_c x_c†|H¹) ≥ 0
(Castelnuovo/Rosati), kernel first at n = 2g+1 with kernel vector = the L-polynomial;
uniform constant c_C = λ_min(T_{2g}) — uniformity IS dim H¹ < ∞; (3) genus-1 closed
form (margin = Frobenius discriminant / Hasse slack); (4) a kernel-checked Lean
certificate for a named curve (T_n over ℤ[√q]; integer congruence format of
`lean/weilcert` with NO bridge proposition — the identification is exact point
counting), plus the signing-rigidity companion on the curve.

**Composite route**: AG owns (1)–(3) (proof sketches complete; six-digit numerical
verification already run) → CS/Lean seat instantiates (4) through `CertFramework`
(AG estimates a weekend; CS-1 prices it — trivial next to the ζ rungs) → GT's G4(A)
machinery transplants for the signing companion → NT checks the ledger normalization
and supplies the Katz–Sarnak inputs for the AG-4 family laws → the curve-side
`oracle.py` (ten lines, both sides finite sums) imports the repo's oracle discipline.

**Hardest step + owner**: none for (1)–(4) as stated (AG: "theorem-with-complete-
proof-sketch, ready to be written"). The sharp Christoffel version of AG-2(ii) is
weeks and optional.

**Difficulty**: days-to-weeks total. The highest provability on the board, and the
value is not decoration: it is the calibration world for C1 (§4), the first
kernel-checked RH-margin of any global object, and the exact statement of what
uniformity IS (finiteness) — the axiom UPT must replace.

**Pre-proof stress test**: AG-P1 reproduction by repo instruments (kill criterion:
any CONVERGED smooth inter-threshold decay or nonzero converged margin past
2r·ln q kills the dictionary); AG-4(e)'s point-counting afternoon for the family
CDFs (measures the wall-margin tail exponent before anyone proves it).

### T3. The Rigidity Transfer Theorem (density-not-arithmetic, made a theorem)

**Merged statement** (DG-3 form, NT-2 input, CO-2(e) rider): Let μ₁, μ₂ be symmetric
point measures with sup_{T ≤ e²T*}|N₁ − N₂| ≤ D, both of log-type density. Then
|ln λ[μ₁](L) − ln λ[μ₂](L)| ≤ C₀·ℓ·(D + 1). Corollaries: (i) with
D = sup|S(T)| (unconditional, Trudgian), the envelope transfers between ζ and the
smooth staircase with O(ℓ) offset — upgrading §2.17 from measurement to theorem;
(ii) Poisson's D ≍ √(N ln ln N) predicts its measured super-constant, sub-exponent
cost (−4.5 nats); (iii) [rider, CO-2(e)] the transfer is of VALUES only: no
form-level equivalence follows, and none exists (λ_rel = 2.6e-5).

**Composite route**: DG owns the transplantation proof (Blaschke-free products +
Levin perturbed-sine estimates; its jitter stress test already run, order-of-
magnitude slack) → HA supplies the Levin/Avdonin machinery and the exceptional-set
control near coincidences (NT-2(c)'s leak point) → NT supplies the S(T) constants
and the displacement corollary (its 10-line lemma) → NA/Lean certify the finite core
(Lipschitz of a fixed Galerkin section under sample-point motion via rank-2 interval
updates — DG names it the natural next kernel-checked statement after
`weil_window_positive`).

**Hardest step + owner**: the floor-zone comparison at log scale (the minimizer's
ridge structure interleaving with both sequences; a polynomial-in-K loss is fatal,
e^{CDℓ} is fine) — DG owns, with HA's Levin toolbox.

**Difficulty**: months, self-contained; DG's own assessment "highest
value-per-effort in this plan" — the panel agrees: it is the license for T1/T5 to
transfer from the staircase to ζ, the Hilbert–Pólya constraint table's foundation,
and the most provable statement in the precis' item-4 cluster.

**Pre-proof stress test**: repeat the jitter experiment at L = 2.996 (tests
C(ℓ) ∝ ℓ); the GUE point (DG-P3/NT-P2: predicted within ~2 nats of true, ≥ 3× closer
in log to smooth than to Poisson); Q3's resolution (the factor-6.3 anomaly at
L = 3.555 must be shown to be truncation, or the sharp form is in trouble).

### T4. The Marginal Law (π²/2 as the first derived constant)

**Merged statement** (H2 + law-theory RUN-4): (i) [identity, unconditional in the
model] λ is the smallest root of the 2×2 secular equation in the rank-two update of
the deleted pair; whenever the pair-coupling is gap-small,
f(t₀) = ln(1 + 2|ψ̂₋(t₀)|²_pair/λ₋) + explicit gap corrections. (ii) [profile] for
the graded staircase, |ψ̂₋(t₀)|²/λ₋ = (eT*/t₀)^{π²/2 + o(1)} for t₀ ≤ (1−δ)eT* —
equivalently f(t₀) = (π²/2)(1+o(1))ln(eT*/t₀), the measured 0.98–1.04 plateau.

**Composite route**: HA owns both parts (H2) → law-theory's frame builder is the
instrument and its nine-point measurement the target → NA runs the same-day P3
closure test (at t₀ = 20.7, L = 2.485: e^{ΔE} − 1 vs 2|ψ̂₋|²/λ₋ within 25%) → AG's
curve-side deletion (an exact Toeplitz difference) calibrates the non-additivity
where truth is known (composite C1).

**Hardest step + owner**: the constant (not the shape): gluing gap potentials over
~e^{2a} gaps with summable errors — a new equilibrium computation for the graded
lattice with one defect; HA owns. BK's corridor is too wide for the constant.

**Difficulty**: (i) days; shape with π²/2 in a corridor: weeks; the constant: months.
Program value: the first envelope constant DERIVED rather than fitted, and the
mechanism quantum (per-zero worth) for everything else; also the cleanest test that
the seat's machinery predicts the NEXT decade of ln(eT*/t) rather than fitting the
measured one (HA's own risk note).

**Pre-proof stress test**: H2(e) as specified (P3 falsifier at > 40% forces the full
secular treatment and would undercut the perturbative route).

### T5. The two-sided envelope sandwich (the law as a theorem for the density class)

**Merged statement** (DG-2.3 bracket → H3 shape → law-theory P4 construction): for
the staircase (and any R-rigid sequence, R in the constants), explicit
0 < b₁ ≤ b₂, c₂ with

  b₁·a·e^{2a}(1 − C/ln a) ≤ E(a) ≤ b₂·e^{2a}(2a + c₂),

the upper bound carrying the measured (2a + c₀) shape via the canonical-product ×
prolate-window ansatz with SHARED suppression (the ~20% interaction is automatic in
the product potential, per H3's design); stage-0 form (DG-2.3, cruder but
constants-now): 2π e^{ℓ}(1−o(1)) ≤ E ≤ 2π(e²+1)e^{ℓ}(1+o(1)).

**Composite route**: DG proves stage 0 (Levin sine-type lower construction + Jensen
budget upper — months, publishable alone) → HA proves the shaped upper (BM-corrector
bookkeeping; weeks–months) and attacks the a·e^{2a} lower (Turán blocks — shares
T1(ii)'s wall) → law-theory P4's numerical implementation of the ansatz is the
cheapest kill test (if E_ansatz misses by a growing factor, the whole product/chirp
picture dies) → T3 transfers the result to ζ → CT's model-ladder gauge consumes it:
with T5 proved, UPT factors cleanly as [proved envelope of a zeta-free ladder] ×
[one comparison constant c], which is the program's §3 normalization made exact.

**Hardest step + owner**: the lower bound's per-block constant (the same
lattice-adapted Turán lemma as T1(ii)/H1(c) — one wall, three payoffs); HA owns.
Matching b₁ = b₂ (deriving b) is explicitly OUT of scope: law-theory §2.2 proved
every bulk assignment fails; the constant must come through T4's defect calculus or
Q1's resolution.

**Difficulty**: stage 0: months; shaped upper: weeks–months; matched constants:
research program.

**Pre-proof stress test**: H3(e) (the ansatz evaluated at L = 2.485/2.996 against
E = 21.8/33.1 with the δ-scan's interior optimum); DG-2(e)'s envelope-descent
signatures on the true minimizer (P1: drop −5.4 ± 0.8 at 2T*, L = 2.996).

**Bench note** (not ranked, but the panel's consensus falsifier): any candidate
transfer inequality produced under T1–T5 must be run against GT's signing polytope
(31 wrong signings at L = 4.04) and CO-3's certified interval ledger before anyone
invests in it — an inequality that also "certifies" a wrong signing is refuted in
minutes (GT §4's offer; the 1-of-32 ground truth).

---

## 4. Cross-expert composite lemmas

New statements no single seat proposed, each jointly enabled by two-plus seats.

### C1. The function-field marginal law (π²/2 in the world where RH is a theorem)

**Statement.** Let C/F_q have distinct Frobenius angles; for an angle pair ±θ_j
define the deletion worth f_C(θ_j; n) = ln λ_min(T_n(μ_C)) − ln λ_min(T_n(μ_C minus
the pair)). Then (i) [exact, finite] f_C is given by H2(i)'s rank-two secular
identity applied to the Zak-fiber Toeplitz matrix — a closed-form finite computation
(AG-1's reduction makes the deleted-pair resolvent explicit); (ii) [the ladder] for
AG-3(ii)'s spliced quasi-periodic sets converging to the RvM density, the deletion
worth of a node at scaled height t converges to (π²/2)·ln(t_cap/t) with t_cap the
splice's capacity height — i.e. the π²/2 profile PROVED first on the solvable end,
with the lattice limit (pure periodic, AG-3(i)) correctly giving worth ≡ 0 (zero
toll at constant density = law-theory §2.1's exact dichotomy).
**Enabled by**: AG (Zak reduction, spliced models) × HA (rank-two identity, defect
potential) × law-theory (measured target + the AP dichotomy as the calibration
anchor) × NA (instrument). **First test**: measure f_C on the genus-2/F₇ curve
against the exact Toeplitz difference (calibrates non-additivity where truth is
known — the control experiment AG-P3 asked for, now with H2's identity as the
instrument).

### C2. Certified dual-witness extraction as a Lean theorem

**Statement.** For the (L = 497/200, m = 12 or 24) window there exist rational nodes
0 < t₁ < … < t_r and rational weights w_j > 0 (r ≤ m) together with a kernel-verified
proof that (a) A/DEN − Σ_j w_j E_rat(t_j) is entrywise within a certified δ'' of a
PSD matrix (E_rat(t_j) = rationalized frame matrices with certified spherical-Bessel
tails), hence (b) the certified window margin is WITNESSED by a positive quadrature,
and (c) the nodes satisfy |t₁ − 14.1347| + |t₂ − 21.0220| ≤ stated bounds. The first
formal artifact whose mathematical CONTENT is the zeros themselves (Groskin-adjacent,
but kernel-checked), and the first dual-side certificate: O(N(T*)) numbers against
O(m²) for the primal.
**Enabled by**: CO (CO-1's witness theory + the executed blind NNLS extraction:
centroid 14.079 weight 2.047 with no zero information supplied) × NA (Lemma 4(ii)'s
inequality-form kernel checking — the enabling Lean technology) × CS (CS-2's
compilation contract and size pricing) × the Lean framework (`CertFramework`).
**First test**: rationalize the existing NNLS witness at m = 12 and check (a) in
interval arithmetic before any Lean is written.

### C3. The capacity endpoint in the de Branges chain

**Statement.** Let H_sm be the canonical system with spectral measure μ_sm (DG-1)
and B(E_τ) its chain. Then the type-a member has exact sampling horizon eT*(a):
(i) any element of B(E_a) vanishing on supp μ_sm ∩ [0, (1+δ)eT*] is zero (T1(i) in
chain language, via the chain/PW norm equivalence of DG-1.1); (ii) the Weyl-disk
rotation of H_sm at spectral parameter t exhausts the type-a budget at
t = eT*(1 + o(1)), the turning-point coordinate being x*(t) = ½ln(t/2π); (iii) the
defect-worth profile acquires an Airy zone at the capacity edge whose relative width
shrinks like (a·eT*)^{−2/3} — the (eT* − t)^{3/2} softening law-theory measured at
two points, now with a scaling prediction (HA-P2).
**Enabled by**: HA (H1 + H4(ii)'s screw-function bridge to Suzuki's normalization) ×
DG (DG-1's normal form and the chain machinery) × NT (S(T) transfer). **Value**:
plants the program's first new theorem inside the exact structure (canonical
systems) where any Hilbert–Pólya candidate must live, and makes the capacity
endpoint a constraint on the candidate's Hamiltonian, not just on its counting
function. **First test**: H4(e)'s Jacobian cross-check of the screw-kernel section
at one L; then HA-P2's four surgeries at L = 3.4.

### C4. The saturating-stopping-height law (one formula for mid-range and deep)

**Statement.** E(L) + A = 2π[D(T*) − D(e^{w(L)}T*)] where w(L) is the standoff
height of the minimizer's descent; mid-range, w(L) solves
e^{w}(w−1) = (b/2π)(ℓ+c₀) − 1 (measured band 1.11–1.22, reproducing the
three-constant law exactly, §2(iii)); deep, w(L) ↑ w∞ = 1.2785 (the root of
e^{w}(w−1) = 1), equivalently dE/dc → 4π — the Fuchs cap — with crossover at
L ∈ [4.3, 4.6]. **Discriminating measurement, fit-free**: extract the stopping
height directly from the deep minimizers (DG-2(e)'s envelope-extraction utility on
the L = 4.25/4.5/4.6 vectors): saturation at ≈ 3.6T* confirms the bend as mechanism;
continued drift refutes it — no envelope fitting, no Rayleigh–Ritz degeneracy in the
answer.
**Enabled by**: DG (action identity + extraction tool) × law-theory (invariant
constants) × deep-windows (the ladders) × HA (the Airy/turning-point layer at the
standoff). No seat proposed connecting the bend question to the stopping-height
observable; the identity 2A = 2π[D(T*) − D(T_s)] (§2) is what makes it a
one-experiment discriminator.

### C5. Kernel-checked arithmetic-signing rigidity (the 1-of-32 theorem, formal)

**Statement.** At L = 497/200 on the certified 12-dimensional space: for every
signing σ ≠ all-plus of the prime-power bands, a kernel-verified rational witness
vector x_σ with x_σᵀ Q^σ x_σ < 0 — jointly with the existing positivity certificate:
"on this window the positivity cone of the signing polytope is exactly the
arithmetic vertex", machine-checked. Extends the flagship artifact from "the
arithmetic form is positive" to "positivity is a measure-zero conspiracy in sign
space" — the program's sharpest structural fact about WHY ensemble/averaging methods
cannot see it (GT §5's warning, made a theorem).
**Enabled by**: GT (G4(A), sweep executed at float level: unique positive 1/8 and
1/32, wrong signings at −0.25 to −2.67) × NA/CO (interval Rayleigh upper bounds, one
vector per signing — minutes each) × Lean (`CertFramework` re-derivation; witness
format is a single rational vector per signing, far lighter than the positivity
side). **First test**: GT's (e)(α) spectral-basis re-run at m ≥ 32 to fix the
witness vectors.

---

## 5. The kill list (program law; refuting evidence cited)

K1. **The corner-kink creep mechanism is dead.** Pre-registered kink-enrichment
experiment (PLAN-numerical-analysis L1/L2(e), 2026-07-26): snap enrichment 24+4
lands at 3.7403e-10, ABOVE plain m = 32 (3.5709e-10); Model K refuted; the creep is
a log-regularized truncation-jump effect Θ(A_L/(m ln m)). RESULTS.md's revision note
already adopts this. Law: the phrase "interior derivative kinks" is retired; the
route to operator margins is hp geometric grading, not snap functions.

K2. **Bulk prolate/Landau–Widom derivation of the mid-range constants is dead.**
law-theory §2.0–2.2: replacing the zero sum by the density integral makes λ order
one (the margin is a DISCRETENESS effect); every bulk functional (M0 area-deficit,
LW plunge, Fuchs concentration) fails in size AND shape (Fuchs: 14.98 vs measured
21.99 at L = 2.485, optimum never engaging the staircase). **Scope note (required)**:
this kills BULK derivations of (b, c₀) in the mid-range. It does NOT kill (a) the
defect-mode use of the LW/BK constant (T4's π²/2 route — the constant appears in the
rank-one-removal derivative, exactly where law-theory measured it), nor (b) the
deep-regime Fuchs 4π cap, which is Q1's live hypothesis.

K3. **The expander-mixing/positivity-transfer angle is dead**, by its own seat's
verdict (PLAN-graph-theory §5): the divisibility graph is an amenable Cayley graph
(no gap exists to be found); the mixing inequality's "error term" IS the zero-side
frame — the explicit formula restated. Honest residue: G2's unconditional floor
λ(L) ≥ −C·e^{L/4 − c√(L/2)} (worth finishing; weeks) and the tier map.

K4. **Envelope-preconditioning at FORM level is dead.** CO-2(e): the relative margin
against the smooth-staircase frame is 2.6e-5, not O(1); bounded relative
certificates would need the true zeros to sub-spacing accuracy (circular). Law: the
envelope divides out of the VALUE, never of the FORM; Track B's bounded per-window
certificates do not exist in any density-normalized format. (Value-level gauges —
CT's model ladder, law-theory's E + A homogeneity — are untouched.)

K5. **The 2 ln j₀ numerology is dead.** b = 1.755 ≈ 2 ln j₀ = 1.75530 was a
degenerate-fit coincidence: the deformation experiments select the invariant
b = 1.51 ± 0.06 (law-theory §3.3); HA §3 records it as "the program's cleanest
example of four-digit numerology manufactured by a parameter-degenerate fit". Law:
no constant identification from the L-scan alone; deformation (or derivation) or it
does not count.

K6. **Threshold knife-edge / threshold-distance normalizations are doubly dead**
(pre-panel, restated because plans still brush it): operator-level non-collapse
(RESULTS §threshold) + Glide Theorem; CT prediction 1: any N_p referencing
dist(L, ∂W_p) or absolute window position violates proved facts.

K7. **Constant-toll-per-zero / additive per-zero accounting is dead**: 20× misfit
(RESULTS) and law-theory §3.3–3.4 (additive functional built from the MEASURED
marginal profile still fails the α-derivative by 3.4×; marginal sums overshoot by
~20%). Law: zero–zero interactions are essential; upper-bound constructions must
share suppression (T5's design).

K8. **Keyhole-as-discovery stays dead** (Groskin arXiv:2605.20224, prior art;
RESULTS diligence). All keyhole/node phenomena are validated-pipeline confirmations.
CO-1(e)'s witness extractions inherit this caveat by CO's own statement.

---

## 6. Adjudication queue

Q1. **Bend vs bias (THE priority).** Deep-windows verdict (ii) vs NA's
Rayleigh–Ritz-bias claim. Current evidence, both sides: FOR the bend — deviations
+0.90/+1.53/+1.92 nats at L = 4.25/4.50/4.60 with pairwise slopes at 4π to 0.1–1%;
AGAINST — post-interim runs.csv shows the L = 4.25 decrement INCREASING at m = 144
(5.2589e-35, below the quoted Aitken limit), L = 4.75 falling 7.3× (m=128→160),
L = 5.0 still falling 42× per step (7.008e-55 at m = 176); fit_report's own
creep-model floors carry the flag "C overestimated, conservative"; and the fitted-b
collapse across F1→F3 (1.66 → 1.31 → 1.05) is exactly NA's predicted bias signature.
**Settling program**: (a) NA's creep-corrected joint fit λ_m = λ + A_L/(m ln m) over
the full runs.csv (no new compute); (b) finish the L = 4.75/5.00 ladders and land
L = 5.50 (also Q2); (c) one hp-graded-basis run at L = 4.5 (NA L2(ii)) to break the
single-basis-family degeneracy; (d) the fit-free discriminator: C4's stopping-height
extraction on the existing deep minimizers. Decision rule: bend is confirmed only if
(a), (c) and (d) agree.

Q2. **Connes/Groskin normalization (precis tension 1) — still OPEN.** The L = 5.5
triple (152/168/184) never landed; runs.csv confirms. Separation at stake: old law
9.0e-77 vs Fuchs-form/comparator ≈ 1e-70..-74 (anchored at L = 4.6, ≈ 3.7e-55 at
L = 5.0 vs law 1.2e-56; the m = 176 value 7.0e-55 is nearer the Fuchs form but
unconverged). Keep the 30%-drift m = 200 contingency.

Q3. **The smooth-vs-true factor 6.3 at L = 3.555 (precis tension 2).** True
9.909e-22 vs smooth 1.577e-22 at (Gcut = 420, m = 48) — the true zeros BEAT the
staircase by 6× exactly where lower L shows near-equality. Settling experiment:
law-theory's exact-Bessel builder (100× faster) at Gcut = 840/1680/3360, m = 64,
both sequences; plus the GUE point (Q6) at the same configuration. If the excess
survives Gcut → ∞, the rigidity offset GROWS with L — T3's sharp form and
law-theory §3.5's shared-constants claim both need repair; if it dies, it was
differential frame-truncation convergence, and NT-2/DG-3 proceed as stated.

Q4. **The value of b (three-way).** NT-P1 (deep b_eff → 1.755 ± 0.02) vs law-theory
(1.51 ± 0.06 by deformation) vs 4π-cap (b loses meaning past L ≈ 4.3). Settling:
Q1's outcome + one deformation run (α-derivative) at L = 3.4 with the exact-Bessel
builder + frozen-parameter refits with the creep correction. Note NT-P1's own
falsifier (b_eff < 1.70) is close to firing on the Aitken limits (1.72–1.74,
descending).

Q5. **Certificate pricing — SETTLED this session.** δ* = λ/‖v‖₁² confirmed at the
fifth window (4.489e-21 at L = 711/200, m = 40; ‖v‖₁² = 4.009 in CO's predicted
band). Program law: (i) every future ball certificate prices at δ < λ/‖v‖₁², CO-2/
CS-1(v) jointly canonical; (ii) no δ ≥ 1e-20 ball certificate can ever exist at the
p = 5 window; (iii) the precis' artifact conflict is void (no Lean rung exists at
711/200; `WeilcertDeeper`'s δ = 1e-19 at 749/250 has 10⁴× headroom). Remaining
cheap check: CO-P2(a)'s claim of ~12 orders of unused headroom at the m = 12 rung
(δ widenable to ~1.5e-8) — minutes, and it would let the flagship artifact be
re-shipped with an honest-size ball.

Q6. **The GUE rigidity point** (DG-P3 = NT-P2, same experiment, near-identical
bands: λ_GUE within ~1 order of true, ≥ 3× closer in log to smooth than Poisson).
One afternoon with a CUE sampler; falsifies or fixes the variance-controls-offset
mechanism under T3.

Q7. **Turning point vs fixed profile at the capacity edge** (HA-P2 vs H4(iii)):
u½ at L = 3.4 in [2.2, 2.5] (Airy) vs 2.0 ± 0.1 (fixed). Four RUN-4-style surgeries.
Feeds C3 and T1(ii)'s softening layer.

Q8. **MSS real-rootedness (GT-G4(B)) — refute-or-live for the interlacing angle.**
32 exact 12×12 characteristic polynomials at L = 497/200 (exact rational, cheap). A
real-rootedness failure closes the MSS door before anyone spends months on it;
GT-P1's Perron −γ constant at N = 10⁷ plus the Hilberdink prior-art check (NT owns
diligence) settles G1's novelty.

Q9. **AG dictionary gate**: repo-instrument reproduction of AG-P1's staircase
numbers (kill: converged inter-threshold decay); then the GL(2) port (NT-3(e)(3),
Ramanujan Δ — collapse on e^{L/4} vs e^{L/2}, ~28 orders of separation at L = 5,
one session, unmissable at m = 32) as the sharpest test of the analytic-conductor
scaling that AG-4/NT-3 and the family data all assume.

---

## 7. Allocation recommendation

Principle (from the convergence map): the program's provable frontier is entirely on
the density/staircase side plus the finite/certified side; the UPT residue is not
attackable by any seat this quarter, and the correct spend is to (1) bank the
theorems that are near-free, (2) settle the bend, because every deep-side plan
prices off the envelope's true asymptotic, and (3) re-tool the certificate pipeline
around the floors that are now law.

**Days 0–30** (bank the provable; settle the cheap adjudications):
- T1(i) hard horizon written and proved — HA seat, with NT supplying cited constants
  (co-owners of the writeup). Also HA's two-page AP-dichotomy lemma (law-theory
  §2.1) into THEOREMS.md — the calibration anchor, essentially free.
- T2 in full — AG seat writes AG-1/AG-2; CS+Lean seat builds the F₅ curve
  certificate through `CertFramework`; GT contributes the signing companion spec
  (C5). Target: first kernel-checked RH-margin of a global object inside the month.
- T4(i) rank-two identity + the same-day P3 closure test — HA + NA.
- Adjudications Q1(a,d), Q3, Q5-remainder, Q6, Q8, Q9-gate: NA seat (lead) +
  deep-windows re-engaged to land L = 4.75/5.0/5.5 (Q1(b)/Q2); DG runs the
  stopping-height extraction (C4) on the existing deep vectors.
- CO + NA: certified θ(L) ladder (CO-4 — the one-scalar disproof channel, easy) and
  certified interval-ledger endpoints (CO-3) at two windows.
- CS + Lean: adopt the rounded-Cholesky redesign decision (NA-L4(ii) vs CS-1(iii)
  per-column; recommendation: NA's inequality format — linear in depth — with CS's
  parity split; acceptance tests = CS-P1/P2).

**Days 30–60** (the medium theorems; the bend resolved):
- T3 full attempt — DG owner; HA (Levin/exceptional sets), NT (S(T) inputs), NA+Lean
  (certified finite core). This is the block most worth protecting from scope creep.
- T5 stage 0 (DG's bracket) + shaped upper bound (HA, with law-theory P4's numerics
  run first as the kill test).
- T1(ii) effective horizon — HA on the lattice-adapted Turán lemma (the shared wall;
  any progress pays into T1, T5, and H1(iii) simultaneously).
- C2 design + interval prototype (CO + NA); NT-4(i) quantitative converse Weil with
  the Davenport–Heilbronn calibration (NT — the repo owns a real off-line zero; this
  is the disproof channel's theory made explicit).
- Q4 closed with the creep-corrected refits; ENVELOPE.md revised to whichever law
  survived (this gates any outward communication of the law).

**Days 60–90** (the constants; the research walls, entered deliberately):
- T4(ii): the π²/2 derivation (HA), with C1's function-field calibration built first
  (AG + HA + NA) — prove it on the solvable end, then transfer the computation.
- C4 as theory: if Q1 confirmed the bend, derive the saturating standoff (DG obstacle
  problem + HA's BM technology — the type-loss o(e^{−ℓ}) wall is entered here and
  nowhere earlier); if Q1 refuted it, freeze (A, b, μ) = law-theory's values and
  restate M3 as deriving THOSE.
- C2 built as a Lean artifact (CS + Lean + CO).
- CT re-engaged at low load throughout as the program's bookkeeping conscience: the
  standing coherence oracle (already law), the nested-hp single-staircase instrument
  (Lemma 1(iv) — the basis on which the two historical misreadings cannot recur),
  and the step-certificate/NNO schema paper with Track B mining restricted to nested
  stages (CT prediction 5 + CO/CS pricing).
- GT at bounded load: finish G2's unconditional floor with NT's explicit constants
  (the tier map is genuinely useful to Track A budgeting); no further expander work.

**Seats by re-engagement weight**: HA (heaviest — owns the hard step of three of the
five targets), NA and DG (instrument spine + T3), AG (T2 + C1), NT (inputs,
diligence, GL(2)), CO (ledgers, duals, C2), CS+Lean (redesign + C2/C5), deep-windows
agent (Q1/Q2 completion), GT and CT (bounded, high leverage-per-day).

**What this buys if it all lands**: by day 90 the program would hold — as theorems —
the capacity endpoint, the function-field ladder with a formal rung, the rigidity
transfer, the marginal mechanism at least in shape, and a two-sided envelope; the
law's asymptotic form settled by measurement; and a certificate pipeline priced at
its information-theoretic floor. None of that is UPT. All of it is the perimeter
UPT will be stated on, and every plan in this panel — by its own honest
assessment — agrees that is the correct next spend.


---

# COORDINATOR'S ERRATA AND ROUND-2 LEDGER (appended 2026-07-26, after the honing round)

The four owning seats (NT, DG, AG, HA) completed Round-2 honing; their
appendices live in the respective PLAN files. Corrections to THIS document:

1. **T1(i) IS FALSE AS MERGED — do not take to paper or Lean.** HA Round 2
   gives an explicit counterexample (polynomial x sinc-power in PW_a ∩ L²
   vanishing on any finite head): finitely many linear conditions never force
   vanishing. The surviving form is the TWO-HORIZON restatement T1':
   e·T* is the variational (worth/count) horizon; e²·T* is the hard horizon
   via anchored Jensen (anchor hypothesis necessary). Consistency: measured
   stopping heights 3.03–3.39·T* and the C4 saturation 3.59·T* lie strictly
   inside (e·T*, e²·T*) = (2.72, 7.39)·T*. Full days-scale sketch: HA Round 2
   item (b); unconditional-for-zeta corollary via NT's R1/R2.
2. **Bookkeeping slip in §2 header**: D(eT*) = −7/8 exactly, not 0; the exact
   zero is the signed integral ∫₀^{eT*}(a/π − ρ̂) = 0. Found independently by
   NT (numeric) and DG (symbolic); cancels in all displayed consequences.
3. **New exact identity (NT Round 2)**: the super-Nyquist surplus on
   [T*, eT*] equals the deficit mass e^ℓ exactly — e·T* is the balayage
   height of the deficit measure (semantic upgrade for T1').
4. **C4 protocol upgraded (DG Round 2)**: three hypotheses, not two; level
   tests detect only abrupt saturation; the smooth-cap/drift separation
   requires the shape test. Executable protocol with reference tables is in
   PLAN-differential-geometry.md Round 2(c).
5. **AG Round-1 P3 withdrawn by its author** (already answered by law-theory
   RUN 4); AG's T2/C1 merges corrected to the pure-integer Gram G_n and the
   REDUCED wall 2(2g−2)ln q as the discrete capacity height; π²/2 confirmed
   absent at constant density (must emerge from grading).
6. **T3 refinements (DG Round 2)**: separation clause and tail clause boxed;
   Q3's factor-6.3 sits inside T3's budget (threatens shared-constants, not
   bounded transfer). NT input package (R1/R2 licenses with explicit
   constants, full displacement proof) is in PLAN-number-theory.md Round 2(b).
7. **First fully kernel-checkable end-to-end window**: AG Round 2(d) supplies
   the complete integer spec CurveCert_E5 (bridge = decide point count over
   ZMod 5, no interval arithmetic); implementation dispatched.

Status of the top-five after Round 2: T1 → restated (T1'), sketch upgraded,
still #1; T2 → strengthened (paper-ready AG-1 + Lean spec); T3 → full proof
skeleton, one wall (G1, HA toolbox); T4 → strengthened (secular identity
verified exact in the FF pilot); T5 → unchanged. Kill list unchanged plus:
T1(i)-as-merged added.
