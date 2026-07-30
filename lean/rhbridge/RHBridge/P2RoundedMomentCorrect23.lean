import RHBridge.P2RoundedFlatFactorCheckpoint23
import RHBridge.P2RoundedMomentLengths23
import RHBridge.P2RoundedMomentCheckpointCheck23_moments
import RHBridge.P2RoundedMomentCheckpointCheck23_mode0
import RHBridge.P2RoundedMomentCheckpointCheck23_mode1
import RHBridge.P2RoundedMomentCheckpointCheck23_mode2
import RHBridge.P2RoundedMomentCheckpointCheck23_mode3
import RHBridge.P2RoundedMomentCheckpointCheck23_mode4
import RHBridge.P2RoundedMomentCheckpointCheck23_mode5
import RHBridge.P2RoundedMomentCheckpointCheck23_mode6
import RHBridge.P2RoundedMomentCheckpointCheck23_mode7
import RHBridge.P2RoundedMomentCheckpointCheck23_mode8
import RHBridge.P2RoundedMomentCheckpointCheck23_mode9
import RHBridge.P2RoundedMomentCheckpointCheck23_mode10
import RHBridge.P2RoundedMomentCheckpointCheck23_mode11
import RHBridge.P2RoundedMomentCheckpointCheck23_mode12
import RHBridge.P2RoundedMomentCheckpointCheck23_mode13
import RHBridge.P2RoundedMomentCheckpointCheck23_mode14
import RHBridge.P2RoundedMomentCheckpointCheck23_mode15
import RHBridge.P2RoundedMomentCheckpointCheck23_mode16
import RHBridge.P2RoundedMomentCheckpointCheck23_mode17
import RHBridge.P2RoundedMomentCheckpointCheck23_mode18
import RHBridge.P2RoundedMomentCheckpointCheck23_mode19
import RHBridge.P2RoundedMomentCheckpointCheck23_mode20
import RHBridge.P2RoundedMomentCheckpointCheck23_mode21
import RHBridge.P2RoundedMomentCheckpointCheck23_mode22
import RHBridge.P2RoundedMomentCheckpointCheck23_mode23
import RHBridge.P2RoundedMomentCheckpointCheck23_mode24
import RHBridge.P2RoundedMomentCheckpointCheck23_mode25
import RHBridge.P2RoundedMomentCheckpointCheck23_mode26
import RHBridge.P2RoundedMomentCheckpointCheck23_mode27
import RHBridge.P2RoundedMomentCheckpointCheck23_mode28
import RHBridge.P2RoundedMomentCheckpointCheck23_mode29
import RHBridge.P2RoundedMomentCheckpointCheck23_mode30
import RHBridge.P2RoundedMomentCheckpointCheck23_mode31
import RHBridge.P2RoundedMomentCheckpointCheck23_mode32
import RHBridge.P2RoundedMomentCheckpointCheck23_mode33
import RHBridge.P2RoundedMomentCheckpointCheck23_mode34
import RHBridge.P2RoundedMomentCheckpointCheck23_mode35
import RHBridge.P2RoundedMomentCheckpointCheck23_mode36
import RHBridge.P2RoundedMomentCheckpointCheck23_mode37
import RHBridge.P2RoundedMomentCheckpointCheck23_mode38
import RHBridge.P2RoundedMomentCheckpointCheck23_mode39
import RHBridge.P2RoundedMomentCheckpointCheck23_mode40
import RHBridge.P2RoundedMomentCheckpointCheck23_mode41
import RHBridge.P2RoundedMomentCheckpointCheck23_mode42
import RHBridge.P2RoundedMomentCheckpointCheck23_mode43
import RHBridge.P2RoundedMomentCheckpointCheck23_mode44
import RHBridge.P2RoundedMomentCheckpointCheck23_mode45
import RHBridge.P2RoundedMomentCheckpointCheck23_mode46
import RHBridge.P2RoundedMomentCheckpointCheck23_mode47

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

theorem panel23DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel23FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23DefectMomentRange0) panel23DefectMomentRange64) panel23DefectMomentRange128) panel23DefectMomentRange192) panel23DefectMomentRange256) row

