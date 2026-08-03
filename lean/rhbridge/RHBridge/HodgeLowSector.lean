/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.HodgeHighSector

/-!
# Exact Hodge trace identity and the residual two-mode gate

On an old Weil eigenmode, write `s = degree + lambda` for its incidence
eigenvalue, `d = q^2` for the newly activated prime-power degree, and

* `a` for the old-place collar cross trace;
* `e` for the new-event collar cross trace;
* `r = a + e` for the combined Weil cross trace.

The first theorem rewrites the Hodge-return row using the combined trace.  It
is a purely algebraic identity, not a positivity statement.

After the high old modes and the Hodge trace have been paid for, reflection
leaves two low modes in the numerically hardest odd block.  The second theorem
records the exact principal-minor criterion for that two-mode contraction.
Its determinant hypothesis is the remaining arithmetic boundary estimate; it
is deliberately not assumed to follow from Hodge smoothing.
-/

namespace RHP2Bridge.HodgeLowSector

noncomputable section

/-- Eigenmode form of the Hodge-return trace.

The left side is

`tau (1-tau) (q^-1 e - q s^-1 a)`.

Using `q^2=d`, `tau^2(s+d)=s`, and `r=a+e`, the right side separates the
new-event trace from a smoothed copy of the combined Weil boundary trace.
No sign or positivity assumption occurs in the statement. -/
theorem scalar_eigenmode_hodge_trace_identity
    {s d q tau a e r : ℝ}
    (hs : s ≠ 0) (hsd : s + d ≠ 0) (hq : q ≠ 0) (htau : tau ≠ 0)
    (hq2 : q ^ 2 = d) (htau2 : tau ^ 2 * (s + d) = s)
    (hr : r = a + e) :
    tau * (1 - tau) * (e / q - q * a / s) =
      (1 - tau) / (q * tau) * (e - d / (s + d) * r) := by
  subst r
  field_simp [hs, hsd, hq, htau]
  rw [hq2]
  have hbracket : e * (s + d) - d * (a + e) = e * s - d * a := by
    ring
  rw [hbracket]
  calc
    tau ^ 2 * (1 - tau) * (e * s - d * a) * (s + d) =
        (1 - tau) * (e * s - d * a) * (tau ^ 2 * (s + d)) := by ring
    _ = (1 - tau) * (e * s - d * a) * s := by rw [htau2]
    _ = (1 - tau) * s * (e * s - d * a) := by ring

/-- A real symmetric two-mode form is nonnegative exactly when its determinant
is nonnegative, once its first diagonal principal minor is strictly positive.

The form is written with off-diagonal entry `-b`, matching the difference
between a diagonal old-energy matrix and a boundary-trace Gram matrix. -/
theorem two_mode_psd_iff_determinant
    {a b c : ℝ} (ha : 0 < a) :
    (∀ x y : ℝ, 0 ≤ a * x ^ 2 - 2 * b * x * y + c * y ^ 2) ↔
      0 ≤ a * c - b ^ 2 := by
  constructor
  · intro h
    have hvalue := h (b / a) 1
    have hmul :
        0 ≤ a * (a * (b / a) ^ 2 - 2 * b * (b / a) * 1 + c * 1 ^ 2) :=
      mul_nonneg ha.le hvalue
    have hid :
        a * (a * (b / a) ^ 2 - 2 * b * (b / a) * 1 + c * 1 ^ 2) =
          a * c - b ^ 2 := by
      field_simp [ne_of_gt ha]
      <;> ring
    rwa [hid] at hmul
  · intro hdet x y
    have hid :
        a * (a * x ^ 2 - 2 * b * x * y + c * y ^ 2) =
          (a * x - b * y) ^ 2 + (a * c - b ^ 2) * y ^ 2 := by
      ring
    have hright :
        0 ≤ (a * x - b * y) ^ 2 + (a * c - b ^ 2) * y ^ 2 :=
      add_nonneg (sq_nonneg _) (mul_nonneg hdet (sq_nonneg y))
    have hmul :
        0 ≤ a * (a * x ^ 2 - 2 * b * x * y + c * y ^ 2) := by
      rwa [hid]
    by_contra hneg
    have hformneg : a * x ^ 2 - 2 * b * x * y + c * y ^ 2 < 0 :=
      lt_of_not_ge hneg
    exact (not_lt_of_ge hmul) (mul_neg_of_pos_of_neg ha hformneg)

/-- Exact two-mode contraction certificate after all independently controlled
high-sector and Hodge costs have been removed from the collar form.

Here `lambda1, lambda2` are the two old Weil eigenvalues and `hij` are the
entries of the dual Gram matrix of their *combined arithmetic boundary
traces* in the remaining collar metric.  Thus the determinant on the right is
the genuine residual theorem, rather than a renamed Hodge inequality. -/
theorem two_mode_contraction_iff_principal_minor
    {lambda1 lambda2 h11 h12 h22 : ℝ}
    (hfirst : 0 < lambda1 - h11) :
    (∀ x y : ℝ,
      h11 * x ^ 2 + 2 * h12 * x * y + h22 * y ^ 2 ≤
        lambda1 * x ^ 2 + lambda2 * y ^ 2) ↔
      0 ≤ (lambda1 - h11) * (lambda2 - h22) - h12 ^ 2 := by
  rw [← two_mode_psd_iff_determinant hfirst]
  constructor <;> intro h x y
  · have hxy := h x y
    linarith
  · have hxy := h x y
    linarith

end

end RHP2Bridge.HodgeLowSector
