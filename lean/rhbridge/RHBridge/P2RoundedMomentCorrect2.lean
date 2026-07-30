import RHBridge.P2RoundedFlatFactorCheckpoint2
import RHBridge.P2RoundedMomentLengths2
import RHBridge.P2RoundedMomentCheckpointCheck2_moments
import RHBridge.P2RoundedMomentCheckpointCheck2_mode0
import RHBridge.P2RoundedMomentCheckpointCheck2_mode1
import RHBridge.P2RoundedMomentCheckpointCheck2_mode2
import RHBridge.P2RoundedMomentCheckpointCheck2_mode3
import RHBridge.P2RoundedMomentCheckpointCheck2_mode4
import RHBridge.P2RoundedMomentCheckpointCheck2_mode5
import RHBridge.P2RoundedMomentCheckpointCheck2_mode6
import RHBridge.P2RoundedMomentCheckpointCheck2_mode7
import RHBridge.P2RoundedMomentCheckpointCheck2_mode8
import RHBridge.P2RoundedMomentCheckpointCheck2_mode9
import RHBridge.P2RoundedMomentCheckpointCheck2_mode10
import RHBridge.P2RoundedMomentCheckpointCheck2_mode11
import RHBridge.P2RoundedMomentCheckpointCheck2_mode12
import RHBridge.P2RoundedMomentCheckpointCheck2_mode13
import RHBridge.P2RoundedMomentCheckpointCheck2_mode14
import RHBridge.P2RoundedMomentCheckpointCheck2_mode15
import RHBridge.P2RoundedMomentCheckpointCheck2_mode16
import RHBridge.P2RoundedMomentCheckpointCheck2_mode17
import RHBridge.P2RoundedMomentCheckpointCheck2_mode18
import RHBridge.P2RoundedMomentCheckpointCheck2_mode19
import RHBridge.P2RoundedMomentCheckpointCheck2_mode20
import RHBridge.P2RoundedMomentCheckpointCheck2_mode21
import RHBridge.P2RoundedMomentCheckpointCheck2_mode22
import RHBridge.P2RoundedMomentCheckpointCheck2_mode23
import RHBridge.P2RoundedMomentCheckpointCheck2_mode24
import RHBridge.P2RoundedMomentCheckpointCheck2_mode25
import RHBridge.P2RoundedMomentCheckpointCheck2_mode26
import RHBridge.P2RoundedMomentCheckpointCheck2_mode27
import RHBridge.P2RoundedMomentCheckpointCheck2_mode28
import RHBridge.P2RoundedMomentCheckpointCheck2_mode29
import RHBridge.P2RoundedMomentCheckpointCheck2_mode30
import RHBridge.P2RoundedMomentCheckpointCheck2_mode31
import RHBridge.P2RoundedMomentCheckpointCheck2_mode32
import RHBridge.P2RoundedMomentCheckpointCheck2_mode33
import RHBridge.P2RoundedMomentCheckpointCheck2_mode34
import RHBridge.P2RoundedMomentCheckpointCheck2_mode35
import RHBridge.P2RoundedMomentCheckpointCheck2_mode36
import RHBridge.P2RoundedMomentCheckpointCheck2_mode37
import RHBridge.P2RoundedMomentCheckpointCheck2_mode38
import RHBridge.P2RoundedMomentCheckpointCheck2_mode39
import RHBridge.P2RoundedMomentCheckpointCheck2_mode40
import RHBridge.P2RoundedMomentCheckpointCheck2_mode41
import RHBridge.P2RoundedMomentCheckpointCheck2_mode42
import RHBridge.P2RoundedMomentCheckpointCheck2_mode43
import RHBridge.P2RoundedMomentCheckpointCheck2_mode44
import RHBridge.P2RoundedMomentCheckpointCheck2_mode45
import RHBridge.P2RoundedMomentCheckpointCheck2_mode46
import RHBridge.P2RoundedMomentCheckpointCheck2_mode47

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

theorem panel2DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel2FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2DefectMomentRange0) panel2DefectMomentRange64) panel2DefectMomentRange128) panel2DefectMomentRange192) panel2DefectMomentRange256) row

