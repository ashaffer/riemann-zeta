import RHBridge.P2RoundedMomentLengths19
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19BoundedRefinementRange576 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel19BoundedRefinementAt
      576 600 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel19BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
