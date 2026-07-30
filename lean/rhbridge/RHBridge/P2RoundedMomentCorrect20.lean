import RHBridge.P2RoundedFlatFactorCheckpoint20
import RHBridge.P2RoundedMomentLengths20
import RHBridge.P2RoundedMomentCheckpointCheck20_moments
import RHBridge.P2RoundedMomentCheckpointCheck20_mode0
import RHBridge.P2RoundedMomentCheckpointCheck20_mode1
import RHBridge.P2RoundedMomentCheckpointCheck20_mode2
import RHBridge.P2RoundedMomentCheckpointCheck20_mode3
import RHBridge.P2RoundedMomentCheckpointCheck20_mode4
import RHBridge.P2RoundedMomentCheckpointCheck20_mode5
import RHBridge.P2RoundedMomentCheckpointCheck20_mode6
import RHBridge.P2RoundedMomentCheckpointCheck20_mode7
import RHBridge.P2RoundedMomentCheckpointCheck20_mode8
import RHBridge.P2RoundedMomentCheckpointCheck20_mode9
import RHBridge.P2RoundedMomentCheckpointCheck20_mode10
import RHBridge.P2RoundedMomentCheckpointCheck20_mode11
import RHBridge.P2RoundedMomentCheckpointCheck20_mode12
import RHBridge.P2RoundedMomentCheckpointCheck20_mode13
import RHBridge.P2RoundedMomentCheckpointCheck20_mode14
import RHBridge.P2RoundedMomentCheckpointCheck20_mode15
import RHBridge.P2RoundedMomentCheckpointCheck20_mode16
import RHBridge.P2RoundedMomentCheckpointCheck20_mode17
import RHBridge.P2RoundedMomentCheckpointCheck20_mode18
import RHBridge.P2RoundedMomentCheckpointCheck20_mode19
import RHBridge.P2RoundedMomentCheckpointCheck20_mode20
import RHBridge.P2RoundedMomentCheckpointCheck20_mode21
import RHBridge.P2RoundedMomentCheckpointCheck20_mode22
import RHBridge.P2RoundedMomentCheckpointCheck20_mode23
import RHBridge.P2RoundedMomentCheckpointCheck20_mode24
import RHBridge.P2RoundedMomentCheckpointCheck20_mode25
import RHBridge.P2RoundedMomentCheckpointCheck20_mode26
import RHBridge.P2RoundedMomentCheckpointCheck20_mode27
import RHBridge.P2RoundedMomentCheckpointCheck20_mode28
import RHBridge.P2RoundedMomentCheckpointCheck20_mode29
import RHBridge.P2RoundedMomentCheckpointCheck20_mode30
import RHBridge.P2RoundedMomentCheckpointCheck20_mode31
import RHBridge.P2RoundedMomentCheckpointCheck20_mode32
import RHBridge.P2RoundedMomentCheckpointCheck20_mode33
import RHBridge.P2RoundedMomentCheckpointCheck20_mode34
import RHBridge.P2RoundedMomentCheckpointCheck20_mode35
import RHBridge.P2RoundedMomentCheckpointCheck20_mode36
import RHBridge.P2RoundedMomentCheckpointCheck20_mode37
import RHBridge.P2RoundedMomentCheckpointCheck20_mode38
import RHBridge.P2RoundedMomentCheckpointCheck20_mode39
import RHBridge.P2RoundedMomentCheckpointCheck20_mode40
import RHBridge.P2RoundedMomentCheckpointCheck20_mode41
import RHBridge.P2RoundedMomentCheckpointCheck20_mode42
import RHBridge.P2RoundedMomentCheckpointCheck20_mode43
import RHBridge.P2RoundedMomentCheckpointCheck20_mode44
import RHBridge.P2RoundedMomentCheckpointCheck20_mode45
import RHBridge.P2RoundedMomentCheckpointCheck20_mode46
import RHBridge.P2RoundedMomentCheckpointCheck20_mode47

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

theorem panel20DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel20FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20DefectMomentRange0) panel20DefectMomentRange64) panel20DefectMomentRange128) panel20DefectMomentRange192) panel20DefectMomentRange256) row

