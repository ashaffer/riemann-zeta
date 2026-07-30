import RHBridge.P2RoundedMomentCorrect16
import RHBridge.P2RoundedMomentRefinementCheck16_0
import RHBridge.P2RoundedMomentRefinementCheck16_32
import RHBridge.P2RoundedMomentRefinementCheck16_64
import RHBridge.P2RoundedMomentRefinementCheck16_96
import RHBridge.P2RoundedMomentRefinementCheck16_128
import RHBridge.P2RoundedMomentRefinementCheck16_160
import RHBridge.P2RoundedMomentRefinementCheck16_192
import RHBridge.P2RoundedMomentRefinementCheck16_224
import RHBridge.P2RoundedMomentRefinementCheck16_256
import RHBridge.P2RoundedMomentRefinementCheck16_288
import RHBridge.P2RoundedMomentRefinementCheck16_320
import RHBridge.P2RoundedMomentRefinementCheck16_352
import RHBridge.P2RoundedMomentRefinementCheck16_384
import RHBridge.P2RoundedMomentRefinementCheck16_416
import RHBridge.P2RoundedMomentRefinementCheck16_448
import RHBridge.P2RoundedMomentRefinementCheck16_480
import RHBridge.P2RoundedMomentRefinementCheck16_512
import RHBridge.P2RoundedMomentRefinementCheck16_544
import RHBridge.P2RoundedMomentRefinementCheck16_576

namespace RHP2Bridge

theorem panel16BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel16MomentData
        P2RoundedFactorCheckpointData.panel16FlatCache
        ⟨16, by decide⟩ panel16MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨16, by decide⟩ r) := by
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
        (panel16BoundedRefinementRange0) panel16BoundedRefinementRange32) panel16BoundedRefinementRange64) panel16BoundedRefinementRange96) panel16BoundedRefinementRange128) panel16BoundedRefinementRange160) panel16BoundedRefinementRange192) panel16BoundedRefinementRange224) panel16BoundedRefinementRange256) panel16BoundedRefinementRange288) panel16BoundedRefinementRange320) panel16BoundedRefinementRange352) panel16BoundedRefinementRange384) panel16BoundedRefinementRange416) panel16BoundedRefinementRange448) panel16BoundedRefinementRange480) panel16BoundedRefinementRange512) panel16BoundedRefinementRange544) panel16BoundedRefinementRange576) r
  simpa only [panel16BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
