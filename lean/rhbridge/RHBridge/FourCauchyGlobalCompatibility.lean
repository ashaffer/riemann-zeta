/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Finite algebra for the four-Cauchy exterior-source audit

This file kernel-checks only the exact algebra used in R185:

* scalar pullbacks (root rotations and positive dilations) commute globally;
* localization creates a projection/commutator boundary cocycle, which is
  only one source channel and not the total KNC charge;
* a formal inverse compressed through a projection leaves the omitted exterior tail;
* one pole mode cancels one Lerch mode on each exterior side; and
* the even branch of the first singular Toeplitz extension requires a new
  Chebyshev recurrence, while the odd branch requires reflected-lag equality.

It does not formalize Suzuki's analytic operator, the split finite-part old
Lerch equation, Cauchy boundary values, the affine reflection law, boundary
jets, von Mangoldt sums, the form-domain state adapter, kernel-null charge, a
completed global compatibility calculation, a completed-source factor, a
zero-free strip, or RH.  In particular, none of the theorems below uses the
old homogeneous equation or proves exterior vanishing on its kernel.
-/

namespace RHBridge.FourCauchyGlobalCompatibility

/-- Pullback of a scalar function by multiplication of its argument.  Root
rotations and positive dilations are both instances of this operation. -/
def scalarPullback (scale : ℂ) (F : ℂ → ℂ) : ℂ → ℂ :=
  fun z => F (scale * z)

/-- Scalar root rotations and dilations commute before interval compression. -/
theorem scalarPullback_commutes (first second : ℂ) (F : ℂ → ℂ) :
    scalarPullback first (scalarPullback second F) =
      scalarPullback second (scalarPullback first F) := by
  funext z
  simp only [scalarPullback]
  congr 1
  ring

/-- Multiplicative reflection.  The value at zero uses the standard
group-with-zero convention and is irrelevant to the exterior-ray audit. -/
noncomputable def multiplicativeReflection (F : ℂ → ℂ) : ℂ → ℂ :=
  fun z => F z⁻¹

/-- Reflection normalizes scalar pullbacks by swapping a scale with its
inverse; it is a semidirect relation, not commutation of individual scales. -/
theorem reflection_conjugates_scalarPullback (scale : ℂ) (F : ℂ → ℂ) :
    multiplicativeReflection (scalarPullback scale F) =
      scalarPullback scale⁻¹ (multiplicativeReflection F) := by
  funext z
  simp [multiplicativeReflection, scalarPullback, mul_inv_rev, mul_comm]

/-- The inverse-paired pullback used by the bilateral prime source is
reflection invariant even though either directed pullback is merely swapped. -/
theorem reflection_commutes_with_paired_pullback (scale : ℂ) (F : ℂ → ℂ) :
    multiplicativeReflection
        (fun z => scalarPullback scale F z + scalarPullback scale⁻¹ F z) =
      (fun z =>
        scalarPullback scale (multiplicativeReflection F) z +
          scalarPullback scale⁻¹ (multiplicativeReflection F) z) := by
  funext z
  simp [multiplicativeReflection, scalarPullback, mul_inv_rev, mul_comm, add_comm]

section NoncommutativeRing

variable {R : Type*} [Ring R]

/-- The commutator convention used by the boundary-cocycle audit. -/
def commutator (x y : R) : R := x * y - y * x

/-- Exact Leibniz/cocycle identity for a product commutator. -/
theorem commutator_product (first second projection : R) :
    commutator (first * second) projection =
      first * commutator second projection +
        commutator first projection * second := by
  simp only [commutator]
  noncomm_ring

/-- If `projection` is idempotent, all old-to-exterior leakage is the
compressed defect `Q (D P - P D P)`; there is no bulk leakage term. -/
theorem projection_leakage_is_commutator
    (projection dilation : R) (hprojection : projection * projection = projection) :
    (1 - projection) * dilation * projection =
      (1 - projection) *
        (dilation * projection - projection * dilation * projection) := by
  symm
  calc
    (1 - projection) *
          (dilation * projection - projection * dilation * projection) =
        (1 - projection) * dilation * projection -
          (projection - projection * projection) * dilation * projection := by
            noncomm_ring
    _ = (1 - projection) * dilation * projection := by rw [hprojection]; simp

