import RHBridge.P2RoundedFlatFactorCheckpoint4
import RHBridge.P2RoundedMomentLengths4
import RHBridge.P2RoundedMomentCheckpointCheck4_moments
import RHBridge.P2RoundedMomentCheckpointCheck4_mode0
import RHBridge.P2RoundedMomentCheckpointCheck4_mode1
import RHBridge.P2RoundedMomentCheckpointCheck4_mode2
import RHBridge.P2RoundedMomentCheckpointCheck4_mode3
import RHBridge.P2RoundedMomentCheckpointCheck4_mode4
import RHBridge.P2RoundedMomentCheckpointCheck4_mode5
import RHBridge.P2RoundedMomentCheckpointCheck4_mode6
import RHBridge.P2RoundedMomentCheckpointCheck4_mode7
import RHBridge.P2RoundedMomentCheckpointCheck4_mode8
import RHBridge.P2RoundedMomentCheckpointCheck4_mode9
import RHBridge.P2RoundedMomentCheckpointCheck4_mode10
import RHBridge.P2RoundedMomentCheckpointCheck4_mode11
import RHBridge.P2RoundedMomentCheckpointCheck4_mode12
import RHBridge.P2RoundedMomentCheckpointCheck4_mode13
import RHBridge.P2RoundedMomentCheckpointCheck4_mode14
import RHBridge.P2RoundedMomentCheckpointCheck4_mode15
import RHBridge.P2RoundedMomentCheckpointCheck4_mode16
import RHBridge.P2RoundedMomentCheckpointCheck4_mode17
import RHBridge.P2RoundedMomentCheckpointCheck4_mode18
import RHBridge.P2RoundedMomentCheckpointCheck4_mode19
import RHBridge.P2RoundedMomentCheckpointCheck4_mode20
import RHBridge.P2RoundedMomentCheckpointCheck4_mode21
import RHBridge.P2RoundedMomentCheckpointCheck4_mode22
import RHBridge.P2RoundedMomentCheckpointCheck4_mode23
import RHBridge.P2RoundedMomentCheckpointCheck4_mode24
import RHBridge.P2RoundedMomentCheckpointCheck4_mode25
import RHBridge.P2RoundedMomentCheckpointCheck4_mode26
import RHBridge.P2RoundedMomentCheckpointCheck4_mode27
import RHBridge.P2RoundedMomentCheckpointCheck4_mode28
import RHBridge.P2RoundedMomentCheckpointCheck4_mode29
import RHBridge.P2RoundedMomentCheckpointCheck4_mode30
import RHBridge.P2RoundedMomentCheckpointCheck4_mode31
import RHBridge.P2RoundedMomentCheckpointCheck4_mode32
import RHBridge.P2RoundedMomentCheckpointCheck4_mode33
import RHBridge.P2RoundedMomentCheckpointCheck4_mode34
import RHBridge.P2RoundedMomentCheckpointCheck4_mode35
import RHBridge.P2RoundedMomentCheckpointCheck4_mode36
import RHBridge.P2RoundedMomentCheckpointCheck4_mode37
import RHBridge.P2RoundedMomentCheckpointCheck4_mode38
import RHBridge.P2RoundedMomentCheckpointCheck4_mode39
import RHBridge.P2RoundedMomentCheckpointCheck4_mode40
import RHBridge.P2RoundedMomentCheckpointCheck4_mode41
import RHBridge.P2RoundedMomentCheckpointCheck4_mode42
import RHBridge.P2RoundedMomentCheckpointCheck4_mode43
import RHBridge.P2RoundedMomentCheckpointCheck4_mode44
import RHBridge.P2RoundedMomentCheckpointCheck4_mode45
import RHBridge.P2RoundedMomentCheckpointCheck4_mode46
import RHBridge.P2RoundedMomentCheckpointCheck4_mode47

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

theorem panel4DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel4FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4DefectMomentRange0) panel4DefectMomentRange64) panel4DefectMomentRange128) panel4DefectMomentRange192) panel4DefectMomentRange256) row

