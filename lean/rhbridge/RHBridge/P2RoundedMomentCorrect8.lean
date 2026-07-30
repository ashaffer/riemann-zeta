import RHBridge.P2RoundedFlatFactorCheckpoint8
import RHBridge.P2RoundedMomentLengths8
import RHBridge.P2RoundedMomentCheckpointCheck8_moments
import RHBridge.P2RoundedMomentCheckpointCheck8_mode0
import RHBridge.P2RoundedMomentCheckpointCheck8_mode1
import RHBridge.P2RoundedMomentCheckpointCheck8_mode2
import RHBridge.P2RoundedMomentCheckpointCheck8_mode3
import RHBridge.P2RoundedMomentCheckpointCheck8_mode4
import RHBridge.P2RoundedMomentCheckpointCheck8_mode5
import RHBridge.P2RoundedMomentCheckpointCheck8_mode6
import RHBridge.P2RoundedMomentCheckpointCheck8_mode7
import RHBridge.P2RoundedMomentCheckpointCheck8_mode8
import RHBridge.P2RoundedMomentCheckpointCheck8_mode9
import RHBridge.P2RoundedMomentCheckpointCheck8_mode10
import RHBridge.P2RoundedMomentCheckpointCheck8_mode11
import RHBridge.P2RoundedMomentCheckpointCheck8_mode12
import RHBridge.P2RoundedMomentCheckpointCheck8_mode13
import RHBridge.P2RoundedMomentCheckpointCheck8_mode14
import RHBridge.P2RoundedMomentCheckpointCheck8_mode15
import RHBridge.P2RoundedMomentCheckpointCheck8_mode16
import RHBridge.P2RoundedMomentCheckpointCheck8_mode17
import RHBridge.P2RoundedMomentCheckpointCheck8_mode18
import RHBridge.P2RoundedMomentCheckpointCheck8_mode19
import RHBridge.P2RoundedMomentCheckpointCheck8_mode20
import RHBridge.P2RoundedMomentCheckpointCheck8_mode21
import RHBridge.P2RoundedMomentCheckpointCheck8_mode22
import RHBridge.P2RoundedMomentCheckpointCheck8_mode23
import RHBridge.P2RoundedMomentCheckpointCheck8_mode24
import RHBridge.P2RoundedMomentCheckpointCheck8_mode25
import RHBridge.P2RoundedMomentCheckpointCheck8_mode26
import RHBridge.P2RoundedMomentCheckpointCheck8_mode27
import RHBridge.P2RoundedMomentCheckpointCheck8_mode28
import RHBridge.P2RoundedMomentCheckpointCheck8_mode29
import RHBridge.P2RoundedMomentCheckpointCheck8_mode30
import RHBridge.P2RoundedMomentCheckpointCheck8_mode31
import RHBridge.P2RoundedMomentCheckpointCheck8_mode32
import RHBridge.P2RoundedMomentCheckpointCheck8_mode33
import RHBridge.P2RoundedMomentCheckpointCheck8_mode34
import RHBridge.P2RoundedMomentCheckpointCheck8_mode35
import RHBridge.P2RoundedMomentCheckpointCheck8_mode36
import RHBridge.P2RoundedMomentCheckpointCheck8_mode37
import RHBridge.P2RoundedMomentCheckpointCheck8_mode38
import RHBridge.P2RoundedMomentCheckpointCheck8_mode39
import RHBridge.P2RoundedMomentCheckpointCheck8_mode40
import RHBridge.P2RoundedMomentCheckpointCheck8_mode41
import RHBridge.P2RoundedMomentCheckpointCheck8_mode42
import RHBridge.P2RoundedMomentCheckpointCheck8_mode43
import RHBridge.P2RoundedMomentCheckpointCheck8_mode44
import RHBridge.P2RoundedMomentCheckpointCheck8_mode45
import RHBridge.P2RoundedMomentCheckpointCheck8_mode46
import RHBridge.P2RoundedMomentCheckpointCheck8_mode47

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

theorem panel8DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel8FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8DefectMomentRange0) panel8DefectMomentRange64) panel8DefectMomentRange128) panel8DefectMomentRange192) panel8DefectMomentRange256) row

