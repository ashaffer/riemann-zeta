import RHBridge.P2RoundedFlatFactorCheckpoint0
import RHBridge.P2RoundedMomentLengths0
import RHBridge.P2RoundedMomentCheckpointCheck0_moments
import RHBridge.P2RoundedMomentCheckpointCheck0_mode0
import RHBridge.P2RoundedMomentCheckpointCheck0_mode1
import RHBridge.P2RoundedMomentCheckpointCheck0_mode2
import RHBridge.P2RoundedMomentCheckpointCheck0_mode3
import RHBridge.P2RoundedMomentCheckpointCheck0_mode4
import RHBridge.P2RoundedMomentCheckpointCheck0_mode5
import RHBridge.P2RoundedMomentCheckpointCheck0_mode6
import RHBridge.P2RoundedMomentCheckpointCheck0_mode7
import RHBridge.P2RoundedMomentCheckpointCheck0_mode8
import RHBridge.P2RoundedMomentCheckpointCheck0_mode9
import RHBridge.P2RoundedMomentCheckpointCheck0_mode10
import RHBridge.P2RoundedMomentCheckpointCheck0_mode11
import RHBridge.P2RoundedMomentCheckpointCheck0_mode12
import RHBridge.P2RoundedMomentCheckpointCheck0_mode13
import RHBridge.P2RoundedMomentCheckpointCheck0_mode14
import RHBridge.P2RoundedMomentCheckpointCheck0_mode15
import RHBridge.P2RoundedMomentCheckpointCheck0_mode16
import RHBridge.P2RoundedMomentCheckpointCheck0_mode17
import RHBridge.P2RoundedMomentCheckpointCheck0_mode18
import RHBridge.P2RoundedMomentCheckpointCheck0_mode19
import RHBridge.P2RoundedMomentCheckpointCheck0_mode20
import RHBridge.P2RoundedMomentCheckpointCheck0_mode21
import RHBridge.P2RoundedMomentCheckpointCheck0_mode22
import RHBridge.P2RoundedMomentCheckpointCheck0_mode23
import RHBridge.P2RoundedMomentCheckpointCheck0_mode24
import RHBridge.P2RoundedMomentCheckpointCheck0_mode25
import RHBridge.P2RoundedMomentCheckpointCheck0_mode26
import RHBridge.P2RoundedMomentCheckpointCheck0_mode27
import RHBridge.P2RoundedMomentCheckpointCheck0_mode28
import RHBridge.P2RoundedMomentCheckpointCheck0_mode29
import RHBridge.P2RoundedMomentCheckpointCheck0_mode30
import RHBridge.P2RoundedMomentCheckpointCheck0_mode31
import RHBridge.P2RoundedMomentCheckpointCheck0_mode32
import RHBridge.P2RoundedMomentCheckpointCheck0_mode33
import RHBridge.P2RoundedMomentCheckpointCheck0_mode34
import RHBridge.P2RoundedMomentCheckpointCheck0_mode35
import RHBridge.P2RoundedMomentCheckpointCheck0_mode36
import RHBridge.P2RoundedMomentCheckpointCheck0_mode37
import RHBridge.P2RoundedMomentCheckpointCheck0_mode38
import RHBridge.P2RoundedMomentCheckpointCheck0_mode39
import RHBridge.P2RoundedMomentCheckpointCheck0_mode40
import RHBridge.P2RoundedMomentCheckpointCheck0_mode41
import RHBridge.P2RoundedMomentCheckpointCheck0_mode42
import RHBridge.P2RoundedMomentCheckpointCheck0_mode43
import RHBridge.P2RoundedMomentCheckpointCheck0_mode44
import RHBridge.P2RoundedMomentCheckpointCheck0_mode45
import RHBridge.P2RoundedMomentCheckpointCheck0_mode46
import RHBridge.P2RoundedMomentCheckpointCheck0_mode47

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

theorem panel0DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel0FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0DefectMomentRange0) panel0DefectMomentRange64) panel0DefectMomentRange128) panel0DefectMomentRange192) panel0DefectMomentRange256) row

