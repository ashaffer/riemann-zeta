import RHBridge.P2RoundedFlatFactorCheckpoint17
import RHBridge.P2RoundedMomentLengths17
import RHBridge.P2RoundedMomentCheckpointCheck17_moments
import RHBridge.P2RoundedMomentCheckpointCheck17_mode0
import RHBridge.P2RoundedMomentCheckpointCheck17_mode1
import RHBridge.P2RoundedMomentCheckpointCheck17_mode2
import RHBridge.P2RoundedMomentCheckpointCheck17_mode3
import RHBridge.P2RoundedMomentCheckpointCheck17_mode4
import RHBridge.P2RoundedMomentCheckpointCheck17_mode5
import RHBridge.P2RoundedMomentCheckpointCheck17_mode6
import RHBridge.P2RoundedMomentCheckpointCheck17_mode7
import RHBridge.P2RoundedMomentCheckpointCheck17_mode8
import RHBridge.P2RoundedMomentCheckpointCheck17_mode9
import RHBridge.P2RoundedMomentCheckpointCheck17_mode10
import RHBridge.P2RoundedMomentCheckpointCheck17_mode11
import RHBridge.P2RoundedMomentCheckpointCheck17_mode12
import RHBridge.P2RoundedMomentCheckpointCheck17_mode13
import RHBridge.P2RoundedMomentCheckpointCheck17_mode14
import RHBridge.P2RoundedMomentCheckpointCheck17_mode15
import RHBridge.P2RoundedMomentCheckpointCheck17_mode16
import RHBridge.P2RoundedMomentCheckpointCheck17_mode17
import RHBridge.P2RoundedMomentCheckpointCheck17_mode18
import RHBridge.P2RoundedMomentCheckpointCheck17_mode19
import RHBridge.P2RoundedMomentCheckpointCheck17_mode20
import RHBridge.P2RoundedMomentCheckpointCheck17_mode21
import RHBridge.P2RoundedMomentCheckpointCheck17_mode22
import RHBridge.P2RoundedMomentCheckpointCheck17_mode23
import RHBridge.P2RoundedMomentCheckpointCheck17_mode24
import RHBridge.P2RoundedMomentCheckpointCheck17_mode25
import RHBridge.P2RoundedMomentCheckpointCheck17_mode26
import RHBridge.P2RoundedMomentCheckpointCheck17_mode27
import RHBridge.P2RoundedMomentCheckpointCheck17_mode28
import RHBridge.P2RoundedMomentCheckpointCheck17_mode29
import RHBridge.P2RoundedMomentCheckpointCheck17_mode30
import RHBridge.P2RoundedMomentCheckpointCheck17_mode31
import RHBridge.P2RoundedMomentCheckpointCheck17_mode32
import RHBridge.P2RoundedMomentCheckpointCheck17_mode33
import RHBridge.P2RoundedMomentCheckpointCheck17_mode34
import RHBridge.P2RoundedMomentCheckpointCheck17_mode35
import RHBridge.P2RoundedMomentCheckpointCheck17_mode36
import RHBridge.P2RoundedMomentCheckpointCheck17_mode37
import RHBridge.P2RoundedMomentCheckpointCheck17_mode38
import RHBridge.P2RoundedMomentCheckpointCheck17_mode39
import RHBridge.P2RoundedMomentCheckpointCheck17_mode40
import RHBridge.P2RoundedMomentCheckpointCheck17_mode41
import RHBridge.P2RoundedMomentCheckpointCheck17_mode42
import RHBridge.P2RoundedMomentCheckpointCheck17_mode43
import RHBridge.P2RoundedMomentCheckpointCheck17_mode44
import RHBridge.P2RoundedMomentCheckpointCheck17_mode45
import RHBridge.P2RoundedMomentCheckpointCheck17_mode46
import RHBridge.P2RoundedMomentCheckpointCheck17_mode47

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

theorem panel17DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel17FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17DefectMomentRange0) panel17DefectMomentRange64) panel17DefectMomentRange128) panel17DefectMomentRange192) panel17DefectMomentRange256) row

