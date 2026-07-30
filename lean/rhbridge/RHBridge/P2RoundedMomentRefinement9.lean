import RHBridge.P2RoundedMomentCorrect9
import RHBridge.P2RoundedMomentRefinementCheck9_0
import RHBridge.P2RoundedMomentRefinementCheck9_32
import RHBridge.P2RoundedMomentRefinementCheck9_64
import RHBridge.P2RoundedMomentRefinementCheck9_96
import RHBridge.P2RoundedMomentRefinementCheck9_128
import RHBridge.P2RoundedMomentRefinementCheck9_160
import RHBridge.P2RoundedMomentRefinementCheck9_192
import RHBridge.P2RoundedMomentRefinementCheck9_224
import RHBridge.P2RoundedMomentRefinementCheck9_256
import RHBridge.P2RoundedMomentRefinementCheck9_288
import RHBridge.P2RoundedMomentRefinementCheck9_320
import RHBridge.P2RoundedMomentRefinementCheck9_352
import RHBridge.P2RoundedMomentRefinementCheck9_384
import RHBridge.P2RoundedMomentRefinementCheck9_416
import RHBridge.P2RoundedMomentRefinementCheck9_448
import RHBridge.P2RoundedMomentRefinementCheck9_480
import RHBridge.P2RoundedMomentRefinementCheck9_512
import RHBridge.P2RoundedMomentRefinementCheck9_544
import RHBridge.P2RoundedMomentRefinementCheck9_576

namespace RHP2Bridge

theorem panel9BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel9MomentData
        P2RoundedFactorCheckpointData.panel9FlatCache
        ⟨9, by decide⟩ panel9MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨9, by decide⟩ r) := by
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
        (panel9BoundedRefinementRange0) panel9BoundedRefinementRange32) panel9BoundedRefinementRange64) panel9BoundedRefinementRange96) panel9BoundedRefinementRange128) panel9BoundedRefinementRange160) panel9BoundedRefinementRange192) panel9BoundedRefinementRange224) panel9BoundedRefinementRange256) panel9BoundedRefinementRange288) panel9BoundedRefinementRange320) panel9BoundedRefinementRange352) panel9BoundedRefinementRange384) panel9BoundedRefinementRange416) panel9BoundedRefinementRange448) panel9BoundedRefinementRange480) panel9BoundedRefinementRange512) panel9BoundedRefinementRange544) panel9BoundedRefinementRange576) r
  simpa only [panel9BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
