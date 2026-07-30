import RHBridge.P2RoundedMomentCorrect23
import RHBridge.P2RoundedMomentRefinementCheck23_0
import RHBridge.P2RoundedMomentRefinementCheck23_32
import RHBridge.P2RoundedMomentRefinementCheck23_64
import RHBridge.P2RoundedMomentRefinementCheck23_96
import RHBridge.P2RoundedMomentRefinementCheck23_128
import RHBridge.P2RoundedMomentRefinementCheck23_160
import RHBridge.P2RoundedMomentRefinementCheck23_192
import RHBridge.P2RoundedMomentRefinementCheck23_224
import RHBridge.P2RoundedMomentRefinementCheck23_256
import RHBridge.P2RoundedMomentRefinementCheck23_288
import RHBridge.P2RoundedMomentRefinementCheck23_320
import RHBridge.P2RoundedMomentRefinementCheck23_352
import RHBridge.P2RoundedMomentRefinementCheck23_384
import RHBridge.P2RoundedMomentRefinementCheck23_416
import RHBridge.P2RoundedMomentRefinementCheck23_448
import RHBridge.P2RoundedMomentRefinementCheck23_480
import RHBridge.P2RoundedMomentRefinementCheck23_512
import RHBridge.P2RoundedMomentRefinementCheck23_544
import RHBridge.P2RoundedMomentRefinementCheck23_576

namespace RHP2Bridge

theorem panel23BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel23MomentData
        P2RoundedFactorCheckpointData.panel23FlatCache
        ⟨23, by decide⟩ panel23MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨23, by decide⟩ r) := by
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
        (panel23BoundedRefinementRange0) panel23BoundedRefinementRange32) panel23BoundedRefinementRange64) panel23BoundedRefinementRange96) panel23BoundedRefinementRange128) panel23BoundedRefinementRange160) panel23BoundedRefinementRange192) panel23BoundedRefinementRange224) panel23BoundedRefinementRange256) panel23BoundedRefinementRange288) panel23BoundedRefinementRange320) panel23BoundedRefinementRange352) panel23BoundedRefinementRange384) panel23BoundedRefinementRange416) panel23BoundedRefinementRange448) panel23BoundedRefinementRange480) panel23BoundedRefinementRange512) panel23BoundedRefinementRange544) panel23BoundedRefinementRange576) r
  simpa only [panel23BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
