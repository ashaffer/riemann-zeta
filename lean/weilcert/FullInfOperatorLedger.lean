/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import FullInfAnalyticLedger

/-!
# Operator-to-block estimates for the clipped FULLINF form

This file proves the analytic *algebra* between the Fourier leakage and pole
projection estimates and the two block bounds consumed by `FullInfTransfer`.
It is deliberately independent of the zeta-specific construction of the
multiplier.  The clipped form is represented as

`alpha * inner + D (C x) (C y) + rankTwo(gPlus,gMinus)`.

Here `C` is the band-restriction map, `D` is bounded in absolute value by
`M`, and the two pole vectors have norm at most `G`.  If `C` has squared
leakage at most `rho` on `Uᵊ` and each pole vector has projection residual
at most `delta`, the complement and cross constants are exactly

`alpha - M*rho - 2*delta^2` and `M*sqrt(rho) + 2*G*delta`.
-/

namespace FullInfOperatorLedger

open scoped RealInnerProductSpace

variable {E K : Type*}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [NormedAddCommGroup K] [InnerProductSpace ℝ K]

/-- Squaring a leakage estimate produces the `rho` loss used on the
orthogonal-complement diagonal. -/
lemma norm_sq_le_of_le_sqrt_mul {rho : ℝ} (hrho : 0 ≤ rho)
    {x y : ℝ} (hx : 0 ≤ x) (hxy : x ≤ Real.sqrt rho * y) :
    x ^ 2 ≤ rho * y ^ 2 := by
  have hsquare := pow_le_pow_left₀ hx hxy 2
  rw [mul_pow, Real.sq_sqrt hrho] at hsquare
  exact hsquare

/-- Conversely, a squared leakage bound implies the square-root norm bound.
This is the direction used to feed an integrated band-energy theorem into the
operator cross estimate. -/
lemma norm_le_sqrt_mul_of_sq_le {rho x y : ℝ}
    (hrho : 0 ≤ rho) (hx : 0 ≤ x) (hy : 0 ≤ y)
    (hsq : x ^ 2 ≤ rho * y ^ 2) :
    x ≤ Real.sqrt rho * y := by
  apply (sq_le_sq₀ hx (mul_nonneg (Real.sqrt_nonneg _) hy)).mp
  rw [mul_pow, Real.sq_sqrt hrho]
  exact hsq

/-- The band multiplier contributes at worst `-M*rho` on a vector satisfying
the leakage estimate. -/
theorem band_diagonal_lower
    (D : K →ₗ[ℝ] K →ₗ[ℝ] ℝ) (M rho : ℝ) (x : K) (yNorm : ℝ)
    (hM : 0 ≤ M) (hrho : 0 ≤ rho)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hleak : ‖x‖ ≤ Real.sqrt rho * yNorm) :
    -(M * rho * yNorm ^ 2) ≤ D x x := by
  have hsq : ‖x‖ ^ 2 ≤ rho * yNorm ^ 2 :=
    norm_sq_le_of_le_sqrt_mul hrho (norm_nonneg x) hleak
  have hscaled : M * ‖x‖ ^ 2 ≤ M * (rho * yNorm ^ 2) :=
    mul_le_mul_of_nonneg_left hsq hM
  have habs : |D x x| ≤ M * ‖x‖ ^ 2 := by
    simpa [pow_two, mul_assoc] using hD x x
  calc
    -(M * rho * yNorm ^ 2) ≤ -(M * ‖x‖ ^ 2) := by
      simpa [mul_assoc] using neg_le_neg hscaled
    _ ≤ D x x := neg_le_of_abs_le habs

/-- The diagonal of the symmetric rank-two pole term loses at most
`2*delta^2`. -/
theorem rankTwo_diagonal_lower
    (gPlus gMinus w : E) (delta : ℝ)
    (hPlus : |inner ℝ w gPlus| ≤ delta * ‖w‖)
    (hMinus : |inner ℝ w gMinus| ≤ delta * ‖w‖) :
    -(2 * delta ^ 2 * ‖w‖ ^ 2) ≤
      inner ℝ w gPlus * inner ℝ w gMinus +
        inner ℝ w gMinus * inner ℝ w gPlus := by
  have hprod :
      |inner ℝ w gPlus * inner ℝ w gMinus| ≤
        (delta * ‖w‖) * (delta * ‖w‖) := by
    rw [abs_mul]
    have hdeltaNorm : 0 ≤ delta * ‖w‖ :=
      (abs_nonneg (inner ℝ w gPlus)).trans hPlus
    exact mul_le_mul hPlus hMinus (abs_nonneg _) hdeltaNorm
  have hlower := neg_le_of_abs_le hprod
  nlinarith

