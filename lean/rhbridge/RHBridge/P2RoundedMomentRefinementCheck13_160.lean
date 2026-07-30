import RHBridge.P2RoundedMomentLengths13
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13BoundedRefinementRange160 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel13BoundedRefinementAt
      160 192 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel13BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
