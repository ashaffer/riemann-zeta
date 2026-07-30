/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelCertificateData
import RHBridge.P2PoleCoefficientCertificate
import RHBridge.P2EntryTable
import Batteries.Data.Vector.Lemmas

/-!
# Low-memory aggregate certificate for canonical `p = 2` containment

The generated artifact stores one rounded sum of the 32 canonical panel
integrals for each of the 600 upper-triangular entries.  Thus the expensive
finite checker need not elaborate a 19,200-row table.  Its only band
obligation is to show that each exact dense sum is within the sum of the 32
individual half-grid rounding errors.

This file consumes those exact-rational obligations and performs all
analytic error accounting in Lean.
-/

namespace RHP2Bridge

open scoped BigOperators

namespace P2PanelCertificateAggregate

/-- The generated rounded positive-half panel sum for either parity block. -/
def generatedBandIntegralQ (e : P2EntryIndex) : ℚ :=
  match e.block with
  | .even => P2PanelCertificateData.evenBandIntegralQ e.row e.col
  | .odd => P2PanelCertificateData.oddBandIntegralQ e.row e.col

/-- The generated final center, rounded to the common `10^-30` grid. -/
def generatedCenterQ (e : P2EntryIndex) : ℚ :=
  match e.block with
  | .even => P2PanelCertificateData.evenCenterNumerator e.row.val e.col.val /
      P2PanelCertificateData.centerScale
  | .odd => P2PanelCertificateData.oddCenterNumerator e.row.val e.col.val /
      P2PanelCertificateData.centerScale

/-- The integer-grid version of the exact stored interval center. -/
def generatedStoredCenterNumerator (e : P2EntryIndex) : ℤ :=
  match e.block with
  | .even => P2PanelCertificateData.evenStoredCenterNumerator e.row.val e.col.val
  | .odd => P2PanelCertificateData.oddStoredCenterNumerator e.row.val e.col.val

def generatedStoredCenterQ (e : P2EntryIndex) : ℚ :=
  generatedStoredCenterNumerator e / P2PanelCertificateData.centerScale

/-- Exact rational assembly used before the final `10^-30` rounding. -/
def generatedApproxCenterQ (e : P2EntryIndex) : ℚ :=
  DenseRatPoly.p2AlphaCenterQ *
      DenseRatPoly.p2EntryDiagonalIndicatorQ e +
    DenseRatPoly.p2InvTwoPiCenterQ * (2 * generatedBandIntegralQ e) +
    DenseRatPoly.p2EntryPoleSignQ e.block *
      DenseRatPoly.p2EntryTaylorPoleCenterQ e

/-- Exact pole product assembled from a supplied coefficient vector. -/
def entryTaylorPoleCenterFromVector
    (poles : Vector ℚ 48) (e : P2EntryIndex) : ℚ :=
  2 * poles.get (p2EntryPoleMode e.block e.col) *
    poles.get (p2EntryPoleMode e.block e.row)

/-- Assembly variant whose 48 pole coefficients are supplied by one shared
vector. -/
def generatedApproxCenterFromPoles
    (poles : Vector ℚ 48) (e : P2EntryIndex) : ℚ :=
  DenseRatPoly.p2AlphaCenterQ *
      DenseRatPoly.p2EntryDiagonalIndicatorQ e +
    DenseRatPoly.p2InvTwoPiCenterQ * (2 * generatedBandIntegralQ e) +
    DenseRatPoly.p2EntryPoleSignQ e.block *
      entryTaylorPoleCenterFromVector poles e

/-- The generated exact pole table, materialized once for row-major center
checking. -/
def generatedPoleCoeffVector : Vector ℚ 48 :=
  Vector.ofFn P2PoleCoefficientCertificateData.poleCoeffQ

@[simp] theorem generatedPoleCoeffVector_get (n : Fin 48) :
    generatedPoleCoeffVector.get n =
      P2PoleCoefficientCertificateData.poleCoeffQ n := by
  simp [generatedPoleCoeffVector]

def finalCenterRoundingRadiusQ : ℚ :=
  1 / (2 * P2PanelCertificateData.centerScale)

def analyticRadiusQ : ℚ :=
  P2PanelCertificateData.analyticRadiusNumerator /
    P2PanelCertificateData.centerScale

