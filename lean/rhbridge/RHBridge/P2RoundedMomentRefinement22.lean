import RHBridge.P2RoundedMomentCorrect22
import RHBridge.P2RoundedMomentRefinementCheck22_0
import RHBridge.P2RoundedMomentRefinementCheck22_32
import RHBridge.P2RoundedMomentRefinementCheck22_64
import RHBridge.P2RoundedMomentRefinementCheck22_96
import RHBridge.P2RoundedMomentRefinementCheck22_128
import RHBridge.P2RoundedMomentRefinementCheck22_160
import RHBridge.P2RoundedMomentRefinementCheck22_192
import RHBridge.P2RoundedMomentRefinementCheck22_224
import RHBridge.P2RoundedMomentRefinementCheck22_256
import RHBridge.P2RoundedMomentRefinementCheck22_288
import RHBridge.P2RoundedMomentRefinementCheck22_320
import RHBridge.P2RoundedMomentRefinementCheck22_352
import RHBridge.P2RoundedMomentRefinementCheck22_384
import RHBridge.P2RoundedMomentRefinementCheck22_416
import RHBridge.P2RoundedMomentRefinementCheck22_448
import RHBridge.P2RoundedMomentRefinementCheck22_480
import RHBridge.P2RoundedMomentRefinementCheck22_512
import RHBridge.P2RoundedMomentRefinementCheck22_544
import RHBridge.P2RoundedMomentRefinementCheck22_576

namespace RHP2Bridge

theorem panel22BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel22MomentData
        P2RoundedFactorCheckpointData.panel22FlatCache
        ⟨22, by decide⟩ panel22MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨22, by decide⟩ r) := by
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
        (panel22BoundedRefinementRange0) panel22BoundedRefinementRange32) panel22BoundedRefinementRange64) panel22BoundedRefinementRange96) panel22BoundedRefinementRange128) panel22BoundedRefinementRange160) panel22BoundedRefinementRange192) panel22BoundedRefinementRange224) panel22BoundedRefinementRange256) panel22BoundedRefinementRange288) panel22BoundedRefinementRange320) panel22BoundedRefinementRange352) panel22BoundedRefinementRange384) panel22BoundedRefinementRange416) panel22BoundedRefinementRange448) panel22BoundedRefinementRange480) panel22BoundedRefinementRange512) panel22BoundedRefinementRange544) panel22BoundedRefinementRange576) r
  simpa only [panel22BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
