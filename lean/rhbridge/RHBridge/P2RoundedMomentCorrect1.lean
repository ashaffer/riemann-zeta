import RHBridge.P2RoundedFlatFactorCheckpoint1
import RHBridge.P2RoundedMomentLengths1
import RHBridge.P2RoundedMomentCheckpointCheck1_moments
import RHBridge.P2RoundedMomentCheckpointCheck1_mode0
import RHBridge.P2RoundedMomentCheckpointCheck1_mode1
import RHBridge.P2RoundedMomentCheckpointCheck1_mode2
import RHBridge.P2RoundedMomentCheckpointCheck1_mode3
import RHBridge.P2RoundedMomentCheckpointCheck1_mode4
import RHBridge.P2RoundedMomentCheckpointCheck1_mode5
import RHBridge.P2RoundedMomentCheckpointCheck1_mode6
import RHBridge.P2RoundedMomentCheckpointCheck1_mode7
import RHBridge.P2RoundedMomentCheckpointCheck1_mode8
import RHBridge.P2RoundedMomentCheckpointCheck1_mode9
import RHBridge.P2RoundedMomentCheckpointCheck1_mode10
import RHBridge.P2RoundedMomentCheckpointCheck1_mode11
import RHBridge.P2RoundedMomentCheckpointCheck1_mode12
import RHBridge.P2RoundedMomentCheckpointCheck1_mode13
import RHBridge.P2RoundedMomentCheckpointCheck1_mode14
import RHBridge.P2RoundedMomentCheckpointCheck1_mode15
import RHBridge.P2RoundedMomentCheckpointCheck1_mode16
import RHBridge.P2RoundedMomentCheckpointCheck1_mode17
import RHBridge.P2RoundedMomentCheckpointCheck1_mode18
import RHBridge.P2RoundedMomentCheckpointCheck1_mode19
import RHBridge.P2RoundedMomentCheckpointCheck1_mode20
import RHBridge.P2RoundedMomentCheckpointCheck1_mode21
import RHBridge.P2RoundedMomentCheckpointCheck1_mode22
import RHBridge.P2RoundedMomentCheckpointCheck1_mode23
import RHBridge.P2RoundedMomentCheckpointCheck1_mode24
import RHBridge.P2RoundedMomentCheckpointCheck1_mode25
import RHBridge.P2RoundedMomentCheckpointCheck1_mode26
import RHBridge.P2RoundedMomentCheckpointCheck1_mode27
import RHBridge.P2RoundedMomentCheckpointCheck1_mode28
import RHBridge.P2RoundedMomentCheckpointCheck1_mode29
import RHBridge.P2RoundedMomentCheckpointCheck1_mode30
import RHBridge.P2RoundedMomentCheckpointCheck1_mode31
import RHBridge.P2RoundedMomentCheckpointCheck1_mode32
import RHBridge.P2RoundedMomentCheckpointCheck1_mode33
import RHBridge.P2RoundedMomentCheckpointCheck1_mode34
import RHBridge.P2RoundedMomentCheckpointCheck1_mode35
import RHBridge.P2RoundedMomentCheckpointCheck1_mode36
import RHBridge.P2RoundedMomentCheckpointCheck1_mode37
import RHBridge.P2RoundedMomentCheckpointCheck1_mode38
import RHBridge.P2RoundedMomentCheckpointCheck1_mode39
import RHBridge.P2RoundedMomentCheckpointCheck1_mode40
import RHBridge.P2RoundedMomentCheckpointCheck1_mode41
import RHBridge.P2RoundedMomentCheckpointCheck1_mode42
import RHBridge.P2RoundedMomentCheckpointCheck1_mode43
import RHBridge.P2RoundedMomentCheckpointCheck1_mode44
import RHBridge.P2RoundedMomentCheckpointCheck1_mode45
import RHBridge.P2RoundedMomentCheckpointCheck1_mode46
import RHBridge.P2RoundedMomentCheckpointCheck1_mode47

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

theorem panel1DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel1FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1DefectMomentRange0) panel1DefectMomentRange64) panel1DefectMomentRange128) panel1DefectMomentRange192) panel1DefectMomentRange256) row

