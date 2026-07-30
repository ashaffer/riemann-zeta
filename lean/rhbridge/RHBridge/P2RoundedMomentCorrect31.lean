import RHBridge.P2RoundedFlatFactorCheckpoint31
import RHBridge.P2RoundedMomentLengths31
import RHBridge.P2RoundedMomentCheckpointCheck31_moments
import RHBridge.P2RoundedMomentCheckpointCheck31_mode0
import RHBridge.P2RoundedMomentCheckpointCheck31_mode1
import RHBridge.P2RoundedMomentCheckpointCheck31_mode2
import RHBridge.P2RoundedMomentCheckpointCheck31_mode3
import RHBridge.P2RoundedMomentCheckpointCheck31_mode4
import RHBridge.P2RoundedMomentCheckpointCheck31_mode5
import RHBridge.P2RoundedMomentCheckpointCheck31_mode6
import RHBridge.P2RoundedMomentCheckpointCheck31_mode7
import RHBridge.P2RoundedMomentCheckpointCheck31_mode8
import RHBridge.P2RoundedMomentCheckpointCheck31_mode9
import RHBridge.P2RoundedMomentCheckpointCheck31_mode10
import RHBridge.P2RoundedMomentCheckpointCheck31_mode11
import RHBridge.P2RoundedMomentCheckpointCheck31_mode12
import RHBridge.P2RoundedMomentCheckpointCheck31_mode13
import RHBridge.P2RoundedMomentCheckpointCheck31_mode14
import RHBridge.P2RoundedMomentCheckpointCheck31_mode15
import RHBridge.P2RoundedMomentCheckpointCheck31_mode16
import RHBridge.P2RoundedMomentCheckpointCheck31_mode17
import RHBridge.P2RoundedMomentCheckpointCheck31_mode18
import RHBridge.P2RoundedMomentCheckpointCheck31_mode19
import RHBridge.P2RoundedMomentCheckpointCheck31_mode20
import RHBridge.P2RoundedMomentCheckpointCheck31_mode21
import RHBridge.P2RoundedMomentCheckpointCheck31_mode22
import RHBridge.P2RoundedMomentCheckpointCheck31_mode23
import RHBridge.P2RoundedMomentCheckpointCheck31_mode24
import RHBridge.P2RoundedMomentCheckpointCheck31_mode25
import RHBridge.P2RoundedMomentCheckpointCheck31_mode26
import RHBridge.P2RoundedMomentCheckpointCheck31_mode27
import RHBridge.P2RoundedMomentCheckpointCheck31_mode28
import RHBridge.P2RoundedMomentCheckpointCheck31_mode29
import RHBridge.P2RoundedMomentCheckpointCheck31_mode30
import RHBridge.P2RoundedMomentCheckpointCheck31_mode31
import RHBridge.P2RoundedMomentCheckpointCheck31_mode32
import RHBridge.P2RoundedMomentCheckpointCheck31_mode33
import RHBridge.P2RoundedMomentCheckpointCheck31_mode34
import RHBridge.P2RoundedMomentCheckpointCheck31_mode35
import RHBridge.P2RoundedMomentCheckpointCheck31_mode36
import RHBridge.P2RoundedMomentCheckpointCheck31_mode37
import RHBridge.P2RoundedMomentCheckpointCheck31_mode38
import RHBridge.P2RoundedMomentCheckpointCheck31_mode39
import RHBridge.P2RoundedMomentCheckpointCheck31_mode40
import RHBridge.P2RoundedMomentCheckpointCheck31_mode41
import RHBridge.P2RoundedMomentCheckpointCheck31_mode42
import RHBridge.P2RoundedMomentCheckpointCheck31_mode43
import RHBridge.P2RoundedMomentCheckpointCheck31_mode44
import RHBridge.P2RoundedMomentCheckpointCheck31_mode45
import RHBridge.P2RoundedMomentCheckpointCheck31_mode46
import RHBridge.P2RoundedMomentCheckpointCheck31_mode47

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

theorem panel31DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel31FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31DefectMomentRange0) panel31DefectMomentRange64) panel31DefectMomentRange128) panel31DefectMomentRange192) panel31DefectMomentRange256) row

