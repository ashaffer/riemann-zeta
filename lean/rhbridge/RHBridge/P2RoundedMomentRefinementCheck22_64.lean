import RHBridge.P2RoundedMomentLengths22
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22BoundedRefinementRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      panel22BoundedRefinementAt
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
    panel22BoundedRefinementAt
    P2RoundedSharedEvaluator.QBall.Refines
  decide +kernel

end RHP2Bridge
