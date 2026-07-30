import RHBridge.P2RoundedMomentCorrect4
import RHBridge.P2RoundedMomentRefinementCheck4_0
import RHBridge.P2RoundedMomentRefinementCheck4_32
import RHBridge.P2RoundedMomentRefinementCheck4_64
import RHBridge.P2RoundedMomentRefinementCheck4_96
import RHBridge.P2RoundedMomentRefinementCheck4_128
import RHBridge.P2RoundedMomentRefinementCheck4_160
import RHBridge.P2RoundedMomentRefinementCheck4_192
import RHBridge.P2RoundedMomentRefinementCheck4_224
import RHBridge.P2RoundedMomentRefinementCheck4_256
import RHBridge.P2RoundedMomentRefinementCheck4_288
import RHBridge.P2RoundedMomentRefinementCheck4_320
import RHBridge.P2RoundedMomentRefinementCheck4_352
import RHBridge.P2RoundedMomentRefinementCheck4_384
import RHBridge.P2RoundedMomentRefinementCheck4_416
import RHBridge.P2RoundedMomentRefinementCheck4_448
import RHBridge.P2RoundedMomentRefinementCheck4_480
import RHBridge.P2RoundedMomentRefinementCheck4_512
import RHBridge.P2RoundedMomentRefinementCheck4_544
import RHBridge.P2RoundedMomentRefinementCheck4_576

namespace RHP2Bridge

theorem panel4BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel4MomentData
        P2RoundedFactorCheckpointData.panel4FlatCache
        ⟨4, by decide⟩ panel4MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨4, by decide⟩ r) := by
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
        (panel4BoundedRefinementRange0) panel4BoundedRefinementRange32) panel4BoundedRefinementRange64) panel4BoundedRefinementRange96) panel4BoundedRefinementRange128) panel4BoundedRefinementRange160) panel4BoundedRefinementRange192) panel4BoundedRefinementRange224) panel4BoundedRefinementRange256) panel4BoundedRefinementRange288) panel4BoundedRefinementRange320) panel4BoundedRefinementRange352) panel4BoundedRefinementRange384) panel4BoundedRefinementRange416) panel4BoundedRefinementRange448) panel4BoundedRefinementRange480) panel4BoundedRefinementRange512) panel4BoundedRefinementRange544) panel4BoundedRefinementRange576) r
  simpa only [panel4BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
