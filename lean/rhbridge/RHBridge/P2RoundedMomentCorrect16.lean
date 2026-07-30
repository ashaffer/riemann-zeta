import RHBridge.P2RoundedFlatFactorCheckpoint16
import RHBridge.P2RoundedMomentLengths16
import RHBridge.P2RoundedMomentCheckpointCheck16_moments
import RHBridge.P2RoundedMomentCheckpointCheck16_mode0
import RHBridge.P2RoundedMomentCheckpointCheck16_mode1
import RHBridge.P2RoundedMomentCheckpointCheck16_mode2
import RHBridge.P2RoundedMomentCheckpointCheck16_mode3
import RHBridge.P2RoundedMomentCheckpointCheck16_mode4
import RHBridge.P2RoundedMomentCheckpointCheck16_mode5
import RHBridge.P2RoundedMomentCheckpointCheck16_mode6
import RHBridge.P2RoundedMomentCheckpointCheck16_mode7
import RHBridge.P2RoundedMomentCheckpointCheck16_mode8
import RHBridge.P2RoundedMomentCheckpointCheck16_mode9
import RHBridge.P2RoundedMomentCheckpointCheck16_mode10
import RHBridge.P2RoundedMomentCheckpointCheck16_mode11
import RHBridge.P2RoundedMomentCheckpointCheck16_mode12
import RHBridge.P2RoundedMomentCheckpointCheck16_mode13
import RHBridge.P2RoundedMomentCheckpointCheck16_mode14
import RHBridge.P2RoundedMomentCheckpointCheck16_mode15
import RHBridge.P2RoundedMomentCheckpointCheck16_mode16
import RHBridge.P2RoundedMomentCheckpointCheck16_mode17
import RHBridge.P2RoundedMomentCheckpointCheck16_mode18
import RHBridge.P2RoundedMomentCheckpointCheck16_mode19
import RHBridge.P2RoundedMomentCheckpointCheck16_mode20
import RHBridge.P2RoundedMomentCheckpointCheck16_mode21
import RHBridge.P2RoundedMomentCheckpointCheck16_mode22
import RHBridge.P2RoundedMomentCheckpointCheck16_mode23
import RHBridge.P2RoundedMomentCheckpointCheck16_mode24
import RHBridge.P2RoundedMomentCheckpointCheck16_mode25
import RHBridge.P2RoundedMomentCheckpointCheck16_mode26
import RHBridge.P2RoundedMomentCheckpointCheck16_mode27
import RHBridge.P2RoundedMomentCheckpointCheck16_mode28
import RHBridge.P2RoundedMomentCheckpointCheck16_mode29
import RHBridge.P2RoundedMomentCheckpointCheck16_mode30
import RHBridge.P2RoundedMomentCheckpointCheck16_mode31
import RHBridge.P2RoundedMomentCheckpointCheck16_mode32
import RHBridge.P2RoundedMomentCheckpointCheck16_mode33
import RHBridge.P2RoundedMomentCheckpointCheck16_mode34
import RHBridge.P2RoundedMomentCheckpointCheck16_mode35
import RHBridge.P2RoundedMomentCheckpointCheck16_mode36
import RHBridge.P2RoundedMomentCheckpointCheck16_mode37
import RHBridge.P2RoundedMomentCheckpointCheck16_mode38
import RHBridge.P2RoundedMomentCheckpointCheck16_mode39
import RHBridge.P2RoundedMomentCheckpointCheck16_mode40
import RHBridge.P2RoundedMomentCheckpointCheck16_mode41
import RHBridge.P2RoundedMomentCheckpointCheck16_mode42
import RHBridge.P2RoundedMomentCheckpointCheck16_mode43
import RHBridge.P2RoundedMomentCheckpointCheck16_mode44
import RHBridge.P2RoundedMomentCheckpointCheck16_mode45
import RHBridge.P2RoundedMomentCheckpointCheck16_mode46
import RHBridge.P2RoundedMomentCheckpointCheck16_mode47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedMomentRefinement

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

private theorem vector_ext_fin
    {α : Type} {n : Nat} {v w : Vector α n}
    (h : ∀ i : Fin n, v.get i = w.get i) : v = w := by
  apply Vector.ext
  intro i hi
  exact h ⟨i, hi⟩

