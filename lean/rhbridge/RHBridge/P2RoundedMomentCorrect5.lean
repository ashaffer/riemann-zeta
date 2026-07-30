import RHBridge.P2RoundedFlatFactorCheckpoint5
import RHBridge.P2RoundedMomentLengths5
import RHBridge.P2RoundedMomentCheckpointCheck5_moments
import RHBridge.P2RoundedMomentCheckpointCheck5_mode0
import RHBridge.P2RoundedMomentCheckpointCheck5_mode1
import RHBridge.P2RoundedMomentCheckpointCheck5_mode2
import RHBridge.P2RoundedMomentCheckpointCheck5_mode3
import RHBridge.P2RoundedMomentCheckpointCheck5_mode4
import RHBridge.P2RoundedMomentCheckpointCheck5_mode5
import RHBridge.P2RoundedMomentCheckpointCheck5_mode6
import RHBridge.P2RoundedMomentCheckpointCheck5_mode7
import RHBridge.P2RoundedMomentCheckpointCheck5_mode8
import RHBridge.P2RoundedMomentCheckpointCheck5_mode9
import RHBridge.P2RoundedMomentCheckpointCheck5_mode10
import RHBridge.P2RoundedMomentCheckpointCheck5_mode11
import RHBridge.P2RoundedMomentCheckpointCheck5_mode12
import RHBridge.P2RoundedMomentCheckpointCheck5_mode13
import RHBridge.P2RoundedMomentCheckpointCheck5_mode14
import RHBridge.P2RoundedMomentCheckpointCheck5_mode15
import RHBridge.P2RoundedMomentCheckpointCheck5_mode16
import RHBridge.P2RoundedMomentCheckpointCheck5_mode17
import RHBridge.P2RoundedMomentCheckpointCheck5_mode18
import RHBridge.P2RoundedMomentCheckpointCheck5_mode19
import RHBridge.P2RoundedMomentCheckpointCheck5_mode20
import RHBridge.P2RoundedMomentCheckpointCheck5_mode21
import RHBridge.P2RoundedMomentCheckpointCheck5_mode22
import RHBridge.P2RoundedMomentCheckpointCheck5_mode23
import RHBridge.P2RoundedMomentCheckpointCheck5_mode24
import RHBridge.P2RoundedMomentCheckpointCheck5_mode25
import RHBridge.P2RoundedMomentCheckpointCheck5_mode26
import RHBridge.P2RoundedMomentCheckpointCheck5_mode27
import RHBridge.P2RoundedMomentCheckpointCheck5_mode28
import RHBridge.P2RoundedMomentCheckpointCheck5_mode29
import RHBridge.P2RoundedMomentCheckpointCheck5_mode30
import RHBridge.P2RoundedMomentCheckpointCheck5_mode31
import RHBridge.P2RoundedMomentCheckpointCheck5_mode32
import RHBridge.P2RoundedMomentCheckpointCheck5_mode33
import RHBridge.P2RoundedMomentCheckpointCheck5_mode34
import RHBridge.P2RoundedMomentCheckpointCheck5_mode35
import RHBridge.P2RoundedMomentCheckpointCheck5_mode36
import RHBridge.P2RoundedMomentCheckpointCheck5_mode37
import RHBridge.P2RoundedMomentCheckpointCheck5_mode38
import RHBridge.P2RoundedMomentCheckpointCheck5_mode39
import RHBridge.P2RoundedMomentCheckpointCheck5_mode40
import RHBridge.P2RoundedMomentCheckpointCheck5_mode41
import RHBridge.P2RoundedMomentCheckpointCheck5_mode42
import RHBridge.P2RoundedMomentCheckpointCheck5_mode43
import RHBridge.P2RoundedMomentCheckpointCheck5_mode44
import RHBridge.P2RoundedMomentCheckpointCheck5_mode45
import RHBridge.P2RoundedMomentCheckpointCheck5_mode46
import RHBridge.P2RoundedMomentCheckpointCheck5_mode47

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

theorem panel5DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel5FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5DefectMomentRange0) panel5DefectMomentRange64) panel5DefectMomentRange128) panel5DefectMomentRange192) panel5DefectMomentRange256) row