/-- The exact dense rational panel sum specialized to the even block. -/
def exactEvenBandIntegralQ (i j : Fin 24) : ℚ :=
  DenseRatPoly.p2EntryPanelSumQ ⟨.even, i, j⟩

/-- The exact dense rational panel sum specialized to the odd block. -/
def exactOddBandIntegralQ (i j : Fin 24) : ℚ :=
  DenseRatPoly.p2EntryPanelSumQ ⟨.odd, i, j⟩

/-- The only expensive finite band obligations retained by the aggregate
consumer. -/
def BandSumCertificates : Prop :=
  P2PanelCertificateData.EvenBandIntegralSumCertificate exactEvenBandIntegralQ ∧
    P2PanelCertificateData.OddBandIntegralSumCertificate exactOddBandIntegralQ

/-- Cheap finite arithmetic: the aggregate band table plus the 48 exact pole
coefficients assemble to the emitted final centers up to half a `10^-30`
grid unit. -/
def CenterRoundingCertificate : Prop :=
  ∀ e : P2UpperEntryIndex,
    |generatedApproxCenterQ e.val - generatedCenterQ e.val| ≤
      finalCenterRoundingRadiusQ

/-- Executable row-major form.  The outer `let` ensures that native
evaluation constructs the 48 exact pole coefficients only once. -/
def SharedCenterRoundingCertificate : Prop :=
  let poles := generatedPoleCoeffVector
  ∀ r : Fin 600,
    |generatedApproxCenterFromPoles poles (p2UpperEntryAt r).val -
        generatedCenterQ (p2UpperEntryAt r).val| ≤
      finalCenterRoundingRadiusQ

/-- A generic sum-of-rounding-errors lemma.  A checker may use this to turn
32 independently rounded panel equalities into the aggregate obligation. -/
theorem abs_sum_sub_of_panel_rounding
    {exact rounded : Fin 32 → ℚ} {ε : ℚ}
    (h : ∀ k, |exact k - rounded k| ≤ ε) :
    |(∑ k, exact k) - ∑ k, rounded k| ≤ 32 * ε := by
  rw [← Finset.sum_sub_distrib]
  calc
    |∑ k, (exact k - rounded k)| ≤ ∑ k, |exact k - rounded k| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _k : Fin 32, ε := Finset.sum_le_sum fun k _ => h k
    _ = 32 * ε := by simp

theorem exactBandIntegral_sub_generated_le
    (h : BandSumCertificates) (e : P2UpperEntryIndex) :
    |DenseRatPoly.p2EntryPanelSumQ e.val -
        generatedBandIntegralQ e.val| ≤
      P2PanelCertificateData.bandIntegralRoundingRadius := by
  rcases e with ⟨⟨block, i, j⟩, hij⟩
  cases block
  · exact h.1 i j hij
  · exact h.2 i j hij

theorem entryPanelSum_sub_generated_le
    (h : BandSumCertificates) (e : P2UpperEntryIndex) :
    |p2EntryPanelSum e.val - (generatedBandIntegralQ e.val : ℝ)| ≤
      (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ) := by
  rw [DenseRatPoly.p2EntryPanelSum_eq_cast_dense]
  rw [← Rat.cast_sub, ← Rat.cast_abs]
  exact_mod_cast exactBandIntegral_sub_generated_le h e

theorem positiveHalfBandIntegral_sub_generated_le
    (h : BandSumCertificates) (e : P2UpperEntryIndex) :
    |p2PositiveHalfBandIntegral e.val -
        (generatedBandIntegralQ e.val : ℝ)| ≤
      p2PositiveHalfBandErrorBound +
        (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ) := by
  calc
    |p2PositiveHalfBandIntegral e.val -
        (generatedBandIntegralQ e.val : ℝ)| ≤
      |p2PositiveHalfBandIntegral e.val - p2EntryPanelSum e.val| +
        |p2EntryPanelSum e.val - (generatedBandIntegralQ e.val : ℝ)| :=
      abs_sub_le _ _ _
    _ ≤ p2PositiveHalfBandErrorBound +
        (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ) :=
      add_le_add
        (abs_p2PositiveHalfBandIntegral_sub_entryPanelSum_le e.val)
        (entryPanelSum_sub_generated_le h e)

