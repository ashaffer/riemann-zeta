# agent-floor-witness — the Floor Witness, kernel-checked (2026-07-26)

Dispatch: PT seat R2.5 / R2.2 C-9 dispatch spec (`results/ias/SEAT-proof-theory.md`),
executed by the Lean track. Artifact: `lean/weilcert/FloorWitness.lean` (new
`lean_lib` target, lakefile append-only). Data generation + adjudication scripts in
the session scratchpad (`floor_gen1.py`, `floor_gen2.py`).

> **FLAG — pre-registered T1 prediction (i) missed, for an exactly-diagnosed
> basis-bookkeeping reason; the miss STRENGTHENS the artifact. Details in §3.
> The witness value in the frame the dispatch's generation path actually
> produces is 1.5338e−21 (below the [3.5, 5.5]e−21 band); the same exact
> numerator read in the orthonormal frame in which Q5's δ* was measured is
> 4.48873e−21 — dead-center in the band and equal to Q5's settled 4.489e−21.
> Nothing landed above 1e−20 (T1's own named kill direction), headroom passed
> at 6.52× (required ≥ 1.8×), and the coherence oracle passed on all legs.
> Proceeded under the unambiguous-correction clause; the coordinator should
> confirm this adjudication before the artifact is cited program-wide.**

## 1. What was proved (in words)

Four kernel-checked theorems about the explicit rational matrix
`mRat = aFun/10^25` — the exact-rational midpoint matrix of the truncated Weil
form of ζ at support L = 711/200 in the unnormalized Legendre basis P₀..P₃₉
(m = 40), the basis of every existing house ball certificate:

1. **`floor_witness`** (the dispatch statement, verbatim shape): there exists a
   symmetric rational 40×40 matrix M entrywise within δ = 1e−20 of `mRat`
   together with a rational direction x such that x ⬝ᵥ M *ᵥ x < 0.
   The witness is the rank-one adversary M = mRat − δ·s·sᵀ, s = sign(x)
   (CS-1(v)); the kernel reduces the whole check to ONE exact-ℤ inequality.
2. **`no_ball_certificate_ge` / `no_ball_certificate`**: consequently the
   conclusion of the house window theorems (`weil_window_positive` shape — "every
   matrix entrywise within δ' of the midpoint has positive quadratic form") is
   FALSE at this window for EVERY δ' ≥ 1e−20. No sound entrywise-ball
   certificate of the repo's form with δ ≥ 1e−20 can exist at L = 711/200.
3. **`depth_law_bracket`** (formal regression of the depth law, Q5):
   the ℓ¹-normalized Rayleigh value of the witness is kernel-checked into the
   two-sided enclosure (1.5e−21, 1.6e−21):
   `15/10^22·(Σ|xᵢ|)² < xᵀ·mRat·x < 16/10^22·(Σ|xᵢ|)²`.
   This is the measured certificate floor δ* at the fifth window, now a
   kernel fact (in the house basis).
4. **`headroom_sixfold`**: `6·(xᵀ·mRat·x) < δ·(Σ|xᵢ|)²` — the pre-registered
   headroom criterion, kernel-checked with margin (measured 6.52×).

Kernel-side integer facts (all by `decide`, ℤ only, no ℚ decide, no
`native_decide`): symmetry of the 1600-entry data, sign-vector bounds |sᵢ| ≤ 1,
the sign/abs coherence sᵢxᵢ = |xᵢ|, a nonzero pivot, and the single bracket
`15000·sWit² < qWit < 16000·sWit²` where
qWit = Σᵢⱼ xᵢAᵢⱼxⱼ (36-digit integer) and sWit = Σᵢ|xᵢ| (as integers scaled by
10^15/10^25). Everything else is exact ℚ algebra (rank-one split + cast lemmas).

Interpretation rides the usual computer-assisted Bridge, stated as always: the
true Weil matrix at this window lies entrywise within the exact identification
budget 4.989e−26 of `mRat` (220-bit outward-rounded interval enclosures,
`src/certified_spectral.py`). Center-robustness (prose, not formalized): since
the witness value is 1.53e−21 and |xᵀEx| ≤ c·(Σ|xᵢ|)² for any entrywise-c
recentering, the same adversary kills a δ = 1e−20 ball around ANY center within
c < 8.47e−21 of `mRat` — 10⁴ times more than the identification budget. The
impossibility is a property of the window, not of our rounding.

## 2. Data provenance

Per the dispatch's generation path, pathology-#5 discipline throughout:

- Enclosures: `certified_spectral_form(711/200, 40)` — 220-bit iv enclosures,
  unnormalized Legendre basis (30 s). Endpoints extracted as exact Fractions
  from raw mpf tuples (no float/decimal pass anywhere).
- `A = round(10^25 · midpoint)` in exact integer arithmetic (DENP = 25 per
  spec); symmetry exact; identification budget = max rounding + max halfwidth
  = **4.989e−26**, exact.
- Witness x: bottom eigenvector of the midpoint matrix itself (mp.eigsy at
  dps 60 — spec asked ≥ 30 digits), truncated to denominator 10^15 per spec
  (max-entry normalization). 20 nonzero entries (the even-parity block; odd
  block is exactly zero). Spectral gap in this frame λ₂/λ₁ = 2.093e−18 /
  6.993e−21 ≈ 299, so the 1e−15 truncation (angle ~1e−14 ≪ the 0.04 the spec
  requires) moves the Rayleigh value only in the 7th digit.
- s = sign(x) entrywise (0 on the odd block — handled by |sᵢ| ≤ 1 in the ball
  bound; the reduction identity uses sᵢxᵢ = |xᵢ|, kernel-checked).
- EVERY identity asserted in Lean was first re-verified exactly in
  Fraction/int arithmetic (script `floor_gen2.py` §c: symmetry; sign bounds
  and coherence; the two-sided bracket; independent full-matrix Fraction
  evaluation of xᵀ(mRat − δssᵀ)x = −9.6716e−20 < 0 and its exact agreement
  with the rank-one reduction; ball membership; pivot). Any failed assert
  aborts with no emission.

Key exact numbers:
- qWit = 175223096934935167175041588725801241 (36 digits),
  sWit = 3379909906132830.
- Exact witness ratio qWit/(sWit²·10^25) = **1.533843689e−21**;
  headroom vs 1e−20 = **6.520×**.
- Orthonormal-frame cross-read of the same numerator: **4.48873e−21** = Q5's
  δ* (4.489e−21) to all printed digits; conversion factor
  (ℓ¹_unnorm/ℓ¹_orth)² = 2.92646, verified exactly to close the decomposition.

## 3. Pre-registration check (R2.6 T1) — verbatim outcomes

| T1 clause | pre-registered | measured | verdict |
|---|---|---|---|
| (i) witness value x⬝ᵥA.mulVec x/(Σ\|xᵢ\|)² in [3.5, 5.5]e−21 | reproduce Q5's δ* = 4.489e−21 | **1.5338e−21** in the frame the generation path produces (house/unnormalized); **4.48873e−21** for the identical numerator in the orthonormal frame where Q5's δ* was measured | **MISSED as literally stated; exactly diagnosed** (below) |
| (ii) headroom vs δ = 1e−20 ≥ 1.8× | ≥ 1.8× | **6.520×** | PASS |
| (iii) coherence oracle within combined budgets | pass | all three legs PASS (below) | PASS |
| Kill ("if (i) lands ABOVE 1e−20 … Q5's settled number is wrong") | not above 1e−20 | 1.53e−21 ≪ 1e−20; Q5 reproduced exactly in its own frame | **NOT TRIGGERED** |

**Diagnosis of the (i) miss, verified in exact arithmetic.** Q5's
δ* = λ/‖v‖₁² was computed with `spectral_margins.spectral_form`, which works in
the ORTHONORMAL Legendre basis (Gram = I). The dispatch's generation path
("emit A at DENP = 25 from certified_spectral midpoints") produces the
UNNORMALIZED-basis matrix — the basis of every existing Lean ball certificate,
hence the right one for a "no certificate of the repo's ball form" statement.
The two frames differ by the ℓ¹ weights √Gₖ, Gₖ = 2a/(2k+1): with the identical
exact numerator, ratio_unnorm × (ℓ¹_un/ℓ¹_orth)² = 1.533844e−21 × 2.92646 =
4.48873e−21 = ratio_orth, and 4.48873e−21 sits mid-band. So the band was
calibrated in the orthonormal frame while the spec's data path (correctly)
emits the house frame; the floor in the house frame is LOWER, i.e. the
impossibility is stronger than pre-registered. No data was adjusted; both
frames' numbers are reported. Anchors reproduced along the way: λ₁(orth) =
1.7997229e−20 (inside the certified enclosure), λ₂ = 1.071e−17 (λ₂/λ₁ = 595 ≈
the spec's 600), ‖u₁‖₁² = 4.00943 (SYNTHESIS: 4.0094).

**Adjudication.** The task's strict reading ("outside band → stop") collided
with its mathematical-error clause ("verify exactly, document, proceed only if
the correction is unambiguous"). The correction is unambiguous (a pure
basis-unit conversion, closed exactly; every underlying program number
reproduces; the deviation direction only strengthens the theorem), so the
artifact was built — with this section as the prominent flag, and the explicit
request that the coordinator countersign before program-wide citation.

**Coherence oracle** (standing, pathology-#5; no nested certificate exists at
this window — SYNTHESIS already corrected the precis conflation — so the three
applicable legs were run):
- b1: every emitted integer within ½ grid step of the exact enclosure midpoint;
  max |A/10^25 − mid| = 4.989e−26 ≤ 5e−26. PASS.
- b2: dps-60 orthonormal λ₁ from the midpoints = 1.79972291e−20, inside the
  certified enclosure (1.7997e−20, 1.79972291e−20]. PASS.
- b3: cross-implementation, entrywise: independent `spectral_form` GL-quadrature
  path vs midpoints·nₖnⱼ — max discrepancy **1.63e−40** (budget 1e−24). PASS.
  Incident worth recording: the first b3 run passed `float(711/200)` (binary-
  inexact) as L and manufactured a phantom 9.7e−16 "discrepancy" — pathology
  #4's exact failure mode, caught by the budget check and fixed by passing the
  exact decimal mpf ('3.555'). The oracle discipline caught its own operator.

## 4. Audits (verbatim)

Toolchain: Lean 4.32.1 (elan), mathlib pinned by `lean/weilcert/lake-manifest.json`.
Build: `cd lean/weilcert && lake build FloorWitness` — exit 0, module compile
~86 s; sole warning is the mathlib style linter on the file-level
`set_option maxHeartbeats` (house pattern, same as `WeilcertDeeper`).

```
$ lake env lean audit_floor.lean        # import FloorWitness + #print axioms
'FloorWitness.floor_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.no_ball_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.no_ball_certificate_ge' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.depth_law_bracket' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.headroom_sixfold' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.witness_negative' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.mBad_in_ball' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.mBad_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.xQ_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.key_bracket' depends on axioms: [propext, Classical.choice, Quot.sound]
'FloorWitness.a_symm_int' depends on axioms: [Quot.sound]
'FloorWitness.s_bound' depends on axioms: [propext]
'FloorWitness.s_abs_x' depends on axioms: [propext]
```

Zero sorries (no `sorryAx`), no `native_decide` (no `Lean.ofReduceBool` /
`Lean.trustCompiler`) — certified by the axiom lists above; the only
occurrences of either string in the file are documentation comments.

## 5. Deviations from the PT dispatch spec

1. **T1 prediction (i)** — missed as literally stated; exact diagnosis and
   adjudication in §3 (the flagged item).
2. **Sharpened, not weakened**: the spec's single inequality
   `x ⬝ᵥ A.mulVec x < δ·(Σ|xᵢ|)²` was kernel-checked as the two-sided bracket
   `key_bracket` (15000·sWit² < qWit < 16000·sWit²), whose upper half implies
   the spec's inequality with 6.25× slack; this also yields `depth_law_bracket`
   and `headroom_sixfold` beyond the dispatch's asked-for statement.
3. **Additional theorem**: `no_ball_certificate_ge` states impossibility for
   every δ' ≥ 1e−20 (the dispatch's headline "δ ≥ 1e−20" made formal, not just
   the point value δ = 1e−20).
4. **Witness eigenvector frame**: x is the bottom eigenvector of the midpoint
   matrix itself (std eigenproblem; gap 299) rather than the transported
   generalized eigenvector the spec's stability numbers (λ₂/λ₁ ≈ 600) refer
   to; the two directions give ℓ¹-Rayleigh values agreeing to 5 digits
   (1.533844 vs 1.533850e−21) and the spec's θ ≤ 0.04 requirement is met with
   ~12 orders to spare either way.
5. **Precision above spec**: eigenvector at dps 60 (spec: 30 digits);
   endpoint conversion via exact mpf-tuple → Fraction (no decimal round-trip).
6. Naming: the spec's `A` is `mRat` (house convention); `M.IsSymm`,
   ball, and negativity clauses are verbatim.

## 6. Meaning

This is the program's first kernel-checked IMPOSSIBILITY artifact — the
negative wing of the artifact stack that the Π₁ asymmetry has always implied
(merge M2). Every prior Lean artifact certifies that positivity holds on some
window; this one certifies that a whole PROOF FORMAT — the entrywise-ball
certificate, the repo's own workhorse — cannot exist at δ ≥ 1e−20 at the
fifth window, exactly as the depth law prices it (δ* = λ/‖v‖₁², Q5; CS-1(v)
floors). Concretely: `WeilcertDeeper` (L = 749/250) ships at δ = 1e−19 with
10⁴× headroom, while two hundredths of an L-unit deeper the same format is
now PROVEN — by the kernel, from 21-digit exact data, under the three standard
axioms — to admit no certificate at 10× finer radius; any sound ball
certificate at L = 711/200 must carry ≥ 21 digits per entry. The certificate-
size lower bounds of the cartography (exp(Θ(e^{L/2})) bits) thus acquire their
first theorem-grade instance at a built window, and the depth law itself now
has a formal regression test: a kernel-checked two-sided enclosure
(1.5e−21, 1.6e−21) of the measured floor. To this program's knowledge (PT-3(c))
it is the first kernel-checked proof-complexity lower-bound artifact attached
to a live open problem's proof family.

## Files

- `lean/weilcert/FloorWitness.lean` — 2014 lines (1690 data, 324 header+proof).
- `lean/weilcert/lakefile.toml` — appended `[[lean_lib]] name = "FloorWitness"`.
- Scratchpad (session): `floor_gen1.py` (enclosures → midpoints → eigen-data →
  candidate adjudication), `floor_gen2.py` (deviation decomposition, coherence
  oracle, exact re-verification, data emission), `floor_phase1.pkl` /
  `floor_final.pkl` (frozen state), `fw_build*.log`, `audit_floor.lean`.

Verify yourself:
```
cd lean/weilcert && lake exe cache get && lake build FloorWitness
cat > /tmp/check.lean <<'EOF'
import FloorWitness
#print axioms FloorWitness.floor_witness
#print axioms FloorWitness.no_ball_certificate_ge
#print axioms FloorWitness.depth_law_bracket
EOF
lake env lean /tmp/check.lean
```


---

## Coordinator countersignature (2026-07-26)

Independently re-verified: green build; `floor_witness`, `no_ball_certificate_ge`,
`depth_law_bracket`, `headroom_sixfold` all on exactly
[propext, Classical.choice, Quot.sound]; zero sorries; reconciliation arithmetic
checked (1.5338e-21 x 2.92646 = 4.4886e-21, matching Q5's orthonormal-frame
delta* = 4.489e-21 to its printed precision). RULING on the flagged T1
deviation: the pre-registered band [3.5, 5.5]e-21 was stated in the orthonormal
frame; the artifact's frame (unnormalized Legendre, the repo's actual
ball-certificate basis) is the correct frame for the impossibility statement,
and the two reads are related by the exact l1 basis-weight factor. This is a
units bookkeeping error in the PREDICTION, not in the artifact; the named kill
direction (value above 1e-20) is far from triggered, and the miss direction
makes the impossibility strictly stronger. COUNTERSIGNED for program-wide
citation. Standing lesson added to program law: pre-registered numerical bands
must state their frame/normalization explicitly.
