import RHBridge.P2RoundedFlatFactorCheckpoint6
import RHBridge.P2RoundedMomentLengths6
import RHBridge.P2RoundedMomentCheckpointCheck6_moments
import RHBridge.P2RoundedMomentCheckpointCheck6_mode0
import RHBridge.P2RoundedMomentCheckpointCheck6_mode1
import RHBridge.P2RoundedMomentCheckpointCheck6_mode2
import RHBridge.P2RoundedMomentCheckpointCheck6_mode3
import RHBridge.P2RoundedMomentCheckpointCheck6_mode4
import RHBridge.P2RoundedMomentCheckpointCheck6_mode5
import RHBridge.P2RoundedMomentCheckpointCheck6_mode6
import RHBridge.P2RoundedMomentCheckpointCheck6_mode7
import RHBridge.P2RoundedMomentCheckpointCheck6_mode8
import RHBridge.P2RoundedMomentCheckpointCheck6_mode9
import RHBridge.P2RoundedMomentCheckpointCheck6_mode10
import RHBridge.P2RoundedMomentCheckpointCheck6_mode11
import RHBridge.P2RoundedMomentCheckpointCheck6_mode12
import RHBridge.P2RoundedMomentCheckpointCheck6_mode13
import RHBridge.P2RoundedMomentCheckpointCheck6_mode14
import RHBridge.P2RoundedMomentCheckpointCheck6_mode15
import RHBridge.P2RoundedMomentCheckpointCheck6_mode16
import RHBridge.P2RoundedMomentCheckpointCheck6_mode17
import RHBridge.P2RoundedMomentCheckpointCheck6_mode18
import RHBridge.P2RoundedMomentCheckpointCheck6_mode19
import RHBridge.P2RoundedMomentCheckpointCheck6_mode20
import RHBridge.P2RoundedMomentCheckpointCheck6_mode21
import RHBridge.P2RoundedMomentCheckpointCheck6_mode22
import RHBridge.P2RoundedMomentCheckpointCheck6_mode23
import RHBridge.P2RoundedMomentCheckpointCheck6_mode24
import RHBridge.P2RoundedMomentCheckpointCheck6_mode25
import RHBridge.P2RoundedMomentCheckpointCheck6_mode26
import RHBridge.P2RoundedMomentCheckpointCheck6_mode27
import RHBridge.P2RoundedMomentCheckpointCheck6_mode28
import RHBridge.P2RoundedMomentCheckpointCheck6_mode29
import RHBridge.P2RoundedMomentCheckpointCheck6_mode30
import RHBridge.P2RoundedMomentCheckpointCheck6_mode31
import RHBridge.P2RoundedMomentCheckpointCheck6_mode32
import RHBridge.P2RoundedMomentCheckpointCheck6_mode33
import RHBridge.P2RoundedMomentCheckpointCheck6_mode34
import RHBridge.P2RoundedMomentCheckpointCheck6_mode35
import RHBridge.P2RoundedMomentCheckpointCheck6_mode36
import RHBridge.P2RoundedMomentCheckpointCheck6_mode37
import RHBridge.P2RoundedMomentCheckpointCheck6_mode38
import RHBridge.P2RoundedMomentCheckpointCheck6_mode39
import RHBridge.P2RoundedMomentCheckpointCheck6_mode40
import RHBridge.P2RoundedMomentCheckpointCheck6_mode41
import RHBridge.P2RoundedMomentCheckpointCheck6_mode42
import RHBridge.P2RoundedMomentCheckpointCheck6_mode43
import RHBridge.P2RoundedMomentCheckpointCheck6_mode44
import RHBridge.P2RoundedMomentCheckpointCheck6_mode45
import RHBridge.P2RoundedMomentCheckpointCheck6_mode46
import RHBridge.P2RoundedMomentCheckpointCheck6_mode47

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

theorem panel6DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel6FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6DefectMomentRange0) panel6DefectMomentRange64) panel6DefectMomentRange128) panel6DefectMomentRange192) panel6DefectMomentRange256) row

