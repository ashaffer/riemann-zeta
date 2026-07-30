import RHBridge.P2RoundedFlatFactorCheckpoint9
import RHBridge.P2RoundedMomentLengths9
import RHBridge.P2RoundedMomentCheckpointCheck9_moments
import RHBridge.P2RoundedMomentCheckpointCheck9_mode0
import RHBridge.P2RoundedMomentCheckpointCheck9_mode1
import RHBridge.P2RoundedMomentCheckpointCheck9_mode2
import RHBridge.P2RoundedMomentCheckpointCheck9_mode3
import RHBridge.P2RoundedMomentCheckpointCheck9_mode4
import RHBridge.P2RoundedMomentCheckpointCheck9_mode5
import RHBridge.P2RoundedMomentCheckpointCheck9_mode6
import RHBridge.P2RoundedMomentCheckpointCheck9_mode7
import RHBridge.P2RoundedMomentCheckpointCheck9_mode8
import RHBridge.P2RoundedMomentCheckpointCheck9_mode9
import RHBridge.P2RoundedMomentCheckpointCheck9_mode10
import RHBridge.P2RoundedMomentCheckpointCheck9_mode11
import RHBridge.P2RoundedMomentCheckpointCheck9_mode12
import RHBridge.P2RoundedMomentCheckpointCheck9_mode13
import RHBridge.P2RoundedMomentCheckpointCheck9_mode14
import RHBridge.P2RoundedMomentCheckpointCheck9_mode15
import RHBridge.P2RoundedMomentCheckpointCheck9_mode16
import RHBridge.P2RoundedMomentCheckpointCheck9_mode17
import RHBridge.P2RoundedMomentCheckpointCheck9_mode18
import RHBridge.P2RoundedMomentCheckpointCheck9_mode19
import RHBridge.P2RoundedMomentCheckpointCheck9_mode20
import RHBridge.P2RoundedMomentCheckpointCheck9_mode21
import RHBridge.P2RoundedMomentCheckpointCheck9_mode22
import RHBridge.P2RoundedMomentCheckpointCheck9_mode23
import RHBridge.P2RoundedMomentCheckpointCheck9_mode24
import RHBridge.P2RoundedMomentCheckpointCheck9_mode25
import RHBridge.P2RoundedMomentCheckpointCheck9_mode26
import RHBridge.P2RoundedMomentCheckpointCheck9_mode27
import RHBridge.P2RoundedMomentCheckpointCheck9_mode28
import RHBridge.P2RoundedMomentCheckpointCheck9_mode29
import RHBridge.P2RoundedMomentCheckpointCheck9_mode30
import RHBridge.P2RoundedMomentCheckpointCheck9_mode31
import RHBridge.P2RoundedMomentCheckpointCheck9_mode32
import RHBridge.P2RoundedMomentCheckpointCheck9_mode33
import RHBridge.P2RoundedMomentCheckpointCheck9_mode34
import RHBridge.P2RoundedMomentCheckpointCheck9_mode35
import RHBridge.P2RoundedMomentCheckpointCheck9_mode36
import RHBridge.P2RoundedMomentCheckpointCheck9_mode37
import RHBridge.P2RoundedMomentCheckpointCheck9_mode38
import RHBridge.P2RoundedMomentCheckpointCheck9_mode39
import RHBridge.P2RoundedMomentCheckpointCheck9_mode40
import RHBridge.P2RoundedMomentCheckpointCheck9_mode41
import RHBridge.P2RoundedMomentCheckpointCheck9_mode42
import RHBridge.P2RoundedMomentCheckpointCheck9_mode43
import RHBridge.P2RoundedMomentCheckpointCheck9_mode44
import RHBridge.P2RoundedMomentCheckpointCheck9_mode45
import RHBridge.P2RoundedMomentCheckpointCheck9_mode46
import RHBridge.P2RoundedMomentCheckpointCheck9_mode47

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

theorem panel9DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel9FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9DefectMomentRange0) panel9DefectMomentRange64) panel9DefectMomentRange128) panel9DefectMomentRange192) panel9DefectMomentRange256) row

