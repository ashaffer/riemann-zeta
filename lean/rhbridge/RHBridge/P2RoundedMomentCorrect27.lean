import RHBridge.P2RoundedFlatFactorCheckpoint27
import RHBridge.P2RoundedMomentLengths27
import RHBridge.P2RoundedMomentCheckpointCheck27_moments
import RHBridge.P2RoundedMomentCheckpointCheck27_mode0
import RHBridge.P2RoundedMomentCheckpointCheck27_mode1
import RHBridge.P2RoundedMomentCheckpointCheck27_mode2
import RHBridge.P2RoundedMomentCheckpointCheck27_mode3
import RHBridge.P2RoundedMomentCheckpointCheck27_mode4
import RHBridge.P2RoundedMomentCheckpointCheck27_mode5
import RHBridge.P2RoundedMomentCheckpointCheck27_mode6
import RHBridge.P2RoundedMomentCheckpointCheck27_mode7
import RHBridge.P2RoundedMomentCheckpointCheck27_mode8
import RHBridge.P2RoundedMomentCheckpointCheck27_mode9
import RHBridge.P2RoundedMomentCheckpointCheck27_mode10
import RHBridge.P2RoundedMomentCheckpointCheck27_mode11
import RHBridge.P2RoundedMomentCheckpointCheck27_mode12
import RHBridge.P2RoundedMomentCheckpointCheck27_mode13
import RHBridge.P2RoundedMomentCheckpointCheck27_mode14
import RHBridge.P2RoundedMomentCheckpointCheck27_mode15
import RHBridge.P2RoundedMomentCheckpointCheck27_mode16
import RHBridge.P2RoundedMomentCheckpointCheck27_mode17
import RHBridge.P2RoundedMomentCheckpointCheck27_mode18
import RHBridge.P2RoundedMomentCheckpointCheck27_mode19
import RHBridge.P2RoundedMomentCheckpointCheck27_mode20
import RHBridge.P2RoundedMomentCheckpointCheck27_mode21
import RHBridge.P2RoundedMomentCheckpointCheck27_mode22
import RHBridge.P2RoundedMomentCheckpointCheck27_mode23
import RHBridge.P2RoundedMomentCheckpointCheck27_mode24
import RHBridge.P2RoundedMomentCheckpointCheck27_mode25
import RHBridge.P2RoundedMomentCheckpointCheck27_mode26
import RHBridge.P2RoundedMomentCheckpointCheck27_mode27
import RHBridge.P2RoundedMomentCheckpointCheck27_mode28
import RHBridge.P2RoundedMomentCheckpointCheck27_mode29
import RHBridge.P2RoundedMomentCheckpointCheck27_mode30
import RHBridge.P2RoundedMomentCheckpointCheck27_mode31
import RHBridge.P2RoundedMomentCheckpointCheck27_mode32
import RHBridge.P2RoundedMomentCheckpointCheck27_mode33
import RHBridge.P2RoundedMomentCheckpointCheck27_mode34
import RHBridge.P2RoundedMomentCheckpointCheck27_mode35
import RHBridge.P2RoundedMomentCheckpointCheck27_mode36
import RHBridge.P2RoundedMomentCheckpointCheck27_mode37
import RHBridge.P2RoundedMomentCheckpointCheck27_mode38
import RHBridge.P2RoundedMomentCheckpointCheck27_mode39
import RHBridge.P2RoundedMomentCheckpointCheck27_mode40
import RHBridge.P2RoundedMomentCheckpointCheck27_mode41
import RHBridge.P2RoundedMomentCheckpointCheck27_mode42
import RHBridge.P2RoundedMomentCheckpointCheck27_mode43
import RHBridge.P2RoundedMomentCheckpointCheck27_mode44
import RHBridge.P2RoundedMomentCheckpointCheck27_mode45
import RHBridge.P2RoundedMomentCheckpointCheck27_mode46
import RHBridge.P2RoundedMomentCheckpointCheck27_mode47

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

theorem panel27DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel27FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27DefectMomentRange0) panel27DefectMomentRange64) panel27DefectMomentRange128) panel27DefectMomentRange192) panel27DefectMomentRange256) row

