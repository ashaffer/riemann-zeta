import RHBridge.P2RoundedMomentLengths12
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12BoundedRefinementRange512 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel12BoundedRefinementAt
      512 544 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel12BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