theorem panel23Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode0MatVecRange0) panel23Mode0MatVecRange32) panel23Mode0MatVecRange64) panel23Mode0MatVecRange96) panel23Mode0MatVecRange128) row

theorem panel23Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode1MatVecRange0) panel23Mode1MatVecRange32) panel23Mode1MatVecRange64) panel23Mode1MatVecRange96) panel23Mode1MatVecRange128) row

theorem panel23Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode2MatVecRange0) panel23Mode2MatVecRange32) panel23Mode2MatVecRange64) panel23Mode2MatVecRange96) panel23Mode2MatVecRange128) row

theorem panel23Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode3MatVecRange0) panel23Mode3MatVecRange32) panel23Mode3MatVecRange64) panel23Mode3MatVecRange96) panel23Mode3MatVecRange128) row

theorem panel23Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode4MatVecRange0) panel23Mode4MatVecRange32) panel23Mode4MatVecRange64) panel23Mode4MatVecRange96) panel23Mode4MatVecRange128) row

theorem panel23Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode5MatVecRange0) panel23Mode5MatVecRange32) panel23Mode5MatVecRange64) panel23Mode5MatVecRange96) panel23Mode5MatVecRange128) row

theorem panel23Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode6MatVecRange0) panel23Mode6MatVecRange32) panel23Mode6MatVecRange64) panel23Mode6MatVecRange96) panel23Mode6MatVecRange128) row

theorem panel23Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode7MatVecRange0) panel23Mode7MatVecRange32) panel23Mode7MatVecRange64) panel23Mode7MatVecRange96) panel23Mode7MatVecRange128) row

theorem panel23Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode8MatVecRange0) panel23Mode8MatVecRange32) panel23Mode8MatVecRange64) panel23Mode8MatVecRange96) panel23Mode8MatVecRange128) row

theorem panel23Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode9MatVecRange0) panel23Mode9MatVecRange32) panel23Mode9MatVecRange64) panel23Mode9MatVecRange96) panel23Mode9MatVecRange128) row

theorem panel23Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode10MatVecRange0) panel23Mode10MatVecRange32) panel23Mode10MatVecRange64) panel23Mode10MatVecRange96) panel23Mode10MatVecRange128) row

theorem panel23Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode11MatVecRange0) panel23Mode11MatVecRange32) panel23Mode11MatVecRange64) panel23Mode11MatVecRange96) panel23Mode11MatVecRange128) row

theorem panel23Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode12MatVecRange0) panel23Mode12MatVecRange32) panel23Mode12MatVecRange64) panel23Mode12MatVecRange96) panel23Mode12MatVecRange128) row

theorem panel23Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode13MatVecRange0) panel23Mode13MatVecRange32) panel23Mode13MatVecRange64) panel23Mode13MatVecRange96) panel23Mode13MatVecRange128) row

theorem panel23Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode14MatVecRange0) panel23Mode14MatVecRange32) panel23Mode14MatVecRange64) panel23Mode14MatVecRange96) panel23Mode14MatVecRange128) row

theorem panel23Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode15MatVecRange0) panel23Mode15MatVecRange32) panel23Mode15MatVecRange64) panel23Mode15MatVecRange96) panel23Mode15MatVecRange128) row

theorem panel23Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode16MatVecRange0) panel23Mode16MatVecRange32) panel23Mode16MatVecRange64) panel23Mode16MatVecRange96) panel23Mode16MatVecRange128) row

theorem panel23Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode17MatVecRange0) panel23Mode17MatVecRange32) panel23Mode17MatVecRange64) panel23Mode17MatVecRange96) panel23Mode17MatVecRange128) row

theorem panel23Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode18MatVecRange0) panel23Mode18MatVecRange32) panel23Mode18MatVecRange64) panel23Mode18MatVecRange96) panel23Mode18MatVecRange128) row

theorem panel23Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode19MatVecRange0) panel23Mode19MatVecRange32) panel23Mode19MatVecRange64) panel23Mode19MatVecRange96) panel23Mode19MatVecRange128) row