theorem panel5Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode0MatVecRange0) panel5Mode0MatVecRange32) panel5Mode0MatVecRange64) panel5Mode0MatVecRange96) panel5Mode0MatVecRange128) row

theorem panel5Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode1MatVecRange0) panel5Mode1MatVecRange32) panel5Mode1MatVecRange64) panel5Mode1MatVecRange96) panel5Mode1MatVecRange128) row

theorem panel5Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode2MatVecRange0) panel5Mode2MatVecRange32) panel5Mode2MatVecRange64) panel5Mode2MatVecRange96) panel5Mode2MatVecRange128) row

theorem panel5Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode3MatVecRange0) panel5Mode3MatVecRange32) panel5Mode3MatVecRange64) panel5Mode3MatVecRange96) panel5Mode3MatVecRange128) row

theorem panel5Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode4MatVecRange0) panel5Mode4MatVecRange32) panel5Mode4MatVecRange64) panel5Mode4MatVecRange96) panel5Mode4MatVecRange128) row

theorem panel5Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode5MatVecRange0) panel5Mode5MatVecRange32) panel5Mode5MatVecRange64) panel5Mode5MatVecRange96) panel5Mode5MatVecRange128) row

theorem panel5Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode6MatVecRange0) panel5Mode6MatVecRange32) panel5Mode6MatVecRange64) panel5Mode6MatVecRange96) panel5Mode6MatVecRange128) row

theorem panel5Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode7MatVecRange0) panel5Mode7MatVecRange32) panel5Mode7MatVecRange64) panel5Mode7MatVecRange96) panel5Mode7MatVecRange128) row

theorem panel5Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode8MatVecRange0) panel5Mode8MatVecRange32) panel5Mode8MatVecRange64) panel5Mode8MatVecRange96) panel5Mode8MatVecRange128) row

theorem panel5Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode9MatVecRange0) panel5Mode9MatVecRange32) panel5Mode9MatVecRange64) panel5Mode9MatVecRange96) panel5Mode9MatVecRange128) row

theorem panel5Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode10MatVecRange0) panel5Mode10MatVecRange32) panel5Mode10MatVecRange64) panel5Mode10MatVecRange96) panel5Mode10MatVecRange128) row

theorem panel5Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode11MatVecRange0) panel5Mode11MatVecRange32) panel5Mode11MatVecRange64) panel5Mode11MatVecRange96) panel5Mode11MatVecRange128) row

theorem panel5Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode12MatVecRange0) panel5Mode12MatVecRange32) panel5Mode12MatVecRange64) panel5Mode12MatVecRange96) panel5Mode12MatVecRange128) row

theorem panel5Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode13MatVecRange0) panel5Mode13MatVecRange32) panel5Mode13MatVecRange64) panel5Mode13MatVecRange96) panel5Mode13MatVecRange128) row

theorem panel5Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode14MatVecRange0) panel5Mode14MatVecRange32) panel5Mode14MatVecRange64) panel5Mode14MatVecRange96) panel5Mode14MatVecRange128) row

theorem panel5Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode15MatVecRange0) panel5Mode15MatVecRange32) panel5Mode15MatVecRange64) panel5Mode15MatVecRange96) panel5Mode15MatVecRange128) row

theorem panel5Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode16MatVecRange0) panel5Mode16MatVecRange32) panel5Mode16MatVecRange64) panel5Mode16MatVecRange96) panel5Mode16MatVecRange128) row

theorem panel5Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode17MatVecRange0) panel5Mode17MatVecRange32) panel5Mode17MatVecRange64) panel5Mode17MatVecRange96) panel5Mode17MatVecRange128) row

theorem panel5Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode18MatVecRange0) panel5Mode18MatVecRange32) panel5Mode18MatVecRange64) panel5Mode18MatVecRange96) panel5Mode18MatVecRange128) row

theorem panel5Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode19MatVecRange0) panel5Mode19MatVecRange32) panel5Mode19MatVecRange64) panel5Mode19MatVecRange96) panel5Mode19MatVecRange128) row

