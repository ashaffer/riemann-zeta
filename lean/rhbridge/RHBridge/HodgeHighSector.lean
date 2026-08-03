/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LowEnergySector
import RHBridge.IncidenceCycleObstruction

/-!
# The high-incidence part of the Hodge loss

Let `S` be the positive old incidence operator, let `q2` be the one-event
shell increment, and put

`tau = sqrt (S / (S + q2 I))`, `K = I - tau`.

On the spectral subspace `S >= cutoff I`, functional calculus bounds `K^2`
by

`q2^2 / (4 * cutoff * (cutoff + q2))`.

The final theorem below records a noncircular way to spend this loss.  An
ordinary `L²` cross estimate consumes `d` units of a collar floor, while the
Hodge trace consumes the additional explicitly displayed `m * y2` units.
No positivity of the desired Weil--Schur complement is assumed.
-/

namespace RHP2Bridge.HodgeHighSector

noncomputable section

open LowEnergySector

/-- Rational upper bound for the squared Hodge multiplier above an incidence
cutoff.  Here `q2` denotes `q^2`, so its square is the `q^4` numerator in the
usual notation. -/
def highHodgeMultiplier (cutoff q2 : ℝ) : ℝ :=
  q2 ^ 2 / (4 * cutoff * (cutoff + q2))

/-- Exact squared norm of the Hodge multiplier on the spectral half-line
`[cutoff, ∞)`. -/
def exactHighHodgeMultiplier (cutoff q2 : ℝ) : ℝ :=
  (1 - Real.sqrt (cutoff / (cutoff + q2))) ^ 2

theorem highHodgeMultiplier_nonneg
    {cutoff q2 : ℝ} (hcutoff : 0 < cutoff) (hq2 : 0 ≤ q2) :
    0 ≤ highHodgeMultiplier cutoff q2 := by
  unfold highHodgeMultiplier
  positivity

/-- The sharp rational form of scalar Hodge smoothing.  It improves the
`S^-2` estimate by retaining the additional `(s + q2)` denominator. -/
theorem scalar_hodge_loss_sharp
    {s q2 tau : ℝ} (hs : 0 < s) (hq2 : 0 ≤ q2)
    (htau : 0 ≤ tau) (htau_sq : tau ^ 2 * (s + q2) = s) :
    (1 - tau) ^ 2 ≤ q2 ^ 2 / (4 * s * (s + q2)) := by
  have hsum : 0 < s + q2 := by linarith
  have htau_sq_le_one : tau ^ 2 ≤ 1 := by
    apply le_of_mul_le_mul_right _ hsum
    rw [htau_sq]
    nlinarith
  have htau_le_one : tau ≤ 1 := by
    nlinarith [sq_nonneg (tau + 1)]
  have hone : 0 ≤ 1 - tau := sub_nonneg.mpr htau_le_one
  have hfactor : q2 = (1 - tau ^ 2) * (s + q2) := by
    nlinarith [htau_sq]
  have hbase : 0 ≤ (1 - tau) * (s + q2) :=
    mul_nonneg hone hsum.le
  have hlinear :
      2 * tau * ((1 - tau) * (s + q2)) ≤ q2 := by
    have hfactor' :
        (1 - tau ^ 2) * (s + q2) =
          (1 + tau) * ((1 - tau) * (s + q2)) := by ring
    calc
      2 * tau * ((1 - tau) * (s + q2)) ≤
          (1 + tau) * ((1 - tau) * (s + q2)) :=
        mul_le_mul_of_nonneg_right (by linarith) hbase
      _ = (1 - tau ^ 2) * (s + q2) := hfactor'.symm
      _ = q2 := hfactor.symm
  have hlinear_nonneg :
      0 ≤ 2 * tau * ((1 - tau) * (s + q2)) := by positivity
  have hsquare :
      (2 * tau * ((1 - tau) * (s + q2))) ^ 2 ≤ q2 ^ 2 :=
    (sq_le_sq₀ hlinear_nonneg hq2).2 hlinear
  have hden : 0 < 4 * s * (s + q2) := by positivity
  apply (le_div_iff₀ hden).2
  calc
    (1 - tau) ^ 2 * (4 * s * (s + q2)) =
        4 * (1 - tau) ^ 2 * s * (s + q2) := by ring
    _ = 4 * (1 - tau) ^ 2 * (tau ^ 2 * (s + q2)) * (s + q2) := by
      rw [htau_sq]
    _ = (2 * tau * ((1 - tau) * (s + q2))) ^ 2 := by ring
    _ ≤ q2 ^ 2 := hsquare

