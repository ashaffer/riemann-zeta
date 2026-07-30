import RHBridge.P2RoundedMomentCorrect12
import RHBridge.P2RoundedMomentRefinementCheck12_0
import RHBridge.P2RoundedMomentRefinementCheck12_32
import RHBridge.P2RoundedMomentRefinementCheck12_64
import RHBridge.P2RoundedMomentRefinementCheck12_96
import RHBridge.P2RoundedMomentRefinementCheck12_128
import RHBridge.P2RoundedMomentRefinementCheck12_160
import RHBridge.P2RoundedMomentRefinementCheck12_192
import RHBridge.P2RoundedMomentRefinementCheck12_224
import RHBridge.P2RoundedMomentRefinementCheck12_256
import RHBridge.P2RoundedMomentRefinementCheck12_288
import RHBridge.P2RoundedMomentRefinementCheck12_320
import RHBridge.P2RoundedMomentRefinementCheck12_352
import RHBridge.P2RoundedMomentRefinementCheck12_384
import RHBridge.P2RoundedMomentRefinementCheck12_416
import RHBridge.P2RoundedMomentRefinementCheck12_448
import RHBridge.P2RoundedMomentRefinementCheck12_480
import RHBridge.P2RoundedMomentRefinementCheck12_512
import RHBridge.P2RoundedMomentRefinementCheck12_544
import RHBridge.P2RoundedMomentRefinementCheck12_576

namespace RHP2Bridge

theorem panel12BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel12MomentData
        P2RoundedFactorCheckpointData.panel12FlatCache
        ⟨12, by decide⟩ panel12MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨12, by decide⟩ r) := by
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
        (panel12BoundedRefinementRange0) panel12BoundedRefinementRange32) panel12BoundedRefinementRange64) panel12BoundedRefinementRange96) panel12BoundedRefinementRange128) panel12BoundedRefinementRange160) panel12BoundedRefinementRange192) panel12BoundedRefinementRange224) panel12BoundedRefinementRange256) panel12BoundedRefinementRange288) panel12BoundedRefinementRange320) panel12BoundedRefinementRange352) panel12BoundedRefinementRange384) panel12BoundedRefinementRange416) panel12BoundedRefinementRange448) panel12BoundedRefinementRange480) panel12BoundedRefinementRange512) panel12BoundedRefinementRange544) panel12BoundedRefinementRange576) r
  simpa only [panel12BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
