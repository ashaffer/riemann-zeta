/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelComposition
import RHBridge.P2PoleApprox
import RHBridge.P2RationalPolynomial

/-!
# Rational mirrors of the canonical `p = 2` certificate polynomials

This file keeps all generated polynomial arithmetic in `ℚ[X]`.  The cast
theorems identify the rational mirrors with the real polynomials used by the
analytic panel and pole-error theorems.  Thus generated coefficient tables
can be checked over `ℚ`, with a single proved cast at the analytic boundary.
-/

namespace RHP2Bridge

namespace RatPoly

open Polynomial
open scoped BigOperators

/-! ## Rational elementary coefficients -/

/-- Real and imaginary parts of `I^n`, computed in `ℚ`. -/
def iPowComponentsQ : ℕ → ℚ × ℚ
  | 0 => (1, 0)
  | n + 1 => (-(iPowComponentsQ n).2, (iPowComponentsQ n).1)

def iPowReQ (n : ℕ) : ℚ := (iPowComponentsQ n).1

def iPowImQ (n : ℕ) : ℚ := (iPowComponentsQ n).2

theorem iPowComponentsQ_cast (n : ℕ) :
    ((iPowReQ n : ℚ) : ℝ) = (Complex.I ^ n).re ∧
      ((iPowImQ n : ℚ) : ℝ) = (Complex.I ^ n).im := by
  induction n with
  | zero => simp [iPowReQ, iPowImQ, iPowComponentsQ]
  | succ n ih =>
      rw [pow_succ]
      constructor
      · change ((-iPowImQ n : ℚ) : ℝ) =
          ((Complex.I ^ n) * Complex.I).re
        rw [Rat.cast_neg, ih.2]
        simp [Complex.mul_re]
      · change ((iPowReQ n : ℚ) : ℝ) =
          ((Complex.I ^ n) * Complex.I).im
        rw [ih.1]
        simp [Complex.mul_im]

@[simp] theorem iPowReQ_cast (n : ℕ) :
    ((iPowReQ n : ℚ) : ℝ) = (Complex.I ^ n).re :=
  (iPowComponentsQ_cast n).1

@[simp] theorem iPowImQ_cast (n : ℕ) :
    ((iPowImQ n : ℚ) : ℝ) = (Complex.I ^ n).im :=
  (iPowComponentsQ_cast n).2

def p2LogTwoCenterQ : ℚ :=
  69314718055994535 / 100000000000000000

def p2PrimeAmplitudeCenterQ : ℚ :=
  9802581434685475 / 10000000000000000

@[simp] theorem p2LogTwoCenterQ_cast :
    (p2LogTwoCenterQ : ℝ) = p2LogTwoCenter := by
  norm_num [p2LogTwoCenterQ, p2LogTwoCenter]

@[simp] theorem p2PrimeAmplitudeCenterQ_cast :
    (p2PrimeAmplitudeCenterQ : ℝ) = p2PrimeAmplitudeCenter := by
  norm_num [p2PrimeAmplitudeCenterQ, p2PrimeAmplitudeCenter]

def p2ShiftedPowerTailCenterQ : ℕ → ℚ
  | 3 => 12302203694272605164 / 10 ^ 23
  | 5 => 1513318071016888708 / 10 ^ 26
  | 7 => 248187933250395478 / 10 ^ 29
  | 9 => 457876177281654 / 10 ^ 30
  | 11 => 9009664018164 / 10 ^ 32
  | 13 => 1846555525330 / 10 ^ 35
  | 15 => 389237872480 / 10 ^ 38
  | 17 => 83750453653 / 10 ^ 41
  | 19 => 18304725494 / 10 ^ 44
  | 21 => 4050409104 / 10 ^ 47
  | 23 => 905240534 / 10 ^ 50
  | 25 => 203984837 / 10 ^ 53
  | 27 => 46283155 / 10 ^ 56
  | 29 => 10563071 / 10 ^ 59
  | 31 => 2422946 / 10 ^ 62
  | _ => 0