/-- Square-root specialization of the sharp rational smoothing law. -/
theorem scalar_hodge_sqrt_loss_sharp
    {s q2 : ℝ} (hs : 0 < s) (hq2 : 0 ≤ q2) :
    (1 - Real.sqrt (s / (s + q2))) ^ 2 ≤
      q2 ^ 2 / (4 * s * (s + q2)) := by
  apply scalar_hodge_loss_sharp hs hq2 (Real.sqrt_nonneg _)
  rw [Real.sq_sqrt (div_nonneg hs.le (by linarith : 0 ≤ s + q2))]
  field_simp

/-- The exact high-half-line multiplier is bounded by the rational constant
used in the operator budget. -/
theorem exactHighHodgeMultiplier_le
    {cutoff q2 : ℝ} (hcutoff : 0 < cutoff) (hq2 : 0 ≤ q2) :
    exactHighHodgeMultiplier cutoff q2 ≤
      highHodgeMultiplier cutoff q2 := by
  exact scalar_hodge_sqrt_loss_sharp hcutoff hq2

/-- The sharp smoothing majorant decreases when the incidence spectral
cutoff is raised. -/
theorem highHodgeMultiplier_anti
    {cutoff s q2 : ℝ} (hcutoff : 0 < cutoff)
    (hcs : cutoff ≤ s) (hq2 : 0 ≤ q2) :
    q2 ^ 2 / (4 * s * (s + q2)) ≤
      highHodgeMultiplier cutoff q2 := by
  unfold highHodgeMultiplier
  have hs : 0 < s := hcutoff.trans_le hcs
  have hleft : 0 < 4 * s * (s + q2) := by positivity
  have hright : 0 < 4 * cutoff * (cutoff + q2) := by positivity
  apply (div_le_div_iff₀ hleft hright).2
  have hsum_le : cutoff + q2 ≤ s + q2 := by linarith
  have hproduct :
      cutoff * (cutoff + q2) ≤ s * (s + q2) :=
    mul_le_mul hcs hsum_le
      (add_nonneg hcutoff.le hq2) hs.le
  have hden :
      4 * cutoff * (cutoff + q2) ≤ 4 * s * (s + q2) := by
    nlinarith
  exact mul_le_mul_of_nonneg_left hden (sq_nonneg q2)

/-- Pointwise eigenvalue form of the high-incidence Hodge estimate. -/
theorem scalar_hodge_loss_on_high_incidence
    {cutoff s q2 tau : ℝ} (hcutoff : 0 < cutoff)
    (hcs : cutoff ≤ s) (hq2 : 0 ≤ q2)
    (htau : 0 ≤ tau) (htau_sq : tau ^ 2 * (s + q2) = s) :
    (1 - tau) ^ 2 ≤ highHodgeMultiplier cutoff q2 := by
  exact (scalar_hodge_loss_sharp (hcutoff.trans_le hcs) hq2 htau htau_sq).trans
    (highHodgeMultiplier_anti hcutoff hcs hq2)

/-- A high incidence cutoff for `S` becomes a high old-Weil-energy cutoff
for `Q_a = S - degree * I`. -/
theorem high_incidence_implies_high_weil
    {incidenceEnergy oldEnergy normSq cutoff degree : ℝ}
    (hincidence : cutoff * normSq ≤ incidenceEnergy)
    (hold : oldEnergy = incidenceEnergy - degree * normSq) :
    (cutoff - degree) * normSq ≤ oldEnergy := by
  rw [hold]
  linarith

/-- Operator-ready pointwise estimate.  In an application,
`highTraceNormSq = ‖P_high Y w‖²` and `y2` is an upper bound for
`‖P_high Y‖²`. -/
theorem high_hodge_trace_loss_bound
    {loss highTraceNormSq collarNormSq multiplier y2 : ℝ}
    (hm : 0 ≤ multiplier)
    (hloss : loss ≤ multiplier * highTraceNormSq)
    (htrace : highTraceNormSq ≤ y2 * collarNormSq) :
    loss ≤ (multiplier * y2) * collarNormSq := by
  calc
    loss ≤ multiplier * highTraceNormSq := hloss
    _ ≤ multiplier * (y2 * collarNormSq) :=
      mul_le_mul_of_nonneg_left htrace hm
    _ = (multiplier * y2) * collarNormSq := by ring