/-- A contraction on the low block and `sqrt rho` leakage on the high block
give the expected `M*sqrt rho` cross estimate. -/
theorem band_cross_bound
    (D : K →ₗ[ℝ] K →ₗ[ℝ] ℝ) (M rho : ℝ) (x y : K)
    (uNorm wNorm : ℝ) (hM : 0 ≤ M)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hx : ‖x‖ ≤ uNorm)
    (hy : ‖y‖ ≤ Real.sqrt rho * wNorm) :
    |D x y| ≤ M * Real.sqrt rho * uNorm * wNorm := by
  have huNorm0 : 0 ≤ uNorm := (norm_nonneg x).trans hx
  calc
    |D x y| ≤ M * ‖x‖ * ‖y‖ := hD x y
    _ ≤ M * uNorm * ‖y‖ := by
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hx hM) (norm_nonneg y)
    _ ≤ M * uNorm * (Real.sqrt rho * wNorm) := by
      exact mul_le_mul_of_nonneg_left hy (mul_nonneg hM huNorm0)
    _ = M * Real.sqrt rho * uNorm * wNorm := by ring

/-- Norm bounds for the two pole vectors and residual pairing bounds give
the `2*G*delta` rank-two cross estimate. -/
theorem rankTwo_cross_bound
    (gPlus gMinus u w : E) (G delta : ℝ)
    (hG : 0 ≤ G) (_hDelta : 0 ≤ delta)
    (hgPlus : ‖gPlus‖ ≤ G) (hgMinus : ‖gMinus‖ ≤ G)
    (hwPlus : |inner ℝ w gPlus| ≤ delta * ‖w‖)
    (hwMinus : |inner ℝ w gMinus| ≤ delta * ‖w‖) :
    |inner ℝ u gPlus * inner ℝ w gMinus +
        inner ℝ u gMinus * inner ℝ w gPlus| ≤
      2 * G * delta * ‖u‖ * ‖w‖ := by
  have huPlus : |inner ℝ u gPlus| ≤ G * ‖u‖ := by
    calc
      |inner ℝ u gPlus| ≤ ‖u‖ * ‖gPlus‖ := abs_real_inner_le_norm _ _
      _ ≤ ‖u‖ * G := mul_le_mul_of_nonneg_left hgPlus (norm_nonneg _)
      _ = G * ‖u‖ := mul_comm _ _
  have huMinus : |inner ℝ u gMinus| ≤ G * ‖u‖ := by
    calc
      |inner ℝ u gMinus| ≤ ‖u‖ * ‖gMinus‖ := abs_real_inner_le_norm _ _
      _ ≤ ‖u‖ * G := mul_le_mul_of_nonneg_left hgMinus (norm_nonneg _)
      _ = G * ‖u‖ := mul_comm _ _
  calc
    |inner ℝ u gPlus * inner ℝ w gMinus +
        inner ℝ u gMinus * inner ℝ w gPlus| ≤
        |inner ℝ u gPlus * inner ℝ w gMinus| +
          |inner ℝ u gMinus * inner ℝ w gPlus| := abs_add_le _ _
    _ ≤ (G * ‖u‖) * (delta * ‖w‖) +
          (G * ‖u‖) * (delta * ‖w‖) := by
      rw [abs_mul, abs_mul]
      exact add_le_add
        (mul_le_mul huPlus hwMinus (abs_nonneg _)
          (mul_nonneg hG (norm_nonneg _)))
        (mul_le_mul huMinus hwPlus (abs_nonneg _)
          (mul_nonneg hG (norm_nonneg _)))
    _ = 2 * G * delta * ‖u‖ * ‖w‖ := by ring

