import RHBridge.P2RoundedFlatFactorCheckpoint18
import RHBridge.P2RoundedMomentLengths18
import RHBridge.P2RoundedMomentCheckpointCheck18_moments
import RHBridge.P2RoundedMomentCheckpointCheck18_mode0
import RHBridge.P2RoundedMomentCheckpointCheck18_mode1
import RHBridge.P2RoundedMomentCheckpointCheck18_mode2
import RHBridge.P2RoundedMomentCheckpointCheck18_mode3
import RHBridge.P2RoundedMomentCheckpointCheck18_mode4
import RHBridge.P2RoundedMomentCheckpointCheck18_mode5
import RHBridge.P2RoundedMomentCheckpointCheck18_mode6
import RHBridge.P2RoundedMomentCheckpointCheck18_mode7
import RHBridge.P2RoundedMomentCheckpointCheck18_mode8
import RHBridge.P2RoundedMomentCheckpointCheck18_mode9
import RHBridge.P2RoundedMomentCheckpointCheck18_mode10
import RHBridge.P2RoundedMomentCheckpointCheck18_mode11
import RHBridge.P2RoundedMomentCheckpointCheck18_mode12
import RHBridge.P2RoundedMomentCheckpointCheck18_mode13
import RHBridge.P2RoundedMomentCheckpointCheck18_mode14
import RHBridge.P2RoundedMomentCheckpointCheck18_mode15
import RHBridge.P2RoundedMomentCheckpointCheck18_mode16
import RHBridge.P2RoundedMomentCheckpointCheck18_mode17
import RHBridge.P2RoundedMomentCheckpointCheck18_mode18
import RHBridge.P2RoundedMomentCheckpointCheck18_mode19
import RHBridge.P2RoundedMomentCheckpointCheck18_mode20
import RHBridge.P2RoundedMomentCheckpointCheck18_mode21
import RHBridge.P2RoundedMomentCheckpointCheck18_mode22
import RHBridge.P2RoundedMomentCheckpointCheck18_mode23
import RHBridge.P2RoundedMomentCheckpointCheck18_mode24
import RHBridge.P2RoundedMomentCheckpointCheck18_mode25
import RHBridge.P2RoundedMomentCheckpointCheck18_mode26
import RHBridge.P2RoundedMomentCheckpointCheck18_mode27
import RHBridge.P2RoundedMomentCheckpointCheck18_mode28
import RHBridge.P2RoundedMomentCheckpointCheck18_mode29
import RHBridge.P2RoundedMomentCheckpointCheck18_mode30
import RHBridge.P2RoundedMomentCheckpointCheck18_mode31
import RHBridge.P2RoundedMomentCheckpointCheck18_mode32
import RHBridge.P2RoundedMomentCheckpointCheck18_mode33
import RHBridge.P2RoundedMomentCheckpointCheck18_mode34
import RHBridge.P2RoundedMomentCheckpointCheck18_mode35
import RHBridge.P2RoundedMomentCheckpointCheck18_mode36
import RHBridge.P2RoundedMomentCheckpointCheck18_mode37
import RHBridge.P2RoundedMomentCheckpointCheck18_mode38
import RHBridge.P2RoundedMomentCheckpointCheck18_mode39
import RHBridge.P2RoundedMomentCheckpointCheck18_mode40
import RHBridge.P2RoundedMomentCheckpointCheck18_mode41
import RHBridge.P2RoundedMomentCheckpointCheck18_mode42
import RHBridge.P2RoundedMomentCheckpointCheck18_mode43
import RHBridge.P2RoundedMomentCheckpointCheck18_mode44
import RHBridge.P2RoundedMomentCheckpointCheck18_mode45
import RHBridge.P2RoundedMomentCheckpointCheck18_mode46
import RHBridge.P2RoundedMomentCheckpointCheck18_mode47

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

theorem panel18DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel18FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18DefectMomentRange0) panel18DefectMomentRange64) panel18DefectMomentRange128) panel18DefectMomentRange192) panel18DefectMomentRange256) row

