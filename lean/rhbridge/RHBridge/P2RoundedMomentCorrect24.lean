import RHBridge.P2RoundedFlatFactorCheckpoint24
import RHBridge.P2RoundedMomentLengths24
import RHBridge.P2RoundedMomentCheckpointCheck24_moments
import RHBridge.P2RoundedMomentCheckpointCheck24_mode0
import RHBridge.P2RoundedMomentCheckpointCheck24_mode1
import RHBridge.P2RoundedMomentCheckpointCheck24_mode2
import RHBridge.P2RoundedMomentCheckpointCheck24_mode3
import RHBridge.P2RoundedMomentCheckpointCheck24_mode4
import RHBridge.P2RoundedMomentCheckpointCheck24_mode5
import RHBridge.P2RoundedMomentCheckpointCheck24_mode6
import RHBridge.P2RoundedMomentCheckpointCheck24_mode7
import RHBridge.P2RoundedMomentCheckpointCheck24_mode8
import RHBridge.P2RoundedMomentCheckpointCheck24_mode9
import RHBridge.P2RoundedMomentCheckpointCheck24_mode10
import RHBridge.P2RoundedMomentCheckpointCheck24_mode11
import RHBridge.P2RoundedMomentCheckpointCheck24_mode12
import RHBridge.P2RoundedMomentCheckpointCheck24_mode13
import RHBridge.P2RoundedMomentCheckpointCheck24_mode14
import RHBridge.P2RoundedMomentCheckpointCheck24_mode15
import RHBridge.P2RoundedMomentCheckpointCheck24_mode16
import RHBridge.P2RoundedMomentCheckpointCheck24_mode17
import RHBridge.P2RoundedMomentCheckpointCheck24_mode18
import RHBridge.P2RoundedMomentCheckpointCheck24_mode19
import RHBridge.P2RoundedMomentCheckpointCheck24_mode20
import RHBridge.P2RoundedMomentCheckpointCheck24_mode21
import RHBridge.P2RoundedMomentCheckpointCheck24_mode22
import RHBridge.P2RoundedMomentCheckpointCheck24_mode23
import RHBridge.P2RoundedMomentCheckpointCheck24_mode24
import RHBridge.P2RoundedMomentCheckpointCheck24_mode25
import RHBridge.P2RoundedMomentCheckpointCheck24_mode26
import RHBridge.P2RoundedMomentCheckpointCheck24_mode27
import RHBridge.P2RoundedMomentCheckpointCheck24_mode28
import RHBridge.P2RoundedMomentCheckpointCheck24_mode29
import RHBridge.P2RoundedMomentCheckpointCheck24_mode30
import RHBridge.P2RoundedMomentCheckpointCheck24_mode31
import RHBridge.P2RoundedMomentCheckpointCheck24_mode32
import RHBridge.P2RoundedMomentCheckpointCheck24_mode33
import RHBridge.P2RoundedMomentCheckpointCheck24_mode34
import RHBridge.P2RoundedMomentCheckpointCheck24_mode35
import RHBridge.P2RoundedMomentCheckpointCheck24_mode36
import RHBridge.P2RoundedMomentCheckpointCheck24_mode37
import RHBridge.P2RoundedMomentCheckpointCheck24_mode38
import RHBridge.P2RoundedMomentCheckpointCheck24_mode39
import RHBridge.P2RoundedMomentCheckpointCheck24_mode40
import RHBridge.P2RoundedMomentCheckpointCheck24_mode41
import RHBridge.P2RoundedMomentCheckpointCheck24_mode42
import RHBridge.P2RoundedMomentCheckpointCheck24_mode43
import RHBridge.P2RoundedMomentCheckpointCheck24_mode44
import RHBridge.P2RoundedMomentCheckpointCheck24_mode45
import RHBridge.P2RoundedMomentCheckpointCheck24_mode46
import RHBridge.P2RoundedMomentCheckpointCheck24_mode47

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

theorem panel24DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel24FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24DefectMomentRange0) panel24DefectMomentRange64) panel24DefectMomentRange128) panel24DefectMomentRange192) panel24DefectMomentRange256) row

