import RHBridge.P2RoundedMomentLengths22
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22BoundedRefinementRange512 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel22BoundedRefinementAt
      512 544 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel22BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
