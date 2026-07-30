import RHBridge.P2RoundedFlatFactorCheckpoint28
import RHBridge.P2RoundedMomentLengths28
import RHBridge.P2RoundedMomentCheckpointCheck28_moments
import RHBridge.P2RoundedMomentCheckpointCheck28_mode0
import RHBridge.P2RoundedMomentCheckpointCheck28_mode1
import RHBridge.P2RoundedMomentCheckpointCheck28_mode2
import RHBridge.P2RoundedMomentCheckpointCheck28_mode3
import RHBridge.P2RoundedMomentCheckpointCheck28_mode4
import RHBridge.P2RoundedMomentCheckpointCheck28_mode5
import RHBridge.P2RoundedMomentCheckpointCheck28_mode6
import RHBridge.P2RoundedMomentCheckpointCheck28_mode7
import RHBridge.P2RoundedMomentCheckpointCheck28_mode8
import RHBridge.P2RoundedMomentCheckpointCheck28_mode9
import RHBridge.P2RoundedMomentCheckpointCheck28_mode10
import RHBridge.P2RoundedMomentCheckpointCheck28_mode11
import RHBridge.P2RoundedMomentCheckpointCheck28_mode12
import RHBridge.P2RoundedMomentCheckpointCheck28_mode13
import RHBridge.P2RoundedMomentCheckpointCheck28_mode14
import RHBridge.P2RoundedMomentCheckpointCheck28_mode15
import RHBridge.P2RoundedMomentCheckpointCheck28_mode16
import RHBridge.P2RoundedMomentCheckpointCheck28_mode17
import RHBridge.P2RoundedMomentCheckpointCheck28_mode18
import RHBridge.P2RoundedMomentCheckpointCheck28_mode19
import RHBridge.P2RoundedMomentCheckpointCheck28_mode20
import RHBridge.P2RoundedMomentCheckpointCheck28_mode21
import RHBridge.P2RoundedMomentCheckpointCheck28_mode22
import RHBridge.P2RoundedMomentCheckpointCheck28_mode23
import RHBridge.P2RoundedMomentCheckpointCheck28_mode24
import RHBridge.P2RoundedMomentCheckpointCheck28_mode25
import RHBridge.P2RoundedMomentCheckpointCheck28_mode26
import RHBridge.P2RoundedMomentCheckpointCheck28_mode27
import RHBridge.P2RoundedMomentCheckpointCheck28_mode28
import RHBridge.P2RoundedMomentCheckpointCheck28_mode29
import RHBridge.P2RoundedMomentCheckpointCheck28_mode30
import RHBridge.P2RoundedMomentCheckpointCheck28_mode31
import RHBridge.P2RoundedMomentCheckpointCheck28_mode32
import RHBridge.P2RoundedMomentCheckpointCheck28_mode33
import RHBridge.P2RoundedMomentCheckpointCheck28_mode34
import RHBridge.P2RoundedMomentCheckpointCheck28_mode35
import RHBridge.P2RoundedMomentCheckpointCheck28_mode36
import RHBridge.P2RoundedMomentCheckpointCheck28_mode37
import RHBridge.P2RoundedMomentCheckpointCheck28_mode38
import RHBridge.P2RoundedMomentCheckpointCheck28_mode39
import RHBridge.P2RoundedMomentCheckpointCheck28_mode40
import RHBridge.P2RoundedMomentCheckpointCheck28_mode41
import RHBridge.P2RoundedMomentCheckpointCheck28_mode42
import RHBridge.P2RoundedMomentCheckpointCheck28_mode43
import RHBridge.P2RoundedMomentCheckpointCheck28_mode44
import RHBridge.P2RoundedMomentCheckpointCheck28_mode45
import RHBridge.P2RoundedMomentCheckpointCheck28_mode46
import RHBridge.P2RoundedMomentCheckpointCheck28_mode47

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

theorem panel28DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel28FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28DefectMomentRange0) panel28DefectMomentRange64) panel28DefectMomentRange128) panel28DefectMomentRange192) panel28DefectMomentRange256) row

