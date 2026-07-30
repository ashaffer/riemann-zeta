import RHBridge.P2RoundedMomentLengths4
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4BoundedRefinementRange288 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel4BoundedRefinementAt
      288 320 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel4BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
