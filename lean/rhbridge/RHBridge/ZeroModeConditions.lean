/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SuzukiEulerLagrange
import RHBridge.WeilCrossKernel

/-!
# Necessary conditions for a localized zero mode

A zero vector of a nonnegative quadratic form lies in its radical.  For the
zeta Weil form this forces an exact weak balance between the pole,
archimedean, and every active prime-shift trace.
-/

namespace RHP2Bridge.ZeroModeConditions

noncomputable section

open GeneralZetaWeilForm SupportDecomposition WeilCrossKernel

/-- Scalar radical lemma: if the quadratic polynomial on every line is
nonnegative and its old diagonal is zero, then its cross coefficient is zero. -/
theorem cross_eq_zero_of_zero_energy_line_nonnegative
    {C D : ℝ} (hline : ∀ t : ℝ, 0 ≤ 2 * t * C + t ^ 2 * D) :
    C = 0 := by
  have hD : 0 ≤ D := by
    nlinarith [hline 1, hline (-1)]
  have hline' : ∀ t : ℝ, 0 ≤ 0 + 2 * t * C + t ^ 2 * D := by
    simpa using hline
  have hdet := RelativeCrossNecessity.cross_sq_le_of_quadratic_nonneg
    (A := 0) (C := C) (D := D) (by norm_num)
    hD hline'
  nlinarith [sq_nonneg C]

/-- Exact weak Euler--Lagrange balance forced by a radical vector. -/
theorem pole_add_archimedean_eq_prime_of_weilCross_eq_zero
    {a : ℝ} {u v : TestSpace a} (hzero : weilCross a u v = 0) :
    poleCross a u v + archimedeanCross a u v = primeCross a u v := by
  rw [weilCross_eq_components] at hzero
  linarith

/-- Expanded distributional condition: the smooth pole/digamma trace equals
the finite sum of translated prime-power traces against every variation. -/
theorem pole_add_archimedean_eq_primeShift_sum
    {a : ℝ} {u v : TestSpace a} (hzero : weilCross a u v = 0) :
    poleCross a u v + archimedeanCross a u v =
      ∑ n ∈ activePrimePowers a, primePowerCross a n u v := by
  rw [← primeCross_eq_sum]
  exact pole_add_archimedean_eq_prime_of_weilCross_eq_zero hzero

/-- Fully expanded finite-delay equation with the exact von Mangoldt
coefficients and logarithmic shifts. -/
theorem pole_add_archimedean_eq_weighted_autocorrelationCross_sum
    {a : ℝ} {u v : TestSpace a} (hzero : weilCross a u v = 0) :
    poleCross a u v + archimedeanCross a u v =
      ∑ n ∈ activePrimePowers a,
        2 * ArithmeticFunction.vonMangoldt n / Real.sqrt n *
          autocorrelationCross a (Real.log n) u v := by
  rw [pole_add_archimedean_eq_primeShift_sum hzero]
  apply Finset.sum_congr rfl
  intro n _
  exact primePowerCross_eq a n u v

/-- Smooth Suzuki formulation of the same necessary condition. -/
theorem smooth_zeroMode_balance
    {a : ℝ} {φ ψ : GuinandWeilFormula.SmoothCompactSupportData a}
    (hradical : SuzukiEulerLagrange.polarizedScrewCross φ ψ = 0) :
    poleCross a φ.toTestSpace ψ.toTestSpace +
        archimedeanCross a φ.toTestSpace ψ.toTestSpace =
      ∑ n ∈ activePrimePowers a,
        primePowerCross a n φ.toTestSpace ψ.toTestSpace := by
  apply pole_add_archimedean_eq_primeShift_sum
  rw [← SuzukiEulerLagrange.polarizedScrewCross_eq_weilCross]
  exact hradical

end

end RHP2Bridge.ZeroModeConditions
