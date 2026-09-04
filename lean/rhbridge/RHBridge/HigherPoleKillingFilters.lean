/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ShiftedPsiRampBridge

/-!
# Exact low-order certificates for higher pole-killing filters

The companion report proves the general Lagrange-interpolation formula.  This
file kernel-checks the first two nontrivial higher-order rational identities,
their moment constraints, and their unstable inverse principal parts.
-/

namespace RHP2Bridge.HigherPoleKillingFilters

/-- Endpoint normalization for the rates `0,1,2` order-two filter. -/
theorem orderTwo_endpoint :
    (1 / 2 : ℝ) - 4 + 9 / 2 = 1 := by norm_num

/-- Its first pole moment vanishes. -/
theorem orderTwo_moment_zero :
    (1 / 2 : ℝ) - 4 / 2 + (9 / 2) / 3 = 0 := by norm_num

/-- Its second pole moment vanishes, giving a double multiplier zero. -/
theorem orderTwo_first_derivative_zero :
    (1 / 2 : ℝ) - 4 / 2 ^ 2 + (9 / 2) / 3 ^ 2 = 0 := by norm_num

/-- Exact Laplace multiplier for the minimal order-two filter. -/
theorem orderTwo_laplace_identity (s : ℝ)
    (h0 : s ≠ 0) (h1 : s + 1 ≠ 0) (h2 : s + 2 ≠ 0) :
    (1 / 2 : ℝ) / s - 4 / (s + 1) + (9 / 2) / (s + 2) =
      (s - 1) ^ 2 / (s * (s + 1) * (s + 2)) := by
  field_simp [h0, h1, h2]
  ring

/-- The order-two kernel polynomial has the sign pattern `+,-,+` on
`y=0,1/2,1`, certifying the two expected fronts after continuity. -/
theorem orderTwo_polynomial_sign_samples :
    (0 : ℝ) < 1 / 2 ∧
      (1 / 2 : ℝ) - 4 * (1 / 2) + (9 / 2) * (1 / 2) ^ 2 < 0 ∧
      (1 / 2 : ℝ) - 4 + 9 / 2 > 0 := by
  norm_num

/-- Endpoint normalization for the rates `0,1,2,3` order-three filter. -/
theorem orderThree_endpoint :
    (-1 / 6 : ℝ) + 4 - 27 / 2 + 32 / 3 = 1 := by norm_num

/-- The three denominator moments vanish. -/
theorem orderThree_moments :
    ((-1 / 6 : ℝ) + 4 / 2 - (27 / 2) / 3 + (32 / 3) / 4 = 0) ∧
      ((-1 / 6 : ℝ) + 4 / 2 ^ 2 - (27 / 2) / 3 ^ 2 +
          (32 / 3) / 4 ^ 2 = 0) ∧
      ((-1 / 6 : ℝ) + 4 / 2 ^ 3 - (27 / 2) / 3 ^ 3 +
          (32 / 3) / 4 ^ 3 = 0) := by
  norm_num

/-- Exact Laplace multiplier for the minimal order-three filter. -/
theorem orderThree_laplace_identity (s : ℝ)
    (h0 : s ≠ 0) (h1 : s + 1 ≠ 0) (h2 : s + 2 ≠ 0)
    (h3 : s + 3 ≠ 0) :
    (-1 / 6 : ℝ) / s + 4 / (s + 1) - (27 / 2) / (s + 2) +
        (32 / 3) / (s + 3) =
      (s - 1) ^ 3 / (s * (s + 1) * (s + 2) * (s + 3)) := by
  field_simp [h0, h1, h2, h3]
  ring

/-- The double-zero inverse contains first-degree exponential instability;
the displayed first two terms are its complete principal part at `q=δ`. -/
theorem orderTwo_inverse_principal_part (q δ : ℝ) (h : q - δ ≠ 0) :
    q * (q + δ) * (q + 2 * δ) / (q - δ) ^ 2 =
      q + 5 * δ + 11 * δ ^ 2 / (q - δ) +
        6 * δ ^ 3 / (q - δ) ^ 2 := by
  field_simp [h]
  ring

/-- The triple-zero inverse contains second-degree exponential instability. -/
theorem orderThree_inverse_principal_part (q δ : ℝ) (h : q - δ ≠ 0) :
    q * (q + δ) * (q + 2 * δ) * (q + 3 * δ) / (q - δ) ^ 3 =
      q + 9 * δ + 35 * δ ^ 2 / (q - δ) +
        50 * δ ^ 3 / (q - δ) ^ 2 + 24 * δ ^ 4 / (q - δ) ^ 3 := by
  field_simp [h]
  ring

