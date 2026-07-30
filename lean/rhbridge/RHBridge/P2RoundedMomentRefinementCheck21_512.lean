import RHBridge.P2RoundedMomentLengths21
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21BoundedRefinementRange512 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel21BoundedRefinementAt
      512 544 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel21BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