theorem panel9Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode0MatVecRange0) panel9Mode0MatVecRange32) panel9Mode0MatVecRange64) panel9Mode0MatVecRange96) panel9Mode0MatVecRange128) row

theorem panel9Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode1MatVecRange0) panel9Mode1MatVecRange32) panel9Mode1MatVecRange64) panel9Mode1MatVecRange96) panel9Mode1MatVecRange128) row

theorem panel9Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode2MatVecRange0) panel9Mode2MatVecRange32) panel9Mode2MatVecRange64) panel9Mode2MatVecRange96) panel9Mode2MatVecRange128) row

theorem panel9Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode3MatVecRange0) panel9Mode3MatVecRange32) panel9Mode3MatVecRange64) panel9Mode3MatVecRange96) panel9Mode3MatVecRange128) row

theorem panel9Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode4MatVecRange0) panel9Mode4MatVecRange32) panel9Mode4MatVecRange64) panel9Mode4MatVecRange96) panel9Mode4MatVecRange128) row

theorem panel9Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode5MatVecRange0) panel9Mode5MatVecRange32) panel9Mode5MatVecRange64) panel9Mode5MatVecRange96) panel9Mode5MatVecRange128) row

theorem panel9Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode6MatVecRange0) panel9Mode6MatVecRange32) panel9Mode6MatVecRange64) panel9Mode6MatVecRange96) panel9Mode6MatVecRange128) row

theorem panel9Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode7MatVecRange0) panel9Mode7MatVecRange32) panel9Mode7MatVecRange64) panel9Mode7MatVecRange96) panel9Mode7MatVecRange128) row

theorem panel9Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode8MatVecRange0) panel9Mode8MatVecRange32) panel9Mode8MatVecRange64) panel9Mode8MatVecRange96) panel9Mode8MatVecRange128) row

theorem panel9Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode9MatVecRange0) panel9Mode9MatVecRange32) panel9Mode9MatVecRange64) panel9Mode9MatVecRange96) panel9Mode9MatVecRange128) row

theorem panel9Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode10MatVecRange0) panel9Mode10MatVecRange32) panel9Mode10MatVecRange64) panel9Mode10MatVecRange96) panel9Mode10MatVecRange128) row

theorem panel9Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode11MatVecRange0) panel9Mode11MatVecRange32) panel9Mode11MatVecRange64) panel9Mode11MatVecRange96) panel9Mode11MatVecRange128) row

theorem panel9Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode12MatVecRange0) panel9Mode12MatVecRange32) panel9Mode12MatVecRange64) panel9Mode12MatVecRange96) panel9Mode12MatVecRange128) row

theorem panel9Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode13MatVecRange0) panel9Mode13MatVecRange32) panel9Mode13MatVecRange64) panel9Mode13MatVecRange96) panel9Mode13MatVecRange128) row

theorem panel9Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode14MatVecRange0) panel9Mode14MatVecRange32) panel9Mode14MatVecRange64) panel9Mode14MatVecRange96) panel9Mode14MatVecRange128) row

theorem panel9Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode15MatVecRange0) panel9Mode15MatVecRange32) panel9Mode15MatVecRange64) panel9Mode15MatVecRange96) panel9Mode15MatVecRange128) row

theorem panel9Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode16MatVecRange0) panel9Mode16MatVecRange32) panel9Mode16MatVecRange64) panel9Mode16MatVecRange96) panel9Mode16MatVecRange128) row

theorem panel9Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode17MatVecRange0) panel9Mode17MatVecRange32) panel9Mode17MatVecRange64) panel9Mode17MatVecRange96) panel9Mode17MatVecRange128) row

theorem panel9Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode18MatVecRange0) panel9Mode18MatVecRange32) panel9Mode18MatVecRange64) panel9Mode18MatVecRange96) panel9Mode18MatVecRange128) row

theorem panel9Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode19MatVecRange0) panel9Mode19MatVecRange32) panel9Mode19MatVecRange64) panel9Mode19MatVecRange96) panel9Mode19MatVecRange128) row