theorem panel0Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode0MatVecRange0) panel0Mode0MatVecRange32) panel0Mode0MatVecRange64) panel0Mode0MatVecRange96) panel0Mode0MatVecRange128) row

theorem panel0Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode1MatVecRange0) panel0Mode1MatVecRange32) panel0Mode1MatVecRange64) panel0Mode1MatVecRange96) panel0Mode1MatVecRange128) row

theorem panel0Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode2MatVecRange0) panel0Mode2MatVecRange32) panel0Mode2MatVecRange64) panel0Mode2MatVecRange96) panel0Mode2MatVecRange128) row

theorem panel0Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode3MatVecRange0) panel0Mode3MatVecRange32) panel0Mode3MatVecRange64) panel0Mode3MatVecRange96) panel0Mode3MatVecRange128) row

theorem panel0Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode4MatVecRange0) panel0Mode4MatVecRange32) panel0Mode4MatVecRange64) panel0Mode4MatVecRange96) panel0Mode4MatVecRange128) row

theorem panel0Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode5MatVecRange0) panel0Mode5MatVecRange32) panel0Mode5MatVecRange64) panel0Mode5MatVecRange96) panel0Mode5MatVecRange128) row

theorem panel0Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode6MatVecRange0) panel0Mode6MatVecRange32) panel0Mode6MatVecRange64) panel0Mode6MatVecRange96) panel0Mode6MatVecRange128) row

theorem panel0Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode7MatVecRange0) panel0Mode7MatVecRange32) panel0Mode7MatVecRange64) panel0Mode7MatVecRange96) panel0Mode7MatVecRange128) row

theorem panel0Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode8MatVecRange0) panel0Mode8MatVecRange32) panel0Mode8MatVecRange64) panel0Mode8MatVecRange96) panel0Mode8MatVecRange128) row

theorem panel0Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode9MatVecRange0) panel0Mode9MatVecRange32) panel0Mode9MatVecRange64) panel0Mode9MatVecRange96) panel0Mode9MatVecRange128) row

theorem panel0Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode10MatVecRange0) panel0Mode10MatVecRange32) panel0Mode10MatVecRange64) panel0Mode10MatVecRange96) panel0Mode10MatVecRange128) row

theorem panel0Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode11MatVecRange0) panel0Mode11MatVecRange32) panel0Mode11MatVecRange64) panel0Mode11MatVecRange96) panel0Mode11MatVecRange128) row

theorem panel0Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode12MatVecRange0) panel0Mode12MatVecRange32) panel0Mode12MatVecRange64) panel0Mode12MatVecRange96) panel0Mode12MatVecRange128) row

theorem panel0Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode13MatVecRange0) panel0Mode13MatVecRange32) panel0Mode13MatVecRange64) panel0Mode13MatVecRange96) panel0Mode13MatVecRange128) row

theorem panel0Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode14MatVecRange0) panel0Mode14MatVecRange32) panel0Mode14MatVecRange64) panel0Mode14MatVecRange96) panel0Mode14MatVecRange128) row

theorem panel0Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode15MatVecRange0) panel0Mode15MatVecRange32) panel0Mode15MatVecRange64) panel0Mode15MatVecRange96) panel0Mode15MatVecRange128) row

theorem panel0Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode16MatVecRange0) panel0Mode16MatVecRange32) panel0Mode16MatVecRange64) panel0Mode16MatVecRange96) panel0Mode16MatVecRange128) row

theorem panel0Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode17MatVecRange0) panel0Mode17MatVecRange32) panel0Mode17MatVecRange64) panel0Mode17MatVecRange96) panel0Mode17MatVecRange128) row

theorem panel0Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode18MatVecRange0) panel0Mode18MatVecRange32) panel0Mode18MatVecRange64) panel0Mode18MatVecRange96) panel0Mode18MatVecRange128) row

theorem panel0Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode19MatVecRange0) panel0Mode19MatVecRange32) panel0Mode19MatVecRange64) panel0Mode19MatVecRange96) panel0Mode19MatVecRange128) row