theorem panel6Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode0MatVecRange0) panel6Mode0MatVecRange32) panel6Mode0MatVecRange64) panel6Mode0MatVecRange96) panel6Mode0MatVecRange128) row

theorem panel6Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode1MatVecRange0) panel6Mode1MatVecRange32) panel6Mode1MatVecRange64) panel6Mode1MatVecRange96) panel6Mode1MatVecRange128) row

theorem panel6Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode2MatVecRange0) panel6Mode2MatVecRange32) panel6Mode2MatVecRange64) panel6Mode2MatVecRange96) panel6Mode2MatVecRange128) row

theorem panel6Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode3MatVecRange0) panel6Mode3MatVecRange32) panel6Mode3MatVecRange64) panel6Mode3MatVecRange96) panel6Mode3MatVecRange128) row

theorem panel6Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode4MatVecRange0) panel6Mode4MatVecRange32) panel6Mode4MatVecRange64) panel6Mode4MatVecRange96) panel6Mode4MatVecRange128) row

theorem panel6Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode5MatVecRange0) panel6Mode5MatVecRange32) panel6Mode5MatVecRange64) panel6Mode5MatVecRange96) panel6Mode5MatVecRange128) row

theorem panel6Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode6MatVecRange0) panel6Mode6MatVecRange32) panel6Mode6MatVecRange64) panel6Mode6MatVecRange96) panel6Mode6MatVecRange128) row

theorem panel6Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode7MatVecRange0) panel6Mode7MatVecRange32) panel6Mode7MatVecRange64) panel6Mode7MatVecRange96) panel6Mode7MatVecRange128) row

theorem panel6Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode8MatVecRange0) panel6Mode8MatVecRange32) panel6Mode8MatVecRange64) panel6Mode8MatVecRange96) panel6Mode8MatVecRange128) row

theorem panel6Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode9MatVecRange0) panel6Mode9MatVecRange32) panel6Mode9MatVecRange64) panel6Mode9MatVecRange96) panel6Mode9MatVecRange128) row

theorem panel6Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode10MatVecRange0) panel6Mode10MatVecRange32) panel6Mode10MatVecRange64) panel6Mode10MatVecRange96) panel6Mode10MatVecRange128) row

theorem panel6Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode11MatVecRange0) panel6Mode11MatVecRange32) panel6Mode11MatVecRange64) panel6Mode11MatVecRange96) panel6Mode11MatVecRange128) row

theorem panel6Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode12MatVecRange0) panel6Mode12MatVecRange32) panel6Mode12MatVecRange64) panel6Mode12MatVecRange96) panel6Mode12MatVecRange128) row

theorem panel6Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode13MatVecRange0) panel6Mode13MatVecRange32) panel6Mode13MatVecRange64) panel6Mode13MatVecRange96) panel6Mode13MatVecRange128) row

theorem panel6Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode14MatVecRange0) panel6Mode14MatVecRange32) panel6Mode14MatVecRange64) panel6Mode14MatVecRange96) panel6Mode14MatVecRange128) row

theorem panel6Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode15MatVecRange0) panel6Mode15MatVecRange32) panel6Mode15MatVecRange64) panel6Mode15MatVecRange96) panel6Mode15MatVecRange128) row

theorem panel6Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode16MatVecRange0) panel6Mode16MatVecRange32) panel6Mode16MatVecRange64) panel6Mode16MatVecRange96) panel6Mode16MatVecRange128) row

theorem panel6Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode17MatVecRange0) panel6Mode17MatVecRange32) panel6Mode17MatVecRange64) panel6Mode17MatVecRange96) panel6Mode17MatVecRange128) row

theorem panel6Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode18MatVecRange0) panel6Mode18MatVecRange32) panel6Mode18MatVecRange64) panel6Mode18MatVecRange96) panel6Mode18MatVecRange128) row

theorem panel6Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode19MatVecRange0) panel6Mode19MatVecRange32) panel6Mode19MatVecRange64) panel6Mode19MatVecRange96) panel6Mode19MatVecRange128) row

