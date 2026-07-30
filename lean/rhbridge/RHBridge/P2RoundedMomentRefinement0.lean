import RHBridge.P2RoundedMomentCorrect0
import RHBridge.P2RoundedMomentRefinementCheck0_0
import RHBridge.P2RoundedMomentRefinementCheck0_32
import RHBridge.P2RoundedMomentRefinementCheck0_64
import RHBridge.P2RoundedMomentRefinementCheck0_96
import RHBridge.P2RoundedMomentRefinementCheck0_128
import RHBridge.P2RoundedMomentRefinementCheck0_160
import RHBridge.P2RoundedMomentRefinementCheck0_192
import RHBridge.P2RoundedMomentRefinementCheck0_224
import RHBridge.P2RoundedMomentRefinementCheck0_256
import RHBridge.P2RoundedMomentRefinementCheck0_288
import RHBridge.P2RoundedMomentRefinementCheck0_320
import RHBridge.P2RoundedMomentRefinementCheck0_352
import RHBridge.P2RoundedMomentRefinementCheck0_384
import RHBridge.P2RoundedMomentRefinementCheck0_416
import RHBridge.P2RoundedMomentRefinementCheck0_448
import RHBridge.P2RoundedMomentRefinementCheck0_480
import RHBridge.P2RoundedMomentRefinementCheck0_512
import RHBridge.P2RoundedMomentRefinementCheck0_544
import RHBridge.P2RoundedMomentRefinementCheck0_576

namespace RHP2Bridge

theorem panel0BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel0MomentData
        P2RoundedFactorCheckpointData.panel0FlatCache
        ⟨0, by decide⟩ panel0MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨0, by decide⟩ r) := by
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
        (panel0BoundedRefinementRange0) panel0BoundedRefinementRange32) panel0BoundedRefinementRange64) panel0BoundedRefinementRange96) panel0BoundedRefinementRange128) panel0BoundedRefinementRange160) panel0BoundedRefinementRange192) panel0BoundedRefinementRange224) panel0BoundedRefinementRange256) panel0BoundedRefinementRange288) panel0BoundedRefinementRange320) panel0BoundedRefinementRange352) panel0BoundedRefinementRange384) panel0BoundedRefinementRange416) panel0BoundedRefinementRange448) panel0BoundedRefinementRange480) panel0BoundedRefinementRange512) panel0BoundedRefinementRange544) panel0BoundedRefinementRange576) r
  simpa only [panel0BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