theorem p2ShiftedPowerTailCenterQ_cast_of_lt
    (k : ℕ) (hk : k < 16) :
    (p2ShiftedPowerTailCenterQ (2 * k + 1) : ℝ) =
      p2ShiftedPowerTailCenter (2 * k + 1) := by
  interval_cases k <;>
    norm_num [p2ShiftedPowerTailCenterQ, p2ShiftedPowerTailCenter] at hk ⊢

/-! ## The 64-term finite-prefix reciprocal model -/

def prefixAQ (n : ℕ) : ℚ := (n : ℚ) + 1 / 4

def prefixDenominatorBaseQ (n : ℕ) (c : ℚ) : ℚ :=
  prefixAQ n ^ 2 + (c / 2) ^ 2

noncomputable def prefixDenominatorPerturbationQ
    (n : ℕ) (c : ℚ) : QPoly :=
  C (c / (2 * prefixDenominatorBaseQ n c)) * X +
    C (1 / (4 * prefixDenominatorBaseQ n c)) * X ^ 2

noncomputable def geometricReciprocalQ (r : QPoly) (N : ℕ) : QPoly :=
  ∑ k ∈ Finset.range N, (-r) ^ k

noncomputable def quarterPrefixTermPolynomialQ
    (n : ℕ) (c : ℚ) (M : ℕ) : QPoly :=
  C (prefixAQ n / (prefixAQ n ^ 2 + 625)) -
    C (prefixAQ n) *
      (C (prefixDenominatorBaseQ n c)⁻¹ *
        geometricReciprocalQ (prefixDenominatorPerturbationQ n c) M)

noncomputable def quarterDifferenceFinitePrefixPolynomialQ
    (c : ℚ) (M : ℕ) : QPoly :=
  ∑ n ∈ Finset.range 64, quarterPrefixTermPolynomialQ n c M

@[simp] theorem prefixAQ_cast (n : ℕ) :
    (prefixAQ n : ℝ) = prefixA n := by
  simp [prefixAQ, prefixA]

@[simp] theorem prefixDenominatorBaseQ_cast (n : ℕ) (c : ℚ) :
    (prefixDenominatorBaseQ n c : ℝ) =
      prefixDenominatorBase n (c : ℝ) := by
  simp [prefixDenominatorBaseQ, prefixDenominatorBase]

theorem toReal_prefixDenominatorPerturbationQ (n : ℕ) (c : ℚ) :
    toReal (prefixDenominatorPerturbationQ n c) =
      prefixDenominatorPerturbation n (c : ℝ) := by
  simp [prefixDenominatorPerturbationQ,
    prefixDenominatorPerturbation]

theorem toReal_geometricReciprocalQ (r : QPoly) (N : ℕ) :
    toReal (geometricReciprocalQ r N) =
      PolyEnclosure.geometricReciprocal (toReal r) N := by
  unfold geometricReciprocalQ PolyEnclosure.geometricReciprocal
  rw [toReal_finset_sum]
  apply Finset.sum_congr rfl
  intro k hk
  simp

theorem toReal_quarterPrefixTermPolynomialQ
    (n : ℕ) (c : ℚ) (M : ℕ) :
    toReal (quarterPrefixTermPolynomialQ n c M) =
      quarterPrefixTermPolynomial n (c : ℝ) M := by
  simp [quarterPrefixTermPolynomialQ, quarterPrefixTermPolynomial,
    toReal_geometricReciprocalQ,
    toReal_prefixDenominatorPerturbationQ]

theorem toReal_quarterDifferenceFinitePrefixPolynomialQ
    (c : ℚ) (M : ℕ) :
    toReal (quarterDifferenceFinitePrefixPolynomialQ c M) =
      quarterDifferenceFinitePrefixPolynomial (c : ℝ) M := by
  unfold quarterDifferenceFinitePrefixPolynomialQ
    quarterDifferenceFinitePrefixPolynomial
  rw [toReal_finset_sum]
  apply Finset.sum_congr rfl
  intro n hn
  exact toReal_quarterPrefixTermPolynomialQ n c M

