/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRounded

/-!
# Integral semantics for rounded canonical `p = 2` polynomials

This file connects the executable uniform-error semantics of
`RoundedRatPoly.Approx` to exact rational polynomial integrals.  In
particular, an enclosure on the normalized interval `[-1,1]` gives an
integral radius of exactly twice its uniform error.  Scaling by a
nonnegative rational panel half-width then gives the original-coordinate
panel radius used by the canonical certificate checker.
-/

namespace RHP2Bridge

namespace P2RoundedCanonical

open scoped BigOperators

/-- Multiplying a normalized integral enclosure by a nonnegative rational
panel half-width multiplies its radius by the same amount.  Both the center
and radius remain executable rational expressions. -/
theorem abs_scaledExactIntegral_sub_approxCenter_le
    {exact : DenseRatPoly.Poly} {approx : RoundedRatPoly.Approx}
    (hencl : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal exact) approx)
    (halfWidth : ℚ) (hhalfWidth : 0 ≤ halfWidth) :
    |halfWidth * DenseRatPoly.exactIntegral exact (-1) 1 -
        halfWidth * DenseRatPoly.exactIntegral approx.coeffs (-1) 1| ≤
      2 * halfWidth * approx.error := by
  have hint := abs_dense_exactIntegral_sub_approx_le exact approx hencl
  rw [← mul_sub, abs_mul, abs_of_nonneg hhalfWidth]
  calc
    halfWidth *
        |DenseRatPoly.exactIntegral exact (-1) 1 -
          DenseRatPoly.exactIntegral approx.coeffs (-1) 1| ≤
        halfWidth * (2 * approx.error) :=
      mul_le_mul_of_nonneg_left hint hhalfWidth
    _ = 2 * halfWidth * approx.error := by ring

/-- Original-coordinate form of
`abs_scaledExactIntegral_sub_approxCenter_le`.  If `approx` encloses the
normalized polynomial `p(h*t)` on `[-1,1]`, then its rational center and
radius enclose the exact integral of `p` on `[-h,h]`. -/
theorem abs_centeredExactIntegral_sub_approxCenter_le
    {exact : DenseRatPoly.Poly} {approx : RoundedRatPoly.Approx}
    (halfWidth : ℚ) (hhalfWidth : 0 ≤ halfWidth)
    (hencl : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine exact 0 halfWidth)) approx) :
    |DenseRatPoly.exactIntegral exact (-halfWidth) halfWidth -
        halfWidth * DenseRatPoly.exactIntegral approx.coeffs (-1) 1| ≤
      2 * halfWidth * approx.error := by
  rw [dense_exactIntegral_centered_eq_scale_normalized]
  exact abs_scaledExactIntegral_sub_approxCenter_le
    hencl halfWidth hhalfWidth

/-- Sum a finite family of independently rounded normalized panel
integrals.  The aggregate radius is the sum of the executable panel
radii; no common per-panel bound is required. -/
theorem abs_sum_scaledExactIntegral_sub_approxCenters_le
    {ι : Type*} (s : Finset ι)
    (exact : ι → DenseRatPoly.Poly)
    (approx : ι → RoundedRatPoly.Approx)
    (halfWidth : ι → ℚ)
    (hhalfWidth : ∀ k ∈ s, 0 ≤ halfWidth k)
    (hencl : ∀ k ∈ s, RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exact k)) (approx k)) :
    |(∑ k ∈ s, halfWidth k *
          DenseRatPoly.exactIntegral (exact k) (-1) 1) -
        ∑ k ∈ s, halfWidth k *
          DenseRatPoly.exactIntegral (approx k).coeffs (-1) 1| ≤
      ∑ k ∈ s, 2 * halfWidth k * (approx k).error := by
  rw [← Finset.sum_sub_distrib]
  calc
    |∑ k ∈ s,
        (halfWidth k * DenseRatPoly.exactIntegral (exact k) (-1) 1 -
          halfWidth k *
            DenseRatPoly.exactIntegral (approx k).coeffs (-1) 1)| ≤
        ∑ k ∈ s,
          |halfWidth k * DenseRatPoly.exactIntegral (exact k) (-1) 1 -
            halfWidth k *
              DenseRatPoly.exactIntegral (approx k).coeffs (-1) 1| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ s, 2 * halfWidth k * (approx k).error := by
      exact Finset.sum_le_sum fun k hk =>
        abs_scaledExactIntegral_sub_approxCenter_le
          (hencl k hk) (halfWidth k) (hhalfWidth k hk)

/-- Finite-family original-coordinate form.  Each exact polynomial is
integrated on its own centered panel `[-halfWidth k, halfWidth k]`, while
the rounded approximation is integrated on the common normalized domain
`[-1,1]`. -/
theorem abs_sum_centeredExactIntegral_sub_approxCenters_le
    {ι : Type*} (s : Finset ι)
    (exact : ι → DenseRatPoly.Poly)
    (approx : ι → RoundedRatPoly.Approx)
    (halfWidth : ι → ℚ)
    (hhalfWidth : ∀ k ∈ s, 0 ≤ halfWidth k)
    (hencl : ∀ k ∈ s, RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine (exact k) 0 (halfWidth k)))
      (approx k)) :
    |(∑ k ∈ s, DenseRatPoly.exactIntegral (exact k)
          (-(halfWidth k)) (halfWidth k)) -
        ∑ k ∈ s, halfWidth k *
          DenseRatPoly.exactIntegral (approx k).coeffs (-1) 1| ≤
      ∑ k ∈ s, 2 * halfWidth k * (approx k).error := by
  have hnormalized :=
    abs_sum_scaledExactIntegral_sub_approxCenters_le s
      (fun k => DenseRatPoly.affine (exact k) 0 (halfWidth k))
      approx halfWidth hhalfWidth hencl
  have hexact :
      (∑ k ∈ s, DenseRatPoly.exactIntegral (exact k)
          (-(halfWidth k)) (halfWidth k)) =
        ∑ k ∈ s, halfWidth k *
          DenseRatPoly.exactIntegral
            (DenseRatPoly.affine (exact k) 0 (halfWidth k)) (-1) 1 := by
    apply Finset.sum_congr rfl
    intro k hk
    exact dense_exactIntegral_centered_eq_scale_normalized
      (exact k) (halfWidth k)
  rw [hexact]
  exact hnormalized

/-- Full finite-index wrapper, convenient for the fixed 32-panel canonical
certificate. -/
theorem abs_fin_sum_centeredExactIntegral_sub_approxCenters_le
    {N : ℕ}
    (exact : Fin N → DenseRatPoly.Poly)
    (approx : Fin N → RoundedRatPoly.Approx)
    (halfWidth : Fin N → ℚ)
    (hhalfWidth : ∀ k, 0 ≤ halfWidth k)
    (hencl : ∀ k, RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine (exact k) 0 (halfWidth k)))
      (approx k)) :
    |(∑ k, DenseRatPoly.exactIntegral (exact k)
          (-(halfWidth k)) (halfWidth k)) -
        ∑ k, halfWidth k *
          DenseRatPoly.exactIntegral (approx k).coeffs (-1) 1| ≤
      ∑ k, 2 * halfWidth k * (approx k).error := by
  exact abs_sum_centeredExactIntegral_sub_approxCenters_le Finset.univ
    exact approx halfWidth (fun k _ => hhalfWidth k)
    (fun k _ => hencl k)

end P2RoundedCanonical

end RHP2Bridge
