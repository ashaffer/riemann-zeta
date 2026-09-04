/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact guards for the R188 principal-band serialization audit

Set `X = M^100`.  The core R187 additive band has radius `M^-99`.
This file checks the elementary exponent, denominator/quotient, determinant,
affine-center, and complete-square algebra used in the hostile R188 audit.

In particular, high denominator does not mean low determinant: unit rational
modes at denominators `X` and `2X-1` both lie in the core, while their reduced
determinant is `X-1`.  The same band also contains determinant one and a
reducible `(1,2)` denominator pair.

This file does **not** formalize Fourier or Poisson summation, the primitive
mask Fourier-algebra bound, Mellin separation, the prime number theorem, the
top-semiprime lower block, Wright's theorem, R87, any completed R71 estimate,
a zero-free strip, the four-cycle bound, or RH.
-/

namespace RHBridge.R188PrincipalBandSerialization

/-- The frozen R187/R188 strip parameter. -/
def eta : ℚ := 1 / 100

/-- The completed-energy target is `X^(49/50)`. -/
theorem targetExponent : (1 : ℚ) - 2 * eta = 49 / 50 := by
  norm_num [eta]

/-- The direct natural energy exponent is strictly larger than the target. -/
theorem target_lt_natural : (49 : ℚ) / 50 < 1 := by
  norm_num

/-- R105's recorded scalar Wright output on the surviving top `k ~ X^2`
box is worse than the direct energy exponent by `7/8`.  This is only exponent
bookkeeping; no analytic theorem is imported here. -/
theorem scalarWrightTop_excess : (15 : ℚ) / 8 - 1 = 7 / 8 := by
  norm_num

/-- The field-level exponent whose square is the completed-energy target. -/
def targetFieldExponent : ℚ := 1 / 2 - eta

/-- Fifth-order Fourier decay permits cofactors below this exponent to be
discarded at the target field scale. -/
def targetCofactorExponent : ℚ := 1 - eta / 5

/-- Fifth-order Fourier decay permits numerators above this exponent to be
discarded at the target field scale. -/
def targetNumeratorExponent : ℚ := eta / 4

/-- Exact low-cofactor exponent ledger:
`X^(1/2) (X^(499/500)/X)^5 = X^(49/100)`. -/
theorem targetMatched_lowCofactorExponent :
    (1 : ℚ) / 2 + 5 * (targetCofactorExponent - 1) =
      targetFieldExponent := by
  norm_num [targetCofactorExponent, targetFieldExponent, eta]

/-- Exact large-numerator exponent ledger:
`X^(1/2) (X^(1/400))^-4 = X^(49/100)`. -/
theorem targetMatched_largeNumeratorExponent :
    (1 : ℚ) / 2 - 4 * targetNumeratorExponent =
      targetFieldExponent := by
  norm_num [targetNumeratorExponent, targetFieldExponent, eta]

/-- The target-matched cofactor collar leaves physical quotient exponent
`1/500`. -/
theorem targetMatched_quotientExponent :
    (1 : ℚ) - targetCofactorExponent = 1 / 500 := by
  norm_num [targetCofactorExponent, eta]

/-- The retained numerator exponent is `1/400`. -/
theorem targetMatched_numeratorExponent :
    targetNumeratorExponent = 1 / 400 := by
  norm_num [targetNumeratorExponent, eta]

/-- Integer-power realization of `X`. -/
def scale (M : ℕ) : ℕ := M ^ 100

/-- Integer-power realization of the reciprocal core radius denominator. -/
def coreDenominator (M : ℕ) : ℕ := M ^ 99

/-- A unit rational mode at denominator `X=M^100` lies in the core whenever
`M` is positive. -/
theorem coreDenominator_le_scale (M : ℕ) (hM : 0 < M) :
    coreDenominator M ≤ scale M := by
  exact Nat.pow_le_pow_right hM (by omega)

/-- If a nonzero numerator obeys the core inequality
`a M^99 ≤ q`, its denominator is at least `M^99`. -/
theorem nonzeroCoreMode_forces_highDenominator
    (M a q : ℕ) (ha : 0 < a) (hcore : a * coreDenominator M ≤ q) :
    coreDenominator M ≤ q := by
  calc
    coreDenominator M = 1 * coreDenominator M := by simp
    _ ≤ a * coreDenominator M :=
      Nat.mul_le_mul_right (coreDenominator M) ha
    _ ≤ q := hcore

/-- On an active shell `q*r ≤ C*X`, a core denominator leaves only the
small physical quotient `r ≤ C*M`.  This is the exact integer form of the
`X^(1/100)` quotient ledger. -/
theorem coreMode_forces_smallPhysicalQuotient
    (M C q r : ℕ) (hM : 0 < M)
    (hq : coreDenominator M ≤ q)
    (hactive : q * r ≤ C * scale M) :
    r ≤ C * M := by
  have hfactor : coreDenominator M * r ≤ coreDenominator M * (C * M) := by
    calc
      coreDenominator M * r ≤ q * r := Nat.mul_le_mul_right r hq
      _ ≤ C * scale M := hactive
      _ = coreDenominator M * (C * M) := by
        simp only [coreDenominator, scale]
        ring
  exact Nat.le_of_mul_le_mul_left hfactor (pow_pos hM 99)

