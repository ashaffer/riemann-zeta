import RHBridge.P2RoundedMomentCorrect5
import RHBridge.P2RoundedMomentRefinementCheck5_0
import RHBridge.P2RoundedMomentRefinementCheck5_32
import RHBridge.P2RoundedMomentRefinementCheck5_64
import RHBridge.P2RoundedMomentRefinementCheck5_96
import RHBridge.P2RoundedMomentRefinementCheck5_128
import RHBridge.P2RoundedMomentRefinementCheck5_160
import RHBridge.P2RoundedMomentRefinementCheck5_192
import RHBridge.P2RoundedMomentRefinementCheck5_224
import RHBridge.P2RoundedMomentRefinementCheck5_256
import RHBridge.P2RoundedMomentRefinementCheck5_288
import RHBridge.P2RoundedMomentRefinementCheck5_320
import RHBridge.P2RoundedMomentRefinementCheck5_352
import RHBridge.P2RoundedMomentRefinementCheck5_384
import RHBridge.P2RoundedMomentRefinementCheck5_416
import RHBridge.P2RoundedMomentRefinementCheck5_448
import RHBridge.P2RoundedMomentRefinementCheck5_480
import RHBridge.P2RoundedMomentRefinementCheck5_512
import RHBridge.P2RoundedMomentRefinementCheck5_544
import RHBridge.P2RoundedMomentRefinementCheck5_576

namespace RHP2Bridge

theorem panel5BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel5MomentData
        P2RoundedFactorCheckpointData.panel5FlatCache
        ⟨5, by decide⟩ panel5MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨5, by decide⟩ r) := by
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
        (panel5BoundedRefinementRange0) panel5BoundedRefinementRange32) panel5BoundedRefinementRange64) panel5BoundedRefinementRange96) panel5BoundedRefinementRange128) panel5BoundedRefinementRange160) panel5BoundedRefinementRange192) panel5BoundedRefinementRange224) panel5BoundedRefinementRange256) panel5BoundedRefinementRange288) panel5BoundedRefinementRange320) panel5BoundedRefinementRange352) panel5BoundedRefinementRange384) panel5BoundedRefinementRange416) panel5BoundedRefinementRange448) panel5BoundedRefinementRange480) panel5BoundedRefinementRange512) panel5BoundedRefinementRange544) panel5BoundedRefinementRange576) r
  simpa only [panel5BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
