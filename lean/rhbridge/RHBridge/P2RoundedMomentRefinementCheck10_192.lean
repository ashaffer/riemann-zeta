import RHBridge.P2RoundedMomentLengths10
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10BoundedRefinementRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel10BoundedRefinementAt
      192 224 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel10BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
