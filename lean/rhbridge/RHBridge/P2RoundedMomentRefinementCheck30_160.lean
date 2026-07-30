import RHBridge.P2RoundedMomentLengths30
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30BoundedRefinementRange160 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel30BoundedRefinementAt
      160 192 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel30BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
