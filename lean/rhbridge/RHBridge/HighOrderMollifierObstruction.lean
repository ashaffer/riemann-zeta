/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# High-order logarithmic mollifier obstruction

This file formalizes the elementary exponent ledger behind the
proportional-order mollifier audit.  It does not state or import a zero-free
criterion.

The stable entropy form of the naively isolated carrier is nonnegative.  More
importantly, at the outer edge of the critical strip its doubled exponent is
exactly the effective-support exponent of the tapered coefficients.  Hence a
mollifier-alone mean-value condition at natural scale leaves no strict outer
edge exponent surplus.
-/

namespace RHP2Bridge.HighOrderMollifierObstruction

noncomputable section

/-- Stable entropy form of the residue exponent.  In the complete high-order
Mellin argument this is only a diagnostic because a central pole at `w=1`
must also be retained. -/
def entropyCarrierRate (alpha delta : ℝ) : ℝ :=
  alpha * (delta / alpha - 1 - Real.log (delta / alpha))

/-- The entropy carrier is nonnegative for positive parameters. -/
theorem entropyCarrierRate_nonneg
    {alpha delta : ℝ} (halpha : 0 < alpha) (hdelta : 0 < delta) :
    0 ≤ entropyCarrierRate alpha delta := by
  unfold entropyCarrierRate
  have hx : 0 < delta / alpha := div_pos hdelta halpha
  have hlog : Real.log (delta / alpha) ≤ delta / alpha - 1 :=
    Real.log_le_sub_one_of_pos hx
  apply mul_nonneg halpha.le
  linarith

/-- The entropy carrier vanishes when the displacement equals the taper
shift. -/
@[simp] theorem entropyCarrierRate_self
    {alpha : ℝ} (halpha : alpha ≠ 0) :
    entropyCarrierRate alpha alpha = 0 := by
  simp [entropyCarrierRate, halpha]

/-- Algebraically convenient form of the naively isolated target carrier. -/
def naiveCarrierRate (alpha delta : ℝ) : ℝ :=
  delta + alpha * (Real.log (alpha / delta) - 1)

/-- Effective power exponent of the squared proportional-order cutoff in the
interior-saddle regime `0 < alpha < 1/2`. -/
def effectiveSupportExponent (alpha : ℝ) : ℝ :=
  1 - 2 * alpha + 2 * alpha * Real.log (2 * alpha)

/-- Exact repayment identity at the outer edge `delta = 1/2`. -/
theorem outerEdge_repayment (alpha : ℝ) :
    2 * naiveCarrierRate alpha (1 / 2) =
      effectiveSupportExponent alpha := by
  unfold naiveCarrierRate effectiveSupportExponent
  have hdiv : alpha / (1 / 2 : ℝ) = 2 * alpha := by ring
  rw [hdiv]
  ring

/-- If the mollifier-alone effective-support exponent is at the natural
mean-value threshold, the naively isolated outer-edge carrier has no strict
exponent surplus.  The complete Mellin argument is even less favorable
because it also contains the central residue polynomial. -/
theorem no_outerEdge_surplus
    {alpha theta : ℝ}
    (hmean : theta * effectiveSupportExponent alpha ≤ 1) :
    2 * theta * naiveCarrierRate alpha (1 / 2) ≤ 1 := by
  calc
    2 * theta * naiveCarrierRate alpha (1 / 2) =
        theta * (2 * naiveCarrierRate alpha (1 / 2)) := by ring
    _ = theta * effectiveSupportExponent alpha := by
      rw [outerEdge_repayment]
    _ ≤ 1 := hmean

/-- Reusing the first-order auxiliary kernel with a cutoff of order `k`
leaves a central Mellin pole of order `k-1`. -/
def centralMellinPoleOrder (k : ℕ) : ℕ := k - 1

@[simp] theorem centralMellinPoleOrder_zero :
    centralMellinPoleOrder 0 = 0 := rfl

@[simp] theorem centralMellinPoleOrder_one :
    centralMellinPoleOrder 1 = 0 := rfl

@[simp] theorem centralMellinPoleOrder_succ_succ (k : ℕ) :
    centralMellinPoleOrder (k + 2) = k + 1 := by
  simp [centralMellinPoleOrder]

end

end RHP2Bridge.HighOrderMollifierObstruction