/-- Determinant one and determinant `X-1` both occur among unit modes in the
same high-denominator band.  The hypotheses are precisely the two core
denominator inequalities. -/
theorem lowAndHighDeterminant_witness
    (D X : ℕ) (hX : 0 < X) (hDX : D ≤ X) :
    D ≤ X + 1 ∧
    D ≤ 2 * X - 1 ∧
    (1 : ℤ) * ((X : ℤ) + 1) - 1 * (X : ℤ) = 1 ∧
    (1 : ℤ) * (2 * (X : ℤ) - 1) - 1 * (X : ℤ) = (X : ℤ) - 1 := by
  constructor
  · omega
  constructor
  · omega
  constructor <;> ring

/-- Pairing the surviving determinant `X-1` with a physical shift `j=X`
retains the quadratic product scale `j*theta=X^2-X`. -/
theorem highShiftDeterminant_product (X : ℤ) :
    X * (X - 1) = X ^ 2 - X := by
  ring

/-- The same high-denominator band also admits a reducible denominator pair:
`gcd(X,2X)=X`, hence the reduced pair is `(1,2)` when `X>0`. -/
theorem reduciblePair_witness (X : ℕ) (hX : 0 < X) :
    Nat.gcd X (2 * X) = X ∧ X / X = 1 ∧ (2 * X) / X = 2 := by
  constructor
  · rw [mul_comm]
    simp
  constructor
  · exact Nat.div_self hX
  · exact Nat.mul_div_left 2 hX

/-- Matching an affine center by one scalar zero mode at `r₁` leaves the
exact normalized residual `beta*(r₂-r₁)/norm` at `r₂`. -/
theorem affineScalarAxis_residual
    (alpha beta norm J₀ r₁ r₂ S : ℝ)
    (hnorm : norm ≠ 0)
    (hmatch : S * J₀ = (alpha + beta * r₁) / norm) :
    (alpha + beta * r₂) / norm - S * J₀ =
      beta * (r₂ - r₁) / norm := by
  rw [hmatch]
  field_simp [hnorm]
  ring

/-- Consequently one scalar axis cannot match two distinct samples of a
genuinely affine center. -/
theorem affineCenter_needsTwoChannels
    (alpha beta norm J₀ r₁ r₂ S : ℝ)
    (hnorm : norm ≠ 0) (hbeta : beta ≠ 0) (hr : r₁ ≠ r₂)
    (hmatch₁ : S * J₀ = (alpha + beta * r₁) / norm) :
    S * J₀ ≠ (alpha + beta * r₂) / norm := by
  intro hmatch₂
  have hres := affineScalarAxis_residual
    alpha beta norm J₀ r₁ r₂ S hnorm hmatch₁
  rw [hmatch₂] at hres
  have : beta * (r₂ - r₁) = 0 := by
    have hdiv : beta * (r₂ - r₁) / norm = 0 := by
      simpa using hres.symm
    exact (div_eq_zero_iff.mp hdiv).resolve_right hnorm
  rcases mul_eq_zero.mp this with hbeta' | hr'
  · exact hbeta hbeta'
  · exact hr (sub_eq_zero.mp hr').symm

/-- Every packet/reducible/constant-center/log-center cross term in the
completed real square.  The center is subtracted. -/
theorem completedFourChannel_square
    (packet reducible centerConstant centerLog : ℝ) :
    (packet + reducible - centerConstant - centerLog) ^ 2 =
      packet ^ 2
      + 2 * packet * reducible
      - 2 * packet * centerConstant
      - 2 * packet * centerLog
      + reducible ^ 2
      - 2 * reducible * centerConstant
      - 2 * reducible * centerLog
      + centerConstant ^ 2
      + 2 * centerConstant * centerLog
      + centerLog ^ 2 := by
  ring

/-- `n` coherent packets of amplitude `1/n` have total amplitude one; their
self ledger is `1/n`, while their cross ledger is `1-1/n`. -/
theorem coherentPacket_crossLedger (n : ℕ) (hn : 0 < n) :
    (n : ℚ) * (1 / (n : ℚ)) = 1 ∧
    (n : ℚ) * (1 / (n : ℚ)) ^ 2 = 1 / (n : ℚ) ∧
    (n : ℚ) * ((n : ℚ) - 1) * (1 / (n : ℚ)) ^ 2 =
      1 - 1 / (n : ℚ) := by
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast hn.ne'
  constructor
  · field_simp [hnq]
  constructor
  · field_simp [hnq]
  · field_simp [hnq]

/-- Exact coherent completion fixture: packet aggregate `1`, reducible
channel `1`, and two center channels summing to `2-1/n` leave square `1/n²`.
This is an algebraic cancellation guard, not an R71 counterexample. -/
theorem coherentCompleted_fixture (n : ℕ) (hn : 0 < n) :
    ((1 : ℚ) + 1 - 3 / 2 - (1 / 2 - 1 / (n : ℚ))) ^ 2 =
      (1 / (n : ℚ)) ^ 2 := by
  have hnq : (n : ℚ) ≠ 0 := by exact_mod_cast hn.ne'
  field_simp [hnq]
  ring

end RHBridge.R188PrincipalBandSerialization
