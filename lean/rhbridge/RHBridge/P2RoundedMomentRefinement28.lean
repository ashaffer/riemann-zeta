import RHBridge.P2RoundedMomentCorrect28
import RHBridge.P2RoundedMomentRefinementCheck28_0
import RHBridge.P2RoundedMomentRefinementCheck28_32
import RHBridge.P2RoundedMomentRefinementCheck28_64
import RHBridge.P2RoundedMomentRefinementCheck28_96
import RHBridge.P2RoundedMomentRefinementCheck28_128
import RHBridge.P2RoundedMomentRefinementCheck28_160
import RHBridge.P2RoundedMomentRefinementCheck28_192
import RHBridge.P2RoundedMomentRefinementCheck28_224
import RHBridge.P2RoundedMomentRefinementCheck28_256
import RHBridge.P2RoundedMomentRefinementCheck28_288
import RHBridge.P2RoundedMomentRefinementCheck28_320
import RHBridge.P2RoundedMomentRefinementCheck28_352
import RHBridge.P2RoundedMomentRefinementCheck28_384
import RHBridge.P2RoundedMomentRefinementCheck28_416
import RHBridge.P2RoundedMomentRefinementCheck28_448
import RHBridge.P2RoundedMomentRefinementCheck28_480
import RHBridge.P2RoundedMomentRefinementCheck28_512
import RHBridge.P2RoundedMomentRefinementCheck28_544
import RHBridge.P2RoundedMomentRefinementCheck28_576

namespace RHP2Bridge

theorem panel28BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel28MomentData
        P2RoundedFactorCheckpointData.panel28FlatCache
        ⟨28, by decide⟩ panel28MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨28, by decide⟩ r) := by
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
        (panel28BoundedRefinementRange0) panel28BoundedRefinementRange32) panel28BoundedRefinementRange64) panel28BoundedRefinementRange96) panel28BoundedRefinementRange128) panel28BoundedRefinementRange160) panel28BoundedRefinementRange192) panel28BoundedRefinementRange224) panel28BoundedRefinementRange256) panel28BoundedRefinementRange288) panel28BoundedRefinementRange320) panel28BoundedRefinementRange352) panel28BoundedRefinementRange384) panel28BoundedRefinementRange416) panel28BoundedRefinementRange448) panel28BoundedRefinementRange480) panel28BoundedRefinementRange512) panel28BoundedRefinementRange544) panel28BoundedRefinementRange576) r
  simpa only [panel28BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