theorem panel24Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode0MatVecRange0) panel24Mode0MatVecRange32) panel24Mode0MatVecRange64) panel24Mode0MatVecRange96) panel24Mode0MatVecRange128) row

theorem panel24Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode1MatVecRange0) panel24Mode1MatVecRange32) panel24Mode1MatVecRange64) panel24Mode1MatVecRange96) panel24Mode1MatVecRange128) row

theorem panel24Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode2MatVecRange0) panel24Mode2MatVecRange32) panel24Mode2MatVecRange64) panel24Mode2MatVecRange96) panel24Mode2MatVecRange128) row

theorem panel24Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode3MatVecRange0) panel24Mode3MatVecRange32) panel24Mode3MatVecRange64) panel24Mode3MatVecRange96) panel24Mode3MatVecRange128) row

theorem panel24Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode4MatVecRange0) panel24Mode4MatVecRange32) panel24Mode4MatVecRange64) panel24Mode4MatVecRange96) panel24Mode4MatVecRange128) row

theorem panel24Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode5MatVecRange0) panel24Mode5MatVecRange32) panel24Mode5MatVecRange64) panel24Mode5MatVecRange96) panel24Mode5MatVecRange128) row

theorem panel24Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode6MatVecRange0) panel24Mode6MatVecRange32) panel24Mode6MatVecRange64) panel24Mode6MatVecRange96) panel24Mode6MatVecRange128) row

theorem panel24Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode7MatVecRange0) panel24Mode7MatVecRange32) panel24Mode7MatVecRange64) panel24Mode7MatVecRange96) panel24Mode7MatVecRange128) row

theorem panel24Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode8MatVecRange0) panel24Mode8MatVecRange32) panel24Mode8MatVecRange64) panel24Mode8MatVecRange96) panel24Mode8MatVecRange128) row

theorem panel24Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode9MatVecRange0) panel24Mode9MatVecRange32) panel24Mode9MatVecRange64) panel24Mode9MatVecRange96) panel24Mode9MatVecRange128) row

theorem panel24Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode10MatVecRange0) panel24Mode10MatVecRange32) panel24Mode10MatVecRange64) panel24Mode10MatVecRange96) panel24Mode10MatVecRange128) row

theorem panel24Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode11MatVecRange0) panel24Mode11MatVecRange32) panel24Mode11MatVecRange64) panel24Mode11MatVecRange96) panel24Mode11MatVecRange128) row

theorem panel24Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode12MatVecRange0) panel24Mode12MatVecRange32) panel24Mode12MatVecRange64) panel24Mode12MatVecRange96) panel24Mode12MatVecRange128) row

theorem panel24Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode13MatVecRange0) panel24Mode13MatVecRange32) panel24Mode13MatVecRange64) panel24Mode13MatVecRange96) panel24Mode13MatVecRange128) row

theorem panel24Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode14MatVecRange0) panel24Mode14MatVecRange32) panel24Mode14MatVecRange64) panel24Mode14MatVecRange96) panel24Mode14MatVecRange128) row

theorem panel24Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode15MatVecRange0) panel24Mode15MatVecRange32) panel24Mode15MatVecRange64) panel24Mode15MatVecRange96) panel24Mode15MatVecRange128) row

theorem panel24Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode16MatVecRange0) panel24Mode16MatVecRange32) panel24Mode16MatVecRange64) panel24Mode16MatVecRange96) panel24Mode16MatVecRange128) row

theorem panel24Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode17MatVecRange0) panel24Mode17MatVecRange32) panel24Mode17MatVecRange64) panel24Mode17MatVecRange96) panel24Mode17MatVecRange128) row

theorem panel24Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode18MatVecRange0) panel24Mode18MatVecRange32) panel24Mode18MatVecRange64) panel24Mode18MatVecRange96) panel24Mode18MatVecRange128) row

theorem panel24Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode19MatVecRange0) panel24Mode19MatVecRange32) panel24Mode19MatVecRange64) panel24Mode19MatVecRange96) panel24Mode19MatVecRange128) row