theorem abs_generatedBandIntegral_le
    (h : BandSumCertificates) (e : P2UpperEntryIndex) :
    |(generatedBandIntegralQ e.val : ℝ)| ≤
      373 + (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ) := by
  calc
    |(generatedBandIntegralQ e.val : ℝ)| =
        |p2EntryPanelSum e.val -
          (p2EntryPanelSum e.val -
            (generatedBandIntegralQ e.val : ℝ))| := by ring_nf
    _ ≤ |p2EntryPanelSum e.val| +
        |p2EntryPanelSum e.val -
          (generatedBandIntegralQ e.val : ℝ)| := abs_sub _ _
    _ ≤ 373 + (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ) :=
      add_le_add (abs_p2EntryPanelSum_le e.val)
        (entryPanelSum_sub_generated_le h e)

theorem generatedStoredCenterQ_eq (e : P2EntryIndex) :
    generatedStoredCenterQ e = DenseRatPoly.p2StoredCenterQ e := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    simp only [generatedStoredCenterQ, generatedStoredCenterNumerator,
      P2PanelCertificateData.evenStoredCenterNumerator,
      P2PanelCertificateData.oddStoredCenterNumerator,
      P2PanelCertificateData.storedScaleMultiplier,
      P2PanelCertificateData.betaScaledNumerator,
      P2PanelCertificateData.centerScale,
      DenseRatPoly.p2StoredCenterQ, p2StoredCenterNumerator]
  all_goals
    by_cases h : i = j
    · subst j
      simp
      norm_num
      ring
    · have hv : i.val ≠ j.val := fun hij => h (Fin.ext hij)
      simp [h, hv]
      norm_num
      ring

private theorem int_grid_fit
    {a b : ℤ} {r R s : ℕ} (hs : 0 < s)
    (h : Int.natAbs (a - b) + r ≤ R) :
    |(a : ℚ) / s - (b : ℚ) / s| + (r : ℚ) / s ≤
      (R : ℚ) / s := by
  have hsQ : (0 : ℚ) < s := by exact_mod_cast hs
  calc
    |(a : ℚ) / s - (b : ℚ) / s| + (r : ℚ) / s =
        ((Int.natAbs (a - b) : ℕ) : ℚ) / s + (r : ℚ) / s := by
      rw [← sub_div, ← Int.cast_sub, abs_div, abs_of_pos hsQ,
        ← Int.cast_abs, Int.abs_eq_natAbs, Int.cast_natCast]
    _ = ((Int.natAbs (a - b) + r : ℕ) : ℚ) / s := by
      push_cast
      ring
    _ ≤ (R : ℚ) / s := by
      exact div_le_div_of_nonneg_right (by exact_mod_cast h) hsQ.le

/-- The integer table checks exactly the real center-radius relation needed
after the common analytic ledger has been paid. -/
theorem generatedCenter_fit
    (e : P2UpperEntryIndex) :
    |(generatedCenterQ e.val : ℝ) - p2StoredCenter e.val| +
        (analyticRadiusQ : ℝ) ≤ p2StoredRadius := by
  have hq :
      |generatedCenterQ e.val - generatedStoredCenterQ e.val| +
          analyticRadiusQ ≤
        (P2PanelCertificateData.storedRadiusNumerator : ℚ) /
          P2PanelCertificateData.centerScale := by
    rcases e with ⟨⟨block, i, j⟩, hij⟩
    cases block
    · have hfit := P2PanelCertificateData.evenCenterFitsStored i j hij
      simpa [generatedCenterQ, generatedStoredCenterQ,
        generatedStoredCenterNumerator, analyticRadiusQ,
        P2PanelCertificateData.centerScale,
        P2PanelCertificateData.storedRadiusNumerator] using
          (int_grid_fit (s := P2PanelCertificateData.centerScale)
            (by norm_num [P2PanelCertificateData.centerScale]) hfit)
    · have hfit := P2PanelCertificateData.oddCenterFitsStored i j hij
      simpa [generatedCenterQ, generatedStoredCenterQ,
        generatedStoredCenterNumerator, analyticRadiusQ,
        P2PanelCertificateData.centerScale,
        P2PanelCertificateData.storedRadiusNumerator] using
          (int_grid_fit (s := P2PanelCertificateData.centerScale)
            (by norm_num [P2PanelCertificateData.centerScale]) hfit)
  have hreal :
      (((|generatedCenterQ e.val - generatedStoredCenterQ e.val| +
          analyticRadiusQ : ℚ) : ℚ) : ℝ) ≤
        ((((P2PanelCertificateData.storedRadiusNumerator : ℚ) /
          P2PanelCertificateData.centerScale : ℚ) : ℚ) : ℝ) := by
    exact_mod_cast hq
  rw [DenseRatPoly.p2StoredCenter_eq_cast_dense,
    ← generatedStoredCenterQ_eq, p2StoredRadius_eq]
  rw [← Rat.cast_sub, ← Rat.cast_abs, ← Rat.cast_add]
  convert hreal using 1
  all_goals
    norm_num [P2PanelCertificateData.storedRadiusNumerator,
      P2PanelCertificateData.centerScale]

