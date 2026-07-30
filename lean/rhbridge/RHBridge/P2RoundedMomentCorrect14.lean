import RHBridge.P2RoundedFlatFactorCheckpoint14
import RHBridge.P2RoundedMomentLengths14
import RHBridge.P2RoundedMomentCheckpointCheck14_moments
import RHBridge.P2RoundedMomentCheckpointCheck14_mode0
import RHBridge.P2RoundedMomentCheckpointCheck14_mode1
import RHBridge.P2RoundedMomentCheckpointCheck14_mode2
import RHBridge.P2RoundedMomentCheckpointCheck14_mode3
import RHBridge.P2RoundedMomentCheckpointCheck14_mode4
import RHBridge.P2RoundedMomentCheckpointCheck14_mode5
import RHBridge.P2RoundedMomentCheckpointCheck14_mode6
import RHBridge.P2RoundedMomentCheckpointCheck14_mode7
import RHBridge.P2RoundedMomentCheckpointCheck14_mode8
import RHBridge.P2RoundedMomentCheckpointCheck14_mode9
import RHBridge.P2RoundedMomentCheckpointCheck14_mode10
import RHBridge.P2RoundedMomentCheckpointCheck14_mode11
import RHBridge.P2RoundedMomentCheckpointCheck14_mode12
import RHBridge.P2RoundedMomentCheckpointCheck14_mode13
import RHBridge.P2RoundedMomentCheckpointCheck14_mode14
import RHBridge.P2RoundedMomentCheckpointCheck14_mode15
import RHBridge.P2RoundedMomentCheckpointCheck14_mode16
import RHBridge.P2RoundedMomentCheckpointCheck14_mode17
import RHBridge.P2RoundedMomentCheckpointCheck14_mode18
import RHBridge.P2RoundedMomentCheckpointCheck14_mode19
import RHBridge.P2RoundedMomentCheckpointCheck14_mode20
import RHBridge.P2RoundedMomentCheckpointCheck14_mode21
import RHBridge.P2RoundedMomentCheckpointCheck14_mode22
import RHBridge.P2RoundedMomentCheckpointCheck14_mode23
import RHBridge.P2RoundedMomentCheckpointCheck14_mode24
import RHBridge.P2RoundedMomentCheckpointCheck14_mode25
import RHBridge.P2RoundedMomentCheckpointCheck14_mode26
import RHBridge.P2RoundedMomentCheckpointCheck14_mode27
import RHBridge.P2RoundedMomentCheckpointCheck14_mode28
import RHBridge.P2RoundedMomentCheckpointCheck14_mode29
import RHBridge.P2RoundedMomentCheckpointCheck14_mode30
import RHBridge.P2RoundedMomentCheckpointCheck14_mode31
import RHBridge.P2RoundedMomentCheckpointCheck14_mode32
import RHBridge.P2RoundedMomentCheckpointCheck14_mode33
import RHBridge.P2RoundedMomentCheckpointCheck14_mode34
import RHBridge.P2RoundedMomentCheckpointCheck14_mode35
import RHBridge.P2RoundedMomentCheckpointCheck14_mode36
import RHBridge.P2RoundedMomentCheckpointCheck14_mode37
import RHBridge.P2RoundedMomentCheckpointCheck14_mode38
import RHBridge.P2RoundedMomentCheckpointCheck14_mode39
import RHBridge.P2RoundedMomentCheckpointCheck14_mode40
import RHBridge.P2RoundedMomentCheckpointCheck14_mode41
import RHBridge.P2RoundedMomentCheckpointCheck14_mode42
import RHBridge.P2RoundedMomentCheckpointCheck14_mode43
import RHBridge.P2RoundedMomentCheckpointCheck14_mode44
import RHBridge.P2RoundedMomentCheckpointCheck14_mode45
import RHBridge.P2RoundedMomentCheckpointCheck14_mode46
import RHBridge.P2RoundedMomentCheckpointCheck14_mode47

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

theorem panel14DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel14FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14DefectMomentRange0) panel14DefectMomentRange64) panel14DefectMomentRange128) panel14DefectMomentRange192) panel14DefectMomentRange256) row

