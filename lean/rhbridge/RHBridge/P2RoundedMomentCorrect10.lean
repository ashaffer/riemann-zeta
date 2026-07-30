import RHBridge.P2RoundedFlatFactorCheckpoint10
import RHBridge.P2RoundedMomentLengths10
import RHBridge.P2RoundedMomentCheckpointCheck10_moments
import RHBridge.P2RoundedMomentCheckpointCheck10_mode0
import RHBridge.P2RoundedMomentCheckpointCheck10_mode1
import RHBridge.P2RoundedMomentCheckpointCheck10_mode2
import RHBridge.P2RoundedMomentCheckpointCheck10_mode3
import RHBridge.P2RoundedMomentCheckpointCheck10_mode4
import RHBridge.P2RoundedMomentCheckpointCheck10_mode5
import RHBridge.P2RoundedMomentCheckpointCheck10_mode6
import RHBridge.P2RoundedMomentCheckpointCheck10_mode7
import RHBridge.P2RoundedMomentCheckpointCheck10_mode8
import RHBridge.P2RoundedMomentCheckpointCheck10_mode9
import RHBridge.P2RoundedMomentCheckpointCheck10_mode10
import RHBridge.P2RoundedMomentCheckpointCheck10_mode11
import RHBridge.P2RoundedMomentCheckpointCheck10_mode12
import RHBridge.P2RoundedMomentCheckpointCheck10_mode13
import RHBridge.P2RoundedMomentCheckpointCheck10_mode14
import RHBridge.P2RoundedMomentCheckpointCheck10_mode15
import RHBridge.P2RoundedMomentCheckpointCheck10_mode16
import RHBridge.P2RoundedMomentCheckpointCheck10_mode17
import RHBridge.P2RoundedMomentCheckpointCheck10_mode18
import RHBridge.P2RoundedMomentCheckpointCheck10_mode19
import RHBridge.P2RoundedMomentCheckpointCheck10_mode20
import RHBridge.P2RoundedMomentCheckpointCheck10_mode21
import RHBridge.P2RoundedMomentCheckpointCheck10_mode22
import RHBridge.P2RoundedMomentCheckpointCheck10_mode23
import RHBridge.P2RoundedMomentCheckpointCheck10_mode24
import RHBridge.P2RoundedMomentCheckpointCheck10_mode25
import RHBridge.P2RoundedMomentCheckpointCheck10_mode26
import RHBridge.P2RoundedMomentCheckpointCheck10_mode27
import RHBridge.P2RoundedMomentCheckpointCheck10_mode28
import RHBridge.P2RoundedMomentCheckpointCheck10_mode29
import RHBridge.P2RoundedMomentCheckpointCheck10_mode30
import RHBridge.P2RoundedMomentCheckpointCheck10_mode31
import RHBridge.P2RoundedMomentCheckpointCheck10_mode32
import RHBridge.P2RoundedMomentCheckpointCheck10_mode33
import RHBridge.P2RoundedMomentCheckpointCheck10_mode34
import RHBridge.P2RoundedMomentCheckpointCheck10_mode35
import RHBridge.P2RoundedMomentCheckpointCheck10_mode36
import RHBridge.P2RoundedMomentCheckpointCheck10_mode37
import RHBridge.P2RoundedMomentCheckpointCheck10_mode38
import RHBridge.P2RoundedMomentCheckpointCheck10_mode39
import RHBridge.P2RoundedMomentCheckpointCheck10_mode40
import RHBridge.P2RoundedMomentCheckpointCheck10_mode41
import RHBridge.P2RoundedMomentCheckpointCheck10_mode42
import RHBridge.P2RoundedMomentCheckpointCheck10_mode43
import RHBridge.P2RoundedMomentCheckpointCheck10_mode44
import RHBridge.P2RoundedMomentCheckpointCheck10_mode45
import RHBridge.P2RoundedMomentCheckpointCheck10_mode46
import RHBridge.P2RoundedMomentCheckpointCheck10_mode47

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

theorem panel10DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel10FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10DefectMomentRange0) panel10DefectMomentRange64) panel10DefectMomentRange128) panel10DefectMomentRange192) panel10DefectMomentRange256) row