theorem panel16DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel16FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16DefectMomentRange0) panel16DefectMomentRange64) panel16DefectMomentRange128) panel16DefectMomentRange192) panel16DefectMomentRange256) row

theorem panel16Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode0MatVecRange0) panel16Mode0MatVecRange32) panel16Mode0MatVecRange64) panel16Mode0MatVecRange96) panel16Mode0MatVecRange128) row

theorem panel16Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode1MatVecRange0) panel16Mode1MatVecRange32) panel16Mode1MatVecRange64) panel16Mode1MatVecRange96) panel16Mode1MatVecRange128) row

theorem panel16Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode2MatVecRange0) panel16Mode2MatVecRange32) panel16Mode2MatVecRange64) panel16Mode2MatVecRange96) panel16Mode2MatVecRange128) row

theorem panel16Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode3MatVecRange0) panel16Mode3MatVecRange32) panel16Mode3MatVecRange64) panel16Mode3MatVecRange96) panel16Mode3MatVecRange128) row

theorem panel16Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode4MatVecRange0) panel16Mode4MatVecRange32) panel16Mode4MatVecRange64) panel16Mode4MatVecRange96) panel16Mode4MatVecRange128) row

theorem panel16Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode5MatVecRange0) panel16Mode5MatVecRange32) panel16Mode5MatVecRange64) panel16Mode5MatVecRange96) panel16Mode5MatVecRange128) row

theorem panel16Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode6MatVecRange0) panel16Mode6MatVecRange32) panel16Mode6MatVecRange64) panel16Mode6MatVecRange96) panel16Mode6MatVecRange128) row

theorem panel16Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode7MatVecRange0) panel16Mode7MatVecRange32) panel16Mode7MatVecRange64) panel16Mode7MatVecRange96) panel16Mode7MatVecRange128) row

theorem panel16Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode8MatVecRange0) panel16Mode8MatVecRange32) panel16Mode8MatVecRange64) panel16Mode8MatVecRange96) panel16Mode8MatVecRange128) row

theorem panel16Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode9MatVecRange0) panel16Mode9MatVecRange32) panel16Mode9MatVecRange64) panel16Mode9MatVecRange96) panel16Mode9MatVecRange128) row

theorem panel16Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode10MatVecRange0) panel16Mode10MatVecRange32) panel16Mode10MatVecRange64) panel16Mode10MatVecRange96) panel16Mode10MatVecRange128) row

theorem panel16Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode11MatVecRange0) panel16Mode11MatVecRange32) panel16Mode11MatVecRange64) panel16Mode11MatVecRange96) panel16Mode11MatVecRange128) row

theorem panel16Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode12MatVecRange0) panel16Mode12MatVecRange32) panel16Mode12MatVecRange64) panel16Mode12MatVecRange96) panel16Mode12MatVecRange128) row

theorem panel16Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode13MatVecRange0) panel16Mode13MatVecRange32) panel16Mode13MatVecRange64) panel16Mode13MatVecRange96) panel16Mode13MatVecRange128) row

theorem panel16Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode14MatVecRange0) panel16Mode14MatVecRange32) panel16Mode14MatVecRange64) panel16Mode14MatVecRange96) panel16Mode14MatVecRange128) row

theorem panel16Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode15MatVecRange0) panel16Mode15MatVecRange32) panel16Mode15MatVecRange64) panel16Mode15MatVecRange96) panel16Mode15MatVecRange128) row

theorem panel16Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode16MatVecRange0) panel16Mode16MatVecRange32) panel16Mode16MatVecRange64) panel16Mode16MatVecRange96) panel16Mode16MatVecRange128) row

theorem panel16Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode17MatVecRange0) panel16Mode17MatVecRange32) panel16Mode17MatVecRange64) panel16Mode17MatVecRange96) panel16Mode17MatVecRange128) row

theorem panel16Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode18MatVecRange0) panel16Mode18MatVecRange32) panel16Mode18MatVecRange64) panel16Mode18MatVecRange96) panel16Mode18MatVecRange128) row

