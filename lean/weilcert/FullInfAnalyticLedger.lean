/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import FullInfLegendreLedger
import FullInfTransfer

/-!
# Scalar complement and cross ledgers for `FULLINF` at `L = 7/4`

The analytic transfer uses

* `alpha - M*rho - 2*delta^2` on the orthogonal complement, and
* `M*sqrt(rho) + 2*G*delta` for the low/high cross block.

This file checks the complete exact-real arithmetic turning the separately
proved bounds on `rho` and `delta`, together with simple directed bounds on
`alpha`, `M`, and `G`, into the rational F8 constants.  It deliberately does
not assert the zeta-specific identification of those analytic quantities.
-/

namespace FullInfAnalyticLedger

open scoped RealInnerProductSpace

/-- Complement diagonal produced by the clipped-symbol and pole estimates. -/
noncomputable def complementFloor (alpha M rho delta : ℝ) : ℝ :=
  alpha - M * rho - 2 * delta ^ 2

/-- Cross-block bound produced by band leakage and the two pole vectors. -/
noncomputable def crossBound (M rho G delta : ℝ) : ℝ :=
  M * Real.sqrt rho + 2 * G * delta

/-- Cross-block bound when the band map is only known to have low-block norm
at most `A`, rather than to be a contraction.  This weaker variant is useful
because at the p=2 endpoint the elementary finite-band estimate `A = 4`
already leaves enormous room in the final determinant. -/
noncomputable def crossBoundWithLow (A M rho G delta : ℝ) : ℝ :=
  A * M * Real.sqrt rho + 2 * G * delta

/-- A rational upper enclosure for the square root of the certified F2
leakage constant. -/
theorem sqrt_p2_rho_lt :
    Real.sqrt ((81 : ℝ) / 10 ^ 23) < (28461 : ℝ) / 10 ^ 15 := by
  rw [Real.sqrt_lt] <;> norm_num

/-- The complement scalar is strictly above `1.093` under the directed
endpoint enclosures used by the certificate. -/
theorem p2_complementFloor_gt
    {alpha M rho delta : ℝ}
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (_hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95) :
    (1093 : ℝ) / 1000 < complementFloor alpha M rho delta := by
  have hMrho : M * rho ≤
      ((7447 : ℝ) / 1000) * ((81 : ℝ) / 10 ^ 23) :=
    mul_le_mul hM hrho hrho0 (by norm_num)
  have hdeltaSq : delta ^ 2 ≤ ((195 : ℝ) / 10 ^ 95) ^ 2 := by
    exact pow_le_pow_left₀ hdelta0 hdelta 2
  unfold complementFloor
  have hrat :
      (1093 : ℝ) / 1000 <
        (109387 : ℝ) / 100000 -
          ((7447 : ℝ) / 1000) * ((81 : ℝ) / 10 ^ 23) -
            2 * ((195 : ℝ) / 10 ^ 95) ^ 2 := by
    norm_num
  nlinarith

/-- The low/high cross scalar is strictly below `2.12e-10` under the same
directed endpoint enclosures and the harmless pole-vector norm bound `G≤1`. -/
theorem p2_crossBound_lt
    {M rho G delta : ℝ}
    (_hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (_hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (_hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95) :
    crossBound M rho G delta < (212 : ℝ) / 10 ^ 12 := by
  have hsqrt0 : 0 ≤ Real.sqrt rho := Real.sqrt_nonneg _
  have hsqrt : Real.sqrt rho < (28461 : ℝ) / 10 ^ 15 :=
    (Real.sqrt_le_sqrt hrho).trans_lt sqrt_p2_rho_lt
  have hband : M * Real.sqrt rho <
      ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) := by
    calc
      M * Real.sqrt rho ≤
          ((7447 : ℝ) / 1000) * Real.sqrt rho :=
        mul_le_mul_of_nonneg_right hM hsqrt0
      _ < ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) :=
        mul_lt_mul_of_pos_left hsqrt (by norm_num)
  have hpole : 2 * G * delta ≤ 2 * 1 * ((195 : ℝ) / 10 ^ 95) := by
    gcongr
  unfold crossBound
  calc
    M * Real.sqrt rho + 2 * G * delta <
        ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) +
          2 * 1 * ((195 : ℝ) / 10 ^ 95) :=
      add_lt_add_of_lt_of_le hband hpole
    _ < (212 : ℝ) / 10 ^ 12 := by norm_num

/-- Even the elementary low-block band norm `‖C u‖ ≤ 4‖u‖` gives a
cross scalar below `8.5e-10`.  This avoids needing the full-line Plancherel
identification merely to retain the p=2 positivity conclusion. -/
theorem p2_crossBoundWithLow_four_lt
    {M rho G delta : ℝ}
    (_hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (_hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (_hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95) :
    crossBoundWithLow 4 M rho G delta < (85 : ℝ) / 10 ^ 11 := by
  have hsqrt0 : 0 ≤ Real.sqrt rho := Real.sqrt_nonneg _
  have hsqrt : Real.sqrt rho < (28461 : ℝ) / 10 ^ 15 :=
    (Real.sqrt_le_sqrt hrho).trans_lt sqrt_p2_rho_lt
  have hband : 4 * M * Real.sqrt rho <
      4 * ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) := by
    calc
      4 * M * Real.sqrt rho ≤
          4 * ((7447 : ℝ) / 1000) * Real.sqrt rho := by
        gcongr
      _ < 4 * ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) := by
        gcongr
  have hpole : 2 * G * delta ≤ 2 * 1 * ((195 : ℝ) / 10 ^ 95) := by
    gcongr
  unfold crossBoundWithLow
  calc
    4 * M * Real.sqrt rho + 2 * G * delta <
        4 * ((7447 : ℝ) / 1000) * ((28461 : ℝ) / 10 ^ 15) +
          2 * 1 * ((195 : ℝ) / 10 ^ 95) :=
      add_lt_add_of_lt_of_le hband hpole
    _ < (85 : ℝ) / 10 ^ 11 := by norm_num

