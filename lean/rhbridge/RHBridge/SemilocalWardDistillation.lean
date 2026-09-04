/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Pi
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Order
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Abstract Ward lemmas distilled from the semilocal audit

This file records four reusable facts which do not depend on zeta arithmetic.

* A positive old-space floor turns mixed-plane nonnegativity into the Ward
  (Schur/Cauchy) inequality, with a division-free proof in both directions.
* `m` scalar constraints remove at most `m` dimensions.
* A correction carried by two scalar channels vanishes on their joint kernel
  and factors through a two-dimensional moment map.
* The scalar skeleton of the signed projection-difference countermodel has an
  exact Ward quotient which is unbounded as its old-space floor collapses.

These are method constraints, not positivity or propagation theorems for the
Weil form.  In particular, the final family supplies no zeta-specific input.
-/

namespace RHBridge.SemilocalWardDistillation

noncomputable section

section WardCauchy

/-- The scalar quadratic form associated to an old/collar block with old
energy `A`, cross term `B`, and collar energy `D`. -/
def mixedQuadratic (A B D x y : ℝ) : ℝ :=
  A * x ^ 2 + 2 * B * x * y + D * y ^ 2

/-- Division-free Ward necessity.  Evaluating the mixed quadratic form at
`(-B, A)` gives `A * (A * D - B^2)`.  Thus a strictly positive old floor
forces the Schur/Cauchy inequality without choosing a minimizing quotient. -/
theorem wardCauchy_of_mixed_nonnegative {A B D : ℝ} (hA : 0 < A)
    (hmix : ∀ x y : ℝ, 0 ≤ mixedQuadratic A B D x y) :
    B ^ 2 ≤ A * D := by
  have htest := hmix (-B) A
  have hfactor : mixedQuadratic A B D (-B) A =
      A * (A * D - B ^ 2) := by
    simp only [mixedQuadratic]
    ring
  rw [hfactor] at htest
  by_contra hdet
  have hneg : A * D - B ^ 2 < 0 := by
    exact sub_neg.mpr (lt_of_not_ge hdet)
  exact (not_lt_of_ge htest) (mul_neg_of_pos_of_neg hA hneg)

/-- Division-free Ward sufficiency.  Multiplication by the positive floor
turns the mixed form into a sum of two manifestly nonnegative squares:

`A Q(x,y) = (A x + B y)^2 + (A D - B^2)y^2`.
-/
theorem mixed_nonnegative_of_wardCauchy {A B D : ℝ} (hA : 0 < A)
    (hdet : B ^ 2 ≤ A * D) :
    ∀ x y : ℝ, 0 ≤ mixedQuadratic A B D x y := by
  intro x y
  have hsquare : 0 ≤ (A * x + B * y) ^ 2 := sq_nonneg _
  have hremainder : 0 ≤ (A * D - B ^ 2) * y ^ 2 :=
    mul_nonneg (sub_nonneg.mpr hdet) (sq_nonneg y)
  have hscaled : 0 ≤ A * mixedQuadratic A B D x y := by
    have hsum := add_nonneg hsquare hremainder
    have hfactor :
        (A * x + B * y) ^ 2 + (A * D - B ^ 2) * y ^ 2 =
          A * mixedQuadratic A B D x y := by
      simp only [mixedQuadratic]
      ring
    rwa [hfactor] at hsum
  by_contra hq
  have hqneg : mixedQuadratic A B D x y < 0 := lt_of_not_ge hq
  exact (not_lt_of_ge hscaled) (mul_neg_of_pos_of_neg hA hqneg)

/-- Exact bivariate Ward--Cauchy equivalence at a positive old floor. -/
theorem mixedNonnegative_iff_wardCauchy {A B D : ℝ} (hA : 0 < A) :
    (∀ x y : ℝ, 0 ≤ mixedQuadratic A B D x y) ↔ B ^ 2 ≤ A * D := by
  constructor
  · exact wardCauchy_of_mixed_nonnegative hA
  · exact mixed_nonnegative_of_wardCauchy hA

