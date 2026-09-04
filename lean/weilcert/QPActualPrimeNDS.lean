import Mathlib

/-!
Exact algebra used by the actual-prime neighbourhood-degree-sum audit.
This file certifies identities and injectivity steps, not the open
asymptotic occupied-cell estimate.
-/

namespace QPActualPrimeNDS

theorem error_divisor_identity
    (a x c C d E : ℤ) :
    C * (x * d - a * c) - c * (x * E - a * C) = x * (C * d - c * E) := by
  ring

theorem equal_determinant_difference
    (b B b' B' c C : ℤ)
    (h : b * c - B * C = b' * c - B' * C) :
    c * (b - b') = C * (B - B') := by
  linarith

theorem equal_error_difference
    (r s r' s' c C : ℤ)
    (h : C * r - c * s = C * r' - c * s') :
    C * (r - r') = c * (s - s') := by
  linarith

theorem two_large_coprime_divisors_impossible
    (L x y M : ℤ)
    (hx : x ∣ L) (hy : y ∣ L) (hcop : IsCoprime x y)
    (hne : L ≠ 0) (hxy : M < |x * y|) (hL : |L| ≤ M) : False := by
  have hprod : x * y ∣ L := hcop.mul_dvd hx hy
  obtain ⟨k, hk⟩ := hprod
  rw [hk] at hne hL
  have hk0 : k ≠ 0 := by
    intro hkzero
    subst k
    simp at hne
  have hkabs : 1 ≤ |k| := Int.one_le_abs hk0
  have hscale : |x * y| ≤ |x * y| * |k| := by
    have := mul_le_mul_of_nonneg_left hkabs (abs_nonneg (x * y))
    simpa using this
  have hbound : |x * y| ≤ |x * y * k| := by
    calc
      |x * y| ≤ |x * y| * |k| := hscale
      _ = |x * y * k| := (abs_mul (x * y) k).symm
  linarith

theorem doubleStarFixture_primes :
    Nat.Prime 2934067 ∧ Nat.Prime 2934073 ∧ Nat.Prime 2934079 ∧
    Nat.Prime 2934091 ∧ Nat.Prime 2934097 ∧ Nat.Prime 2934103 ∧
    Nat.Prime 2934109 := by
  norm_num [Nat.prime_def]

theorem doubleStarFixture_windows :
    |8 * (2934073 : ℤ) * 2934091 * 2934109 - 5868182^3| ≤ 5868182 * 1912 ∧
    |8 * (2934073 : ℤ) * 2934097 * 2934103 - 5868182^3| ≤ 5868182 * 1912 ∧
    |8 * (2934079 : ℤ) * 2934091 * 2934103 - 5868182^3| ≤ 5868182 * 1912 ∧
    |8 * (2934079 : ℤ) * 2934097 * 2934097 - 5868182^3| ≤ 5868182 * 1912 ∧
    |8 * (2934067 : ℤ) * 2934097 * 2934109 - 5868182^3| ≤ 5868182 * 1912 ∧
    |8 * (2934067 : ℤ) * 2934103 * 2934103 - 5868182^3| ≤ 5868182 * 1912 := by
  norm_num [abs_of_nonpos, abs_of_nonneg]

theorem doubleStarFixture_determinants :
    (2934091 : ℤ) * 2934109 - 2934097 * 2934103 = -72 ∧
    (2934091 : ℤ) * 2934103 - 2934097 * 2934097 = -36 ∧
    (2934097 : ℤ) * 2934109 - 2934103 * 2934103 = -36 := by
  norm_num

end QPActualPrimeNDS