theorem panel23Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode20MatVecRange0) panel23Mode20MatVecRange32) panel23Mode20MatVecRange64) panel23Mode20MatVecRange96) panel23Mode20MatVecRange128) row

theorem panel23Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode21MatVecRange0) panel23Mode21MatVecRange32) panel23Mode21MatVecRange64) panel23Mode21MatVecRange96) panel23Mode21MatVecRange128) row

theorem panel23Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode22MatVecRange0) panel23Mode22MatVecRange32) panel23Mode22MatVecRange64) panel23Mode22MatVecRange96) panel23Mode22MatVecRange128) row

theorem panel23Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode23MatVecRange0) panel23Mode23MatVecRange32) panel23Mode23MatVecRange64) panel23Mode23MatVecRange96) panel23Mode23MatVecRange128) row

theorem panel23Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode24MatVecRange0) panel23Mode24MatVecRange32) panel23Mode24MatVecRange64) panel23Mode24MatVecRange96) panel23Mode24MatVecRange128) row

theorem panel23Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode25MatVecRange0) panel23Mode25MatVecRange32) panel23Mode25MatVecRange64) panel23Mode25MatVecRange96) panel23Mode25MatVecRange128) row

theorem panel23Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode26MatVecRange0) panel23Mode26MatVecRange32) panel23Mode26MatVecRange64) panel23Mode26MatVecRange96) panel23Mode26MatVecRange128) row

theorem panel23Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode27MatVecRange0) panel23Mode27MatVecRange32) panel23Mode27MatVecRange64) panel23Mode27MatVecRange96) panel23Mode27MatVecRange128) row

theorem panel23Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode28MatVecRange0) panel23Mode28MatVecRange32) panel23Mode28MatVecRange64) panel23Mode28MatVecRange96) panel23Mode28MatVecRange128) row

theorem panel23Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode29MatVecRange0) panel23Mode29MatVecRange32) panel23Mode29MatVecRange64) panel23Mode29MatVecRange96) panel23Mode29MatVecRange128) row

theorem panel23Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode30MatVecRange0) panel23Mode30MatVecRange32) panel23Mode30MatVecRange64) panel23Mode30MatVecRange96) panel23Mode30MatVecRange128) row

theorem panel23Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode31MatVecRange0) panel23Mode31MatVecRange32) panel23Mode31MatVecRange64) panel23Mode31MatVecRange96) panel23Mode31MatVecRange128) row

theorem panel23Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode32MatVecRange0) panel23Mode32MatVecRange32) panel23Mode32MatVecRange64) panel23Mode32MatVecRange96) panel23Mode32MatVecRange128) row

theorem panel23Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode33MatVecRange0) panel23Mode33MatVecRange32) panel23Mode33MatVecRange64) panel23Mode33MatVecRange96) panel23Mode33MatVecRange128) row

theorem panel23Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode34MatVecRange0) panel23Mode34MatVecRange32) panel23Mode34MatVecRange64) panel23Mode34MatVecRange96) panel23Mode34MatVecRange128) row

theorem panel23Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode35MatVecRange0) panel23Mode35MatVecRange32) panel23Mode35MatVecRange64) panel23Mode35MatVecRange96) panel23Mode35MatVecRange128) row

theorem panel23Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode36MatVecRange0) panel23Mode36MatVecRange32) panel23Mode36MatVecRange64) panel23Mode36MatVecRange96) panel23Mode36MatVecRange128) row

theorem panel23Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode37MatVecRange0) panel23Mode37MatVecRange32) panel23Mode37MatVecRange64) panel23Mode37MatVecRange96) panel23Mode37MatVecRange128) row

theorem panel23Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode38MatVecRange0) panel23Mode38MatVecRange32) panel23Mode38MatVecRange64) panel23Mode38MatVecRange96) panel23Mode38MatVecRange128) row

theorem panel23Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode39MatVecRange0) panel23Mode39MatVecRange32) panel23Mode39MatVecRange64) panel23Mode39MatVecRange96) panel23Mode39MatVecRange128) row

