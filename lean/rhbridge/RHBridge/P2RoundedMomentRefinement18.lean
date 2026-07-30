import RHBridge.P2RoundedMomentCorrect18
import RHBridge.P2RoundedMomentRefinementCheck18_0
import RHBridge.P2RoundedMomentRefinementCheck18_32
import RHBridge.P2RoundedMomentRefinementCheck18_64
import RHBridge.P2RoundedMomentRefinementCheck18_96
import RHBridge.P2RoundedMomentRefinementCheck18_128
import RHBridge.P2RoundedMomentRefinementCheck18_160
import RHBridge.P2RoundedMomentRefinementCheck18_192
import RHBridge.P2RoundedMomentRefinementCheck18_224
import RHBridge.P2RoundedMomentRefinementCheck18_256
import RHBridge.P2RoundedMomentRefinementCheck18_288
import RHBridge.P2RoundedMomentRefinementCheck18_320
import RHBridge.P2RoundedMomentRefinementCheck18_352
import RHBridge.P2RoundedMomentRefinementCheck18_384
import RHBridge.P2RoundedMomentRefinementCheck18_416
import RHBridge.P2RoundedMomentRefinementCheck18_448
import RHBridge.P2RoundedMomentRefinementCheck18_480
import RHBridge.P2RoundedMomentRefinementCheck18_512
import RHBridge.P2RoundedMomentRefinementCheck18_544
import RHBridge.P2RoundedMomentRefinementCheck18_576

namespace RHP2Bridge

theorem panel18BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel18MomentData
        P2RoundedFactorCheckpointData.panel18FlatCache
        ⟨18, by decide⟩ panel18MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨18, by decide⟩ r) := by
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
        (panel18BoundedRefinementRange0) panel18BoundedRefinementRange32) panel18BoundedRefinementRange64) panel18BoundedRefinementRange96) panel18BoundedRefinementRange128) panel18BoundedRefinementRange160) panel18BoundedRefinementRange192) panel18BoundedRefinementRange224) panel18BoundedRefinementRange256) panel18BoundedRefinementRange288) panel18BoundedRefinementRange320) panel18BoundedRefinementRange352) panel18BoundedRefinementRange384) panel18BoundedRefinementRange416) panel18BoundedRefinementRange448) panel18BoundedRefinementRange480) panel18BoundedRefinementRange512) panel18BoundedRefinementRange544) panel18BoundedRefinementRange576) r
  simpa only [panel18BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