theorem panel24Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode20MatVecRange0) panel24Mode20MatVecRange32) panel24Mode20MatVecRange64) panel24Mode20MatVecRange96) panel24Mode20MatVecRange128) row

theorem panel24Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode21MatVecRange0) panel24Mode21MatVecRange32) panel24Mode21MatVecRange64) panel24Mode21MatVecRange96) panel24Mode21MatVecRange128) row

theorem panel24Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode22MatVecRange0) panel24Mode22MatVecRange32) panel24Mode22MatVecRange64) panel24Mode22MatVecRange96) panel24Mode22MatVecRange128) row

theorem panel24Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode23MatVecRange0) panel24Mode23MatVecRange32) panel24Mode23MatVecRange64) panel24Mode23MatVecRange96) panel24Mode23MatVecRange128) row

theorem panel24Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode24MatVecRange0) panel24Mode24MatVecRange32) panel24Mode24MatVecRange64) panel24Mode24MatVecRange96) panel24Mode24MatVecRange128) row

theorem panel24Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode25MatVecRange0) panel24Mode25MatVecRange32) panel24Mode25MatVecRange64) panel24Mode25MatVecRange96) panel24Mode25MatVecRange128) row

theorem panel24Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode26MatVecRange0) panel24Mode26MatVecRange32) panel24Mode26MatVecRange64) panel24Mode26MatVecRange96) panel24Mode26MatVecRange128) row

theorem panel24Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode27MatVecRange0) panel24Mode27MatVecRange32) panel24Mode27MatVecRange64) panel24Mode27MatVecRange96) panel24Mode27MatVecRange128) row

theorem panel24Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode28MatVecRange0) panel24Mode28MatVecRange32) panel24Mode28MatVecRange64) panel24Mode28MatVecRange96) panel24Mode28MatVecRange128) row

theorem panel24Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode29MatVecRange0) panel24Mode29MatVecRange32) panel24Mode29MatVecRange64) panel24Mode29MatVecRange96) panel24Mode29MatVecRange128) row

theorem panel24Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode30MatVecRange0) panel24Mode30MatVecRange32) panel24Mode30MatVecRange64) panel24Mode30MatVecRange96) panel24Mode30MatVecRange128) row

theorem panel24Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode31MatVecRange0) panel24Mode31MatVecRange32) panel24Mode31MatVecRange64) panel24Mode31MatVecRange96) panel24Mode31MatVecRange128) row

theorem panel24Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode32MatVecRange0) panel24Mode32MatVecRange32) panel24Mode32MatVecRange64) panel24Mode32MatVecRange96) panel24Mode32MatVecRange128) row

theorem panel24Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode33MatVecRange0) panel24Mode33MatVecRange32) panel24Mode33MatVecRange64) panel24Mode33MatVecRange96) panel24Mode33MatVecRange128) row

theorem panel24Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode34MatVecRange0) panel24Mode34MatVecRange32) panel24Mode34MatVecRange64) panel24Mode34MatVecRange96) panel24Mode34MatVecRange128) row

theorem panel24Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode35MatVecRange0) panel24Mode35MatVecRange32) panel24Mode35MatVecRange64) panel24Mode35MatVecRange96) panel24Mode35MatVecRange128) row

theorem panel24Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode36MatVecRange0) panel24Mode36MatVecRange32) panel24Mode36MatVecRange64) panel24Mode36MatVecRange96) panel24Mode36MatVecRange128) row

theorem panel24Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode37MatVecRange0) panel24Mode37MatVecRange32) panel24Mode37MatVecRange64) panel24Mode37MatVecRange96) panel24Mode37MatVecRange128) row

theorem panel24Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode38MatVecRange0) panel24Mode38MatVecRange32) panel24Mode38MatVecRange64) panel24Mode38MatVecRange96) panel24Mode38MatVecRange128) row

theorem panel24Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode39MatVecRange0) panel24Mode39MatVecRange32) panel24Mode39MatVecRange64) panel24Mode39MatVecRange96) panel24Mode39MatVecRange128) row

