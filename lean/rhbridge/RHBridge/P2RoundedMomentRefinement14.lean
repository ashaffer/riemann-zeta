import RHBridge.P2RoundedMomentCorrect14
import RHBridge.P2RoundedMomentRefinementCheck14_0
import RHBridge.P2RoundedMomentRefinementCheck14_32
import RHBridge.P2RoundedMomentRefinementCheck14_64
import RHBridge.P2RoundedMomentRefinementCheck14_96
import RHBridge.P2RoundedMomentRefinementCheck14_128
import RHBridge.P2RoundedMomentRefinementCheck14_160
import RHBridge.P2RoundedMomentRefinementCheck14_192
import RHBridge.P2RoundedMomentRefinementCheck14_224
import RHBridge.P2RoundedMomentRefinementCheck14_256
import RHBridge.P2RoundedMomentRefinementCheck14_288
import RHBridge.P2RoundedMomentRefinementCheck14_320
import RHBridge.P2RoundedMomentRefinementCheck14_352
import RHBridge.P2RoundedMomentRefinementCheck14_384
import RHBridge.P2RoundedMomentRefinementCheck14_416
import RHBridge.P2RoundedMomentRefinementCheck14_448
import RHBridge.P2RoundedMomentRefinementCheck14_480
import RHBridge.P2RoundedMomentRefinementCheck14_512
import RHBridge.P2RoundedMomentRefinementCheck14_544
import RHBridge.P2RoundedMomentRefinementCheck14_576

namespace RHP2Bridge

theorem panel14BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel14MomentData
        P2RoundedFactorCheckpointData.panel14FlatCache
        ⟨14, by decide⟩ panel14MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨14, by decide⟩ r) := by
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
        (panel14BoundedRefinementRange0) panel14BoundedRefinementRange32) panel14BoundedRefinementRange64) panel14BoundedRefinementRange96) panel14BoundedRefinementRange128) panel14BoundedRefinementRange160) panel14BoundedRefinementRange192) panel14BoundedRefinementRange224) panel14BoundedRefinementRange256) panel14BoundedRefinementRange288) panel14BoundedRefinementRange320) panel14BoundedRefinementRange352) panel14BoundedRefinementRange384) panel14BoundedRefinementRange416) panel14BoundedRefinementRange448) panel14BoundedRefinementRange480) panel14BoundedRefinementRange512) panel14BoundedRefinementRange544) panel14BoundedRefinementRange576) r
  simpa only [panel14BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