/-- High-sector Schur estimate after paying an additional collar reserve for
the Hodge loss.  Unlike an assumption on the Schur surplus, all hypotheses
are estimates on the unminimized old/collar block.

The ordinary cross term costs `d * collarNormSq`; the Hodge penalty costs
`j * collarNormSq`. -/
theorem modified_block_nonnegative_on_highEnergy
    {oldEnergy collarEnergy cross oldNormSq collarNormSq
      hodgeLoss mu d c j : ℝ}
    (hmu : 0 ≤ mu) (hd : 0 ≤ d) (hc : 0 ≤ c)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hOld : IsHighEnergy mu oldEnergy oldNormSq)
    (hCollar : (d + j) * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hconstant : c ^ 2 ≤ mu * d)
    (hLoss : hodgeLoss ≤ j * collarNormSq) :
    0 ≤ oldEnergy + 2 * cross + collarEnergy - hodgeLoss := by
  have hPaid : d * collarNormSq ≤ collarEnergy - hodgeLoss := by
    nlinarith
  have hPaidNonneg : 0 ≤ collarEnergy - hodgeLoss :=
    (mul_nonneg hd hnCollar).trans hPaid
  have hdet :
      cross ^ 2 ≤ oldEnergy * (collarEnergy - hodgeLoss) :=
    cross_sq_le_on_highEnergy hmu hd hc hnOld hnCollar hOld hPaid
      hCross hconstant
  have hquad := SupportDecomposition.add_two_mul_nonneg_of_cross_sq_le
    ((mul_nonneg hmu hnOld).trans hOld) hPaidNonneg hdet
  linarith

/-- Combined high-incidence closure criterion with the Hodge multiplier and
the norm of the high return trace displayed explicitly. -/
theorem modified_block_nonnegative_of_high_hodge_trace
    {oldEnergy collarEnergy cross oldNormSq collarNormSq hodgeLoss
      highTraceNormSq mu d c multiplier y2 : ℝ}
    (hmu : 0 ≤ mu) (hd : 0 ≤ d) (hc : 0 ≤ c)
    (hm : 0 ≤ multiplier)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hOld : IsHighEnergy mu oldEnergy oldNormSq)
    (hCollar : (d + multiplier * y2) * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hconstant : c ^ 2 ≤ mu * d)
    (hloss : hodgeLoss ≤ multiplier * highTraceNormSq)
    (htrace : highTraceNormSq ≤ y2 * collarNormSq) :
    0 ≤ oldEnergy + 2 * cross + collarEnergy - hodgeLoss := by
  exact modified_block_nonnegative_on_highEnergy hmu hd hc hnOld hnCollar
    hOld hCollar hCross hconstant
    (high_hodge_trace_loss_bound hm hloss htrace)

/-- Solving the high-sector constant exactly: if `floor` is the collar
`L²` floor and `j < floor` is reserved for the Hodge loss, every old vector
above the energy cutoff

`mu_high = c^2 / (floor - j)`

is closed by the ordinary cross estimate. -/
theorem modified_block_nonnegative_above_explicit_cutoff
    {oldEnergy collarEnergy cross oldNormSq collarNormSq
      hodgeLoss floor j c : ℝ}
    (hc : 0 ≤ c) (hnOld : 0 ≤ oldNormSq)
    (hnCollar : 0 ≤ collarNormSq) (hgap : j < floor)
    (hOld : IsHighEnergy (c ^ 2 / (floor - j)) oldEnergy oldNormSq)
    (hCollar : floor * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hLoss : hodgeLoss ≤ j * collarNormSq) :
    0 ≤ oldEnergy + 2 * cross + collarEnergy - hodgeLoss := by
  have hd : 0 ≤ floor - j := sub_nonneg.mpr hgap.le
  have hdpos : 0 < floor - j := sub_pos.mpr hgap
  have hmu : 0 ≤ c ^ 2 / (floor - j) := div_nonneg (sq_nonneg c) hd
  have hconstant :
      c ^ 2 ≤ (c ^ 2 / (floor - j)) * (floor - j) := by
    rw [div_mul_cancel₀ (c ^ 2) (ne_of_gt hdpos)]
  apply modified_block_nonnegative_on_highEnergy
    (mu := c ^ 2 / (floor - j)) (d := floor - j) (c := c) (j := j)
    hmu hd hc hnOld hnCollar hOld
  · convert hCollar using 1
    ring
  · exact hCross
  · exact hconstant
  · exact hLoss

