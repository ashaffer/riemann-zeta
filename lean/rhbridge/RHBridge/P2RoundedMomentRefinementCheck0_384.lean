import RHBridge.P2RoundedMomentLengths0
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0BoundedRefinementRange384 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel0BoundedRefinementAt
      384 416 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel0BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