/-- Projection residual control implies the high-block pairing estimate used
for a pole vector. -/
theorem abs_inner_le_projection_residual
    (U : Submodule ℝ E) [U.HasOrthogonalProjection]
    {g w : E} {delta : ℝ} (hw : w ∈ Uᗮ)
    (hres : ‖g - U.starProjection g‖ ≤ delta) :
    |inner ℝ w g| ≤ delta * ‖w‖ := by
  have hzero : inner ℝ w (U.starProjection g) = 0 := by
    rw [real_inner_comm]
    exact Submodule.inner_right_of_mem_orthogonal
      (U.starProjection_apply_mem g) hw
  have hid : inner ℝ w g = inner ℝ w (g - U.starProjection g) := by
    rw [inner_sub_right, hzero, sub_zero]
  rw [hid]
  calc
    |inner ℝ w (g - U.starProjection g)| ≤
        ‖w‖ * ‖g - U.starProjection g‖ := abs_real_inner_le_norm _ _
    _ ≤ ‖w‖ * delta :=
      mul_le_mul_of_nonneg_left hres (norm_nonneg _)
    _ = delta * ‖w‖ := mul_comm _ _

section Form

variable (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
  [U.HasOrthogonalProjection]
  (C : E →L[ℝ] K) (D : K →ₗ[ℝ] K →ₗ[ℝ] ℝ)
  (gPlus gMinus : E) (alpha M rho G delta : ℝ)

/-- The complement block inequality follows from the band leakage and pole
projection residual estimates. -/
theorem clippedForm_complement_lower
    (hM0 : 0 ≤ M) (hrho0 : 0 ≤ rho)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x gPlus * inner ℝ y gMinus +
          inner ℝ x gMinus * inner ℝ y gPlus))
    (hleakSq : ∀ w ∈ Uᗮ, ‖C w‖ ^ 2 ≤ rho * ‖w‖ ^ 2)
    (hresPlus : ‖gPlus - U.starProjection gPlus‖ ≤ delta)
    (hresMinus : ‖gMinus - U.starProjection gMinus‖ ≤ delta) :
    ∀ w ∈ Uᗮ,
      FullInfAnalyticLedger.complementFloor alpha M rho delta * ‖w‖ ^ 2 ≤
        B w w := by
  intro w hw
  have hPlus := abs_inner_le_projection_residual U hw hresPlus
  have hMinus := abs_inner_le_projection_residual U hw hresMinus
  have hleak : ‖C w‖ ≤ Real.sqrt rho * ‖w‖ :=
    norm_le_sqrt_mul_of_sq_le hrho0 (norm_nonneg _) (norm_nonneg _)
      (hleakSq w hw)
  have hband := band_diagonal_lower D M rho (C w) ‖w‖
    hM0 hrho0 hD hleak
  have hpole := rankTwo_diagonal_lower gPlus gMinus w delta hPlus hMinus
  rw [hform, real_inner_self_eq_norm_sq]
  unfold FullInfAnalyticLedger.complementFloor
  nlinarith

/-- The low/high cross inequality follows from contraction of the band map,
band leakage, and the pole projection residuals. -/
theorem clippedForm_cross_bound
    (hM0 : 0 ≤ M) (hG0 : 0 ≤ G) (hdelta0 : 0 ≤ delta)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x gPlus * inner ℝ y gMinus +
          inner ℝ x gMinus * inner ℝ y gPlus))
    (hcontract : ∀ x, ‖C x‖ ≤ ‖x‖)
    (hleak : ∀ w ∈ Uᗮ, ‖C w‖ ≤ Real.sqrt rho * ‖w‖)
    (hgPlus : ‖gPlus‖ ≤ G) (hgMinus : ‖gMinus‖ ≤ G)
    (hresPlus : ‖gPlus - U.starProjection gPlus‖ ≤ delta)
    (hresMinus : ‖gMinus - U.starProjection gMinus‖ ≤ delta) :
    ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ FullInfAnalyticLedger.crossBound M rho G delta * ‖u‖ * ‖w‖ := by
  intro u hu w hw
  have horth : inner ℝ u w = 0 :=
    Submodule.inner_right_of_mem_orthogonal hu hw
  have hPlus := abs_inner_le_projection_residual U hw hresPlus
  have hMinus := abs_inner_le_projection_residual U hw hresMinus
  have hband := band_cross_bound D M rho (C u) (C w) ‖u‖ ‖w‖
    hM0 hD (hcontract u) (hleak w hw)
  have hpole := rankTwo_cross_bound gPlus gMinus u w G delta
    hG0 hdelta0 hgPlus hgMinus hPlus hMinus
  rw [hform, horth, mul_zero, zero_add]
  calc
    |D (C u) (C w) +
        (inner ℝ u gPlus * inner ℝ w gMinus +
          inner ℝ u gMinus * inner ℝ w gPlus)| ≤
        |D (C u) (C w)| +
          |inner ℝ u gPlus * inner ℝ w gMinus +
            inner ℝ u gMinus * inner ℝ w gPlus| := abs_add_le _ _
    _ ≤ M * Real.sqrt rho * ‖u‖ * ‖w‖ +
          2 * G * delta * ‖u‖ * ‖w‖ := add_le_add hband hpole
    _ = FullInfAnalyticLedger.crossBound M rho G delta * ‖u‖ * ‖w‖ := by
      unfold FullInfAnalyticLedger.crossBound
      ring

