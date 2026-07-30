import RHBridge.P2RoundedMomentLengths3
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3BoundedRefinementRange512 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel3BoundedRefinementAt
      512 544 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel3BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