theorem panel10Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode0MatVecRange0) panel10Mode0MatVecRange32) panel10Mode0MatVecRange64) panel10Mode0MatVecRange96) panel10Mode0MatVecRange128) row

theorem panel10Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode1MatVecRange0) panel10Mode1MatVecRange32) panel10Mode1MatVecRange64) panel10Mode1MatVecRange96) panel10Mode1MatVecRange128) row

theorem panel10Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode2MatVecRange0) panel10Mode2MatVecRange32) panel10Mode2MatVecRange64) panel10Mode2MatVecRange96) panel10Mode2MatVecRange128) row

theorem panel10Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode3MatVecRange0) panel10Mode3MatVecRange32) panel10Mode3MatVecRange64) panel10Mode3MatVecRange96) panel10Mode3MatVecRange128) row

theorem panel10Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode4MatVecRange0) panel10Mode4MatVecRange32) panel10Mode4MatVecRange64) panel10Mode4MatVecRange96) panel10Mode4MatVecRange128) row

theorem panel10Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode5MatVecRange0) panel10Mode5MatVecRange32) panel10Mode5MatVecRange64) panel10Mode5MatVecRange96) panel10Mode5MatVecRange128) row

theorem panel10Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode6MatVecRange0) panel10Mode6MatVecRange32) panel10Mode6MatVecRange64) panel10Mode6MatVecRange96) panel10Mode6MatVecRange128) row

theorem panel10Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode7MatVecRange0) panel10Mode7MatVecRange32) panel10Mode7MatVecRange64) panel10Mode7MatVecRange96) panel10Mode7MatVecRange128) row

theorem panel10Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode8MatVecRange0) panel10Mode8MatVecRange32) panel10Mode8MatVecRange64) panel10Mode8MatVecRange96) panel10Mode8MatVecRange128) row

theorem panel10Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode9MatVecRange0) panel10Mode9MatVecRange32) panel10Mode9MatVecRange64) panel10Mode9MatVecRange96) panel10Mode9MatVecRange128) row

theorem panel10Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode10MatVecRange0) panel10Mode10MatVecRange32) panel10Mode10MatVecRange64) panel10Mode10MatVecRange96) panel10Mode10MatVecRange128) row

theorem panel10Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode11MatVecRange0) panel10Mode11MatVecRange32) panel10Mode11MatVecRange64) panel10Mode11MatVecRange96) panel10Mode11MatVecRange128) row

theorem panel10Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode12MatVecRange0) panel10Mode12MatVecRange32) panel10Mode12MatVecRange64) panel10Mode12MatVecRange96) panel10Mode12MatVecRange128) row

theorem panel10Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode13MatVecRange0) panel10Mode13MatVecRange32) panel10Mode13MatVecRange64) panel10Mode13MatVecRange96) panel10Mode13MatVecRange128) row

theorem panel10Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode14MatVecRange0) panel10Mode14MatVecRange32) panel10Mode14MatVecRange64) panel10Mode14MatVecRange96) panel10Mode14MatVecRange128) row

theorem panel10Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode15MatVecRange0) panel10Mode15MatVecRange32) panel10Mode15MatVecRange64) panel10Mode15MatVecRange96) panel10Mode15MatVecRange128) row

theorem panel10Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode16MatVecRange0) panel10Mode16MatVecRange32) panel10Mode16MatVecRange64) panel10Mode16MatVecRange96) panel10Mode16MatVecRange128) row

theorem panel10Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode17MatVecRange0) panel10Mode17MatVecRange32) panel10Mode17MatVecRange64) panel10Mode17MatVecRange96) panel10Mode17MatVecRange128) row

theorem panel10Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode18MatVecRange0) panel10Mode18MatVecRange32) panel10Mode18MatVecRange64) panel10Mode18MatVecRange96) panel10Mode18MatVecRange128) row

theorem panel10Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode19MatVecRange0) panel10Mode19MatVecRange32) panel10Mode19MatVecRange64) panel10Mode19MatVecRange96) panel10Mode19MatVecRange128) row

