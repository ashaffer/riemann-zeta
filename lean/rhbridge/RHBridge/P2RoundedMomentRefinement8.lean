import RHBridge.P2RoundedMomentCorrect8
import RHBridge.P2RoundedMomentRefinementCheck8_0
import RHBridge.P2RoundedMomentRefinementCheck8_32
import RHBridge.P2RoundedMomentRefinementCheck8_64
import RHBridge.P2RoundedMomentRefinementCheck8_96
import RHBridge.P2RoundedMomentRefinementCheck8_128
import RHBridge.P2RoundedMomentRefinementCheck8_160
import RHBridge.P2RoundedMomentRefinementCheck8_192
import RHBridge.P2RoundedMomentRefinementCheck8_224
import RHBridge.P2RoundedMomentRefinementCheck8_256
import RHBridge.P2RoundedMomentRefinementCheck8_288
import RHBridge.P2RoundedMomentRefinementCheck8_320
import RHBridge.P2RoundedMomentRefinementCheck8_352
import RHBridge.P2RoundedMomentRefinementCheck8_384
import RHBridge.P2RoundedMomentRefinementCheck8_416
import RHBridge.P2RoundedMomentRefinementCheck8_448
import RHBridge.P2RoundedMomentRefinementCheck8_480
import RHBridge.P2RoundedMomentRefinementCheck8_512
import RHBridge.P2RoundedMomentRefinementCheck8_544
import RHBridge.P2RoundedMomentRefinementCheck8_576

namespace RHP2Bridge

theorem panel8BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel8MomentData
        P2RoundedFactorCheckpointData.panel8FlatCache
        ⟨8, by decide⟩ panel8MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨8, by decide⟩ r) := by
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
        (panel8BoundedRefinementRange0) panel8BoundedRefinementRange32) panel8BoundedRefinementRange64) panel8BoundedRefinementRange96) panel8BoundedRefinementRange128) panel8BoundedRefinementRange160) panel8BoundedRefinementRange192) panel8BoundedRefinementRange224) panel8BoundedRefinementRange256) panel8BoundedRefinementRange288) panel8BoundedRefinementRange320) panel8BoundedRefinementRange352) panel8BoundedRefinementRange384) panel8BoundedRefinementRange416) panel8BoundedRefinementRange448) panel8BoundedRefinementRange480) panel8BoundedRefinementRange512) panel8BoundedRefinementRange544) panel8BoundedRefinementRange576) r
  simpa only [panel8BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