theorem panel20Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode0MatVecRange0) panel20Mode0MatVecRange32) panel20Mode0MatVecRange64) panel20Mode0MatVecRange96) panel20Mode0MatVecRange128) row

theorem panel20Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode1MatVecRange0) panel20Mode1MatVecRange32) panel20Mode1MatVecRange64) panel20Mode1MatVecRange96) panel20Mode1MatVecRange128) row

theorem panel20Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode2MatVecRange0) panel20Mode2MatVecRange32) panel20Mode2MatVecRange64) panel20Mode2MatVecRange96) panel20Mode2MatVecRange128) row

theorem panel20Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode3MatVecRange0) panel20Mode3MatVecRange32) panel20Mode3MatVecRange64) panel20Mode3MatVecRange96) panel20Mode3MatVecRange128) row

theorem panel20Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode4MatVecRange0) panel20Mode4MatVecRange32) panel20Mode4MatVecRange64) panel20Mode4MatVecRange96) panel20Mode4MatVecRange128) row

theorem panel20Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode5MatVecRange0) panel20Mode5MatVecRange32) panel20Mode5MatVecRange64) panel20Mode5MatVecRange96) panel20Mode5MatVecRange128) row

theorem panel20Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode6MatVecRange0) panel20Mode6MatVecRange32) panel20Mode6MatVecRange64) panel20Mode6MatVecRange96) panel20Mode6MatVecRange128) row

theorem panel20Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode7MatVecRange0) panel20Mode7MatVecRange32) panel20Mode7MatVecRange64) panel20Mode7MatVecRange96) panel20Mode7MatVecRange128) row

theorem panel20Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode8MatVecRange0) panel20Mode8MatVecRange32) panel20Mode8MatVecRange64) panel20Mode8MatVecRange96) panel20Mode8MatVecRange128) row

theorem panel20Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode9MatVecRange0) panel20Mode9MatVecRange32) panel20Mode9MatVecRange64) panel20Mode9MatVecRange96) panel20Mode9MatVecRange128) row

theorem panel20Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode10MatVecRange0) panel20Mode10MatVecRange32) panel20Mode10MatVecRange64) panel20Mode10MatVecRange96) panel20Mode10MatVecRange128) row

theorem panel20Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode11MatVecRange0) panel20Mode11MatVecRange32) panel20Mode11MatVecRange64) panel20Mode11MatVecRange96) panel20Mode11MatVecRange128) row

theorem panel20Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode12MatVecRange0) panel20Mode12MatVecRange32) panel20Mode12MatVecRange64) panel20Mode12MatVecRange96) panel20Mode12MatVecRange128) row

theorem panel20Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode13MatVecRange0) panel20Mode13MatVecRange32) panel20Mode13MatVecRange64) panel20Mode13MatVecRange96) panel20Mode13MatVecRange128) row

theorem panel20Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode14MatVecRange0) panel20Mode14MatVecRange32) panel20Mode14MatVecRange64) panel20Mode14MatVecRange96) panel20Mode14MatVecRange128) row

theorem panel20Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode15MatVecRange0) panel20Mode15MatVecRange32) panel20Mode15MatVecRange64) panel20Mode15MatVecRange96) panel20Mode15MatVecRange128) row

theorem panel20Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode16MatVecRange0) panel20Mode16MatVecRange32) panel20Mode16MatVecRange64) panel20Mode16MatVecRange96) panel20Mode16MatVecRange128) row

theorem panel20Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode17MatVecRange0) panel20Mode17MatVecRange32) panel20Mode17MatVecRange64) panel20Mode17MatVecRange96) panel20Mode17MatVecRange128) row

theorem panel20Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode18MatVecRange0) panel20Mode18MatVecRange32) panel20Mode18MatVecRange64) panel20Mode18MatVecRange96) panel20Mode18MatVecRange128) row

theorem panel20Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode19MatVecRange0) panel20Mode19MatVecRange32) panel20Mode19MatVecRange64) panel20Mode19MatVecRange96) panel20Mode19MatVecRange128) row