theorem panel1Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode0MatVecRange0) panel1Mode0MatVecRange32) panel1Mode0MatVecRange64) panel1Mode0MatVecRange96) panel1Mode0MatVecRange128) row

theorem panel1Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode1MatVecRange0) panel1Mode1MatVecRange32) panel1Mode1MatVecRange64) panel1Mode1MatVecRange96) panel1Mode1MatVecRange128) row

theorem panel1Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode2MatVecRange0) panel1Mode2MatVecRange32) panel1Mode2MatVecRange64) panel1Mode2MatVecRange96) panel1Mode2MatVecRange128) row

theorem panel1Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode3MatVecRange0) panel1Mode3MatVecRange32) panel1Mode3MatVecRange64) panel1Mode3MatVecRange96) panel1Mode3MatVecRange128) row

theorem panel1Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode4MatVecRange0) panel1Mode4MatVecRange32) panel1Mode4MatVecRange64) panel1Mode4MatVecRange96) panel1Mode4MatVecRange128) row

theorem panel1Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode5MatVecRange0) panel1Mode5MatVecRange32) panel1Mode5MatVecRange64) panel1Mode5MatVecRange96) panel1Mode5MatVecRange128) row

theorem panel1Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode6MatVecRange0) panel1Mode6MatVecRange32) panel1Mode6MatVecRange64) panel1Mode6MatVecRange96) panel1Mode6MatVecRange128) row

theorem panel1Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode7MatVecRange0) panel1Mode7MatVecRange32) panel1Mode7MatVecRange64) panel1Mode7MatVecRange96) panel1Mode7MatVecRange128) row

theorem panel1Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode8MatVecRange0) panel1Mode8MatVecRange32) panel1Mode8MatVecRange64) panel1Mode8MatVecRange96) panel1Mode8MatVecRange128) row

theorem panel1Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode9MatVecRange0) panel1Mode9MatVecRange32) panel1Mode9MatVecRange64) panel1Mode9MatVecRange96) panel1Mode9MatVecRange128) row

theorem panel1Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode10MatVecRange0) panel1Mode10MatVecRange32) panel1Mode10MatVecRange64) panel1Mode10MatVecRange96) panel1Mode10MatVecRange128) row

theorem panel1Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode11MatVecRange0) panel1Mode11MatVecRange32) panel1Mode11MatVecRange64) panel1Mode11MatVecRange96) panel1Mode11MatVecRange128) row

theorem panel1Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode12MatVecRange0) panel1Mode12MatVecRange32) panel1Mode12MatVecRange64) panel1Mode12MatVecRange96) panel1Mode12MatVecRange128) row

theorem panel1Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode13MatVecRange0) panel1Mode13MatVecRange32) panel1Mode13MatVecRange64) panel1Mode13MatVecRange96) panel1Mode13MatVecRange128) row

theorem panel1Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode14MatVecRange0) panel1Mode14MatVecRange32) panel1Mode14MatVecRange64) panel1Mode14MatVecRange96) panel1Mode14MatVecRange128) row

theorem panel1Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode15MatVecRange0) panel1Mode15MatVecRange32) panel1Mode15MatVecRange64) panel1Mode15MatVecRange96) panel1Mode15MatVecRange128) row

theorem panel1Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode16MatVecRange0) panel1Mode16MatVecRange32) panel1Mode16MatVecRange64) panel1Mode16MatVecRange96) panel1Mode16MatVecRange128) row

theorem panel1Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode17MatVecRange0) panel1Mode17MatVecRange32) panel1Mode17MatVecRange64) panel1Mode17MatVecRange96) panel1Mode17MatVecRange128) row

theorem panel1Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode18MatVecRange0) panel1Mode18MatVecRange32) panel1Mode18MatVecRange64) panel1Mode18MatVecRange96) panel1Mode18MatVecRange128) row

theorem panel1Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode19MatVecRange0) panel1Mode19MatVecRange32) panel1Mode19MatVecRange64) panel1Mode19MatVecRange96) panel1Mode19MatVecRange128) row

