/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilFormula

/-!
# Fixed-window moment savings imply symmetric zero-free strips

This file formalizes only the exact exponent arithmetic. It does not assume or
prove the open completed fourth-moment estimate. The analytic input is isolated
as a horizontal-displacement bound for all nontrivial zeta zeros.
-/

namespace RHP2Bridge.FixedWindowStripReduction

open GuinandWeilFormula

noncomputable section

/-- Every nontrivial zero lies in the closed strip
`eta ≤ re rho ≤ 1 - eta`. -/
def NontrivialZerosInClosedStrip (eta : ℝ) : Prop :=
  ∀ rho : NontrivialZetaZero,
    eta ≤ rho.val.re ∧ rho.val.re ≤ 1 - eta

/-- Every nontrivial zero has horizontal displacement at most `delta` from the
critical line. -/
def HorizontalDisplacementAtMost (delta : ℝ) : Prop :=
  ∀ rho : NontrivialZetaZero,
    |rho.val.re - 1 / 2| ≤ delta

/-- A displacement bound `delta ≤ 1/2 - eta` gives the corresponding
symmetric zero-free strip. -/
theorem closedStrip_of_displacementAtMost
    {delta eta : ℝ}
    (hdisp : HorizontalDisplacementAtMost delta)
    (hdelta : delta ≤ 1 / 2 - eta) :
    NontrivialZerosInClosedStrip eta := by
  intro rho
  have hbounds := (abs_le.mp (hdisp rho))
  constructor <;> linarith

/-- The exact full-frequency fourth-moment exponent implication used by the
fixed-strip sprint: if the analytic argument gives
`4 * Delta ≤ 2 - kappa`, then all nontrivial zeros lie in
`kappa/4 ≤ re rho ≤ 1 - kappa/4`. -/
theorem closedStrip_of_fullFourthMomentExponent
    {Delta kappa : ℝ}
    (hdisp : HorizontalDisplacementAtMost Delta)
    (hexponent : 4 * Delta ≤ 2 - kappa) :
    NontrivialZerosInClosedStrip (kappa / 4) := by
  apply closedStrip_of_displacementAtMost hdisp
  linarith

/-- Localization of every nontrivial zero on the critical line, stated in the
same subtype language as the zero-side formalization. -/
def CriticalLineLocalization : Prop :=
  ∀ rho : NontrivialZetaZero, rho.val.re = 1 / 2

/-- If symmetric strips are available for every saving `0 < kappa < 2`, their
intersection is the critical line. This is the logical full-RH endpoint of the
fixed-window fourth-moment program; proving the required family of arithmetic
moment estimates remains the substantive open input. -/
theorem criticalLineLocalization_of_allFourthMomentSavings
    (hstrip : ∀ kappa : ℝ, 0 < kappa → kappa < 2 →
      NontrivialZerosInClosedStrip (kappa / 4)) :
    CriticalLineLocalization := by
  intro rho
  by_contra hne
  let displacement : ℝ := |rho.val.re - 1 / 2|
  have hdisplacement_pos : 0 < displacement := by
    dsimp [displacement]
    exact abs_pos.mpr (sub_ne_zero.mpr hne)
  have hlower : -(1 / 2 : ℝ) < rho.val.re - 1 / 2 := by
    linarith [rho.property.2.1]
  have hupper : rho.val.re - 1 / 2 < (1 / 2 : ℝ) := by
    linarith [rho.property.2.2]
  have hdisplacement_lt_half : displacement < 1 / 2 := by
    dsimp [displacement]
    exact (abs_lt.mpr ⟨hlower, hupper⟩)
  let kappa : ℝ := 2 - 2 * displacement
  have hkappa_pos : 0 < kappa := by
    dsimp [kappa]
    linarith
  have hkappa_lt_two : kappa < 2 := by
    dsimp [kappa]
    linarith
  rcases hstrip kappa hkappa_pos hkappa_lt_two rho with
    ⟨hstrip_lower, hstrip_upper⟩
  have hdisplacement_bound :
      displacement ≤ 1 / 2 - kappa / 4 := by
    dsimp [displacement]
    apply abs_le.mpr
    constructor <;> linarith
  dsimp [kappa] at hdisplacement_bound
  linarith

end

end RHP2Bridge.FixedWindowStripReduction