/-- Algebra behind the kernel-independent displacement of a simple boundary
front. -/
theorem universal_simple_front_shift (C K φ' δ : ℝ) (hC : C ≠ 0) :
    -C * φ' * (δ * (K / C)) + δ * φ' * K = 0 := by
  field_simp [hC]
  ring

/-- Algebra behind the kernel-dependent second displacement coefficient.  In
the analytic theorem `r = k''(c₀)/k'(c₀)`. -/
theorem universal_simple_front_second_shift
    (C K₀ K₁ r σ : ℝ) (hC : C ≠ 0) :
    -C * ((K₀ ^ 2 / (2 * C ^ 2) - K₁ / C) * (r - 2 * σ)) -
        C * r * (K₀ / C) ^ 2 / 2 - K₀ * (K₀ / C) * (σ - r) -
        K₁ * (r - 2 * σ) = 0 := by
  field_simp [hC]
  ring

/-- Each first-order inverse factor is a positive exponential tail added to
the identity impulse when `a,σ,δ` are nonnegative. -/
theorem inverse_positive_factor (q a σ δ : ℝ) (h : q - σ * δ ≠ 0) :
    (q + a * δ) / (q - σ * δ) =
      1 + (a + σ) * δ / (q - σ * δ) := by
  rw [show σ * δ = δ * σ by ring] at h ⊢
  field_simp [h]
  ring

/-- The confluent order-two Laguerre kernel has a double zero at an arbitrary
positive anchor `σ`.  This is a rational certificate of its Laplace transform. -/
theorem confluentOrderTwo_laplace_identity (s a σ : ℝ) (h : s + a ≠ 0) :
    1 / (s + a) - 2 * (a + σ) / (s + a) ^ 2 +
        (a + σ) ^ 2 / (s + a) ^ 3 =
      (s - σ) ^ 2 / (s + a) ^ 3 := by
  field_simp [h]
  ring

/-- The minimal rates `0,1,2`, notch-order-one, endpoint-order-one filter has
zero endpoint value and normalized first endpoint derivative. -/
theorem endpointFlatOne_endpoint_jets :
    ((-1 / 2 : ℝ) + 2 - 3 / 2 = 0) ∧
      (-(0 : ℝ) * (-1 / 2) - 1 * 2 - 2 * (-3 / 2) = 1) := by
  norm_num

/-- The same endpoint-flat filter kills the pole moment at the anchor one. -/
theorem endpointFlatOne_moment_zero :
    (-1 / 2 : ℝ) + 2 / 2 - (3 / 2) / 3 = 0 := by
  norm_num

/-- Exact transfer identity for the first genuinely endpoint-flat minimal
filter.  Its relative degree is two instead of one. -/
theorem endpointFlatOne_laplace_identity (s : ℝ)
    (h0 : s ≠ 0) (h1 : s + 1 ≠ 0) (h2 : s + 2 ≠ 0) :
    (-1 / 2 : ℝ) / s + 2 / (s + 1) - (3 / 2) / (s + 2) =
      (s - 1) / (s * (s + 1) * (s + 2)) := by
  field_simp [h0, h1, h2]
  ring

/-- Rational certificate for the associated-Laguerre `(m,r)=(1,1)`
confluent normal form
`v exp(-a v) - (a+σ)v^2 exp(-a v)/2`. -/
theorem associatedLaguerreOneOne_laplace_identity
    (s a σ : ℝ) (h : s + a ≠ 0) :
    1 / (s + a) ^ 2 - (a + σ) / (s + a) ^ 3 =
      (s - σ) / (s + a) ^ 3 := by
  field_simp [h]
  ring

/-- Appending one endpoint-flat order is exactly convolution with the
positive smoothing factor `δ/(q+a₂δ)`. -/
theorem endpointFlat_positive_smoothing_factor
    (q δ σ a₀ a₁ a₂ : ℝ)
    (h₀ : q + a₀ * δ ≠ 0) (h₁ : q + a₁ * δ ≠ 0)
    (h₂ : q + a₂ * δ ≠ 0) :
    δ * (q - σ * δ) /
        ((q + a₀ * δ) * (q + a₁ * δ) * (q + a₂ * δ)) =
      ((q - σ * δ) / ((q + a₀ * δ) * (q + a₁ * δ))) *
        (δ / (q + a₂ * δ)) := by
  field_simp [h₀, h₁, h₂]

end RHP2Bridge.HigherPoleKillingFilters
