import RHBridge.P2RoundedMomentCorrect15
import RHBridge.P2RoundedMomentRefinementCheck15_0
import RHBridge.P2RoundedMomentRefinementCheck15_32
import RHBridge.P2RoundedMomentRefinementCheck15_64
import RHBridge.P2RoundedMomentRefinementCheck15_96
import RHBridge.P2RoundedMomentRefinementCheck15_128
import RHBridge.P2RoundedMomentRefinementCheck15_160
import RHBridge.P2RoundedMomentRefinementCheck15_192
import RHBridge.P2RoundedMomentRefinementCheck15_224
import RHBridge.P2RoundedMomentRefinementCheck15_256
import RHBridge.P2RoundedMomentRefinementCheck15_288
import RHBridge.P2RoundedMomentRefinementCheck15_320
import RHBridge.P2RoundedMomentRefinementCheck15_352
import RHBridge.P2RoundedMomentRefinementCheck15_384
import RHBridge.P2RoundedMomentRefinementCheck15_416
import RHBridge.P2RoundedMomentRefinementCheck15_448
import RHBridge.P2RoundedMomentRefinementCheck15_480
import RHBridge.P2RoundedMomentRefinementCheck15_512
import RHBridge.P2RoundedMomentRefinementCheck15_544
import RHBridge.P2RoundedMomentRefinementCheck15_576

namespace RHP2Bridge

theorem panel15BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel15MomentData
        P2RoundedFactorCheckpointData.panel15FlatCache
        ⟨15, by decide⟩ panel15MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨15, by decide⟩ r) := by
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
        (panel15BoundedRefinementRange0) panel15BoundedRefinementRange32) panel15BoundedRefinementRange64) panel15BoundedRefinementRange96) panel15BoundedRefinementRange128) panel15BoundedRefinementRange160) panel15BoundedRefinementRange192) panel15BoundedRefinementRange224) panel15BoundedRefinementRange256) panel15BoundedRefinementRange288) panel15BoundedRefinementRange320) panel15BoundedRefinementRange352) panel15BoundedRefinementRange384) panel15BoundedRefinementRange416) panel15BoundedRefinementRange448) panel15BoundedRefinementRange480) panel15BoundedRefinementRange512) panel15BoundedRefinementRange544) panel15BoundedRefinementRange576) r
  simpa only [panel15BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