theorem panel27Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode0MatVecRange0) panel27Mode0MatVecRange32) panel27Mode0MatVecRange64) panel27Mode0MatVecRange96) panel27Mode0MatVecRange128) row

theorem panel27Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode1MatVecRange0) panel27Mode1MatVecRange32) panel27Mode1MatVecRange64) panel27Mode1MatVecRange96) panel27Mode1MatVecRange128) row

theorem panel27Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode2MatVecRange0) panel27Mode2MatVecRange32) panel27Mode2MatVecRange64) panel27Mode2MatVecRange96) panel27Mode2MatVecRange128) row

theorem panel27Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode3MatVecRange0) panel27Mode3MatVecRange32) panel27Mode3MatVecRange64) panel27Mode3MatVecRange96) panel27Mode3MatVecRange128) row

theorem panel27Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode4MatVecRange0) panel27Mode4MatVecRange32) panel27Mode4MatVecRange64) panel27Mode4MatVecRange96) panel27Mode4MatVecRange128) row

theorem panel27Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode5MatVecRange0) panel27Mode5MatVecRange32) panel27Mode5MatVecRange64) panel27Mode5MatVecRange96) panel27Mode5MatVecRange128) row

theorem panel27Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode6MatVecRange0) panel27Mode6MatVecRange32) panel27Mode6MatVecRange64) panel27Mode6MatVecRange96) panel27Mode6MatVecRange128) row

theorem panel27Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode7MatVecRange0) panel27Mode7MatVecRange32) panel27Mode7MatVecRange64) panel27Mode7MatVecRange96) panel27Mode7MatVecRange128) row

theorem panel27Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode8MatVecRange0) panel27Mode8MatVecRange32) panel27Mode8MatVecRange64) panel27Mode8MatVecRange96) panel27Mode8MatVecRange128) row

theorem panel27Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode9MatVecRange0) panel27Mode9MatVecRange32) panel27Mode9MatVecRange64) panel27Mode9MatVecRange96) panel27Mode9MatVecRange128) row

theorem panel27Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode10MatVecRange0) panel27Mode10MatVecRange32) panel27Mode10MatVecRange64) panel27Mode10MatVecRange96) panel27Mode10MatVecRange128) row

theorem panel27Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode11MatVecRange0) panel27Mode11MatVecRange32) panel27Mode11MatVecRange64) panel27Mode11MatVecRange96) panel27Mode11MatVecRange128) row

theorem panel27Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode12MatVecRange0) panel27Mode12MatVecRange32) panel27Mode12MatVecRange64) panel27Mode12MatVecRange96) panel27Mode12MatVecRange128) row

theorem panel27Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode13MatVecRange0) panel27Mode13MatVecRange32) panel27Mode13MatVecRange64) panel27Mode13MatVecRange96) panel27Mode13MatVecRange128) row

theorem panel27Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode14MatVecRange0) panel27Mode14MatVecRange32) panel27Mode14MatVecRange64) panel27Mode14MatVecRange96) panel27Mode14MatVecRange128) row

theorem panel27Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode15MatVecRange0) panel27Mode15MatVecRange32) panel27Mode15MatVecRange64) panel27Mode15MatVecRange96) panel27Mode15MatVecRange128) row

theorem panel27Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode16MatVecRange0) panel27Mode16MatVecRange32) panel27Mode16MatVecRange64) panel27Mode16MatVecRange96) panel27Mode16MatVecRange128) row

theorem panel27Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode17MatVecRange0) panel27Mode17MatVecRange32) panel27Mode17MatVecRange64) panel27Mode17MatVecRange96) panel27Mode17MatVecRange128) row

theorem panel27Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode18MatVecRange0) panel27Mode18MatVecRange32) panel27Mode18MatVecRange64) panel27Mode18MatVecRange96) panel27Mode18MatVecRange128) row

theorem panel27Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode19MatVecRange0) panel27Mode19MatVecRange32) panel27Mode19MatVecRange64) panel27Mode19MatVecRange96) panel27Mode19MatVecRange128) row