theorem panel4Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode0MatVecRange0) panel4Mode0MatVecRange32) panel4Mode0MatVecRange64) panel4Mode0MatVecRange96) panel4Mode0MatVecRange128) row

theorem panel4Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode1MatVecRange0) panel4Mode1MatVecRange32) panel4Mode1MatVecRange64) panel4Mode1MatVecRange96) panel4Mode1MatVecRange128) row

theorem panel4Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode2MatVecRange0) panel4Mode2MatVecRange32) panel4Mode2MatVecRange64) panel4Mode2MatVecRange96) panel4Mode2MatVecRange128) row

theorem panel4Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode3MatVecRange0) panel4Mode3MatVecRange32) panel4Mode3MatVecRange64) panel4Mode3MatVecRange96) panel4Mode3MatVecRange128) row

theorem panel4Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode4MatVecRange0) panel4Mode4MatVecRange32) panel4Mode4MatVecRange64) panel4Mode4MatVecRange96) panel4Mode4MatVecRange128) row

theorem panel4Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode5MatVecRange0) panel4Mode5MatVecRange32) panel4Mode5MatVecRange64) panel4Mode5MatVecRange96) panel4Mode5MatVecRange128) row

theorem panel4Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode6MatVecRange0) panel4Mode6MatVecRange32) panel4Mode6MatVecRange64) panel4Mode6MatVecRange96) panel4Mode6MatVecRange128) row

theorem panel4Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode7MatVecRange0) panel4Mode7MatVecRange32) panel4Mode7MatVecRange64) panel4Mode7MatVecRange96) panel4Mode7MatVecRange128) row

theorem panel4Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode8MatVecRange0) panel4Mode8MatVecRange32) panel4Mode8MatVecRange64) panel4Mode8MatVecRange96) panel4Mode8MatVecRange128) row

theorem panel4Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode9MatVecRange0) panel4Mode9MatVecRange32) panel4Mode9MatVecRange64) panel4Mode9MatVecRange96) panel4Mode9MatVecRange128) row

theorem panel4Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode10MatVecRange0) panel4Mode10MatVecRange32) panel4Mode10MatVecRange64) panel4Mode10MatVecRange96) panel4Mode10MatVecRange128) row

theorem panel4Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode11MatVecRange0) panel4Mode11MatVecRange32) panel4Mode11MatVecRange64) panel4Mode11MatVecRange96) panel4Mode11MatVecRange128) row

theorem panel4Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode12MatVecRange0) panel4Mode12MatVecRange32) panel4Mode12MatVecRange64) panel4Mode12MatVecRange96) panel4Mode12MatVecRange128) row

theorem panel4Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode13MatVecRange0) panel4Mode13MatVecRange32) panel4Mode13MatVecRange64) panel4Mode13MatVecRange96) panel4Mode13MatVecRange128) row

theorem panel4Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode14MatVecRange0) panel4Mode14MatVecRange32) panel4Mode14MatVecRange64) panel4Mode14MatVecRange96) panel4Mode14MatVecRange128) row

theorem panel4Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode15MatVecRange0) panel4Mode15MatVecRange32) panel4Mode15MatVecRange64) panel4Mode15MatVecRange96) panel4Mode15MatVecRange128) row

theorem panel4Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode16MatVecRange0) panel4Mode16MatVecRange32) panel4Mode16MatVecRange64) panel4Mode16MatVecRange96) panel4Mode16MatVecRange128) row

theorem panel4Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode17MatVecRange0) panel4Mode17MatVecRange32) panel4Mode17MatVecRange64) panel4Mode17MatVecRange96) panel4Mode17MatVecRange128) row

theorem panel4Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode18MatVecRange0) panel4Mode18MatVecRange32) panel4Mode18MatVecRange64) panel4Mode18MatVecRange96) panel4Mode18MatVecRange128) row

theorem panel4Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode19MatVecRange0) panel4Mode19MatVecRange32) panel4Mode19MatVecRange64) panel4Mode19MatVecRange96) panel4Mode19MatVecRange128) row

