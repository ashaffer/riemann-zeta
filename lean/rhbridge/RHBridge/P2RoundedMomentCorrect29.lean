import RHBridge.P2RoundedFlatFactorCheckpoint29
import RHBridge.P2RoundedMomentLengths29
import RHBridge.P2RoundedMomentCheckpointCheck29_moments
import RHBridge.P2RoundedMomentCheckpointCheck29_mode0
import RHBridge.P2RoundedMomentCheckpointCheck29_mode1
import RHBridge.P2RoundedMomentCheckpointCheck29_mode2
import RHBridge.P2RoundedMomentCheckpointCheck29_mode3
import RHBridge.P2RoundedMomentCheckpointCheck29_mode4
import RHBridge.P2RoundedMomentCheckpointCheck29_mode5
import RHBridge.P2RoundedMomentCheckpointCheck29_mode6
import RHBridge.P2RoundedMomentCheckpointCheck29_mode7
import RHBridge.P2RoundedMomentCheckpointCheck29_mode8
import RHBridge.P2RoundedMomentCheckpointCheck29_mode9
import RHBridge.P2RoundedMomentCheckpointCheck29_mode10
import RHBridge.P2RoundedMomentCheckpointCheck29_mode11
import RHBridge.P2RoundedMomentCheckpointCheck29_mode12
import RHBridge.P2RoundedMomentCheckpointCheck29_mode13
import RHBridge.P2RoundedMomentCheckpointCheck29_mode14
import RHBridge.P2RoundedMomentCheckpointCheck29_mode15
import RHBridge.P2RoundedMomentCheckpointCheck29_mode16
import RHBridge.P2RoundedMomentCheckpointCheck29_mode17
import RHBridge.P2RoundedMomentCheckpointCheck29_mode18
import RHBridge.P2RoundedMomentCheckpointCheck29_mode19
import RHBridge.P2RoundedMomentCheckpointCheck29_mode20
import RHBridge.P2RoundedMomentCheckpointCheck29_mode21
import RHBridge.P2RoundedMomentCheckpointCheck29_mode22
import RHBridge.P2RoundedMomentCheckpointCheck29_mode23
import RHBridge.P2RoundedMomentCheckpointCheck29_mode24
import RHBridge.P2RoundedMomentCheckpointCheck29_mode25
import RHBridge.P2RoundedMomentCheckpointCheck29_mode26
import RHBridge.P2RoundedMomentCheckpointCheck29_mode27
import RHBridge.P2RoundedMomentCheckpointCheck29_mode28
import RHBridge.P2RoundedMomentCheckpointCheck29_mode29
import RHBridge.P2RoundedMomentCheckpointCheck29_mode30
import RHBridge.P2RoundedMomentCheckpointCheck29_mode31
import RHBridge.P2RoundedMomentCheckpointCheck29_mode32
import RHBridge.P2RoundedMomentCheckpointCheck29_mode33
import RHBridge.P2RoundedMomentCheckpointCheck29_mode34
import RHBridge.P2RoundedMomentCheckpointCheck29_mode35
import RHBridge.P2RoundedMomentCheckpointCheck29_mode36
import RHBridge.P2RoundedMomentCheckpointCheck29_mode37
import RHBridge.P2RoundedMomentCheckpointCheck29_mode38
import RHBridge.P2RoundedMomentCheckpointCheck29_mode39
import RHBridge.P2RoundedMomentCheckpointCheck29_mode40
import RHBridge.P2RoundedMomentCheckpointCheck29_mode41
import RHBridge.P2RoundedMomentCheckpointCheck29_mode42
import RHBridge.P2RoundedMomentCheckpointCheck29_mode43
import RHBridge.P2RoundedMomentCheckpointCheck29_mode44
import RHBridge.P2RoundedMomentCheckpointCheck29_mode45
import RHBridge.P2RoundedMomentCheckpointCheck29_mode46
import RHBridge.P2RoundedMomentCheckpointCheck29_mode47

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

theorem panel29DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel29FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29DefectMomentRange0) panel29DefectMomentRange64) panel29DefectMomentRange128) panel29DefectMomentRange192) panel29DefectMomentRange256) row

