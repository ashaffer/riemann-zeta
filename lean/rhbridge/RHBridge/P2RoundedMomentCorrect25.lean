import RHBridge.P2RoundedFlatFactorCheckpoint25
import RHBridge.P2RoundedMomentLengths25
import RHBridge.P2RoundedMomentCheckpointCheck25_moments
import RHBridge.P2RoundedMomentCheckpointCheck25_mode0
import RHBridge.P2RoundedMomentCheckpointCheck25_mode1
import RHBridge.P2RoundedMomentCheckpointCheck25_mode2
import RHBridge.P2RoundedMomentCheckpointCheck25_mode3
import RHBridge.P2RoundedMomentCheckpointCheck25_mode4
import RHBridge.P2RoundedMomentCheckpointCheck25_mode5
import RHBridge.P2RoundedMomentCheckpointCheck25_mode6
import RHBridge.P2RoundedMomentCheckpointCheck25_mode7
import RHBridge.P2RoundedMomentCheckpointCheck25_mode8
import RHBridge.P2RoundedMomentCheckpointCheck25_mode9
import RHBridge.P2RoundedMomentCheckpointCheck25_mode10
import RHBridge.P2RoundedMomentCheckpointCheck25_mode11
import RHBridge.P2RoundedMomentCheckpointCheck25_mode12
import RHBridge.P2RoundedMomentCheckpointCheck25_mode13
import RHBridge.P2RoundedMomentCheckpointCheck25_mode14
import RHBridge.P2RoundedMomentCheckpointCheck25_mode15
import RHBridge.P2RoundedMomentCheckpointCheck25_mode16
import RHBridge.P2RoundedMomentCheckpointCheck25_mode17
import RHBridge.P2RoundedMomentCheckpointCheck25_mode18
import RHBridge.P2RoundedMomentCheckpointCheck25_mode19
import RHBridge.P2RoundedMomentCheckpointCheck25_mode20
import RHBridge.P2RoundedMomentCheckpointCheck25_mode21
import RHBridge.P2RoundedMomentCheckpointCheck25_mode22
import RHBridge.P2RoundedMomentCheckpointCheck25_mode23
import RHBridge.P2RoundedMomentCheckpointCheck25_mode24
import RHBridge.P2RoundedMomentCheckpointCheck25_mode25
import RHBridge.P2RoundedMomentCheckpointCheck25_mode26
import RHBridge.P2RoundedMomentCheckpointCheck25_mode27
import RHBridge.P2RoundedMomentCheckpointCheck25_mode28
import RHBridge.P2RoundedMomentCheckpointCheck25_mode29
import RHBridge.P2RoundedMomentCheckpointCheck25_mode30
import RHBridge.P2RoundedMomentCheckpointCheck25_mode31
import RHBridge.P2RoundedMomentCheckpointCheck25_mode32
import RHBridge.P2RoundedMomentCheckpointCheck25_mode33
import RHBridge.P2RoundedMomentCheckpointCheck25_mode34
import RHBridge.P2RoundedMomentCheckpointCheck25_mode35
import RHBridge.P2RoundedMomentCheckpointCheck25_mode36
import RHBridge.P2RoundedMomentCheckpointCheck25_mode37
import RHBridge.P2RoundedMomentCheckpointCheck25_mode38
import RHBridge.P2RoundedMomentCheckpointCheck25_mode39
import RHBridge.P2RoundedMomentCheckpointCheck25_mode40
import RHBridge.P2RoundedMomentCheckpointCheck25_mode41
import RHBridge.P2RoundedMomentCheckpointCheck25_mode42
import RHBridge.P2RoundedMomentCheckpointCheck25_mode43
import RHBridge.P2RoundedMomentCheckpointCheck25_mode44
import RHBridge.P2RoundedMomentCheckpointCheck25_mode45
import RHBridge.P2RoundedMomentCheckpointCheck25_mode46
import RHBridge.P2RoundedMomentCheckpointCheck25_mode47

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

theorem panel25DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel25FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25DefectMomentRange0) panel25DefectMomentRange64) panel25DefectMomentRange128) panel25DefectMomentRange192) panel25DefectMomentRange256) row

