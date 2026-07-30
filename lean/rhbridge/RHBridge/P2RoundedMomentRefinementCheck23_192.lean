import RHBridge.P2RoundedMomentLengths23
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23BoundedRefinementRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel23BoundedRefinementAt
      192 224 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel23BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
