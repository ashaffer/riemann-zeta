import RHBridge.P2RoundedMomentCheckpointData2
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2Mode2MatVecRange0 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel2MomentData.matvecs
            .even ⟨1, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel2MomentData.moments
            (P2RoundedFactorCheckpointData.panel2FlatCache.component
              .even ⟨1, by decide⟩).coeffs).get row)
      0 32 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel2Mode2MatVecRange32 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel2MomentData.matvecs
            .even ⟨1, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel2MomentData.moments
            (P2RoundedFactorCheckpointData.panel2FlatCache.component
              .even ⟨1, by decide⟩).coeffs).get row)
      32 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel2Mode2MatVecRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel2MomentData.matvecs
            .even ⟨1, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel2MomentData.moments
            (P2RoundedFactorCheckpointData.panel2FlatCache.component
              .even ⟨1, by decide⟩).coeffs).get row)
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel2Mode2MatVecRange96 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel2MomentData.matvecs
            .even ⟨1, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel2MomentData.moments
            (P2RoundedFactorCheckpointData.panel2FlatCache.component
              .even ⟨1, by decide⟩).coeffs).get row)
      96 128 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel2Mode2MatVecRange128 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel2MomentData.matvecs
            .even ⟨1, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel2MomentData.moments
            (P2RoundedFactorCheckpointData.panel2FlatCache.component
              .even ⟨1, by decide⟩).coeffs).get row)
      128 149 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

end RHP2Bridge
