import RHBridge.P2RoundedMomentRefinement0
import RHBridge.P2RoundedMomentRefinement1
import RHBridge.P2RoundedMomentRefinement2
import RHBridge.P2RoundedMomentRefinement3
import RHBridge.P2RoundedMomentRefinement4
import RHBridge.P2RoundedMomentRefinement5
import RHBridge.P2RoundedMomentRefinement6
import RHBridge.P2RoundedMomentRefinement7
import RHBridge.P2RoundedMomentRefinement8
import RHBridge.P2RoundedMomentRefinement9
import RHBridge.P2RoundedMomentRefinement10
import RHBridge.P2RoundedMomentRefinement11
import RHBridge.P2RoundedMomentRefinement12
import RHBridge.P2RoundedMomentRefinement13
import RHBridge.P2RoundedMomentRefinement14
import RHBridge.P2RoundedMomentRefinement15
import RHBridge.P2RoundedMomentRefinement16
import RHBridge.P2RoundedMomentRefinement17
import RHBridge.P2RoundedMomentRefinement18
import RHBridge.P2RoundedMomentRefinement19
import RHBridge.P2RoundedMomentRefinement20
import RHBridge.P2RoundedMomentRefinement21
import RHBridge.P2RoundedMomentRefinement22
import RHBridge.P2RoundedMomentRefinement23
import RHBridge.P2RoundedMomentRefinement24
import RHBridge.P2RoundedMomentRefinement25
import RHBridge.P2RoundedMomentRefinement26
import RHBridge.P2RoundedMomentRefinement27
import RHBridge.P2RoundedMomentRefinement28
import RHBridge.P2RoundedMomentRefinement29
import RHBridge.P2RoundedMomentRefinement30
import RHBridge.P2RoundedMomentRefinement31

namespace RHP2Bridge

namespace P2RoundedBoundedCertificate

open P2RoundedSharedEvaluator
open P2RoundedMomentRefinement
open P2RoundedBoundedTriple
open P2PanelCertificateAggregate

/-- The 32 generated direct-compose caches, dispatched by canonical panel. -/
def canonicalRoundedCache (k : Fin 32) : PanelCache :=
  match k.val with
  | 0 => P2RoundedFactorCheckpointData.panel0FlatCache
  | 1 => P2RoundedFactorCheckpointData.panel1FlatCache
  | 2 => P2RoundedFactorCheckpointData.panel2FlatCache
  | 3 => P2RoundedFactorCheckpointData.panel3FlatCache
  | 4 => P2RoundedFactorCheckpointData.panel4FlatCache
  | 5 => P2RoundedFactorCheckpointData.panel5FlatCache
  | 6 => P2RoundedFactorCheckpointData.panel6FlatCache
  | 7 => P2RoundedFactorCheckpointData.panel7FlatCache
  | 8 => P2RoundedFactorCheckpointData.panel8FlatCache
  | 9 => P2RoundedFactorCheckpointData.panel9FlatCache
  | 10 => P2RoundedFactorCheckpointData.panel10FlatCache
  | 11 => P2RoundedFactorCheckpointData.panel11FlatCache
  | 12 => P2RoundedFactorCheckpointData.panel12FlatCache
  | 13 => P2RoundedFactorCheckpointData.panel13FlatCache
  | 14 => P2RoundedFactorCheckpointData.panel14FlatCache
  | 15 => P2RoundedFactorCheckpointData.panel15FlatCache
  | 16 => P2RoundedFactorCheckpointData.panel16FlatCache
  | 17 => P2RoundedFactorCheckpointData.panel17FlatCache
  | 18 => P2RoundedFactorCheckpointData.panel18FlatCache
  | 19 => P2RoundedFactorCheckpointData.panel19FlatCache
  | 20 => P2RoundedFactorCheckpointData.panel20FlatCache
  | 21 => P2RoundedFactorCheckpointData.panel21FlatCache
  | 22 => P2RoundedFactorCheckpointData.panel22FlatCache
  | 23 => P2RoundedFactorCheckpointData.panel23FlatCache
  | 24 => P2RoundedFactorCheckpointData.panel24FlatCache
  | 25 => P2RoundedFactorCheckpointData.panel25FlatCache
  | 26 => P2RoundedFactorCheckpointData.panel26FlatCache
  | 27 => P2RoundedFactorCheckpointData.panel27FlatCache
  | 28 => P2RoundedFactorCheckpointData.panel28FlatCache
  | 29 => P2RoundedFactorCheckpointData.panel29FlatCache
  | 30 => P2RoundedFactorCheckpointData.panel30FlatCache
  | 31 => P2RoundedFactorCheckpointData.panel31FlatCache
  | _ => P2RoundedFactorCheckpointData.panel0FlatCache

