import RHBridge.P2RoundedMomentLengths27
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27BoundedRefinementRange256 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel27BoundedRefinementAt
      256 288 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel27BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
