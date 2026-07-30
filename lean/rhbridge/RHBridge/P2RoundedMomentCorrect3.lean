import RHBridge.P2RoundedFlatFactorCheckpoint3
import RHBridge.P2RoundedMomentLengths3
import RHBridge.P2RoundedMomentCheckpointCheck3_moments
import RHBridge.P2RoundedMomentCheckpointCheck3_mode0
import RHBridge.P2RoundedMomentCheckpointCheck3_mode1
import RHBridge.P2RoundedMomentCheckpointCheck3_mode2
import RHBridge.P2RoundedMomentCheckpointCheck3_mode3
import RHBridge.P2RoundedMomentCheckpointCheck3_mode4
import RHBridge.P2RoundedMomentCheckpointCheck3_mode5
import RHBridge.P2RoundedMomentCheckpointCheck3_mode6
import RHBridge.P2RoundedMomentCheckpointCheck3_mode7
import RHBridge.P2RoundedMomentCheckpointCheck3_mode8
import RHBridge.P2RoundedMomentCheckpointCheck3_mode9
import RHBridge.P2RoundedMomentCheckpointCheck3_mode10
import RHBridge.P2RoundedMomentCheckpointCheck3_mode11
import RHBridge.P2RoundedMomentCheckpointCheck3_mode12
import RHBridge.P2RoundedMomentCheckpointCheck3_mode13
import RHBridge.P2RoundedMomentCheckpointCheck3_mode14
import RHBridge.P2RoundedMomentCheckpointCheck3_mode15
import RHBridge.P2RoundedMomentCheckpointCheck3_mode16
import RHBridge.P2RoundedMomentCheckpointCheck3_mode17
import RHBridge.P2RoundedMomentCheckpointCheck3_mode18
import RHBridge.P2RoundedMomentCheckpointCheck3_mode19
import RHBridge.P2RoundedMomentCheckpointCheck3_mode20
import RHBridge.P2RoundedMomentCheckpointCheck3_mode21
import RHBridge.P2RoundedMomentCheckpointCheck3_mode22
import RHBridge.P2RoundedMomentCheckpointCheck3_mode23
import RHBridge.P2RoundedMomentCheckpointCheck3_mode24
import RHBridge.P2RoundedMomentCheckpointCheck3_mode25
import RHBridge.P2RoundedMomentCheckpointCheck3_mode26
import RHBridge.P2RoundedMomentCheckpointCheck3_mode27
import RHBridge.P2RoundedMomentCheckpointCheck3_mode28
import RHBridge.P2RoundedMomentCheckpointCheck3_mode29
import RHBridge.P2RoundedMomentCheckpointCheck3_mode30
import RHBridge.P2RoundedMomentCheckpointCheck3_mode31
import RHBridge.P2RoundedMomentCheckpointCheck3_mode32
import RHBridge.P2RoundedMomentCheckpointCheck3_mode33
import RHBridge.P2RoundedMomentCheckpointCheck3_mode34
import RHBridge.P2RoundedMomentCheckpointCheck3_mode35
import RHBridge.P2RoundedMomentCheckpointCheck3_mode36
import RHBridge.P2RoundedMomentCheckpointCheck3_mode37
import RHBridge.P2RoundedMomentCheckpointCheck3_mode38
import RHBridge.P2RoundedMomentCheckpointCheck3_mode39
import RHBridge.P2RoundedMomentCheckpointCheck3_mode40
import RHBridge.P2RoundedMomentCheckpointCheck3_mode41
import RHBridge.P2RoundedMomentCheckpointCheck3_mode42
import RHBridge.P2RoundedMomentCheckpointCheck3_mode43
import RHBridge.P2RoundedMomentCheckpointCheck3_mode44
import RHBridge.P2RoundedMomentCheckpointCheck3_mode45
import RHBridge.P2RoundedMomentCheckpointCheck3_mode46
import RHBridge.P2RoundedMomentCheckpointCheck3_mode47

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

theorem panel3DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel3FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3DefectMomentRange0) panel3DefectMomentRange64) panel3DefectMomentRange128) panel3DefectMomentRange192) panel3DefectMomentRange256) row

