import RHBridge.P2RoundedMomentCorrect6
import RHBridge.P2RoundedMomentRefinementCheck6_0
import RHBridge.P2RoundedMomentRefinementCheck6_32
import RHBridge.P2RoundedMomentRefinementCheck6_64
import RHBridge.P2RoundedMomentRefinementCheck6_96
import RHBridge.P2RoundedMomentRefinementCheck6_128
import RHBridge.P2RoundedMomentRefinementCheck6_160
import RHBridge.P2RoundedMomentRefinementCheck6_192
import RHBridge.P2RoundedMomentRefinementCheck6_224
import RHBridge.P2RoundedMomentRefinementCheck6_256
import RHBridge.P2RoundedMomentRefinementCheck6_288
import RHBridge.P2RoundedMomentRefinementCheck6_320
import RHBridge.P2RoundedMomentRefinementCheck6_352
import RHBridge.P2RoundedMomentRefinementCheck6_384
import RHBridge.P2RoundedMomentRefinementCheck6_416
import RHBridge.P2RoundedMomentRefinementCheck6_448
import RHBridge.P2RoundedMomentRefinementCheck6_480
import RHBridge.P2RoundedMomentRefinementCheck6_512
import RHBridge.P2RoundedMomentRefinementCheck6_544
import RHBridge.P2RoundedMomentRefinementCheck6_576

namespace RHP2Bridge

theorem panel6BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel6MomentData
        P2RoundedFactorCheckpointData.panel6FlatCache
        ⟨6, by decide⟩ panel6MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨6, by decide⟩ r) := by
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
        (panel6BoundedRefinementRange0) panel6BoundedRefinementRange32) panel6BoundedRefinementRange64) panel6BoundedRefinementRange96) panel6BoundedRefinementRange128) panel6BoundedRefinementRange160) panel6BoundedRefinementRange192) panel6BoundedRefinementRange224) panel6BoundedRefinementRange256) panel6BoundedRefinementRange288) panel6BoundedRefinementRange320) panel6BoundedRefinementRange352) panel6BoundedRefinementRange384) panel6BoundedRefinementRange416) panel6BoundedRefinementRange448) panel6BoundedRefinementRange480) panel6BoundedRefinementRange512) panel6BoundedRefinementRange544) panel6BoundedRefinementRange576) r
  simpa only [panel6BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
