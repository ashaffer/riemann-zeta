import RHBridge.P2RoundedMomentCheckpointData29
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29DefectMomentRange0 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel29MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs)
      0 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel29DefectMomentRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel29MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs)
      64 128 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel29DefectMomentRange128 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel29MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs)
      128 192 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel29DefectMomentRange192 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel29MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs)
      192 256 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel29DefectMomentRange256 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 297 =>
        (P2RoundedFactorCheckpointData.panel29MomentData.moments).get row =
          P2RoundedTripleMoment.momentDot row.val
            P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs)
      256 297 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

end RHP2Bridge