/-- Fully explicit high-incidence/Hodge cutoff.  The return-trace constant is
`y2 = ‖P_high Y‖²`, and the Hodge reserve is

`j = highHodgeMultiplier cutoff q2 * y2`.

The only analytic inputs left are the raw collar floor and ordinary `L²`
cross bound; no Weil--Schur positivity occurs among the hypotheses. -/
theorem modified_block_nonnegative_above_hodge_cutoff
    {oldEnergy collarEnergy cross oldNormSq collarNormSq hodgeLoss
      highTraceNormSq cutoff q2 y2 floor c : ℝ}
    (hcutoff : 0 < cutoff) (hq2 : 0 ≤ q2)
    (hc : 0 ≤ c) (hnOld : 0 ≤ oldNormSq)
    (hnCollar : 0 ≤ collarNormSq)
    (hgap : highHodgeMultiplier cutoff q2 * y2 < floor)
    (hOld : IsHighEnergy
      (c ^ 2 / (floor - highHodgeMultiplier cutoff q2 * y2))
      oldEnergy oldNormSq)
    (hCollar : floor * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hloss : hodgeLoss ≤
      highHodgeMultiplier cutoff q2 * highTraceNormSq)
    (htrace : highTraceNormSq ≤ y2 * collarNormSq) :
    0 ≤ oldEnergy + 2 * cross + collarEnergy - hodgeLoss := by
  have hm := highHodgeMultiplier_nonneg hcutoff hq2
  apply modified_block_nonnegative_above_explicit_cutoff hc hnOld hnCollar
    hgap hOld hCollar hCross
  exact high_hodge_trace_loss_bound hm hloss htrace

/-- The compact-resolvent high-tail budget in its directly usable form.

On `Q_a ≥ mu I`, minimizing the ordinary cross term costs at most
`crossNorm^2 / mu` units of collar `L²` energy.  On the corresponding
incidence sector `S = Q_a + degree * I ≥ (mu + degree) I`, the Hodge
penalty costs at most

`highHodgeMultiplier (mu + degree) q2 * returnNormSq`.

Thus their sum fitting below the raw collar floor closes the entire high
tail.  Dividing `hbudget` by `collarFloor` gives the dimensionless estimate

`crossNorm^2 / (collarFloor * mu)
  + q2^2 * returnNormSq /
      (4 * collarFloor * (mu + degree) * (mu + degree + q2)) ≤ 1`.