theorem panel18Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode0MatVecRange0) panel18Mode0MatVecRange32) panel18Mode0MatVecRange64) panel18Mode0MatVecRange96) panel18Mode0MatVecRange128) row

theorem panel18Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode1MatVecRange0) panel18Mode1MatVecRange32) panel18Mode1MatVecRange64) panel18Mode1MatVecRange96) panel18Mode1MatVecRange128) row

theorem panel18Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode2MatVecRange0) panel18Mode2MatVecRange32) panel18Mode2MatVecRange64) panel18Mode2MatVecRange96) panel18Mode2MatVecRange128) row

theorem panel18Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode3MatVecRange0) panel18Mode3MatVecRange32) panel18Mode3MatVecRange64) panel18Mode3MatVecRange96) panel18Mode3MatVecRange128) row

theorem panel18Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode4MatVecRange0) panel18Mode4MatVecRange32) panel18Mode4MatVecRange64) panel18Mode4MatVecRange96) panel18Mode4MatVecRange128) row

theorem panel18Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode5MatVecRange0) panel18Mode5MatVecRange32) panel18Mode5MatVecRange64) panel18Mode5MatVecRange96) panel18Mode5MatVecRange128) row

theorem panel18Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode6MatVecRange0) panel18Mode6MatVecRange32) panel18Mode6MatVecRange64) panel18Mode6MatVecRange96) panel18Mode6MatVecRange128) row

theorem panel18Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode7MatVecRange0) panel18Mode7MatVecRange32) panel18Mode7MatVecRange64) panel18Mode7MatVecRange96) panel18Mode7MatVecRange128) row

theorem panel18Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode8MatVecRange0) panel18Mode8MatVecRange32) panel18Mode8MatVecRange64) panel18Mode8MatVecRange96) panel18Mode8MatVecRange128) row

theorem panel18Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode9MatVecRange0) panel18Mode9MatVecRange32) panel18Mode9MatVecRange64) panel18Mode9MatVecRange96) panel18Mode9MatVecRange128) row

theorem panel18Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode10MatVecRange0) panel18Mode10MatVecRange32) panel18Mode10MatVecRange64) panel18Mode10MatVecRange96) panel18Mode10MatVecRange128) row

theorem panel18Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode11MatVecRange0) panel18Mode11MatVecRange32) panel18Mode11MatVecRange64) panel18Mode11MatVecRange96) panel18Mode11MatVecRange128) row

theorem panel18Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode12MatVecRange0) panel18Mode12MatVecRange32) panel18Mode12MatVecRange64) panel18Mode12MatVecRange96) panel18Mode12MatVecRange128) row

theorem panel18Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode13MatVecRange0) panel18Mode13MatVecRange32) panel18Mode13MatVecRange64) panel18Mode13MatVecRange96) panel18Mode13MatVecRange128) row

theorem panel18Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode14MatVecRange0) panel18Mode14MatVecRange32) panel18Mode14MatVecRange64) panel18Mode14MatVecRange96) panel18Mode14MatVecRange128) row

theorem panel18Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode15MatVecRange0) panel18Mode15MatVecRange32) panel18Mode15MatVecRange64) panel18Mode15MatVecRange96) panel18Mode15MatVecRange128) row

theorem panel18Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode16MatVecRange0) panel18Mode16MatVecRange32) panel18Mode16MatVecRange64) panel18Mode16MatVecRange96) panel18Mode16MatVecRange128) row

theorem panel18Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode17MatVecRange0) panel18Mode17MatVecRange32) panel18Mode17MatVecRange64) panel18Mode17MatVecRange96) panel18Mode17MatVecRange128) row

theorem panel18Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode18MatVecRange0) panel18Mode18MatVecRange32) panel18Mode18MatVecRange64) panel18Mode18MatVecRange96) panel18Mode18MatVecRange128) row

theorem panel18Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode19MatVecRange0) panel18Mode19MatVecRange32) panel18Mode19MatVecRange64) panel18Mode19MatVecRange96) panel18Mode19MatVecRange128) row