theorem panel0Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode20MatVecRange0) panel0Mode20MatVecRange32) panel0Mode20MatVecRange64) panel0Mode20MatVecRange96) panel0Mode20MatVecRange128) row

theorem panel0Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode21MatVecRange0) panel0Mode21MatVecRange32) panel0Mode21MatVecRange64) panel0Mode21MatVecRange96) panel0Mode21MatVecRange128) row

theorem panel0Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode22MatVecRange0) panel0Mode22MatVecRange32) panel0Mode22MatVecRange64) panel0Mode22MatVecRange96) panel0Mode22MatVecRange128) row

theorem panel0Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode23MatVecRange0) panel0Mode23MatVecRange32) panel0Mode23MatVecRange64) panel0Mode23MatVecRange96) panel0Mode23MatVecRange128) row

theorem panel0Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode24MatVecRange0) panel0Mode24MatVecRange32) panel0Mode24MatVecRange64) panel0Mode24MatVecRange96) panel0Mode24MatVecRange128) row

theorem panel0Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode25MatVecRange0) panel0Mode25MatVecRange32) panel0Mode25MatVecRange64) panel0Mode25MatVecRange96) panel0Mode25MatVecRange128) row

theorem panel0Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode26MatVecRange0) panel0Mode26MatVecRange32) panel0Mode26MatVecRange64) panel0Mode26MatVecRange96) panel0Mode26MatVecRange128) row

theorem panel0Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode27MatVecRange0) panel0Mode27MatVecRange32) panel0Mode27MatVecRange64) panel0Mode27MatVecRange96) panel0Mode27MatVecRange128) row

theorem panel0Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode28MatVecRange0) panel0Mode28MatVecRange32) panel0Mode28MatVecRange64) panel0Mode28MatVecRange96) panel0Mode28MatVecRange128) row

theorem panel0Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode29MatVecRange0) panel0Mode29MatVecRange32) panel0Mode29MatVecRange64) panel0Mode29MatVecRange96) panel0Mode29MatVecRange128) row

theorem panel0Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode30MatVecRange0) panel0Mode30MatVecRange32) panel0Mode30MatVecRange64) panel0Mode30MatVecRange96) panel0Mode30MatVecRange128) row

theorem panel0Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode31MatVecRange0) panel0Mode31MatVecRange32) panel0Mode31MatVecRange64) panel0Mode31MatVecRange96) panel0Mode31MatVecRange128) row

theorem panel0Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode32MatVecRange0) panel0Mode32MatVecRange32) panel0Mode32MatVecRange64) panel0Mode32MatVecRange96) panel0Mode32MatVecRange128) row

theorem panel0Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode33MatVecRange0) panel0Mode33MatVecRange32) panel0Mode33MatVecRange64) panel0Mode33MatVecRange96) panel0Mode33MatVecRange128) row

theorem panel0Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode34MatVecRange0) panel0Mode34MatVecRange32) panel0Mode34MatVecRange64) panel0Mode34MatVecRange96) panel0Mode34MatVecRange128) row

theorem panel0Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode35MatVecRange0) panel0Mode35MatVecRange32) panel0Mode35MatVecRange64) panel0Mode35MatVecRange96) panel0Mode35MatVecRange128) row

theorem panel0Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode36MatVecRange0) panel0Mode36MatVecRange32) panel0Mode36MatVecRange64) panel0Mode36MatVecRange96) panel0Mode36MatVecRange128) row

theorem panel0Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode37MatVecRange0) panel0Mode37MatVecRange32) panel0Mode37MatVecRange64) panel0Mode37MatVecRange96) panel0Mode37MatVecRange128) row

theorem panel0Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode38MatVecRange0) panel0Mode38MatVecRange32) panel0Mode38MatVecRange64) panel0Mode38MatVecRange96) panel0Mode38MatVecRange128) row

theorem panel0Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode39MatVecRange0) panel0Mode39MatVecRange32) panel0Mode39MatVecRange64) panel0Mode39MatVecRange96) panel0Mode39MatVecRange128) row

