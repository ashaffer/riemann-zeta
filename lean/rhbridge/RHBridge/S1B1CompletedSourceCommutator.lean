/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring

/-!
# Finite algebra for the S1-B1 completed-source commutator audit

This file proves only the finite operator identities used by the audit:

* a multiplication/convolution commutator weights each kernel entry by a
  window difference;
* the source reconstruction obtained by adding the residual is tautological;
* commuting a reflection-odd projector with a multiplier gives a reflected
  copy of the original source times an explicit multiplier difference; and
* two such reflection commutators collapse back to scalar multiplication.

No analytic R71 estimate, completed-zeta identity, zero-free strip, or
statement of RH is formalized or proved here.
-/

namespace RHBridge.S1B1CompletedSourceCommutator

noncomputable section

section FiniteKernel

variable {ι : Type*} [Fintype ι]

/-- A finite kernel operator.  The divisor-incidence matrix used in the
arithmetic application is one instance. -/
def kernelOp (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι) : ℂ :=
  ∑ y, K x y * f y

/-- Pointwise multiplication by a window. -/
def multiplierOp (w f : ι → ℂ) (x : ι) : ℂ := w x * f x

/-- The convention `[M_w,T_K]=M_w T_K-T_K M_w`. -/
def windowKernelCommutator
    (w : ι → ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι) : ℂ :=
  multiplierOp w (kernelOp K f) x - kernelOp K (multiplierOp w f) x

/-- Exact kernel-difference formula for a finite window commutator. -/
theorem windowKernelCommutator_eq
    (w : ι → ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι) :
    windowKernelCommutator w K f x =
      ∑ y, K x y * (w x - w y) * f y := by
  simp only [windowKernelCommutator, multiplierOp, kernelOp, Finset.mul_sum]
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro y _
  ring

/-- Adding the inner-weight residual reconstructs the original windowed
source exactly.  This is an identity, not a strict adapter. -/
theorem source_reconstruction
    (w : ι → ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι) :
    windowKernelCommutator w K f x + kernelOp K (multiplierOp w f) x =
      multiplierOp w (kernelOp K f) x := by
  simp [windowKernelCommutator]

/-- If the inner-weight residual vanishes after a chosen output compression,
the commutator is exactly the original windowed source.  The number-theoretic
narrow-shell support check establishing this hypothesis is kept in the human
and executable audits. -/
theorem commutator_eq_source_of_residual_zero
    (w : ι → ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι)
    (hzero : kernelOp K (multiplierOp w f) x = 0) :
    windowKernelCommutator w K f x =
      multiplierOp w (kernelOp K f) x := by
  have h := source_reconstruction w K f x
  rw [hzero, add_zero] at h
  exact h

/-- A constant window has no commutator information. -/
theorem constant_window_commutator_zero
    (c : ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι) :
    windowKernelCommutator (fun _ => c) K f x = 0 := by
  rw [windowKernelCommutator_eq]
  simp

/-- More generally, if the window is constant on every kernel edge entering
`x`, the commutator vanishes at `x`.  Hard initial divisor cutoffs have this
property after compression to their interior. -/
theorem commutator_zero_of_edgewise_constant
    (w : ι → ℂ) (K : ι → ι → ℂ) (f : ι → ℂ) (x : ι)
    (h : ∀ y, K x y ≠ 0 → w x = w y) :
    windowKernelCommutator w K f x = 0 := by
  rw [windowKernelCommutator_eq]
  apply Finset.sum_eq_zero
  intro y _
  by_cases hK : K x y = 0
  · simp [hK]
  · simp [h y hK]

end FiniteKernel

section Reflection

variable {ι : Type*}

/-- Pullback by a chosen reflection. -/
def reflectOp (r : ι → ι) (f : ι → ℂ) (x : ι) : ℂ := f (r x)

/-- The reflection-odd projector `(I-R)/2`. -/
def oddProjection (r : ι → ι) (f : ι → ℂ) (x : ι) : ℂ :=
  (f x - f (r x)) / 2

/-- The convention `[P_-,M_H]=P_-M_H-M_HP_-`. -/
def reflectionMultiplierCommutator
    (r : ι → ι) (H f : ι → ℂ) (x : ι) : ℂ :=
  oddProjection r (multiplierOp H f) x -
    multiplierOp H (oddProjection r f) x

/-- Exact normal form for one reflection/multiplier commutator. -/
theorem reflectionMultiplierCommutator_eq
    (r : ι → ι) (H f : ι → ℂ) (x : ι) :
    reflectionMultiplierCommutator r H f x =
      (H x - H (r x)) / 2 * f (r x) := by
  simp [reflectionMultiplierCommutator, oddProjection, multiplierOp]
  ring

/-- A reflection-even multiplier has zero commutator with the odd
projection, independently of the source. -/
theorem even_multiplier_commutator_zero
    (r : ι → ι) (H f : ι → ℂ) (x : ι)
    (hH : H (r x) = H x) :
    reflectionMultiplierCommutator r H f x = 0 := by
  rw [reflectionMultiplierCommutator_eq, hH]
  ring

/-- Under an involution, two reflection/multiplier commutators return to
ordinary scalar multiplication of the original source. -/
theorem two_reflection_commutators_collapse
    (r : ι → ι) (hr : Function.Involutive r)
    (G H f : ι → ℂ) (x : ι) :
    reflectionMultiplierCommutator r G
        (reflectionMultiplierCommutator r H f) x =
      -((G x - G (r x)) * (H x - H (r x))) / 4 * f x := by
  rw [reflectionMultiplierCommutator_eq, reflectionMultiplierCommutator_eq]
  rw [hr x]
  ring

/-- Normal form for the crossed-product operators generated by
multiplication and one involutive reflection. -/
def crossedOp (r : ι → ι) (a b f : ι → ℂ) (x : ι) : ℂ :=
  a x * f x + b x * f (r x)

/-- Composition stays in the two-channel normal form `M_a + M_b R`.
Consequently finite iteration of window/reflection algebra cannot create an
additional independent source channel. -/
theorem crossedOp_comp_normal_form
    (r : ι → ι) (hr : Function.Involutive r)
    (a b c d f : ι → ℂ) (x : ι) :
    crossedOp r a b (crossedOp r c d f) x =
      crossedOp r
        (fun y => a y * c y + b y * d (r y))
        (fun y => a y * d y + b y * c (r y)) f x := by
  simp [crossedOp, hr x]
  ring

end Reflection

section MultiplierFactor

/-- Elementary factorization underlying
`q_h(z)-q_h(-z)=4 sinh(hz)(cosh(hz)-exp(h/2))`.  The analytic substitution
and its off-critical nonvanishing are outside this finite-algebra file. -/
theorem difference_of_shifted_squares
    (x y c : ℂ) :
    (x - c) ^ 2 - (y - c) ^ 2 = (x - y) * (x + y - 2 * c) := by
  ring

end MultiplierFactor

end

end RHBridge.S1B1CompletedSourceCommutator