theorem panel17Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode0MatVecRange0) panel17Mode0MatVecRange32) panel17Mode0MatVecRange64) panel17Mode0MatVecRange96) panel17Mode0MatVecRange128) row

theorem panel17Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode1MatVecRange0) panel17Mode1MatVecRange32) panel17Mode1MatVecRange64) panel17Mode1MatVecRange96) panel17Mode1MatVecRange128) row

theorem panel17Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode2MatVecRange0) panel17Mode2MatVecRange32) panel17Mode2MatVecRange64) panel17Mode2MatVecRange96) panel17Mode2MatVecRange128) row

theorem panel17Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode3MatVecRange0) panel17Mode3MatVecRange32) panel17Mode3MatVecRange64) panel17Mode3MatVecRange96) panel17Mode3MatVecRange128) row

theorem panel17Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode4MatVecRange0) panel17Mode4MatVecRange32) panel17Mode4MatVecRange64) panel17Mode4MatVecRange96) panel17Mode4MatVecRange128) row

theorem panel17Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode5MatVecRange0) panel17Mode5MatVecRange32) panel17Mode5MatVecRange64) panel17Mode5MatVecRange96) panel17Mode5MatVecRange128) row

theorem panel17Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode6MatVecRange0) panel17Mode6MatVecRange32) panel17Mode6MatVecRange64) panel17Mode6MatVecRange96) panel17Mode6MatVecRange128) row

theorem panel17Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode7MatVecRange0) panel17Mode7MatVecRange32) panel17Mode7MatVecRange64) panel17Mode7MatVecRange96) panel17Mode7MatVecRange128) row

theorem panel17Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode8MatVecRange0) panel17Mode8MatVecRange32) panel17Mode8MatVecRange64) panel17Mode8MatVecRange96) panel17Mode8MatVecRange128) row

theorem panel17Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode9MatVecRange0) panel17Mode9MatVecRange32) panel17Mode9MatVecRange64) panel17Mode9MatVecRange96) panel17Mode9MatVecRange128) row

theorem panel17Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode10MatVecRange0) panel17Mode10MatVecRange32) panel17Mode10MatVecRange64) panel17Mode10MatVecRange96) panel17Mode10MatVecRange128) row

theorem panel17Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode11MatVecRange0) panel17Mode11MatVecRange32) panel17Mode11MatVecRange64) panel17Mode11MatVecRange96) panel17Mode11MatVecRange128) row

theorem panel17Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode12MatVecRange0) panel17Mode12MatVecRange32) panel17Mode12MatVecRange64) panel17Mode12MatVecRange96) panel17Mode12MatVecRange128) row

theorem panel17Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode13MatVecRange0) panel17Mode13MatVecRange32) panel17Mode13MatVecRange64) panel17Mode13MatVecRange96) panel17Mode13MatVecRange128) row

theorem panel17Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode14MatVecRange0) panel17Mode14MatVecRange32) panel17Mode14MatVecRange64) panel17Mode14MatVecRange96) panel17Mode14MatVecRange128) row

theorem panel17Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode15MatVecRange0) panel17Mode15MatVecRange32) panel17Mode15MatVecRange64) panel17Mode15MatVecRange96) panel17Mode15MatVecRange128) row

theorem panel17Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode16MatVecRange0) panel17Mode16MatVecRange32) panel17Mode16MatVecRange64) panel17Mode16MatVecRange96) panel17Mode16MatVecRange128) row

theorem panel17Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode17MatVecRange0) panel17Mode17MatVecRange32) panel17Mode17MatVecRange64) panel17Mode17MatVecRange96) panel17Mode17MatVecRange128) row

theorem panel17Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode18MatVecRange0) panel17Mode18MatVecRange32) panel17Mode18MatVecRange64) panel17Mode18MatVecRange96) panel17Mode18MatVecRange128) row

theorem panel17Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode19MatVecRange0) panel17Mode19MatVecRange32) panel17Mode19MatVecRange64) panel17Mode19MatVecRange96) panel17Mode19MatVecRange128) row