theorem panel29Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode0MatVecRange0) panel29Mode0MatVecRange32) panel29Mode0MatVecRange64) panel29Mode0MatVecRange96) panel29Mode0MatVecRange128) row

theorem panel29Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode1MatVecRange0) panel29Mode1MatVecRange32) panel29Mode1MatVecRange64) panel29Mode1MatVecRange96) panel29Mode1MatVecRange128) row

theorem panel29Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode2MatVecRange0) panel29Mode2MatVecRange32) panel29Mode2MatVecRange64) panel29Mode2MatVecRange96) panel29Mode2MatVecRange128) row

theorem panel29Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode3MatVecRange0) panel29Mode3MatVecRange32) panel29Mode3MatVecRange64) panel29Mode3MatVecRange96) panel29Mode3MatVecRange128) row

theorem panel29Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode4MatVecRange0) panel29Mode4MatVecRange32) panel29Mode4MatVecRange64) panel29Mode4MatVecRange96) panel29Mode4MatVecRange128) row

theorem panel29Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode5MatVecRange0) panel29Mode5MatVecRange32) panel29Mode5MatVecRange64) panel29Mode5MatVecRange96) panel29Mode5MatVecRange128) row

theorem panel29Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode6MatVecRange0) panel29Mode6MatVecRange32) panel29Mode6MatVecRange64) panel29Mode6MatVecRange96) panel29Mode6MatVecRange128) row

theorem panel29Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode7MatVecRange0) panel29Mode7MatVecRange32) panel29Mode7MatVecRange64) panel29Mode7MatVecRange96) panel29Mode7MatVecRange128) row

theorem panel29Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode8MatVecRange0) panel29Mode8MatVecRange32) panel29Mode8MatVecRange64) panel29Mode8MatVecRange96) panel29Mode8MatVecRange128) row

theorem panel29Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode9MatVecRange0) panel29Mode9MatVecRange32) panel29Mode9MatVecRange64) panel29Mode9MatVecRange96) panel29Mode9MatVecRange128) row

theorem panel29Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode10MatVecRange0) panel29Mode10MatVecRange32) panel29Mode10MatVecRange64) panel29Mode10MatVecRange96) panel29Mode10MatVecRange128) row

theorem panel29Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode11MatVecRange0) panel29Mode11MatVecRange32) panel29Mode11MatVecRange64) panel29Mode11MatVecRange96) panel29Mode11MatVecRange128) row

theorem panel29Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode12MatVecRange0) panel29Mode12MatVecRange32) panel29Mode12MatVecRange64) panel29Mode12MatVecRange96) panel29Mode12MatVecRange128) row

theorem panel29Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode13MatVecRange0) panel29Mode13MatVecRange32) panel29Mode13MatVecRange64) panel29Mode13MatVecRange96) panel29Mode13MatVecRange128) row

theorem panel29Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode14MatVecRange0) panel29Mode14MatVecRange32) panel29Mode14MatVecRange64) panel29Mode14MatVecRange96) panel29Mode14MatVecRange128) row

theorem panel29Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode15MatVecRange0) panel29Mode15MatVecRange32) panel29Mode15MatVecRange64) panel29Mode15MatVecRange96) panel29Mode15MatVecRange128) row

theorem panel29Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode16MatVecRange0) panel29Mode16MatVecRange32) panel29Mode16MatVecRange64) panel29Mode16MatVecRange96) panel29Mode16MatVecRange128) row

theorem panel29Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode17MatVecRange0) panel29Mode17MatVecRange32) panel29Mode17MatVecRange64) panel29Mode17MatVecRange96) panel29Mode17MatVecRange128) row

theorem panel29Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode18MatVecRange0) panel29Mode18MatVecRange32) panel29Mode18MatVecRange64) panel29Mode18MatVecRange96) panel29Mode18MatVecRange128) row

theorem panel29Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode19MatVecRange0) panel29Mode19MatVecRange32) panel29Mode19MatVecRange64) panel29Mode19MatVecRange96) panel29Mode19MatVecRange128) row

