import RHBridge.P2RoundedMomentLengths15
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15BoundedRefinementRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel15BoundedRefinementAt
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel15BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
