import RHBridge.P2RoundedMomentLengths20
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20BoundedRefinementRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel20BoundedRefinementAt
      192 224 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel20BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
