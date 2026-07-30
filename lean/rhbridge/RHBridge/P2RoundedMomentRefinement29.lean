import RHBridge.P2RoundedMomentCorrect29
import RHBridge.P2RoundedMomentRefinementCheck29_0
import RHBridge.P2RoundedMomentRefinementCheck29_32
import RHBridge.P2RoundedMomentRefinementCheck29_64
import RHBridge.P2RoundedMomentRefinementCheck29_96
import RHBridge.P2RoundedMomentRefinementCheck29_128
import RHBridge.P2RoundedMomentRefinementCheck29_160
import RHBridge.P2RoundedMomentRefinementCheck29_192
import RHBridge.P2RoundedMomentRefinementCheck29_224
import RHBridge.P2RoundedMomentRefinementCheck29_256
import RHBridge.P2RoundedMomentRefinementCheck29_288
import RHBridge.P2RoundedMomentRefinementCheck29_320
import RHBridge.P2RoundedMomentRefinementCheck29_352
import RHBridge.P2RoundedMomentRefinementCheck29_384
import RHBridge.P2RoundedMomentRefinementCheck29_416
import RHBridge.P2RoundedMomentRefinementCheck29_448
import RHBridge.P2RoundedMomentRefinementCheck29_480
import RHBridge.P2RoundedMomentRefinementCheck29_512
import RHBridge.P2RoundedMomentRefinementCheck29_544
import RHBridge.P2RoundedMomentRefinementCheck29_576

namespace RHP2Bridge

theorem panel29BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel29MomentData
        P2RoundedFactorCheckpointData.panel29FlatCache
        ⟨29, by decide⟩ panel29MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨29, by decide⟩ r) := by
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
        (panel29BoundedRefinementRange0) panel29BoundedRefinementRange32) panel29BoundedRefinementRange64) panel29BoundedRefinementRange96) panel29BoundedRefinementRange128) panel29BoundedRefinementRange160) panel29BoundedRefinementRange192) panel29BoundedRefinementRange224) panel29BoundedRefinementRange256) panel29BoundedRefinementRange288) panel29BoundedRefinementRange320) panel29BoundedRefinementRange352) panel29BoundedRefinementRange384) panel29BoundedRefinementRange416) panel29BoundedRefinementRange448) panel29BoundedRefinementRange480) panel29BoundedRefinementRange512) panel29BoundedRefinementRange544) panel29BoundedRefinementRange576) r
  simpa only [panel29BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
