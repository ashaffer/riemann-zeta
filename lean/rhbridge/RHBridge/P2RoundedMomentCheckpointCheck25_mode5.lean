import RHBridge.P2RoundedMomentCheckpointData25
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25Mode5MatVecRange0 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel25MomentData.matvecs
            .odd ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel25MomentData.moments
            (P2RoundedFactorCheckpointData.panel25FlatCache.component
              .odd ⟨2, by decide⟩).coeffs).get row)
      0 32 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel25Mode5MatVecRange32 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel25MomentData.matvecs
            .odd ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel25MomentData.moments
            (P2RoundedFactorCheckpointData.panel25FlatCache.component
              .odd ⟨2, by decide⟩).coeffs).get row)
      32 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel25Mode5MatVecRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel25MomentData.matvecs
            .odd ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel25MomentData.moments
            (P2RoundedFactorCheckpointData.panel25FlatCache.component
              .odd ⟨2, by decide⟩).coeffs).get row)
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel25Mode5MatVecRange96 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel25MomentData.matvecs
            .odd ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel25MomentData.moments
            (P2RoundedFactorCheckpointData.panel25FlatCache.component
              .odd ⟨2, by decide⟩).coeffs).get row)
      96 128 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel25Mode5MatVecRange128 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel25MomentData.matvecs
            .odd ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel25MomentData.moments
            (P2RoundedFactorCheckpointData.panel25FlatCache.component
              .odd ⟨2, by decide⟩).coeffs).get row)
      128 149 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

end RHP2Bridge
