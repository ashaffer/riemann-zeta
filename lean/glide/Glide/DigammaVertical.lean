/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Digamma on positive vertical lines

This module contains only normalization-free facts about
`y ↦ re (Complex.digamma (a + I * y))`.  In particular it has no quarter-line,
prime, or certificate declarations.
-/

open Real Set
open scoped ComplexConjugate

namespace Complex

/-- Complex conjugation commutes with the derivative of `Gamma`. -/
lemma deriv_Gamma_conj (z : ℂ) :
    deriv Gamma (conj z) = conj (deriv Gamma z) := by
  have hfun : conj ∘ Gamma ∘ conj = Gamma := by
    funext w
    simp [Function.comp_apply, Gamma_conj]
  have h := congrFun (deriv_conj_conj (f := Gamma)) (conj z)
  rw [hfun] at h
  simpa [Function.comp_apply] using h

/-- The digamma function commutes with complex conjugation. -/
@[simp]
lemma digamma_conj (z : ℂ) : digamma (conj z) = conj (digamma z) := by
  rw [digamma_def]
  simp only [logDeriv_apply, deriv_Gamma_conj, Gamma_conj, map_div₀]

end Complex

namespace GlideKernel

/-- The real part of the digamma function on the vertical line `Re z = a`. -/
noncomputable def verticalDigammaReal (a y : ℝ) : ℝ :=
  (Complex.digamma ((a : ℂ) + Complex.I * (y : ℂ))).re

/-- Complex conjugation commutes with the derivative of Gamma. -/
lemma deriv_Gamma_conj (z : ℂ) :
    deriv Complex.Gamma (conj z) = conj (deriv Complex.Gamma z) :=
  Complex.deriv_Gamma_conj z

/-- The digamma function respects complex conjugation. -/
lemma digamma_conj (z : ℂ) :
    Complex.digamma (conj z) = conj (Complex.digamma z) :=
  Complex.digamma_conj z

/-- The real part of digamma on any vertical line is even. -/
lemma verticalDigammaReal_neg (a y : ℝ) :
    verticalDigammaReal a (-y) = verticalDigammaReal a y := by
  unfold verticalDigammaReal
  have hline :
      (a : ℂ) + Complex.I * ((-y : ℝ) : ℂ) =
        conj ((a : ℂ) + Complex.I * (y : ℂ)) := by
    simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I,
      Complex.ofReal_neg]
    ring
  rw [hline, Complex.digamma_conj]
  exact Complex.conj_re _

private lemma verticalLine_ne_neg_nat {a : ℝ} (ha : 0 < a) (y : ℝ) (m : ℕ) :
    (a : ℂ) + Complex.I * (y : ℂ) ≠ -(m : ℂ) := by
  intro h
  have hre := congrArg Complex.re h
  simp only [Complex.add_re, Complex.ofReal_re, Complex.mul_re, Complex.I_re,
    Complex.I_im, zero_mul, Complex.ofReal_im, mul_zero, sub_zero,
    Complex.neg_re, Complex.natCast_re] at hre
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
  linarith

/-- The real part of digamma is continuous along every vertical line in the
positive half-plane. -/
lemma continuousAt_verticalDigammaReal {a : ℝ} (ha : 0 < a) (y : ℝ) :
    ContinuousAt (verticalDigammaReal a) y := by
  let line : ℝ → ℂ := fun s ↦ (a : ℂ) + Complex.I * (s : ℂ)
  have hz : ∀ m : ℕ, line y ≠ -(m : ℂ) := by
    simpa only [line] using fun m ↦ verticalLine_ne_neg_nat ha y m
  have hGamma : AnalyticAt ℂ Complex.Gamma (line y) :=
    (Meromorphic.Gamma (line y)).analyticAt (Complex.continuousAt_Gamma (line y) hz)
  have hDigamma : ContinuousAt Complex.digamma (line y) := by
    rw [Complex.digamma_def]
    change ContinuousAt (fun z ↦ logDeriv Complex.Gamma z) (line y)
    simp only [logDeriv_apply]
    exact (hGamma.deriv.div hGamma (Complex.Gamma_ne_zero hz)).continuousAt
  have hline : ContinuousAt line y := by
    unfold line
    fun_prop
  unfold verticalDigammaReal
  change ContinuousAt (fun s ↦ (Complex.digamma (line s)).re) y
  exact Complex.continuous_re.continuousAt.comp (hDigamma.comp hline)

lemma continuous_verticalDigammaReal {a : ℝ} (ha : 0 < a) :
    Continuous (verticalDigammaReal a) :=
  continuous_iff_continuousAt.2 (continuousAt_verticalDigammaReal ha)

/-- Chain rule from a complex derivative of `digamma` to its real part along
the vertical line `Re z = a`. -/
lemma hasDerivAt_verticalDigammaReal_of_complex {a y : ℝ} {d : ℂ}
    (h : HasDerivAt Complex.digamma d ((a : ℂ) + Complex.I * (y : ℂ))) :
    HasDerivAt (verticalDigammaReal a) (Complex.I * d).re y := by
  have hline : HasDerivAt (fun z : ℂ ↦ (a : ℂ) + Complex.I * z)
      Complex.I (y : ℂ) := by
    simpa using (hasDerivAt_id (y : ℂ)).const_mul Complex.I |>.const_add (a : ℂ)
  have hcomp := h.comp (y : ℂ) hline
  have hreal := hcomp.real_of_complex
  unfold verticalDigammaReal
  simpa [Function.comp_def, mul_comm d Complex.I] using hreal

end GlideKernel