theorem panel6Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode20MatVecRange0) panel6Mode20MatVecRange32) panel6Mode20MatVecRange64) panel6Mode20MatVecRange96) panel6Mode20MatVecRange128) row

theorem panel6Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode21MatVecRange0) panel6Mode21MatVecRange32) panel6Mode21MatVecRange64) panel6Mode21MatVecRange96) panel6Mode21MatVecRange128) row

theorem panel6Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode22MatVecRange0) panel6Mode22MatVecRange32) panel6Mode22MatVecRange64) panel6Mode22MatVecRange96) panel6Mode22MatVecRange128) row

theorem panel6Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode23MatVecRange0) panel6Mode23MatVecRange32) panel6Mode23MatVecRange64) panel6Mode23MatVecRange96) panel6Mode23MatVecRange128) row

theorem panel6Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode24MatVecRange0) panel6Mode24MatVecRange32) panel6Mode24MatVecRange64) panel6Mode24MatVecRange96) panel6Mode24MatVecRange128) row

theorem panel6Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode25MatVecRange0) panel6Mode25MatVecRange32) panel6Mode25MatVecRange64) panel6Mode25MatVecRange96) panel6Mode25MatVecRange128) row

theorem panel6Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode26MatVecRange0) panel6Mode26MatVecRange32) panel6Mode26MatVecRange64) panel6Mode26MatVecRange96) panel6Mode26MatVecRange128) row

theorem panel6Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode27MatVecRange0) panel6Mode27MatVecRange32) panel6Mode27MatVecRange64) panel6Mode27MatVecRange96) panel6Mode27MatVecRange128) row

theorem panel6Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode28MatVecRange0) panel6Mode28MatVecRange32) panel6Mode28MatVecRange64) panel6Mode28MatVecRange96) panel6Mode28MatVecRange128) row

theorem panel6Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode29MatVecRange0) panel6Mode29MatVecRange32) panel6Mode29MatVecRange64) panel6Mode29MatVecRange96) panel6Mode29MatVecRange128) row

theorem panel6Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode30MatVecRange0) panel6Mode30MatVecRange32) panel6Mode30MatVecRange64) panel6Mode30MatVecRange96) panel6Mode30MatVecRange128) row

theorem panel6Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode31MatVecRange0) panel6Mode31MatVecRange32) panel6Mode31MatVecRange64) panel6Mode31MatVecRange96) panel6Mode31MatVecRange128) row

theorem panel6Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode32MatVecRange0) panel6Mode32MatVecRange32) panel6Mode32MatVecRange64) panel6Mode32MatVecRange96) panel6Mode32MatVecRange128) row

theorem panel6Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode33MatVecRange0) panel6Mode33MatVecRange32) panel6Mode33MatVecRange64) panel6Mode33MatVecRange96) panel6Mode33MatVecRange128) row

theorem panel6Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode34MatVecRange0) panel6Mode34MatVecRange32) panel6Mode34MatVecRange64) panel6Mode34MatVecRange96) panel6Mode34MatVecRange128) row

theorem panel6Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode35MatVecRange0) panel6Mode35MatVecRange32) panel6Mode35MatVecRange64) panel6Mode35MatVecRange96) panel6Mode35MatVecRange128) row

theorem panel6Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode36MatVecRange0) panel6Mode36MatVecRange32) panel6Mode36MatVecRange64) panel6Mode36MatVecRange96) panel6Mode36MatVecRange128) row

theorem panel6Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode37MatVecRange0) panel6Mode37MatVecRange32) panel6Mode37MatVecRange64) panel6Mode37MatVecRange96) panel6Mode37MatVecRange128) row

theorem panel6Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode38MatVecRange0) panel6Mode38MatVecRange32) panel6Mode38MatVecRange64) panel6Mode38MatVecRange96) panel6Mode38MatVecRange128) row

theorem panel6Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode39MatVecRange0) panel6Mode39MatVecRange32) panel6Mode39MatVecRange64) panel6Mode39MatVecRange96) panel6Mode39MatVecRange128) row