theorem panel3Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode0MatVecRange0) panel3Mode0MatVecRange32) panel3Mode0MatVecRange64) panel3Mode0MatVecRange96) panel3Mode0MatVecRange128) row

theorem panel3Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode1MatVecRange0) panel3Mode1MatVecRange32) panel3Mode1MatVecRange64) panel3Mode1MatVecRange96) panel3Mode1MatVecRange128) row

theorem panel3Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode2MatVecRange0) panel3Mode2MatVecRange32) panel3Mode2MatVecRange64) panel3Mode2MatVecRange96) panel3Mode2MatVecRange128) row

theorem panel3Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode3MatVecRange0) panel3Mode3MatVecRange32) panel3Mode3MatVecRange64) panel3Mode3MatVecRange96) panel3Mode3MatVecRange128) row

theorem panel3Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode4MatVecRange0) panel3Mode4MatVecRange32) panel3Mode4MatVecRange64) panel3Mode4MatVecRange96) panel3Mode4MatVecRange128) row

theorem panel3Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode5MatVecRange0) panel3Mode5MatVecRange32) panel3Mode5MatVecRange64) panel3Mode5MatVecRange96) panel3Mode5MatVecRange128) row

theorem panel3Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode6MatVecRange0) panel3Mode6MatVecRange32) panel3Mode6MatVecRange64) panel3Mode6MatVecRange96) panel3Mode6MatVecRange128) row

theorem panel3Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode7MatVecRange0) panel3Mode7MatVecRange32) panel3Mode7MatVecRange64) panel3Mode7MatVecRange96) panel3Mode7MatVecRange128) row

theorem panel3Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode8MatVecRange0) panel3Mode8MatVecRange32) panel3Mode8MatVecRange64) panel3Mode8MatVecRange96) panel3Mode8MatVecRange128) row

theorem panel3Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode9MatVecRange0) panel3Mode9MatVecRange32) panel3Mode9MatVecRange64) panel3Mode9MatVecRange96) panel3Mode9MatVecRange128) row

theorem panel3Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode10MatVecRange0) panel3Mode10MatVecRange32) panel3Mode10MatVecRange64) panel3Mode10MatVecRange96) panel3Mode10MatVecRange128) row

theorem panel3Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode11MatVecRange0) panel3Mode11MatVecRange32) panel3Mode11MatVecRange64) panel3Mode11MatVecRange96) panel3Mode11MatVecRange128) row

theorem panel3Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode12MatVecRange0) panel3Mode12MatVecRange32) panel3Mode12MatVecRange64) panel3Mode12MatVecRange96) panel3Mode12MatVecRange128) row

theorem panel3Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode13MatVecRange0) panel3Mode13MatVecRange32) panel3Mode13MatVecRange64) panel3Mode13MatVecRange96) panel3Mode13MatVecRange128) row

theorem panel3Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode14MatVecRange0) panel3Mode14MatVecRange32) panel3Mode14MatVecRange64) panel3Mode14MatVecRange96) panel3Mode14MatVecRange128) row

theorem panel3Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode15MatVecRange0) panel3Mode15MatVecRange32) panel3Mode15MatVecRange64) panel3Mode15MatVecRange96) panel3Mode15MatVecRange128) row

theorem panel3Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode16MatVecRange0) panel3Mode16MatVecRange32) panel3Mode16MatVecRange64) panel3Mode16MatVecRange96) panel3Mode16MatVecRange128) row

theorem panel3Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode17MatVecRange0) panel3Mode17MatVecRange32) panel3Mode17MatVecRange64) panel3Mode17MatVecRange96) panel3Mode17MatVecRange128) row

theorem panel3Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode18MatVecRange0) panel3Mode18MatVecRange32) panel3Mode18MatVecRange64) panel3Mode18MatVecRange96) panel3Mode18MatVecRange128) row

theorem panel3Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode19MatVecRange0) panel3Mode19MatVecRange32) panel3Mode19MatVecRange64) panel3Mode19MatVecRange96) panel3Mode19MatVecRange128) row