theorem panel2Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode0MatVecRange0) panel2Mode0MatVecRange32) panel2Mode0MatVecRange64) panel2Mode0MatVecRange96) panel2Mode0MatVecRange128) row

theorem panel2Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode1MatVecRange0) panel2Mode1MatVecRange32) panel2Mode1MatVecRange64) panel2Mode1MatVecRange96) panel2Mode1MatVecRange128) row

theorem panel2Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode2MatVecRange0) panel2Mode2MatVecRange32) panel2Mode2MatVecRange64) panel2Mode2MatVecRange96) panel2Mode2MatVecRange128) row

theorem panel2Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode3MatVecRange0) panel2Mode3MatVecRange32) panel2Mode3MatVecRange64) panel2Mode3MatVecRange96) panel2Mode3MatVecRange128) row

theorem panel2Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode4MatVecRange0) panel2Mode4MatVecRange32) panel2Mode4MatVecRange64) panel2Mode4MatVecRange96) panel2Mode4MatVecRange128) row

theorem panel2Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode5MatVecRange0) panel2Mode5MatVecRange32) panel2Mode5MatVecRange64) panel2Mode5MatVecRange96) panel2Mode5MatVecRange128) row

theorem panel2Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode6MatVecRange0) panel2Mode6MatVecRange32) panel2Mode6MatVecRange64) panel2Mode6MatVecRange96) panel2Mode6MatVecRange128) row

theorem panel2Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode7MatVecRange0) panel2Mode7MatVecRange32) panel2Mode7MatVecRange64) panel2Mode7MatVecRange96) panel2Mode7MatVecRange128) row

theorem panel2Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode8MatVecRange0) panel2Mode8MatVecRange32) panel2Mode8MatVecRange64) panel2Mode8MatVecRange96) panel2Mode8MatVecRange128) row

theorem panel2Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode9MatVecRange0) panel2Mode9MatVecRange32) panel2Mode9MatVecRange64) panel2Mode9MatVecRange96) panel2Mode9MatVecRange128) row

theorem panel2Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode10MatVecRange0) panel2Mode10MatVecRange32) panel2Mode10MatVecRange64) panel2Mode10MatVecRange96) panel2Mode10MatVecRange128) row

theorem panel2Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode11MatVecRange0) panel2Mode11MatVecRange32) panel2Mode11MatVecRange64) panel2Mode11MatVecRange96) panel2Mode11MatVecRange128) row

theorem panel2Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode12MatVecRange0) panel2Mode12MatVecRange32) panel2Mode12MatVecRange64) panel2Mode12MatVecRange96) panel2Mode12MatVecRange128) row

theorem panel2Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode13MatVecRange0) panel2Mode13MatVecRange32) panel2Mode13MatVecRange64) panel2Mode13MatVecRange96) panel2Mode13MatVecRange128) row

theorem panel2Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode14MatVecRange0) panel2Mode14MatVecRange32) panel2Mode14MatVecRange64) panel2Mode14MatVecRange96) panel2Mode14MatVecRange128) row

theorem panel2Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode15MatVecRange0) panel2Mode15MatVecRange32) panel2Mode15MatVecRange64) panel2Mode15MatVecRange96) panel2Mode15MatVecRange128) row

theorem panel2Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode16MatVecRange0) panel2Mode16MatVecRange32) panel2Mode16MatVecRange64) panel2Mode16MatVecRange96) panel2Mode16MatVecRange128) row

theorem panel2Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode17MatVecRange0) panel2Mode17MatVecRange32) panel2Mode17MatVecRange64) panel2Mode17MatVecRange96) panel2Mode17MatVecRange128) row

theorem panel2Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode18MatVecRange0) panel2Mode18MatVecRange32) panel2Mode18MatVecRange64) panel2Mode18MatVecRange96) panel2Mode18MatVecRange128) row

theorem panel2Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode19MatVecRange0) panel2Mode19MatVecRange32) panel2Mode19MatVecRange64) panel2Mode19MatVecRange96) panel2Mode19MatVecRange128) row

