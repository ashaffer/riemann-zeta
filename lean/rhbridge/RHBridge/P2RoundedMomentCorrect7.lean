import RHBridge.P2RoundedFlatFactorCheckpoint7
import RHBridge.P2RoundedMomentLengths7
import RHBridge.P2RoundedMomentCheckpointCheck7_moments
import RHBridge.P2RoundedMomentCheckpointCheck7_mode0
import RHBridge.P2RoundedMomentCheckpointCheck7_mode1
import RHBridge.P2RoundedMomentCheckpointCheck7_mode2
import RHBridge.P2RoundedMomentCheckpointCheck7_mode3
import RHBridge.P2RoundedMomentCheckpointCheck7_mode4
import RHBridge.P2RoundedMomentCheckpointCheck7_mode5
import RHBridge.P2RoundedMomentCheckpointCheck7_mode6
import RHBridge.P2RoundedMomentCheckpointCheck7_mode7
import RHBridge.P2RoundedMomentCheckpointCheck7_mode8
import RHBridge.P2RoundedMomentCheckpointCheck7_mode9
import RHBridge.P2RoundedMomentCheckpointCheck7_mode10
import RHBridge.P2RoundedMomentCheckpointCheck7_mode11
import RHBridge.P2RoundedMomentCheckpointCheck7_mode12
import RHBridge.P2RoundedMomentCheckpointCheck7_mode13
import RHBridge.P2RoundedMomentCheckpointCheck7_mode14
import RHBridge.P2RoundedMomentCheckpointCheck7_mode15
import RHBridge.P2RoundedMomentCheckpointCheck7_mode16
import RHBridge.P2RoundedMomentCheckpointCheck7_mode17
import RHBridge.P2RoundedMomentCheckpointCheck7_mode18
import RHBridge.P2RoundedMomentCheckpointCheck7_mode19
import RHBridge.P2RoundedMomentCheckpointCheck7_mode20
import RHBridge.P2RoundedMomentCheckpointCheck7_mode21
import RHBridge.P2RoundedMomentCheckpointCheck7_mode22
import RHBridge.P2RoundedMomentCheckpointCheck7_mode23
import RHBridge.P2RoundedMomentCheckpointCheck7_mode24
import RHBridge.P2RoundedMomentCheckpointCheck7_mode25
import RHBridge.P2RoundedMomentCheckpointCheck7_mode26
import RHBridge.P2RoundedMomentCheckpointCheck7_mode27
import RHBridge.P2RoundedMomentCheckpointCheck7_mode28
import RHBridge.P2RoundedMomentCheckpointCheck7_mode29
import RHBridge.P2RoundedMomentCheckpointCheck7_mode30
import RHBridge.P2RoundedMomentCheckpointCheck7_mode31
import RHBridge.P2RoundedMomentCheckpointCheck7_mode32
import RHBridge.P2RoundedMomentCheckpointCheck7_mode33
import RHBridge.P2RoundedMomentCheckpointCheck7_mode34
import RHBridge.P2RoundedMomentCheckpointCheck7_mode35
import RHBridge.P2RoundedMomentCheckpointCheck7_mode36
import RHBridge.P2RoundedMomentCheckpointCheck7_mode37
import RHBridge.P2RoundedMomentCheckpointCheck7_mode38
import RHBridge.P2RoundedMomentCheckpointCheck7_mode39
import RHBridge.P2RoundedMomentCheckpointCheck7_mode40
import RHBridge.P2RoundedMomentCheckpointCheck7_mode41
import RHBridge.P2RoundedMomentCheckpointCheck7_mode42
import RHBridge.P2RoundedMomentCheckpointCheck7_mode43
import RHBridge.P2RoundedMomentCheckpointCheck7_mode44
import RHBridge.P2RoundedMomentCheckpointCheck7_mode45
import RHBridge.P2RoundedMomentCheckpointCheck7_mode46
import RHBridge.P2RoundedMomentCheckpointCheck7_mode47

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

theorem panel7DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel7FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7DefectMomentRange0) panel7DefectMomentRange64) panel7DefectMomentRange128) panel7DefectMomentRange192) panel7DefectMomentRange256) row