theorem panel16Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode19MatVecRange0) panel16Mode19MatVecRange32) panel16Mode19MatVecRange64) panel16Mode19MatVecRange96) panel16Mode19MatVecRange128) row

theorem panel16Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode20MatVecRange0) panel16Mode20MatVecRange32) panel16Mode20MatVecRange64) panel16Mode20MatVecRange96) panel16Mode20MatVecRange128) row

theorem panel16Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode21MatVecRange0) panel16Mode21MatVecRange32) panel16Mode21MatVecRange64) panel16Mode21MatVecRange96) panel16Mode21MatVecRange128) row

theorem panel16Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode22MatVecRange0) panel16Mode22MatVecRange32) panel16Mode22MatVecRange64) panel16Mode22MatVecRange96) panel16Mode22MatVecRange128) row

theorem panel16Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode23MatVecRange0) panel16Mode23MatVecRange32) panel16Mode23MatVecRange64) panel16Mode23MatVecRange96) panel16Mode23MatVecRange128) row

theorem panel16Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode24MatVecRange0) panel16Mode24MatVecRange32) panel16Mode24MatVecRange64) panel16Mode24MatVecRange96) panel16Mode24MatVecRange128) row

theorem panel16Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode25MatVecRange0) panel16Mode25MatVecRange32) panel16Mode25MatVecRange64) panel16Mode25MatVecRange96) panel16Mode25MatVecRange128) row

theorem panel16Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode26MatVecRange0) panel16Mode26MatVecRange32) panel16Mode26MatVecRange64) panel16Mode26MatVecRange96) panel16Mode26MatVecRange128) row

theorem panel16Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode27MatVecRange0) panel16Mode27MatVecRange32) panel16Mode27MatVecRange64) panel16Mode27MatVecRange96) panel16Mode27MatVecRange128) row

theorem panel16Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode28MatVecRange0) panel16Mode28MatVecRange32) panel16Mode28MatVecRange64) panel16Mode28MatVecRange96) panel16Mode28MatVecRange128) row

theorem panel16Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode29MatVecRange0) panel16Mode29MatVecRange32) panel16Mode29MatVecRange64) panel16Mode29MatVecRange96) panel16Mode29MatVecRange128) row

theorem panel16Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode30MatVecRange0) panel16Mode30MatVecRange32) panel16Mode30MatVecRange64) panel16Mode30MatVecRange96) panel16Mode30MatVecRange128) row

theorem panel16Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode31MatVecRange0) panel16Mode31MatVecRange32) panel16Mode31MatVecRange64) panel16Mode31MatVecRange96) panel16Mode31MatVecRange128) row

theorem panel16Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode32MatVecRange0) panel16Mode32MatVecRange32) panel16Mode32MatVecRange64) panel16Mode32MatVecRange96) panel16Mode32MatVecRange128) row

theorem panel16Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode33MatVecRange0) panel16Mode33MatVecRange32) panel16Mode33MatVecRange64) panel16Mode33MatVecRange96) panel16Mode33MatVecRange128) row

theorem panel16Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode34MatVecRange0) panel16Mode34MatVecRange32) panel16Mode34MatVecRange64) panel16Mode34MatVecRange96) panel16Mode34MatVecRange128) row

theorem panel16Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode35MatVecRange0) panel16Mode35MatVecRange32) panel16Mode35MatVecRange64) panel16Mode35MatVecRange96) panel16Mode35MatVecRange128) row

theorem panel16Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode36MatVecRange0) panel16Mode36MatVecRange32) panel16Mode36MatVecRange64) panel16Mode36MatVecRange96) panel16Mode36MatVecRange128) row

theorem panel16Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode37MatVecRange0) panel16Mode37MatVecRange32) panel16Mode37MatVecRange64) panel16Mode37MatVecRange96) panel16Mode37MatVecRange128) row

theorem panel16Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode38MatVecRange0) panel16Mode38MatVecRange32) panel16Mode38MatVecRange64) panel16Mode38MatVecRange96) panel16Mode38MatVecRange128) row

theorem panel16Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode39MatVecRange0) panel16Mode39MatVecRange32) panel16Mode39MatVecRange64) panel16Mode39MatVecRange96) panel16Mode39MatVecRange128) row