theorem panel2Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode20MatVecRange0) panel2Mode20MatVecRange32) panel2Mode20MatVecRange64) panel2Mode20MatVecRange96) panel2Mode20MatVecRange128) row

theorem panel2Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode21MatVecRange0) panel2Mode21MatVecRange32) panel2Mode21MatVecRange64) panel2Mode21MatVecRange96) panel2Mode21MatVecRange128) row

theorem panel2Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode22MatVecRange0) panel2Mode22MatVecRange32) panel2Mode22MatVecRange64) panel2Mode22MatVecRange96) panel2Mode22MatVecRange128) row

theorem panel2Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode23MatVecRange0) panel2Mode23MatVecRange32) panel2Mode23MatVecRange64) panel2Mode23MatVecRange96) panel2Mode23MatVecRange128) row

theorem panel2Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode24MatVecRange0) panel2Mode24MatVecRange32) panel2Mode24MatVecRange64) panel2Mode24MatVecRange96) panel2Mode24MatVecRange128) row

theorem panel2Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode25MatVecRange0) panel2Mode25MatVecRange32) panel2Mode25MatVecRange64) panel2Mode25MatVecRange96) panel2Mode25MatVecRange128) row

theorem panel2Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode26MatVecRange0) panel2Mode26MatVecRange32) panel2Mode26MatVecRange64) panel2Mode26MatVecRange96) panel2Mode26MatVecRange128) row

theorem panel2Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode27MatVecRange0) panel2Mode27MatVecRange32) panel2Mode27MatVecRange64) panel2Mode27MatVecRange96) panel2Mode27MatVecRange128) row

theorem panel2Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode28MatVecRange0) panel2Mode28MatVecRange32) panel2Mode28MatVecRange64) panel2Mode28MatVecRange96) panel2Mode28MatVecRange128) row

theorem panel2Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode29MatVecRange0) panel2Mode29MatVecRange32) panel2Mode29MatVecRange64) panel2Mode29MatVecRange96) panel2Mode29MatVecRange128) row

theorem panel2Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode30MatVecRange0) panel2Mode30MatVecRange32) panel2Mode30MatVecRange64) panel2Mode30MatVecRange96) panel2Mode30MatVecRange128) row

theorem panel2Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode31MatVecRange0) panel2Mode31MatVecRange32) panel2Mode31MatVecRange64) panel2Mode31MatVecRange96) panel2Mode31MatVecRange128) row

theorem panel2Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode32MatVecRange0) panel2Mode32MatVecRange32) panel2Mode32MatVecRange64) panel2Mode32MatVecRange96) panel2Mode32MatVecRange128) row

theorem panel2Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode33MatVecRange0) panel2Mode33MatVecRange32) panel2Mode33MatVecRange64) panel2Mode33MatVecRange96) panel2Mode33MatVecRange128) row

theorem panel2Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode34MatVecRange0) panel2Mode34MatVecRange32) panel2Mode34MatVecRange64) panel2Mode34MatVecRange96) panel2Mode34MatVecRange128) row

theorem panel2Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode35MatVecRange0) panel2Mode35MatVecRange32) panel2Mode35MatVecRange64) panel2Mode35MatVecRange96) panel2Mode35MatVecRange128) row

theorem panel2Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode36MatVecRange0) panel2Mode36MatVecRange32) panel2Mode36MatVecRange64) panel2Mode36MatVecRange96) panel2Mode36MatVecRange128) row

theorem panel2Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode37MatVecRange0) panel2Mode37MatVecRange32) panel2Mode37MatVecRange64) panel2Mode37MatVecRange96) panel2Mode37MatVecRange128) row

theorem panel2Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode38MatVecRange0) panel2Mode38MatVecRange32) panel2Mode38MatVecRange64) panel2Mode38MatVecRange96) panel2Mode38MatVecRange128) row

theorem panel2Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode39MatVecRange0) panel2Mode39MatVecRange32) panel2Mode39MatVecRange64) panel2Mode39MatVecRange96) panel2Mode39MatVecRange128) row