theorem panel17Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode20MatVecRange0) panel17Mode20MatVecRange32) panel17Mode20MatVecRange64) panel17Mode20MatVecRange96) panel17Mode20MatVecRange128) row

theorem panel17Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode21MatVecRange0) panel17Mode21MatVecRange32) panel17Mode21MatVecRange64) panel17Mode21MatVecRange96) panel17Mode21MatVecRange128) row

theorem panel17Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode22MatVecRange0) panel17Mode22MatVecRange32) panel17Mode22MatVecRange64) panel17Mode22MatVecRange96) panel17Mode22MatVecRange128) row

theorem panel17Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode23MatVecRange0) panel17Mode23MatVecRange32) panel17Mode23MatVecRange64) panel17Mode23MatVecRange96) panel17Mode23MatVecRange128) row

theorem panel17Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode24MatVecRange0) panel17Mode24MatVecRange32) panel17Mode24MatVecRange64) panel17Mode24MatVecRange96) panel17Mode24MatVecRange128) row

theorem panel17Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode25MatVecRange0) panel17Mode25MatVecRange32) panel17Mode25MatVecRange64) panel17Mode25MatVecRange96) panel17Mode25MatVecRange128) row

theorem panel17Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode26MatVecRange0) panel17Mode26MatVecRange32) panel17Mode26MatVecRange64) panel17Mode26MatVecRange96) panel17Mode26MatVecRange128) row

theorem panel17Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode27MatVecRange0) panel17Mode27MatVecRange32) panel17Mode27MatVecRange64) panel17Mode27MatVecRange96) panel17Mode27MatVecRange128) row

theorem panel17Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode28MatVecRange0) panel17Mode28MatVecRange32) panel17Mode28MatVecRange64) panel17Mode28MatVecRange96) panel17Mode28MatVecRange128) row

theorem panel17Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode29MatVecRange0) panel17Mode29MatVecRange32) panel17Mode29MatVecRange64) panel17Mode29MatVecRange96) panel17Mode29MatVecRange128) row

theorem panel17Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode30MatVecRange0) panel17Mode30MatVecRange32) panel17Mode30MatVecRange64) panel17Mode30MatVecRange96) panel17Mode30MatVecRange128) row

theorem panel17Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode31MatVecRange0) panel17Mode31MatVecRange32) panel17Mode31MatVecRange64) panel17Mode31MatVecRange96) panel17Mode31MatVecRange128) row

theorem panel17Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode32MatVecRange0) panel17Mode32MatVecRange32) panel17Mode32MatVecRange64) panel17Mode32MatVecRange96) panel17Mode32MatVecRange128) row

theorem panel17Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode33MatVecRange0) panel17Mode33MatVecRange32) panel17Mode33MatVecRange64) panel17Mode33MatVecRange96) panel17Mode33MatVecRange128) row

theorem panel17Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode34MatVecRange0) panel17Mode34MatVecRange32) panel17Mode34MatVecRange64) panel17Mode34MatVecRange96) panel17Mode34MatVecRange128) row

theorem panel17Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode35MatVecRange0) panel17Mode35MatVecRange32) panel17Mode35MatVecRange64) panel17Mode35MatVecRange96) panel17Mode35MatVecRange128) row

theorem panel17Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode36MatVecRange0) panel17Mode36MatVecRange32) panel17Mode36MatVecRange64) panel17Mode36MatVecRange96) panel17Mode36MatVecRange128) row

theorem panel17Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode37MatVecRange0) panel17Mode37MatVecRange32) panel17Mode37MatVecRange64) panel17Mode37MatVecRange96) panel17Mode37MatVecRange128) row

theorem panel17Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode38MatVecRange0) panel17Mode38MatVecRange32) panel17Mode38MatVecRange64) panel17Mode38MatVecRange96) panel17Mode38MatVecRange128) row

theorem panel17Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode39MatVecRange0) panel17Mode39MatVecRange32) panel17Mode39MatVecRange64) panel17Mode39MatVecRange96) panel17Mode39MatVecRange128) row