/-- Exact alignment is a constant-one Ward estimate.  If the old energy
dominates `C^2` and the cross term is exactly `C * D`, no division by the old
floor is needed. -/
theorem wardCauchy_of_exact_alignment {A B C D : ℝ}
    (hA : C ^ 2 ≤ A) (hB : B = C * D) :
    B ^ 2 ≤ A * D ^ 2 := by
  have hmul := mul_le_mul_of_nonneg_right hA (sq_nonneg D)
  rw [hB]
  nlinarith

/-- Reserve-absorbed approximate alignment.  The old energy has an aligned
piece `C^2` and a nonnegative reserve `R`; the cross term has aligned part
`C*D` and error `E`.  If the error-square is at most `eta^2 R`, the reserve
absorbs it with no loss beyond adding `eta^2` to the collar energy.

The core identity, after multiplying by `R`, is

`R ((C^2+R)(D^2+eta^2) - (CD+E)^2)`

`= (RD-CE)^2 + (C^2+R)(R eta^2-E^2)`.
-/
theorem wardCauchy_of_reserve_absorbed_alignment
    {A B C D E R eta : ℝ}
    (hR : 0 ≤ R) (hA : C ^ 2 + R ≤ A)
    (hB : B = C * D + E) (hE : E ^ 2 ≤ eta ^ 2 * R) :
    B ^ 2 ≤ A * (D ^ 2 + eta ^ 2) := by
  have hcollar : 0 ≤ D ^ 2 + eta ^ 2 :=
    add_nonneg (sq_nonneg D) (sq_nonneg eta)
  have htop :
      (C ^ 2 + R) * (D ^ 2 + eta ^ 2) ≤
        A * (D ^ 2 + eta ^ 2) :=
    mul_le_mul_of_nonneg_right hA hcollar
  rcases hR.eq_or_lt with rfl | hRpos
  · have hEzero : E = 0 := by
      have hEsq := sq_nonneg E
      nlinarith
    rw [hB, hEzero, add_zero]
    have hA0 : 0 ≤ A := (sq_nonneg C).trans (by simpa using hA)
    have htail : A * D ^ 2 ≤ A * (D ^ 2 + eta ^ 2) :=
      mul_le_mul_of_nonneg_left (le_add_of_nonneg_right (sq_nonneg eta)) hA0
    exact (wardCauchy_of_exact_alignment (C := C) (D := D)
      (by simpa using hA) rfl).trans htail
  · have herror : 0 ≤ R * eta ^ 2 - E ^ 2 := by
      have : E ^ 2 ≤ R * eta ^ 2 := by
        nlinarith [hE]
      exact sub_nonneg.mpr this
    have hbase : 0 ≤ C ^ 2 + R := add_nonneg (sq_nonneg C) hRpos.le
    have hsum :
        0 ≤ (R * D - C * E) ^ 2 +
          (C ^ 2 + R) * (R * eta ^ 2 - E ^ 2) :=
      add_nonneg (sq_nonneg _) (mul_nonneg hbase herror)
    have hid :
        (R * D - C * E) ^ 2 +
            (C ^ 2 + R) * (R * eta ^ 2 - E ^ 2) =
          R * ((C ^ 2 + R) * (D ^ 2 + eta ^ 2) -
            (C * D + E) ^ 2) := by
      ring
    rw [hid] at hsum
    have hmiddle :
        (C * D + E) ^ 2 ≤ (C ^ 2 + R) * (D ^ 2 + eta ^ 2) := by
      by_contra hneg
      have hdiff :
          (C ^ 2 + R) * (D ^ 2 + eta ^ 2) - (C * D + E) ^ 2 < 0 := by
        exact sub_neg.mpr (lt_of_not_ge hneg)
      exact (not_lt_of_ge hsum) (mul_neg_of_pos_of_neg hRpos hdiff)
    rw [hB]
    exact hmiddle.trans htop

/-- Reserve-localized Schur closure.  The cross square uses only `C` copies of
an auxiliary energy `G`; the collar diagonal retains a reserve `S - M*G`.
If `G` occupies at most an `omega` fraction of `S` and the combined charge
`M+C` fits in that fraction, then the full mixed block is nonnegative.

This packages the recurring ledger

`B^2 <= C A G`, `D >= S-MG`, `G <= omega S`, `(M+C)omega <= 1`

