import RHBridge.P2RoundedMomentLengths31
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31BoundedRefinementRange448 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel31BoundedRefinementAt
      448 480 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel31BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