/-- Both directed scalar conclusions packaged together. -/
theorem p2_complement_and_cross_ledger
    {alpha M rho G delta : ℝ}
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95) :
    (1093 : ℝ) / 1000 < complementFloor alpha M rho delta ∧
      crossBound M rho G delta < (212 : ℝ) / 10 ^ 12 :=
  ⟨p2_complementFloor_gt halpha hM0 hM hrho0 hrho hdelta0 hdelta,
    p2_crossBound_lt hM0 hM hrho0 hrho hG0 hG hdelta0 hdelta⟩

/-! ## Composition with the abstract F8 projection theorem -/

/-- Feed the raw clipped-symbol and pole expressions into the exact `p = 2`
projection ledger.  After this theorem, an analytic application need not
manually round the complement and cross constants: it supplies the natural
`complementFloor` and `crossBound` estimates and their directed scalar
enclosures. -/
theorem p2_projection_lower_bound_of_raw_analytic_ledger
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (alpha M rho G delta : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U,
      (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u)
    (hcomplementRaw : ∀ w ∈ Uᗮ,
      complementFloor alpha M rho delta * ‖w‖ ^ 2 ≤ B w w)
    (hcrossRaw : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ crossBound M rho G delta * ‖u‖ * ‖w‖)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  obtain ⟨hfloor, hcrossScalar⟩ :=
    p2_complement_and_cross_ledger halpha hM0 hM hrho0 hrho
      hG0 hG hdelta0 hdelta
  apply FullInfTransfer.fullinf_p2_projection_lower_bound
    B U hsymm hfinite
  · intro w hw
    calc
      (1093 / 1000 : ℝ) * ‖w‖ ^ 2 ≤
          complementFloor alpha M rho delta * ‖w‖ ^ 2 :=
        mul_le_mul_of_nonneg_right hfloor.le (sq_nonneg ‖w‖)
      _ ≤ B w w := hcomplementRaw w hw
  · intro u hu w hw
    calc
      |B u w| ≤ crossBound M rho G delta * ‖u‖ * ‖w‖ :=
        hcrossRaw u hu w hw
      _ ≤ (212 / 10 ^ 12 : ℝ) * ‖u‖ * ‖w‖ := by
        gcongr
  · exact hf

/-- A Plancherel-free p=2 composition.  It accepts the elementary low-band
constant `4`, uses the resulting (slightly larger) exact cross ledger, and
still proves the same final strict lower bound. -/
theorem p2_projection_lower_bound_of_raw_analytic_ledger_low4
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (alpha M rho G delta : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U,
      (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u)
    (hcomplementRaw : ∀ w ∈ Uᗮ,
      complementFloor alpha M rho delta * ‖w‖ ^ 2 ≤ B w w)
    (hcrossRaw : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ crossBoundWithLow 4 M rho G delta * ‖u‖ * ‖w‖)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    (hrho0 : 0 ≤ rho) (hrho : rho ≤ (81 : ℝ) / 10 ^ 23)
    (hG0 : 0 ≤ G) (hG : G ≤ 1)
    (hdelta0 : 0 ≤ delta) (hdelta : delta ≤ (195 : ℝ) / 10 ^ 95)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  have hfloor := p2_complementFloor_gt
    halpha hM0 hM hrho0 hrho hdelta0 hdelta
  have hcrossScalar := p2_crossBoundWithLow_four_lt
    hM0 hM hrho0 hrho hG0 hG hdelta0 hdelta
  apply FullInfTransfer.starProjection_strict_lower_bound B U
    (227 / 10 ^ 7) (1093 / 1000) (85 / 10 ^ 11) (22699 / 10 ^ 9)
    hsymm hfinite
  · intro w hw
    calc
      (1093 / 1000 : ℝ) * ‖w‖ ^ 2 ≤
          complementFloor alpha M rho delta * ‖w‖ ^ 2 :=
        mul_le_mul_of_nonneg_right hfloor.le (sq_nonneg ‖w‖)
      _ ≤ B w w := hcomplementRaw w hw
  · intro u hu w hw
    calc
      |B u w| ≤ crossBoundWithLow 4 M rho G delta * ‖u‖ * ‖w‖ :=
        hcrossRaw u hu w hw
      _ ≤ (85 / 10 ^ 11 : ℝ) * ‖u‖ * ‖w‖ := by
        gcongr
  · norm_num
  · norm_num
  · norm_num
  · exact hf

end FullInfAnalyticLedger