theorem panel5Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode20MatVecRange0) panel5Mode20MatVecRange32) panel5Mode20MatVecRange64) panel5Mode20MatVecRange96) panel5Mode20MatVecRange128) row

theorem panel5Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode21MatVecRange0) panel5Mode21MatVecRange32) panel5Mode21MatVecRange64) panel5Mode21MatVecRange96) panel5Mode21MatVecRange128) row

theorem panel5Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode22MatVecRange0) panel5Mode22MatVecRange32) panel5Mode22MatVecRange64) panel5Mode22MatVecRange96) panel5Mode22MatVecRange128) row

theorem panel5Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode23MatVecRange0) panel5Mode23MatVecRange32) panel5Mode23MatVecRange64) panel5Mode23MatVecRange96) panel5Mode23MatVecRange128) row

theorem panel5Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode24MatVecRange0) panel5Mode24MatVecRange32) panel5Mode24MatVecRange64) panel5Mode24MatVecRange96) panel5Mode24MatVecRange128) row

theorem panel5Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode25MatVecRange0) panel5Mode25MatVecRange32) panel5Mode25MatVecRange64) panel5Mode25MatVecRange96) panel5Mode25MatVecRange128) row

theorem panel5Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode26MatVecRange0) panel5Mode26MatVecRange32) panel5Mode26MatVecRange64) panel5Mode26MatVecRange96) panel5Mode26MatVecRange128) row

theorem panel5Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode27MatVecRange0) panel5Mode27MatVecRange32) panel5Mode27MatVecRange64) panel5Mode27MatVecRange96) panel5Mode27MatVecRange128) row

theorem panel5Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode28MatVecRange0) panel5Mode28MatVecRange32) panel5Mode28MatVecRange64) panel5Mode28MatVecRange96) panel5Mode28MatVecRange128) row

theorem panel5Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode29MatVecRange0) panel5Mode29MatVecRange32) panel5Mode29MatVecRange64) panel5Mode29MatVecRange96) panel5Mode29MatVecRange128) row

theorem panel5Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode30MatVecRange0) panel5Mode30MatVecRange32) panel5Mode30MatVecRange64) panel5Mode30MatVecRange96) panel5Mode30MatVecRange128) row

theorem panel5Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode31MatVecRange0) panel5Mode31MatVecRange32) panel5Mode31MatVecRange64) panel5Mode31MatVecRange96) panel5Mode31MatVecRange128) row

theorem panel5Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode32MatVecRange0) panel5Mode32MatVecRange32) panel5Mode32MatVecRange64) panel5Mode32MatVecRange96) panel5Mode32MatVecRange128) row

theorem panel5Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode33MatVecRange0) panel5Mode33MatVecRange32) panel5Mode33MatVecRange64) panel5Mode33MatVecRange96) panel5Mode33MatVecRange128) row

theorem panel5Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode34MatVecRange0) panel5Mode34MatVecRange32) panel5Mode34MatVecRange64) panel5Mode34MatVecRange96) panel5Mode34MatVecRange128) row

theorem panel5Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode35MatVecRange0) panel5Mode35MatVecRange32) panel5Mode35MatVecRange64) panel5Mode35MatVecRange96) panel5Mode35MatVecRange128) row

theorem panel5Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode36MatVecRange0) panel5Mode36MatVecRange32) panel5Mode36MatVecRange64) panel5Mode36MatVecRange96) panel5Mode36MatVecRange128) row

theorem panel5Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode37MatVecRange0) panel5Mode37MatVecRange32) panel5Mode37MatVecRange64) panel5Mode37MatVecRange96) panel5Mode37MatVecRange128) row

theorem panel5Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode38MatVecRange0) panel5Mode38MatVecRange32) panel5Mode38MatVecRange64) panel5Mode38MatVecRange96) panel5Mode38MatVecRange128) row

theorem panel5Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode39MatVecRange0) panel5Mode39MatVecRange32) panel5Mode39MatVecRange64) panel5Mode39MatVecRange96) panel5Mode39MatVecRange128) row