/-! ## Rational non-prefix defect polynomial -/

noncomputable def p2RationalQuarterTailPolyQ : QPoly :=
  ∑ k ∈ Finset.range 16,
    (C ((-1 : ℚ) ^ k * 625 ^ k *
          p2ShiftedPowerTailCenterQ (2 * k + 1)) -
      C ((-1 : ℚ) ^ k * p2ShiftedPowerTailCenterQ (2 * k + 1) /
          2 ^ (2 * k)) * X ^ (2 * k))

noncomputable def cosTaylorPolynomialQ (N : ℕ) (L : ℚ) : QPoly :=
  ∑ m ∈ Finset.range N,
    C (iPowReQ m * L ^ m / (m.factorial : ℚ)) * X ^ m

noncomputable def p2RationalNonPrefixPolyQ : QPoly :=
  p2RationalQuarterTailPolyQ +
    C p2PrimeAmplitudeCenterQ *
      (1 - cosTaylorPolynomialQ 128 p2LogTwoCenterQ)

theorem toReal_p2RationalQuarterTailPolyQ :
    toReal p2RationalQuarterTailPolyQ = p2RationalQuarterTailPoly := by
  unfold p2RationalQuarterTailPolyQ p2RationalQuarterTailPoly
  rw [toReal_finset_sum]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [toReal_sub, toReal_C, toReal_mul, toReal_pow, toReal_X]
  have hc := p2ShiftedPowerTailCenterQ_cast_of_lt k
    (Finset.mem_range.mp hk)
  simp only [Rat.cast_mul, Rat.cast_pow, Rat.cast_neg, Rat.cast_ofNat,
    Rat.cast_div]
  rw [hc]
  norm_num

theorem toReal_cosTaylorPolynomialQ (N : ℕ) (L : ℚ) :
    toReal (cosTaylorPolynomialQ N L) =
      cosTaylorPolynomial N (L : ℝ) := by
  unfold cosTaylorPolynomialQ cosTaylorPolynomial
  rw [toReal_finset_sum]
  apply Finset.sum_congr rfl
  intro m hm
  simp only [toReal_mul, toReal_C, toReal_pow, toReal_X]
  push_cast
  rw [iPowReQ_cast]

theorem toReal_p2RationalNonPrefixPolyQ :
    toReal p2RationalNonPrefixPolyQ = p2RationalNonPrefixPoly := by
  unfold p2RationalNonPrefixPolyQ p2RationalNonPrefixPoly
  rw [toReal_add, toReal_p2RationalQuarterTailPolyQ, toReal_mul,
    toReal_C, toReal_sub, toReal_one,
    toReal_cosTaylorPolynomialQ]
  rw [p2PrimeAmplitudeCenterQ_cast, p2LogTwoCenterQ_cast]

noncomputable def p2DefectPanelPolynomialQ (c : ℚ) (M : ℕ) : QPoly :=
  quarterDifferenceFinitePrefixPolynomialQ c M +
    shift p2RationalNonPrefixPolyQ c

theorem toReal_p2DefectPanelPolynomialQ (c : ℚ) (M : ℕ) :
    toReal (p2DefectPanelPolynomialQ c M) =
      p2DefectPanelPolynomial (c : ℝ) M := by
  unfold p2DefectPanelPolynomialQ p2DefectPanelPolynomial
  rw [toReal_add, toReal_quarterDifferenceFinitePrefixPolynomialQ,
    toReal_shift, toReal_p2RationalNonPrefixPolyQ]

/-! ## Degree-100 spherical and selected-component mirrors -/

/-- Exact rational form of the Rodrigues-weight moment. -/
def weightMomentQ (n m : ℕ) : ℚ :=
  ∑ l ∈ Finset.range (n + 1),
    (-1 : ℚ) ^ (l + n) * (n.choose l : ℚ) *
      ((1 : ℚ) ^ (m + 2 * (n - l) + 1) -
        (-1 : ℚ) ^ (m + 2 * (n - l) + 1)) /
          (m + 2 * (n - l) + 1 : ℚ)