theorem panel8Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode0MatVecRange0) panel8Mode0MatVecRange32) panel8Mode0MatVecRange64) panel8Mode0MatVecRange96) panel8Mode0MatVecRange128) row

theorem panel8Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode1MatVecRange0) panel8Mode1MatVecRange32) panel8Mode1MatVecRange64) panel8Mode1MatVecRange96) panel8Mode1MatVecRange128) row

theorem panel8Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode2MatVecRange0) panel8Mode2MatVecRange32) panel8Mode2MatVecRange64) panel8Mode2MatVecRange96) panel8Mode2MatVecRange128) row

theorem panel8Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode3MatVecRange0) panel8Mode3MatVecRange32) panel8Mode3MatVecRange64) panel8Mode3MatVecRange96) panel8Mode3MatVecRange128) row

theorem panel8Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode4MatVecRange0) panel8Mode4MatVecRange32) panel8Mode4MatVecRange64) panel8Mode4MatVecRange96) panel8Mode4MatVecRange128) row

theorem panel8Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode5MatVecRange0) panel8Mode5MatVecRange32) panel8Mode5MatVecRange64) panel8Mode5MatVecRange96) panel8Mode5MatVecRange128) row

theorem panel8Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode6MatVecRange0) panel8Mode6MatVecRange32) panel8Mode6MatVecRange64) panel8Mode6MatVecRange96) panel8Mode6MatVecRange128) row

theorem panel8Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode7MatVecRange0) panel8Mode7MatVecRange32) panel8Mode7MatVecRange64) panel8Mode7MatVecRange96) panel8Mode7MatVecRange128) row

theorem panel8Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode8MatVecRange0) panel8Mode8MatVecRange32) panel8Mode8MatVecRange64) panel8Mode8MatVecRange96) panel8Mode8MatVecRange128) row

theorem panel8Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode9MatVecRange0) panel8Mode9MatVecRange32) panel8Mode9MatVecRange64) panel8Mode9MatVecRange96) panel8Mode9MatVecRange128) row

theorem panel8Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode10MatVecRange0) panel8Mode10MatVecRange32) panel8Mode10MatVecRange64) panel8Mode10MatVecRange96) panel8Mode10MatVecRange128) row

theorem panel8Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode11MatVecRange0) panel8Mode11MatVecRange32) panel8Mode11MatVecRange64) panel8Mode11MatVecRange96) panel8Mode11MatVecRange128) row

theorem panel8Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode12MatVecRange0) panel8Mode12MatVecRange32) panel8Mode12MatVecRange64) panel8Mode12MatVecRange96) panel8Mode12MatVecRange128) row

theorem panel8Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode13MatVecRange0) panel8Mode13MatVecRange32) panel8Mode13MatVecRange64) panel8Mode13MatVecRange96) panel8Mode13MatVecRange128) row

theorem panel8Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode14MatVecRange0) panel8Mode14MatVecRange32) panel8Mode14MatVecRange64) panel8Mode14MatVecRange96) panel8Mode14MatVecRange128) row

theorem panel8Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode15MatVecRange0) panel8Mode15MatVecRange32) panel8Mode15MatVecRange64) panel8Mode15MatVecRange96) panel8Mode15MatVecRange128) row

theorem panel8Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode16MatVecRange0) panel8Mode16MatVecRange32) panel8Mode16MatVecRange64) panel8Mode16MatVecRange96) panel8Mode16MatVecRange128) row

theorem panel8Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode17MatVecRange0) panel8Mode17MatVecRange32) panel8Mode17MatVecRange64) panel8Mode17MatVecRange96) panel8Mode17MatVecRange128) row

theorem panel8Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode18MatVecRange0) panel8Mode18MatVecRange32) panel8Mode18MatVecRange64) panel8Mode18MatVecRange96) panel8Mode18MatVecRange128) row

theorem panel8Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode19MatVecRange0) panel8Mode19MatVecRange32) panel8Mode19MatVecRange64) panel8Mode19MatVecRange96) panel8Mode19MatVecRange128) row

