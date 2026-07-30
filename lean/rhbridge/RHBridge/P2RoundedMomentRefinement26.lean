import RHBridge.P2RoundedMomentCorrect26
import RHBridge.P2RoundedMomentRefinementCheck26_0
import RHBridge.P2RoundedMomentRefinementCheck26_32
import RHBridge.P2RoundedMomentRefinementCheck26_64
import RHBridge.P2RoundedMomentRefinementCheck26_96
import RHBridge.P2RoundedMomentRefinementCheck26_128
import RHBridge.P2RoundedMomentRefinementCheck26_160
import RHBridge.P2RoundedMomentRefinementCheck26_192
import RHBridge.P2RoundedMomentRefinementCheck26_224
import RHBridge.P2RoundedMomentRefinementCheck26_256
import RHBridge.P2RoundedMomentRefinementCheck26_288
import RHBridge.P2RoundedMomentRefinementCheck26_320
import RHBridge.P2RoundedMomentRefinementCheck26_352
import RHBridge.P2RoundedMomentRefinementCheck26_384
import RHBridge.P2RoundedMomentRefinementCheck26_416
import RHBridge.P2RoundedMomentRefinementCheck26_448
import RHBridge.P2RoundedMomentRefinementCheck26_480
import RHBridge.P2RoundedMomentRefinementCheck26_512
import RHBridge.P2RoundedMomentRefinementCheck26_544
import RHBridge.P2RoundedMomentRefinementCheck26_576

namespace RHP2Bridge

theorem panel26BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel26MomentData
        P2RoundedFactorCheckpointData.panel26FlatCache
        ⟨26, by decide⟩ panel26MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨26, by decide⟩ r) := by
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
        (panel26BoundedRefinementRange0) panel26BoundedRefinementRange32) panel26BoundedRefinementRange64) panel26BoundedRefinementRange96) panel26BoundedRefinementRange128) panel26BoundedRefinementRange160) panel26BoundedRefinementRange192) panel26BoundedRefinementRange224) panel26BoundedRefinementRange256) panel26BoundedRefinementRange288) panel26BoundedRefinementRange320) panel26BoundedRefinementRange352) panel26BoundedRefinementRange384) panel26BoundedRefinementRange416) panel26BoundedRefinementRange448) panel26BoundedRefinementRange480) panel26BoundedRefinementRange512) panel26BoundedRefinementRange544) panel26BoundedRefinementRange576) r
  simpa only [panel26BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
