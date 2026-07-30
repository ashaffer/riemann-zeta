import RHBridge.P2RoundedMomentCorrect25
import RHBridge.P2RoundedMomentRefinementCheck25_0
import RHBridge.P2RoundedMomentRefinementCheck25_32
import RHBridge.P2RoundedMomentRefinementCheck25_64
import RHBridge.P2RoundedMomentRefinementCheck25_96
import RHBridge.P2RoundedMomentRefinementCheck25_128
import RHBridge.P2RoundedMomentRefinementCheck25_160
import RHBridge.P2RoundedMomentRefinementCheck25_192
import RHBridge.P2RoundedMomentRefinementCheck25_224
import RHBridge.P2RoundedMomentRefinementCheck25_256
import RHBridge.P2RoundedMomentRefinementCheck25_288
import RHBridge.P2RoundedMomentRefinementCheck25_320
import RHBridge.P2RoundedMomentRefinementCheck25_352
import RHBridge.P2RoundedMomentRefinementCheck25_384
import RHBridge.P2RoundedMomentRefinementCheck25_416
import RHBridge.P2RoundedMomentRefinementCheck25_448
import RHBridge.P2RoundedMomentRefinementCheck25_480
import RHBridge.P2RoundedMomentRefinementCheck25_512
import RHBridge.P2RoundedMomentRefinementCheck25_544
import RHBridge.P2RoundedMomentRefinementCheck25_576

namespace RHP2Bridge

theorem panel25BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel25MomentData
        P2RoundedFactorCheckpointData.panel25FlatCache
        ⟨25, by decide⟩ panel25MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨25, by decide⟩ r) := by
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
        (panel25BoundedRefinementRange0) panel25BoundedRefinementRange32) panel25BoundedRefinementRange64) panel25BoundedRefinementRange96) panel25BoundedRefinementRange128) panel25BoundedRefinementRange160) panel25BoundedRefinementRange192) panel25BoundedRefinementRange224) panel25BoundedRefinementRange256) panel25BoundedRefinementRange288) panel25BoundedRefinementRange320) panel25BoundedRefinementRange352) panel25BoundedRefinementRange384) panel25BoundedRefinementRange416) panel25BoundedRefinementRange448) panel25BoundedRefinementRange480) panel25BoundedRefinementRange512) panel25BoundedRefinementRange544) panel25BoundedRefinementRange576) r
  simpa only [panel25BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