theorem panel8Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode20MatVecRange0) panel8Mode20MatVecRange32) panel8Mode20MatVecRange64) panel8Mode20MatVecRange96) panel8Mode20MatVecRange128) row

theorem panel8Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode21MatVecRange0) panel8Mode21MatVecRange32) panel8Mode21MatVecRange64) panel8Mode21MatVecRange96) panel8Mode21MatVecRange128) row

theorem panel8Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode22MatVecRange0) panel8Mode22MatVecRange32) panel8Mode22MatVecRange64) panel8Mode22MatVecRange96) panel8Mode22MatVecRange128) row

theorem panel8Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode23MatVecRange0) panel8Mode23MatVecRange32) panel8Mode23MatVecRange64) panel8Mode23MatVecRange96) panel8Mode23MatVecRange128) row

theorem panel8Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode24MatVecRange0) panel8Mode24MatVecRange32) panel8Mode24MatVecRange64) panel8Mode24MatVecRange96) panel8Mode24MatVecRange128) row

theorem panel8Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode25MatVecRange0) panel8Mode25MatVecRange32) panel8Mode25MatVecRange64) panel8Mode25MatVecRange96) panel8Mode25MatVecRange128) row

theorem panel8Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode26MatVecRange0) panel8Mode26MatVecRange32) panel8Mode26MatVecRange64) panel8Mode26MatVecRange96) panel8Mode26MatVecRange128) row

theorem panel8Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode27MatVecRange0) panel8Mode27MatVecRange32) panel8Mode27MatVecRange64) panel8Mode27MatVecRange96) panel8Mode27MatVecRange128) row

theorem panel8Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode28MatVecRange0) panel8Mode28MatVecRange32) panel8Mode28MatVecRange64) panel8Mode28MatVecRange96) panel8Mode28MatVecRange128) row

theorem panel8Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode29MatVecRange0) panel8Mode29MatVecRange32) panel8Mode29MatVecRange64) panel8Mode29MatVecRange96) panel8Mode29MatVecRange128) row

theorem panel8Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode30MatVecRange0) panel8Mode30MatVecRange32) panel8Mode30MatVecRange64) panel8Mode30MatVecRange96) panel8Mode30MatVecRange128) row

theorem panel8Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode31MatVecRange0) panel8Mode31MatVecRange32) panel8Mode31MatVecRange64) panel8Mode31MatVecRange96) panel8Mode31MatVecRange128) row

theorem panel8Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode32MatVecRange0) panel8Mode32MatVecRange32) panel8Mode32MatVecRange64) panel8Mode32MatVecRange96) panel8Mode32MatVecRange128) row

theorem panel8Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode33MatVecRange0) panel8Mode33MatVecRange32) panel8Mode33MatVecRange64) panel8Mode33MatVecRange96) panel8Mode33MatVecRange128) row

theorem panel8Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode34MatVecRange0) panel8Mode34MatVecRange32) panel8Mode34MatVecRange64) panel8Mode34MatVecRange96) panel8Mode34MatVecRange128) row

theorem panel8Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode35MatVecRange0) panel8Mode35MatVecRange32) panel8Mode35MatVecRange64) panel8Mode35MatVecRange96) panel8Mode35MatVecRange128) row

theorem panel8Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode36MatVecRange0) panel8Mode36MatVecRange32) panel8Mode36MatVecRange64) panel8Mode36MatVecRange96) panel8Mode36MatVecRange128) row

theorem panel8Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode37MatVecRange0) panel8Mode37MatVecRange32) panel8Mode37MatVecRange64) panel8Mode37MatVecRange96) panel8Mode37MatVecRange128) row

theorem panel8Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode38MatVecRange0) panel8Mode38MatVecRange32) panel8Mode38MatVecRange64) panel8Mode38MatVecRange96) panel8Mode38MatVecRange128) row

theorem panel8Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode39MatVecRange0) panel8Mode39MatVecRange32) panel8Mode39MatVecRange64) panel8Mode39MatVecRange96) panel8Mode39MatVecRange128) row