theorem panel23Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode40MatVecRange0) panel23Mode40MatVecRange32) panel23Mode40MatVecRange64) panel23Mode40MatVecRange96) panel23Mode40MatVecRange128) row

theorem panel23Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode41MatVecRange0) panel23Mode41MatVecRange32) panel23Mode41MatVecRange64) panel23Mode41MatVecRange96) panel23Mode41MatVecRange128) row

theorem panel23Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode42MatVecRange0) panel23Mode42MatVecRange32) panel23Mode42MatVecRange64) panel23Mode42MatVecRange96) panel23Mode42MatVecRange128) row

theorem panel23Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode43MatVecRange0) panel23Mode43MatVecRange32) panel23Mode43MatVecRange64) panel23Mode43MatVecRange96) panel23Mode43MatVecRange128) row

theorem panel23Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode44MatVecRange0) panel23Mode44MatVecRange32) panel23Mode44MatVecRange64) panel23Mode44MatVecRange96) panel23Mode44MatVecRange128) row

theorem panel23Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode45MatVecRange0) panel23Mode45MatVecRange32) panel23Mode45MatVecRange64) panel23Mode45MatVecRange96) panel23Mode45MatVecRange128) row

theorem panel23Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode46MatVecRange0) panel23Mode46MatVecRange32) panel23Mode46MatVecRange64) panel23Mode46MatVecRange96) panel23Mode46MatVecRange128) row

theorem panel23Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel23MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel23MomentData.moments
        (P2RoundedFactorCheckpointData.panel23FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel23Mode47MatVecRange0) panel23Mode47MatVecRange32) panel23Mode47MatVecRange64) panel23Mode47MatVecRange96) panel23Mode47MatVecRange128) row

theorem panel23MomentData_correct :
    P2RoundedFactorCheckpointData.panel23MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel23FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel23DefectMoments_eq panel23ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel23Mode0MatVec_eq
      · exact panel23Mode2MatVec_eq
      · exact panel23Mode4MatVec_eq
      · exact panel23Mode6MatVec_eq
      · exact panel23Mode8MatVec_eq
      · exact panel23Mode10MatVec_eq
      · exact panel23Mode12MatVec_eq
      · exact panel23Mode14MatVec_eq
      · exact panel23Mode16MatVec_eq
      · exact panel23Mode18MatVec_eq
      · exact panel23Mode20MatVec_eq
      · exact panel23Mode22MatVec_eq
      · exact panel23Mode24MatVec_eq
      · exact panel23Mode26MatVec_eq
      · exact panel23Mode28MatVec_eq
      · exact panel23Mode30MatVec_eq
      · exact panel23Mode32MatVec_eq
      · exact panel23Mode34MatVec_eq
      · exact panel23Mode36MatVec_eq
      · exact panel23Mode38MatVec_eq
      · exact panel23Mode40MatVec_eq
      · exact panel23Mode42MatVec_eq
      · exact panel23Mode44MatVec_eq
      · exact panel23Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel23Mode1MatVec_eq
      · exact panel23Mode3MatVec_eq
      · exact panel23Mode5MatVec_eq
      · exact panel23Mode7MatVec_eq
      · exact panel23Mode9MatVec_eq
      · exact panel23Mode11MatVec_eq
      · exact panel23Mode13MatVec_eq
      · exact panel23Mode15MatVec_eq
      · exact panel23Mode17MatVec_eq
      · exact panel23Mode19MatVec_eq
      · exact panel23Mode21MatVec_eq
      · exact panel23Mode23MatVec_eq
      · exact panel23Mode25MatVec_eq
      · exact panel23Mode27MatVec_eq
      · exact panel23Mode29MatVec_eq
      · exact panel23Mode31MatVec_eq
      · exact panel23Mode33MatVec_eq
      · exact panel23Mode35MatVec_eq
      · exact panel23Mode37MatVec_eq
      · exact panel23Mode39MatVec_eq
      · exact panel23Mode41MatVec_eq
      · exact panel23Mode43MatVec_eq
      · exact panel23Mode45MatVec_eq
      · exact panel23Mode47MatVec_eq

end RHP2Bridge