without dividing by the possibly small old energy `A`. -/
theorem mixed_nonnegative_of_reserve_localized_schur
    {A B C G D S M omega : ℝ}
    (hA : 0 ≤ A) (hC : 0 ≤ C) (hG : 0 ≤ G) (hS : 0 ≤ S)
    (hM : 0 ≤ M) (homega : 0 ≤ omega)
    (hcross : B ^ 2 ≤ C * A * G)
    (hdiagonal : S - M * G ≤ D)
    (hlocalized : G ≤ omega * S)
    (hbudget : (M + C) * omega ≤ 1) :
    ∀ x y : ℝ, 0 ≤ mixedQuadratic A B D x y := by
  have hMC : 0 ≤ M + C := add_nonneg hM hC
  have homegaS : 0 ≤ omega * S := mul_nonneg homega hS
  have hcharged : (M + C) * G ≤ S := by
    calc
      (M + C) * G ≤ (M + C) * (omega * S) :=
        mul_le_mul_of_nonneg_left hlocalized hMC
      _ = ((M + C) * omega) * S := by ring
      _ ≤ 1 * S := mul_le_mul_of_nonneg_right hbudget hS
      _ = S := one_mul S
  have hCGreserve : C * G ≤ S - M * G := by
    nlinarith
  have hCGD : C * G ≤ D := hCGreserve.trans hdiagonal
  have hD : 0 ≤ D :=
    (mul_nonneg hC hG).trans hCGD
  have hdet : B ^ 2 ≤ A * D := by
    calc
      B ^ 2 ≤ C * A * G := hcross
      _ = A * (C * G) := by ring
      _ ≤ A * D := mul_le_mul_of_nonneg_left hCGD hA
  rcases hA.eq_or_lt with rfl | hApos
  · have hBzero : B = 0 := by
      nlinarith [sq_nonneg B]
    intro x y
    simp [mixedQuadratic, hBzero, mul_nonneg hD (sq_nonneg y)]
  · exact mixed_nonnegative_of_wardCauchy hApos hdet

end WardCauchy

section FiniteConstraints

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- Package a finite family of scalar constraints into its joint moment map. -/
def constraintMap {m : ℕ} (ell : Fin m → V →ₗ[K] K) : V →ₗ[K] (Fin m → K) :=
  LinearMap.pi ell

@[simp] theorem constraintMap_apply {m : ℕ} (ell : Fin m → V →ₗ[K] K)
    (v : V) (i : Fin m) :
    constraintMap ell v i = ell i v :=
  rfl

/-- The joint kernel of the packaged map is exactly the intersection of the
individual constraint kernels. -/
theorem ker_constraintMap {m : ℕ} (ell : Fin m → V →ₗ[K] K) :
    LinearMap.ker (constraintMap ell) = ⨅ i, LinearMap.ker (ell i) := by
  exact LinearMap.ker_pi ell

/-- `m` scalar constraints have rank at most `m`. -/
theorem finrank_range_constraintMap_le {m : ℕ}
    (ell : Fin m → V →ₗ[K] K) :
    Module.finrank K (LinearMap.range (constraintMap ell)) ≤ m := by
  calc
    Module.finrank K (LinearMap.range (constraintMap ell)) ≤
        Module.finrank K (Fin m → K) :=
      (LinearMap.range (constraintMap ell)).finrank_le
    _ = m := by simp

/-- Finite-constraint survival: in a finite-dimensional ambient space,
imposing `m` scalar equations removes at most `m` dimensions. -/
theorem finrank_le_jointKernel_add_constraints [FiniteDimensional K V]
    {m : ℕ} (ell : Fin m → V →ₗ[K] K) :
    Module.finrank K V ≤
      Module.finrank K ↥(⨅ i, LinearMap.ker (ell i)) + m := by
  let F := constraintMap ell
  have hrank := F.finrank_range_add_finrank_ker
  have hrange : Module.finrank K (LinearMap.range F) ≤ m := by
    simpa [F] using finrank_range_constraintMap_le ell
  have hker : LinearMap.ker F = ⨅ i, LinearMap.ker (ell i) := by
    simpa [F] using ker_constraintMap ell
  rw [hker] at hrank
  omega

