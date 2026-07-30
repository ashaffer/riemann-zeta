/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelCertificateAggregate

/-!
# Finite rounded-ball boundary for canonical `p = 2`

This file isolates the small theorem that a rounded evaluator must discharge.
For each of the 600 upper-triangular entries, the evaluator supplies a rational
center and a rational radius enclosing the exact dense panel sum.  The finite
certificate checks that this ball fits inside the generated aggregate band's
`10^-15` rational allowance.

No analytic statement is decided by computation here: `hEncloses` is an
ordinary Lean theorem.  Only the final rational ball-containment predicate is
intended for `decide +kernel`.
-/

namespace RHP2Bridge

open scoped BigOperators

namespace P2RoundedBandCertificate

open P2PanelCertificateAggregate

/-- The compact rational predicate checked after rounded evaluation. -/
def FitsGeneratedBand
    (center radius : P2EntryIndex → ℚ) : Prop :=
  ∀ e : P2UpperEntryIndex,
    |center e.val - generatedBandIntegralQ e.val| + radius e.val ≤
      P2PanelCertificateData.bandIntegralRoundingRadius

/-- A rounded ball around an exact value that fits in the generated band
implies the generated aggregate certificate for that value. -/
theorem abs_exact_sub_generated_le_of_ball
    {exact center generated radius allowance : ℚ}
    (hEncloses : |exact - center| ≤ radius)
    (hFits : |center - generated| + radius ≤ allowance) :
    |exact - generated| ≤ allowance := by
  calc
    |exact - generated| = |(exact - center) + (center - generated)| := by
      ring_nf
    _ ≤ |exact - center| + |center - generated| := abs_add_le _ _
    _ ≤ radius + |center - generated| :=
      add_le_add hEncloses (le_refl _)
    _ = |center - generated| + radius := add_comm _ _
    _ ≤ allowance := hFits

/-- Semantic rounded enclosures plus the finite rational predicate imply the
two aggregate band-sum obligations consumed by the analytic proof. -/
theorem bandSumCertificates_of_fitsGeneratedBand
    (center radius : P2EntryIndex → ℚ)
    (hEncloses : ∀ e : P2UpperEntryIndex,
      |DenseRatPoly.p2EntryPanelSumQ e.val - center e.val| ≤ radius e.val)
    (hFits : FitsGeneratedBand center radius) :
    BandSumCertificates := by
  constructor
  · intro i j hij
    let e : P2UpperEntryIndex := ⟨⟨.even, i, j⟩, hij⟩
    exact abs_exact_sub_generated_le_of_ball (hEncloses e) (hFits e)
  · intro i j hij
    let e : P2UpperEntryIndex := ⟨⟨.odd, i, j⟩, hij⟩
    exact abs_exact_sub_generated_le_of_ball (hEncloses e) (hFits e)

/-- Enumeration-indexed variant.  This is the preferred executable boundary:
it permits a single shared 600-entry vector to be materialized by an outer
`let`, while the semantic proof uses the proved bijection of the generated
upper-entry table. -/
def FitsGeneratedBandTable
    (center radius : Fin 600 → ℚ) : Prop :=
  ∀ r : Fin 600,
    |center r - generatedBandIntegralQ (p2UpperEntryAt r).val| + radius r ≤
      P2PanelCertificateData.bandIntegralRoundingRadius

theorem bandSumCertificates_of_fitsGeneratedBandTable
    (center radius : Fin 600 → ℚ)
    (hEncloses : ∀ r : Fin 600,
      |DenseRatPoly.p2EntryPanelSumQ (p2UpperEntryAt r).val - center r| ≤
        radius r)
    (hFits : FitsGeneratedBandTable center radius) :
    BandSumCertificates := by
  constructor
  · intro i j hij
    let e : P2UpperEntryIndex := ⟨⟨.even, i, j⟩, hij⟩
    let r := p2UpperEntryEquiv.symm e
    have hr : p2UpperEntryAt r = e := p2UpperEntryEquiv.apply_symm_apply e
    have h := abs_exact_sub_generated_le_of_ball (hEncloses r) (hFits r)
    rw [hr] at h
    simpa [exactEvenBandIntegralQ, generatedBandIntegralQ, e] using h
  · intro i j hij
    let e : P2UpperEntryIndex := ⟨⟨.odd, i, j⟩, hij⟩
    let r := p2UpperEntryEquiv.symm e
    have hr : p2UpperEntryAt r = e := p2UpperEntryEquiv.apply_symm_apply e
    have h := abs_exact_sub_generated_le_of_ball (hEncloses r) (hFits r)
    rw [hr] at h
    simpa [exactOddBandIntegralQ, generatedBandIntegralQ, e] using h

end P2RoundedBandCertificate

end RHP2Bridge