theorem panel1Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode20MatVecRange0) panel1Mode20MatVecRange32) panel1Mode20MatVecRange64) panel1Mode20MatVecRange96) panel1Mode20MatVecRange128) row

theorem panel1Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode21MatVecRange0) panel1Mode21MatVecRange32) panel1Mode21MatVecRange64) panel1Mode21MatVecRange96) panel1Mode21MatVecRange128) row

theorem panel1Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode22MatVecRange0) panel1Mode22MatVecRange32) panel1Mode22MatVecRange64) panel1Mode22MatVecRange96) panel1Mode22MatVecRange128) row

theorem panel1Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode23MatVecRange0) panel1Mode23MatVecRange32) panel1Mode23MatVecRange64) panel1Mode23MatVecRange96) panel1Mode23MatVecRange128) row

theorem panel1Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode24MatVecRange0) panel1Mode24MatVecRange32) panel1Mode24MatVecRange64) panel1Mode24MatVecRange96) panel1Mode24MatVecRange128) row

theorem panel1Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode25MatVecRange0) panel1Mode25MatVecRange32) panel1Mode25MatVecRange64) panel1Mode25MatVecRange96) panel1Mode25MatVecRange128) row

theorem panel1Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode26MatVecRange0) panel1Mode26MatVecRange32) panel1Mode26MatVecRange64) panel1Mode26MatVecRange96) panel1Mode26MatVecRange128) row

theorem panel1Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode27MatVecRange0) panel1Mode27MatVecRange32) panel1Mode27MatVecRange64) panel1Mode27MatVecRange96) panel1Mode27MatVecRange128) row

theorem panel1Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode28MatVecRange0) panel1Mode28MatVecRange32) panel1Mode28MatVecRange64) panel1Mode28MatVecRange96) panel1Mode28MatVecRange128) row

theorem panel1Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode29MatVecRange0) panel1Mode29MatVecRange32) panel1Mode29MatVecRange64) panel1Mode29MatVecRange96) panel1Mode29MatVecRange128) row

theorem panel1Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode30MatVecRange0) panel1Mode30MatVecRange32) panel1Mode30MatVecRange64) panel1Mode30MatVecRange96) panel1Mode30MatVecRange128) row

theorem panel1Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode31MatVecRange0) panel1Mode31MatVecRange32) panel1Mode31MatVecRange64) panel1Mode31MatVecRange96) panel1Mode31MatVecRange128) row

theorem panel1Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode32MatVecRange0) panel1Mode32MatVecRange32) panel1Mode32MatVecRange64) panel1Mode32MatVecRange96) panel1Mode32MatVecRange128) row

theorem panel1Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode33MatVecRange0) panel1Mode33MatVecRange32) panel1Mode33MatVecRange64) panel1Mode33MatVecRange96) panel1Mode33MatVecRange128) row

theorem panel1Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode34MatVecRange0) panel1Mode34MatVecRange32) panel1Mode34MatVecRange64) panel1Mode34MatVecRange96) panel1Mode34MatVecRange128) row

theorem panel1Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode35MatVecRange0) panel1Mode35MatVecRange32) panel1Mode35MatVecRange64) panel1Mode35MatVecRange96) panel1Mode35MatVecRange128) row

theorem panel1Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode36MatVecRange0) panel1Mode36MatVecRange32) panel1Mode36MatVecRange64) panel1Mode36MatVecRange96) panel1Mode36MatVecRange128) row

theorem panel1Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode37MatVecRange0) panel1Mode37MatVecRange32) panel1Mode37MatVecRange64) panel1Mode37MatVecRange96) panel1Mode37MatVecRange128) row

theorem panel1Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode38MatVecRange0) panel1Mode38MatVecRange32) panel1Mode38MatVecRange64) panel1Mode38MatVecRange96) panel1Mode38MatVecRange128) row

theorem panel1Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode39MatVecRange0) panel1Mode39MatVecRange32) panel1Mode39MatVecRange64) panel1Mode39MatVecRange96) panel1Mode39MatVecRange128) row