theorem panel20Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode20MatVecRange0) panel20Mode20MatVecRange32) panel20Mode20MatVecRange64) panel20Mode20MatVecRange96) panel20Mode20MatVecRange128) row

theorem panel20Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode21MatVecRange0) panel20Mode21MatVecRange32) panel20Mode21MatVecRange64) panel20Mode21MatVecRange96) panel20Mode21MatVecRange128) row

theorem panel20Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode22MatVecRange0) panel20Mode22MatVecRange32) panel20Mode22MatVecRange64) panel20Mode22MatVecRange96) panel20Mode22MatVecRange128) row

theorem panel20Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode23MatVecRange0) panel20Mode23MatVecRange32) panel20Mode23MatVecRange64) panel20Mode23MatVecRange96) panel20Mode23MatVecRange128) row

theorem panel20Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode24MatVecRange0) panel20Mode24MatVecRange32) panel20Mode24MatVecRange64) panel20Mode24MatVecRange96) panel20Mode24MatVecRange128) row

theorem panel20Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode25MatVecRange0) panel20Mode25MatVecRange32) panel20Mode25MatVecRange64) panel20Mode25MatVecRange96) panel20Mode25MatVecRange128) row

theorem panel20Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode26MatVecRange0) panel20Mode26MatVecRange32) panel20Mode26MatVecRange64) panel20Mode26MatVecRange96) panel20Mode26MatVecRange128) row

theorem panel20Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode27MatVecRange0) panel20Mode27MatVecRange32) panel20Mode27MatVecRange64) panel20Mode27MatVecRange96) panel20Mode27MatVecRange128) row

theorem panel20Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode28MatVecRange0) panel20Mode28MatVecRange32) panel20Mode28MatVecRange64) panel20Mode28MatVecRange96) panel20Mode28MatVecRange128) row

theorem panel20Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode29MatVecRange0) panel20Mode29MatVecRange32) panel20Mode29MatVecRange64) panel20Mode29MatVecRange96) panel20Mode29MatVecRange128) row

theorem panel20Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode30MatVecRange0) panel20Mode30MatVecRange32) panel20Mode30MatVecRange64) panel20Mode30MatVecRange96) panel20Mode30MatVecRange128) row

theorem panel20Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode31MatVecRange0) panel20Mode31MatVecRange32) panel20Mode31MatVecRange64) panel20Mode31MatVecRange96) panel20Mode31MatVecRange128) row

theorem panel20Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode32MatVecRange0) panel20Mode32MatVecRange32) panel20Mode32MatVecRange64) panel20Mode32MatVecRange96) panel20Mode32MatVecRange128) row

theorem panel20Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode33MatVecRange0) panel20Mode33MatVecRange32) panel20Mode33MatVecRange64) panel20Mode33MatVecRange96) panel20Mode33MatVecRange128) row

theorem panel20Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode34MatVecRange0) panel20Mode34MatVecRange32) panel20Mode34MatVecRange64) panel20Mode34MatVecRange96) panel20Mode34MatVecRange128) row

theorem panel20Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode35MatVecRange0) panel20Mode35MatVecRange32) panel20Mode35MatVecRange64) panel20Mode35MatVecRange96) panel20Mode35MatVecRange128) row

theorem panel20Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode36MatVecRange0) panel20Mode36MatVecRange32) panel20Mode36MatVecRange64) panel20Mode36MatVecRange96) panel20Mode36MatVecRange128) row

theorem panel20Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode37MatVecRange0) panel20Mode37MatVecRange32) panel20Mode37MatVecRange64) panel20Mode37MatVecRange96) panel20Mode37MatVecRange128) row

theorem panel20Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode38MatVecRange0) panel20Mode38MatVecRange32) panel20Mode38MatVecRange64) panel20Mode38MatVecRange96) panel20Mode38MatVecRange128) row

theorem panel20Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode39MatVecRange0) panel20Mode39MatVecRange32) panel20Mode39MatVecRange64) panel20Mode39MatVecRange96) panel20Mode39MatVecRange128) row