theorem panel3Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode20MatVecRange0) panel3Mode20MatVecRange32) panel3Mode20MatVecRange64) panel3Mode20MatVecRange96) panel3Mode20MatVecRange128) row

theorem panel3Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode21MatVecRange0) panel3Mode21MatVecRange32) panel3Mode21MatVecRange64) panel3Mode21MatVecRange96) panel3Mode21MatVecRange128) row

theorem panel3Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode22MatVecRange0) panel3Mode22MatVecRange32) panel3Mode22MatVecRange64) panel3Mode22MatVecRange96) panel3Mode22MatVecRange128) row

theorem panel3Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode23MatVecRange0) panel3Mode23MatVecRange32) panel3Mode23MatVecRange64) panel3Mode23MatVecRange96) panel3Mode23MatVecRange128) row

theorem panel3Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode24MatVecRange0) panel3Mode24MatVecRange32) panel3Mode24MatVecRange64) panel3Mode24MatVecRange96) panel3Mode24MatVecRange128) row

theorem panel3Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode25MatVecRange0) panel3Mode25MatVecRange32) panel3Mode25MatVecRange64) panel3Mode25MatVecRange96) panel3Mode25MatVecRange128) row

theorem panel3Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode26MatVecRange0) panel3Mode26MatVecRange32) panel3Mode26MatVecRange64) panel3Mode26MatVecRange96) panel3Mode26MatVecRange128) row

theorem panel3Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode27MatVecRange0) panel3Mode27MatVecRange32) panel3Mode27MatVecRange64) panel3Mode27MatVecRange96) panel3Mode27MatVecRange128) row

theorem panel3Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode28MatVecRange0) panel3Mode28MatVecRange32) panel3Mode28MatVecRange64) panel3Mode28MatVecRange96) panel3Mode28MatVecRange128) row

theorem panel3Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode29MatVecRange0) panel3Mode29MatVecRange32) panel3Mode29MatVecRange64) panel3Mode29MatVecRange96) panel3Mode29MatVecRange128) row

theorem panel3Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode30MatVecRange0) panel3Mode30MatVecRange32) panel3Mode30MatVecRange64) panel3Mode30MatVecRange96) panel3Mode30MatVecRange128) row

theorem panel3Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode31MatVecRange0) panel3Mode31MatVecRange32) panel3Mode31MatVecRange64) panel3Mode31MatVecRange96) panel3Mode31MatVecRange128) row

theorem panel3Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode32MatVecRange0) panel3Mode32MatVecRange32) panel3Mode32MatVecRange64) panel3Mode32MatVecRange96) panel3Mode32MatVecRange128) row

theorem panel3Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode33MatVecRange0) panel3Mode33MatVecRange32) panel3Mode33MatVecRange64) panel3Mode33MatVecRange96) panel3Mode33MatVecRange128) row

theorem panel3Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode34MatVecRange0) panel3Mode34MatVecRange32) panel3Mode34MatVecRange64) panel3Mode34MatVecRange96) panel3Mode34MatVecRange128) row

theorem panel3Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode35MatVecRange0) panel3Mode35MatVecRange32) panel3Mode35MatVecRange64) panel3Mode35MatVecRange96) panel3Mode35MatVecRange128) row

theorem panel3Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode36MatVecRange0) panel3Mode36MatVecRange32) panel3Mode36MatVecRange64) panel3Mode36MatVecRange96) panel3Mode36MatVecRange128) row

theorem panel3Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode37MatVecRange0) panel3Mode37MatVecRange32) panel3Mode37MatVecRange64) panel3Mode37MatVecRange96) panel3Mode37MatVecRange128) row

theorem panel3Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode38MatVecRange0) panel3Mode38MatVecRange32) panel3Mode38MatVecRange64) panel3Mode38MatVecRange96) panel3Mode38MatVecRange128) row

theorem panel3Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode39MatVecRange0) panel3Mode39MatVecRange32) panel3Mode39MatVecRange64) panel3Mode39MatVecRange96) panel3Mode39MatVecRange128) row

