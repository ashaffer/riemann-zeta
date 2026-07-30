import RHBridge.P2RoundedMomentLengths9
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9BoundedRefinementRange544 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel9BoundedRefinementAt
      544 576 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel9BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