theorem panel16Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode40MatVecRange0) panel16Mode40MatVecRange32) panel16Mode40MatVecRange64) panel16Mode40MatVecRange96) panel16Mode40MatVecRange128) row

theorem panel16Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode41MatVecRange0) panel16Mode41MatVecRange32) panel16Mode41MatVecRange64) panel16Mode41MatVecRange96) panel16Mode41MatVecRange128) row

theorem panel16Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode42MatVecRange0) panel16Mode42MatVecRange32) panel16Mode42MatVecRange64) panel16Mode42MatVecRange96) panel16Mode42MatVecRange128) row

theorem panel16Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode43MatVecRange0) panel16Mode43MatVecRange32) panel16Mode43MatVecRange64) panel16Mode43MatVecRange96) panel16Mode43MatVecRange128) row

theorem panel16Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode44MatVecRange0) panel16Mode44MatVecRange32) panel16Mode44MatVecRange64) panel16Mode44MatVecRange96) panel16Mode44MatVecRange128) row

theorem panel16Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode45MatVecRange0) panel16Mode45MatVecRange32) panel16Mode45MatVecRange64) panel16Mode45MatVecRange96) panel16Mode45MatVecRange128) row

theorem panel16Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode46MatVecRange0) panel16Mode46MatVecRange32) panel16Mode46MatVecRange64) panel16Mode46MatVecRange96) panel16Mode46MatVecRange128) row

theorem panel16Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel16MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel16MomentData.moments
        (P2RoundedFactorCheckpointData.panel16FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel16Mode47MatVecRange0) panel16Mode47MatVecRange32) panel16Mode47MatVecRange64) panel16Mode47MatVecRange96) panel16Mode47MatVecRange128) row

theorem panel16MomentData_correct :
    P2RoundedFactorCheckpointData.panel16MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel16FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel16DefectMoments_eq panel16ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel16Mode0MatVec_eq
      · exact panel16Mode2MatVec_eq
      · exact panel16Mode4MatVec_eq
      · exact panel16Mode6MatVec_eq
      · exact panel16Mode8MatVec_eq
      · exact panel16Mode10MatVec_eq
      · exact panel16Mode12MatVec_eq
      · exact panel16Mode14MatVec_eq
      · exact panel16Mode16MatVec_eq
      · exact panel16Mode18MatVec_eq
      · exact panel16Mode20MatVec_eq
      · exact panel16Mode22MatVec_eq
      · exact panel16Mode24MatVec_eq
      · exact panel16Mode26MatVec_eq
      · exact panel16Mode28MatVec_eq
      · exact panel16Mode30MatVec_eq
      · exact panel16Mode32MatVec_eq
      · exact panel16Mode34MatVec_eq
      · exact panel16Mode36MatVec_eq
      · exact panel16Mode38MatVec_eq
      · exact panel16Mode40MatVec_eq
      · exact panel16Mode42MatVec_eq
      · exact panel16Mode44MatVec_eq
      · exact panel16Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel16Mode1MatVec_eq
      · exact panel16Mode3MatVec_eq
      · exact panel16Mode5MatVec_eq
      · exact panel16Mode7MatVec_eq
      · exact panel16Mode9MatVec_eq
      · exact panel16Mode11MatVec_eq
      · exact panel16Mode13MatVec_eq
      · exact panel16Mode15MatVec_eq
      · exact panel16Mode17MatVec_eq
      · exact panel16Mode19MatVec_eq
      · exact panel16Mode21MatVec_eq
      · exact panel16Mode23MatVec_eq
      · exact panel16Mode25MatVec_eq
      · exact panel16Mode27MatVec_eq
      · exact panel16Mode29MatVec_eq
      · exact panel16Mode31MatVec_eq
      · exact panel16Mode33MatVec_eq
      · exact panel16Mode35MatVec_eq
      · exact panel16Mode37MatVec_eq
      · exact panel16Mode39MatVec_eq
      · exact panel16Mode41MatVec_eq
      · exact panel16Mode43MatVec_eq
      · exact panel16Mode45MatVec_eq
      · exact panel16Mode47MatVec_eq

end RHP2Bridge