theorem panel31Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode0MatVecRange0) panel31Mode0MatVecRange32) panel31Mode0MatVecRange64) panel31Mode0MatVecRange96) panel31Mode0MatVecRange128) row

theorem panel31Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode1MatVecRange0) panel31Mode1MatVecRange32) panel31Mode1MatVecRange64) panel31Mode1MatVecRange96) panel31Mode1MatVecRange128) row

theorem panel31Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode2MatVecRange0) panel31Mode2MatVecRange32) panel31Mode2MatVecRange64) panel31Mode2MatVecRange96) panel31Mode2MatVecRange128) row

theorem panel31Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode3MatVecRange0) panel31Mode3MatVecRange32) panel31Mode3MatVecRange64) panel31Mode3MatVecRange96) panel31Mode3MatVecRange128) row

theorem panel31Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode4MatVecRange0) panel31Mode4MatVecRange32) panel31Mode4MatVecRange64) panel31Mode4MatVecRange96) panel31Mode4MatVecRange128) row

theorem panel31Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode5MatVecRange0) panel31Mode5MatVecRange32) panel31Mode5MatVecRange64) panel31Mode5MatVecRange96) panel31Mode5MatVecRange128) row

theorem panel31Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode6MatVecRange0) panel31Mode6MatVecRange32) panel31Mode6MatVecRange64) panel31Mode6MatVecRange96) panel31Mode6MatVecRange128) row

theorem panel31Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode7MatVecRange0) panel31Mode7MatVecRange32) panel31Mode7MatVecRange64) panel31Mode7MatVecRange96) panel31Mode7MatVecRange128) row

theorem panel31Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode8MatVecRange0) panel31Mode8MatVecRange32) panel31Mode8MatVecRange64) panel31Mode8MatVecRange96) panel31Mode8MatVecRange128) row

theorem panel31Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode9MatVecRange0) panel31Mode9MatVecRange32) panel31Mode9MatVecRange64) panel31Mode9MatVecRange96) panel31Mode9MatVecRange128) row

theorem panel31Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode10MatVecRange0) panel31Mode10MatVecRange32) panel31Mode10MatVecRange64) panel31Mode10MatVecRange96) panel31Mode10MatVecRange128) row

theorem panel31Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode11MatVecRange0) panel31Mode11MatVecRange32) panel31Mode11MatVecRange64) panel31Mode11MatVecRange96) panel31Mode11MatVecRange128) row

theorem panel31Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode12MatVecRange0) panel31Mode12MatVecRange32) panel31Mode12MatVecRange64) panel31Mode12MatVecRange96) panel31Mode12MatVecRange128) row

theorem panel31Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode13MatVecRange0) panel31Mode13MatVecRange32) panel31Mode13MatVecRange64) panel31Mode13MatVecRange96) panel31Mode13MatVecRange128) row

theorem panel31Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode14MatVecRange0) panel31Mode14MatVecRange32) panel31Mode14MatVecRange64) panel31Mode14MatVecRange96) panel31Mode14MatVecRange128) row

theorem panel31Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode15MatVecRange0) panel31Mode15MatVecRange32) panel31Mode15MatVecRange64) panel31Mode15MatVecRange96) panel31Mode15MatVecRange128) row

theorem panel31Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode16MatVecRange0) panel31Mode16MatVecRange32) panel31Mode16MatVecRange64) panel31Mode16MatVecRange96) panel31Mode16MatVecRange128) row

theorem panel31Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode17MatVecRange0) panel31Mode17MatVecRange32) panel31Mode17MatVecRange64) panel31Mode17MatVecRange96) panel31Mode17MatVecRange128) row

theorem panel31Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode18MatVecRange0) panel31Mode18MatVecRange32) panel31Mode18MatVecRange64) panel31Mode18MatVecRange96) panel31Mode18MatVecRange128) row

theorem panel31Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode19MatVecRange0) panel31Mode19MatVecRange32) panel31Mode19MatVecRange64) panel31Mode19MatVecRange96) panel31Mode19MatVecRange128) row