/-- Quantitative form of finite-constraint survival.  If the ambient space
has at least `r + m` dimensions, at least `r` dimensions survive all `m`
constraints. -/
theorem le_finrank_jointKernel_of_add_le_finrank [FiniteDimensional K V]
    {m r : ℕ} (ell : Fin m → V →ₗ[K] K)
    (hdim : r + m ≤ Module.finrank K V) :
    r ≤ Module.finrank K ↥(⨅ i, LinearMap.ker (ell i)) := by
  have hbound := finrank_le_jointKernel_add_constraints ell
  omega

end FiniteConstraints

section TwoChannelCorrection

variable {K V : Type*} [CommRing K] [AddCommGroup V] [Module K V]

/-- The universal symmetric correction carried by two scalar channels.  The
zeta pole term is its sesquilinear analogue. -/
def twoChannelCorrection (ell₀ ell₁ : V →ₗ[K] K) (v w : V) : K :=
  ell₀ v * ell₁ w + ell₁ v * ell₀ w

/-- The two-dimensional moment map through which the correction factors. -/
def twoChannelMomentMap (ell₀ ell₁ : V →ₗ[K] K) : V →ₗ[K] K × K :=
  ell₀.prod ell₁

/-- Symmetric off-diagonal pairing on the two-channel target. -/
def swapPairing (a b : K × K) : K :=
  a.1 * b.2 + a.2 * b.1

/-- Exact factorization of every two-channel correction through the moment
map. -/
theorem twoChannelCorrection_factorization (ell₀ ell₁ : V →ₗ[K] K)
    (v w : V) :
    twoChannelCorrection ell₀ ell₁ v w =
      swapPairing (twoChannelMomentMap ell₀ ell₁ v)
        (twoChannelMomentMap ell₀ ell₁ w) :=
  rfl

/-- A vector in the joint moment kernel annihilates the correction in the
left slot. -/
theorem twoChannelCorrection_eq_zero_of_left
    (ell₀ ell₁ : V →ₗ[K] K) {v w : V}
    (h₀ : ell₀ v = 0) (h₁ : ell₁ v = 0) :
    twoChannelCorrection ell₀ ell₁ v w = 0 := by
  simp [twoChannelCorrection, h₀, h₁]

/-- A vector in the joint moment kernel annihilates the correction in the
right slot. -/
theorem twoChannelCorrection_eq_zero_of_right
    (ell₀ ell₁ : V →ₗ[K] K) {v w : V}
    (h₀ : ell₀ w = 0) (h₁ : ell₁ w = 0) :
    twoChannelCorrection ell₀ ell₁ v w = 0 := by
  simp [twoChannelCorrection, h₀, h₁]

/-- Adding a two-channel correction does not change any bilinear form on the
joint moment kernel. -/
theorem add_twoChannelCorrection_eq_left
    (base : V → V → K) (ell₀ ell₁ : V →ₗ[K] K) {v w : V}
    (h₀ : ell₀ v = 0) (h₁ : ell₁ v = 0) :
    base v w + twoChannelCorrection ell₀ ell₁ v w = base v w := by
  rw [twoChannelCorrection_eq_zero_of_left ell₀ ell₁ h₀ h₁, add_zero]

end TwoChannelCorrection

section DivergentWardFamily

/-- Squared positive-channel weight in the projection-difference family. -/
def positiveChannelWeightSq (delta : ℝ) : ℝ :=
  (1 + delta ^ 2) / (1 + delta)

/-- Squared reverse-channel weight in the projection-difference family. -/
def reverseChannelWeightSq (delta : ℝ) : ℝ :=
  (delta - delta ^ 2) / (1 + delta)

/-- The collapsing old-space energy in the family. -/
def counterFloor (delta : ℝ) : ℝ :=
  delta ^ 2

/-- The squared old/collar cross term in the family. -/
def counterCrossSq (delta : ℝ) : ℝ :=
  (1 + delta ^ 2) * (delta - delta ^ 2)

/-- The two squared mixing weights sum to one. -/
theorem channelWeightSq_sum (delta : ℝ) (hdelta : delta ≠ -1) :
    positiveChannelWeightSq delta + reverseChannelWeightSq delta = 1 := by
  have hden : 1 + delta ≠ 0 := by
    intro h
    apply hdelta
    linarith
  simp only [positiveChannelWeightSq, reverseChannelWeightSq]
  field_simp [hden]
  ring