theorem panel14Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode0MatVecRange0) panel14Mode0MatVecRange32) panel14Mode0MatVecRange64) panel14Mode0MatVecRange96) panel14Mode0MatVecRange128) row

theorem panel14Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode1MatVecRange0) panel14Mode1MatVecRange32) panel14Mode1MatVecRange64) panel14Mode1MatVecRange96) panel14Mode1MatVecRange128) row

theorem panel14Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode2MatVecRange0) panel14Mode2MatVecRange32) panel14Mode2MatVecRange64) panel14Mode2MatVecRange96) panel14Mode2MatVecRange128) row

theorem panel14Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode3MatVecRange0) panel14Mode3MatVecRange32) panel14Mode3MatVecRange64) panel14Mode3MatVecRange96) panel14Mode3MatVecRange128) row

theorem panel14Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode4MatVecRange0) panel14Mode4MatVecRange32) panel14Mode4MatVecRange64) panel14Mode4MatVecRange96) panel14Mode4MatVecRange128) row

theorem panel14Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode5MatVecRange0) panel14Mode5MatVecRange32) panel14Mode5MatVecRange64) panel14Mode5MatVecRange96) panel14Mode5MatVecRange128) row

theorem panel14Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode6MatVecRange0) panel14Mode6MatVecRange32) panel14Mode6MatVecRange64) panel14Mode6MatVecRange96) panel14Mode6MatVecRange128) row

theorem panel14Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode7MatVecRange0) panel14Mode7MatVecRange32) panel14Mode7MatVecRange64) panel14Mode7MatVecRange96) panel14Mode7MatVecRange128) row

theorem panel14Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode8MatVecRange0) panel14Mode8MatVecRange32) panel14Mode8MatVecRange64) panel14Mode8MatVecRange96) panel14Mode8MatVecRange128) row

theorem panel14Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode9MatVecRange0) panel14Mode9MatVecRange32) panel14Mode9MatVecRange64) panel14Mode9MatVecRange96) panel14Mode9MatVecRange128) row

theorem panel14Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode10MatVecRange0) panel14Mode10MatVecRange32) panel14Mode10MatVecRange64) panel14Mode10MatVecRange96) panel14Mode10MatVecRange128) row

theorem panel14Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode11MatVecRange0) panel14Mode11MatVecRange32) panel14Mode11MatVecRange64) panel14Mode11MatVecRange96) panel14Mode11MatVecRange128) row

theorem panel14Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode12MatVecRange0) panel14Mode12MatVecRange32) panel14Mode12MatVecRange64) panel14Mode12MatVecRange96) panel14Mode12MatVecRange128) row

theorem panel14Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode13MatVecRange0) panel14Mode13MatVecRange32) panel14Mode13MatVecRange64) panel14Mode13MatVecRange96) panel14Mode13MatVecRange128) row

theorem panel14Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode14MatVecRange0) panel14Mode14MatVecRange32) panel14Mode14MatVecRange64) panel14Mode14MatVecRange96) panel14Mode14MatVecRange128) row

theorem panel14Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode15MatVecRange0) panel14Mode15MatVecRange32) panel14Mode15MatVecRange64) panel14Mode15MatVecRange96) panel14Mode15MatVecRange128) row

theorem panel14Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode16MatVecRange0) panel14Mode16MatVecRange32) panel14Mode16MatVecRange64) panel14Mode16MatVecRange96) panel14Mode16MatVecRange128) row

theorem panel14Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode17MatVecRange0) panel14Mode17MatVecRange32) panel14Mode17MatVecRange64) panel14Mode17MatVecRange96) panel14Mode17MatVecRange128) row

theorem panel14Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode18MatVecRange0) panel14Mode18MatVecRange32) panel14Mode18MatVecRange64) panel14Mode18MatVecRange96) panel14Mode18MatVecRange128) row

theorem panel14Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode19MatVecRange0) panel14Mode19MatVecRange32) panel14Mode19MatVecRange64) panel14Mode19MatVecRange96) panel14Mode19MatVecRange128) row