theorem panel18Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode20MatVecRange0) panel18Mode20MatVecRange32) panel18Mode20MatVecRange64) panel18Mode20MatVecRange96) panel18Mode20MatVecRange128) row

theorem panel18Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode21MatVecRange0) panel18Mode21MatVecRange32) panel18Mode21MatVecRange64) panel18Mode21MatVecRange96) panel18Mode21MatVecRange128) row

theorem panel18Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode22MatVecRange0) panel18Mode22MatVecRange32) panel18Mode22MatVecRange64) panel18Mode22MatVecRange96) panel18Mode22MatVecRange128) row

theorem panel18Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode23MatVecRange0) panel18Mode23MatVecRange32) panel18Mode23MatVecRange64) panel18Mode23MatVecRange96) panel18Mode23MatVecRange128) row

theorem panel18Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode24MatVecRange0) panel18Mode24MatVecRange32) panel18Mode24MatVecRange64) panel18Mode24MatVecRange96) panel18Mode24MatVecRange128) row

theorem panel18Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode25MatVecRange0) panel18Mode25MatVecRange32) panel18Mode25MatVecRange64) panel18Mode25MatVecRange96) panel18Mode25MatVecRange128) row

theorem panel18Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode26MatVecRange0) panel18Mode26MatVecRange32) panel18Mode26MatVecRange64) panel18Mode26MatVecRange96) panel18Mode26MatVecRange128) row

theorem panel18Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode27MatVecRange0) panel18Mode27MatVecRange32) panel18Mode27MatVecRange64) panel18Mode27MatVecRange96) panel18Mode27MatVecRange128) row

theorem panel18Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode28MatVecRange0) panel18Mode28MatVecRange32) panel18Mode28MatVecRange64) panel18Mode28MatVecRange96) panel18Mode28MatVecRange128) row

theorem panel18Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode29MatVecRange0) panel18Mode29MatVecRange32) panel18Mode29MatVecRange64) panel18Mode29MatVecRange96) panel18Mode29MatVecRange128) row

theorem panel18Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode30MatVecRange0) panel18Mode30MatVecRange32) panel18Mode30MatVecRange64) panel18Mode30MatVecRange96) panel18Mode30MatVecRange128) row

theorem panel18Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode31MatVecRange0) panel18Mode31MatVecRange32) panel18Mode31MatVecRange64) panel18Mode31MatVecRange96) panel18Mode31MatVecRange128) row

theorem panel18Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode32MatVecRange0) panel18Mode32MatVecRange32) panel18Mode32MatVecRange64) panel18Mode32MatVecRange96) panel18Mode32MatVecRange128) row

theorem panel18Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode33MatVecRange0) panel18Mode33MatVecRange32) panel18Mode33MatVecRange64) panel18Mode33MatVecRange96) panel18Mode33MatVecRange128) row

theorem panel18Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode34MatVecRange0) panel18Mode34MatVecRange32) panel18Mode34MatVecRange64) panel18Mode34MatVecRange96) panel18Mode34MatVecRange128) row

theorem panel18Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode35MatVecRange0) panel18Mode35MatVecRange32) panel18Mode35MatVecRange64) panel18Mode35MatVecRange96) panel18Mode35MatVecRange128) row

theorem panel18Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode36MatVecRange0) panel18Mode36MatVecRange32) panel18Mode36MatVecRange64) panel18Mode36MatVecRange96) panel18Mode36MatVecRange128) row

theorem panel18Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode37MatVecRange0) panel18Mode37MatVecRange32) panel18Mode37MatVecRange64) panel18Mode37MatVecRange96) panel18Mode37MatVecRange128) row

theorem panel18Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode38MatVecRange0) panel18Mode38MatVecRange32) panel18Mode38MatVecRange64) panel18Mode38MatVecRange96) panel18Mode38MatVecRange128) row

theorem panel18Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode39MatVecRange0) panel18Mode39MatVecRange32) panel18Mode39MatVecRange64) panel18Mode39MatVecRange96) panel18Mode39MatVecRange128) row

