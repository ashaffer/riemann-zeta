import RHBridge.P2RoundedMomentCorrect13
import RHBridge.P2RoundedMomentRefinementCheck13_0
import RHBridge.P2RoundedMomentRefinementCheck13_32
import RHBridge.P2RoundedMomentRefinementCheck13_64
import RHBridge.P2RoundedMomentRefinementCheck13_96
import RHBridge.P2RoundedMomentRefinementCheck13_128
import RHBridge.P2RoundedMomentRefinementCheck13_160
import RHBridge.P2RoundedMomentRefinementCheck13_192
import RHBridge.P2RoundedMomentRefinementCheck13_224
import RHBridge.P2RoundedMomentRefinementCheck13_256
import RHBridge.P2RoundedMomentRefinementCheck13_288
import RHBridge.P2RoundedMomentRefinementCheck13_320
import RHBridge.P2RoundedMomentRefinementCheck13_352
import RHBridge.P2RoundedMomentRefinementCheck13_384
import RHBridge.P2RoundedMomentRefinementCheck13_416
import RHBridge.P2RoundedMomentRefinementCheck13_448
import RHBridge.P2RoundedMomentRefinementCheck13_480
import RHBridge.P2RoundedMomentRefinementCheck13_512
import RHBridge.P2RoundedMomentRefinementCheck13_544
import RHBridge.P2RoundedMomentRefinementCheck13_576

namespace RHP2Bridge

theorem panel13BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel13MomentData
        P2RoundedFactorCheckpointData.panel13FlatCache
        ⟨13, by decide⟩ panel13MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨13, by decide⟩ r) := by
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
        (panel13BoundedRefinementRange0) panel13BoundedRefinementRange32) panel13BoundedRefinementRange64) panel13BoundedRefinementRange96) panel13BoundedRefinementRange128) panel13BoundedRefinementRange160) panel13BoundedRefinementRange192) panel13BoundedRefinementRange224) panel13BoundedRefinementRange256) panel13BoundedRefinementRange288) panel13BoundedRefinementRange320) panel13BoundedRefinementRange352) panel13BoundedRefinementRange384) panel13BoundedRefinementRange416) panel13BoundedRefinementRange448) panel13BoundedRefinementRange480) panel13BoundedRefinementRange512) panel13BoundedRefinementRange544) panel13BoundedRefinementRange576) r
  simpa only [panel13BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
