import RHBridge.P2RoundedMomentLengths26
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26BoundedRefinementRange352 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel26BoundedRefinementAt
      352 384 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel26BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