theorem panel2Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode40MatVecRange0) panel2Mode40MatVecRange32) panel2Mode40MatVecRange64) panel2Mode40MatVecRange96) panel2Mode40MatVecRange128) row

theorem panel2Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode41MatVecRange0) panel2Mode41MatVecRange32) panel2Mode41MatVecRange64) panel2Mode41MatVecRange96) panel2Mode41MatVecRange128) row

theorem panel2Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode42MatVecRange0) panel2Mode42MatVecRange32) panel2Mode42MatVecRange64) panel2Mode42MatVecRange96) panel2Mode42MatVecRange128) row

theorem panel2Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode43MatVecRange0) panel2Mode43MatVecRange32) panel2Mode43MatVecRange64) panel2Mode43MatVecRange96) panel2Mode43MatVecRange128) row

theorem panel2Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode44MatVecRange0) panel2Mode44MatVecRange32) panel2Mode44MatVecRange64) panel2Mode44MatVecRange96) panel2Mode44MatVecRange128) row

theorem panel2Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode45MatVecRange0) panel2Mode45MatVecRange32) panel2Mode45MatVecRange64) panel2Mode45MatVecRange96) panel2Mode45MatVecRange128) row

theorem panel2Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode46MatVecRange0) panel2Mode46MatVecRange32) panel2Mode46MatVecRange64) panel2Mode46MatVecRange96) panel2Mode46MatVecRange128) row

theorem panel2Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel2MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel2MomentData.moments
        (P2RoundedFactorCheckpointData.panel2FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel2Mode47MatVecRange0) panel2Mode47MatVecRange32) panel2Mode47MatVecRange64) panel2Mode47MatVecRange96) panel2Mode47MatVecRange128) row

theorem panel2MomentData_correct :
    P2RoundedFactorCheckpointData.panel2MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel2FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel2DefectMoments_eq panel2ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel2Mode0MatVec_eq
      · exact panel2Mode2MatVec_eq
      · exact panel2Mode4MatVec_eq
      · exact panel2Mode6MatVec_eq
      · exact panel2Mode8MatVec_eq
      · exact panel2Mode10MatVec_eq
      · exact panel2Mode12MatVec_eq
      · exact panel2Mode14MatVec_eq
      · exact panel2Mode16MatVec_eq
      · exact panel2Mode18MatVec_eq
      · exact panel2Mode20MatVec_eq
      · exact panel2Mode22MatVec_eq
      · exact panel2Mode24MatVec_eq
      · exact panel2Mode26MatVec_eq
      · exact panel2Mode28MatVec_eq
      · exact panel2Mode30MatVec_eq
      · exact panel2Mode32MatVec_eq
      · exact panel2Mode34MatVec_eq
      · exact panel2Mode36MatVec_eq
      · exact panel2Mode38MatVec_eq
      · exact panel2Mode40MatVec_eq
      · exact panel2Mode42MatVec_eq
      · exact panel2Mode44MatVec_eq
      · exact panel2Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel2Mode1MatVec_eq
      · exact panel2Mode3MatVec_eq
      · exact panel2Mode5MatVec_eq
      · exact panel2Mode7MatVec_eq
      · exact panel2Mode9MatVec_eq
      · exact panel2Mode11MatVec_eq
      · exact panel2Mode13MatVec_eq
      · exact panel2Mode15MatVec_eq
      · exact panel2Mode17MatVec_eq
      · exact panel2Mode19MatVec_eq
      · exact panel2Mode21MatVec_eq
      · exact panel2Mode23MatVec_eq
      · exact panel2Mode25MatVec_eq
      · exact panel2Mode27MatVec_eq
      · exact panel2Mode29MatVec_eq
      · exact panel2Mode31MatVec_eq
      · exact panel2Mode33MatVec_eq
      · exact panel2Mode35MatVec_eq
      · exact panel2Mode37MatVec_eq
      · exact panel2Mode39MatVec_eq
      · exact panel2Mode41MatVec_eq
      · exact panel2Mode43MatVec_eq
      · exact panel2Mode45MatVec_eq
      · exact panel2Mode47MatVec_eq

end RHP2Bridge
