import RHBridge.P2RoundedMomentCorrect31
import RHBridge.P2RoundedMomentRefinementCheck31_0
import RHBridge.P2RoundedMomentRefinementCheck31_32
import RHBridge.P2RoundedMomentRefinementCheck31_64
import RHBridge.P2RoundedMomentRefinementCheck31_96
import RHBridge.P2RoundedMomentRefinementCheck31_128
import RHBridge.P2RoundedMomentRefinementCheck31_160
import RHBridge.P2RoundedMomentRefinementCheck31_192
import RHBridge.P2RoundedMomentRefinementCheck31_224
import RHBridge.P2RoundedMomentRefinementCheck31_256
import RHBridge.P2RoundedMomentRefinementCheck31_288
import RHBridge.P2RoundedMomentRefinementCheck31_320
import RHBridge.P2RoundedMomentRefinementCheck31_352
import RHBridge.P2RoundedMomentRefinementCheck31_384
import RHBridge.P2RoundedMomentRefinementCheck31_416
import RHBridge.P2RoundedMomentRefinementCheck31_448
import RHBridge.P2RoundedMomentRefinementCheck31_480
import RHBridge.P2RoundedMomentRefinementCheck31_512
import RHBridge.P2RoundedMomentRefinementCheck31_544
import RHBridge.P2RoundedMomentRefinementCheck31_576

namespace RHP2Bridge

theorem panel31BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel31MomentData
        P2RoundedFactorCheckpointData.panel31FlatCache
        ⟨31, by decide⟩ panel31MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨31, by decide⟩ r) := by
  intro r
  have hraw := P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31BoundedRefinementRange0) panel31BoundedRefinementRange32) panel31BoundedRefinementRange64) panel31BoundedRefinementRange96) panel31BoundedRefinementRange128) panel31BoundedRefinementRange160) panel31BoundedRefinementRange192) panel31BoundedRefinementRange224) panel31BoundedRefinementRange256) panel31BoundedRefinementRange288) panel31BoundedRefinementRange320) panel31BoundedRefinementRange352) panel31BoundedRefinementRange384) panel31BoundedRefinementRange416) panel31BoundedRefinementRange448) panel31BoundedRefinementRange480) panel31BoundedRefinementRange512) panel31BoundedRefinementRange544) panel31BoundedRefinementRange576) r
  simpa only [panel31BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
