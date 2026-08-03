/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SupportDecomposition

/-!
# Polarized kernel decomposition of the zeta Weil form

This file separates the old/collar cross interaction into its pole,
archimedean, and prime-power pieces.  The signs are important: none of the
three pieces is asserted positive.  A Cauchy--Schwarz proof of propagation
must therefore produce a positive factorization of their *combined* kernel.
-/

namespace RHP2Bridge.WeilCrossKernel

noncomputable section

open scoped ArithmeticFunction
open GeneralZetaWeilForm SupportDecomposition

/-- Polarization of a real-valued quadratic functional. -/
def polarize {V : Type*} [Add V] (Q : V → ℝ) (u v : V) : ℝ :=
  (Q (u + v) - Q u - Q v) / 2

def poleCross (a : ℝ) (u v : TestSpace a) : ℝ :=
  polarize (poleTerm a) u v

def archimedeanCross (a : ℝ) (u v : TestSpace a) : ℝ :=
  polarize (archimedeanTerm a) u v

/-- Real polarization of the time-domain autocorrelation at one shift. -/
def autocorrelationCross (a t : ℝ) (u v : TestSpace a) : ℝ :=
  polarize (AutocorrelationPlancherel.intervalAutocorrelation a t) u v

def primePowerCross (a : ℝ) (n : ℕ) (u v : TestSpace a) : ℝ :=
  polarize (fun f ↦ primePowerTerm a f n) u v

def primeCross (a : ℝ) (u v : TestSpace a) : ℝ :=
  polarize (primeTerm a) u v

/-- The rank-two pole cross term, with all factors and signs explicit. -/
theorem poleCross_eq (a : ℝ) (u v : TestSpace a) :
    poleCross a u v =
      inner ℝ u (PoleProjection.polePlusL2 a) *
          inner ℝ v (PoleProjection.poleMinusL2 a) +
        inner ℝ u (PoleProjection.poleMinusL2 a) *
          inner ℝ v (PoleProjection.polePlusL2 a) := by
  simp only [poleCross, polarize, poleTerm, inner_add_left]
  ring

/-- Each arithmetic cross block is the polarized translation correlation
with the exact von Mangoldt normalization. -/
theorem primePowerCross_eq (a : ℝ) (n : ℕ) (u v : TestSpace a) :
    primePowerCross a n u v =
      2 * Λ n / Real.sqrt n *
        autocorrelationCross a (Real.log n) u v := by
  simp only [primePowerCross, autocorrelationCross, polarize, primePowerTerm]
  ring

/-- Polarization commutes with the finite prime-power sum. -/
theorem primeCross_eq_sum (a : ℝ) (u v : TestSpace a) :
    primeCross a u v =
      ∑ n ∈ activePrimePowers a, primePowerCross a n u v := by
  simp only [primeCross, polarize, primeTerm, primePowerCross]
  rw [← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib]
  simp_rw [div_eq_mul_inv]
  rw [← Finset.sum_mul]

/-- Exact combined-kernel formula.  In particular, the arithmetic cross
block enters with a minus sign. -/
theorem weilCross_eq_components (a : ℝ) (u v : TestSpace a) :
    weilCross a u v =
      poleCross a u v + archimedeanCross a u v - primeCross a u v := by
  simp only [weilCross, poleCross, archimedeanCross, primeCross, polarize,
    weilForm]
  ring

/-- Expanded form displaying every active prime-power cross interaction. -/
theorem weilCross_eq_kernel_sum (a : ℝ) (u v : TestSpace a) :
    weilCross a u v = poleCross a u v + archimedeanCross a u v -
      ∑ n ∈ activePrimePowers a, primePowerCross a n u v := by
  rw [weilCross_eq_components, primeCross_eq_sum]

end

end RHP2Bridge.WeilCrossKernel