@[simp] theorem generatedApproxCenterFromPoles_eq
    (e : P2EntryIndex) :
    generatedApproxCenterFromPoles generatedPoleCoeffVector e =
      generatedApproxCenterQ e := by
  simp only [generatedApproxCenterFromPoles, generatedApproxCenterQ,
    entryTaylorPoleCenterFromVector, generatedPoleCoeffVector_get,
    DenseRatPoly.p2EntryTaylorPoleCenterQ]
  rw [← p2PoleCoeffCertificate (p2EntryPoleMode e.block e.col),
    ← p2PoleCoeffCertificate (p2EntryPoleMode e.block e.row)]

theorem centerRoundingCertificate_of_shared
    (h : SharedCenterRoundingCertificate) : CenterRoundingCertificate := by
  intro e
  have hr := h (p2UpperEntryEquiv.symm e)
  have hidx : p2UpperEntryAt (p2UpperEntryEquiv.symm e) = e :=
    p2UpperEntryEquiv.apply_symm_apply e
  rw [hidx, generatedApproxCenterFromPoles_eq] at hr
  exact hr

set_option maxRecDepth 100000 in
/-- Closed exact-rational verification of the final center rounding. -/
theorem sharedCenterRoundingCertificate : SharedCenterRoundingCertificate := by
  unfold SharedCenterRoundingCertificate
  decide +kernel

theorem centerRoundingCertificate : CenterRoundingCertificate :=
  centerRoundingCertificate_of_shared sharedCenterRoundingCertificate

theorem generatedApproxCenter_eq_cast (e : P2EntryIndex) :
    p2AlphaCenter * p2EntryDiagonalIndicator e +
        p2InvTwoPiCenter * (2 * (generatedBandIntegralQ e : ℝ)) +
        p2EntryPoleSign e.block * p2EntryTaylorPoleCenter e =
      (generatedApproxCenterQ e : ℝ) := by
  unfold generatedApproxCenterQ
  push_cast
  rw [DenseRatPoly.p2EntryTaylorPoleCenter_eq_cast_dense]
  simp

theorem generatedApproxCenter_sub_center_le (e : P2UpperEntryIndex) :
    |(generatedApproxCenterQ e.val : ℝ) -
        (generatedCenterQ e.val : ℝ)| ≤
      (finalCenterRoundingRadiusQ : ℝ) := by
  rw [← Rat.cast_sub, ← Rat.cast_abs]
  exact_mod_cast centerRoundingCertificate e