/-- Mixing eigenvalues `delta` and `-1` with the displayed weights produces
the old-space floor `delta^2` exactly. -/
theorem mixedOldEnergy_eq_counterFloor (delta : ℝ) (hdelta : delta ≠ -1) :
    delta * positiveChannelWeightSq delta - reverseChannelWeightSq delta =
      counterFloor delta := by
  have hden : 1 + delta ≠ 0 := by
    intro h
    apply hdelta
    linarith
  simp only [positiveChannelWeightSq, reverseChannelWeightSq, counterFloor]
  field_simp [hden]
  ring

/-- The squared cross term of the orthogonal mixing is exactly the numerator
used by `counterCrossSq`. -/
theorem mixedCrossSq_eq_counterCrossSq (delta : ℝ) (hdelta : delta ≠ -1) :
    (1 + delta) ^ 2 * positiveChannelWeightSq delta *
        reverseChannelWeightSq delta = counterCrossSq delta := by
  have hden : 1 + delta ≠ 0 := by
    intro h
    apply hdelta
    linarith
  simp only [positiveChannelWeightSq, reverseChannelWeightSq, counterCrossSq]
  field_simp [hden]

/-- On `0 < delta < 1`, both mixing weights are strictly positive. -/
theorem channelWeightSq_pos {delta : ℝ} (hdelta : 0 < delta)
    (hdeltaOne : delta < 1) :
    0 < positiveChannelWeightSq delta ∧
      0 < reverseChannelWeightSq delta := by
  have hden : 0 < 1 + delta := by linarith
  have hnumReverse : 0 < delta - delta ^ 2 := by
    have hprod := mul_pos hdelta (sub_pos.mpr hdeltaOne)
    nlinarith
  constructor
  · exact div_pos (by positivity) hden
  · exact div_pos hnumReverse hden

/-- Exact closed form of the Ward quotient. -/
theorem counterCrossSq_div_counterFloor {delta : ℝ} (hdelta : delta ≠ 0) :
    counterCrossSq delta / counterFloor delta =
      (1 + delta ^ 2) * (delta⁻¹ - 1) := by
  simp only [counterCrossSq, counterFloor]
  field_simp [hdelta]

/-- Division-free unboundedness certificate: for every proposed Ward constant
`R ≥ 0`, an explicit `delta` in `(0,1)` makes cross-square exceed `R` times
the old floor. -/
theorem exists_counterCrossSq_gt_mul_counterFloor (R : ℝ) (hR : 0 ≤ R) :
    ∃ delta : ℝ, 0 < delta ∧ delta < 1 ∧
      R * counterFloor delta < counterCrossSq delta := by
  let delta : ℝ := 1 / (R + 2)
  have hden : 0 < R + 2 := by linarith
  have hdenOne : 1 < R + 2 := by linarith
  have hdelta : 0 < delta := by
    exact one_div_pos.mpr hden
  have hdeltaOne : delta < 1 := by
    simpa [delta] using (div_lt_one hden).mpr hdenOne
  have hmul : delta * (R + 2) = 1 := by
    dsimp [delta]
    field_simp [ne_of_gt hden]
  have hRdelta : R * delta = 1 - 2 * delta := by
    nlinarith [hmul]
  have hRdeltaSq : R * delta ^ 2 = delta - 2 * delta ^ 2 := by
    calc
      R * delta ^ 2 = (R * delta) * delta := by ring
      _ = (1 - 2 * delta) * delta := by rw [hRdelta]
      _ = delta - 2 * delta ^ 2 := by ring
  have hgap : 0 < delta ^ 2 * (1 + delta - delta ^ 2) := by
    have hsmall : 0 < delta - delta ^ 2 := by
      have hprod := mul_pos hdelta (sub_pos.mpr hdeltaOne)
      nlinarith
    exact mul_pos (sq_pos_of_pos hdelta) (by linarith)
  refine ⟨delta, hdelta, hdeltaOne, ?_⟩
  have hid :
      counterCrossSq delta - R * counterFloor delta =
        delta ^ 2 * (1 + delta - delta ^ 2) := by
    rw [counterCrossSq, counterFloor, hRdeltaSq]
    ring
  linarith

