import RHBridge.P2RoundedMomentCheckpointData16
import RHBridge.P2RoundedGeneratedCertificate

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16Mode4MatVecRange0 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel16MomentData.matvecs
            .even ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel16MomentData.moments
            (P2RoundedFactorCheckpointData.panel16FlatCache.component
              .even ⟨2, by decide⟩).coeffs).get row)
      0 32 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel16Mode4MatVecRange32 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel16MomentData.matvecs
            .even ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel16MomentData.moments
            (P2RoundedFactorCheckpointData.panel16FlatCache.component
              .even ⟨2, by decide⟩).coeffs).get row)
      32 64 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel16Mode4MatVecRange64 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel16MomentData.matvecs
            .even ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel16MomentData.moments
            (P2RoundedFactorCheckpointData.panel16FlatCache.component
              .even ⟨2, by decide⟩).coeffs).get row)
      64 96 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel16Mode4MatVecRange96 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel16MomentData.matvecs
            .even ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel16MomentData.moments
            (P2RoundedFactorCheckpointData.panel16FlatCache.component
              .even ⟨2, by decide⟩).coeffs).get row)
      96 128 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

theorem panel16Mode4MatVecRange128 :
    P2RoundedGeneratedCertificate.FinRangeAll
      (fun row : Fin 149 =>
        (P2RoundedFactorCheckpointData.panel16MomentData.matvecs
            .even ⟨2, by decide⟩).get row =
          (P2RoundedTripleMoment.hankelMatVecFromMoments
            P2RoundedFactorCheckpointData.panel16MomentData.moments
            (P2RoundedFactorCheckpointData.panel16FlatCache.component
              .even ⟨2, by decide⟩).coeffs).get row)
      128 149 := by
  unfold P2RoundedGeneratedCertificate.FinRangeAll
  decide +kernel

end RHP2Bridge
