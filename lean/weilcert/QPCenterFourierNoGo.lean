import Mathlib

/-!
# Exact ledgers for the center-convolution relaxation

The analytic DFT identities are finite-dimensional unitary invariance.  This
file mechanically checks the polynomial and exponent arithmetic used in the
countermodel and density audit.
-/

namespace QPCenterFourierNoGo

/-- Grouping an `r`-point interval by its additive sum costs asymptotically
`2r/3` relative to the square of its cardinality. -/
theorem repeatedRowRatio (r L : ℚ) (hr : r ≠ 0) :
    L ^ 2 * (2 * r ^ 3 + r) / 3 =
      (2 * r / 3 + 1 / (3 * r)) * (r * L) ^ 2 := by
  field_simp

/-- At the critical relation `q=D^(33/16)`, the fourth-power density gap
`D^3/q` has exponent `15/16`. -/
theorem criticalDensityGap : (3 : ℚ) - 33 / 16 = 15 / 16 := by
  norm_num

/-- Exact integer comparison in the finite hard-window fixture. -/
theorem finiteHardWindowGroupedExceedsTarget :
    (16060 : ℕ) > 33 * 16 ^ 2 := by
  norm_num

/-- The same finite fixture remains above the target after deleting
diagonal row pairs. -/
theorem finiteHardWindowOffDiagonalExceedsTarget :
    (12572 : ℕ) > 33 * 16 ^ 2 := by
  norm_num

/-- Its actual ungrouped row-pair energy is below the target. -/
theorem finiteHardWindowRowPairBelowTarget :
    (2310 : ℕ) < 33 * 16 ^ 2 := by
  norm_num

end QPCenterFourierNoGo