/-- Variant of `clippedForm_cross_bound` for a band map whose low-block norm
is bounded by `A‖u‖`. -/
theorem clippedForm_cross_bound_with_low
    (A : ℝ)
    (hM0 : 0 ≤ M) (hG0 : 0 ≤ G) (hdelta0 : 0 ≤ delta)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x gPlus * inner ℝ y gMinus +
          inner ℝ x gMinus * inner ℝ y gPlus))
    (hlow : ∀ x, ‖C x‖ ≤ A * ‖x‖)
    (hleak : ∀ w ∈ Uᗮ, ‖C w‖ ≤ Real.sqrt rho * ‖w‖)
    (hgPlus : ‖gPlus‖ ≤ G) (hgMinus : ‖gMinus‖ ≤ G)
    (hresPlus : ‖gPlus - U.starProjection gPlus‖ ≤ delta)
    (hresMinus : ‖gMinus - U.starProjection gMinus‖ ≤ delta) :
    ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤
        FullInfAnalyticLedger.crossBoundWithLow A M rho G delta * ‖u‖ * ‖w‖ := by
  intro u hu w hw
  have horth : inner ℝ u w = 0 :=
    Submodule.inner_right_of_mem_orthogonal hu hw
  have hPlus := abs_inner_le_projection_residual U hw hresPlus
  have hMinus := abs_inner_le_projection_residual U hw hresMinus
  have hband := band_cross_bound D M rho (C u) (C w) (A * ‖u‖) ‖w‖
    hM0 hD (hlow u) (hleak w hw)
  have hpole := rankTwo_cross_bound gPlus gMinus u w G delta
    hG0 hdelta0 hgPlus hgMinus hPlus hMinus
  rw [hform, horth, mul_zero, zero_add]
  calc
    |D (C u) (C w) +
        (inner ℝ u gPlus * inner ℝ w gMinus +
          inner ℝ u gMinus * inner ℝ w gPlus)| ≤
        |D (C u) (C w)| +
          |inner ℝ u gPlus * inner ℝ w gMinus +
            inner ℝ u gMinus * inner ℝ w gPlus| := abs_add_le _ _
    _ ≤ M * Real.sqrt rho * (A * ‖u‖) * ‖w‖ +
          2 * G * delta * ‖u‖ * ‖w‖ := add_le_add hband hpole
    _ = FullInfAnalyticLedger.crossBoundWithLow A M rho G delta *
          ‖u‖ * ‖w‖ := by
      unfold FullInfAnalyticLedger.crossBoundWithLow
      ring