theorem panel28Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode0MatVecRange0) panel28Mode0MatVecRange32) panel28Mode0MatVecRange64) panel28Mode0MatVecRange96) panel28Mode0MatVecRange128) row

theorem panel28Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode1MatVecRange0) panel28Mode1MatVecRange32) panel28Mode1MatVecRange64) panel28Mode1MatVecRange96) panel28Mode1MatVecRange128) row

theorem panel28Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode2MatVecRange0) panel28Mode2MatVecRange32) panel28Mode2MatVecRange64) panel28Mode2MatVecRange96) panel28Mode2MatVecRange128) row

theorem panel28Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode3MatVecRange0) panel28Mode3MatVecRange32) panel28Mode3MatVecRange64) panel28Mode3MatVecRange96) panel28Mode3MatVecRange128) row

theorem panel28Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode4MatVecRange0) panel28Mode4MatVecRange32) panel28Mode4MatVecRange64) panel28Mode4MatVecRange96) panel28Mode4MatVecRange128) row

theorem panel28Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode5MatVecRange0) panel28Mode5MatVecRange32) panel28Mode5MatVecRange64) panel28Mode5MatVecRange96) panel28Mode5MatVecRange128) row

theorem panel28Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode6MatVecRange0) panel28Mode6MatVecRange32) panel28Mode6MatVecRange64) panel28Mode6MatVecRange96) panel28Mode6MatVecRange128) row

theorem panel28Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode7MatVecRange0) panel28Mode7MatVecRange32) panel28Mode7MatVecRange64) panel28Mode7MatVecRange96) panel28Mode7MatVecRange128) row

theorem panel28Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode8MatVecRange0) panel28Mode8MatVecRange32) panel28Mode8MatVecRange64) panel28Mode8MatVecRange96) panel28Mode8MatVecRange128) row

theorem panel28Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode9MatVecRange0) panel28Mode9MatVecRange32) panel28Mode9MatVecRange64) panel28Mode9MatVecRange96) panel28Mode9MatVecRange128) row

theorem panel28Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode10MatVecRange0) panel28Mode10MatVecRange32) panel28Mode10MatVecRange64) panel28Mode10MatVecRange96) panel28Mode10MatVecRange128) row

theorem panel28Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode11MatVecRange0) panel28Mode11MatVecRange32) panel28Mode11MatVecRange64) panel28Mode11MatVecRange96) panel28Mode11MatVecRange128) row

theorem panel28Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode12MatVecRange0) panel28Mode12MatVecRange32) panel28Mode12MatVecRange64) panel28Mode12MatVecRange96) panel28Mode12MatVecRange128) row

theorem panel28Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode13MatVecRange0) panel28Mode13MatVecRange32) panel28Mode13MatVecRange64) panel28Mode13MatVecRange96) panel28Mode13MatVecRange128) row

theorem panel28Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode14MatVecRange0) panel28Mode14MatVecRange32) panel28Mode14MatVecRange64) panel28Mode14MatVecRange96) panel28Mode14MatVecRange128) row

theorem panel28Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode15MatVecRange0) panel28Mode15MatVecRange32) panel28Mode15MatVecRange64) panel28Mode15MatVecRange96) panel28Mode15MatVecRange128) row

theorem panel28Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode16MatVecRange0) panel28Mode16MatVecRange32) panel28Mode16MatVecRange64) panel28Mode16MatVecRange96) panel28Mode16MatVecRange128) row

theorem panel28Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode17MatVecRange0) panel28Mode17MatVecRange32) panel28Mode17MatVecRange64) panel28Mode17MatVecRange96) panel28Mode17MatVecRange128) row

theorem panel28Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode18MatVecRange0) panel28Mode18MatVecRange32) panel28Mode18MatVecRange64) panel28Mode18MatVecRange96) panel28Mode18MatVecRange128) row

theorem panel28Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode19MatVecRange0) panel28Mode19MatVecRange32) panel28Mode19MatVecRange64) panel28Mode19MatVecRange96) panel28Mode19MatVecRange128) row

