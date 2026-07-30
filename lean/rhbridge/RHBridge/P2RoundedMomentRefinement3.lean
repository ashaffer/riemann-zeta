import RHBridge.P2RoundedMomentCorrect3
import RHBridge.P2RoundedMomentRefinementCheck3_0
import RHBridge.P2RoundedMomentRefinementCheck3_32
import RHBridge.P2RoundedMomentRefinementCheck3_64
import RHBridge.P2RoundedMomentRefinementCheck3_96
import RHBridge.P2RoundedMomentRefinementCheck3_128
import RHBridge.P2RoundedMomentRefinementCheck3_160
import RHBridge.P2RoundedMomentRefinementCheck3_192
import RHBridge.P2RoundedMomentRefinementCheck3_224
import RHBridge.P2RoundedMomentRefinementCheck3_256
import RHBridge.P2RoundedMomentRefinementCheck3_288
import RHBridge.P2RoundedMomentRefinementCheck3_320
import RHBridge.P2RoundedMomentRefinementCheck3_352
import RHBridge.P2RoundedMomentRefinementCheck3_384
import RHBridge.P2RoundedMomentRefinementCheck3_416
import RHBridge.P2RoundedMomentRefinementCheck3_448
import RHBridge.P2RoundedMomentRefinementCheck3_480
import RHBridge.P2RoundedMomentRefinementCheck3_512
import RHBridge.P2RoundedMomentRefinementCheck3_544
import RHBridge.P2RoundedMomentRefinementCheck3_576

namespace RHP2Bridge

theorem panel3BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel3MomentData
        P2RoundedFactorCheckpointData.panel3FlatCache
        ⟨3, by decide⟩ panel3MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨3, by decide⟩ r) := by
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
        (panel3BoundedRefinementRange0) panel3BoundedRefinementRange32) panel3BoundedRefinementRange64) panel3BoundedRefinementRange96) panel3BoundedRefinementRange128) panel3BoundedRefinementRange160) panel3BoundedRefinementRange192) panel3BoundedRefinementRange224) panel3BoundedRefinementRange256) panel3BoundedRefinementRange288) panel3BoundedRefinementRange320) panel3BoundedRefinementRange352) panel3BoundedRefinementRange384) panel3BoundedRefinementRange416) panel3BoundedRefinementRange448) panel3BoundedRefinementRange480) panel3BoundedRefinementRange512) panel3BoundedRefinementRange544) panel3BoundedRefinementRange576) r
  simpa only [panel3BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