theorem panel14Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode20MatVecRange0) panel14Mode20MatVecRange32) panel14Mode20MatVecRange64) panel14Mode20MatVecRange96) panel14Mode20MatVecRange128) row

theorem panel14Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode21MatVecRange0) panel14Mode21MatVecRange32) panel14Mode21MatVecRange64) panel14Mode21MatVecRange96) panel14Mode21MatVecRange128) row

theorem panel14Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode22MatVecRange0) panel14Mode22MatVecRange32) panel14Mode22MatVecRange64) panel14Mode22MatVecRange96) panel14Mode22MatVecRange128) row

theorem panel14Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode23MatVecRange0) panel14Mode23MatVecRange32) panel14Mode23MatVecRange64) panel14Mode23MatVecRange96) panel14Mode23MatVecRange128) row

theorem panel14Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode24MatVecRange0) panel14Mode24MatVecRange32) panel14Mode24MatVecRange64) panel14Mode24MatVecRange96) panel14Mode24MatVecRange128) row

theorem panel14Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode25MatVecRange0) panel14Mode25MatVecRange32) panel14Mode25MatVecRange64) panel14Mode25MatVecRange96) panel14Mode25MatVecRange128) row

theorem panel14Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode26MatVecRange0) panel14Mode26MatVecRange32) panel14Mode26MatVecRange64) panel14Mode26MatVecRange96) panel14Mode26MatVecRange128) row

theorem panel14Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode27MatVecRange0) panel14Mode27MatVecRange32) panel14Mode27MatVecRange64) panel14Mode27MatVecRange96) panel14Mode27MatVecRange128) row

theorem panel14Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode28MatVecRange0) panel14Mode28MatVecRange32) panel14Mode28MatVecRange64) panel14Mode28MatVecRange96) panel14Mode28MatVecRange128) row

theorem panel14Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode29MatVecRange0) panel14Mode29MatVecRange32) panel14Mode29MatVecRange64) panel14Mode29MatVecRange96) panel14Mode29MatVecRange128) row

theorem panel14Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode30MatVecRange0) panel14Mode30MatVecRange32) panel14Mode30MatVecRange64) panel14Mode30MatVecRange96) panel14Mode30MatVecRange128) row

theorem panel14Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode31MatVecRange0) panel14Mode31MatVecRange32) panel14Mode31MatVecRange64) panel14Mode31MatVecRange96) panel14Mode31MatVecRange128) row

theorem panel14Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode32MatVecRange0) panel14Mode32MatVecRange32) panel14Mode32MatVecRange64) panel14Mode32MatVecRange96) panel14Mode32MatVecRange128) row

theorem panel14Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode33MatVecRange0) panel14Mode33MatVecRange32) panel14Mode33MatVecRange64) panel14Mode33MatVecRange96) panel14Mode33MatVecRange128) row

theorem panel14Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode34MatVecRange0) panel14Mode34MatVecRange32) panel14Mode34MatVecRange64) panel14Mode34MatVecRange96) panel14Mode34MatVecRange128) row

theorem panel14Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode35MatVecRange0) panel14Mode35MatVecRange32) panel14Mode35MatVecRange64) panel14Mode35MatVecRange96) panel14Mode35MatVecRange128) row

theorem panel14Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode36MatVecRange0) panel14Mode36MatVecRange32) panel14Mode36MatVecRange64) panel14Mode36MatVecRange96) panel14Mode36MatVecRange128) row

theorem panel14Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode37MatVecRange0) panel14Mode37MatVecRange32) panel14Mode37MatVecRange64) panel14Mode37MatVecRange96) panel14Mode37MatVecRange128) row

theorem panel14Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode38MatVecRange0) panel14Mode38MatVecRange32) panel14Mode38MatVecRange64) panel14Mode38MatVecRange96) panel14Mode38MatVecRange128) row

theorem panel14Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode39MatVecRange0) panel14Mode39MatVecRange32) panel14Mode39MatVecRange64) panel14Mode39MatVecRange96) panel14Mode39MatVecRange128) row