theorem panel7Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode0MatVecRange0) panel7Mode0MatVecRange32) panel7Mode0MatVecRange64) panel7Mode0MatVecRange96) panel7Mode0MatVecRange128) row

theorem panel7Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode1MatVecRange0) panel7Mode1MatVecRange32) panel7Mode1MatVecRange64) panel7Mode1MatVecRange96) panel7Mode1MatVecRange128) row

theorem panel7Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode2MatVecRange0) panel7Mode2MatVecRange32) panel7Mode2MatVecRange64) panel7Mode2MatVecRange96) panel7Mode2MatVecRange128) row

theorem panel7Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode3MatVecRange0) panel7Mode3MatVecRange32) panel7Mode3MatVecRange64) panel7Mode3MatVecRange96) panel7Mode3MatVecRange128) row

theorem panel7Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode4MatVecRange0) panel7Mode4MatVecRange32) panel7Mode4MatVecRange64) panel7Mode4MatVecRange96) panel7Mode4MatVecRange128) row

theorem panel7Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode5MatVecRange0) panel7Mode5MatVecRange32) panel7Mode5MatVecRange64) panel7Mode5MatVecRange96) panel7Mode5MatVecRange128) row

theorem panel7Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode6MatVecRange0) panel7Mode6MatVecRange32) panel7Mode6MatVecRange64) panel7Mode6MatVecRange96) panel7Mode6MatVecRange128) row

theorem panel7Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode7MatVecRange0) panel7Mode7MatVecRange32) panel7Mode7MatVecRange64) panel7Mode7MatVecRange96) panel7Mode7MatVecRange128) row

theorem panel7Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode8MatVecRange0) panel7Mode8MatVecRange32) panel7Mode8MatVecRange64) panel7Mode8MatVecRange96) panel7Mode8MatVecRange128) row

theorem panel7Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode9MatVecRange0) panel7Mode9MatVecRange32) panel7Mode9MatVecRange64) panel7Mode9MatVecRange96) panel7Mode9MatVecRange128) row

theorem panel7Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode10MatVecRange0) panel7Mode10MatVecRange32) panel7Mode10MatVecRange64) panel7Mode10MatVecRange96) panel7Mode10MatVecRange128) row

theorem panel7Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode11MatVecRange0) panel7Mode11MatVecRange32) panel7Mode11MatVecRange64) panel7Mode11MatVecRange96) panel7Mode11MatVecRange128) row

theorem panel7Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode12MatVecRange0) panel7Mode12MatVecRange32) panel7Mode12MatVecRange64) panel7Mode12MatVecRange96) panel7Mode12MatVecRange128) row

theorem panel7Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode13MatVecRange0) panel7Mode13MatVecRange32) panel7Mode13MatVecRange64) panel7Mode13MatVecRange96) panel7Mode13MatVecRange128) row

theorem panel7Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode14MatVecRange0) panel7Mode14MatVecRange32) panel7Mode14MatVecRange64) panel7Mode14MatVecRange96) panel7Mode14MatVecRange128) row

theorem panel7Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode15MatVecRange0) panel7Mode15MatVecRange32) panel7Mode15MatVecRange64) panel7Mode15MatVecRange96) panel7Mode15MatVecRange128) row

theorem panel7Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode16MatVecRange0) panel7Mode16MatVecRange32) panel7Mode16MatVecRange64) panel7Mode16MatVecRange96) panel7Mode16MatVecRange128) row

theorem panel7Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode17MatVecRange0) panel7Mode17MatVecRange32) panel7Mode17MatVecRange64) panel7Mode17MatVecRange96) panel7Mode17MatVecRange128) row

theorem panel7Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode18MatVecRange0) panel7Mode18MatVecRange32) panel7Mode18MatVecRange64) panel7Mode18MatVecRange96) panel7Mode18MatVecRange128) row

theorem panel7Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode19MatVecRange0) panel7Mode19MatVecRange32) panel7Mode19MatVecRange64) panel7Mode19MatVecRange96) panel7Mode19MatVecRange128) row