theorem panel10Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode20MatVecRange0) panel10Mode20MatVecRange32) panel10Mode20MatVecRange64) panel10Mode20MatVecRange96) panel10Mode20MatVecRange128) row

theorem panel10Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode21MatVecRange0) panel10Mode21MatVecRange32) panel10Mode21MatVecRange64) panel10Mode21MatVecRange96) panel10Mode21MatVecRange128) row

theorem panel10Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode22MatVecRange0) panel10Mode22MatVecRange32) panel10Mode22MatVecRange64) panel10Mode22MatVecRange96) panel10Mode22MatVecRange128) row

theorem panel10Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode23MatVecRange0) panel10Mode23MatVecRange32) panel10Mode23MatVecRange64) panel10Mode23MatVecRange96) panel10Mode23MatVecRange128) row

theorem panel10Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode24MatVecRange0) panel10Mode24MatVecRange32) panel10Mode24MatVecRange64) panel10Mode24MatVecRange96) panel10Mode24MatVecRange128) row

theorem panel10Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode25MatVecRange0) panel10Mode25MatVecRange32) panel10Mode25MatVecRange64) panel10Mode25MatVecRange96) panel10Mode25MatVecRange128) row

theorem panel10Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode26MatVecRange0) panel10Mode26MatVecRange32) panel10Mode26MatVecRange64) panel10Mode26MatVecRange96) panel10Mode26MatVecRange128) row

theorem panel10Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode27MatVecRange0) panel10Mode27MatVecRange32) panel10Mode27MatVecRange64) panel10Mode27MatVecRange96) panel10Mode27MatVecRange128) row

theorem panel10Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode28MatVecRange0) panel10Mode28MatVecRange32) panel10Mode28MatVecRange64) panel10Mode28MatVecRange96) panel10Mode28MatVecRange128) row

theorem panel10Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode29MatVecRange0) panel10Mode29MatVecRange32) panel10Mode29MatVecRange64) panel10Mode29MatVecRange96) panel10Mode29MatVecRange128) row

theorem panel10Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode30MatVecRange0) panel10Mode30MatVecRange32) panel10Mode30MatVecRange64) panel10Mode30MatVecRange96) panel10Mode30MatVecRange128) row

theorem panel10Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode31MatVecRange0) panel10Mode31MatVecRange32) panel10Mode31MatVecRange64) panel10Mode31MatVecRange96) panel10Mode31MatVecRange128) row

theorem panel10Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode32MatVecRange0) panel10Mode32MatVecRange32) panel10Mode32MatVecRange64) panel10Mode32MatVecRange96) panel10Mode32MatVecRange128) row

theorem panel10Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode33MatVecRange0) panel10Mode33MatVecRange32) panel10Mode33MatVecRange64) panel10Mode33MatVecRange96) panel10Mode33MatVecRange128) row

theorem panel10Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode34MatVecRange0) panel10Mode34MatVecRange32) panel10Mode34MatVecRange64) panel10Mode34MatVecRange96) panel10Mode34MatVecRange128) row

theorem panel10Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode35MatVecRange0) panel10Mode35MatVecRange32) panel10Mode35MatVecRange64) panel10Mode35MatVecRange96) panel10Mode35MatVecRange128) row

theorem panel10Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode36MatVecRange0) panel10Mode36MatVecRange32) panel10Mode36MatVecRange64) panel10Mode36MatVecRange96) panel10Mode36MatVecRange128) row

theorem panel10Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode37MatVecRange0) panel10Mode37MatVecRange32) panel10Mode37MatVecRange64) panel10Mode37MatVecRange96) panel10Mode37MatVecRange128) row

theorem panel10Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode38MatVecRange0) panel10Mode38MatVecRange32) panel10Mode38MatVecRange64) panel10Mode38MatVecRange96) panel10Mode38MatVecRange128) row

theorem panel10Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode39MatVecRange0) panel10Mode39MatVecRange32) panel10Mode39MatVecRange64) panel10Mode39MatVecRange96) panel10Mode39MatVecRange128) row

