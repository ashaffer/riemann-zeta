/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedBandCertificate
import RHBridge.P2RoundedSharedEvaluator

/-!
# Kernel certificate for the canonical `p = 2` rounded band table

The outer `let` is intentional: the 32-panel by 600-entry rounded vector is
constructed once, then all final center-radius comparisons are performed on
that shared value.  The theorem is checked by Lean's kernel evaluator; no
native-code decision axiom is used.
-/

namespace RHP2Bridge

namespace P2RoundedBandCertificateCheck

open P2PanelCertificateAggregate
open P2RoundedSharedEvaluator

/-- Closed rational containment predicate for all 600 rounded aggregate
balls. -/
def FullRoundedBandFits : Prop :=
  let balls := allEntryBalls
  ∀ r : Fin 600,
    |(balls.get r).center -
        generatedBandIntegralQ (p2UpperEntryAt r).val| +
      (balls.get r).radius ≤
        P2PanelCertificateData.bandIntegralRoundingRadius

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Kernel-checked finite arithmetic certificate. -/
theorem fullRoundedBandFits : FullRoundedBandFits := by
  decide +kernel

theorem fitsGeneratedBandTable :
    P2RoundedBandCertificate.FitsGeneratedBandTable
      generatedEntryCenterQ generatedEntryRadiusQ := by
  simpa [FullRoundedBandFits, generatedEntryCenterQ,
    generatedEntryRadiusQ] using fullRoundedBandFits

/-- The kernel predicate and the analytic rounded-enclosure theorem together
discharge the only two hypotheses left by the aggregate containment proof. -/
theorem roundedBandSumCertificates : BandSumCertificates := by
  apply P2RoundedBandCertificate.bandSumCertificates_of_fitsGeneratedBandTable
      generatedEntryCenterQ generatedEntryRadiusQ
  · intro r
    simpa [generatedEntryAt] using
      abs_p2EntryPanelSumQ_sub_generatedEntryCenterQ_le r
  · exact fitsGeneratedBandTable

/-- Unconditional canonical `p = 2` matrix containment.  Its finite leaf is
`fullRoundedBandFits`; all analytic approximation errors are verified by the
ordinary Lean theorems in the rounded evaluator and integral bridge. -/
theorem p2_canonical_matrix_containment :
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
  exact P2PanelCertificateAggregate.p2_matrix_containment_of_bandSumCertificates
    roundedBandSumCertificates

end P2RoundedBandCertificateCheck

end RHP2Bridge
