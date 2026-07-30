import RHBridge.P2RoundedMomentLengths0
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0BoundedRefinementRange512 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel0BoundedRefinementAt
      512 544 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel0BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