theorem panel29Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode20MatVecRange0) panel29Mode20MatVecRange32) panel29Mode20MatVecRange64) panel29Mode20MatVecRange96) panel29Mode20MatVecRange128) row

theorem panel29Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode21MatVecRange0) panel29Mode21MatVecRange32) panel29Mode21MatVecRange64) panel29Mode21MatVecRange96) panel29Mode21MatVecRange128) row

theorem panel29Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode22MatVecRange0) panel29Mode22MatVecRange32) panel29Mode22MatVecRange64) panel29Mode22MatVecRange96) panel29Mode22MatVecRange128) row

theorem panel29Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode23MatVecRange0) panel29Mode23MatVecRange32) panel29Mode23MatVecRange64) panel29Mode23MatVecRange96) panel29Mode23MatVecRange128) row

theorem panel29Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode24MatVecRange0) panel29Mode24MatVecRange32) panel29Mode24MatVecRange64) panel29Mode24MatVecRange96) panel29Mode24MatVecRange128) row

theorem panel29Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode25MatVecRange0) panel29Mode25MatVecRange32) panel29Mode25MatVecRange64) panel29Mode25MatVecRange96) panel29Mode25MatVecRange128) row

theorem panel29Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode26MatVecRange0) panel29Mode26MatVecRange32) panel29Mode26MatVecRange64) panel29Mode26MatVecRange96) panel29Mode26MatVecRange128) row

theorem panel29Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode27MatVecRange0) panel29Mode27MatVecRange32) panel29Mode27MatVecRange64) panel29Mode27MatVecRange96) panel29Mode27MatVecRange128) row

theorem panel29Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode28MatVecRange0) panel29Mode28MatVecRange32) panel29Mode28MatVecRange64) panel29Mode28MatVecRange96) panel29Mode28MatVecRange128) row

theorem panel29Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode29MatVecRange0) panel29Mode29MatVecRange32) panel29Mode29MatVecRange64) panel29Mode29MatVecRange96) panel29Mode29MatVecRange128) row

theorem panel29Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode30MatVecRange0) panel29Mode30MatVecRange32) panel29Mode30MatVecRange64) panel29Mode30MatVecRange96) panel29Mode30MatVecRange128) row

theorem panel29Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode31MatVecRange0) panel29Mode31MatVecRange32) panel29Mode31MatVecRange64) panel29Mode31MatVecRange96) panel29Mode31MatVecRange128) row

theorem panel29Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode32MatVecRange0) panel29Mode32MatVecRange32) panel29Mode32MatVecRange64) panel29Mode32MatVecRange96) panel29Mode32MatVecRange128) row

theorem panel29Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode33MatVecRange0) panel29Mode33MatVecRange32) panel29Mode33MatVecRange64) panel29Mode33MatVecRange96) panel29Mode33MatVecRange128) row

theorem panel29Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode34MatVecRange0) panel29Mode34MatVecRange32) panel29Mode34MatVecRange64) panel29Mode34MatVecRange96) panel29Mode34MatVecRange128) row

theorem panel29Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode35MatVecRange0) panel29Mode35MatVecRange32) panel29Mode35MatVecRange64) panel29Mode35MatVecRange96) panel29Mode35MatVecRange128) row

theorem panel29Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode36MatVecRange0) panel29Mode36MatVecRange32) panel29Mode36MatVecRange64) panel29Mode36MatVecRange96) panel29Mode36MatVecRange128) row

theorem panel29Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode37MatVecRange0) panel29Mode37MatVecRange32) panel29Mode37MatVecRange64) panel29Mode37MatVecRange96) panel29Mode37MatVecRange128) row

theorem panel29Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode38MatVecRange0) panel29Mode38MatVecRange32) panel29Mode38MatVecRange64) panel29Mode38MatVecRange96) panel29Mode38MatVecRange128) row

theorem panel29Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode39MatVecRange0) panel29Mode39MatVecRange32) panel29Mode39MatVecRange64) panel29Mode39MatVecRange96) panel29Mode39MatVecRange128) row