/-- End-to-end abstract `p = 2` composition from a clipped-operator
decomposition, band leakage, pole projection residuals, and the finite block.
The remaining endpoint-specific work is now confined to constructing these
objects and proving the displayed decomposition and scalar enclosures. -/
theorem p2_projection_lower_bound_of_clipped_operator_ledger
    (hsymm : ∀ x y, B x y = B y x)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x gPlus * inner ℝ y gMinus +
          inner ℝ x gMinus * inner ℝ y gPlus))
    (hfinite : ∀ u ∈ U,
      (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hcontract : ∀ x, ‖C x‖ ≤ ‖x‖)
    (hleakSq : ∀ w ∈ Uᗮ, ‖C w‖ ^ 2 ≤ rho * ‖w‖ ^ 2)
    (hgPlus : ‖gPlus‖ ≤ G) (hgMinus : ‖gMinus‖ ≤ G)
    (hresPlus : ‖gPlus - U.starProjection gPlus‖ ≤ delta)
    (hresMinus : ‖gMinus - U.starProjection gMinus‖ ≤ delta)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  have hleak : ∀ w ∈ Uᗮ, ‖C w‖ ≤ Real.sqrt rho * ‖w‖ := by
    intro w hw
    exact norm_le_sqrt_mul_of_sq_le hrho0 (norm_nonneg _) (norm_nonneg _)
      (hleakSq w hw)
  apply FullInfAnalyticLedger.p2_projection_lower_bound_of_raw_analytic_ledger
    B U alpha M rho G delta hsymm hfinite
  · exact clippedForm_complement_lower
      (B := B) (U := U) (C := C) (D := D)
      (gPlus := gPlus) (gMinus := gMinus)
      (alpha := alpha) (M := M) (rho := rho) (delta := delta)
      hM0 hrho0 hD hform hleakSq hresPlus hresMinus
  · exact clippedForm_cross_bound
      (B := B) (U := U) (C := C) (D := D)
      (gPlus := gPlus) (gMinus := gMinus)
      (alpha := alpha) (M := M) (rho := rho) (G := G) (delta := delta)
      hM0 hG0 hdelta0 hD hform hcontract hleak hgPlus hgMinus
      hresPlus hresMinus
  · exact halpha
  · exact hM0
  · exact hM
  · exact hrho0
  · exact hrho
  · exact hG0
  · exact hG
  · exact hdelta0
  · exact hdelta
  · exact hf

/-- Plancherel-free endpoint composition.  A finite-band construction only
needs to prove `‖C x‖ ≤ 4‖x‖`; the exact low4 scalar ledger still yields the
same p=2 strict lower bound. -/
theorem p2_projection_lower_bound_of_clipped_operator_ledger_low4
    (hsymm : ∀ x y, B x y = B y x)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x gPlus * inner ℝ y gMinus +
          inner ℝ x gMinus * inner ℝ y gPlus))
    (hfinite : ∀ u ∈ U,
      (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hlow : ∀ x, ‖C x‖ ≤ 4 * ‖x‖)
    (hleakSq : ∀ w ∈ Uᗮ, ‖C w‖ ^ 2 ≤ rho * ‖w‖ ^ 2)
    (hgPlus : ‖gPlus‖ ≤ G) (hgMinus : ‖gMinus‖ ≤ G)
    (hresPlus : ‖gPlus - U.starProjection gPlus‖ ≤ delta)
    (hresMinus : ‖gMinus - U.starProjection gMinus‖ ≤ delta)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  have hleak : ∀ w ∈ Uᗮ, ‖C w‖ ≤ Real.sqrt rho * ‖w‖ := by
    intro w hw
    exact norm_le_sqrt_mul_of_sq_le hrho0 (norm_nonneg _) (norm_nonneg _)
      (hleakSq w hw)
  apply FullInfAnalyticLedger.p2_projection_lower_bound_of_raw_analytic_ledger_low4
    B U alpha M rho G delta hsymm hfinite
  · exact clippedForm_complement_lower
      (B := B) (U := U) (C := C) (D := D)
      (gPlus := gPlus) (gMinus := gMinus)
      (alpha := alpha) (M := M) (rho := rho) (delta := delta)
      hM0 hrho0 hD hform hleakSq hresPlus hresMinus
  · exact clippedForm_cross_bound_with_low
      (B := B) (U := U) (C := C) (D := D)
      (gPlus := gPlus) (gMinus := gMinus)
      (alpha := alpha) (M := M) (rho := rho) (G := G) (delta := delta)
      4 hM0 hG0 hdelta0 hD hform hlow hleak hgPlus hgMinus
      hresPlus hresMinus
  · exact halpha
  · exact hM0
  · exact hM
  · exact hrho0
  · exact hrho
  · exact hG0
  · exact hG
  · exact hdelta0
  · exact hdelta
  · exact hf

end Form

end FullInfOperatorLedger