/-- The 32 generated exact moment/matvec tables. -/
def canonicalRoundedMomentData (k : Fin 32) : PanelMomentData :=
  match k.val with
  | 0 => P2RoundedFactorCheckpointData.panel0MomentData
  | 1 => P2RoundedFactorCheckpointData.panel1MomentData
  | 2 => P2RoundedFactorCheckpointData.panel2MomentData
  | 3 => P2RoundedFactorCheckpointData.panel3MomentData
  | 4 => P2RoundedFactorCheckpointData.panel4MomentData
  | 5 => P2RoundedFactorCheckpointData.panel5MomentData
  | 6 => P2RoundedFactorCheckpointData.panel6MomentData
  | 7 => P2RoundedFactorCheckpointData.panel7MomentData
  | 8 => P2RoundedFactorCheckpointData.panel8MomentData
  | 9 => P2RoundedFactorCheckpointData.panel9MomentData
  | 10 => P2RoundedFactorCheckpointData.panel10MomentData
  | 11 => P2RoundedFactorCheckpointData.panel11MomentData
  | 12 => P2RoundedFactorCheckpointData.panel12MomentData
  | 13 => P2RoundedFactorCheckpointData.panel13MomentData
  | 14 => P2RoundedFactorCheckpointData.panel14MomentData
  | 15 => P2RoundedFactorCheckpointData.panel15MomentData
  | 16 => P2RoundedFactorCheckpointData.panel16MomentData
  | 17 => P2RoundedFactorCheckpointData.panel17MomentData
  | 18 => P2RoundedFactorCheckpointData.panel18MomentData
  | 19 => P2RoundedFactorCheckpointData.panel19MomentData
  | 20 => P2RoundedFactorCheckpointData.panel20MomentData
  | 21 => P2RoundedFactorCheckpointData.panel21MomentData
  | 22 => P2RoundedFactorCheckpointData.panel22MomentData
  | 23 => P2RoundedFactorCheckpointData.panel23MomentData
  | 24 => P2RoundedFactorCheckpointData.panel24MomentData
  | 25 => P2RoundedFactorCheckpointData.panel25MomentData
  | 26 => P2RoundedFactorCheckpointData.panel26MomentData
  | 27 => P2RoundedFactorCheckpointData.panel27MomentData
  | 28 => P2RoundedFactorCheckpointData.panel28MomentData
  | 29 => P2RoundedFactorCheckpointData.panel29MomentData
  | 30 => P2RoundedFactorCheckpointData.panel30MomentData
  | 31 => P2RoundedFactorCheckpointData.panel31MomentData
  | _ => P2RoundedFactorCheckpointData.panel0MomentData

/-- Every staged table is kernel-identified with its exact
moment and Hankel-matvec specification. -/
theorem canonicalRoundedMomentData_correct :
    ∀ k, (canonicalRoundedMomentData k).CorrectFor
      (canonicalRoundedCache k) := by
  intro k
  fin_cases k
  · exact panel0MomentData_correct
  · exact panel1MomentData_correct
  · exact panel2MomentData_correct
  · exact panel3MomentData_correct
  · exact panel4MomentData_correct
  · exact panel5MomentData_correct
  · exact panel6MomentData_correct
  · exact panel7MomentData_correct
  · exact panel8MomentData_correct
  · exact panel9MomentData_correct
  · exact panel10MomentData_correct
  · exact panel11MomentData_correct
  · exact panel12MomentData_correct
  · exact panel13MomentData_correct
  · exact panel14MomentData_correct
  · exact panel15MomentData_correct
  · exact panel16MomentData_correct
  · exact panel17MomentData_correct
  · exact panel18MomentData_correct
  · exact panel19MomentData_correct
  · exact panel20MomentData_correct
  · exact panel21MomentData_correct
  · exact panel22MomentData_correct
  · exact panel23MomentData_correct
  · exact panel24MomentData_correct
  · exact panel25MomentData_correct
  · exact panel26MomentData_correct
  · exact panel27MomentData_correct
  · exact panel28MomentData_correct
  · exact panel29MomentData_correct
  · exact panel30MomentData_correct
  · exact panel31MomentData_correct