theorem panel8Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode40MatVecRange0) panel8Mode40MatVecRange32) panel8Mode40MatVecRange64) panel8Mode40MatVecRange96) panel8Mode40MatVecRange128) row

theorem panel8Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode41MatVecRange0) panel8Mode41MatVecRange32) panel8Mode41MatVecRange64) panel8Mode41MatVecRange96) panel8Mode41MatVecRange128) row

theorem panel8Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode42MatVecRange0) panel8Mode42MatVecRange32) panel8Mode42MatVecRange64) panel8Mode42MatVecRange96) panel8Mode42MatVecRange128) row

theorem panel8Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode43MatVecRange0) panel8Mode43MatVecRange32) panel8Mode43MatVecRange64) panel8Mode43MatVecRange96) panel8Mode43MatVecRange128) row

theorem panel8Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode44MatVecRange0) panel8Mode44MatVecRange32) panel8Mode44MatVecRange64) panel8Mode44MatVecRange96) panel8Mode44MatVecRange128) row

theorem panel8Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode45MatVecRange0) panel8Mode45MatVecRange32) panel8Mode45MatVecRange64) panel8Mode45MatVecRange96) panel8Mode45MatVecRange128) row

theorem panel8Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode46MatVecRange0) panel8Mode46MatVecRange32) panel8Mode46MatVecRange64) panel8Mode46MatVecRange96) panel8Mode46MatVecRange128) row

theorem panel8Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel8MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel8MomentData.moments
        (P2RoundedFactorCheckpointData.panel8FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel8Mode47MatVecRange0) panel8Mode47MatVecRange32) panel8Mode47MatVecRange64) panel8Mode47MatVecRange96) panel8Mode47MatVecRange128) row

theorem panel8MomentData_correct :
    P2RoundedFactorCheckpointData.panel8MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel8FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel8DefectMoments_eq panel8ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel8Mode0MatVec_eq
      · exact panel8Mode2MatVec_eq
      · exact panel8Mode4MatVec_eq
      · exact panel8Mode6MatVec_eq
      · exact panel8Mode8MatVec_eq
      · exact panel8Mode10MatVec_eq
      · exact panel8Mode12MatVec_eq
      · exact panel8Mode14MatVec_eq
      · exact panel8Mode16MatVec_eq
      · exact panel8Mode18MatVec_eq
      · exact panel8Mode20MatVec_eq
      · exact panel8Mode22MatVec_eq
      · exact panel8Mode24MatVec_eq
      · exact panel8Mode26MatVec_eq
      · exact panel8Mode28MatVec_eq
      · exact panel8Mode30MatVec_eq
      · exact panel8Mode32MatVec_eq
      · exact panel8Mode34MatVec_eq
      · exact panel8Mode36MatVec_eq
      · exact panel8Mode38MatVec_eq
      · exact panel8Mode40MatVec_eq
      · exact panel8Mode42MatVec_eq
      · exact panel8Mode44MatVec_eq
      · exact panel8Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel8Mode1MatVec_eq
      · exact panel8Mode3MatVec_eq
      · exact panel8Mode5MatVec_eq
      · exact panel8Mode7MatVec_eq
      · exact panel8Mode9MatVec_eq
      · exact panel8Mode11MatVec_eq
      · exact panel8Mode13MatVec_eq
      · exact panel8Mode15MatVec_eq
      · exact panel8Mode17MatVec_eq
      · exact panel8Mode19MatVec_eq
      · exact panel8Mode21MatVec_eq
      · exact panel8Mode23MatVec_eq
      · exact panel8Mode25MatVec_eq
      · exact panel8Mode27MatVec_eq
      · exact panel8Mode29MatVec_eq
      · exact panel8Mode31MatVec_eq
      · exact panel8Mode33MatVec_eq
      · exact panel8Mode35MatVec_eq
      · exact panel8Mode37MatVec_eq
      · exact panel8Mode39MatVec_eq
      · exact panel8Mode41MatVec_eq
      · exact panel8Mode43MatVec_eq
      · exact panel8Mode45MatVec_eq
      · exact panel8Mode47MatVec_eq

end RHP2Bridge