theorem panel25Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode0MatVecRange0) panel25Mode0MatVecRange32) panel25Mode0MatVecRange64) panel25Mode0MatVecRange96) panel25Mode0MatVecRange128) row

theorem panel25Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode1MatVecRange0) panel25Mode1MatVecRange32) panel25Mode1MatVecRange64) panel25Mode1MatVecRange96) panel25Mode1MatVecRange128) row

theorem panel25Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode2MatVecRange0) panel25Mode2MatVecRange32) panel25Mode2MatVecRange64) panel25Mode2MatVecRange96) panel25Mode2MatVecRange128) row

theorem panel25Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode3MatVecRange0) panel25Mode3MatVecRange32) panel25Mode3MatVecRange64) panel25Mode3MatVecRange96) panel25Mode3MatVecRange128) row

theorem panel25Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode4MatVecRange0) panel25Mode4MatVecRange32) panel25Mode4MatVecRange64) panel25Mode4MatVecRange96) panel25Mode4MatVecRange128) row

theorem panel25Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode5MatVecRange0) panel25Mode5MatVecRange32) panel25Mode5MatVecRange64) panel25Mode5MatVecRange96) panel25Mode5MatVecRange128) row

theorem panel25Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode6MatVecRange0) panel25Mode6MatVecRange32) panel25Mode6MatVecRange64) panel25Mode6MatVecRange96) panel25Mode6MatVecRange128) row

theorem panel25Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode7MatVecRange0) panel25Mode7MatVecRange32) panel25Mode7MatVecRange64) panel25Mode7MatVecRange96) panel25Mode7MatVecRange128) row

theorem panel25Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode8MatVecRange0) panel25Mode8MatVecRange32) panel25Mode8MatVecRange64) panel25Mode8MatVecRange96) panel25Mode8MatVecRange128) row

theorem panel25Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode9MatVecRange0) panel25Mode9MatVecRange32) panel25Mode9MatVecRange64) panel25Mode9MatVecRange96) panel25Mode9MatVecRange128) row

theorem panel25Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode10MatVecRange0) panel25Mode10MatVecRange32) panel25Mode10MatVecRange64) panel25Mode10MatVecRange96) panel25Mode10MatVecRange128) row

theorem panel25Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode11MatVecRange0) panel25Mode11MatVecRange32) panel25Mode11MatVecRange64) panel25Mode11MatVecRange96) panel25Mode11MatVecRange128) row

theorem panel25Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode12MatVecRange0) panel25Mode12MatVecRange32) panel25Mode12MatVecRange64) panel25Mode12MatVecRange96) panel25Mode12MatVecRange128) row

theorem panel25Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode13MatVecRange0) panel25Mode13MatVecRange32) panel25Mode13MatVecRange64) panel25Mode13MatVecRange96) panel25Mode13MatVecRange128) row

theorem panel25Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode14MatVecRange0) panel25Mode14MatVecRange32) panel25Mode14MatVecRange64) panel25Mode14MatVecRange96) panel25Mode14MatVecRange128) row

theorem panel25Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode15MatVecRange0) panel25Mode15MatVecRange32) panel25Mode15MatVecRange64) panel25Mode15MatVecRange96) panel25Mode15MatVecRange128) row

theorem panel25Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode16MatVecRange0) panel25Mode16MatVecRange32) panel25Mode16MatVecRange64) panel25Mode16MatVecRange96) panel25Mode16MatVecRange128) row

theorem panel25Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode17MatVecRange0) panel25Mode17MatVecRange32) panel25Mode17MatVecRange64) panel25Mode17MatVecRange96) panel25Mode17MatVecRange128) row

theorem panel25Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode18MatVecRange0) panel25Mode18MatVecRange32) panel25Mode18MatVecRange64) panel25Mode18MatVecRange96) panel25Mode18MatVecRange128) row

theorem panel25Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode19MatVecRange0) panel25Mode19MatVecRange32) panel25Mode19MatVecRange64) panel25Mode19MatVecRange96) panel25Mode19MatVecRange128) row

