/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.NoncommRing

/-!
# Finite cyclic trace obstruction for semilocal Hankel models

The continuum Weil trace obtained from a quantized differential is an
infinite-dimensional trace anomaly.  This file records the elementary reason
that an exactly unitary finite collocation cannot reproduce it: cyclicity of
the ordinary finite trace makes the pairing vanish whenever the test
multiplier commutes with the unitary multiplier.
-/

namespace RHBridge.SemilocalHankelTraceNoGo

/-- The difference between a projection and its conjugate.  In the intended
application `V` is the inverse (adjoint) of `U`. -/
def projectionDefect {n R : Type*} [Fintype n] [CommRing R]
    (P U V : Matrix n n R) : Matrix n n R :=
  P - V * P * U

/-- Failure of the test multiplier `F` to commute with the model multiplier
`U`, with the orientation used by the anomaly-budget identity. -/
def commutationDefect {n R : Type*} [Fintype n] [CommRing R]
    (F U : Matrix n n R) : Matrix n n R :=
  F * U - U * F

/-- Failure of `V` to be a right inverse of `U`.  In a unitary model one has
`V = Uᴴ`, so this is the unitarity defect `I - U Uᴴ`. -/
def rightInverseDefect {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (U V : Matrix n n R) : Matrix n n R :=
  1 - U * V

/-- Exact finite anomaly budget.  A finite section can retain the continuum
trace anomaly only through failure of multiplier commutation, failure of
right-invertibility/unitarity, or both:

`tr(F(P - V P U))`

`= tr((F U - U F)V P) + tr(F(I - U V)P)`.

No projection, adjoint, or invertibility hypothesis is needed. -/
theorem trace_mul_projectionDefect_eq_anomalyBudget
    {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (F P U V : Matrix n n R) :
    Matrix.trace (F * projectionDefect P U V) =
      Matrix.trace (commutationDefect F U * V * P) +
        Matrix.trace (F * rightInverseDefect U V * P) := by
  have hrotate :
      Matrix.trace (F * (V * P * U)) =
        Matrix.trace ((U * F * V) * P) := by
    calc
      Matrix.trace (F * (V * P * U)) =
          Matrix.trace ((F * V * P) * U) := by
        congr 1
        simp only [Matrix.mul_assoc]
      _ = Matrix.trace (U * (F * V * P)) :=
        Matrix.trace_mul_comm (F * V * P) U
      _ = Matrix.trace ((U * F * V) * P) := by
        congr 1
        simp only [Matrix.mul_assoc]
  have hbudget :
      F - U * F * V =
        commutationDefect F U * V + F * rightInverseDefect U V := by
    simp only [commutationDefect, rightInverseDefect]
    noncomm_ring
  calc
    Matrix.trace (F * projectionDefect P U V) =
        Matrix.trace (F * P) - Matrix.trace (F * (V * P * U)) := by
      simp only [projectionDefect, mul_sub, Matrix.trace_sub]
    _ = Matrix.trace (F * P) - Matrix.trace ((U * F * V) * P) := by
      rw [hrotate]
    _ = Matrix.trace ((F - U * F * V) * P) := by
      simp only [sub_mul, Matrix.trace_sub]
    _ = Matrix.trace
          ((commutationDefect F U * V + F * rightInverseDefect U V) * P) := by
      rw [hbudget]
    _ = Matrix.trace (commutationDefect F U * V * P) +
          Matrix.trace (F * rightInverseDefect U V * P) := by
      simp only [add_mul, Matrix.trace_add]

/-- A regulator `W` introduces one further, and completely explicit, anomaly
channel.  Besides the original commutation and right-inverse defects, the
regulated trace can survive through failure of `W` to commute with `U`:

`tr(W F (P - V P U))`

`= tr(W(FU-UF)VP) + tr((WU-UW)FVP) + tr(WF(I-UV)P)`.

This is the product-rule form of the finite anomaly budget. -/
theorem trace_mul_weighted_projectionDefect_eq_anomalyBudget
    {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (W F P U V : Matrix n n R) :
    Matrix.trace (W * F * projectionDefect P U V) =
      Matrix.trace (W * commutationDefect F U * V * P) +
        Matrix.trace (commutationDefect W U * F * V * P) +
          Matrix.trace (W * F * rightInverseDefect U V * P) := by
  have hproduct :
      commutationDefect (W * F) U =
        W * commutationDefect F U + commutationDefect W U * F := by
    simp only [commutationDefect]
    noncomm_ring
  rw [trace_mul_projectionDefect_eq_anomalyBudget (W * F) P U V, hproduct]
  simp only [add_mul, Matrix.trace_add, Matrix.mul_assoc]

/-- If the physical multiplier commutes with `U` and `V` is a right inverse,
the regulated trace anomaly is exactly the regulator commutator. -/
theorem trace_mul_weighted_projectionDefect_eq_regulatorCommutator
    {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (W F P U V : Matrix n n R)
    (hFU : F * U = U * F) (hUV : U * V = 1) :
    Matrix.trace (W * F * projectionDefect P U V) =
      Matrix.trace (commutationDefect W U * F * V * P) := by
  rw [trace_mul_weighted_projectionDefect_eq_anomalyBudget W F P U V]
  simp [commutationDefect, hFU, rightInverseDefect, hUV]

/-- A finite cyclic trace cannot see the quantized-differential anomaly.
No idempotence assumption on `P` is needed. -/
theorem trace_mul_projectionDefect_eq_zero
    {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (F P U V : Matrix n n R)
    (hFU : F * U = U * F) (hUV : U * V = 1) :
    Matrix.trace (F * projectionDefect P U V) = 0 := by
  have hcycle :
      Matrix.trace (F * (V * P * U)) = Matrix.trace (F * P) := by
    calc
      Matrix.trace (F * (V * P * U)) =
          Matrix.trace ((F * V * P) * U) := by
            congr 1
            simp only [Matrix.mul_assoc]
      _ = Matrix.trace (U * (F * V * P)) :=
        Matrix.trace_mul_comm (F * V * P) U
      _ = Matrix.trace (F * P) := by
        congr 1
        calc
          U * (F * V * P) = (U * F) * V * P := by
            simp only [Matrix.mul_assoc]
          _ = (F * U) * V * P := by rw [← hFU]
          _ = F * (U * V) * P := by simp only [Matrix.mul_assoc]
          _ = F * P := by rw [hUV]; simp
  simp only [projectionDefect, mul_sub, Matrix.trace_sub, hcycle, sub_self]

end RHBridge.SemilocalHankelTraceNoGo
