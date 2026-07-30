import RHBridge.P2RoundedMomentCorrect30
import RHBridge.P2RoundedMomentRefinementCheck30_0
import RHBridge.P2RoundedMomentRefinementCheck30_32
import RHBridge.P2RoundedMomentRefinementCheck30_64
import RHBridge.P2RoundedMomentRefinementCheck30_96
import RHBridge.P2RoundedMomentRefinementCheck30_128
import RHBridge.P2RoundedMomentRefinementCheck30_160
import RHBridge.P2RoundedMomentRefinementCheck30_192
import RHBridge.P2RoundedMomentRefinementCheck30_224
import RHBridge.P2RoundedMomentRefinementCheck30_256
import RHBridge.P2RoundedMomentRefinementCheck30_288
import RHBridge.P2RoundedMomentRefinementCheck30_320
import RHBridge.P2RoundedMomentRefinementCheck30_352
import RHBridge.P2RoundedMomentRefinementCheck30_384
import RHBridge.P2RoundedMomentRefinementCheck30_416
import RHBridge.P2RoundedMomentRefinementCheck30_448
import RHBridge.P2RoundedMomentRefinementCheck30_480
import RHBridge.P2RoundedMomentRefinementCheck30_512
import RHBridge.P2RoundedMomentRefinementCheck30_544
import RHBridge.P2RoundedMomentRefinementCheck30_576

namespace RHP2Bridge

theorem panel30BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel30MomentData
        P2RoundedFactorCheckpointData.panel30FlatCache
        ⟨30, by decide⟩ panel30MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨30, by decide⟩ r) := by
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
        (panel30BoundedRefinementRange0) panel30BoundedRefinementRange32) panel30BoundedRefinementRange64) panel30BoundedRefinementRange96) panel30BoundedRefinementRange128) panel30BoundedRefinementRange160) panel30BoundedRefinementRange192) panel30BoundedRefinementRange224) panel30BoundedRefinementRange256) panel30BoundedRefinementRange288) panel30BoundedRefinementRange320) panel30BoundedRefinementRange352) panel30BoundedRefinementRange384) panel30BoundedRefinementRange416) panel30BoundedRefinementRange448) panel30BoundedRefinementRange480) panel30BoundedRefinementRange512) panel30BoundedRefinementRange544) panel30BoundedRefinementRange576) r
  simpa only [panel30BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
