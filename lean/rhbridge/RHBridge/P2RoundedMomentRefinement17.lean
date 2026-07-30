import RHBridge.P2RoundedMomentCorrect17
import RHBridge.P2RoundedMomentRefinementCheck17_0
import RHBridge.P2RoundedMomentRefinementCheck17_32
import RHBridge.P2RoundedMomentRefinementCheck17_64
import RHBridge.P2RoundedMomentRefinementCheck17_96
import RHBridge.P2RoundedMomentRefinementCheck17_128
import RHBridge.P2RoundedMomentRefinementCheck17_160
import RHBridge.P2RoundedMomentRefinementCheck17_192
import RHBridge.P2RoundedMomentRefinementCheck17_224
import RHBridge.P2RoundedMomentRefinementCheck17_256
import RHBridge.P2RoundedMomentRefinementCheck17_288
import RHBridge.P2RoundedMomentRefinementCheck17_320
import RHBridge.P2RoundedMomentRefinementCheck17_352
import RHBridge.P2RoundedMomentRefinementCheck17_384
import RHBridge.P2RoundedMomentRefinementCheck17_416
import RHBridge.P2RoundedMomentRefinementCheck17_448
import RHBridge.P2RoundedMomentRefinementCheck17_480
import RHBridge.P2RoundedMomentRefinementCheck17_512
import RHBridge.P2RoundedMomentRefinementCheck17_544
import RHBridge.P2RoundedMomentRefinementCheck17_576

namespace RHP2Bridge

theorem panel17BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel17MomentData
        P2RoundedFactorCheckpointData.panel17FlatCache
        ⟨17, by decide⟩ panel17MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨17, by decide⟩ r) := by
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
        (panel17BoundedRefinementRange0) panel17BoundedRefinementRange32) panel17BoundedRefinementRange64) panel17BoundedRefinementRange96) panel17BoundedRefinementRange128) panel17BoundedRefinementRange160) panel17BoundedRefinementRange192) panel17BoundedRefinementRange224) panel17BoundedRefinementRange256) panel17BoundedRefinementRange288) panel17BoundedRefinementRange320) panel17BoundedRefinementRange352) panel17BoundedRefinementRange384) panel17BoundedRefinementRange416) panel17BoundedRefinementRange448) panel17BoundedRefinementRange480) panel17BoundedRefinementRange512) panel17BoundedRefinementRange544) panel17BoundedRefinementRange576) r
  simpa only [panel17BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