theorem panel5Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode40MatVecRange0) panel5Mode40MatVecRange32) panel5Mode40MatVecRange64) panel5Mode40MatVecRange96) panel5Mode40MatVecRange128) row

theorem panel5Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode41MatVecRange0) panel5Mode41MatVecRange32) panel5Mode41MatVecRange64) panel5Mode41MatVecRange96) panel5Mode41MatVecRange128) row

theorem panel5Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode42MatVecRange0) panel5Mode42MatVecRange32) panel5Mode42MatVecRange64) panel5Mode42MatVecRange96) panel5Mode42MatVecRange128) row

theorem panel5Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode43MatVecRange0) panel5Mode43MatVecRange32) panel5Mode43MatVecRange64) panel5Mode43MatVecRange96) panel5Mode43MatVecRange128) row

theorem panel5Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode44MatVecRange0) panel5Mode44MatVecRange32) panel5Mode44MatVecRange64) panel5Mode44MatVecRange96) panel5Mode44MatVecRange128) row

theorem panel5Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode45MatVecRange0) panel5Mode45MatVecRange32) panel5Mode45MatVecRange64) panel5Mode45MatVecRange96) panel5Mode45MatVecRange128) row

theorem panel5Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode46MatVecRange0) panel5Mode46MatVecRange32) panel5Mode46MatVecRange64) panel5Mode46MatVecRange96) panel5Mode46MatVecRange128) row

theorem panel5Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel5MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel5MomentData.moments
        (P2RoundedFactorCheckpointData.panel5FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel5Mode47MatVecRange0) panel5Mode47MatVecRange32) panel5Mode47MatVecRange64) panel5Mode47MatVecRange96) panel5Mode47MatVecRange128) row

theorem panel5MomentData_correct :
    P2RoundedFactorCheckpointData.panel5MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel5FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel5DefectMoments_eq panel5ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel5Mode0MatVec_eq
      · exact panel5Mode2MatVec_eq
      · exact panel5Mode4MatVec_eq
      · exact panel5Mode6MatVec_eq
      · exact panel5Mode8MatVec_eq
      · exact panel5Mode10MatVec_eq
      · exact panel5Mode12MatVec_eq
      · exact panel5Mode14MatVec_eq
      · exact panel5Mode16MatVec_eq
      · exact panel5Mode18MatVec_eq
      · exact panel5Mode20MatVec_eq
      · exact panel5Mode22MatVec_eq
      · exact panel5Mode24MatVec_eq
      · exact panel5Mode26MatVec_eq
      · exact panel5Mode28MatVec_eq
      · exact panel5Mode30MatVec_eq
      · exact panel5Mode32MatVec_eq
      · exact panel5Mode34MatVec_eq
      · exact panel5Mode36MatVec_eq
      · exact panel5Mode38MatVec_eq
      · exact panel5Mode40MatVec_eq
      · exact panel5Mode42MatVec_eq
      · exact panel5Mode44MatVec_eq
      · exact panel5Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel5Mode1MatVec_eq
      · exact panel5Mode3MatVec_eq
      · exact panel5Mode5MatVec_eq
      · exact panel5Mode7MatVec_eq
      · exact panel5Mode9MatVec_eq
      · exact panel5Mode11MatVec_eq
      · exact panel5Mode13MatVec_eq
      · exact panel5Mode15MatVec_eq
      · exact panel5Mode17MatVec_eq
      · exact panel5Mode19MatVec_eq
      · exact panel5Mode21MatVec_eq
      · exact panel5Mode23MatVec_eq
      · exact panel5Mode25MatVec_eq
      · exact panel5Mode27MatVec_eq
      · exact panel5Mode29MatVec_eq
      · exact panel5Mode31MatVec_eq
      · exact panel5Mode33MatVec_eq
      · exact panel5Mode35MatVec_eq
      · exact panel5Mode37MatVec_eq
      · exact panel5Mode39MatVec_eq
      · exact panel5Mode41MatVec_eq
      · exact panel5Mode43MatVec_eq
      · exact panel5Mode45MatVec_eq
      · exact panel5Mode47MatVec_eq

end RHP2Bridge
