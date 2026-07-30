import RHBridge.P2RoundedMomentLengths28
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28BoundedRefinementRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel28BoundedRefinementAt
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel28BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