theorem panel9Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode20MatVecRange0) panel9Mode20MatVecRange32) panel9Mode20MatVecRange64) panel9Mode20MatVecRange96) panel9Mode20MatVecRange128) row

theorem panel9Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode21MatVecRange0) panel9Mode21MatVecRange32) panel9Mode21MatVecRange64) panel9Mode21MatVecRange96) panel9Mode21MatVecRange128) row

theorem panel9Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode22MatVecRange0) panel9Mode22MatVecRange32) panel9Mode22MatVecRange64) panel9Mode22MatVecRange96) panel9Mode22MatVecRange128) row

theorem panel9Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode23MatVecRange0) panel9Mode23MatVecRange32) panel9Mode23MatVecRange64) panel9Mode23MatVecRange96) panel9Mode23MatVecRange128) row

theorem panel9Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode24MatVecRange0) panel9Mode24MatVecRange32) panel9Mode24MatVecRange64) panel9Mode24MatVecRange96) panel9Mode24MatVecRange128) row

theorem panel9Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode25MatVecRange0) panel9Mode25MatVecRange32) panel9Mode25MatVecRange64) panel9Mode25MatVecRange96) panel9Mode25MatVecRange128) row

theorem panel9Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode26MatVecRange0) panel9Mode26MatVecRange32) panel9Mode26MatVecRange64) panel9Mode26MatVecRange96) panel9Mode26MatVecRange128) row

theorem panel9Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode27MatVecRange0) panel9Mode27MatVecRange32) panel9Mode27MatVecRange64) panel9Mode27MatVecRange96) panel9Mode27MatVecRange128) row

theorem panel9Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode28MatVecRange0) panel9Mode28MatVecRange32) panel9Mode28MatVecRange64) panel9Mode28MatVecRange96) panel9Mode28MatVecRange128) row

theorem panel9Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode29MatVecRange0) panel9Mode29MatVecRange32) panel9Mode29MatVecRange64) panel9Mode29MatVecRange96) panel9Mode29MatVecRange128) row

theorem panel9Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode30MatVecRange0) panel9Mode30MatVecRange32) panel9Mode30MatVecRange64) panel9Mode30MatVecRange96) panel9Mode30MatVecRange128) row

theorem panel9Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode31MatVecRange0) panel9Mode31MatVecRange32) panel9Mode31MatVecRange64) panel9Mode31MatVecRange96) panel9Mode31MatVecRange128) row

theorem panel9Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode32MatVecRange0) panel9Mode32MatVecRange32) panel9Mode32MatVecRange64) panel9Mode32MatVecRange96) panel9Mode32MatVecRange128) row

theorem panel9Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode33MatVecRange0) panel9Mode33MatVecRange32) panel9Mode33MatVecRange64) panel9Mode33MatVecRange96) panel9Mode33MatVecRange128) row

theorem panel9Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode34MatVecRange0) panel9Mode34MatVecRange32) panel9Mode34MatVecRange64) panel9Mode34MatVecRange96) panel9Mode34MatVecRange128) row

theorem panel9Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode35MatVecRange0) panel9Mode35MatVecRange32) panel9Mode35MatVecRange64) panel9Mode35MatVecRange96) panel9Mode35MatVecRange128) row

theorem panel9Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode36MatVecRange0) panel9Mode36MatVecRange32) panel9Mode36MatVecRange64) panel9Mode36MatVecRange96) panel9Mode36MatVecRange128) row

theorem panel9Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode37MatVecRange0) panel9Mode37MatVecRange32) panel9Mode37MatVecRange64) panel9Mode37MatVecRange96) panel9Mode37MatVecRange128) row

theorem panel9Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode38MatVecRange0) panel9Mode38MatVecRange32) panel9Mode38MatVecRange64) panel9Mode38MatVecRange96) panel9Mode38MatVecRange128) row

theorem panel9Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode39MatVecRange0) panel9Mode39MatVecRange32) panel9Mode39MatVecRange64) panel9Mode39MatVecRange96) panel9Mode39MatVecRange128) row