theorem panel3Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode40MatVecRange0) panel3Mode40MatVecRange32) panel3Mode40MatVecRange64) panel3Mode40MatVecRange96) panel3Mode40MatVecRange128) row

theorem panel3Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode41MatVecRange0) panel3Mode41MatVecRange32) panel3Mode41MatVecRange64) panel3Mode41MatVecRange96) panel3Mode41MatVecRange128) row

theorem panel3Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode42MatVecRange0) panel3Mode42MatVecRange32) panel3Mode42MatVecRange64) panel3Mode42MatVecRange96) panel3Mode42MatVecRange128) row

theorem panel3Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode43MatVecRange0) panel3Mode43MatVecRange32) panel3Mode43MatVecRange64) panel3Mode43MatVecRange96) panel3Mode43MatVecRange128) row

theorem panel3Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode44MatVecRange0) panel3Mode44MatVecRange32) panel3Mode44MatVecRange64) panel3Mode44MatVecRange96) panel3Mode44MatVecRange128) row

theorem panel3Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode45MatVecRange0) panel3Mode45MatVecRange32) panel3Mode45MatVecRange64) panel3Mode45MatVecRange96) panel3Mode45MatVecRange128) row

theorem panel3Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode46MatVecRange0) panel3Mode46MatVecRange32) panel3Mode46MatVecRange64) panel3Mode46MatVecRange96) panel3Mode46MatVecRange128) row

theorem panel3Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel3MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel3MomentData.moments
        (P2RoundedFactorCheckpointData.panel3FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel3Mode47MatVecRange0) panel3Mode47MatVecRange32) panel3Mode47MatVecRange64) panel3Mode47MatVecRange96) panel3Mode47MatVecRange128) row

theorem panel3MomentData_correct :
    P2RoundedFactorCheckpointData.panel3MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel3FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel3DefectMoments_eq panel3ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel3Mode0MatVec_eq
      · exact panel3Mode2MatVec_eq
      · exact panel3Mode4MatVec_eq
      · exact panel3Mode6MatVec_eq
      · exact panel3Mode8MatVec_eq
      · exact panel3Mode10MatVec_eq
      · exact panel3Mode12MatVec_eq
      · exact panel3Mode14MatVec_eq
      · exact panel3Mode16MatVec_eq
      · exact panel3Mode18MatVec_eq
      · exact panel3Mode20MatVec_eq
      · exact panel3Mode22MatVec_eq
      · exact panel3Mode24MatVec_eq
      · exact panel3Mode26MatVec_eq
      · exact panel3Mode28MatVec_eq
      · exact panel3Mode30MatVec_eq
      · exact panel3Mode32MatVec_eq
      · exact panel3Mode34MatVec_eq
      · exact panel3Mode36MatVec_eq
      · exact panel3Mode38MatVec_eq
      · exact panel3Mode40MatVec_eq
      · exact panel3Mode42MatVec_eq
      · exact panel3Mode44MatVec_eq
      · exact panel3Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel3Mode1MatVec_eq
      · exact panel3Mode3MatVec_eq
      · exact panel3Mode5MatVec_eq
      · exact panel3Mode7MatVec_eq
      · exact panel3Mode9MatVec_eq
      · exact panel3Mode11MatVec_eq
      · exact panel3Mode13MatVec_eq
      · exact panel3Mode15MatVec_eq
      · exact panel3Mode17MatVec_eq
      · exact panel3Mode19MatVec_eq
      · exact panel3Mode21MatVec_eq
      · exact panel3Mode23MatVec_eq
      · exact panel3Mode25MatVec_eq
      · exact panel3Mode27MatVec_eq
      · exact panel3Mode29MatVec_eq
      · exact panel3Mode31MatVec_eq
      · exact panel3Mode33MatVec_eq
      · exact panel3Mode35MatVec_eq
      · exact panel3Mode37MatVec_eq
      · exact panel3Mode39MatVec_eq
      · exact panel3Mode41MatVec_eq
      · exact panel3Mode43MatVec_eq
      · exact panel3Mode45MatVec_eq
      · exact panel3Mode47MatVec_eq

end RHP2Bridge