/-- Every direct-compose cache carries the proved analytic
enclosure of the exact canonical panel factors. -/
theorem canonicalRoundedCache_encloses :
    ∀ k, (canonicalRoundedCache k).EnclosesCanonical k := by
  intro k
  fin_cases k
  · exact panel0FlatCache_enclosesCanonical
  · exact panel1FlatCache_enclosesCanonical
  · exact panel2FlatCache_enclosesCanonical
  · exact panel3FlatCache_enclosesCanonical
  · exact panel4FlatCache_enclosesCanonical
  · exact panel5FlatCache_enclosesCanonical
  · exact panel6FlatCache_enclosesCanonical
  · exact panel7FlatCache_enclosesCanonical
  · exact panel8FlatCache_enclosesCanonical
  · exact panel9FlatCache_enclosesCanonical
  · exact panel10FlatCache_enclosesCanonical
  · exact panel11FlatCache_enclosesCanonical
  · exact panel12FlatCache_enclosesCanonical
  · exact panel13FlatCache_enclosesCanonical
  · exact panel14FlatCache_enclosesCanonical
  · exact panel15FlatCache_enclosesCanonical
  · exact panel16FlatCache_enclosesCanonical
  · exact panel17FlatCache_enclosesCanonical
  · exact panel18FlatCache_enclosesCanonical
  · exact panel19FlatCache_enclosesCanonical
  · exact panel20FlatCache_enclosesCanonical
  · exact panel21FlatCache_enclosesCanonical
  · exact panel22FlatCache_enclosesCanonical
  · exact panel23FlatCache_enclosesCanonical
  · exact panel24FlatCache_enclosesCanonical
  · exact panel25FlatCache_enclosesCanonical
  · exact panel26FlatCache_enclosesCanonical
  · exact panel27FlatCache_enclosesCanonical
  · exact panel28FlatCache_enclosesCanonical
  · exact panel29FlatCache_enclosesCanonical
  · exact panel30FlatCache_enclosesCanonical
  · exact panel31FlatCache_enclosesCanonical

/-- All 19,200 bounded panel balls refine the residual-aware
generated panel targets. -/
theorem canonicalRoundedBoundedRefinements :
    BoundedMomentPanelTargetRefinements
      canonicalRoundedCache canonicalRoundedMomentData
      canonicalRoundedMomentData_correct := by
  intro k r
  fin_cases k
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel0BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel1BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel2BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel3BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel4BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel5BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel6BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel7BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel8BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel9BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel10BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel11BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel12BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel13BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel14BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel15BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel16BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel17BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel18BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel19BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel20BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel21BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel22BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel23BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel24BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel25BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel26BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel27BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel28BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel29BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel30BoundedRefinements r
  · simpa [canonicalRoundedCache, canonicalRoundedMomentData] using
      panel31BoundedRefinements r

/-- Canonical aggregate band certificates obtained from the
bounded analytic ledger and the ordinary-kernel rational leaves. -/
theorem roundedBandSumCertificates : BandSumCertificates := by
  exact bandSumCertificates_of_boundedMomentTargetRefinements
    canonicalRoundedCache canonicalRoundedMomentData
    canonicalRoundedMomentData_correct
    canonicalRoundedCache_encloses
    canonicalRoundedBoundedRefinements

/-- Unconditional canonical `p = 2` matrix containment through
the direct-compose, bounded-value certificate architecture. -/
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
  exact p2_matrix_containment_of_bandSumCertificates
    roundedBandSumCertificates

/-- The closed containment theorem discharges the final finite premise
of the fixed-window clipped endpoint theorem. -/
theorem p2_canonical_clipped_endpoint
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact p2_clipped_endpoint_of_matrix_containment_no_parity
    p2_canonical_matrix_containment.1
    p2_canonical_matrix_containment.2 hf

end P2RoundedBoundedCertificate

end RHP2Bridge