theorem panel27Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode20MatVecRange0) panel27Mode20MatVecRange32) panel27Mode20MatVecRange64) panel27Mode20MatVecRange96) panel27Mode20MatVecRange128) row

theorem panel27Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode21MatVecRange0) panel27Mode21MatVecRange32) panel27Mode21MatVecRange64) panel27Mode21MatVecRange96) panel27Mode21MatVecRange128) row

theorem panel27Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode22MatVecRange0) panel27Mode22MatVecRange32) panel27Mode22MatVecRange64) panel27Mode22MatVecRange96) panel27Mode22MatVecRange128) row

theorem panel27Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode23MatVecRange0) panel27Mode23MatVecRange32) panel27Mode23MatVecRange64) panel27Mode23MatVecRange96) panel27Mode23MatVecRange128) row

theorem panel27Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode24MatVecRange0) panel27Mode24MatVecRange32) panel27Mode24MatVecRange64) panel27Mode24MatVecRange96) panel27Mode24MatVecRange128) row

theorem panel27Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode25MatVecRange0) panel27Mode25MatVecRange32) panel27Mode25MatVecRange64) panel27Mode25MatVecRange96) panel27Mode25MatVecRange128) row

theorem panel27Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode26MatVecRange0) panel27Mode26MatVecRange32) panel27Mode26MatVecRange64) panel27Mode26MatVecRange96) panel27Mode26MatVecRange128) row

theorem panel27Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode27MatVecRange0) panel27Mode27MatVecRange32) panel27Mode27MatVecRange64) panel27Mode27MatVecRange96) panel27Mode27MatVecRange128) row

theorem panel27Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode28MatVecRange0) panel27Mode28MatVecRange32) panel27Mode28MatVecRange64) panel27Mode28MatVecRange96) panel27Mode28MatVecRange128) row

theorem panel27Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode29MatVecRange0) panel27Mode29MatVecRange32) panel27Mode29MatVecRange64) panel27Mode29MatVecRange96) panel27Mode29MatVecRange128) row

theorem panel27Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode30MatVecRange0) panel27Mode30MatVecRange32) panel27Mode30MatVecRange64) panel27Mode30MatVecRange96) panel27Mode30MatVecRange128) row

theorem panel27Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode31MatVecRange0) panel27Mode31MatVecRange32) panel27Mode31MatVecRange64) panel27Mode31MatVecRange96) panel27Mode31MatVecRange128) row

theorem panel27Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode32MatVecRange0) panel27Mode32MatVecRange32) panel27Mode32MatVecRange64) panel27Mode32MatVecRange96) panel27Mode32MatVecRange128) row

theorem panel27Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode33MatVecRange0) panel27Mode33MatVecRange32) panel27Mode33MatVecRange64) panel27Mode33MatVecRange96) panel27Mode33MatVecRange128) row

theorem panel27Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode34MatVecRange0) panel27Mode34MatVecRange32) panel27Mode34MatVecRange64) panel27Mode34MatVecRange96) panel27Mode34MatVecRange128) row

theorem panel27Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode35MatVecRange0) panel27Mode35MatVecRange32) panel27Mode35MatVecRange64) panel27Mode35MatVecRange96) panel27Mode35MatVecRange128) row

theorem panel27Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode36MatVecRange0) panel27Mode36MatVecRange32) panel27Mode36MatVecRange64) panel27Mode36MatVecRange96) panel27Mode36MatVecRange128) row

theorem panel27Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode37MatVecRange0) panel27Mode37MatVecRange32) panel27Mode37MatVecRange64) panel27Mode37MatVecRange96) panel27Mode37MatVecRange128) row

theorem panel27Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode38MatVecRange0) panel27Mode38MatVecRange32) panel27Mode38MatVecRange64) panel27Mode38MatVecRange96) panel27Mode38MatVecRange128) row

theorem panel27Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode39MatVecRange0) panel27Mode39MatVecRange32) panel27Mode39MatVecRange64) panel27Mode39MatVecRange96) panel27Mode39MatVecRange128) row