theorem panel20Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode40MatVecRange0) panel20Mode40MatVecRange32) panel20Mode40MatVecRange64) panel20Mode40MatVecRange96) panel20Mode40MatVecRange128) row

theorem panel20Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode41MatVecRange0) panel20Mode41MatVecRange32) panel20Mode41MatVecRange64) panel20Mode41MatVecRange96) panel20Mode41MatVecRange128) row

theorem panel20Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode42MatVecRange0) panel20Mode42MatVecRange32) panel20Mode42MatVecRange64) panel20Mode42MatVecRange96) panel20Mode42MatVecRange128) row

theorem panel20Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode43MatVecRange0) panel20Mode43MatVecRange32) panel20Mode43MatVecRange64) panel20Mode43MatVecRange96) panel20Mode43MatVecRange128) row

theorem panel20Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode44MatVecRange0) panel20Mode44MatVecRange32) panel20Mode44MatVecRange64) panel20Mode44MatVecRange96) panel20Mode44MatVecRange128) row

theorem panel20Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode45MatVecRange0) panel20Mode45MatVecRange32) panel20Mode45MatVecRange64) panel20Mode45MatVecRange96) panel20Mode45MatVecRange128) row

theorem panel20Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode46MatVecRange0) panel20Mode46MatVecRange32) panel20Mode46MatVecRange64) panel20Mode46MatVecRange96) panel20Mode46MatVecRange128) row

theorem panel20Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel20MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel20MomentData.moments
        (P2RoundedFactorCheckpointData.panel20FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel20Mode47MatVecRange0) panel20Mode47MatVecRange32) panel20Mode47MatVecRange64) panel20Mode47MatVecRange96) panel20Mode47MatVecRange128) row

theorem panel20MomentData_correct :
    P2RoundedFactorCheckpointData.panel20MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel20FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel20DefectMoments_eq panel20ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel20Mode0MatVec_eq
      · exact panel20Mode2MatVec_eq
      · exact panel20Mode4MatVec_eq
      · exact panel20Mode6MatVec_eq
      · exact panel20Mode8MatVec_eq
      · exact panel20Mode10MatVec_eq
      · exact panel20Mode12MatVec_eq
      · exact panel20Mode14MatVec_eq
      · exact panel20Mode16MatVec_eq
      · exact panel20Mode18MatVec_eq
      · exact panel20Mode20MatVec_eq
      · exact panel20Mode22MatVec_eq
      · exact panel20Mode24MatVec_eq
      · exact panel20Mode26MatVec_eq
      · exact panel20Mode28MatVec_eq
      · exact panel20Mode30MatVec_eq
      · exact panel20Mode32MatVec_eq
      · exact panel20Mode34MatVec_eq
      · exact panel20Mode36MatVec_eq
      · exact panel20Mode38MatVec_eq
      · exact panel20Mode40MatVec_eq
      · exact panel20Mode42MatVec_eq
      · exact panel20Mode44MatVec_eq
      · exact panel20Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel20Mode1MatVec_eq
      · exact panel20Mode3MatVec_eq
      · exact panel20Mode5MatVec_eq
      · exact panel20Mode7MatVec_eq
      · exact panel20Mode9MatVec_eq
      · exact panel20Mode11MatVec_eq
      · exact panel20Mode13MatVec_eq
      · exact panel20Mode15MatVec_eq
      · exact panel20Mode17MatVec_eq
      · exact panel20Mode19MatVec_eq
      · exact panel20Mode21MatVec_eq
      · exact panel20Mode23MatVec_eq
      · exact panel20Mode25MatVec_eq
      · exact panel20Mode27MatVec_eq
      · exact panel20Mode29MatVec_eq
      · exact panel20Mode31MatVec_eq
      · exact panel20Mode33MatVec_eq
      · exact panel20Mode35MatVec_eq
      · exact panel20Mode37MatVec_eq
      · exact panel20Mode39MatVec_eq
      · exact panel20Mode41MatVec_eq
      · exact panel20Mode43MatVec_eq
      · exact panel20Mode45MatVec_eq
      · exact panel20Mode47MatVec_eq

end RHP2Bridge