theorem panel25Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode20MatVecRange0) panel25Mode20MatVecRange32) panel25Mode20MatVecRange64) panel25Mode20MatVecRange96) panel25Mode20MatVecRange128) row

theorem panel25Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode21MatVecRange0) panel25Mode21MatVecRange32) panel25Mode21MatVecRange64) panel25Mode21MatVecRange96) panel25Mode21MatVecRange128) row

theorem panel25Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode22MatVecRange0) panel25Mode22MatVecRange32) panel25Mode22MatVecRange64) panel25Mode22MatVecRange96) panel25Mode22MatVecRange128) row

theorem panel25Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode23MatVecRange0) panel25Mode23MatVecRange32) panel25Mode23MatVecRange64) panel25Mode23MatVecRange96) panel25Mode23MatVecRange128) row

theorem panel25Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode24MatVecRange0) panel25Mode24MatVecRange32) panel25Mode24MatVecRange64) panel25Mode24MatVecRange96) panel25Mode24MatVecRange128) row

theorem panel25Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode25MatVecRange0) panel25Mode25MatVecRange32) panel25Mode25MatVecRange64) panel25Mode25MatVecRange96) panel25Mode25MatVecRange128) row

theorem panel25Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode26MatVecRange0) panel25Mode26MatVecRange32) panel25Mode26MatVecRange64) panel25Mode26MatVecRange96) panel25Mode26MatVecRange128) row

theorem panel25Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode27MatVecRange0) panel25Mode27MatVecRange32) panel25Mode27MatVecRange64) panel25Mode27MatVecRange96) panel25Mode27MatVecRange128) row

theorem panel25Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode28MatVecRange0) panel25Mode28MatVecRange32) panel25Mode28MatVecRange64) panel25Mode28MatVecRange96) panel25Mode28MatVecRange128) row

theorem panel25Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode29MatVecRange0) panel25Mode29MatVecRange32) panel25Mode29MatVecRange64) panel25Mode29MatVecRange96) panel25Mode29MatVecRange128) row

theorem panel25Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode30MatVecRange0) panel25Mode30MatVecRange32) panel25Mode30MatVecRange64) panel25Mode30MatVecRange96) panel25Mode30MatVecRange128) row

theorem panel25Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode31MatVecRange0) panel25Mode31MatVecRange32) panel25Mode31MatVecRange64) panel25Mode31MatVecRange96) panel25Mode31MatVecRange128) row

theorem panel25Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode32MatVecRange0) panel25Mode32MatVecRange32) panel25Mode32MatVecRange64) panel25Mode32MatVecRange96) panel25Mode32MatVecRange128) row

theorem panel25Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode33MatVecRange0) panel25Mode33MatVecRange32) panel25Mode33MatVecRange64) panel25Mode33MatVecRange96) panel25Mode33MatVecRange128) row

theorem panel25Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode34MatVecRange0) panel25Mode34MatVecRange32) panel25Mode34MatVecRange64) panel25Mode34MatVecRange96) panel25Mode34MatVecRange128) row

theorem panel25Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode35MatVecRange0) panel25Mode35MatVecRange32) panel25Mode35MatVecRange64) panel25Mode35MatVecRange96) panel25Mode35MatVecRange128) row

theorem panel25Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode36MatVecRange0) panel25Mode36MatVecRange32) panel25Mode36MatVecRange64) panel25Mode36MatVecRange96) panel25Mode36MatVecRange128) row

theorem panel25Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode37MatVecRange0) panel25Mode37MatVecRange32) panel25Mode37MatVecRange64) panel25Mode37MatVecRange96) panel25Mode37MatVecRange128) row

theorem panel25Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode38MatVecRange0) panel25Mode38MatVecRange32) panel25Mode38MatVecRange64) panel25Mode38MatVecRange96) panel25Mode38MatVecRange128) row

theorem panel25Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode39MatVecRange0) panel25Mode39MatVecRange32) panel25Mode39MatVecRange64) panel25Mode39MatVecRange96) panel25Mode39MatVecRange128) row

