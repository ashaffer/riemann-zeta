import RHBridge.P2RoundedMomentLengths11
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11BoundedRefinementRange576 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel11BoundedRefinementAt
      576 600 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel11BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