theorem panel7Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode20MatVecRange0) panel7Mode20MatVecRange32) panel7Mode20MatVecRange64) panel7Mode20MatVecRange96) panel7Mode20MatVecRange128) row

theorem panel7Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode21MatVecRange0) panel7Mode21MatVecRange32) panel7Mode21MatVecRange64) panel7Mode21MatVecRange96) panel7Mode21MatVecRange128) row

theorem panel7Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode22MatVecRange0) panel7Mode22MatVecRange32) panel7Mode22MatVecRange64) panel7Mode22MatVecRange96) panel7Mode22MatVecRange128) row

theorem panel7Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode23MatVecRange0) panel7Mode23MatVecRange32) panel7Mode23MatVecRange64) panel7Mode23MatVecRange96) panel7Mode23MatVecRange128) row

theorem panel7Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode24MatVecRange0) panel7Mode24MatVecRange32) panel7Mode24MatVecRange64) panel7Mode24MatVecRange96) panel7Mode24MatVecRange128) row

theorem panel7Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode25MatVecRange0) panel7Mode25MatVecRange32) panel7Mode25MatVecRange64) panel7Mode25MatVecRange96) panel7Mode25MatVecRange128) row

theorem panel7Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode26MatVecRange0) panel7Mode26MatVecRange32) panel7Mode26MatVecRange64) panel7Mode26MatVecRange96) panel7Mode26MatVecRange128) row

theorem panel7Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode27MatVecRange0) panel7Mode27MatVecRange32) panel7Mode27MatVecRange64) panel7Mode27MatVecRange96) panel7Mode27MatVecRange128) row

theorem panel7Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode28MatVecRange0) panel7Mode28MatVecRange32) panel7Mode28MatVecRange64) panel7Mode28MatVecRange96) panel7Mode28MatVecRange128) row

theorem panel7Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode29MatVecRange0) panel7Mode29MatVecRange32) panel7Mode29MatVecRange64) panel7Mode29MatVecRange96) panel7Mode29MatVecRange128) row

theorem panel7Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode30MatVecRange0) panel7Mode30MatVecRange32) panel7Mode30MatVecRange64) panel7Mode30MatVecRange96) panel7Mode30MatVecRange128) row

theorem panel7Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode31MatVecRange0) panel7Mode31MatVecRange32) panel7Mode31MatVecRange64) panel7Mode31MatVecRange96) panel7Mode31MatVecRange128) row

theorem panel7Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode32MatVecRange0) panel7Mode32MatVecRange32) panel7Mode32MatVecRange64) panel7Mode32MatVecRange96) panel7Mode32MatVecRange128) row

theorem panel7Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode33MatVecRange0) panel7Mode33MatVecRange32) panel7Mode33MatVecRange64) panel7Mode33MatVecRange96) panel7Mode33MatVecRange128) row

theorem panel7Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode34MatVecRange0) panel7Mode34MatVecRange32) panel7Mode34MatVecRange64) panel7Mode34MatVecRange96) panel7Mode34MatVecRange128) row

theorem panel7Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode35MatVecRange0) panel7Mode35MatVecRange32) panel7Mode35MatVecRange64) panel7Mode35MatVecRange96) panel7Mode35MatVecRange128) row

theorem panel7Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode36MatVecRange0) panel7Mode36MatVecRange32) panel7Mode36MatVecRange64) panel7Mode36MatVecRange96) panel7Mode36MatVecRange128) row

theorem panel7Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode37MatVecRange0) panel7Mode37MatVecRange32) panel7Mode37MatVecRange64) panel7Mode37MatVecRange96) panel7Mode37MatVecRange128) row

theorem panel7Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode38MatVecRange0) panel7Mode38MatVecRange32) panel7Mode38MatVecRange64) panel7Mode38MatVecRange96) panel7Mode38MatVecRange128) row

theorem panel7Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode39MatVecRange0) panel7Mode39MatVecRange32) panel7Mode39MatVecRange64) panel7Mode39MatVecRange96) panel7Mode39MatVecRange128) row

