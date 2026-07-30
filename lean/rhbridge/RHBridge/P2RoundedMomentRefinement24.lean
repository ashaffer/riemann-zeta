import RHBridge.P2RoundedMomentCorrect24
import RHBridge.P2RoundedMomentRefinementCheck24_0
import RHBridge.P2RoundedMomentRefinementCheck24_32
import RHBridge.P2RoundedMomentRefinementCheck24_64
import RHBridge.P2RoundedMomentRefinementCheck24_96
import RHBridge.P2RoundedMomentRefinementCheck24_128
import RHBridge.P2RoundedMomentRefinementCheck24_160
import RHBridge.P2RoundedMomentRefinementCheck24_192
import RHBridge.P2RoundedMomentRefinementCheck24_224
import RHBridge.P2RoundedMomentRefinementCheck24_256
import RHBridge.P2RoundedMomentRefinementCheck24_288
import RHBridge.P2RoundedMomentRefinementCheck24_320
import RHBridge.P2RoundedMomentRefinementCheck24_352
import RHBridge.P2RoundedMomentRefinementCheck24_384
import RHBridge.P2RoundedMomentRefinementCheck24_416
import RHBridge.P2RoundedMomentRefinementCheck24_448
import RHBridge.P2RoundedMomentRefinementCheck24_480
import RHBridge.P2RoundedMomentRefinementCheck24_512
import RHBridge.P2RoundedMomentRefinementCheck24_544
import RHBridge.P2RoundedMomentRefinementCheck24_576

namespace RHP2Bridge

theorem panel24BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel24MomentData
        P2RoundedFactorCheckpointData.panel24FlatCache
        ⟨24, by decide⟩ panel24MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨24, by decide⟩ r) := by
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
        (panel24BoundedRefinementRange0) panel24BoundedRefinementRange32) panel24BoundedRefinementRange64) panel24BoundedRefinementRange96) panel24BoundedRefinementRange128) panel24BoundedRefinementRange160) panel24BoundedRefinementRange192) panel24BoundedRefinementRange224) panel24BoundedRefinementRange256) panel24BoundedRefinementRange288) panel24BoundedRefinementRange320) panel24BoundedRefinementRange352) panel24BoundedRefinementRange384) panel24BoundedRefinementRange416) panel24BoundedRefinementRange448) panel24BoundedRefinementRange480) panel24BoundedRefinementRange512) panel24BoundedRefinementRange544) panel24BoundedRefinementRange576) r
  simpa only [panel24BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
