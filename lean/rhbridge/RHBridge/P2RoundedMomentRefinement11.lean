import RHBridge.P2RoundedMomentCorrect11
import RHBridge.P2RoundedMomentRefinementCheck11_0
import RHBridge.P2RoundedMomentRefinementCheck11_32
import RHBridge.P2RoundedMomentRefinementCheck11_64
import RHBridge.P2RoundedMomentRefinementCheck11_96
import RHBridge.P2RoundedMomentRefinementCheck11_128
import RHBridge.P2RoundedMomentRefinementCheck11_160
import RHBridge.P2RoundedMomentRefinementCheck11_192
import RHBridge.P2RoundedMomentRefinementCheck11_224
import RHBridge.P2RoundedMomentRefinementCheck11_256
import RHBridge.P2RoundedMomentRefinementCheck11_288
import RHBridge.P2RoundedMomentRefinementCheck11_320
import RHBridge.P2RoundedMomentRefinementCheck11_352
import RHBridge.P2RoundedMomentRefinementCheck11_384
import RHBridge.P2RoundedMomentRefinementCheck11_416
import RHBridge.P2RoundedMomentRefinementCheck11_448
import RHBridge.P2RoundedMomentRefinementCheck11_480
import RHBridge.P2RoundedMomentRefinementCheck11_512
import RHBridge.P2RoundedMomentRefinementCheck11_544
import RHBridge.P2RoundedMomentRefinementCheck11_576

namespace RHP2Bridge

theorem panel11BoundedRefinements :
    ∀ r : Fin 600,
      (P2RoundedBoundedTriple.boundedMomentPanelBall
        P2RoundedFactorCheckpointData.panel11MomentData
        P2RoundedFactorCheckpointData.panel11FlatCache
        ⟨11, by decide⟩ panel11MomentData_correct r).Refines
          (P2RoundedPanelRefinement.coarsePanelBall
            ⟨11, by decide⟩ r) := by
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
        (panel11BoundedRefinementRange0) panel11BoundedRefinementRange32) panel11BoundedRefinementRange64) panel11BoundedRefinementRange96) panel11BoundedRefinementRange128) panel11BoundedRefinementRange160) panel11BoundedRefinementRange192) panel11BoundedRefinementRange224) panel11BoundedRefinementRange256) panel11BoundedRefinementRange288) panel11BoundedRefinementRange320) panel11BoundedRefinementRange352) panel11BoundedRefinementRange384) panel11BoundedRefinementRange416) panel11BoundedRefinementRange448) panel11BoundedRefinementRange480) panel11BoundedRefinementRange512) panel11BoundedRefinementRange544) panel11BoundedRefinementRange576) r
  simpa only [panel11BoundedRefinementAt,
    P2RoundedBoundedTriple.boundedMomentPanelBall] using hraw

end RHP2Bridge