theorem panel9Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode40MatVecRange0) panel9Mode40MatVecRange32) panel9Mode40MatVecRange64) panel9Mode40MatVecRange96) panel9Mode40MatVecRange128) row

theorem panel9Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode41MatVecRange0) panel9Mode41MatVecRange32) panel9Mode41MatVecRange64) panel9Mode41MatVecRange96) panel9Mode41MatVecRange128) row

theorem panel9Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode42MatVecRange0) panel9Mode42MatVecRange32) panel9Mode42MatVecRange64) panel9Mode42MatVecRange96) panel9Mode42MatVecRange128) row

theorem panel9Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode43MatVecRange0) panel9Mode43MatVecRange32) panel9Mode43MatVecRange64) panel9Mode43MatVecRange96) panel9Mode43MatVecRange128) row

theorem panel9Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode44MatVecRange0) panel9Mode44MatVecRange32) panel9Mode44MatVecRange64) panel9Mode44MatVecRange96) panel9Mode44MatVecRange128) row

theorem panel9Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode45MatVecRange0) panel9Mode45MatVecRange32) panel9Mode45MatVecRange64) panel9Mode45MatVecRange96) panel9Mode45MatVecRange128) row

theorem panel9Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode46MatVecRange0) panel9Mode46MatVecRange32) panel9Mode46MatVecRange64) panel9Mode46MatVecRange96) panel9Mode46MatVecRange128) row

theorem panel9Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel9MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel9MomentData.moments
        (P2RoundedFactorCheckpointData.panel9FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel9Mode47MatVecRange0) panel9Mode47MatVecRange32) panel9Mode47MatVecRange64) panel9Mode47MatVecRange96) panel9Mode47MatVecRange128) row

theorem panel9MomentData_correct :
    P2RoundedFactorCheckpointData.panel9MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel9FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel9DefectMoments_eq panel9ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel9Mode0MatVec_eq
      · exact panel9Mode2MatVec_eq
      · exact panel9Mode4MatVec_eq
      · exact panel9Mode6MatVec_eq
      · exact panel9Mode8MatVec_eq
      · exact panel9Mode10MatVec_eq
      · exact panel9Mode12MatVec_eq
      · exact panel9Mode14MatVec_eq
      · exact panel9Mode16MatVec_eq
      · exact panel9Mode18MatVec_eq
      · exact panel9Mode20MatVec_eq
      · exact panel9Mode22MatVec_eq
      · exact panel9Mode24MatVec_eq
      · exact panel9Mode26MatVec_eq
      · exact panel9Mode28MatVec_eq
      · exact panel9Mode30MatVec_eq
      · exact panel9Mode32MatVec_eq
      · exact panel9Mode34MatVec_eq
      · exact panel9Mode36MatVec_eq
      · exact panel9Mode38MatVec_eq
      · exact panel9Mode40MatVec_eq
      · exact panel9Mode42MatVec_eq
      · exact panel9Mode44MatVec_eq
      · exact panel9Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel9Mode1MatVec_eq
      · exact panel9Mode3MatVec_eq
      · exact panel9Mode5MatVec_eq
      · exact panel9Mode7MatVec_eq
      · exact panel9Mode9MatVec_eq
      · exact panel9Mode11MatVec_eq
      · exact panel9Mode13MatVec_eq
      · exact panel9Mode15MatVec_eq
      · exact panel9Mode17MatVec_eq
      · exact panel9Mode19MatVec_eq
      · exact panel9Mode21MatVec_eq
      · exact panel9Mode23MatVec_eq
      · exact panel9Mode25MatVec_eq
      · exact panel9Mode27MatVec_eq
      · exact panel9Mode29MatVec_eq
      · exact panel9Mode31MatVec_eq
      · exact panel9Mode33MatVec_eq
      · exact panel9Mode35MatVec_eq
      · exact panel9Mode37MatVec_eq
      · exact panel9Mode39MatVec_eq
      · exact panel9Mode41MatVec_eq
      · exact panel9Mode43MatVec_eq
      · exact panel9Mode45MatVec_eq
      · exact panel9Mode47MatVec_eq

end RHP2Bridge