theorem panel24Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode40MatVecRange0) panel24Mode40MatVecRange32) panel24Mode40MatVecRange64) panel24Mode40MatVecRange96) panel24Mode40MatVecRange128) row

theorem panel24Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode41MatVecRange0) panel24Mode41MatVecRange32) panel24Mode41MatVecRange64) panel24Mode41MatVecRange96) panel24Mode41MatVecRange128) row

theorem panel24Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode42MatVecRange0) panel24Mode42MatVecRange32) panel24Mode42MatVecRange64) panel24Mode42MatVecRange96) panel24Mode42MatVecRange128) row

theorem panel24Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode43MatVecRange0) panel24Mode43MatVecRange32) panel24Mode43MatVecRange64) panel24Mode43MatVecRange96) panel24Mode43MatVecRange128) row

theorem panel24Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode44MatVecRange0) panel24Mode44MatVecRange32) panel24Mode44MatVecRange64) panel24Mode44MatVecRange96) panel24Mode44MatVecRange128) row

theorem panel24Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode45MatVecRange0) panel24Mode45MatVecRange32) panel24Mode45MatVecRange64) panel24Mode45MatVecRange96) panel24Mode45MatVecRange128) row

theorem panel24Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode46MatVecRange0) panel24Mode46MatVecRange32) panel24Mode46MatVecRange64) panel24Mode46MatVecRange96) panel24Mode46MatVecRange128) row

theorem panel24Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel24MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel24MomentData.moments
        (P2RoundedFactorCheckpointData.panel24FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel24Mode47MatVecRange0) panel24Mode47MatVecRange32) panel24Mode47MatVecRange64) panel24Mode47MatVecRange96) panel24Mode47MatVecRange128) row

theorem panel24MomentData_correct :
    P2RoundedFactorCheckpointData.panel24MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel24FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel24DefectMoments_eq panel24ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel24Mode0MatVec_eq
      · exact panel24Mode2MatVec_eq
      · exact panel24Mode4MatVec_eq
      · exact panel24Mode6MatVec_eq
      · exact panel24Mode8MatVec_eq
      · exact panel24Mode10MatVec_eq
      · exact panel24Mode12MatVec_eq
      · exact panel24Mode14MatVec_eq
      · exact panel24Mode16MatVec_eq
      · exact panel24Mode18MatVec_eq
      · exact panel24Mode20MatVec_eq
      · exact panel24Mode22MatVec_eq
      · exact panel24Mode24MatVec_eq
      · exact panel24Mode26MatVec_eq
      · exact panel24Mode28MatVec_eq
      · exact panel24Mode30MatVec_eq
      · exact panel24Mode32MatVec_eq
      · exact panel24Mode34MatVec_eq
      · exact panel24Mode36MatVec_eq
      · exact panel24Mode38MatVec_eq
      · exact panel24Mode40MatVec_eq
      · exact panel24Mode42MatVec_eq
      · exact panel24Mode44MatVec_eq
      · exact panel24Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel24Mode1MatVec_eq
      · exact panel24Mode3MatVec_eq
      · exact panel24Mode5MatVec_eq
      · exact panel24Mode7MatVec_eq
      · exact panel24Mode9MatVec_eq
      · exact panel24Mode11MatVec_eq
      · exact panel24Mode13MatVec_eq
      · exact panel24Mode15MatVec_eq
      · exact panel24Mode17MatVec_eq
      · exact panel24Mode19MatVec_eq
      · exact panel24Mode21MatVec_eq
      · exact panel24Mode23MatVec_eq
      · exact panel24Mode25MatVec_eq
      · exact panel24Mode27MatVec_eq
      · exact panel24Mode29MatVec_eq
      · exact panel24Mode31MatVec_eq
      · exact panel24Mode33MatVec_eq
      · exact panel24Mode35MatVec_eq
      · exact panel24Mode37MatVec_eq
      · exact panel24Mode39MatVec_eq
      · exact panel24Mode41MatVec_eq
      · exact panel24Mode43MatVec_eq
      · exact panel24Mode45MatVec_eq
      · exact panel24Mode47MatVec_eq

end RHP2Bridge