theorem panel31Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode20MatVecRange0) panel31Mode20MatVecRange32) panel31Mode20MatVecRange64) panel31Mode20MatVecRange96) panel31Mode20MatVecRange128) row

theorem panel31Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode21MatVecRange0) panel31Mode21MatVecRange32) panel31Mode21MatVecRange64) panel31Mode21MatVecRange96) panel31Mode21MatVecRange128) row

theorem panel31Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode22MatVecRange0) panel31Mode22MatVecRange32) panel31Mode22MatVecRange64) panel31Mode22MatVecRange96) panel31Mode22MatVecRange128) row

theorem panel31Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode23MatVecRange0) panel31Mode23MatVecRange32) panel31Mode23MatVecRange64) panel31Mode23MatVecRange96) panel31Mode23MatVecRange128) row

theorem panel31Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode24MatVecRange0) panel31Mode24MatVecRange32) panel31Mode24MatVecRange64) panel31Mode24MatVecRange96) panel31Mode24MatVecRange128) row

theorem panel31Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode25MatVecRange0) panel31Mode25MatVecRange32) panel31Mode25MatVecRange64) panel31Mode25MatVecRange96) panel31Mode25MatVecRange128) row

theorem panel31Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode26MatVecRange0) panel31Mode26MatVecRange32) panel31Mode26MatVecRange64) panel31Mode26MatVecRange96) panel31Mode26MatVecRange128) row

theorem panel31Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode27MatVecRange0) panel31Mode27MatVecRange32) panel31Mode27MatVecRange64) panel31Mode27MatVecRange96) panel31Mode27MatVecRange128) row

theorem panel31Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode28MatVecRange0) panel31Mode28MatVecRange32) panel31Mode28MatVecRange64) panel31Mode28MatVecRange96) panel31Mode28MatVecRange128) row

theorem panel31Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode29MatVecRange0) panel31Mode29MatVecRange32) panel31Mode29MatVecRange64) panel31Mode29MatVecRange96) panel31Mode29MatVecRange128) row

theorem panel31Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode30MatVecRange0) panel31Mode30MatVecRange32) panel31Mode30MatVecRange64) panel31Mode30MatVecRange96) panel31Mode30MatVecRange128) row

theorem panel31Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode31MatVecRange0) panel31Mode31MatVecRange32) panel31Mode31MatVecRange64) panel31Mode31MatVecRange96) panel31Mode31MatVecRange128) row

theorem panel31Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode32MatVecRange0) panel31Mode32MatVecRange32) panel31Mode32MatVecRange64) panel31Mode32MatVecRange96) panel31Mode32MatVecRange128) row

theorem panel31Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode33MatVecRange0) panel31Mode33MatVecRange32) panel31Mode33MatVecRange64) panel31Mode33MatVecRange96) panel31Mode33MatVecRange128) row

theorem panel31Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode34MatVecRange0) panel31Mode34MatVecRange32) panel31Mode34MatVecRange64) panel31Mode34MatVecRange96) panel31Mode34MatVecRange128) row

theorem panel31Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode35MatVecRange0) panel31Mode35MatVecRange32) panel31Mode35MatVecRange64) panel31Mode35MatVecRange96) panel31Mode35MatVecRange128) row

theorem panel31Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode36MatVecRange0) panel31Mode36MatVecRange32) panel31Mode36MatVecRange64) panel31Mode36MatVecRange96) panel31Mode36MatVecRange128) row

theorem panel31Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode37MatVecRange0) panel31Mode37MatVecRange32) panel31Mode37MatVecRange64) panel31Mode37MatVecRange96) panel31Mode37MatVecRange128) row

theorem panel31Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode38MatVecRange0) panel31Mode38MatVecRange32) panel31Mode38MatVecRange64) panel31Mode38MatVecRange96) panel31Mode38MatVecRange128) row

theorem panel31Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode39MatVecRange0) panel31Mode39MatVecRange32) panel31Mode39MatVecRange64) panel31Mode39MatVecRange96) panel31Mode39MatVecRange128) row

