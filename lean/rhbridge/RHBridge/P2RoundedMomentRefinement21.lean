import RHBridge.P2RoundedMomentCorrect21
import RHBridge.P2RoundedMomentRefinementCheck21_0
import RHBridge.P2RoundedMomentRefinementCheck21_32
import RHBridge.P2RoundedMomentRefinementCheck21_64
import RHBridge.P2RoundedMomentRefinementCheck21_96
import RHBridge.P2RoundedMomentRefinementCheck21_128
import RHBridge.P2RoundedMomentRefinementCheck21_160
import RHBridge.P2RoundedMomentRefinementCheck21_192
import RHBridge.P2RoundedMomentRefinementCheck21_224
import RHBridge.P2RoundedMomentRefinementCheck21_256
import RHBridge.P2RoundedMomentRefinementCheck21_288
import RHBridge.P2RoundedMomentRefinementCheck21_320
import RHBridge.P2RoundedMomentRefinementCheck21_352
import RHBridge.P2RoundedMomentRefinementCheck21_384
import RHBridge.P2RoundedMomentRefinementCheck21_416
import RHBridge.P2RoundedMomentRefinementCheck21_448
import RHBridge.P2RoundedMomentRefinementCheck21_480
import RHBridge.P2RoundedMomentRefinementCheck21_512
import RHBridge.P2RoundedMomentRefinementCheck21_544
import RHBridge.P2RoundedMomentRefinementCheck21_576

namespace RHP2Bridge

theorem panel21BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel21MomentData
        P2RoundedFactorCheckpointData.panel21FlatCache
        ⟨21, by decide⟩ panel21MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨21, by decide⟩ r) := by
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
        (panel21BoundedRefinementRange0) panel21BoundedRefinementRange32) panel21BoundedRefinementRange64) panel21BoundedRefinementRange96) panel21BoundedRefinementRange128) panel21BoundedRefinementRange160) panel21BoundedRefinementRange192) panel21BoundedRefinementRange224) panel21BoundedRefinementRange256) panel21BoundedRefinementRange288) panel21BoundedRefinementRange320) panel21BoundedRefinementRange352) panel21BoundedRefinementRange384) panel21BoundedRefinementRange416) panel21BoundedRefinementRange448) panel21BoundedRefinementRange480) panel21BoundedRefinementRange512) panel21BoundedRefinementRange544) panel21BoundedRefinementRange576) r
  simpa only [panel21BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