theorem panel10Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode40MatVecRange0) panel10Mode40MatVecRange32) panel10Mode40MatVecRange64) panel10Mode40MatVecRange96) panel10Mode40MatVecRange128) row

theorem panel10Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode41MatVecRange0) panel10Mode41MatVecRange32) panel10Mode41MatVecRange64) panel10Mode41MatVecRange96) panel10Mode41MatVecRange128) row

theorem panel10Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode42MatVecRange0) panel10Mode42MatVecRange32) panel10Mode42MatVecRange64) panel10Mode42MatVecRange96) panel10Mode42MatVecRange128) row

theorem panel10Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode43MatVecRange0) panel10Mode43MatVecRange32) panel10Mode43MatVecRange64) panel10Mode43MatVecRange96) panel10Mode43MatVecRange128) row

theorem panel10Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode44MatVecRange0) panel10Mode44MatVecRange32) panel10Mode44MatVecRange64) panel10Mode44MatVecRange96) panel10Mode44MatVecRange128) row

theorem panel10Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode45MatVecRange0) panel10Mode45MatVecRange32) panel10Mode45MatVecRange64) panel10Mode45MatVecRange96) panel10Mode45MatVecRange128) row

theorem panel10Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode46MatVecRange0) panel10Mode46MatVecRange32) panel10Mode46MatVecRange64) panel10Mode46MatVecRange96) panel10Mode46MatVecRange128) row

theorem panel10Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel10MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel10MomentData.moments
        (P2RoundedFactorCheckpointData.panel10FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel10Mode47MatVecRange0) panel10Mode47MatVecRange32) panel10Mode47MatVecRange64) panel10Mode47MatVecRange96) panel10Mode47MatVecRange128) row

theorem panel10MomentData_correct :
    P2RoundedFactorCheckpointData.panel10MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel10FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel10DefectMoments_eq panel10ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel10Mode0MatVec_eq
      · exact panel10Mode2MatVec_eq
      · exact panel10Mode4MatVec_eq
      · exact panel10Mode6MatVec_eq
      · exact panel10Mode8MatVec_eq
      · exact panel10Mode10MatVec_eq
      · exact panel10Mode12MatVec_eq
      · exact panel10Mode14MatVec_eq
      · exact panel10Mode16MatVec_eq
      · exact panel10Mode18MatVec_eq
      · exact panel10Mode20MatVec_eq
      · exact panel10Mode22MatVec_eq
      · exact panel10Mode24MatVec_eq
      · exact panel10Mode26MatVec_eq
      · exact panel10Mode28MatVec_eq
      · exact panel10Mode30MatVec_eq
      · exact panel10Mode32MatVec_eq
      · exact panel10Mode34MatVec_eq
      · exact panel10Mode36MatVec_eq
      · exact panel10Mode38MatVec_eq
      · exact panel10Mode40MatVec_eq
      · exact panel10Mode42MatVec_eq
      · exact panel10Mode44MatVec_eq
      · exact panel10Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel10Mode1MatVec_eq
      · exact panel10Mode3MatVec_eq
      · exact panel10Mode5MatVec_eq
      · exact panel10Mode7MatVec_eq
      · exact panel10Mode9MatVec_eq
      · exact panel10Mode11MatVec_eq
      · exact panel10Mode13MatVec_eq
      · exact panel10Mode15MatVec_eq
      · exact panel10Mode17MatVec_eq
      · exact panel10Mode19MatVec_eq
      · exact panel10Mode21MatVec_eq
      · exact panel10Mode23MatVec_eq
      · exact panel10Mode25MatVec_eq
      · exact panel10Mode27MatVec_eq
      · exact panel10Mode29MatVec_eq
      · exact panel10Mode31MatVec_eq
      · exact panel10Mode33MatVec_eq
      · exact panel10Mode35MatVec_eq
      · exact panel10Mode37MatVec_eq
      · exact panel10Mode39MatVec_eq
      · exact panel10Mode41MatVec_eq
      · exact panel10Mode43MatVec_eq
      · exact panel10Mode45MatVec_eq
      · exact panel10Mode47MatVec_eq

end RHP2Bridge