theorem panel14Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode40MatVecRange0) panel14Mode40MatVecRange32) panel14Mode40MatVecRange64) panel14Mode40MatVecRange96) panel14Mode40MatVecRange128) row

theorem panel14Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode41MatVecRange0) panel14Mode41MatVecRange32) panel14Mode41MatVecRange64) panel14Mode41MatVecRange96) panel14Mode41MatVecRange128) row

theorem panel14Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode42MatVecRange0) panel14Mode42MatVecRange32) panel14Mode42MatVecRange64) panel14Mode42MatVecRange96) panel14Mode42MatVecRange128) row

theorem panel14Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode43MatVecRange0) panel14Mode43MatVecRange32) panel14Mode43MatVecRange64) panel14Mode43MatVecRange96) panel14Mode43MatVecRange128) row

theorem panel14Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode44MatVecRange0) panel14Mode44MatVecRange32) panel14Mode44MatVecRange64) panel14Mode44MatVecRange96) panel14Mode44MatVecRange128) row

theorem panel14Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode45MatVecRange0) panel14Mode45MatVecRange32) panel14Mode45MatVecRange64) panel14Mode45MatVecRange96) panel14Mode45MatVecRange128) row

theorem panel14Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode46MatVecRange0) panel14Mode46MatVecRange32) panel14Mode46MatVecRange64) panel14Mode46MatVecRange96) panel14Mode46MatVecRange128) row

theorem panel14Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel14MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel14MomentData.moments
        (P2RoundedFactorCheckpointData.panel14FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel14Mode47MatVecRange0) panel14Mode47MatVecRange32) panel14Mode47MatVecRange64) panel14Mode47MatVecRange96) panel14Mode47MatVecRange128) row

theorem panel14MomentData_correct :
    P2RoundedFactorCheckpointData.panel14MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel14FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel14DefectMoments_eq panel14ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel14Mode0MatVec_eq
      · exact panel14Mode2MatVec_eq
      · exact panel14Mode4MatVec_eq
      · exact panel14Mode6MatVec_eq
      · exact panel14Mode8MatVec_eq
      · exact panel14Mode10MatVec_eq
      · exact panel14Mode12MatVec_eq
      · exact panel14Mode14MatVec_eq
      · exact panel14Mode16MatVec_eq
      · exact panel14Mode18MatVec_eq
      · exact panel14Mode20MatVec_eq
      · exact panel14Mode22MatVec_eq
      · exact panel14Mode24MatVec_eq
      · exact panel14Mode26MatVec_eq
      · exact panel14Mode28MatVec_eq
      · exact panel14Mode30MatVec_eq
      · exact panel14Mode32MatVec_eq
      · exact panel14Mode34MatVec_eq
      · exact panel14Mode36MatVec_eq
      · exact panel14Mode38MatVec_eq
      · exact panel14Mode40MatVec_eq
      · exact panel14Mode42MatVec_eq
      · exact panel14Mode44MatVec_eq
      · exact panel14Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel14Mode1MatVec_eq
      · exact panel14Mode3MatVec_eq
      · exact panel14Mode5MatVec_eq
      · exact panel14Mode7MatVec_eq
      · exact panel14Mode9MatVec_eq
      · exact panel14Mode11MatVec_eq
      · exact panel14Mode13MatVec_eq
      · exact panel14Mode15MatVec_eq
      · exact panel14Mode17MatVec_eq
      · exact panel14Mode19MatVec_eq
      · exact panel14Mode21MatVec_eq
      · exact panel14Mode23MatVec_eq
      · exact panel14Mode25MatVec_eq
      · exact panel14Mode27MatVec_eq
      · exact panel14Mode29MatVec_eq
      · exact panel14Mode31MatVec_eq
      · exact panel14Mode33MatVec_eq
      · exact panel14Mode35MatVec_eq
      · exact panel14Mode37MatVec_eq
      · exact panel14Mode39MatVec_eq
      · exact panel14Mode41MatVec_eq
      · exact panel14Mode43MatVec_eq
      · exact panel14Mode45MatVec_eq
      · exact panel14Mode47MatVec_eq

end RHP2Bridge