Replacing the last denominator by `(mu + degree)^2` is a slightly stronger
but simpler sufficient condition. -/
theorem modified_block_nonnegative_of_high_tail_budget
    {oldEnergy collarEnergy cross oldNormSq collarNormSq hodgeLoss
      highTraceNormSq mu degree q2 returnNormSq collarFloor crossNorm : ℝ}
    (hmu : 0 < mu) (hincidence : 0 < mu + degree) (hq2 : 0 ≤ q2)
    (hcrossNorm : 0 ≤ crossNorm)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hOld : IsHighEnergy mu oldEnergy oldNormSq)
    (hCollar : collarFloor * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤
      crossNorm * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hloss : hodgeLoss ≤
      highHodgeMultiplier (mu + degree) q2 * highTraceNormSq)
    (htrace : highTraceNormSq ≤ returnNormSq * collarNormSq)
    (hbudget : crossNorm ^ 2 / mu +
      highHodgeMultiplier (mu + degree) q2 * returnNormSq ≤ collarFloor) :
    0 ≤ oldEnergy + 2 * cross + collarEnergy - hodgeLoss := by
  let crossCost := crossNorm ^ 2 / mu
  let hodgeCost := highHodgeMultiplier (mu + degree) q2 * returnNormSq
  have hcrossCost : 0 ≤ crossCost := by
    dsimp [crossCost]
    positivity
  have hm : 0 ≤ highHodgeMultiplier (mu + degree) q2 :=
    highHodgeMultiplier_nonneg hincidence hq2
  have hconstant : crossNorm ^ 2 ≤ mu * crossCost := by
    dsimp [crossCost]
    rw [mul_div_cancel₀ (crossNorm ^ 2) (ne_of_gt hmu)]
  have hcostCollar :
      (crossCost + hodgeCost) * collarNormSq ≤ collarEnergy := by
    calc
      (crossCost + hodgeCost) * collarNormSq ≤
          collarFloor * collarNormSq :=
        mul_le_mul_of_nonneg_right hbudget hnCollar
      _ ≤ collarEnergy := hCollar
  have hLossCost : hodgeLoss ≤ hodgeCost * collarNormSq := by
    dsimp [hodgeCost]
    exact high_hodge_trace_loss_bound hm hloss htrace
  exact modified_block_nonnegative_on_highEnergy hmu.le hcrossCost
    hcrossNorm hnOld hnCollar hOld hcostCollar hCross hconstant hLossCost

/-- Quantitative lower bound before spending the collar diagonal.  Completing
the high old variable and paying its Hodge trace can decrease the remaining
low-sector collar form by at most

`crossNorm^2 / mu + hodgeCost`.

This is the correct bookkeeping for composing the high-tail argument with a
separate low-sector contraction. -/
theorem high_tail_lower_bound
    {oldEnergy cross oldNormSq collarNormSq hodgeLoss
      mu crossNorm hodgeCost : ℝ}
    (hmu : 0 < mu) (hcrossNorm : 0 ≤ crossNorm)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hOld : IsHighEnergy mu oldEnergy oldNormSq)
    (hCross : |cross| ≤
      crossNorm * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hLoss : hodgeLoss ≤ hodgeCost * collarNormSq) :
    -(crossNorm ^ 2 / mu + hodgeCost) * collarNormSq ≤
      oldEnergy + 2 * cross - hodgeLoss := by
  let crossCost := crossNorm ^ 2 / mu
  have hcrossCost : 0 ≤ crossCost := by
    dsimp [crossCost]
    positivity
  have hconstant : crossNorm ^ 2 ≤ mu * crossCost := by
    dsimp [crossCost]
    rw [mul_div_cancel₀ (crossNorm ^ 2) (ne_of_gt hmu)]
  have h := modified_block_nonnegative_on_highEnergy
    (mu := mu) (d := crossCost) (c := crossNorm) (j := hodgeCost)
    hmu.le hcrossCost hcrossNorm hnOld hnCollar hOld
    (le_refl ((crossCost + hodgeCost) * collarNormSq))
    hCross hconstant hLoss
  dsimp [crossCost] at h ⊢
  linarith

/-- Exact scalar composition rule.  Once the high-tail cost has been
deducted, proving the Hodge-modified low block against the residual collar
energy proves the complete block. -/
theorem high_low_modified_blocks_compose
    {highEnergy lowEnergy collarEnergy highCross lowCross
      highLoss lowLoss collarCost : ℝ}
    (hHigh : -collarCost ≤ highEnergy + 2 * highCross - highLoss)
    (hLow : 0 ≤ lowEnergy + 2 * lowCross + collarEnergy -
      collarCost - lowLoss) :
    0 ≤ highEnergy + lowEnergy + 2 * (highCross + lowCross) +
      collarEnergy - (highLoss + lowLoss) := by
  linarith

/-- Exact quotient-side reserve still required if one works after taking the
old-variable Schur complement: it must dominate the high-trace loss itself.
This small lemma is included to prevent replacing that requirement by mere
nonnegativity of the surplus. -/
theorem high_hodge_loss_of_schur_reserve
    {schurSurplus hodgeLoss highReturn multiplier : ℝ}
    (hloss : hodgeLoss ≤ multiplier * highReturn)
    (hreserve : multiplier * highReturn ≤ schurSurplus) :
    hodgeLoss ≤ schurSurplus :=
  hloss.trans hreserve

end

end RHP2Bridge.HodgeHighSector