theorem panel31Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode40MatVecRange0) panel31Mode40MatVecRange32) panel31Mode40MatVecRange64) panel31Mode40MatVecRange96) panel31Mode40MatVecRange128) row

theorem panel31Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode41MatVecRange0) panel31Mode41MatVecRange32) panel31Mode41MatVecRange64) panel31Mode41MatVecRange96) panel31Mode41MatVecRange128) row

theorem panel31Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode42MatVecRange0) panel31Mode42MatVecRange32) panel31Mode42MatVecRange64) panel31Mode42MatVecRange96) panel31Mode42MatVecRange128) row

theorem panel31Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode43MatVecRange0) panel31Mode43MatVecRange32) panel31Mode43MatVecRange64) panel31Mode43MatVecRange96) panel31Mode43MatVecRange128) row

theorem panel31Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode44MatVecRange0) panel31Mode44MatVecRange32) panel31Mode44MatVecRange64) panel31Mode44MatVecRange96) panel31Mode44MatVecRange128) row

theorem panel31Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode45MatVecRange0) panel31Mode45MatVecRange32) panel31Mode45MatVecRange64) panel31Mode45MatVecRange96) panel31Mode45MatVecRange128) row

theorem panel31Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode46MatVecRange0) panel31Mode46MatVecRange32) panel31Mode46MatVecRange64) panel31Mode46MatVecRange96) panel31Mode46MatVecRange128) row

theorem panel31Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel31MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel31MomentData.moments
        (P2RoundedFactorCheckpointData.panel31FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel31Mode47MatVecRange0) panel31Mode47MatVecRange32) panel31Mode47MatVecRange64) panel31Mode47MatVecRange96) panel31Mode47MatVecRange128) row

theorem panel31MomentData_correct :
    P2RoundedFactorCheckpointData.panel31MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel31FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel31DefectMoments_eq panel31ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel31Mode0MatVec_eq
      · exact panel31Mode2MatVec_eq
      · exact panel31Mode4MatVec_eq
      · exact panel31Mode6MatVec_eq
      · exact panel31Mode8MatVec_eq
      · exact panel31Mode10MatVec_eq
      · exact panel31Mode12MatVec_eq
      · exact panel31Mode14MatVec_eq
      · exact panel31Mode16MatVec_eq
      · exact panel31Mode18MatVec_eq
      · exact panel31Mode20MatVec_eq
      · exact panel31Mode22MatVec_eq
      · exact panel31Mode24MatVec_eq
      · exact panel31Mode26MatVec_eq
      · exact panel31Mode28MatVec_eq
      · exact panel31Mode30MatVec_eq
      · exact panel31Mode32MatVec_eq
      · exact panel31Mode34MatVec_eq
      · exact panel31Mode36MatVec_eq
      · exact panel31Mode38MatVec_eq
      · exact panel31Mode40MatVec_eq
      · exact panel31Mode42MatVec_eq
      · exact panel31Mode44MatVec_eq
      · exact panel31Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel31Mode1MatVec_eq
      · exact panel31Mode3MatVec_eq
      · exact panel31Mode5MatVec_eq
      · exact panel31Mode7MatVec_eq
      · exact panel31Mode9MatVec_eq
      · exact panel31Mode11MatVec_eq
      · exact panel31Mode13MatVec_eq
      · exact panel31Mode15MatVec_eq
      · exact panel31Mode17MatVec_eq
      · exact panel31Mode19MatVec_eq
      · exact panel31Mode21MatVec_eq
      · exact panel31Mode23MatVec_eq
      · exact panel31Mode25MatVec_eq
      · exact panel31Mode27MatVec_eq
      · exact panel31Mode29MatVec_eq
      · exact panel31Mode31MatVec_eq
      · exact panel31Mode33MatVec_eq
      · exact panel31Mode35MatVec_eq
      · exact panel31Mode37MatVec_eq
      · exact panel31Mode39MatVec_eq
      · exact panel31Mode41MatVec_eq
      · exact panel31Mode43MatVec_eq
      · exact panel31Mode45MatVec_eq
      · exact panel31Mode47MatVec_eq

end RHP2Bridge