theorem panel27Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode40MatVecRange0) panel27Mode40MatVecRange32) panel27Mode40MatVecRange64) panel27Mode40MatVecRange96) panel27Mode40MatVecRange128) row

theorem panel27Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode41MatVecRange0) panel27Mode41MatVecRange32) panel27Mode41MatVecRange64) panel27Mode41MatVecRange96) panel27Mode41MatVecRange128) row

theorem panel27Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode42MatVecRange0) panel27Mode42MatVecRange32) panel27Mode42MatVecRange64) panel27Mode42MatVecRange96) panel27Mode42MatVecRange128) row

theorem panel27Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode43MatVecRange0) panel27Mode43MatVecRange32) panel27Mode43MatVecRange64) panel27Mode43MatVecRange96) panel27Mode43MatVecRange128) row

theorem panel27Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode44MatVecRange0) panel27Mode44MatVecRange32) panel27Mode44MatVecRange64) panel27Mode44MatVecRange96) panel27Mode44MatVecRange128) row

theorem panel27Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode45MatVecRange0) panel27Mode45MatVecRange32) panel27Mode45MatVecRange64) panel27Mode45MatVecRange96) panel27Mode45MatVecRange128) row

theorem panel27Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode46MatVecRange0) panel27Mode46MatVecRange32) panel27Mode46MatVecRange64) panel27Mode46MatVecRange96) panel27Mode46MatVecRange128) row

theorem panel27Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel27MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel27MomentData.moments
        (P2RoundedFactorCheckpointData.panel27FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel27Mode47MatVecRange0) panel27Mode47MatVecRange32) panel27Mode47MatVecRange64) panel27Mode47MatVecRange96) panel27Mode47MatVecRange128) row

theorem panel27MomentData_correct :
    P2RoundedFactorCheckpointData.panel27MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel27FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel27DefectMoments_eq panel27ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel27Mode0MatVec_eq
      · exact panel27Mode2MatVec_eq
      · exact panel27Mode4MatVec_eq
      · exact panel27Mode6MatVec_eq
      · exact panel27Mode8MatVec_eq
      · exact panel27Mode10MatVec_eq
      · exact panel27Mode12MatVec_eq
      · exact panel27Mode14MatVec_eq
      · exact panel27Mode16MatVec_eq
      · exact panel27Mode18MatVec_eq
      · exact panel27Mode20MatVec_eq
      · exact panel27Mode22MatVec_eq
      · exact panel27Mode24MatVec_eq
      · exact panel27Mode26MatVec_eq
      · exact panel27Mode28MatVec_eq
      · exact panel27Mode30MatVec_eq
      · exact panel27Mode32MatVec_eq
      · exact panel27Mode34MatVec_eq
      · exact panel27Mode36MatVec_eq
      · exact panel27Mode38MatVec_eq
      · exact panel27Mode40MatVec_eq
      · exact panel27Mode42MatVec_eq
      · exact panel27Mode44MatVec_eq
      · exact panel27Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel27Mode1MatVec_eq
      · exact panel27Mode3MatVec_eq
      · exact panel27Mode5MatVec_eq
      · exact panel27Mode7MatVec_eq
      · exact panel27Mode9MatVec_eq
      · exact panel27Mode11MatVec_eq
      · exact panel27Mode13MatVec_eq
      · exact panel27Mode15MatVec_eq
      · exact panel27Mode17MatVec_eq
      · exact panel27Mode19MatVec_eq
      · exact panel27Mode21MatVec_eq
      · exact panel27Mode23MatVec_eq
      · exact panel27Mode25MatVec_eq
      · exact panel27Mode27MatVec_eq
      · exact panel27Mode29MatVec_eq
      · exact panel27Mode31MatVec_eq
      · exact panel27Mode33MatVec_eq
      · exact panel27Mode35MatVec_eq
      · exact panel27Mode37MatVec_eq
      · exact panel27Mode39MatVec_eq
      · exact panel27Mode41MatVec_eq
      · exact panel27Mode43MatVec_eq
      · exact panel27Mode45MatVec_eq
      · exact panel27Mode47MatVec_eq

end RHP2Bridge