/-- Lean-verified analytic ledger from the actual scalar entry to the
generated `10^-30` center. -/
theorem abs_p2ScalarEntry_sub_generatedCenter_le
    (h : BandSumCertificates) (e : P2UpperEntryIndex) :
    |p2ScalarEntry e.val - (generatedCenterQ e.val : ℝ)| ≤
      (analyticRadiusQ : ℝ) := by
  let eBand : ℝ := p2PositiveHalfBandErrorBound +
    (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ)
  let B : ℝ := 373 +
    (P2PanelCertificateData.bandIntegralRoundingRadius : ℝ)
  let band0 : ℝ := p2InvTwoPiCenter *
    (2 * (generatedBandIntegralQ e.val : ℝ))
  let pole0 : ℝ := p2EntryPoleSign e.val.block *
    p2EntryTaylorPoleCenter e.val
  have hnorm :
      |(1 / (2 * Real.pi)) * (2 * p2PositiveHalfBandIntegral e.val) -
          band0| ≤
        (8 / 25) * eBand + (2 / 10 ^ 20) * B := by
    exact abs_normalizedPositiveHalfIntegral_sub_center_mul_le
      (by norm_num [eBand, p2PositiveHalfBandErrorBound,
        P2PanelCertificateData.bandIntegralRoundingRadius,
        P2PanelCertificateData.bandIntegralScale])
      (by norm_num [B, P2PanelCertificateData.bandIntegralRoundingRadius,
        P2PanelCertificateData.bandIntegralScale])
      (positiveHalfBandIntegral_sub_generated_le h e)
      (abs_generatedBandIntegral_le h e)
  have hpole :
      |p2SignedPoleContribution e.val - pole0| ≤
        1 / 10 ^ 28 + 1 / 10 ^ 17 := by
    exact (abs_p2SignedPoleContribution_sub_signedCenter_lt_of_taylor_enclosure
      e.val (p2EntryTaylorPoleCenter e.val) (1 / 10 ^ 17)
      (abs_p2TaylorPoleContribution_sub_entryCenter_le e.val)).le
  have hthree :
      |p2ScalarEntry e.val -
          (p2AlphaCenter * p2EntryDiagonalIndicator e.val +
            band0 + pole0)| ≤
        1 / 10 ^ 13 +
          ((8 / 25) * eBand + (2 / 10 ^ 20) * B) +
          (1 / 10 ^ 28 + 1 / 10 ^ 17) := by
    rw [p2ScalarEntry_eq_positiveHalf]
    exact abs_threeTermEntry_sub_approx_le
      (abs_p2Alpha_sub_center_lt.le) hnorm hpole
      (p2EntryDiagonalIndicator_zero_or_one e.val)
  have hassembly :
      p2AlphaCenter * p2EntryDiagonalIndicator e.val + band0 + pole0 =
        (generatedApproxCenterQ e.val : ℝ) := by
    exact generatedApproxCenter_eq_cast e.val
  rw [hassembly] at hthree
  calc
    |p2ScalarEntry e.val - (generatedCenterQ e.val : ℝ)| ≤
        |p2ScalarEntry e.val - (generatedApproxCenterQ e.val : ℝ)| +
          |(generatedApproxCenterQ e.val : ℝ) -
            (generatedCenterQ e.val : ℝ)| := abs_sub_le _ _ _
    _ ≤ (1 / 10 ^ 13 +
          ((8 / 25) * eBand + (2 / 10 ^ 20) * B) +
          (1 / 10 ^ 28 + 1 / 10 ^ 17)) +
        (finalCenterRoundingRadiusQ : ℝ) :=
      add_le_add hthree (generatedApproxCenter_sub_center_le e)
    _ ≤ (analyticRadiusQ : ℝ) := by
      norm_num [eBand, B, p2PositiveHalfBandErrorBound,
        P2PanelCertificateData.bandIntegralRoundingRadius,
        P2PanelCertificateData.bandIntegralScale,
        finalCenterRoundingRadiusQ, analyticRadiusQ,
        P2PanelCertificateData.centerScale,
        P2PanelCertificateData.analyticRadiusNumerator]

theorem upperEntryCenterCertificate_of_bandSumCertificates
    (h : BandSumCertificates) : P2UpperEntryCenterCertificate := by
  intro e
  calc
    |p2ScalarEntry e.val - p2StoredCenter e.val| ≤
        |p2ScalarEntry e.val - (generatedCenterQ e.val : ℝ)| +
          |(generatedCenterQ e.val : ℝ) - p2StoredCenter e.val| :=
      abs_sub_le _ _ _
    _ ≤ (analyticRadiusQ : ℝ) +
        |(generatedCenterQ e.val : ℝ) - p2StoredCenter e.val| :=
      add_le_add (abs_p2ScalarEntry_sub_generatedCenter_le h e) (le_refl _)
    _ ≤ p2StoredRadius := by
      have hfit := generatedCenter_fit e
      linarith

/-- Canonical `p = 2` matrix containment, reduced solely to the two compact
aggregate exact-rational band certificates. -/
theorem p2_matrix_containment_of_bandSumCertificates
    (h : BandSumCertificates) :
    (∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j) ∧
    (∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j) := by
  exact p2_matrix_containment_of_upper_entry_enclosures
    (p2UpperEntryEnclosures_of_centerCertificate
      (upperEntryCenterCertificate_of_bandSumCertificates h))

end P2PanelCertificateAggregate

end RHP2Bridge
