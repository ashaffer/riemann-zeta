import RHBridge.P2RoundedMomentLengths14
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14BoundedRefinementRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel14BoundedRefinementAt
      192 224 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel14BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