theorem panel25Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode40MatVecRange0) panel25Mode40MatVecRange32) panel25Mode40MatVecRange64) panel25Mode40MatVecRange96) panel25Mode40MatVecRange128) row

theorem panel25Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode41MatVecRange0) panel25Mode41MatVecRange32) panel25Mode41MatVecRange64) panel25Mode41MatVecRange96) panel25Mode41MatVecRange128) row

theorem panel25Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode42MatVecRange0) panel25Mode42MatVecRange32) panel25Mode42MatVecRange64) panel25Mode42MatVecRange96) panel25Mode42MatVecRange128) row

theorem panel25Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode43MatVecRange0) panel25Mode43MatVecRange32) panel25Mode43MatVecRange64) panel25Mode43MatVecRange96) panel25Mode43MatVecRange128) row

theorem panel25Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode44MatVecRange0) panel25Mode44MatVecRange32) panel25Mode44MatVecRange64) panel25Mode44MatVecRange96) panel25Mode44MatVecRange128) row

theorem panel25Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode45MatVecRange0) panel25Mode45MatVecRange32) panel25Mode45MatVecRange64) panel25Mode45MatVecRange96) panel25Mode45MatVecRange128) row

theorem panel25Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode46MatVecRange0) panel25Mode46MatVecRange32) panel25Mode46MatVecRange64) panel25Mode46MatVecRange96) panel25Mode46MatVecRange128) row

theorem panel25Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel25MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel25MomentData.moments
        (P2RoundedFactorCheckpointData.panel25FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel25Mode47MatVecRange0) panel25Mode47MatVecRange32) panel25Mode47MatVecRange64) panel25Mode47MatVecRange96) panel25Mode47MatVecRange128) row

theorem panel25MomentData_correct :
    P2RoundedFactorCheckpointData.panel25MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel25FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel25DefectMoments_eq panel25ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel25Mode0MatVec_eq
      · exact panel25Mode2MatVec_eq
      · exact panel25Mode4MatVec_eq
      · exact panel25Mode6MatVec_eq
      · exact panel25Mode8MatVec_eq
      · exact panel25Mode10MatVec_eq
      · exact panel25Mode12MatVec_eq
      · exact panel25Mode14MatVec_eq
      · exact panel25Mode16MatVec_eq
      · exact panel25Mode18MatVec_eq
      · exact panel25Mode20MatVec_eq
      · exact panel25Mode22MatVec_eq
      · exact panel25Mode24MatVec_eq
      · exact panel25Mode26MatVec_eq
      · exact panel25Mode28MatVec_eq
      · exact panel25Mode30MatVec_eq
      · exact panel25Mode32MatVec_eq
      · exact panel25Mode34MatVec_eq
      · exact panel25Mode36MatVec_eq
      · exact panel25Mode38MatVec_eq
      · exact panel25Mode40MatVec_eq
      · exact panel25Mode42MatVec_eq
      · exact panel25Mode44MatVec_eq
      · exact panel25Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel25Mode1MatVec_eq
      · exact panel25Mode3MatVec_eq
      · exact panel25Mode5MatVec_eq
      · exact panel25Mode7MatVec_eq
      · exact panel25Mode9MatVec_eq
      · exact panel25Mode11MatVec_eq
      · exact panel25Mode13MatVec_eq
      · exact panel25Mode15MatVec_eq
      · exact panel25Mode17MatVec_eq
      · exact panel25Mode19MatVec_eq
      · exact panel25Mode21MatVec_eq
      · exact panel25Mode23MatVec_eq
      · exact panel25Mode25MatVec_eq
      · exact panel25Mode27MatVec_eq
      · exact panel25Mode29MatVec_eq
      · exact panel25Mode31MatVec_eq
      · exact panel25Mode33MatVec_eq
      · exact panel25Mode35MatVec_eq
      · exact panel25Mode37MatVec_eq
      · exact panel25Mode39MatVec_eq
      · exact panel25Mode41MatVec_eq
      · exact panel25Mode43MatVec_eq
      · exact panel25Mode45MatVec_eq
      · exact panel25Mode47MatVec_eq

end RHP2Bridge