theorem panel0Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode40MatVecRange0) panel0Mode40MatVecRange32) panel0Mode40MatVecRange64) panel0Mode40MatVecRange96) panel0Mode40MatVecRange128) row

theorem panel0Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode41MatVecRange0) panel0Mode41MatVecRange32) panel0Mode41MatVecRange64) panel0Mode41MatVecRange96) panel0Mode41MatVecRange128) row

theorem panel0Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode42MatVecRange0) panel0Mode42MatVecRange32) panel0Mode42MatVecRange64) panel0Mode42MatVecRange96) panel0Mode42MatVecRange128) row

theorem panel0Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode43MatVecRange0) panel0Mode43MatVecRange32) panel0Mode43MatVecRange64) panel0Mode43MatVecRange96) panel0Mode43MatVecRange128) row

theorem panel0Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode44MatVecRange0) panel0Mode44MatVecRange32) panel0Mode44MatVecRange64) panel0Mode44MatVecRange96) panel0Mode44MatVecRange128) row

theorem panel0Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode45MatVecRange0) panel0Mode45MatVecRange32) panel0Mode45MatVecRange64) panel0Mode45MatVecRange96) panel0Mode45MatVecRange128) row

theorem panel0Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode46MatVecRange0) panel0Mode46MatVecRange32) panel0Mode46MatVecRange64) panel0Mode46MatVecRange96) panel0Mode46MatVecRange128) row

theorem panel0Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel0MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel0MomentData.moments
        (P2RoundedFactorCheckpointData.panel0FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel0Mode47MatVecRange0) panel0Mode47MatVecRange32) panel0Mode47MatVecRange64) panel0Mode47MatVecRange96) panel0Mode47MatVecRange128) row

theorem panel0MomentData_correct :
    P2RoundedFactorCheckpointData.panel0MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel0FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel0DefectMoments_eq panel0ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel0Mode0MatVec_eq
      · exact panel0Mode2MatVec_eq
      · exact panel0Mode4MatVec_eq
      · exact panel0Mode6MatVec_eq
      · exact panel0Mode8MatVec_eq
      · exact panel0Mode10MatVec_eq
      · exact panel0Mode12MatVec_eq
      · exact panel0Mode14MatVec_eq
      · exact panel0Mode16MatVec_eq
      · exact panel0Mode18MatVec_eq
      · exact panel0Mode20MatVec_eq
      · exact panel0Mode22MatVec_eq
      · exact panel0Mode24MatVec_eq
      · exact panel0Mode26MatVec_eq
      · exact panel0Mode28MatVec_eq
      · exact panel0Mode30MatVec_eq
      · exact panel0Mode32MatVec_eq
      · exact panel0Mode34MatVec_eq
      · exact panel0Mode36MatVec_eq
      · exact panel0Mode38MatVec_eq
      · exact panel0Mode40MatVec_eq
      · exact panel0Mode42MatVec_eq
      · exact panel0Mode44MatVec_eq
      · exact panel0Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel0Mode1MatVec_eq
      · exact panel0Mode3MatVec_eq
      · exact panel0Mode5MatVec_eq
      · exact panel0Mode7MatVec_eq
      · exact panel0Mode9MatVec_eq
      · exact panel0Mode11MatVec_eq
      · exact panel0Mode13MatVec_eq
      · exact panel0Mode15MatVec_eq
      · exact panel0Mode17MatVec_eq
      · exact panel0Mode19MatVec_eq
      · exact panel0Mode21MatVec_eq
      · exact panel0Mode23MatVec_eq
      · exact panel0Mode25MatVec_eq
      · exact panel0Mode27MatVec_eq
      · exact panel0Mode29MatVec_eq
      · exact panel0Mode31MatVec_eq
      · exact panel0Mode33MatVec_eq
      · exact panel0Mode35MatVec_eq
      · exact panel0Mode37MatVec_eq
      · exact panel0Mode39MatVec_eq
      · exact panel0Mode41MatVec_eq
      · exact panel0Mode43MatVec_eq
      · exact panel0Mode45MatVec_eq
      · exact panel0Mode47MatVec_eq

end RHP2Bridge