theorem panel28Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode20MatVecRange0) panel28Mode20MatVecRange32) panel28Mode20MatVecRange64) panel28Mode20MatVecRange96) panel28Mode20MatVecRange128) row

theorem panel28Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode21MatVecRange0) panel28Mode21MatVecRange32) panel28Mode21MatVecRange64) panel28Mode21MatVecRange96) panel28Mode21MatVecRange128) row

theorem panel28Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode22MatVecRange0) panel28Mode22MatVecRange32) panel28Mode22MatVecRange64) panel28Mode22MatVecRange96) panel28Mode22MatVecRange128) row

theorem panel28Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode23MatVecRange0) panel28Mode23MatVecRange32) panel28Mode23MatVecRange64) panel28Mode23MatVecRange96) panel28Mode23MatVecRange128) row

theorem panel28Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode24MatVecRange0) panel28Mode24MatVecRange32) panel28Mode24MatVecRange64) panel28Mode24MatVecRange96) panel28Mode24MatVecRange128) row

theorem panel28Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode25MatVecRange0) panel28Mode25MatVecRange32) panel28Mode25MatVecRange64) panel28Mode25MatVecRange96) panel28Mode25MatVecRange128) row

theorem panel28Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode26MatVecRange0) panel28Mode26MatVecRange32) panel28Mode26MatVecRange64) panel28Mode26MatVecRange96) panel28Mode26MatVecRange128) row

theorem panel28Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode27MatVecRange0) panel28Mode27MatVecRange32) panel28Mode27MatVecRange64) panel28Mode27MatVecRange96) panel28Mode27MatVecRange128) row

theorem panel28Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode28MatVecRange0) panel28Mode28MatVecRange32) panel28Mode28MatVecRange64) panel28Mode28MatVecRange96) panel28Mode28MatVecRange128) row

theorem panel28Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode29MatVecRange0) panel28Mode29MatVecRange32) panel28Mode29MatVecRange64) panel28Mode29MatVecRange96) panel28Mode29MatVecRange128) row

theorem panel28Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode30MatVecRange0) panel28Mode30MatVecRange32) panel28Mode30MatVecRange64) panel28Mode30MatVecRange96) panel28Mode30MatVecRange128) row

theorem panel28Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode31MatVecRange0) panel28Mode31MatVecRange32) panel28Mode31MatVecRange64) panel28Mode31MatVecRange96) panel28Mode31MatVecRange128) row

theorem panel28Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode32MatVecRange0) panel28Mode32MatVecRange32) panel28Mode32MatVecRange64) panel28Mode32MatVecRange96) panel28Mode32MatVecRange128) row

theorem panel28Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode33MatVecRange0) panel28Mode33MatVecRange32) panel28Mode33MatVecRange64) panel28Mode33MatVecRange96) panel28Mode33MatVecRange128) row

theorem panel28Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode34MatVecRange0) panel28Mode34MatVecRange32) panel28Mode34MatVecRange64) panel28Mode34MatVecRange96) panel28Mode34MatVecRange128) row

theorem panel28Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode35MatVecRange0) panel28Mode35MatVecRange32) panel28Mode35MatVecRange64) panel28Mode35MatVecRange96) panel28Mode35MatVecRange128) row

theorem panel28Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode36MatVecRange0) panel28Mode36MatVecRange32) panel28Mode36MatVecRange64) panel28Mode36MatVecRange96) panel28Mode36MatVecRange128) row

theorem panel28Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode37MatVecRange0) panel28Mode37MatVecRange32) panel28Mode37MatVecRange64) panel28Mode37MatVecRange96) panel28Mode37MatVecRange128) row

theorem panel28Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode38MatVecRange0) panel28Mode38MatVecRange32) panel28Mode38MatVecRange64) panel28Mode38MatVecRange96) panel28Mode38MatVecRange128) row

theorem panel28Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode39MatVecRange0) panel28Mode39MatVecRange32) panel28Mode39MatVecRange64) panel28Mode39MatVecRange96) panel28Mode39MatVecRange128) row

