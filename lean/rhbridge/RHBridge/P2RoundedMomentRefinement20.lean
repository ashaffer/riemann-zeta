import RHBridge.P2RoundedMomentCorrect20
import RHBridge.P2RoundedMomentRefinementCheck20_0
import RHBridge.P2RoundedMomentRefinementCheck20_32
import RHBridge.P2RoundedMomentRefinementCheck20_64
import RHBridge.P2RoundedMomentRefinementCheck20_96
import RHBridge.P2RoundedMomentRefinementCheck20_128
import RHBridge.P2RoundedMomentRefinementCheck20_160
import RHBridge.P2RoundedMomentRefinementCheck20_192
import RHBridge.P2RoundedMomentRefinementCheck20_224
import RHBridge.P2RoundedMomentRefinementCheck20_256
import RHBridge.P2RoundedMomentRefinementCheck20_288
import RHBridge.P2RoundedMomentRefinementCheck20_320
import RHBridge.P2RoundedMomentRefinementCheck20_352
import RHBridge.P2RoundedMomentRefinementCheck20_384
import RHBridge.P2RoundedMomentRefinementCheck20_416
import RHBridge.P2RoundedMomentRefinementCheck20_448
import RHBridge.P2RoundedMomentRefinementCheck20_480
import RHBridge.P2RoundedMomentRefinementCheck20_512
import RHBridge.P2RoundedMomentRefinementCheck20_544
import RHBridge.P2RoundedMomentRefinementCheck20_576

namespace RHP2Bridge

theorem panel20BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel20MomentData
        P2RoundedFactorCheckpointData.panel20FlatCache
        ⟨20, by decide⟩ panel20MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨20, by decide⟩ r) := by
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
        (panel20BoundedRefinementRange0) panel20BoundedRefinementRange32) panel20BoundedRefinementRange64) panel20BoundedRefinementRange96) panel20BoundedRefinementRange128) panel20BoundedRefinementRange160) panel20BoundedRefinementRange192) panel20BoundedRefinementRange224) panel20BoundedRefinementRange256) panel20BoundedRefinementRange288) panel20BoundedRefinementRange320) panel20BoundedRefinementRange352) panel20BoundedRefinementRange384) panel20BoundedRefinementRange416) panel20BoundedRefinementRange448) panel20BoundedRefinementRange480) panel20BoundedRefinementRange512) panel20BoundedRefinementRange544) panel20BoundedRefinementRange576) r
  simpa only [panel20BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