theorem panel29Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode40MatVecRange0) panel29Mode40MatVecRange32) panel29Mode40MatVecRange64) panel29Mode40MatVecRange96) panel29Mode40MatVecRange128) row

theorem panel29Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode41MatVecRange0) panel29Mode41MatVecRange32) panel29Mode41MatVecRange64) panel29Mode41MatVecRange96) panel29Mode41MatVecRange128) row

theorem panel29Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode42MatVecRange0) panel29Mode42MatVecRange32) panel29Mode42MatVecRange64) panel29Mode42MatVecRange96) panel29Mode42MatVecRange128) row

theorem panel29Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode43MatVecRange0) panel29Mode43MatVecRange32) panel29Mode43MatVecRange64) panel29Mode43MatVecRange96) panel29Mode43MatVecRange128) row

theorem panel29Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode44MatVecRange0) panel29Mode44MatVecRange32) panel29Mode44MatVecRange64) panel29Mode44MatVecRange96) panel29Mode44MatVecRange128) row

theorem panel29Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode45MatVecRange0) panel29Mode45MatVecRange32) panel29Mode45MatVecRange64) panel29Mode45MatVecRange96) panel29Mode45MatVecRange128) row

theorem panel29Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode46MatVecRange0) panel29Mode46MatVecRange32) panel29Mode46MatVecRange64) panel29Mode46MatVecRange96) panel29Mode46MatVecRange128) row

theorem panel29Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel29MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel29MomentData.moments
        (P2RoundedFactorCheckpointData.panel29FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel29Mode47MatVecRange0) panel29Mode47MatVecRange32) panel29Mode47MatVecRange64) panel29Mode47MatVecRange96) panel29Mode47MatVecRange128) row

theorem panel29MomentData_correct :
    P2RoundedFactorCheckpointData.panel29MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel29FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel29DefectMoments_eq panel29ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel29Mode0MatVec_eq
      · exact panel29Mode2MatVec_eq
      · exact panel29Mode4MatVec_eq
      · exact panel29Mode6MatVec_eq
      · exact panel29Mode8MatVec_eq
      · exact panel29Mode10MatVec_eq
      · exact panel29Mode12MatVec_eq
      · exact panel29Mode14MatVec_eq
      · exact panel29Mode16MatVec_eq
      · exact panel29Mode18MatVec_eq
      · exact panel29Mode20MatVec_eq
      · exact panel29Mode22MatVec_eq
      · exact panel29Mode24MatVec_eq
      · exact panel29Mode26MatVec_eq
      · exact panel29Mode28MatVec_eq
      · exact panel29Mode30MatVec_eq
      · exact panel29Mode32MatVec_eq
      · exact panel29Mode34MatVec_eq
      · exact panel29Mode36MatVec_eq
      · exact panel29Mode38MatVec_eq
      · exact panel29Mode40MatVec_eq
      · exact panel29Mode42MatVec_eq
      · exact panel29Mode44MatVec_eq
      · exact panel29Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel29Mode1MatVec_eq
      · exact panel29Mode3MatVec_eq
      · exact panel29Mode5MatVec_eq
      · exact panel29Mode7MatVec_eq
      · exact panel29Mode9MatVec_eq
      · exact panel29Mode11MatVec_eq
      · exact panel29Mode13MatVec_eq
      · exact panel29Mode15MatVec_eq
      · exact panel29Mode17MatVec_eq
      · exact panel29Mode19MatVec_eq
      · exact panel29Mode21MatVec_eq
      · exact panel29Mode23MatVec_eq
      · exact panel29Mode25MatVec_eq
      · exact panel29Mode27MatVec_eq
      · exact panel29Mode29MatVec_eq
      · exact panel29Mode31MatVec_eq
      · exact panel29Mode33MatVec_eq
      · exact panel29Mode35MatVec_eq
      · exact panel29Mode37MatVec_eq
      · exact panel29Mode39MatVec_eq
      · exact panel29Mode41MatVec_eq
      · exact panel29Mode43MatVec_eq
      · exact panel29Mode45MatVec_eq
      · exact panel29Mode47MatVec_eq

end RHP2Bridge