theorem panel17Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode40MatVecRange0) panel17Mode40MatVecRange32) panel17Mode40MatVecRange64) panel17Mode40MatVecRange96) panel17Mode40MatVecRange128) row

theorem panel17Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode41MatVecRange0) panel17Mode41MatVecRange32) panel17Mode41MatVecRange64) panel17Mode41MatVecRange96) panel17Mode41MatVecRange128) row

theorem panel17Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode42MatVecRange0) panel17Mode42MatVecRange32) panel17Mode42MatVecRange64) panel17Mode42MatVecRange96) panel17Mode42MatVecRange128) row

theorem panel17Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode43MatVecRange0) panel17Mode43MatVecRange32) panel17Mode43MatVecRange64) panel17Mode43MatVecRange96) panel17Mode43MatVecRange128) row

theorem panel17Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode44MatVecRange0) panel17Mode44MatVecRange32) panel17Mode44MatVecRange64) panel17Mode44MatVecRange96) panel17Mode44MatVecRange128) row

theorem panel17Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode45MatVecRange0) panel17Mode45MatVecRange32) panel17Mode45MatVecRange64) panel17Mode45MatVecRange96) panel17Mode45MatVecRange128) row

theorem panel17Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode46MatVecRange0) panel17Mode46MatVecRange32) panel17Mode46MatVecRange64) panel17Mode46MatVecRange96) panel17Mode46MatVecRange128) row

theorem panel17Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel17MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel17MomentData.moments
        (P2RoundedFactorCheckpointData.panel17FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel17Mode47MatVecRange0) panel17Mode47MatVecRange32) panel17Mode47MatVecRange64) panel17Mode47MatVecRange96) panel17Mode47MatVecRange128) row

theorem panel17MomentData_correct :
    P2RoundedFactorCheckpointData.panel17MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel17FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel17DefectMoments_eq panel17ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel17Mode0MatVec_eq
      · exact panel17Mode2MatVec_eq
      · exact panel17Mode4MatVec_eq
      · exact panel17Mode6MatVec_eq
      · exact panel17Mode8MatVec_eq
      · exact panel17Mode10MatVec_eq
      · exact panel17Mode12MatVec_eq
      · exact panel17Mode14MatVec_eq
      · exact panel17Mode16MatVec_eq
      · exact panel17Mode18MatVec_eq
      · exact panel17Mode20MatVec_eq
      · exact panel17Mode22MatVec_eq
      · exact panel17Mode24MatVec_eq
      · exact panel17Mode26MatVec_eq
      · exact panel17Mode28MatVec_eq
      · exact panel17Mode30MatVec_eq
      · exact panel17Mode32MatVec_eq
      · exact panel17Mode34MatVec_eq
      · exact panel17Mode36MatVec_eq
      · exact panel17Mode38MatVec_eq
      · exact panel17Mode40MatVec_eq
      · exact panel17Mode42MatVec_eq
      · exact panel17Mode44MatVec_eq
      · exact panel17Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel17Mode1MatVec_eq
      · exact panel17Mode3MatVec_eq
      · exact panel17Mode5MatVec_eq
      · exact panel17Mode7MatVec_eq
      · exact panel17Mode9MatVec_eq
      · exact panel17Mode11MatVec_eq
      · exact panel17Mode13MatVec_eq
      · exact panel17Mode15MatVec_eq
      · exact panel17Mode17MatVec_eq
      · exact panel17Mode19MatVec_eq
      · exact panel17Mode21MatVec_eq
      · exact panel17Mode23MatVec_eq
      · exact panel17Mode25MatVec_eq
      · exact panel17Mode27MatVec_eq
      · exact panel17Mode29MatVec_eq
      · exact panel17Mode31MatVec_eq
      · exact panel17Mode33MatVec_eq
      · exact panel17Mode35MatVec_eq
      · exact panel17Mode37MatVec_eq
      · exact panel17Mode39MatVec_eq
      · exact panel17Mode41MatVec_eq
      · exact panel17Mode43MatVec_eq
      · exact panel17Mode45MatVec_eq
      · exact panel17Mode47MatVec_eq

end RHP2Bridge