theorem panel18Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode40MatVecRange0) panel18Mode40MatVecRange32) panel18Mode40MatVecRange64) panel18Mode40MatVecRange96) panel18Mode40MatVecRange128) row

theorem panel18Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode41MatVecRange0) panel18Mode41MatVecRange32) panel18Mode41MatVecRange64) panel18Mode41MatVecRange96) panel18Mode41MatVecRange128) row

theorem panel18Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode42MatVecRange0) panel18Mode42MatVecRange32) panel18Mode42MatVecRange64) panel18Mode42MatVecRange96) panel18Mode42MatVecRange128) row

theorem panel18Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode43MatVecRange0) panel18Mode43MatVecRange32) panel18Mode43MatVecRange64) panel18Mode43MatVecRange96) panel18Mode43MatVecRange128) row

theorem panel18Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode44MatVecRange0) panel18Mode44MatVecRange32) panel18Mode44MatVecRange64) panel18Mode44MatVecRange96) panel18Mode44MatVecRange128) row

theorem panel18Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode45MatVecRange0) panel18Mode45MatVecRange32) panel18Mode45MatVecRange64) panel18Mode45MatVecRange96) panel18Mode45MatVecRange128) row

theorem panel18Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode46MatVecRange0) panel18Mode46MatVecRange32) panel18Mode46MatVecRange64) panel18Mode46MatVecRange96) panel18Mode46MatVecRange128) row

theorem panel18Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel18MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel18MomentData.moments
        (P2RoundedFactorCheckpointData.panel18FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel18Mode47MatVecRange0) panel18Mode47MatVecRange32) panel18Mode47MatVecRange64) panel18Mode47MatVecRange96) panel18Mode47MatVecRange128) row

theorem panel18MomentData_correct :
    P2RoundedFactorCheckpointData.panel18MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel18FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel18DefectMoments_eq panel18ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel18Mode0MatVec_eq
      · exact panel18Mode2MatVec_eq
      · exact panel18Mode4MatVec_eq
      · exact panel18Mode6MatVec_eq
      · exact panel18Mode8MatVec_eq
      · exact panel18Mode10MatVec_eq
      · exact panel18Mode12MatVec_eq
      · exact panel18Mode14MatVec_eq
      · exact panel18Mode16MatVec_eq
      · exact panel18Mode18MatVec_eq
      · exact panel18Mode20MatVec_eq
      · exact panel18Mode22MatVec_eq
      · exact panel18Mode24MatVec_eq
      · exact panel18Mode26MatVec_eq
      · exact panel18Mode28MatVec_eq
      · exact panel18Mode30MatVec_eq
      · exact panel18Mode32MatVec_eq
      · exact panel18Mode34MatVec_eq
      · exact panel18Mode36MatVec_eq
      · exact panel18Mode38MatVec_eq
      · exact panel18Mode40MatVec_eq
      · exact panel18Mode42MatVec_eq
      · exact panel18Mode44MatVec_eq
      · exact panel18Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel18Mode1MatVec_eq
      · exact panel18Mode3MatVec_eq
      · exact panel18Mode5MatVec_eq
      · exact panel18Mode7MatVec_eq
      · exact panel18Mode9MatVec_eq
      · exact panel18Mode11MatVec_eq
      · exact panel18Mode13MatVec_eq
      · exact panel18Mode15MatVec_eq
      · exact panel18Mode17MatVec_eq
      · exact panel18Mode19MatVec_eq
      · exact panel18Mode21MatVec_eq
      · exact panel18Mode23MatVec_eq
      · exact panel18Mode25MatVec_eq
      · exact panel18Mode27MatVec_eq
      · exact panel18Mode29MatVec_eq
      · exact panel18Mode31MatVec_eq
      · exact panel18Mode33MatVec_eq
      · exact panel18Mode35MatVec_eq
      · exact panel18Mode37MatVec_eq
      · exact panel18Mode39MatVec_eq
      · exact panel18Mode41MatVec_eq
      · exact panel18Mode43MatVec_eq
      · exact panel18Mode45MatVec_eq
      · exact panel18Mode47MatVec_eq

end RHP2Bridge
