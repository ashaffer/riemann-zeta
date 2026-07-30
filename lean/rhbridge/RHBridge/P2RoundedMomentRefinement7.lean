import RHBridge.P2RoundedMomentCorrect7
import RHBridge.P2RoundedMomentRefinementCheck7_0
import RHBridge.P2RoundedMomentRefinementCheck7_32
import RHBridge.P2RoundedMomentRefinementCheck7_64
import RHBridge.P2RoundedMomentRefinementCheck7_96
import RHBridge.P2RoundedMomentRefinementCheck7_128
import RHBridge.P2RoundedMomentRefinementCheck7_160
import RHBridge.P2RoundedMomentRefinementCheck7_192
import RHBridge.P2RoundedMomentRefinementCheck7_224
import RHBridge.P2RoundedMomentRefinementCheck7_256
import RHBridge.P2RoundedMomentRefinementCheck7_288
import RHBridge.P2RoundedMomentRefinementCheck7_320
import RHBridge.P2RoundedMomentRefinementCheck7_352
import RHBridge.P2RoundedMomentRefinementCheck7_384
import RHBridge.P2RoundedMomentRefinementCheck7_416
import RHBridge.P2RoundedMomentRefinementCheck7_448
import RHBridge.P2RoundedMomentRefinementCheck7_480
import RHBridge.P2RoundedMomentRefinementCheck7_512
import RHBridge.P2RoundedMomentRefinementCheck7_544
import RHBridge.P2RoundedMomentRefinementCheck7_576

namespace RHP2Bridge

theorem panel7BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel7MomentData
        P2RoundedFactorCheckpointData.panel7FlatCache
        ⟨7, by decide⟩ panel7MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨7, by decide⟩ r) := by
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
        (panel7BoundedRefinementRange0) panel7BoundedRefinementRange32) panel7BoundedRefinementRange64) panel7BoundedRefinementRange96) panel7BoundedRefinementRange128) panel7BoundedRefinementRange160) panel7BoundedRefinementRange192) panel7BoundedRefinementRange224) panel7BoundedRefinementRange256) panel7BoundedRefinementRange288) panel7BoundedRefinementRange320) panel7BoundedRefinementRange352) panel7BoundedRefinementRange384) panel7BoundedRefinementRange416) panel7BoundedRefinementRange448) panel7BoundedRefinementRange480) panel7BoundedRefinementRange512) panel7BoundedRefinementRange544) panel7BoundedRefinementRange576) r
  simpa only [panel7BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
