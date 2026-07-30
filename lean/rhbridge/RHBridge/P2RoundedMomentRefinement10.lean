import RHBridge.P2RoundedMomentCorrect10
import RHBridge.P2RoundedMomentRefinementCheck10_0
import RHBridge.P2RoundedMomentRefinementCheck10_32
import RHBridge.P2RoundedMomentRefinementCheck10_64
import RHBridge.P2RoundedMomentRefinementCheck10_96
import RHBridge.P2RoundedMomentRefinementCheck10_128
import RHBridge.P2RoundedMomentRefinementCheck10_160
import RHBridge.P2RoundedMomentRefinementCheck10_192
import RHBridge.P2RoundedMomentRefinementCheck10_224
import RHBridge.P2RoundedMomentRefinementCheck10_256
import RHBridge.P2RoundedMomentRefinementCheck10_288
import RHBridge.P2RoundedMomentRefinementCheck10_320
import RHBridge.P2RoundedMomentRefinementCheck10_352
import RHBridge.P2RoundedMomentRefinementCheck10_384
import RHBridge.P2RoundedMomentRefinementCheck10_416
import RHBridge.P2RoundedMomentRefinementCheck10_448
import RHBridge.P2RoundedMomentRefinementCheck10_480
import RHBridge.P2RoundedMomentRefinementCheck10_512
import RHBridge.P2RoundedMomentRefinementCheck10_544
import RHBridge.P2RoundedMomentRefinementCheck10_576

namespace RHP2Bridge

theorem panel10BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel10MomentData
        P2RoundedFactorCheckpointData.panel10FlatCache
        ⟨10, by decide⟩ panel10MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨10, by decide⟩ r) := by
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
        (panel10BoundedRefinementRange0) panel10BoundedRefinementRange32) panel10BoundedRefinementRange64) panel10BoundedRefinementRange96) panel10BoundedRefinementRange128) panel10BoundedRefinementRange160) panel10BoundedRefinementRange192) panel10BoundedRefinementRange224) panel10BoundedRefinementRange256) panel10BoundedRefinementRange288) panel10BoundedRefinementRange320) panel10BoundedRefinementRange352) panel10BoundedRefinementRange384) panel10BoundedRefinementRange416) panel10BoundedRefinementRange448) panel10BoundedRefinementRange480) panel10BoundedRefinementRange512) panel10BoundedRefinementRange544) panel10BoundedRefinementRange576) r
  simpa only [panel10BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
