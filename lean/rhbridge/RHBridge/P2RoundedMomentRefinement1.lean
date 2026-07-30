import RHBridge.P2RoundedMomentCorrect1
import RHBridge.P2RoundedMomentRefinementCheck1_0
import RHBridge.P2RoundedMomentRefinementCheck1_32
import RHBridge.P2RoundedMomentRefinementCheck1_64
import RHBridge.P2RoundedMomentRefinementCheck1_96
import RHBridge.P2RoundedMomentRefinementCheck1_128
import RHBridge.P2RoundedMomentRefinementCheck1_160
import RHBridge.P2RoundedMomentRefinementCheck1_192
import RHBridge.P2RoundedMomentRefinementCheck1_224
import RHBridge.P2RoundedMomentRefinementCheck1_256
import RHBridge.P2RoundedMomentRefinementCheck1_288
import RHBridge.P2RoundedMomentRefinementCheck1_320
import RHBridge.P2RoundedMomentRefinementCheck1_352
import RHBridge.P2RoundedMomentRefinementCheck1_384
import RHBridge.P2RoundedMomentRefinementCheck1_416
import RHBridge.P2RoundedMomentRefinementCheck1_448
import RHBridge.P2RoundedMomentRefinementCheck1_480
import RHBridge.P2RoundedMomentRefinementCheck1_512
import RHBridge.P2RoundedMomentRefinementCheck1_544
import RHBridge.P2RoundedMomentRefinementCheck1_576

namespace RHP2Bridge

theorem panel1BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel1MomentData
        P2RoundedFactorCheckpointData.panel1FlatCache
        ⟨1, by decide⟩ panel1MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨1, by decide⟩ r) := by
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
        (panel1BoundedRefinementRange0) panel1BoundedRefinementRange32) panel1BoundedRefinementRange64) panel1BoundedRefinementRange96) panel1BoundedRefinementRange128) panel1BoundedRefinementRange160) panel1BoundedRefinementRange192) panel1BoundedRefinementRange224) panel1BoundedRefinementRange256) panel1BoundedRefinementRange288) panel1BoundedRefinementRange320) panel1BoundedRefinementRange352) panel1BoundedRefinementRange384) panel1BoundedRefinementRange416) panel1BoundedRefinementRange448) panel1BoundedRefinementRange480) panel1BoundedRefinementRange512) panel1BoundedRefinementRange544) panel1BoundedRefinementRange576) r
  simpa only [panel1BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
