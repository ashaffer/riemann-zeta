import RHBridge.P2RoundedMomentCorrect19
import RHBridge.P2RoundedMomentRefinementCheck19_0
import RHBridge.P2RoundedMomentRefinementCheck19_32
import RHBridge.P2RoundedMomentRefinementCheck19_64
import RHBridge.P2RoundedMomentRefinementCheck19_96
import RHBridge.P2RoundedMomentRefinementCheck19_128
import RHBridge.P2RoundedMomentRefinementCheck19_160
import RHBridge.P2RoundedMomentRefinementCheck19_192
import RHBridge.P2RoundedMomentRefinementCheck19_224
import RHBridge.P2RoundedMomentRefinementCheck19_256
import RHBridge.P2RoundedMomentRefinementCheck19_288
import RHBridge.P2RoundedMomentRefinementCheck19_320
import RHBridge.P2RoundedMomentRefinementCheck19_352
import RHBridge.P2RoundedMomentRefinementCheck19_384
import RHBridge.P2RoundedMomentRefinementCheck19_416
import RHBridge.P2RoundedMomentRefinementCheck19_448
import RHBridge.P2RoundedMomentRefinementCheck19_480
import RHBridge.P2RoundedMomentRefinementCheck19_512
import RHBridge.P2RoundedMomentRefinementCheck19_544
import RHBridge.P2RoundedMomentRefinementCheck19_576

namespace RHP2Bridge

theorem panel19BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel19MomentData
        P2RoundedFactorCheckpointData.panel19FlatCache
        ⟨19, by decide⟩ panel19MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨19, by decide⟩ r) := by
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
        (panel19BoundedRefinementRange0) panel19BoundedRefinementRange32) panel19BoundedRefinementRange64) panel19BoundedRefinementRange96) panel19BoundedRefinementRange128) panel19BoundedRefinementRange160) panel19BoundedRefinementRange192) panel19BoundedRefinementRange224) panel19BoundedRefinementRange256) panel19BoundedRefinementRange288) panel19BoundedRefinementRange320) panel19BoundedRefinementRange352) panel19BoundedRefinementRange384) panel19BoundedRefinementRange416) panel19BoundedRefinementRange448) panel19BoundedRefinementRange480) panel19BoundedRefinementRange512) panel19BoundedRefinementRange544) panel19BoundedRefinementRange576) r
  simpa only [panel19BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
