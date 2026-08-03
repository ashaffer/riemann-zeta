/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilFormula

/-!
# Classical literature inputs for the Guinand--Weil formula

This module deliberately isolates results taken from the classical analytic
number-theory literature rather than reproving their full analytic machinery
inside Mathlib.  Importing this module therefore changes the trust boundary:
the declarations below appear as named axioms in `#print axioms`.

The inputs are unconditional.  In particular, they assume neither RH nor
positivity of the Weil form.

The smooth explicit formula goes back to Guinand and Weil.  Standard modern
statements allow compactly supported piecewise `C²` tests, so the globally
smooth class below is a strict subclass.  The second input is its closure in
the logarithmic quadratic-form norm; this is the natural domain dictated by
the logarithmically growing archimedean multiplier.
-/

namespace RHP2Bridge.GuinandWeilLiterature

open scoped Topology

noncomputable section

open GuinandWeilFormula GeneralZetaWeilForm

/-- Classical Paley--Wiener input: a compactly supported smooth function has
an entire bilateral Laplace transform. -/
axiom smooth_bilateralLaplace_entire {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    Differentiable ℂ φ.bilateralLaplace

/-- The normalization-matched smooth Guinand--Weil explicit formula.  This
contains no assertion about the real parts of zeta zeros. -/
axiom smooth_guinandWeil_formula {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    Holds a φ.toTestSpace

/-- Correct low-regularity closure of the explicit formula.  The zero sum is
understood by symmetric exhaustion through closed disks, not as an
unconditionally convergent scalar series. -/
axiom logarithmicDomain_guinandWeil_formula {a : ℝ}
    (f : LogarithmicFormDomain a) :
    DiskHolds a f.val

theorem smooth_zero_sum_eq_weilForm {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    (∑' ρ : NontrivialZetaZero, zeroSummand a φ.toTestSpace ρ) =
      weilForm a φ.toTestSpace :=
  (smooth_guinandWeil_formula φ).2

theorem logarithmic_zero_disk_limit_eq_weilForm {a : ℝ}
    (f : LogarithmicFormDomain a) :
    Filter.Tendsto (fun R : ℝ ↦ zeroSumInDisk R a f.val) Filter.atTop
      (𝓝 (logarithmicWeilForm a f : ℂ)) := by
  simpa [DiskHolds, logarithmicWeilForm] using
    logarithmicDomain_guinandWeil_formula f

end

end RHP2Bridge.GuinandWeilLiterature