theorem panel7Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode40MatVecRange0) panel7Mode40MatVecRange32) panel7Mode40MatVecRange64) panel7Mode40MatVecRange96) panel7Mode40MatVecRange128) row

theorem panel7Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode41MatVecRange0) panel7Mode41MatVecRange32) panel7Mode41MatVecRange64) panel7Mode41MatVecRange96) panel7Mode41MatVecRange128) row

theorem panel7Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode42MatVecRange0) panel7Mode42MatVecRange32) panel7Mode42MatVecRange64) panel7Mode42MatVecRange96) panel7Mode42MatVecRange128) row

theorem panel7Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode43MatVecRange0) panel7Mode43MatVecRange32) panel7Mode43MatVecRange64) panel7Mode43MatVecRange96) panel7Mode43MatVecRange128) row

theorem panel7Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode44MatVecRange0) panel7Mode44MatVecRange32) panel7Mode44MatVecRange64) panel7Mode44MatVecRange96) panel7Mode44MatVecRange128) row

theorem panel7Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode45MatVecRange0) panel7Mode45MatVecRange32) panel7Mode45MatVecRange64) panel7Mode45MatVecRange96) panel7Mode45MatVecRange128) row

theorem panel7Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode46MatVecRange0) panel7Mode46MatVecRange32) panel7Mode46MatVecRange64) panel7Mode46MatVecRange96) panel7Mode46MatVecRange128) row

theorem panel7Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel7MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel7MomentData.moments
        (P2RoundedFactorCheckpointData.panel7FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel7Mode47MatVecRange0) panel7Mode47MatVecRange32) panel7Mode47MatVecRange64) panel7Mode47MatVecRange96) panel7Mode47MatVecRange128) row

theorem panel7MomentData_correct :
    P2RoundedFactorCheckpointData.panel7MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel7FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel7DefectMoments_eq panel7ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel7Mode0MatVec_eq
      · exact panel7Mode2MatVec_eq
      · exact panel7Mode4MatVec_eq
      · exact panel7Mode6MatVec_eq
      · exact panel7Mode8MatVec_eq
      · exact panel7Mode10MatVec_eq
      · exact panel7Mode12MatVec_eq
      · exact panel7Mode14MatVec_eq
      · exact panel7Mode16MatVec_eq
      · exact panel7Mode18MatVec_eq
      · exact panel7Mode20MatVec_eq
      · exact panel7Mode22MatVec_eq
      · exact panel7Mode24MatVec_eq
      · exact panel7Mode26MatVec_eq
      · exact panel7Mode28MatVec_eq
      · exact panel7Mode30MatVec_eq
      · exact panel7Mode32MatVec_eq
      · exact panel7Mode34MatVec_eq
      · exact panel7Mode36MatVec_eq
      · exact panel7Mode38MatVec_eq
      · exact panel7Mode40MatVec_eq
      · exact panel7Mode42MatVec_eq
      · exact panel7Mode44MatVec_eq
      · exact panel7Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel7Mode1MatVec_eq
      · exact panel7Mode3MatVec_eq
      · exact panel7Mode5MatVec_eq
      · exact panel7Mode7MatVec_eq
      · exact panel7Mode9MatVec_eq
      · exact panel7Mode11MatVec_eq
      · exact panel7Mode13MatVec_eq
      · exact panel7Mode15MatVec_eq
      · exact panel7Mode17MatVec_eq
      · exact panel7Mode19MatVec_eq
      · exact panel7Mode21MatVec_eq
      · exact panel7Mode23MatVec_eq
      · exact panel7Mode25MatVec_eq
      · exact panel7Mode27MatVec_eq
      · exact panel7Mode29MatVec_eq
      · exact panel7Mode31MatVec_eq
      · exact panel7Mode33MatVec_eq
      · exact panel7Mode35MatVec_eq
      · exact panel7Mode37MatVec_eq
      · exact panel7Mode39MatVec_eq
      · exact panel7Mode41MatVec_eq
      · exact panel7Mode43MatVec_eq
      · exact panel7Mode45MatVec_eq
      · exact panel7Mode47MatVec_eq

end RHP2Bridge