theorem panel6Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode40MatVecRange0) panel6Mode40MatVecRange32) panel6Mode40MatVecRange64) panel6Mode40MatVecRange96) panel6Mode40MatVecRange128) row

theorem panel6Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode41MatVecRange0) panel6Mode41MatVecRange32) panel6Mode41MatVecRange64) panel6Mode41MatVecRange96) panel6Mode41MatVecRange128) row

theorem panel6Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode42MatVecRange0) panel6Mode42MatVecRange32) panel6Mode42MatVecRange64) panel6Mode42MatVecRange96) panel6Mode42MatVecRange128) row

theorem panel6Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode43MatVecRange0) panel6Mode43MatVecRange32) panel6Mode43MatVecRange64) panel6Mode43MatVecRange96) panel6Mode43MatVecRange128) row

theorem panel6Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode44MatVecRange0) panel6Mode44MatVecRange32) panel6Mode44MatVecRange64) panel6Mode44MatVecRange96) panel6Mode44MatVecRange128) row

theorem panel6Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode45MatVecRange0) panel6Mode45MatVecRange32) panel6Mode45MatVecRange64) panel6Mode45MatVecRange96) panel6Mode45MatVecRange128) row

theorem panel6Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode46MatVecRange0) panel6Mode46MatVecRange32) panel6Mode46MatVecRange64) panel6Mode46MatVecRange96) panel6Mode46MatVecRange128) row

theorem panel6Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel6MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel6MomentData.moments
        (P2RoundedFactorCheckpointData.panel6FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel6Mode47MatVecRange0) panel6Mode47MatVecRange32) panel6Mode47MatVecRange64) panel6Mode47MatVecRange96) panel6Mode47MatVecRange128) row

theorem panel6MomentData_correct :
    P2RoundedFactorCheckpointData.panel6MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel6FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel6DefectMoments_eq panel6ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel6Mode0MatVec_eq
      · exact panel6Mode2MatVec_eq
      · exact panel6Mode4MatVec_eq
      · exact panel6Mode6MatVec_eq
      · exact panel6Mode8MatVec_eq
      · exact panel6Mode10MatVec_eq
      · exact panel6Mode12MatVec_eq
      · exact panel6Mode14MatVec_eq
      · exact panel6Mode16MatVec_eq
      · exact panel6Mode18MatVec_eq
      · exact panel6Mode20MatVec_eq
      · exact panel6Mode22MatVec_eq
      · exact panel6Mode24MatVec_eq
      · exact panel6Mode26MatVec_eq
      · exact panel6Mode28MatVec_eq
      · exact panel6Mode30MatVec_eq
      · exact panel6Mode32MatVec_eq
      · exact panel6Mode34MatVec_eq
      · exact panel6Mode36MatVec_eq
      · exact panel6Mode38MatVec_eq
      · exact panel6Mode40MatVec_eq
      · exact panel6Mode42MatVec_eq
      · exact panel6Mode44MatVec_eq
      · exact panel6Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel6Mode1MatVec_eq
      · exact panel6Mode3MatVec_eq
      · exact panel6Mode5MatVec_eq
      · exact panel6Mode7MatVec_eq
      · exact panel6Mode9MatVec_eq
      · exact panel6Mode11MatVec_eq
      · exact panel6Mode13MatVec_eq
      · exact panel6Mode15MatVec_eq
      · exact panel6Mode17MatVec_eq
      · exact panel6Mode19MatVec_eq
      · exact panel6Mode21MatVec_eq
      · exact panel6Mode23MatVec_eq
      · exact panel6Mode25MatVec_eq
      · exact panel6Mode27MatVec_eq
      · exact panel6Mode29MatVec_eq
      · exact panel6Mode31MatVec_eq
      · exact panel6Mode33MatVec_eq
      · exact panel6Mode35MatVec_eq
      · exact panel6Mode37MatVec_eq
      · exact panel6Mode39MatVec_eq
      · exact panel6Mode41MatVec_eq
      · exact panel6Mode43MatVec_eq
      · exact panel6Mode45MatVec_eq
      · exact panel6Mode47MatVec_eq

end RHP2Bridge