@[simp] theorem weightMomentQ_cast (n m : ℕ) :
    (weightMomentQ n m : ℝ) = weightMoment n m := by
  unfold weightMomentQ weightMoment
  push_cast
  apply Finset.sum_congr rfl
  intro l _hl
  rfl

/-- Rational mirror of `sphericalJRealPolynomial`. -/
noncomputable def sphericalJRealPolynomialQ (n N : ℕ) : QPoly :=
  C (1 / (2 ^ (n + 1) * (n.factorial : ℚ))) * X ^ n *
    ∑ m ∈ Finset.range N,
      C (iPowReQ m * weightMomentQ n m /
        (m.factorial : ℚ)) * X ^ m

theorem toReal_sphericalJRealPolynomialQ (n N : ℕ) :
    toReal (sphericalJRealPolynomialQ n N) =
      sphericalJRealPolynomial n N := by
  unfold sphericalJRealPolynomialQ sphericalJRealPolynomial
  rw [toReal_mul, toReal_mul, toReal_C, toReal_pow, toReal_X,
    toReal_finset_sum]
  have hlead :
      ((1 / (2 ^ (n + 1) * (n.factorial : ℚ)) : ℚ) : ℝ) =
        1 / (2 ^ (n + 1) * (n.factorial : ℝ)) := by
    simp only [Rat.cast_div, Rat.cast_one, Rat.cast_mul, Rat.cast_pow,
      Rat.cast_ofNat, Rat.cast_natCast]
  rw [hlead]
  apply congrArg (fun p : ℝ[X] =>
    C (1 / (2 ^ (n + 1) * (n.factorial : ℝ))) * X ^ n * p)
  apply Finset.sum_congr rfl
  intro m _hm
  rw [toReal_mul, toReal_C, toReal_pow, toReal_X]
  congr 2
  push_cast
  rw [iPowReQ_cast, weightMomentQ_cast]

/-- Rational mirror of the global p=2 spherical polynomial. -/
noncomputable def p2SphericalRealPolynomialQ (n N : ℕ) : QPoly :=
  (sphericalJRealPolynomialQ n N).comp (C (7 / 16) * X)

theorem toReal_p2SphericalRealPolynomialQ (n N : ℕ) :
    toReal (p2SphericalRealPolynomialQ n N) =
      p2SphericalRealPolynomial n N := by
  unfold p2SphericalRealPolynomialQ p2SphericalRealPolynomial
  rw [toReal_comp, toReal_sphericalJRealPolynomialQ, toReal_mul,
    toReal_C, toReal_X]
  norm_num

/-- Degree-100 spherical model shifted to a rational panel center. -/
noncomputable def p2Spherical100PanelPolynomialQ
    (n : ℕ) (c : ℚ) : QPoly :=
  shift (p2SphericalRealPolynomialQ n 100) c

theorem toReal_p2Spherical100PanelPolynomialQ (n : ℕ) (c : ℚ) :
    toReal (p2Spherical100PanelPolynomialQ n c) =
      p2Spherical100PanelPolynomial n (c : ℝ) := by
  unfold p2Spherical100PanelPolynomialQ
    p2Spherical100PanelPolynomial
  rw [toReal_shift, toReal_p2SphericalRealPolynomialQ]

def p2SelectedPhaseQ (kind : P2SelectedKind) (k : ℕ) : ℚ :=
  match kind with
  | .even => (-1 : ℚ) ^ k
  | .odd => -((-1 : ℚ) ^ k)

@[simp] theorem p2SelectedPhaseQ_cast
    (kind : P2SelectedKind) (k : ℕ) :
    (p2SelectedPhaseQ kind k : ℝ) = p2SelectedPhase kind k := by
  cases kind <;> simp [p2SelectedPhaseQ, p2SelectedPhase]

/-- Exact rational version of the canonical selected-component witness,
including its stored rational scale center. -/
noncomputable def p2SelectedComponent100ScaleCenterPolynomialQ
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) : QPoly :=
  C (p2SelectedPhaseQ kind k.val) *
    (C (p2SelectedScaleCenterQ kind k) *
      p2Spherical100PanelPolynomialQ
        (p2SelectedDegree kind k.val) c)