theorem panel4Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode20MatVecRange0) panel4Mode20MatVecRange32) panel4Mode20MatVecRange64) panel4Mode20MatVecRange96) panel4Mode20MatVecRange128) row

theorem panel4Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode21MatVecRange0) panel4Mode21MatVecRange32) panel4Mode21MatVecRange64) panel4Mode21MatVecRange96) panel4Mode21MatVecRange128) row

theorem panel4Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode22MatVecRange0) panel4Mode22MatVecRange32) panel4Mode22MatVecRange64) panel4Mode22MatVecRange96) panel4Mode22MatVecRange128) row

theorem panel4Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode23MatVecRange0) panel4Mode23MatVecRange32) panel4Mode23MatVecRange64) panel4Mode23MatVecRange96) panel4Mode23MatVecRange128) row

theorem panel4Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode24MatVecRange0) panel4Mode24MatVecRange32) panel4Mode24MatVecRange64) panel4Mode24MatVecRange96) panel4Mode24MatVecRange128) row

theorem panel4Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode25MatVecRange0) panel4Mode25MatVecRange32) panel4Mode25MatVecRange64) panel4Mode25MatVecRange96) panel4Mode25MatVecRange128) row

theorem panel4Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode26MatVecRange0) panel4Mode26MatVecRange32) panel4Mode26MatVecRange64) panel4Mode26MatVecRange96) panel4Mode26MatVecRange128) row

theorem panel4Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode27MatVecRange0) panel4Mode27MatVecRange32) panel4Mode27MatVecRange64) panel4Mode27MatVecRange96) panel4Mode27MatVecRange128) row

theorem panel4Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode28MatVecRange0) panel4Mode28MatVecRange32) panel4Mode28MatVecRange64) panel4Mode28MatVecRange96) panel4Mode28MatVecRange128) row

theorem panel4Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode29MatVecRange0) panel4Mode29MatVecRange32) panel4Mode29MatVecRange64) panel4Mode29MatVecRange96) panel4Mode29MatVecRange128) row

theorem panel4Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode30MatVecRange0) panel4Mode30MatVecRange32) panel4Mode30MatVecRange64) panel4Mode30MatVecRange96) panel4Mode30MatVecRange128) row

theorem panel4Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode31MatVecRange0) panel4Mode31MatVecRange32) panel4Mode31MatVecRange64) panel4Mode31MatVecRange96) panel4Mode31MatVecRange128) row

theorem panel4Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode32MatVecRange0) panel4Mode32MatVecRange32) panel4Mode32MatVecRange64) panel4Mode32MatVecRange96) panel4Mode32MatVecRange128) row

theorem panel4Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode33MatVecRange0) panel4Mode33MatVecRange32) panel4Mode33MatVecRange64) panel4Mode33MatVecRange96) panel4Mode33MatVecRange128) row

theorem panel4Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode34MatVecRange0) panel4Mode34MatVecRange32) panel4Mode34MatVecRange64) panel4Mode34MatVecRange96) panel4Mode34MatVecRange128) row

theorem panel4Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode35MatVecRange0) panel4Mode35MatVecRange32) panel4Mode35MatVecRange64) panel4Mode35MatVecRange96) panel4Mode35MatVecRange128) row

theorem panel4Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode36MatVecRange0) panel4Mode36MatVecRange32) panel4Mode36MatVecRange64) panel4Mode36MatVecRange96) panel4Mode36MatVecRange128) row

theorem panel4Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode37MatVecRange0) panel4Mode37MatVecRange32) panel4Mode37MatVecRange64) panel4Mode37MatVecRange96) panel4Mode37MatVecRange128) row

theorem panel4Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode38MatVecRange0) panel4Mode38MatVecRange32) panel4Mode38MatVecRange64) panel4Mode38MatVecRange96) panel4Mode38MatVecRange128) row

theorem panel4Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode39MatVecRange0) panel4Mode39MatVecRange32) panel4Mode39MatVecRange64) panel4Mode39MatVecRange96) panel4Mode39MatVecRange128) row

