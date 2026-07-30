import RHBridge.P2RoundedMomentCheckpointData3
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3DefectMomentRange0 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel3MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs)
      0 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel3DefectMomentRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel3MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs)
      64 128 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel3DefectMomentRange128 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel3MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs)
      128 192 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel3DefectMomentRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel3MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs)
      192 256 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel3DefectMomentRange256 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel3MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs)
      256 297 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

end RHP2Bridge