/-- The actual Ward quotient is unbounded on `0 < delta < 1`. -/
theorem counterWardQuotient_unbounded (R : ℝ) :
    ∃ delta : ℝ, 0 < delta ∧ delta < 1 ∧
      R < counterCrossSq delta / counterFloor delta := by
  obtain ⟨delta, hdelta, hdeltaOne, hcross⟩ :=
    exists_counterCrossSq_gt_mul_counterFloor (max R 0) (le_max_right R 0)
  have hfloor : 0 < counterFloor delta := by
    exact sq_pos_of_pos hdelta
  refine ⟨delta, hdelta, hdeltaOne, ?_⟩
  apply lt_of_le_of_lt (le_max_left R 0)
  exact (lt_div_iff₀ hfloor).mpr hcross

/-- The division-free counterexample occurs inside every prescribed
neighborhood of zero.  For a radius `radius`, take
`eta = min radius 1` and `delta = eta / (R+2)`. -/
theorem exists_counterCrossSq_gt_mul_counterFloor_below
    (R radius : ℝ) (hR : 0 ≤ R) (hradius : 0 < radius) :
    ∃ delta : ℝ, 0 < delta ∧ delta < radius ∧ delta < 1 ∧
      R * counterFloor delta < counterCrossSq delta := by
  let eta : ℝ := min radius 1
  let delta : ℝ := eta / (R + 2)
  have heta : 0 < eta := by
    exact lt_min hradius zero_lt_one
  have hetaRadius : eta ≤ radius := min_le_left _ _
  have hetaOne : eta ≤ 1 := min_le_right _ _
  have hden : 0 < R + 2 := by linarith
  have hdenOne : 1 < R + 2 := by linarith
  have hdelta : 0 < delta := div_pos heta hden
  have hdeltaEta : delta < eta := by
    dsimp [delta]
    exact (div_lt_iff₀ hden).2 (by nlinarith)
  have hdeltaRadius : delta < radius := hdeltaEta.trans_le hetaRadius
  have hdeltaOne : delta < 1 := hdeltaEta.trans_le hetaOne
  have hmul : delta * (R + 2) = eta := by
    dsimp [delta]
    field_simp [ne_of_gt hden]
  have hRdelta : R * delta = eta - 2 * delta := by
    nlinarith [hmul]
  have hRdeltaSq : R * delta ^ 2 = (eta - 2 * delta) * delta := by
    calc
      R * delta ^ 2 = (R * delta) * delta := by ring
      _ = (eta - 2 * delta) * delta := by rw [hRdelta]
  have hsmall : 0 < delta - delta ^ 2 := by
    have hprod := mul_pos hdelta (sub_pos.mpr hdeltaOne)
    nlinarith
  have hstrict : 0 < delta ^ 2 * (1 + delta - delta ^ 2) := by
    exact mul_pos (sq_pos_of_pos hdelta) (by linarith)
  have hnonneg : 0 ≤ delta * (1 - eta) :=
    mul_nonneg hdelta.le (sub_nonneg.mpr hetaOne)
  refine ⟨delta, hdelta, hdeltaRadius, hdeltaOne, ?_⟩
  have hid :
      counterCrossSq delta - R * counterFloor delta =
        delta * (1 - eta) + delta ^ 2 * (1 + delta - delta ^ 2) := by
    rw [counterCrossSq, counterFloor, hRdeltaSq]
    ring
  linarith

/-- Equivalently, the Ward quotient exceeds any prescribed level arbitrarily
close to the collapsing-floor endpoint. -/
theorem counterWardQuotient_unbounded_near_zero (R radius : ℝ)
    (hradius : 0 < radius) :
    ∃ delta : ℝ, 0 < delta ∧ delta < radius ∧ delta < 1 ∧
      R < counterCrossSq delta / counterFloor delta := by
  obtain ⟨delta, hdelta, hdeltaRadius, hdeltaOne, hcross⟩ :=
    exists_counterCrossSq_gt_mul_counterFloor_below
      (max R 0) radius (le_max_right R 0) hradius
  have hfloor : 0 < counterFloor delta := sq_pos_of_pos hdelta
  refine ⟨delta, hdelta, hdeltaRadius, hdeltaOne, ?_⟩
  apply lt_of_le_of_lt (le_max_left R 0)
  exact (lt_div_iff₀ hfloor).2 hcross

end DivergentWardFamily

end

end RHBridge.SemilocalWardDistillation