theorem panel4Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode40MatVecRange0) panel4Mode40MatVecRange32) panel4Mode40MatVecRange64) panel4Mode40MatVecRange96) panel4Mode40MatVecRange128) row

theorem panel4Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode41MatVecRange0) panel4Mode41MatVecRange32) panel4Mode41MatVecRange64) panel4Mode41MatVecRange96) panel4Mode41MatVecRange128) row

theorem panel4Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode42MatVecRange0) panel4Mode42MatVecRange32) panel4Mode42MatVecRange64) panel4Mode42MatVecRange96) panel4Mode42MatVecRange128) row

theorem panel4Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode43MatVecRange0) panel4Mode43MatVecRange32) panel4Mode43MatVecRange64) panel4Mode43MatVecRange96) panel4Mode43MatVecRange128) row

theorem panel4Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode44MatVecRange0) panel4Mode44MatVecRange32) panel4Mode44MatVecRange64) panel4Mode44MatVecRange96) panel4Mode44MatVecRange128) row

theorem panel4Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode45MatVecRange0) panel4Mode45MatVecRange32) panel4Mode45MatVecRange64) panel4Mode45MatVecRange96) panel4Mode45MatVecRange128) row

theorem panel4Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode46MatVecRange0) panel4Mode46MatVecRange32) panel4Mode46MatVecRange64) panel4Mode46MatVecRange96) panel4Mode46MatVecRange128) row

theorem panel4Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel4MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel4MomentData.moments
        (P2RoundedFactorCheckpointData.panel4FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel4Mode47MatVecRange0) panel4Mode47MatVecRange32) panel4Mode47MatVecRange64) panel4Mode47MatVecRange96) panel4Mode47MatVecRange128) row

theorem panel4MomentData_correct :
    P2RoundedFactorCheckpointData.panel4MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel4FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel4DefectMoments_eq panel4ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel4Mode0MatVec_eq
      · exact panel4Mode2MatVec_eq
      · exact panel4Mode4MatVec_eq
      · exact panel4Mode6MatVec_eq
      · exact panel4Mode8MatVec_eq
      · exact panel4Mode10MatVec_eq
      · exact panel4Mode12MatVec_eq
      · exact panel4Mode14MatVec_eq
      · exact panel4Mode16MatVec_eq
      · exact panel4Mode18MatVec_eq
      · exact panel4Mode20MatVec_eq
      · exact panel4Mode22MatVec_eq
      · exact panel4Mode24MatVec_eq
      · exact panel4Mode26MatVec_eq
      · exact panel4Mode28MatVec_eq
      · exact panel4Mode30MatVec_eq
      · exact panel4Mode32MatVec_eq
      · exact panel4Mode34MatVec_eq
      · exact panel4Mode36MatVec_eq
      · exact panel4Mode38MatVec_eq
      · exact panel4Mode40MatVec_eq
      · exact panel4Mode42MatVec_eq
      · exact panel4Mode44MatVec_eq
      · exact panel4Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel4Mode1MatVec_eq
      · exact panel4Mode3MatVec_eq
      · exact panel4Mode5MatVec_eq
      · exact panel4Mode7MatVec_eq
      · exact panel4Mode9MatVec_eq
      · exact panel4Mode11MatVec_eq
      · exact panel4Mode13MatVec_eq
      · exact panel4Mode15MatVec_eq
      · exact panel4Mode17MatVec_eq
      · exact panel4Mode19MatVec_eq
      · exact panel4Mode21MatVec_eq
      · exact panel4Mode23MatVec_eq
      · exact panel4Mode25MatVec_eq
      · exact panel4Mode27MatVec_eq
      · exact panel4Mode29MatVec_eq
      · exact panel4Mode31MatVec_eq
      · exact panel4Mode33MatVec_eq
      · exact panel4Mode35MatVec_eq
      · exact panel4Mode37MatVec_eq
      · exact panel4Mode39MatVec_eq
      · exact panel4Mode41MatVec_eq
      · exact panel4Mode43MatVec_eq
      · exact panel4Mode45MatVec_eq
      · exact panel4Mode47MatVec_eq

end RHP2Bridge