theorem toReal_p2SelectedComponent100ScaleCenterPolynomialQ
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) :
    toReal (p2SelectedComponent100ScaleCenterPolynomialQ kind k c) =
      p2SelectedComponent100ScaleCenterPolynomial kind k (c : ℝ) := by
  unfold p2SelectedComponent100ScaleCenterPolynomialQ
    p2SelectedComponent100ScaleCenterPolynomial
    p2SelectedComponent100PanelPolynomial
    p2SelectedSphericalPanelPolynomial
  rw [toReal_mul, toReal_C, p2SelectedPhaseQ_cast, toReal_mul,
    toReal_C, toReal_p2Spherical100PanelPolynomialQ]

/-! ## Fully composed canonical panel mirror -/

/-- Rational source of the complete scale-centered panel integrand. -/
noncomputable def p2ScaleCenteredPanelIntegrandPolynomialQ
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) : QPoly :=
  p2DefectPanelPolynomialQ c M *
    (p2SelectedComponent100ScaleCenterPolynomialQ kind j c *
      p2SelectedComponent100ScaleCenterPolynomialQ kind i c)

theorem toReal_p2ScaleCenteredPanelIntegrandPolynomialQ
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) :
    toReal (p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M) =
      p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M := by
  unfold p2ScaleCenteredPanelIntegrandPolynomialQ
    p2ScaleCenteredPanelIntegrandPolynomial
    p2CanonicalPanelIntegrandPolynomial
  rw [toReal_mul, toReal_p2DefectPanelPolynomialQ, toReal_mul,
    toReal_p2SelectedComponent100ScaleCenterPolynomialQ,
    toReal_p2SelectedComponent100ScaleCenterPolynomialQ]
  rfl

/-- The complete canonical panel polynomial packaged as a compositional
rational-cast witness. -/
noncomputable def p2ScaleCenteredPanelIntegrandCastWitness
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) :
    CastWitness
      (p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M) :=
  ⟨p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M,
    (toReal_p2ScaleCenteredPanelIntegrandPolynomialQ
      kind i j c M).symm⟩

/-- Direct handoff from a rational generated panel value to the exact real
integral used by the analytic enclosure theorem. -/
theorem p2ScaleCenteredPanel_exactIntegral_eq_cast
    (kind : P2SelectedKind) (i j : Fin 24) (c h : ℚ) (M : ℕ) :
    PolyEnclosure.exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M)
        (-h : ℝ) (h : ℝ) =
      (exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M)
        (-h) h : ℝ) := by
  rw [← toReal_p2ScaleCenteredPanelIntegrandPolynomialQ]
  simpa using (cast_exactIntegral
    (p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M)
    (-h) h).symm

/-- A generated dense coefficient vector may replace the compositional
rational expression after proving one equality in `ℚ[X]`. -/
theorem p2ScaleCenteredPanel_exactIntegral_ofCoeffs_eq
    {n : ℕ} (v : Fin n → ℚ)
    (kind : P2SelectedKind) (i j : Fin 24) (c h : ℚ) (M : ℕ)
    (hpoly : ofCoeffs v =
      p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M) :
    PolyEnclosure.exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M)
        (-h : ℝ) (h : ℝ) =
      (exactIntegralCoeffs v (-h) h : ℝ) := by
  rw [← toReal_p2ScaleCenteredPanelIntegrandPolynomialQ]
  rw [← hpoly]
  simpa using (cast_exactIntegralCoeffs v (-h) h).symm

