import RHBridge.P2RoundedMomentCorrect27
import RHBridge.P2RoundedMomentRefinementCheck27_0
import RHBridge.P2RoundedMomentRefinementCheck27_32
import RHBridge.P2RoundedMomentRefinementCheck27_64
import RHBridge.P2RoundedMomentRefinementCheck27_96
import RHBridge.P2RoundedMomentRefinementCheck27_128
import RHBridge.P2RoundedMomentRefinementCheck27_160
import RHBridge.P2RoundedMomentRefinementCheck27_192
import RHBridge.P2RoundedMomentRefinementCheck27_224
import RHBridge.P2RoundedMomentRefinementCheck27_256
import RHBridge.P2RoundedMomentRefinementCheck27_288
import RHBridge.P2RoundedMomentRefinementCheck27_320
import RHBridge.P2RoundedMomentRefinementCheck27_352
import RHBridge.P2RoundedMomentRefinementCheck27_384
import RHBridge.P2RoundedMomentRefinementCheck27_416
import RHBridge.P2RoundedMomentRefinementCheck27_448
import RHBridge.P2RoundedMomentRefinementCheck27_480
import RHBridge.P2RoundedMomentRefinementCheck27_512
import RHBridge.P2RoundedMomentRefinementCheck27_544
import RHBridge.P2RoundedMomentRefinementCheck27_576

namespace RHP2Bridge

theorem panel27BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel27MomentData
        P2RoundedFactorCheckpointData.panel27FlatCache
        ⟨27, by decide⟩ panel27MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨27, by decide⟩ r) := by
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
        (panel27BoundedRefinementRange0) panel27BoundedRefinementRange32) panel27BoundedRefinementRange64) panel27BoundedRefinementRange96) panel27BoundedRefinementRange128) panel27BoundedRefinementRange160) panel27BoundedRefinementRange192) panel27BoundedRefinementRange224) panel27BoundedRefinementRange256) panel27BoundedRefinementRange288) panel27BoundedRefinementRange320) panel27BoundedRefinementRange352) panel27BoundedRefinementRange384) panel27BoundedRefinementRange416) panel27BoundedRefinementRange448) panel27BoundedRefinementRange480) panel27BoundedRefinementRange512) panel27BoundedRefinementRange544) panel27BoundedRefinementRange576) r
  simpa only [panel27BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
