import RHBridge.P2RoundedMomentCorrect2
import RHBridge.P2RoundedMomentRefinementCheck2_0
import RHBridge.P2RoundedMomentRefinementCheck2_32
import RHBridge.P2RoundedMomentRefinementCheck2_64
import RHBridge.P2RoundedMomentRefinementCheck2_96
import RHBridge.P2RoundedMomentRefinementCheck2_128
import RHBridge.P2RoundedMomentRefinementCheck2_160
import RHBridge.P2RoundedMomentRefinementCheck2_192
import RHBridge.P2RoundedMomentRefinementCheck2_224
import RHBridge.P2RoundedMomentRefinementCheck2_256
import RHBridge.P2RoundedMomentRefinementCheck2_288
import RHBridge.P2RoundedMomentRefinementCheck2_320
import RHBridge.P2RoundedMomentRefinementCheck2_352
import RHBridge.P2RoundedMomentRefinementCheck2_384
import RHBridge.P2RoundedMomentRefinementCheck2_416
import RHBridge.P2RoundedMomentRefinementCheck2_448
import RHBridge.P2RoundedMomentRefinementCheck2_480
import RHBridge.P2RoundedMomentRefinementCheck2_512
import RHBridge.P2RoundedMomentRefinementCheck2_544
import RHBridge.P2RoundedMomentRefinementCheck2_576

namespace RHP2Bridge

theorem panel2BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel2MomentData
        P2RoundedFactorCheckpointData.panel2FlatCache
        ⟨2, by decide⟩ panel2MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨2, by decide⟩ r) := by
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
        (panel2BoundedRefinementRange0) panel2BoundedRefinementRange32) panel2BoundedRefinementRange64) panel2BoundedRefinementRange96) panel2BoundedRefinementRange128) panel2BoundedRefinementRange160) panel2BoundedRefinementRange192) panel2BoundedRefinementRange224) panel2BoundedRefinementRange256) panel2BoundedRefinementRange288) panel2BoundedRefinementRange320) panel2BoundedRefinementRange352) panel2BoundedRefinementRange384) panel2BoundedRefinementRange416) panel2BoundedRefinementRange448) panel2BoundedRefinementRange480) panel2BoundedRefinementRange512) panel2BoundedRefinementRange544) panel2BoundedRefinementRange576) r
  simpa only [panel2BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