theorem panel1Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode40MatVecRange0) panel1Mode40MatVecRange32) panel1Mode40MatVecRange64) panel1Mode40MatVecRange96) panel1Mode40MatVecRange128) row

theorem panel1Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode41MatVecRange0) panel1Mode41MatVecRange32) panel1Mode41MatVecRange64) panel1Mode41MatVecRange96) panel1Mode41MatVecRange128) row

theorem panel1Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode42MatVecRange0) panel1Mode42MatVecRange32) panel1Mode42MatVecRange64) panel1Mode42MatVecRange96) panel1Mode42MatVecRange128) row

theorem panel1Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode43MatVecRange0) panel1Mode43MatVecRange32) panel1Mode43MatVecRange64) panel1Mode43MatVecRange96) panel1Mode43MatVecRange128) row

theorem panel1Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode44MatVecRange0) panel1Mode44MatVecRange32) panel1Mode44MatVecRange64) panel1Mode44MatVecRange96) panel1Mode44MatVecRange128) row

theorem panel1Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode45MatVecRange0) panel1Mode45MatVecRange32) panel1Mode45MatVecRange64) panel1Mode45MatVecRange96) panel1Mode45MatVecRange128) row

theorem panel1Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode46MatVecRange0) panel1Mode46MatVecRange32) panel1Mode46MatVecRange64) panel1Mode46MatVecRange96) panel1Mode46MatVecRange128) row

theorem panel1Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel1MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel1MomentData.moments
        (P2RoundedFactorCheckpointData.panel1FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel1Mode47MatVecRange0) panel1Mode47MatVecRange32) panel1Mode47MatVecRange64) panel1Mode47MatVecRange96) panel1Mode47MatVecRange128) row

theorem panel1MomentData_correct :
    P2RoundedFactorCheckpointData.panel1MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel1FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel1DefectMoments_eq panel1ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel1Mode0MatVec_eq
      · exact panel1Mode2MatVec_eq
      · exact panel1Mode4MatVec_eq
      · exact panel1Mode6MatVec_eq
      · exact panel1Mode8MatVec_eq
      · exact panel1Mode10MatVec_eq
      · exact panel1Mode12MatVec_eq
      · exact panel1Mode14MatVec_eq
      · exact panel1Mode16MatVec_eq
      · exact panel1Mode18MatVec_eq
      · exact panel1Mode20MatVec_eq
      · exact panel1Mode22MatVec_eq
      · exact panel1Mode24MatVec_eq
      · exact panel1Mode26MatVec_eq
      · exact panel1Mode28MatVec_eq
      · exact panel1Mode30MatVec_eq
      · exact panel1Mode32MatVec_eq
      · exact panel1Mode34MatVec_eq
      · exact panel1Mode36MatVec_eq
      · exact panel1Mode38MatVec_eq
      · exact panel1Mode40MatVec_eq
      · exact panel1Mode42MatVec_eq
      · exact panel1Mode44MatVec_eq
      · exact panel1Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel1Mode1MatVec_eq
      · exact panel1Mode3MatVec_eq
      · exact panel1Mode5MatVec_eq
      · exact panel1Mode7MatVec_eq
      · exact panel1Mode9MatVec_eq
      · exact panel1Mode11MatVec_eq
      · exact panel1Mode13MatVec_eq
      · exact panel1Mode15MatVec_eq
      · exact panel1Mode17MatVec_eq
      · exact panel1Mode19MatVec_eq
      · exact panel1Mode21MatVec_eq
      · exact panel1Mode23MatVec_eq
      · exact panel1Mode25MatVec_eq
      · exact panel1Mode27MatVec_eq
      · exact panel1Mode29MatVec_eq
      · exact panel1Mode31MatVec_eq
      · exact panel1Mode33MatVec_eq
      · exact panel1Mode35MatVec_eq
      · exact panel1Mode37MatVec_eq
      · exact panel1Mode39MatVec_eq
      · exact panel1Mode41MatVec_eq
      · exact panel1Mode43MatVec_eq
      · exact panel1Mode45MatVec_eq
      · exact panel1Mode47MatVec_eq

end RHP2Bridge
