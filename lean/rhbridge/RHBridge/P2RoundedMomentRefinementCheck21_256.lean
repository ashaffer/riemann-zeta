import RHBridge.P2RoundedMomentLengths21
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21BoundedRefinementRange256 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel21BoundedRefinementAt
      256 288 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel21BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