theorem panel28Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode40MatVecRange0) panel28Mode40MatVecRange32) panel28Mode40MatVecRange64) panel28Mode40MatVecRange96) panel28Mode40MatVecRange128) row

theorem panel28Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode41MatVecRange0) panel28Mode41MatVecRange32) panel28Mode41MatVecRange64) panel28Mode41MatVecRange96) panel28Mode41MatVecRange128) row

theorem panel28Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode42MatVecRange0) panel28Mode42MatVecRange32) panel28Mode42MatVecRange64) panel28Mode42MatVecRange96) panel28Mode42MatVecRange128) row

theorem panel28Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode43MatVecRange0) panel28Mode43MatVecRange32) panel28Mode43MatVecRange64) panel28Mode43MatVecRange96) panel28Mode43MatVecRange128) row

theorem panel28Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode44MatVecRange0) panel28Mode44MatVecRange32) panel28Mode44MatVecRange64) panel28Mode44MatVecRange96) panel28Mode44MatVecRange128) row

theorem panel28Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode45MatVecRange0) panel28Mode45MatVecRange32) panel28Mode45MatVecRange64) panel28Mode45MatVecRange96) panel28Mode45MatVecRange128) row

theorem panel28Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode46MatVecRange0) panel28Mode46MatVecRange32) panel28Mode46MatVecRange64) panel28Mode46MatVecRange96) panel28Mode46MatVecRange128) row

theorem panel28Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel28MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel28MomentData.moments
        (P2RoundedFactorCheckpointData.panel28FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel28Mode47MatVecRange0) panel28Mode47MatVecRange32) panel28Mode47MatVecRange64) panel28Mode47MatVecRange96) panel28Mode47MatVecRange128) row

theorem panel28MomentData_correct :
    P2RoundedFactorCheckpointData.panel28MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel28FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel28DefectMoments_eq panel28ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel28Mode0MatVec_eq
      · exact panel28Mode2MatVec_eq
      · exact panel28Mode4MatVec_eq
      · exact panel28Mode6MatVec_eq
      · exact panel28Mode8MatVec_eq
      · exact panel28Mode10MatVec_eq
      · exact panel28Mode12MatVec_eq
      · exact panel28Mode14MatVec_eq
      · exact panel28Mode16MatVec_eq
      · exact panel28Mode18MatVec_eq
      · exact panel28Mode20MatVec_eq
      · exact panel28Mode22MatVec_eq
      · exact panel28Mode24MatVec_eq
      · exact panel28Mode26MatVec_eq
      · exact panel28Mode28MatVec_eq
      · exact panel28Mode30MatVec_eq
      · exact panel28Mode32MatVec_eq
      · exact panel28Mode34MatVec_eq
      · exact panel28Mode36MatVec_eq
      · exact panel28Mode38MatVec_eq
      · exact panel28Mode40MatVec_eq
      · exact panel28Mode42MatVec_eq
      · exact panel28Mode44MatVec_eq
      · exact panel28Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel28Mode1MatVec_eq
      · exact panel28Mode3MatVec_eq
      · exact panel28Mode5MatVec_eq
      · exact panel28Mode7MatVec_eq
      · exact panel28Mode9MatVec_eq
      · exact panel28Mode11MatVec_eq
      · exact panel28Mode13MatVec_eq
      · exact panel28Mode15MatVec_eq
      · exact panel28Mode17MatVec_eq
      · exact panel28Mode19MatVec_eq
      · exact panel28Mode21MatVec_eq
      · exact panel28Mode23MatVec_eq
      · exact panel28Mode25MatVec_eq
      · exact panel28Mode27MatVec_eq
      · exact panel28Mode29MatVec_eq
      · exact panel28Mode31MatVec_eq
      · exact panel28Mode33MatVec_eq
      · exact panel28Mode35MatVec_eq
      · exact panel28Mode37MatVec_eq
      · exact panel28Mode39MatVec_eq
      · exact panel28Mode41MatVec_eq
      · exact panel28Mode43MatVec_eq
      · exact panel28Mode45MatVec_eq
      · exact panel28Mode47MatVec_eq

end RHP2Bridge