/-- Dense polynomial equality plus one rational arithmetic equality closes
the exact real panel integral. -/
theorem p2ScaleCenteredPanel_exactIntegral_ofCoeffs_eq_value
    {n : ℕ} {v : Fin n → ℚ} {value : ℚ}
    (kind : P2SelectedKind) (i j : Fin 24) (c h : ℚ) (M : ℕ)
    (hpoly : ofCoeffs v =
      p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M)
    (hvalue : exactIntegralCoeffs v (-h) h = value) :
    PolyEnclosure.exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M)
        (-h : ℝ) (h : ℝ) = (value : ℝ) := by
  rw [p2ScaleCenteredPanel_exactIntegral_ofCoeffs_eq
    v kind i j c h M hpoly, hvalue]

/-! ## Rational pole Taylor core -/

noncomputable def poleTaylorPolynomialQ (s : ℚ) (m : ℕ) : QPoly :=
  ∑ k ∈ Finset.range m,
    monomial k ((s / 2) ^ k / k.factorial)

theorem toReal_poleTaylorPolynomialQ (s : ℚ) (m : ℕ) :
    toReal (poleTaylorPolynomialQ s m) =
      PoleProjection.poleTaylorPolynomial (s : ℝ) m := by
  unfold poleTaylorPolynomialQ PoleProjection.poleTaylorPolynomial
  rw [toReal_finset_sum]
  apply Finset.sum_congr rfl
  intro k _hk
  rw [toReal_monomial]
  congr 1
  simp only [Rat.cast_div, Rat.cast_pow, Rat.cast_natCast,
    Rat.cast_ofNat]

noncomputable def shiftedLegendreQ (n : ℕ) : QPoly :=
  (Polynomial.shiftedLegendre n).map (Int.castRingHom ℚ)

noncomputable def plainLegendreQ (n : ℕ) : QPoly :=
  (shiftedLegendreQ n).comp
    (C (-(1 / 2 : ℚ)) * X + C (1 / 2 : ℚ))

theorem toReal_shiftedLegendreQ (n : ℕ) :
    toReal (shiftedLegendreQ n) =
      LegendreRodrigues.shiftedLegendreReal n := by
  unfold shiftedLegendreQ LegendreRodrigues.shiftedLegendreReal toReal
  rw [Polynomial.map_map]
  congr 1

theorem toReal_plainLegendreQ (n : ℕ) :
    toReal (plainLegendreQ n) =
      LegendreRodrigues.plainLegendre n := by
  unfold plainLegendreQ LegendreRodrigues.plainLegendre
  rw [toReal_comp, toReal_shiftedLegendreQ, toReal_add, toReal_mul,
    toReal_C, toReal_X, toReal_C]
  norm_num

/-- Rational polynomial under the exact integral defining the pole core. -/
noncomputable def p2PoleTaylorRationalCorePolynomialQ (n : ℕ) : QPoly :=
  (poleTaylorPolynomialQ 1 48).comp (C (7 / 16) * X) *
    plainLegendreQ n

/-- Exact rational value of the pole Taylor core. -/
noncomputable def p2PoleTaylorRationalCoreQ (n : ℕ) : ℚ :=
  exactIntegral (p2PoleTaylorRationalCorePolynomialQ n) (-1) 1

theorem toReal_p2PoleTaylorRationalCorePolynomialQ (n : ℕ) :
    toReal (p2PoleTaylorRationalCorePolynomialQ n) =
      (PoleProjection.poleTaylorPolynomial 1 48).comp
          (C (7 / 16) * X) *
        LegendreRodrigues.plainLegendre n := by
  unfold p2PoleTaylorRationalCorePolynomialQ
  rw [toReal_mul, toReal_comp, toReal_poleTaylorPolynomialQ,
    toReal_mul, toReal_C, toReal_X, toReal_plainLegendreQ]
  norm_num

/-- The ostensibly real pole Taylor core is exactly the cast of its rational
counterpart. -/
theorem p2PoleTaylorRationalCore_eq_cast (n : ℕ) :
    p2PoleTaylorRationalCore n =
      (p2PoleTaylorRationalCoreQ n : ℝ) := by
  unfold p2PoleTaylorRationalCore p2PoleTaylorRationalCoreQ
  rw [cast_exactIntegral, toReal_p2PoleTaylorRationalCorePolynomialQ]
  norm_num

end RatPoly

end RHP2Bridge