/-- Compressing an exact global inverse through `projection` produces the
negative omitted exterior tail. -/
theorem compressed_inverse_equals_omitted_tail
    (projection exterior inverse source : R)
    (hsplit : projection + exterior = 1)
    (horthogonal : exterior * projection = 0)
    (hinverse : inverse * source = 1) :
    exterior * inverse * projection * source * projection =
      -(exterior * inverse * exterior * source * projection) := by
  have hzero :
      exterior * inverse * projection * source * projection +
          exterior * inverse * exterior * source * projection = 0 := by
    calc
      exterior * inverse * projection * source * projection +
            exterior * inverse * exterior * source * projection =
          exterior * inverse * (projection + exterior) * source * projection := by
            noncomm_ring
      _ = exterior * inverse * 1 * source * projection := by rw [hsplit]
      _ = exterior * (inverse * source) * projection := by noncomm_ring
      _ = exterior * 1 * projection := by rw [hinverse]
      _ = exterior * projection := by simp
      _ = 0 := horthogonal
  calc
    exterior * inverse * projection * source * projection =
        (exterior * inverse * projection * source * projection +
          exterior * inverse * exterior * source * projection) -
            exterior * inverse * exterior * source * projection := by
              noncomm_ring
    _ = -(exterior * inverse * exterior * source * projection) := by rw [hzero]; simp

end NoncommutativeRing

/-- The right reciprocal pole mode and the leading right Lerch mode cancel. -/
theorem right_pole_lerch_leading_cancel
    (coordinate moment : ℝ) (_hcoordinate : 0 < coordinate) :
    moment / coordinate - moment / coordinate = 0 := by
  ring

/-- The reflected left pole/Lerch pair has the same exact cancellation. -/
theorem left_pole_lerch_leading_cancel
    (coordinate moment : ℝ) (_hcoordinate : 0 < coordinate) :
    coordinate * moment + (-coordinate * moment) = 0 := by
  ring

/-- Determinant factorization for the first three-by-three symmetric Toeplitz
contact block with lags `1,a,c`. -/
theorem toeplitz_three_det_factor (a c : ℝ) :
    1 - 2 * a ^ 2 + 2 * a ^ 2 * c - c ^ 2 =
      (c - 1) * (2 * a ^ 2 - c - 1) := by
  ring

/-- On the even contact component, `(1,-2a,1)` kills every old row. -/
theorem even_contact_old_rows_zero
    (a c : ℝ) (hcontact : c = 2 * a ^ 2 - 1) :
    1 - 2 * a * a + c = 0 ∧
      a - 2 * a + a = 0 ∧
      c - 2 * a * a + 1 = 0 := by
  constructor
  · rw [hcontact]
    ring
  constructor <;> ring_nf
  rw [hcontact]
  ring

/-- The next exterior lag kills the even contact vector exactly when it obeys
the cubic Chebyshev recurrence. -/
theorem even_contact_exterior_zero_iff
    (a c d : ℝ) (hcontact : c = 2 * a ^ 2 - 1) :
    d + a - 2 * a * c = 0 ↔ d = 4 * a ^ 3 - 3 * a := by
  rw [hcontact]
  constructor <;> intro h <;> nlinarith

/-- On the odd contact component `c=1`, the exterior compatibility condition
is the reflected-lag identity `d=a`. -/
theorem odd_contact_exterior_zero_iff (a c d : ℝ) (_hcontact : c = 1) :
    a - d = 0 ↔ d = a := by
  constructor <;> intro h <;> linarith

/-- Coordinate form of the inverse-free two-row boundary stencil. -/
theorem even_boundary_stencil_residual
    (a c d : ℝ) :
    (c - (2 * a ^ 2 - 1) = c + 1 - 2 * a ^ 2) ∧
      (d - (2 * a * c - a) = d + a - 2 * a * c) := by
  constructor <;> ring

/-- The rational charged-contact old block is positive semidefinite by an
explicit sum of squares. -/
theorem charged_contact_old_block_sos (x y z : ℝ) :
    x ^ 2 + y ^ 2 + z ^ 2 + x * y - x * z + y * z =
      ((x + y) ^ 2 + (y + z) ^ 2 + (x - z) ^ 2) / 2 := by
  ring

/-- Its displayed nullvector really is old-null. -/
theorem rational_charged_contact_old_null :
    (1 : ℚ) + (1 / 2 : ℚ) * (-1) + (-1 / 2 : ℚ) = 0 ∧
      (1 / 2 : ℚ) + (-1) + (1 / 2 : ℚ) = 0 ∧
      (-1 / 2 : ℚ) + (1 / 2 : ℚ) * (-1) + 1 = 0 := by
  norm_num

/-- The same rational nullvector has a nonzero exterior charge in the
Toeplitz-algebra countermodel. -/
theorem rational_charged_contact_exterior_charge :
    (1 / 2 : ℚ) + 1 / 2 - 262079 / 32760 = -229319 / 32760 ∧
      (-262079 / 32760 : ℚ) + 1 / 2 + 1 / 2 = -229319 / 32760 := by
  norm_num

/-- The Chebyshev step is exactly the vanishing of the next propagation
residual. -/
theorem chebyshev_step_residual
    (first previous current next : ℝ)
    (hnext : next = 2 * first * current - previous) :
    next - 2 * first * current + previous = 0 := by
  rw [hnext]
  ring

end RHBridge.FourCauchyGlobalCompatibility
