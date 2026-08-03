/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# An elementary logarithmic-weight bound

This module keeps the Fourier logarithmic-weight estimate independent of the
smooth-cutoff construction with which it was originally used.
-/

namespace RHP2Bridge.ExplicitSmoothCutoff

/-- The logarithmic Fourier weight is bounded by the first-Sobolev quadratic
weight. -/
theorem logarithmicWeight_le_quadratic (ξ : ℝ) :
    0 ≤ Real.log (1 + (2 * Real.pi * ξ) ^ 2) ∧
      Real.log (1 + (2 * Real.pi * ξ) ^ 2) ≤ (2 * Real.pi * ξ) ^ 2 := by
  have hs : 0 ≤ (2 * Real.pi * ξ) ^ 2 := sq_nonneg _
  constructor
  · exact Real.log_nonneg (by linarith)
  · have hp : 0 < 1 + (2 * Real.pi * ξ) ^ 2 := by positivity
    simpa using Real.log_le_sub_one_of_pos hp

end RHP2Bridge.ExplicitSmoothCutoff
